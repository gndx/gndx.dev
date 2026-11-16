---
name: blog-imagenes
description: Hace las imágenes de un post de gndx.dev, en es / en / pt, a 1600×900 y en WebP, con la marca GNDX y HyperFrames, y las pone en el post. Son la portada, que también es la imagen de Open Graph, y las imágenes de dentro del artículo (una por cada sección que lo necesite). Úsala cuando Oscar escriba o termine un post, pida imágenes, una portada o ilustraciones para un artículo, quiera cambiar el blog-placeholder de un post viejo, o escriba /blog-imagenes.
---

# Imágenes de un post · gndx.dev

Mismo método que las imágenes del post «Aprende a crear videos con Inteligencia Artificial con Claude Code» (`public/blog/141126-asi-hago-mis-reels-con-ia/`):
- una página de HyperFrames con una imagen por segundo;
- una captura por imagen;
- WebP.

Todo se ejecuta desde la raíz de gndx.dev:
- La plantilla: `.claude/skills/blog-imagenes/plantilla/`.
  - `marca.py`: la marca y las piezas, común a todos los posts.
  - `exportar.py`: revisa las imágenes y las lleva al blog.
  - `nuevo.sh`: empieza un post nuevo.
  - `ejemplo.py`.
  - `README.md`: las piezas.
- El trabajo de cada post: `imagenes/<slug>/`, con `imagenes.py`, `post.json` y sus `assets/logos/` y `assets/capturas/`. Esto se sube a git para poder rehacerlas; lo demás se regenera y está en `.gitignore`.

Antes de empezar:
1. Lee `plantilla/README.md`.
2. Lee el post entero en los tres idiomas: `src/content/blog/{es,en,pt}/`.
3. Si existe, mira el original con piezas a medida: `/Users/gndx/develop/projects/lx-1/videos/blog-asi-hago-mis-reels/imagenes.py`.

## Qué imágenes
- **La portada, siempre.**
  - Lleva el título del post (o una versión más corta), un subtítulo y algo real del tema a la derecha: un logo, una captura o una cifra.
  - Es la `heroImage`, así que también es la imagen al compartir el post: tiene que leerse en pequeño.
- **Dentro del artículo, una por cada sección (H2) que se entienda mejor con un dibujo**: pasos, una comparación, datos, código, herramientas o una línea de tiempo. No hace falta una por párrafo. Suelen ser entre 4 y 9.
- **Cada imagen cuenta una sola idea.**
  - Resume el texto del post en ≤ 30 palabras; no copia el párrafo.
  - Si dos imágenes se parecen, cambia una.
- **Datos y cifras**: solo los del post, que ya están comprobados. Si falta uno, se pregunta; no se inventa.
- **Lo que existe, de su fuente**:
  - logos con `/media-use` (theSVG, GitHub, favicon), nunca redibujados;
  - capturas de webs con `npx hyperframes capture <url>`;
  - fotogramas de un vídeo con `ffmpeg`.
  - Van en `imagenes/<slug>/assets/logos/` y `assets/capturas/`. Las marcas de otros, solo para informar.
- **Que se lea en el blog**:
  - El artículo se ve a 700 px de ancho, menos de la mitad de los 1600 de la imagen. Ningún texto de menos de 24 px.
  - Pocos elementos y grandes.
  - Fondo negro, dorado para lo importante, menta para el código, rojo solo para errores.
- **Los tres idiomas**:
  - Cada idioma lleva el texto de su propio post: no se vuelve a traducir por otro lado.
  - En pt y en el texto suele ser más largo: mira que quepa en las tres hojas.
- **Solo la portada** (por ejemplo, posts viejos con `/blog-placeholder.jpg`): deja en `IMAGENES` solo `portada`.

## Paso a paso
1. **Proyecto.**
   - `sh .claude/skills/blog-imagenes/plantilla/nuevo.sh <slug>` → `imagenes/<slug>/`. El slug es el nombre del archivo del post en español, sin extensión.
   - Revisa `post.json`: tienen que estar los tres idiomas. Si un post se llama distinto en otro idioma, lo encuentra por la fecha; si no aparece, búscalo y ponlo a mano.
   - Si `imagenes/<slug>/` ya existe, se trabaja sobre su `imagenes.py`.
2. **`imagenes/<slug>/imagenes.py`.**
   - Borra el ejemplo y escribe `T`: los textos por idioma, el `pie` y el `alt` de cada imagen.
   - Escribe `IMAGENES = [(nombre, función)]`, con la portada primero. Los nombres son cortos y descriptivos (`portada`, `paso-1-instalar`, `comparativa`…).
   - Combina las piezas de `marca.py`. Si ninguna encaja, escribe una función en `imagenes.py` con las clases y colores de la marca.
3. **Revisión.**
   - `python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug>` tiene que dar **«check: 0 problemas»**, que quiere decir que no hay texto fuera de su caja ni fuera de la imagen, y que el contraste está bien.
   - Mira las hojas `imagenes/<slug>/.hyperframes/capturas/hoja-{es,en,pt}.jpg` con Read. Abre una captura entera si algo se ve raro.
   - Corrige y repite hasta que estén bien en los tres idiomas.
4. **Al blog.**
   - Repite con `--al-blog`: guarda los WebP en `public/blog/<slug>/` e imprime el Markdown de cada idioma.
   - En cada post:
     - en el frontmatter, `heroImage: '/blog/<slug>/portada-<idioma>.webp'`;
     - la portada, tras la introducción (antes del primer H2);
     - cada `![alt](…)`, justo debajo del H2 que ilustra.
   - Las rutas usan el slug en español en los tres idiomas.
5. **Comprobación.**
   - `npm run dev` y abre el post en los tres idiomas en el Chrome de Oscar (`/blog/<slug>`, `/en/blog/…`, `/pt/blog/…`).
   - Comprueba que cargan todas las imágenes y que la portada aparece arriba.
   - `npm run dev` necesita `API_KEY` y `CHANNEL_ID` en `.env`; ver `CLAUDE.md`.
6. **Git.**
   - Trabaja en una rama: la del post si existe, o si no `feat/imagenes-<slug>`.
   - Se suben `imagenes/<slug>/` y `public/blog/<slug>/`.
   - Haz commit o push solo si Oscar lo pide. **Nunca hagas push a `main`**: publica la web.
7. **Entrega en español.**
   - Las rutas de las hojas y de la carpeta en `public/blog/`.
   - La lista de imágenes, cada una con la sección que ilustra.
   - El resultado del check y el peso total.
   - Lo que quedó más flojo.
   - Que puede pedir cambios imagen a imagen: se edita `imagenes.py` y se repiten los pasos 3 y 4, que sobrescriben los WebP.

## Si cambia la marca
Se cambia `plantilla/marca.py`, que usan todos los posts. Para que un post viejo tome el cambio, se repiten los pasos 3 y 4 de ese post.

## Antes de entregar
- [ ] «check: 0 problemas» y las tres hojas revisadas.
- [ ] Portada en `heroImage` en los tres idiomas y cada imagen bajo su sección, con su `alt`.
- [ ] Ningún dato que no esté en el post; logos y capturas de su fuente.
- [ ] El post se ve en los tres idiomas con todas sus imágenes.
- [ ] Nada en `main` y nada subido sin que Oscar lo pida.
