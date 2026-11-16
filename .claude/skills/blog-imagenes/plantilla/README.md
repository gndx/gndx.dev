# Plantilla de imágenes del blog

Las imágenes de un post: la portada, que también es la imagen de Open Graph, y las de dentro del artículo. Van en es / en / pt, a 1600×900 y en WebP, con la marca GNDX: negro con rejilla de puntos, dorado `#D4A843`, Space Grotesk y Space Mono. La skill que las usa es `/blog-imagenes` (`../SKILL.md`).

## Comandos (desde la raíz de gndx.dev)

```sh
sh .claude/skills/blog-imagenes/plantilla/nuevo.sh <slug>                        # → imagenes/<slug>/ (imagenes.py de ejemplo + post.json)
python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug>             # check + capturas + hojas de contacto (no toca el blog)
python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --al-blog   # WebP en public/blog/<slug>/ + el Markdown de cada idioma
python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --publicar  # TinyPNG + raíz de S3 + Markdown con URLs públicas
```

`<slug>` es el nombre del archivo del post en español, sin extensión. `nuevo.sh` busca el post en los tres idiomas; si en otro idioma tiene otro nombre, lo encuentra por la fecha (`pubDate`). La carpeta de imágenes del blog siempre usa el slug en español.

## Qué hay

| Dónde | Qué | ¿Se sube a git? |
|---|---|---|
| `plantilla/marca.py` | La marca (CSS), las piezas y `escribir()`, que genera `index.html` y `orden.json`. La usan todos los posts. | Sí |
| `plantilla/exportar.py` | Hace el check, las capturas y las hojas; con `--publicar`, optimiza mediante TinyPNG, publica en S3 y entrega el Markdown. | Sí |
| `plantilla/ejemplo.py` | El `imagenes.py` con el que empieza cada post: un ejemplo que explica la plantilla. | Sí |
| `plantilla/assets/` | Las fuentes, el logo GNDX y logos comunes: Claude, ElevenLabs, FFmpeg, HyperFrames, OpenAI y Three.js. | Sí |
| `imagenes/<slug>/imagenes.py` | Los textos de cada idioma (`T`, con el `alt` de cada imagen) y qué dibuja cada imagen (`IMAGENES`). | Sí |
| `imagenes/<slug>/post.json` | El slug, los idiomas y el archivo del post en cada uno. | Sí |
| `imagenes/<slug>/assets/logos/`, `assets/capturas/` | Los logos y capturas propios del post. Un logo del post tapa al común del mismo nombre. | Sí |
| `imagenes/<slug>/index.html`, `orden.json`, `meta.json`, `hyperframes.json`, `assets/marca/`, `.hyperframes/` | Lo que se regenera en cada exportación. | No |

## Piezas (`marca.py`)

En los textos, `**así**` sale en dorado y `__así__` en menta.

| Pieza | Para qué |
|---|---|
| `portada(t, kicker, titulo, sub, abajo, lado)` | La portada: título grande a la izquierda; `abajo` y `lado` admiten cualquier pieza |
| `marco(t, kicker, titulo, contenido)` | El resto de imágenes: antetítulo, título, logo, pie y una zona de 1440×540 |
| `dos(izq, der, izq_ancho)` · `columna(...)` · `fila(...)` · `centro(...)` | Para colocar las piezas |
| `texto` · `nota` · `ruta` · `cita` | Párrafo, nota en mono, comando o ruta en pastilla, cita con autor |
| `codigo(lineas, oro, menta)` · `arbol(raiz, items)` | Código con números de línea y sin ventana; árbol de carpetas |
| `metricas` · `cifra` · `barras` · `linea_tiempo` | Datos: tarjetas de dato, un número enorme, barras comparadas, fechas |
| `tarjetas` · `pasos` · `comparar` | Rejilla de ideas, lista numerada, antes y después |
| `logo` · `flujo` · `captura` · `movil` | Logos de su fuente, herramientas unidas por flechas, capturas horizontales o verticales |

Si ninguna pieza encaja, escribe una función nueva en `imagenes.py` que devuelva HTML con las clases y colores de `marca.py`.

El título de cada imagen se encoge solo si no cabe (hasta el 60 % de su tamaño), y el código también si una línea es demasiado larga. Lo que aun así se salga lo avisa `exportar.py`.
