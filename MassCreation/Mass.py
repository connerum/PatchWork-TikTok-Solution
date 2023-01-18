import pyttsx3
import praw
from moviepy.audio.io.AudioFileClip import AudioFileClip
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

# Setup for Text to Speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 195)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def main():
    makeStories()


def makeStories():
    f = open('links.txt', 'r')
    title = 1
    for line in f:
        storyGrabber(line, title)
        title += 1


def storyGrabber(link, title):
    submission = reddit.submission(
        url=link)
    text = submission.selftext
    saveVoice(text, title)


def saveVoice(text, title):
    engine.save_to_file(text, "ttsAudio/" + (str(title) + '.mp3'))
    engine.runAndWait()
    makeVideo(title)


def makeVideo(title):
    videoclip = VideoFileClip("uneditedVideos/" + str(title) + ".mp4")
    new_clip = videoclip.without_audio()
    audio = AudioFileClip("ttsAudio/" + str(title) + ".mp3")
    video_with_new_audio = new_clip.set_audio(audio)
    video_with_new_audio = video_with_new_audio.loop(duration=audio.duration)
    video_with_new_audio.write_videofile("stories/" + "Story" + str(title) + ".mp4",
                                         fps=60, audio_codec="aac", audio_bitrate="160k")
    video_with_new_audio.close()


if __name__ == "__main__":
    main()

