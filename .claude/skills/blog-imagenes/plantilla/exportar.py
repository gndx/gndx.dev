"""Revisa y exporta las imágenes de un post. Se ejecuta desde la raíz de gndx.dev:

  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug>                 → imagenes.py + check + capturas + hojas (no toca el blog)
  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --al-blog       → además, WebP en public/blog/<slug>/ y el Markdown de cada idioma
  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --publicar      → optimiza con TinyPNG, sube a S3 y muestra el Markdown
  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --destino DIR   → los WebP a otra carpeta (para probar sin tocar el blog)

<slug> es la carpeta imagenes/<slug>/ (también vale su ruta). Las capturas y las hojas quedan en imagenes/<slug>/.hyperframes/capturas/.
"""
import json
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PLANTILLA = Path(__file__).resolve().parent
RAIZ = PLANTILLA.parents[3]  # gndx.dev (plantilla → blog-imagenes → skills → .claude → raíz)
HF = "hyperframes@0.9.15"
CALIDAD = 84  # WebP: ~50–150 KB por imagen a 1600×900
TINYPNG = Path.home() / "dotfiles" / "tinypng.sh"
S3UPLOAD = Path.home() / "dotfiles" / "upload.sh"


def main():
    args = sys.argv[1:]
    destino = None
    if "--destino" in args:
        i = args.index("--destino")
        destino = Path(args[i + 1]).expanduser().resolve()
        del args[i:i + 2]
    al_blog = "--al-blog" in args
    publicar = "--publicar" in args
    sueltos = [a for a in args if not a.startswith("--")]
    if not sueltos:
        sys.exit(__doc__)
    proyecto = Path(sueltos[0]).resolve() if Path(sueltos[0]).is_dir() else RAIZ / "imagenes" / sueltos[0]
    if not (proyecto / "imagenes.py").exists():
        sys.exit(f"no existe {proyecto / 'imagenes.py'}: empieza con sh .claude/skills/blog-imagenes/plantilla/nuevo.sh <slug>")
    post = json.loads((proyecto / "post.json").read_text(encoding="utf-8"))

    def npx(*a):
        return subprocess.run(["npx", "--yes", HF, *a], cwd=proyecto, capture_output=True, text=True)

    subprocess.run([sys.executable, "-I", str(proyecto / "imagenes.py")], cwd=proyecto, check=True)
    orden = json.loads((proyecto / "orden.json").read_text(encoding="utf-8"))
    at = ",".join(f"{k + 0.5}" for k in range(len(orden)))

    # 1. check: texto que se sale de su caja o de la imagen, contraste y errores de la página
    r = npx("check", "--json", "--at", at)
    try:
        rep = json.loads(r.stdout[r.stdout.index("{"):])
    except ValueError:
        rep = None
    numero_problemas = None
    if rep is None:
        print("check: no se pudo leer la salida\n", (r.stdout + r.stderr)[-1500:])
    else:
        # Cuentan los errores de cualquier pasada y todo lo de layout (texto que se sale) y contraste.
        # No cuentan los avisos pensados para vídeo (tiempo de lectura, pistas, subcomposiciones): aquí cada segundo es una foto.
        problemas = []
        for seccion in ("lint", "runtime", "layout", "contrast"):
            for f in (rep.get(seccion) or {}).get("findings", []):
                if f.get("severity") == "error" or seccion in ("layout", "contrast"):
                    problemas.append((seccion, f))
        numero_problemas = len(problemas)
        print(f"check: {len(problemas)} problemas" + (" ✓" if not problemas else " (arréglalos antes de llevarlas al blog)"))
        for seccion, f in problemas[:30]:
            sel = f.get("selector", "")
            img = sel.split(" ")[0].lstrip("#") if sel.startswith("#img-") else sel
            print(f"  [{seccion}] {img}: {f.get('code')} · {f.get('message', '')[:140]}" + (f" «{f['text'][:50]}»" if f.get("text") else ""))

    # 2. capturas a 1600×900
    tmp = proyecto / ".hyperframes" / "capturas"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    r = npx("snapshot", "--at", at, "--no-end", "-o", str(tmp))
    pngs = sorted(tmp.glob("frame-*-at-*.png"), key=lambda p: int(p.name.split("-")[1]))
    if len(pngs) != len(orden):
        sys.exit(f"snapshot: {len(pngs)} capturas para {len(orden)} imágenes\n{(r.stdout + r.stderr)[-1500:]}")

    # 3. una hoja de contacto por idioma
    for idioma in post["idiomas"]:
        sel = [p for p, o in zip(pngs, orden) if o["idioma"] == idioma]
        d = tmp / f"_{idioma}"
        d.mkdir()
        for k, p in enumerate(sel):
            shutil.copy(p, d / f"{k:03d}.png")
        filas = math.ceil(len(sel) / 3)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", "1", "-i", str(d / "%03d.png"),
                        "-vf", f"scale=800:450,tile=3x{filas}:padding=16:margin=16:color=0x444444", "-frames:v", "1", "-q:v", "3",
                        str(tmp / f"hoja-{idioma}.jpg")], check=True)
        shutil.rmtree(d)
        print(f"hoja: {tmp / f'hoja-{idioma}.jpg'}")

    if not (al_blog or destino or publicar):
        print("Revisa las hojas (y cada captura si hace falta). Para llevarlas al blog, repite con --al-blog")
        return

    if publicar and numero_problemas != 0:
        sys.exit("no se publica: el check no terminó con 0 problemas")

    # 4. WebP al blog (o a --destino) y el Markdown de cada idioma
    if publicar and (al_blog or destino):
        sys.exit("usa --publicar solo: publica en S3 sin guardar los WebP en el proyecto")

    urls = {}
    total = 0
    if publicar:
        for script in (TINYPNG, S3UPLOAD):
            if not script.exists():
                sys.exit(f"no existe {script}")
        with tempfile.TemporaryDirectory(prefix=f"blog-imagenes-{post['slug']}-") as td:
            dest = Path(td)
            for png, o in zip(pngs, orden):
                nombre = f"{post['slug']}-{o['archivo']}.webp"
                bruto = dest / f"raw-{nombre}"
                salida = dest / nombre
                subprocess.run(["cwebp", "-quiet", "-q", str(CALIDAD), str(png), "-o", str(bruto)], check=True)
                subprocess.run([str(TINYPNG), str(bruto), str(salida)], check=True)
                r = subprocess.run([str(S3UPLOAD), str(salida)], capture_output=True, text=True)
                if r.returncode:
                    sys.exit(f"falló la subida S3 de {nombre}\n{r.stdout}{r.stderr}")
                linea = next((x for x in r.stdout.splitlines() if x.startswith("Public URL: ")), None)
                if not linea:
                    sys.exit(f"S3 no devolvió la URL de {nombre}\n{r.stdout}{r.stderr}")
                urls[o["archivo"]] = linea.removeprefix("Public URL: ").strip()
                total += salida.stat().st_size
        print(f"{len(orden)} WebP optimizados y publicados en S3 · {total / 1024:.0f} KB en total")
    else:
        dest = destino or RAIZ / "public" / "blog" / post["slug"]
        dest.mkdir(parents=True, exist_ok=True)
        for png, o in zip(pngs, orden):
            salida = dest / f"{o['archivo']}.webp"
            subprocess.run(["cwebp", "-quiet", "-q", str(CALIDAD), str(png), "-o", str(salida)], check=True)
            total += salida.stat().st_size
        print(f"{len(orden)} WebP en {dest} · {total / 1024:.0f} KB en total")

    def url(o):
        return urls.get(o["archivo"], f"/blog/{post['slug']}/{o['archivo']}.webp")

    for idioma in post["idiomas"]:
        imgs = [o for o in orden if o["idioma"] == idioma]
        print(f"\n--- {idioma} · {post.get('posts', {}).get(idioma, '(post sin encontrar)')}")
        print(f"heroImage: '{url(imgs[0])}'")
        for o in imgs:
            print(f"![{o['alt']}]({url(o)})")


if __name__ == "__main__":
    main()
