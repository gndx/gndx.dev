"""Imágenes de un post de gndx.dev (es / en / pt), hechas con HyperFrames.  ← Cambia esta línea por el título del post.

Desde la raíz de gndx.dev (exportar.py ejecuta este archivo, que escribe index.html: una imagen por segundo, idioma tras idioma):
      python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug>             → check + capturas + hojas para revisar (no toca el blog)
      python3 -I .claude/skills/blog-imagenes/plantilla/exportar.py <slug> --al-blog   → WebP 1600×900 en public/blog/<slug>/ y el Markdown

Lo que se cambia en cada post: T (los textos de cada idioma, con el `alt` de cada imagen) e IMAGENES (qué dibuja cada una).
La primera imagen es la portada: también es la imagen de Open Graph (heroImage).
Las piezas están en .claude/skills/blog-imagenes/plantilla/marca.py; los logos y capturas del post, en assets/logos/ y assets/capturas/.
Este ejemplo explica la propia plantilla: bórralo y escribe el del post.
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / ".claude" / "skills" / "blog-imagenes" / "plantilla"))  # imagenes/<slug>/ → raíz de gndx.dev
from marca import (arbol, barras, captura, cifra, cita, codigo, columna, comparar, dos, escribir, fila, flujo, linea_tiempo,  # noqa: E402,F401
                   logo, marco, metricas, movil, nota, pasos, portada, ruta, tarjetas, texto)

POST = json.loads((AQUI / "post.json").read_text(encoding="utf-8"))
IDIOMAS = POST["idiomas"]
SLUG = POST["slug"]

T = {
    "es": {
        "pie": "gndx.dev · imágenes del blog",
        "alt": {"portada": "Imágenes del blog con HyperFrames", "pasos": "Cómo se hacen: cuatro pasos y tres comandos",
                "piezas": "Las piezas de la plantilla", "antes": "Antes y después: de la imagen genérica a la del post", "camino": "De los reels al blog"},
        "k0": "Plantilla · gndx.dev", "t0": "Imágenes del blog con **HyperFrames**", "s0": "Del texto del post a WebP en tres idiomas, con la marca GNDX.", "c0": "imágenes por post",
        "k1": "Cómo se hacen", "t1": "Cuatro pasos y **tres comandos**",
        "p1": [("Lee el post", "una imagen por sección que la necesite"), ("Escribe imagenes.py", "textos en es / en / pt y una pieza por imagen"),
               ("Revisa las hojas", "check, capturas y hoja de contacto"), ("Al blog", "WebP en public/blog y el Markdown")],
        "k2": "Las piezas", "t2": "Se combinan, no se dibujan a mano",
        "c2": [("marco()", "antetítulo, título, logo y pie"), ("codigo()", "líneas numeradas, sin ventana"), ("tarjetas()", "rejilla de ideas"),
               ("metricas()", "datos con su etiqueta"), ("linea_tiempo()", "fechas, la última en oro"), ("flujo()", "herramientas con su logo")],
        "k3": "Antes y después", "t3": "Cada post con **su propia** imagen",
        "a3": ("Antes", ["La misma imagen genérica", "Sin texto ni contexto", "Igual en los tres idiomas"]),
        "b3": ("Ahora", ["Portada con el título del post", "Una imagen por paso", "Cada idioma con su texto"]),
        "k4": "De dónde sale", "t4": "Lo que aprendí con los reels, **en el blog**",
        "e4": [("05/11", "Primer reel: LEGO"), ("08/11", "Primer reel tech"), ("14/11", "El post de los reels"), ("16/11", "Esta plantilla")],
        "n4": "Mismo motor que los reels: una página web, un fotograma por imagen.",
    },
    "en": {
        "pie": "gndx.dev · blog images",
        "alt": {"portada": "Blog images with HyperFrames", "pasos": "How they're made: four steps and three commands",
                "piezas": "The template's pieces", "antes": "Before and after: from a generic image to the post's own", "camino": "From reels to the blog"},
        "k0": "Template · gndx.dev", "t0": "Blog images with **HyperFrames**", "s0": "From the post's text to WebP in three languages, with the GNDX brand.", "c0": "images per post",
        "k1": "How they're made", "t1": "Four steps and **three commands**",
        "p1": [("Read the post", "one image per section that needs it"), ("Write imagenes.py", "texts in es / en / pt and one piece per image"),
               ("Check the sheets", "check, captures and contact sheet"), ("To the blog", "WebP in public/blog and the Markdown")],
        "k2": "The pieces", "t2": "Combined, never drawn by hand",
        "c2": [("marco()", "kicker, title, logo and footer"), ("codigo()", "numbered lines, no window"), ("tarjetas()", "a grid of ideas"),
               ("metricas()", "data with its label"), ("linea_tiempo()", "dates, the last one in gold"), ("flujo()", "tools with their logo")],
        "k3": "Before and after", "t3": "Every post with **its own** image",
        "a3": ("Before", ["The same generic image", "No text, no context", "Identical in all three languages"]),
        "b3": ("Now", ["A cover with the post's title", "One image per step", "Each language with its own text"]),
        "k4": "Where it comes from", "t4": "What I learned from reels, **on the blog**",
        "e4": [("Nov 5", "First reel: LEGO"), ("Nov 8", "First tech reel"), ("Nov 14", "The reels post"), ("Nov 16", "This template")],
        "n4": "Same engine as the reels: a web page, one frame per image.",
    },
    "pt": {
        "pie": "gndx.dev · imagens do blog",
        "alt": {"portada": "Imagens do blog com HyperFrames", "pasos": "Como são feitas: quatro passos e três comandos",
                "piezas": "As peças do template", "antes": "Antes e depois: da imagem genérica à do post", "camino": "Dos reels ao blog"},
        "k0": "Template · gndx.dev", "t0": "Imagens do blog com **HyperFrames**", "s0": "Do texto do post a WebP em três idiomas, com a marca GNDX.", "c0": "imagens por post",
        "k1": "Como são feitas", "t1": "Quatro passos e **três comandos**",
        "p1": [("Leia o post", "uma imagem por seção que precisar"), ("Escreva imagenes.py", "textos em es / en / pt e uma peça por imagem"),
               ("Revise as folhas", "check, capturas e folha de contato"), ("Para o blog", "WebP em public/blog e o Markdown")],
        "k2": "As peças", "t2": "Combinadas, nunca desenhadas à mão",
        "c2": [("marco()", "sobretítulo, título, logo e rodapé"), ("codigo()", "linhas numeradas, sem janela"), ("tarjetas()", "uma grade de ideias"),
               ("metricas()", "dados com sua legenda"), ("linea_tiempo()", "datas, a última em dourado"), ("flujo()", "ferramentas com seu logo")],
        "k3": "Antes e depois", "t3": "Cada post com **sua própria** imagem",
        "a3": ("Antes", ["A mesma imagem genérica", "Sem texto nem contexto", "Igual nos três idiomas"]),
        "b3": ("Agora", ["Capa com o título do post", "Uma imagem por passo", "Cada idioma com seu texto"]),
        "k4": "De onde vem", "t4": "O que aprendi com os reels, **no blog**",
        "e4": [("05/11", "Primeiro reel: LEGO"), ("08/11", "Primeiro reel tech"), ("14/11", "O post dos reels"), ("16/11", "Este template")],
        "n4": "O mesmo motor dos reels: uma página web, um quadro por imagem.",
    },
}

COMANDOS = ["$ sh …/nuevo.sh <slug>", "$ python3 -I …/exportar.py <slug>", "$ python3 -I …/exportar.py <slug> --al-blog"]

IMAGENES = [
    ("portada", lambda t: portada(t, t["k0"], t["t0"], t["s0"],
                                  abajo=flujo([("claude", "Claude Code"), ("MD", "imagenes.py"), ("hyperframes", "HyperFrames")]),
                                  lado=cifra(str(5 * len(IDIOMAS)), t["c0"]))),
    ("pasos", lambda t: marco(t, t["k1"], t["t1"], dos(pasos(t["p1"]), codigo(COMANDOS, oro=["$"], menta=["--al-blog"], peq=True, numeros=False), izq_ancho=640))),
    ("piezas", lambda t: marco(t, t["k2"], t["t2"], tarjetas(t["c2"], cols=3))),
    ("antes", lambda t: marco(t, t["k3"], t["t3"], comparar(t["a3"], t["b3"]))),
    ("camino", lambda t: marco(t, t["k4"], t["t4"], columna(linea_tiempo(t["e4"]), texto(t["n4"], 28, "#A8A8A8"), gap=60))),
]

if __name__ == "__main__":
    escribir(AQUI, IMAGENES, T, IDIOMAS)
