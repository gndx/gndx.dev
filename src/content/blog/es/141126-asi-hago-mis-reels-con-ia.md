---
title: 'Aprende a crear videos con Inteligencia Artificial con Claude Code'
description: 'Cómo convierto una sola frase en un reel de 60 segundos con Claude Code, una skill, ElevenLabs, Whisper, HyperFrames y FFmpeg. Incluye la skill completa para personalizar y un prompt para adaptarla a tu canal.'
pubDate: '2026-11-14T21:00:00.000Z'
heroImage: '/blog/141126-asi-hago-mis-reels-con-ia/portada-es.webp'
categories:
  - 'ia'
  - 'herramientas'
authors:
  - 'gndx'
tags:
  - 'claude code'
  - 'skills'
  - 'hyperframes'
  - 'elevenlabs'
  - 'whisper'
  - 'ffmpeg'
  - 'reels'
---

Has visto cientos de vídeos como los míos, pero nadie te explica cómo se hacen. En el reel te lo conté en un minuto; aquí va la versión completa: qué herramienta hace cada cosa, en qué orden, los errores que me costaron y **la skill entera para que la copies**, junto con un prompt que la entiende y te ayuda a adaptarla a tu canal.

La idea de fondo es sencilla: **no edito vídeos, escribo reglas**. Le doy una frase a Claude Code, él lee mis reglas y hace el trabajo pesado. Yo elijo la historia, reviso y corrijo. Y cada corrección se convierte en una regla nueva.

![Así hago mis reels con IA](/blog/141126-asi-hago-mis-reels-con-ia/portada-es.webp)

## Lo que necesitas

| Herramienta | Para qué | Notas |
|---|---|---|
| **Claude Code** | El agente que hace todo el trabajo | Trabaja en tu terminal, dentro de la carpeta del proyecto |
| **Una skill** (`SKILL.md`) | Tus reglas: canal, estilo, voz, pasos | Va en `~/.claude/skills/<nombre>/SKILL.md` |
| **HyperFrames** | Convierte HTML en vídeo | Código abierto (HeyGen). Necesita Node.js 22+, FFmpeg y Chrome. Se usa con `npx hyperframes` |
| **ElevenLabs** | Texto → voz | Una voz prediseñada o tu voz clonada. La clave, solo en una variable de entorno |
| **Whisper** | Voz → texto, para comprobar | El modelo `small`, en local (yo uso faster-whisper) |
| **FFmpeg** | Une, mide y ajusta el audio | Sonoridad, picos y fotogramas negros |
| **Three.js** | El mundo 3D (opcional) | Viene dentro del proyecto |

También uso música con licencia (Epidemic Sound) y una plantilla de proyecto que fui armando reel a reel. Si no tienes plantilla, no pasa nada: en el primer vídeo Claude Code la crea contigo.

## Paso 1 · Todo empieza con una frase

![Paso 1: la frase en Claude Code](/blog/141126-asi-hago-mis-reels-con-ia/paso-1-prompt-es.webp)

Abro Claude Code en la carpeta de mis vídeos y escribo el nombre de la skill seguido del tema, con mis palabras:

```text
/video-tech crea un video explicando cómo usamos esta tool, las herramientas, la estructura, la skill… en pasos, amigable y listo
```

`/video-tech` carga la skill; el resto es el encargo. No hace falta escribir un prompt perfecto: las reglas ya están en la skill. Esa es la gracia.

<aside class="promo-mentor not-prose" aria-label="Mentoría con Oscar Barajas">
<p class="promo-mentor__eyebrow">Mentoría · @gndx</p>
<p class="promo-mentor__title">Compra la carpeta con todos mis aprendizajes</p>
<div class="promo-mentor__options">
<p class="promo-mentor__option"><span class="promo-mentor__price">$1,99 USD</span><span class="promo-mentor__detail">Solo la carpeta</span></p>
<p class="promo-mentor__option promo-mentor__option--featured"><span class="promo-mentor__price">$20 USD</span><span class="promo-mentor__detail">La carpeta + mentoría y seguimiento de tu proyecto</span></p>
</div>
<a class="promo-mentor__cta" href="https://mentor.gndx.dev/" target="_blank" rel="noopener">Ir a mentor.gndx.dev <span aria-hidden="true">→</span></a>
</aside>

## Paso 2 · La skill: un archivo con todas tus reglas

![Paso 2: la skill](/blog/141126-asi-hago-mis-reels-con-ia/paso-2-skill-es.webp)

Una skill es un archivo Markdown con un encabezado (nombre y descripción) y tus instrucciones. Claude Code la lee antes de empezar, así que **si cambias la skill, cambian todos tus vídeos**. La mía tiene seis bloques:

- **El canal**: la cuenta, los temas, el tono y la frase de cierre.
- **Estilo**: colores, fuentes, qué va dibujado y qué es «de verdad», y la zona segura de Instagram.
- **Datos**: solo fuentes primarias, con fecha; los superlativos se cruzan con varias fuentes.
- **Voz**: qué voz, a qué velocidad y cómo escribir las palabras que se leen mal.
- **Paso a paso**: 13 pasos, de la historia al render.
- **Antes de entregar**: la lista que se revisa siempre.

Al final del artículo tienes una versión completa, lista para copiar y personalizar.

## Paso 3 · Una plantilla y tres historias

![Paso 3: plantilla y tres historias](/blog/141126-asi-hago-mis-reels-con-ia/paso-3-plantilla-es.webp)

Claude Code investiga el tema y monta el proyecto desde mi plantilla con un solo comando:

```bash
sh plantillas/nuevo.sh tech mi-reel
```

La plantilla trae todo lo que se repite en cada reel: el script de la voz, el generador de subtítulos y capítulos, el mundo 3D, fuentes, música y efectos. Además crea una **maqueta**: estima los tiempos de la voz a partir del texto, así que el reel se ve entero sin gastar ni un carácter de ElevenLabs.

Después me propone **tres historias distintas**, cada una con su esquema por segundos y los datos ya comprobados. Yo elijo una con un clic. Todas siguen la misma estructura, que es la que mejor me ha funcionado:

1. **Gancho** en los 3 primeros segundos: una pregunta sorprendente sobre lo que estás viendo.
2. **Promesa** corta: «te lo cuento en un minuto».
3. **Capítulos** de 4 a 6 segundos que giran: «pero…», «hasta que…».
4. **Un dato** con número.
5. **Remate** que vuelve al gancho.
6. **Cierre** para seguir.

## Paso 4 · La voz, en una sola toma

![Paso 4: voz y comprobación](/blog/141126-asi-hago-mis-reels-con-ia/paso-4-voz-es.webp)

Claude Code escribe el guion (unas 150 palabras para 60 segundos) y **ElevenLabs** le pone voz. La onda de la imagen es la de verdad: la sonoridad de la voz de este reel, frase a frase.

Aquí aprendí la lección más cara: al principio generaba la voz **frase a frase** y dejaba huecos entre una y otra para que «respiraran» las animaciones. Sonaba a cortes. Ahora todo el guion va **en una sola llamada** y después se corta en los silencios, solo para saber cuándo empieza cada palabra. La voz fluye y los subtítulos siguen yendo palabra a palabra.

Luego **Whisper** escucha cada frase y la compara con el guion. Si una palabra se entiende mal, se escribe como suena: para que dijera bien «FFmpeg», el guion pone «efe efe eme peg» (en pantalla sale la forma correcta).

> 🔐 La clave de ElevenLabs va solo en la variable `ELEVENLABS_API_KEY`. Nunca en un archivo del proyecto, nunca en el chat.

## Paso 5 · El vídeo es una página web

![Paso 5: el vídeo es una página web](/blog/141126-asi-hago-mis-reels-con-ia/paso-5-web-es.webp)

Este es el truco que más sorprende: cada reel es **una página web**. HyperFrames toma un `index.html` con capas (el mundo 3D en un `<canvas>` con Three.js, los subtítulos, los capítulos, las tarjetas, el audio) y una línea de tiempo de GSAP **en pausa**. Cada fotograma es un instante concreto de esa línea de tiempo, así que el resultado es el mismo en cada render.

Antes de renderizar reviso dos cosas:

```bash
npx hyperframes check        # errores, contraste, textos que no da tiempo a leer
npx hyperframes preview      # la vista previa en el navegador
```

Además pongo la **zona segura de Instagram** encima de capturas de varios segundos: la cabecera tapa la parte de arriba, los botones la derecha y el texto del post la de abajo. Todo lo importante va en x 100–980 e y 222–1660 (y a la izquierda de x 900 por debajo de y 1280). Esas medidas salen de un reel publicado, no de una guía.

## Paso 6 · 1.800 fotos que se vuelven un MP4

![Paso 6: render y FFmpeg](/blog/141126-asi-hago-mis-reels-con-ia/paso-6-render-es.webp)

HyperFrames congela la página y la fotografía **1.800 veces** (60 segundos a 30 fps). **FFmpeg** une las fotos con el audio en un MP4, y después lo uso para medir:

```bash
npx hyperframes render -q delivery -o renders/mi-reel.mp4
ffmpeg -i renders/mi-reel.mp4 -filter_complex ebur128=peak=true -f null -   # sonoridad y pico real
ffmpeg -i renders/mi-reel.mp4 -vf blackdetect=d=0.05 -an -f null -          # fotogramas negros
```

Mis objetivos: **entre −13 y −14 LUFS**, pico real **por debajo de −2 dBTP**, ningún fotograma negro y Whisper entendiendo todas las frases sobre la mezcla final. El reel de esta guía salió a −13,9 LUFS y −2,8 dBTP, sin masterizar.

## Paso 7 · Cada error se convierte en una regla

![Paso 7: las correcciones](/blog/141126-asi-hago-mis-reels-con-ia/paso-7-correcciones-es.webp)

Esta es la parte que hace que el sistema mejore. En el `CLAUDE.md` del proyecto hay una sección **«Correcciones»**: cada vez que corrijo algo, Claude Code lo apunta con la fecha y la regla tal como la dije, **antes de seguir**. Si vale para siempre, también cambia la skill o la plantilla.

Ya van 17. Algunas:

- El primer vídeo salió en horizontal y sin voz → **vertical 9:16 y con narración**.
- El logo quedaba debajo de la cabecera de Instagram → **zona segura medida**.
- «Inicias muy flojo» → **el gancho es una pregunta sorprendente**, con algo grande en pantalla en esa palabra.
- La voz sonaba a cortes → **una sola toma**.

El siguiente vídeo ya no repite el error. Por eso cada reel me cuesta menos que el anterior.

## La skill completa (cópiala y hazla tuya)

![Tu turno: la skill y el prompt](/blog/141126-asi-hago-mis-reels-con-ia/tu-skill-es.webp)

Esta es una versión genérica de mi skill. Cambia todo lo que está entre `{{llaves}}` y guárdala en `~/.claude/skills/video-tu-canal/SKILL.md`. Después, en Claude Code, escribe `/video-tu-canal` y el tema.

````markdown
---
name: video-{{tu-canal}}
description: Hace un reel vertical (9:16, 60 s, con voz) para {{@tu-cuenta}} sobre {{tus temas}}, con HyperFrames, voz de ElevenLabs y comprobación con Whisper. Úsala cuando pida un reel o escriba /video-{{tu-canal}}.
---

# Reel · {{@tu-cuenta}}

Todo vive en `{{ruta/de/tu/proyecto}}`. Antes de tocar nada, lee el `CLAUDE.md` del proyecto (sobre todo «Correcciones») y carga la skill `/hyperframes`.

## El canal
- Cuenta: {{@tu-cuenta}} · Plataforma: {{Instagram Reels / TikTok / YouTube Shorts}}.
- Temas: {{3 a 6 temas}}. Público: {{a quién le hablas}}.
- Tono: {{de tú, frases cortas, cercano…}}. Nunca: {{lo que no quieres ver}}.
- Cierre (voz y tarjeta final): «{{Sígueme para más…}}» y solo {{@tu-cuenta}}.

## Estilo
- Formato: 1080 × 1920, 30 fps, 60 s.
- Colores: fondo {{#hex}}, acento {{#hex}} (solo para lo importante), texto {{#hex}}. El rojo, solo para errores.
- Fuentes: {{fuente de títulos}} y {{fuente de etiquetas}}.
- Zona segura de {{tu plataforma}}: todo el texto en x 100–980, y 222–1660 (y x ≤ 900 por debajo de y 1280). Mídela en una captura de un vídeo publicado en tu cuenta y revísala antes de renderizar.
- Logos y productos reales, de su fuente: nunca redibujados.

## Datos
- Solo fuentes primarias (documentación oficial, notas de prensa, papers). Anota la fecha en que lo compruebas.
- Superlativos («el primero», «el más…»): crúzalos con varias fuentes o matízalos en la voz.
- El código que salga en pantalla tiene que funcionar: pruébalo antes.

## Voz
- ElevenLabs, voz {{nombre o ID}} ({{prediseñada / clonada}}), modelo eleven_multilingual_v2, velocidad {{1.1}}.
- La clave va solo en la variable ELEVENLABS_API_KEY: nunca en un archivo ni impresa.
- Una sola toma: todo el guion en una llamada (con tiempos por palabra) y después se corta por frases en los silencios. Frase a frase suena a cortes.
- Cifras en letra en el texto que se lee; en pantalla, en número.
- Lo que la voz lee mal se escribe como suena ({{ej.: «efe efe eme peg» para FFmpeg}}); en pantalla va la forma correcta.
- Comprueba cada frase con Whisper (modelo small, idioma {{es}}) y otra vez sobre la mezcla final.

## Paso a paso
1. Historia. Gancho en los 3 primeros segundos: una pregunta sorprendente sobre lo que se ve, con algo grande en pantalla en su palabra clave. Promesa corta. Capítulos de 4 a 6 s que giran («pero…», «hasta que…»). Un dato con número. Remate que vuelve al gancho. Cierre. Propón 3 historias distintas, con esquema por segundos y los datos ya comprobados, y deja que elija.
2. Datos, con fuente y fecha, en SPEC.md.
3. Proyecto en videos/<nombre>/ (cada versión en su carpeta: -v2, -v3…). Si hay plantilla, cópiala; si no, npx hyperframes init.
4. Guion: unas 150 palabras, contado con conectores, no como lista. La última frase es el cierre.
5. Voz en una toma y Whisper. Mira la duración: la voz acaba antes del segundo 57.
6. Capas a partir de los tiempos de la voz: subtítulos palabra a palabra (abajo, la palabra clave en una pastilla de color), capítulos, notas, cifras que caen dígito a dígito y sellos para logros y errores.
7. Mundo 3D (opcional, Three.js): el protagonista, de verdad; algo nuevo en pantalla cada ~0,2 s.
8. Sonido: música con licencia que baja bajo la voz; un efecto por cada acción visible, más bajo si cae encima de la voz.
9. Revisión: npx hyperframes check con 0 errores y capturas con la zona segura encima.
10. Vista previa abierta en el navegador antes de renderizar.
11. Render con -q delivery y medidas: 1800 fotogramas, −13 a −14 LUFS, pico real ≤ −2 dBTP, sin fotogramas negros, Whisper sobre la mezcla.
12. REVIEW.md: qué se midió, qué no y lo más flojo.
13. Correcciones: cada vez que te corrija algo, añádelo con fecha a «Correcciones» de CLAUDE.md antes de seguir y, si vale para siempre, cámbialo también aquí.

## Antes de entregar, comprueba
- [ ] 0 errores en check y todo el texto dentro de la zona segura.
- [ ] La voz acaba antes del segundo 57 y la tarjeta final dice el cierre.
- [ ] Datos con fuente y fecha; superlativos cruzados.
- [ ] La clave no está en ningún archivo.
- [ ] Pide escucharlo con auriculares.
````

<aside class="promo-mentor not-prose" aria-label="Mentoría con Oscar Barajas">
<p class="promo-mentor__eyebrow">Mentoría · @gndx</p>
<p class="promo-mentor__title">Compra la carpeta con todos mis aprendizajes</p>
<div class="promo-mentor__options">
<p class="promo-mentor__option"><span class="promo-mentor__price">$1,99 USD</span><span class="promo-mentor__detail">Solo la carpeta</span></p>
<p class="promo-mentor__option promo-mentor__option--featured"><span class="promo-mentor__price">$20 USD</span><span class="promo-mentor__detail">La carpeta + mentoría y seguimiento de tu proyecto</span></p>
</div>
<a class="promo-mentor__cta" href="https://mentor.gndx.dev/" target="_blank" rel="noopener">Ir a mentor.gndx.dev <span aria-hidden="true">→</span></a>
</aside>

## El prompt para adaptarla a ti

Pega esto en Claude Code (o en tu chat de IA favorito) seguido de tu skill. Te va a entrevistar, la va a reescribir para tu canal y la va a mejorar cada vez que le digas qué no te gustó de un vídeo:

```text
Eres experto en skills de Claude Code y en vídeo corto para redes.
Abajo te pego mi SKILL.md. Quiero adaptarla a mi canal y mejorarla.

1. Léela entera y resúmeme en 5 líneas qué hace, qué herramientas supone (Claude Code, HyperFrames, ElevenLabs, Whisper, FFmpeg) y qué partes son de ejemplo (lo que está entre {{llaves}}).
2. Entrevístame con una pregunta cada vez (máximo 12): plataforma y formato, mi cuenta y mi público, temas, tono y cómo hablo, colores y fuentes de mi marca, voz (prediseñada o clonada, velocidad), frase de cierre, de dónde saco los datos, lo que nunca quiero ver, qué tengo instalado y dónde está mi proyecto.
3. Con mis respuestas, reescribe la skill completa: misma estructura (encabezado, El canal, Estilo, Datos, Voz, Paso a paso, Antes de entregar), sin ninguna {{llave}} y sin lo que no aplique a mí. Escribe la descripción del encabezado para que Claude Code sepa cuándo usarla.
4. Dime 3 riesgos o huecos que veas (por ejemplo: la zona segura de mi plataforma, los derechos de la música, datos sin fuente, la clave de la API) y cómo los cubre la skill.
5. A partir de ahora, cada vez que te diga qué no me gustó de un vídeo, propón el cambio exacto en la skill (antes → después) y añádelo a una sección «Correcciones» con la fecha.

No inventes nada sobre mí: si no lo sabes, pregúntame.

--- MI SKILL.md ---
(pega aquí tu skill)
```

## Para terminar

Lo que más me sorprendió no fue la IA haciendo vídeos: fue que **el sistema aprende de mis correcciones**. Una frase, una skill y un registro de errores. El resto es repetir, corregir y apuntar.

Si haces tu propia versión, enséñamela: estoy como **@gndx** en Instagram y en YouTube. Y si quieres ver el reel que explica esta guía en 60 segundos, está en mi perfil.
