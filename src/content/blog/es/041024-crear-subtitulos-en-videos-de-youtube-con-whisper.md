---
title: "Crear Subtítulos en VIDEOS de YouTube con WHISPER"
description: "Aprende a usar Whisper, la Inteligencia Artificial gratuita y libre de OpenAI para transcribir el audio de cualquier video de YouTube desde un script en Python y desde tu computadora."
pubDate: "2024-04-11T02:28:42.232Z"
heroImage: "https://s3.amazonaws.com/gndx.dev/subtitulos-de-videos-de-youtube.png"
categories: ["youtube"]
authors: ["gndx"]
tags: ["python", "scripts", "youtube"]
---

Aprende a usar Whisper, la Inteligencia Artificial gratuita y libre de OpenAI, para transcribir el audio de cualquier vídeo de YouTube desde un script en Python y desde tu computadora.

### Crear Subtítulos en VIDEOS de YouTube con WHISPER

Como creador de contenido, nos enfrentamos a muchas tareas en la realización de un vídeo. Una de ellas es crear los subtítulos del vídeo. Existen múltiples herramientas, tanto gratuitas como de pago. Incluso algunos editores de vídeo incluyen en su versión de pago la posibilidad de crear estos subtítulos.

### ¿Cómo crear subtítulos de tus vídeos GRATIS?

Primero, vamos a utilizar Whisper, la IA de OpenAI que nos permite convertir cualquier audio a texto. Con la misma librería, podemos crear subtítulos en el formato "SRT". En simples palabras, un SRT (SubRip Subtitle) es el formato de archivo de subtítulos más popular para contenido de vídeo y es el que utiliza YouTube para cargar subtítulos en cada vídeo.

Antes de comenzar, quiero compartir un vídeo donde creamos un script en Python que permite utilizar Whisper desde nuestras computadoras para convertir de audio a texto. Si ya tienes experiencia, puedes omitir el vídeo y pasar directamente al código.

[Descargar youTubeTranscribe en GitHub](https://github.com/gndx/youTubeTranscribe).

Una vez descargado, tenemos el siguiente código:

```python
import sys
import pytube as pt
import whisper
import datetime

def download_and_transcribe_youtube_video(video_url):
    model = whisper.load_model("large")

    date_now = datetime.datetime.now()
    date_format = "%Y-%m-%d_%H-%M-%S"
    date_string = date_now.strftime(date_format)

    yt = pt.YouTube(video_url)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename="audio_spanish.mp3")

    result = model.transcribe("audio_spanish.mp3", fp16=False)

    file_name = f"file_{date_string}.txt"

    with open(file_name, "w") as file:
        file.write(result["text"])
    print(result["text"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_video_url>")
        sys.exit(1)

    youtube_video_url = sys.argv[1]
    download_and_transcribe_youtube_video(youtube_video_url)
```

Lo que realiza es utilizar la librería pytube para descargar el audio de un vídeo de YouTube y pasarlo por el modelo de Whisper, creando un archivo en txt con el contenido del audio del vídeo.

Ahora, lo que queremos es que este mismo archivo tenga el formato de SRT y las marcas de tiempo del formato.

```python
import sys
import pytube as pt
import whisper
from whisper.utils import get_writer
import datetime

def download_and_transcribe_youtube_video(video_url):
    model = whisper.load_model("large")

    output_directory = "./output"
    date_now = datetime.datetime.now()
    date_format = "%Y-%m-%d_%H-%M-%S"
    date_string = date_now.strftime(date_format)

    yt = pt.YouTube(video_url)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename=f"audio_{date_string}.mp3")

    result = model.transcribe(f"audio_{date_string}.mp3", fp16=False)

    file_name = f"file_{date_string}.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(result["text"])

    txt_writer = get_writer("srt", output_directory)
    txt_writer(result, f"audio_{date_string}.mp3")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_video_url>")
        sys.exit(1)

    youtube_video_url = sys.argv[1]
    download_and_transcribe_youtube_video(youtube_video_url)
```

Este nuevo script cuenta con una utilería que nos permite crear este formato SRT y las marcas de tiempo, y poder subirlo directamente a YouTube. Si analizas el código, puedes apreciar que se ha agregado la función `get_writer` en la línea 92 y 93, y una referencia al output del archivo en la línea 76.

Lo único que tienes que hacer es ejecutar el script con el siguiente comando:

```bash
python src/main.py <youtube_video_url>
```

Este proceso puede tardar un par de minutos, pero el resultado será un archivo en formato SRT con las marcas de tiempo y el contenido del audio del vídeo, y otro archivo en formato TXT.

### ¿Cómo traducir los Subtítulos de tus Vídeos?

Si deseas traducir los subtítulos de tus vídeos, puedes utilizar desde Google Translate hasta herramientas como subtitlestranslator.com, y de esta forma, agregar múltiples idiomas a las traducciones de tu vídeo.

Con estos pasos, podrás crear subtítulos para tus vídeos de YouTube de forma gratuita y desde tu computadora.