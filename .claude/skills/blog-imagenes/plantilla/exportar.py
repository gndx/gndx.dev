"""Revisa y exporta las imágenes de un post. Se ejecuta desde la raíz de gndx.dev:

  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug>                 → imagenes.py + check + capturas + hojas (no toca el blog)
  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --al-blog       → además, WebP en public/blog/<slug>/ y el Markdown de cada idioma
  python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --destino DIR   → los WebP a otra carpeta (para probar sin tocar el blog)

<slug> es la carpeta imagenes/<slug>/ (también vale su ruta). Las capturas y las hojas quedan en imagenes/<slug>/.hyperframes/capturas/.
"""
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

PLANTILLA = Path(__file__).resolve().parent
RAIZ = PLANTILLA.parents[3]  # gndx.dev (plantilla → blog-imagenes → skills → .claude → raíz)
HF = "hyperframes@0.9.15"
CALIDAD = 84  # WebP: ~50–150 KB por imagen a 1600×900


def main():
    args = sys.argv[1:]
    destino = None
    if "--destino" in args:
        i = args.index("--destino")
        destino = Path(args[i + 1]).expanduser().resolve()
        del args[i:i + 2]
    al_blog = "--al-blog" in args
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

    if not (al_blog or destino):
        print("Revisa las hojas (y cada captura si hace falta). Para llevarlas al blog, repite con --al-blog")
        return

    # 4. WebP al blog (o a --destino) y el Markdown de cada idioma
    dest = destino or RAIZ / "public" / "blog" / post["slug"]
    dest.mkdir(parents=True, exist_ok=True)
    total = 0
    for png, o in zip(pngs, orden):
        salida = dest / f"{o['archivo']}.webp"
        subprocess.run(["cwebp", "-quiet", "-q", str(CALIDAD), str(png), "-o", str(salida)], check=True)
        total += salida.stat().st_size
    print(f"{len(orden)} WebP en {dest} · {total / 1024:.0f} KB en total")

    base = f"/blog/{post['slug']}"
    for idioma in post["idiomas"]:
        imgs = [o for o in orden if o["idioma"] == idioma]
        print(f"\n--- {idioma} · {post.get('posts', {}).get(idioma, '(post sin encontrar)')}")
        print(f"heroImage: '{base}/{imgs[0]['archivo']}.webp'")
        for o in imgs:
            print(f"![{o['alt']}]({base}/{o['archivo']}.webp)")


if __name__ == "__main__":
    main()
