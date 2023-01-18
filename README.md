
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
- **COMING SOON** <!-- Center and crop videos to fit TikTok's dimensions. -->

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
    
## Usage

### **Mass Creation**

- **Video file names need to be in increments of 1**
    - Ex. You have 4 videos they would be named the following:
        - **Video File Names:** *1.mp4*, *2.mp4*, *3.mp4*, *4.mp4*
- Reddit URLs **need** to be placed in the file **"links.txt"**
- Video files **need** to be placed in the directory **"uneditedVideos"**

After verifying that these steps are followed, run the **"Mass.py"** script & the mass creation of videos will begin

- The generated Text-to-Speech audio files will be saved to the directory **"ttsAudio"**
- The completed videos will be saved to the directory **"stories"**


### **Splitter**
- Place your uncut video file in the directory **"UnsplitVideo"**
- Edit the **"times.txt"** file with the segments you want your video to be cut into
    - You must write these segments as **seconds**
    - Ex. To cut a 3-minute video into three one-minute videos, you would put the following lines in **"times.txt"**:
        - 0-60
        - 60-120
        - 120-180

After verifying that these steps are followed, run the **"Splitter.py"** script & the splitting of your video will begin

- The split videos are saved in the **"SplitVideos"** directory


### **Web API**
- Run the script **"FlaskWebAPI.py"**
