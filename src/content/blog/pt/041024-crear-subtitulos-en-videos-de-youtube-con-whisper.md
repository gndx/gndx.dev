---
title: 'Crie legendas em VÍDEOS do YouTube com WHISPER'
description: 'Aprenda a usar o Whisper, a Inteligência Artificial gratuita da OpenAI para transcrever o áudio de qualquer vídeo do YouTube a partir de um script Python e do seu computador.'
pubDate: '2024-04-11T02:28:42.232Z'
heroImage: 'https://s3.amazonaws.com/gndx.dev/subtitulos-de-videos-de-youtube.png'
categories:
  - 'YouTube'
authors:
  - 'gndx'
tags:
  - 'píton'
  - 'roteiros'
  - 'YouTube'
---


Aprenda a usar o Whisper, a Inteligência Artificial gratuita da OpenAI, para transcrever o áudio de qualquer vídeo do YouTube a partir de um script Python e do seu computador.

### Crie legendas em VÍDEOS do YouTube com WHISPER

Como criadores de conteúdo, enfrentamos muitas tarefas ao fazer um vídeo. Uma delas é criar as legendas do vídeo. Existem várias ferramentas, gratuitas e pagas. Alguns editores de vídeo incluem até a possibilidade de criar essas legendas em sua versão paga.

### Como criar legendas para seus vídeos GRATUITAMENTE?

Primeiro, usaremos o Whisper, a IA da OpenAI que nos permite converter qualquer áudio em texto. Com a mesma biblioteca podemos criar legendas no formato “SRT”. Simplificando, um SRT (SubRip Subtitle) é o formato de arquivo de legenda mais popular para conteúdo de vídeo e é o que o YouTube usa para carregar legendas em cada vídeo.

Antes de começar, quero compartilhar um vídeo onde criamos um script Python que nos permite usar o Whisper em nossos computadores para converter áudio em texto. Se você já tem experiência, pode pular o vídeo e ir direto para o código.

[Baixe o youTubeTransscribe no GitHub](https://github.com/gndx/youTubeTranscribe).

Depois de baixado, temos o seguinte código:

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

O que ele faz é utilizar a biblioteca pytube para baixar o áudio de um vídeo do YouTube e passá-lo pelo modelo Whisper, criando um arquivo txt com o conteúdo de áudio do vídeo.

Agora, o que queremos é que esse mesmo arquivo tenha o formato SRT e os timestamps do formato.

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

Este novo script possui um utilitário que nos permite criar esse formato SRT e carimbos de data e hora e enviá-los diretamente para o YouTube. Se você analisar o código, poderá ver que a função `get_writer` foi adicionada nas linhas 92 e 93, e uma referência à saída do arquivo na linha 76.

Tudo que você precisa fazer é executar o script com o seguinte comando:

```bash
python src/main.py <youtube_video_url>
```

Este processo pode demorar alguns minutos, mas o resultado será um arquivo em formato SRT com os carimbos de data e hora e conteúdo de áudio do vídeo, e outro arquivo em formato TXT.

### Como traduzir as legendas dos seus vídeos?

Se você deseja traduzir as legendas dos seus vídeos, você pode usar desde o Google Tradutor até ferramentas como subtitlestranslator.com, e desta forma, adicionar vários idiomas às traduções do seu vídeo.

Com essas etapas, você pode criar legendas para seus vídeos do YouTube gratuitamente e no seu computador.
