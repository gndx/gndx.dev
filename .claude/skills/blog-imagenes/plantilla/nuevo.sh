#!/bin/sh
# Empieza las imágenes de un post. Desde la raíz de gndx.dev:
#   sh .claude/skills/blog-imagenes/plantilla/nuevo.sh <slug-del-post>   → imagenes/<slug>/ con imagenes.py (ejemplo) y post.json
# El slug es el nombre del archivo del post en español, sin extensión (src/content/blog/es/<slug>.md).
set -e
SLUG="$1"
[ -n "$SLUG" ] || { echo "uso: sh .claude/skills/blog-imagenes/plantilla/nuevo.sh <slug-del-post>"; exit 1; }
PLANTILLA="$(cd "$(dirname "$0")" && pwd)"
RAIZ="$(cd "$PLANTILLA/../../../.." && pwd)"
DEST="$RAIZ/imagenes/$SLUG"
[ -e "$DEST" ] && { echo "ya existe: $DEST"; exit 1; }

mkdir -p "$DEST/assets/logos" "$DEST/assets/capturas"
cp "$PLANTILLA/ejemplo.py" "$DEST/imagenes.py"

python3 -I - "$DEST" "$SLUG" "$RAIZ" <<'PY'
import json, re, sys
from pathlib import Path

dest, slug, blog = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
raiz = blog / "src" / "content" / "blog"


def fecha(p):
    m = re.search(r"^pubDate:\s*['\"]?([0-9T:\.\-Z]+)", p.read_text(encoding="utf-8"), re.M)
    return m.group(1)[:10] if m else None


def buscar(idioma, nombre):
    return next((raiz / idioma / f"{nombre}.{x}" for x in ("md", "mdx") if (raiz / idioma / f"{nombre}.{x}").exists()), None)


posts = {}
es = buscar("es", slug)
for idioma in ("es", "en", "pt"):
    p = buscar(idioma, slug)
    if p is None and es is not None and (raiz / idioma).is_dir():
        # algunos posts cambian de slug en otro idioma: se busca el de la misma fecha
        mismos = [q for q in sorted((raiz / idioma).glob("*.md*")) if fecha(q) and fecha(q) == fecha(es)]
        p = mismos[0] if len(mismos) == 1 else None
    if p is not None:
        posts[idioma] = str(p.relative_to(blog))
    print(f"  {idioma}: {posts.get(idioma, 'NO ENCONTRADO: ponlo a mano en post.json si existe')}")

idiomas = [i for i in ("es", "en", "pt") if i in posts] or ["es", "en", "pt"]
(dest / "post.json").write_text(json.dumps({"slug": slug, "idiomas": idiomas, "posts": posts}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY
echo "listo: $DEST"
echo "  1. Cambia T e IMAGENES en imagenes/$SLUG/imagenes.py"
echo "  2. python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py $SLUG             (revisar)"
echo "  3. python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py $SLUG --al-blog   (al blog)"
