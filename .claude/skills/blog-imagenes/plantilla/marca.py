"""Marca de las imágenes del blog gndx.dev: 1600×900, negro con rejilla de puntos, dorado #D4A843, Space Grotesk y Space Mono.

Vive en .claude/skills/blog-imagenes/plantilla/ y la usan todos los posts: el contenido de cada uno va en imagenes/<slug>/imagenes.py.
Si cambia la marca, se cambia aquí y se regeneran los posts que hagan falta.
Las fuentes, el logo GNDX y los logos comunes se copian a imagenes/<slug>/assets/marca/ al generar (no se suben a git);
los logos y capturas propios del post van en imagenes/<slug>/assets/logos/ y assets/capturas/.

Texto con marcas (en títulos, textos y tarjetas):  **así** va en dorado y __así__ en menta.
Piezas que se combinan dentro de marco() o portada():
  diseño   dos(izq, der) · columna(...) · fila(...) · centro(...)
  texto    texto(s) · nota(s) · ruta(s) · cita(s, autor)
  código   codigo(lineas, oro=[...], menta=[...]) · arbol(raiz, [(nombre, comentario)])
  datos    metricas([(valor, etiqueta)]) · cifra(valor, etiqueta) · barras([(etiqueta, valor, texto)]) · linea_tiempo([(fecha, texto)])
  listas   tarjetas([(titulo, texto)], cols) · pasos([(titulo, texto)]) · comparar((titulo, [items]), (titulo, [items]))
  marcas   logo(nombre) · flujo([(logo|None|"MD", nombre)]) · captura(ruta) · movil(ruta)
"""
import html
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

W, H = 1600, 900
ORO, ROJO, MENTA, VIOLETA = "#D4A843", "#D71921", "#7EE0B5", "#6A48D1"
e = html.escape
PLANTILLA = Path(__file__).resolve().parent
_PROYECTO = Path(sys.argv[0]).resolve().parent  # la carpeta del post (la de imagenes.py); escribir() la fija


def _ruta_logo(nombre):
    """assets/logos/<nombre>.svg del post o, si no está, el logo común de la plantilla. None si no hay ninguno."""
    if (_PROYECTO / "assets" / "logos" / f"{nombre}.svg").exists():
        return f"assets/logos/{nombre}.svg"
    if (PLANTILLA / "assets" / "logos" / f"{nombre}.svg").exists():
        return f"assets/marca/logos/{nombre}.svg"
    return None


def marcar(s):
    """Escapa el texto; **x** va en dorado y __x__ en menta."""
    s = e(str(s))
    s = re.sub(r"\*\*(.+?)\*\*", r'<b class="o">\1</b>', s)
    return re.sub(r"__(.+?)__", r'<b class="m">\1</b>', s)


def _resaltar(linea, oro, menta):
    s = e(linea)
    for x in oro:
        s = s.replace(e(x), f'<b class="o">{e(x)}</b>')
    for x in menta:
        s = s.replace(e(x), f'<b class="m">{e(x)}</b>')
    return s


# ---------------------------------------------------------------- marcos de imagen

def marco(t, kicker, titulo, contenido):
    """La imagen normal: antetítulo dorado, título, logo GNDX, pie y la zona de contenido (1440×560, desde y 260)."""
    return (f'<div class="kick">{marcar(kicker)}</div><div class="tit" data-ajustar="150">{marcar(titulo)}</div>'
            f'<img class="gndx" src="assets/marca/gndx-logo-transparente.svg" alt=""><div class="pie">{e(t.get("pie", "gndx.dev"))}</div>'
            f'<div class="zona">{contenido}</div>')


def portada(t, kicker, titulo, sub="", abajo="", lado=""):
    """La portada (y la imagen de Open Graph): título grande a la izquierda; `abajo` bajo el subtítulo y `lado` a la derecha."""
    return (f'<div class="por-izq"><div class="kick-p">{marcar(kicker)}</div><div class="tit-p" data-ajustar="330">{marcar(titulo)}</div>'
            + (f'<div class="sub">{marcar(sub)}</div>' if sub else "") + (f'<div class="por-abajo">{abajo}</div>' if abajo else "") + "</div>"
            + (f'<div class="por-der">{lado}</div>' if lado else "")
            + f'<img class="gndx" src="assets/marca/gndx-logo-transparente.svg" alt=""><div class="pie">{e(t.get("pie", "gndx.dev"))}</div>')


# ---------------------------------------------------------------- diseño

def dos(izq, der, izq_ancho=820, gap=80):
    """Dos columnas dentro de la zona: la izquierda de `izq_ancho` px y la derecha con el resto."""
    return f'<div class="dos" style="gap:{gap}px"><div class="col" style="width:{izq_ancho}px">{izq}</div><div class="col" style="flex:1;min-width:0">{der}</div></div>'


def columna(*piezas, gap=28, centrar=False):
    return f'<div class="col" style="gap:{gap}px{";align-items:center;text-align:center" if centrar else ""}">{"".join(piezas)}</div>'


def fila(*piezas, gap=24):
    return f'<div class="fila" style="gap:{gap}px">{"".join(piezas)}</div>'


def centro(pieza):
    return f'<div class="centro">{pieza}</div>'


# ---------------------------------------------------------------- texto

def texto(s, tam=30, color=None):
    return f'<div class="txt" style="font-size:{tam}px{";color:" + color if color else ""}">{marcar(s)}</div>'


def nota(s):
    return f'<div class="nota">{marcar(s)}</div>'


def ruta(s, oro=(), menta=()):
    """Una ruta, un comando o una URL en una pastilla."""
    return f'<div class="ruta">{_resaltar(s, oro, menta)}</div>'


def cita(s, autor=""):
    return f'<div class="cita"><div class="cita-t">«{marcar(s)}»</div>' + (f'<div class="cita-a">— {e(autor)}</div>' if autor else "") + "</div>"


# ---------------------------------------------------------------- código

def codigo(lineas, oro=(), menta=(), peq=False, numeros=True):
    """Código con números de línea, sin ventana de terminal. `oro` y `menta`: trozos que se resaltan."""
    filas = "".join(f'<div class="cl">{f"<span class=num>{k + 1}</span>" if numeros else ""}<span>{_resaltar(l, oro, menta) or "&nbsp;"}</span></div>' for k, l in enumerate(lineas))
    return f'<div class="codigo{" peq" if peq else ""}" data-ajustar="0">{filas}</div>'


def arbol(raiz, items):
    """Árbol de carpetas: items = [(nombre, comentario)]."""
    filas = "".join(f'<div class="arb"><span class="g">{"└─" if k == len(items) - 1 else "├─"}</span> <b>{e(a)}</b>' + (f'<span class="c">{marcar(b)}</span>' if b else "") + "</div>" for k, (a, b) in enumerate(items))
    return f'<div class="arbol"><div class="arb-r">{e(raiz)}</div>{filas}</div>'


# ---------------------------------------------------------------- datos

def metricas(items, cols=3):
    """Tarjetas de dato: items = [(valor, etiqueta)]."""
    celdas = "".join(f'<div class="met"><div class="mv">{marcar(a)}</div><div class="ml">{marcar(b)}</div></div>' for a, b in items)
    return f'<div class="metricas" style="grid-template-columns:repeat({cols}, 1fr)">{celdas}</div>'


def cifra(valor, etiqueta=""):
    """Un número enorme en dorado con su etiqueta debajo."""
    return f'<div class="cifra"><div class="cn">{marcar(valor)}</div>' + (f'<div class="cc">{marcar(etiqueta)}</div>' if etiqueta else "") + "</div>"


def barras(items, destacar=None):
    """Barras horizontales: items = [(etiqueta, valor, texto_del_valor)]. La de `destacar` (índice) va en dorado."""
    tope = max(v for _, v, _ in items) or 1
    filas = "".join(
        f'<div class="bar"><span class="bl">{marcar(a)}</span><div class="bc"><i style="width:{max(1.5, v / tope * 100):.1f}%"'
        f'{" class=d" if k == destacar else ""}></i></div><span class="bv">{marcar(txt)}</span></div>' for k, (a, v, txt) in enumerate(items))
    return f'<div class="barras">{filas}</div>'


def linea_tiempo(items):
    """Línea de tiempo horizontal: items = [(fecha, texto)]. El último punto va en dorado."""
    puntos = "".join(f'<div class="lt-p{" fin" if k == len(items) - 1 else ""}"><div class="lt-f">{marcar(f)}</div><i></i><div class="lt-t">{marcar(x)}</div></div>' for k, (f, x) in enumerate(items))
    return f'<div class="lt"><div class="lt-eje"></div>{puntos}</div>'


# ---------------------------------------------------------------- listas

def tarjetas(items, cols=3):
    """Rejilla de tarjetas: items = [(titulo, texto)]."""
    celdas = "".join(f'<div class="tj"><div class="tjn">{marcar(a)}</div><div class="tjr">{marcar(b)}</div></div>' for a, b in items)
    return f'<div class="tarjetas" style="grid-template-columns:repeat({cols}, 1fr)">{celdas}</div>'


def pasos(items):
    """Lista numerada: items = [(titulo, texto)]."""
    filas = "".join(f'<div class="paso"><div class="pn">{k + 1}</div><div><div class="pt">{marcar(a)}</div>' + (f'<div class="pr">{marcar(b)}</div>' if b else "") + "</div></div>" for k, (a, b) in enumerate(items))
    return f'<div class="pasos">{filas}</div>'


def comparar(a, b):
    """Antes / después (o A contra B): a y b = (titulo, [items]). La A va apagada con ✗; la B en dorado con ✓."""
    def panel(tit, items, clase, marca_):
        return f'<div class="cmp {clase}"><div class="cmp-t">{marcar(tit)}</div>' + "".join(f'<div class="cmp-i"><span>{marca_}</span>{marcar(x)}</div>' for x in items) + "</div>"
    return f'<div class="comparar">{panel(a[0], a[1], "a", "✗")}<div class="cmp-f">→</div>{panel(b[0], b[1], "b", "✓")}</div>'


# ---------------------------------------------------------------- marcas, capturas y logos

def logo(nombre, fondo="osc", tam=64):
    """Logo de assets/logos/<nombre>.svg del post o de los comunes (de su fuente: media-use, theSVG o la web oficial; nunca redibujado).
    fondo: osc | claro."""
    ruta = _ruta_logo(nombre)
    if ruta is None:
        raise SystemExit(f"falta el logo «{nombre}»: guárdalo de su fuente en {_PROYECTO / 'assets' / 'logos' / (nombre + '.svg')}")
    return f'<div class="lg {fondo}" style="width:{tam}px;height:{tam}px"><img src="{ruta}" alt=""></div>'


def flujo(items, fondos=None):
    """Fichas unidas por flechas: items = [(logo, nombre)]; logo = nombre de assets/logos, None (sin logo) o un texto corto ("MD")."""
    fondos = fondos or {}
    fichas = []
    for lg, nom in items:
        if lg and _ruta_logo(lg):
            marca_ = logo(lg, fondos.get(lg, "osc"), 52)
        elif lg:
            marca_ = f'<div class="lg osc md" style="width:52px;height:52px">{e(lg)}</div>'
        else:
            marca_ = ""
        flecha = '<div class="flecha">→</div>' if fichas else ""
        fichas.append(f'<div class="paso-f">{flecha}<div class="ficha">{marca_}<span>{marcar(nom)}</span></div></div>')
    return f'<div class="flujo">{"".join(fichas)}</div>'


def captura(src, ancho=820, giro=0):
    """Una captura horizontal de verdad (web con `npx hyperframes capture`, una app, un fotograma 16:9)."""
    return f'<div class="captura" data-layout-allow-overflow style="width:{ancho}px;transform:rotate({giro}deg)"><img src="{e(src)}" alt=""></div>'


def movil(src, ancho=300, giro=0):
    """Una captura vertical (un fotograma de un reel, una app) en un móvil."""
    return f'<div class="movil" data-layout-allow-overflow style="width:{ancho}px;height:{round(ancho * 16 / 9)}px;transform:rotate({giro}deg)"><img src="{e(src)}" alt=""></div>'


# ---------------------------------------------------------------- estilos

CSS = f"""
    @font-face {{ font-family: "Space Grotesk"; src: url("assets/marca/fonts/space-grotesk.woff2") format("woff2"); font-weight: 300 700; }}
    @font-face {{ font-family: "Space Mono"; src: url("assets/marca/fonts/space-mono-400.woff2") format("woff2"); font-weight: 400; }}
    @font-face {{ font-family: "Space Mono"; src: url("assets/marca/fonts/space-mono-700.woff2") format("woff2"); font-weight: 700; }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #000; }}
    #root {{ position: relative; width: {W}px; height: {H}px; }}
    .img {{ position: absolute; inset: 0; background: #000; overflow: hidden; font-family: "Space Grotesk", sans-serif; color: #E8E8E8; }}
    .img::before {{ content: ""; position: absolute; inset: 0; background: radial-gradient(circle, #262626 1.4px, transparent 1.9px) 0 0 / 26px 26px; }}
    .img::after {{ content: ""; position: absolute; right: -320px; top: -360px; width: 1000px; height: 1000px; border-radius: 50%; background: radial-gradient(circle, rgba(212,168,67,.16), transparent 64%); }}
    .img > * {{ position: absolute; z-index: 1; }}
    .o {{ color: {ORO}; }} .m {{ color: {MENTA}; }} b {{ font-weight: inherit; }}
    .kick {{ left: 80px; top: 64px; font-family: "Space Mono", monospace; font-size: 22px; letter-spacing: .14em; text-transform: uppercase; color: {ORO}; }}
    .tit {{ left: 80px; top: 104px; width: 1300px; max-height: 150px; font-size: 62px; font-weight: 600; line-height: 1.05; letter-spacing: -.025em; color: #fff; }}
    .gndx {{ right: 80px; top: 60px; width: 64px; opacity: .7; }}
    .pie {{ left: 80px; bottom: 44px; font-family: "Space Mono", monospace; font-size: 18px; letter-spacing: .1em; text-transform: uppercase; color: #8A8A8A; }}
    .zona {{ left: 80px; top: 270px; width: 1440px; height: 540px; display: flex; flex-direction: column; justify-content: center; }}
    .por-izq {{ left: 80px; top: 120px; bottom: 110px; width: 880px; display: flex; flex-direction: column; justify-content: center; gap: 30px; }}
    .por-der {{ left: 1010px; right: 80px; top: 120px; bottom: 110px; display: flex; align-items: center; justify-content: center; }}
    .kick-p {{ font-family: "Space Mono", monospace; font-size: 24px; letter-spacing: .14em; text-transform: uppercase; color: {ORO}; }}
    .tit-p {{ max-height: 330px; font-size: 100px; font-weight: 600; line-height: .98; letter-spacing: -.035em; color: #fff; }}
    .sub {{ font-size: 34px; line-height: 1.35; color: #A8A8A8; }}
    .dos {{ display: flex; align-items: center; width: 100%; height: 100%; }}
    .col {{ display: flex; flex-direction: column; justify-content: center; }}
    .fila {{ display: flex; align-items: center; flex-wrap: wrap; }}
    .centro {{ display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; }}
    .txt {{ line-height: 1.35; color: #E8E8E8; }}
    .nota {{ font-family: "Space Mono", monospace; font-size: 24px; line-height: 1.5; color: #A8A8A8; }}
    .ruta {{ align-self: flex-start; font-family: "Space Mono", monospace; font-size: 28px; color: #E8E8E8; background: #111; border: 2px solid #333; border-radius: 99px; padding: 10px 26px; white-space: nowrap; }}
    .cita {{ border-left: 8px solid {ORO}; padding: 8px 0 8px 36px; }}
    .cita-t {{ font-size: 44px; font-weight: 600; line-height: 1.2; color: #fff; letter-spacing: -.015em; }}
    .cita-a {{ margin-top: 18px; font-family: "Space Mono", monospace; font-size: 22px; color: #A8A8A8; }}
    .codigo {{ background: #111; border: 2px solid #333; border-left: 8px solid {MENTA}; border-radius: 14px; padding: 22px 28px; font-family: "Space Mono", monospace; font-weight: 700; font-size: 30px; line-height: 1.7; color: #F2F2F2; white-space: pre; overflow: hidden; }}
    .codigo.peq {{ font-size: 25px; line-height: 1.65; }}
    .cl {{ display: flex; }} .num {{ width: 46px; flex: none; color: #555; font-weight: 400; }}
    .arbol {{ font-family: "Space Mono", monospace; font-size: 28px; line-height: 1.95; }}
    .arb-r {{ color: {ORO}; font-weight: 700; }} .arb {{ white-space: nowrap; }} .arb .g {{ color: #555; }} .arb b {{ color: #fff; font-weight: 700; }} .arb .c {{ color: #8A8A8A; margin-left: 22px; font-size: 24px; }}
    .metricas {{ display: grid; gap: 16px; width: 100%; }}
    .met {{ background: #111; border: 2px solid #333; border-radius: 14px; padding: 18px 22px; }}
    .mv {{ font-size: 46px; font-weight: 600; color: #fff; white-space: nowrap; letter-spacing: -.02em; }} .ml {{ font-family: "Space Mono", monospace; font-size: 21px; color: #A8A8A8; margin-top: 4px; }}
    .cifra .cn {{ font-size: 200px; font-weight: 600; line-height: .9; letter-spacing: -.05em; color: {ORO}; white-space: nowrap; }}
    .cifra .cc {{ margin-top: 16px; font-family: "Space Mono", monospace; font-size: 28px; letter-spacing: .08em; text-transform: uppercase; color: #fff; }}
    .barras {{ display: flex; flex-direction: column; gap: 18px; width: 100%; }}
    .bar {{ display: flex; align-items: center; gap: 22px; }}
    .bl {{ width: 280px; flex: none; font-size: 28px; font-weight: 600; color: #E8E8E8; text-align: right; }}
    .bc {{ flex: 1; height: 44px; background: #0E0E0E; border: 2px solid #262626; border-radius: 10px; overflow: hidden; }}
    .bc i {{ display: block; height: 100%; background: linear-gradient(90deg, #4A3B7A, {VIOLETA}); border-radius: 8px; }} .bc i.d {{ background: {ORO}; }}
    .bv {{ width: 200px; flex: none; font-family: "Space Mono", monospace; font-weight: 700; font-size: 26px; color: #fff; }}
    .lt {{ position: relative; display: flex; justify-content: space-between; width: 100%; padding-top: 4px; }}
    .lt-eje {{ position: absolute; left: 0; right: 0; top: 66px; height: 4px; background: #333; border-radius: 2px; }}
    .lt-p {{ position: relative; flex: 1; display: flex; flex-direction: column; align-items: flex-start; padding-right: 22px; }}
    .lt-f {{ height: 46px; font-family: "Space Mono", monospace; font-weight: 700; font-size: 26px; color: #fff; white-space: nowrap; }}
    .lt-p i {{ display: block; width: 26px; height: 26px; margin: 3px 0 0 0; border-radius: 50%; background: #000; border: 5px solid #8A8A8A; }}
    .lt-p.fin i {{ border-color: {ORO}; background: {ORO}; }} .lt-p.fin .lt-f {{ color: {ORO}; }}
    .lt-t {{ margin-top: 22px; font-size: 27px; line-height: 1.3; color: #C8C8C8; }}
    .tarjetas {{ display: grid; gap: 18px; width: 100%; }} .tarjetas > *, .metricas > * {{ min-width: 0; overflow-wrap: anywhere; }}
    .tj {{ background: #111; border: 2px solid #333; border-top: 6px solid {ORO}; border-radius: 14px; padding: 20px 24px; min-height: 170px; }}
    .tjn {{ font-family: "Space Mono", monospace; font-weight: 700; font-size: 27px; color: #fff; margin-bottom: 12px; }}
    .tjr {{ font-size: 27px; line-height: 1.3; color: #A8A8A8; }}
    .pasos {{ display: flex; flex-direction: column; gap: 20px; }}
    .paso {{ display: flex; gap: 24px; align-items: flex-start; }}
    .pn {{ flex: none; width: 56px; height: 56px; border-radius: 50%; background: {ORO}; color: #000; font-family: "Space Mono", monospace; font-weight: 700; font-size: 28px; display: flex; align-items: center; justify-content: center; }}
    .pt {{ font-size: 36px; font-weight: 600; color: #fff; line-height: 1.2; padding-top: 8px; }} .pr {{ font-size: 27px; color: #A8A8A8; line-height: 1.35; margin-top: 4px; }}
    .comparar {{ display: flex; align-items: stretch; gap: 26px; width: 100%; }}
    .cmp {{ flex: 1; border-radius: 16px; padding: 26px 30px; background: #111; border: 2px solid #333; }}
    .cmp.b {{ border: 4px solid {ORO}; box-shadow: 0 0 40px rgba(212,168,67,.18); }}
    .cmp-t {{ font-family: "Space Mono", monospace; font-weight: 700; font-size: 25px; letter-spacing: .1em; text-transform: uppercase; color: #8A8A8A; margin-bottom: 18px; }}
    .cmp.b .cmp-t {{ color: {ORO}; }}
    .cmp-i {{ display: flex; gap: 16px; font-size: 31px; line-height: 1.35; color: #A8A8A8; padding: 8px 0; }} .cmp.b .cmp-i {{ color: #fff; }}
    .cmp-i span {{ flex: none; width: 28px; font-weight: 700; color: {ROJO}; }} .cmp.b .cmp-i span {{ color: {MENTA}; }}
    .cmp-f {{ align-self: center; font-size: 48px; color: {ORO}; }}
    .lg {{ border-radius: 16px; display: flex; align-items: center; justify-content: center; flex: none; }}
    .lg.osc {{ background: #0B0B0B; border: 2px solid #333; }} .lg.claro {{ background: #F2F2F2; }}
    .lg img {{ width: 64%; height: 64%; object-fit: contain; }}
    .lg.md {{ font-family: "Space Mono", monospace; font-weight: 700; font-size: 20px; color: {ORO}; }}
    .flujo {{ display: flex; flex-wrap: wrap; align-items: center; row-gap: 20px; }}
    .ficha {{ display: flex; align-items: center; gap: 14px; padding: 10px 20px 10px 10px; background: #111; border: 2px solid #333; border-radius: 14px; font-size: 28px; font-weight: 600; color: #fff; white-space: nowrap; }}
    .ficha:not(:has(.lg)) {{ padding-left: 20px; }}
    .paso-f {{ display: flex; align-items: center; }} .flecha {{ margin: 0 12px; font-size: 30px; color: {ORO}; }}
    .captura {{ border-radius: 16px; overflow: hidden; border: 2px solid #333; box-shadow: 0 30px 80px rgba(0,0,0,.6); background: #111; }}
    .captura img {{ width: 100%; display: block; }}
    .movil {{ border: 10px solid #1A1A1A; border-radius: 34px; overflow: hidden; background: #000; box-shadow: 0 0 0 2px #333, 0 30px 80px rgba(0,0,0,.6); flex: none; }}
    .movil img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
"""

# Encoge el texto que no cabe (data-ajustar = alto máximo en px; "0" = solo el ancho), hasta el 60 % de su tamaño. Una vez, antes de la captura.
AJUSTE = """
      function ajustar() {
        document.querySelectorAll("[data-ajustar]").forEach((el) => {
          const alto = +el.dataset.ajustar; let fs = parseFloat(getComputedStyle(el).fontSize);
          if (!el.dataset.fs0) el.dataset.fs0 = fs; else { fs = +el.dataset.fs0; el.style.fontSize = fs + "px"; }
          const min = 0.6 * +el.dataset.fs0;
          while (((alto && el.scrollHeight > alto + 1) || el.scrollWidth > el.clientWidth + 1) && fs - 1 >= min) { fs -= 1; el.style.fontSize = fs + "px"; }
        });
      }
      ajustar();
      if (document.fonts) document.fonts.ready.then(ajustar);
"""


def escribir(aqui, imagenes, textos, idiomas):
    """Escribe index.html (una imagen por segundo, idioma tras idioma) y orden.json con el nombre de cada una.
    imagenes = [(nombre, funcion(t))]; textos = {idioma: {...}}."""
    global _PROYECTO
    aqui = _PROYECTO = Path(aqui).resolve()
    # lo común de la plantilla (fuentes, logo GNDX, logos) y los archivos de proyecto de HyperFrames
    shutil.copytree(PLANTILLA / "assets", aqui / "assets" / "marca", dirs_exist_ok=True)
    if not (aqui / "hyperframes.json").exists():
        shutil.copy(PLANTILLA / "hyperframes.json", aqui / "hyperframes.json")
    if not (aqui / "meta.json").exists():
        ahora = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        (aqui / "meta.json").write_text(json.dumps({"id": f"imagenes-{aqui.name}", "name": f"imagenes-{aqui.name}", "createdAt": ahora}, indent=2) + "\n", encoding="utf-8")
    slots, orden = [], []
    k = 0
    for idioma in idiomas:
        for nombre, pinta in imagenes:
            slots.append(f'      <div id="img-{nombre}-{idioma}" class="clip img" data-start="{k}" data-duration="1" data-track-index="0">{pinta(textos[idioma])}\n      </div>')
            alt = textos[idioma].get("alt", {}).get(nombre)
            if not alt:
                print(f"aviso: falta el alt de «{nombre}» en {idioma} (T['{idioma}']['alt'])")
            orden.append({"archivo": f"{nombre}-{idioma}", "nombre": nombre, "idioma": idioma, "alt": alt or nombre})
            k += 1
    doc = f"""<!doctype html>
<html lang="{idiomas[0]}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>{CSS}    </style>
  </head>
  <body>
    <!-- GENERADO por imagenes.py (no lo edites a mano): {len(imagenes)} imágenes × {len(idiomas)} idiomas, una por segundo (captura en k + 0,5 s). -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{k}" data-width="{W}" data-height="{H}">
{chr(10).join(slots)}
    </div>
    <script>{AJUSTE}
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.to({{}}, {{ duration: {k} }}, 0);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
    (aqui / "index.html").write_text(doc, encoding="utf-8")
    (aqui / "orden.json").write_text(json.dumps(orden, ensure_ascii=False), encoding="utf-8")
    print(f"escrito index.html · {len(imagenes)} imágenes × {len(idiomas)} idiomas = {k}")
