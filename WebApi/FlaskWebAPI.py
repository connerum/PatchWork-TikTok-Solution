import flask
from flask import request, send_file, render_template
import pyttsx3
import praw
from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import YouTube
from moviepy.editor import VideoFileClip

engine = pyttsx3.init()
user_agent = "TikTokSaaS"

# Create an instance of reddit class
reddit = praw.Reddit(username="Objective_Ad7158",
                     password="Ferbiscool2!",
                     client_id="oTWvTeP37ydTpslHTUDRZQ",
                     client_secret="0-8gGOzvYqiQylNjBKqPZf5Vio_7eg",
                     user_agent=user_agent
                     )

# Setup Text to Speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 198)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

app = flask.Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        reddit = request.form.get("reddit")
        yt = request.form.get("yt")
        storyGrabber(reddit)
        saveVideo(yt)
        makeVideo()
        uploadVid = send_file("Upload.mp4", as_attachment=True)
        return uploadVid
    return render_template("index.html")


def storyGrabber(urlInput):
    submission = reddit.submission(
        url=urlInput)
    text = submission.selftext
    saveVoice(text)


def saveVoice(text):
    engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()


def saveVideo(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject.download(filename='video.mp4')


def makeVideo():
    videoclip = VideoFileClip("video.mp4")
    new_clip = videoclip.without_audio()
    audio = AudioFileClip("speech.mp3")
    video_with_new_audio = new_clip.set_audio(audio)
    video_with_new_audio = video_with_new_audio.loop(duration=audio.duration)
    video_with_new_audio.write_videofile("Upload.mp4", fps=30, audio_codec="aac", audio_bitrate="192k")
    video_with_new_audio.close()


app.run()
