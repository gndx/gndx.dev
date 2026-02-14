---
title: 'Create Subtitles on YouTube VIDEOS with WHISPER'
description: 'Learn how to use Whisper, OpenAI''s free Artificial Intelligence to transcribe the audio of any YouTube video from a Python script and from your computer.'
pubDate: '2024-04-11T02:28:42.232Z'
heroImage: 'https://s3.amazonaws.com/gndx.dev/subtitulos-de-videos-de-youtube.png'
categories:
  - 'youtube'
authors:
  - 'gndx'
tags:
  - 'python'
  - 'scripts'
  - 'youtube'
---


Learn how to use Whisper, the free Artificial Intelligence from OpenAI, to transcribe the audio of any YouTube video from a Python script and from your computer.

### Create Subtitles on YouTube VIDEOS with WHISPER

As a content creator, we face many tasks in making a video. One of them is to create the video subtitles. There are multiple tools, both free and paid. Some video editors even include the possibility of creating these subtitles in their paid version.

### How to create subtitles for your videos for FREE?

First, we are going to use Whisper, OpenAI's AI that allows us to convert any audio to text. With the same library, we can create subtitles in the "SRT" format. Simply put, an SRT (SubRip Subtitle) is the most popular subtitle file format for video content and is what YouTube uses to load subtitles on each video.

Before starting, I want to share a video where we created a Python script that allows us to use Whisper from our computers to convert audio to text. If you are already experienced, you can skip the video and go directly to the code.

[Download youTubeTranscribe on GitHub](https://github.com/gndx/youTubeTranscribe).

Once downloaded, we have the following code:

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

What it does is use the pytube library to download the audio from a YouTube video and pass it through the Whisper model, creating a txt file with the audio content of the video.

Now, what we want is for this same file to have the SRT format and the format timestamps.

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

This new script has a utility that allows us to create this SRT format and timestamps, and upload it directly to YouTube. If you analyze the code, you can see that the `get_writer` function has been added on lines 92 and 93, and a reference to the file output on line 76.

All you have to do is run the script with the following command:

```bash
python src/main.py <youtube_video_url>
```

This process may take a couple of minutes, but the result will be a file in SRT format with the timestamps and audio content of the video, and another file in TXT format.

### How to translate the Subtitles of your Videos?

If you want to translate the subtitles of your videos, you can use from Google Translate to tools like subtitlestranslator.com, and in this way, add multiple languages ​​to the translations of your video.

With these steps, you can create subtitles for your YouTube videos for free and from your computer.
