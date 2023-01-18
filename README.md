
# PatchWork TikTok Content Creator

This Python project is designed to split large videos into smaller segments, scrape and convert Reddit stories into text-to-speech audio files, download YouTube videos, and add the Reddit story audio to a video file. Additionally, the project includes separate code to function as a WebAPI, allowing for easy integration with other platforms and applications. With this project, users can easily manage and manipulate their video and audio files to easily and quickly upload to TikTok.




## Authors

- [@connerum](https://github.com/connerum)


## Features
**Mass Creation**
- Load user-selected Reddit URLs from a text file and generate text-to-speech audio files in bulk.
- Load user-selected videos and replace their original audio with the generated text-to-speech audio files.


**Splitter**
- Easily split large videos into multiple shorter segments.


**Cropper**
- Center and crop videos to fit TikTok's dimensions.


**Web API**
- Use Flask to run a basic HTML page where users can enter a Reddit post URL and YouTube video URL.
- The audio and video files will be downloaded, and a text-to-speech audio file will be generated.
- The audio file will then be added to the downloaded video.


## Installation

**Best used in an IDE such as PyCharm**

```bash
  git clone https://github.com/connerum/AllinOneSaaS.git
  cd AllinOneSaaS
  pip3 install -r requirements.txt
```
    
