from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def main():
    segmentInput = int(input("Enter Segment Lengths in Seconds (Ex. 1 minute = 60): "))
    splitVideo(segmentInput)

def splitVideo(segment):
    timeSheetList = getTimeSheet(segment)

    i = 0
    for time in timeSheetList:
        starttime = int(time.split("-")[0])
        endtime = int(time.split("-")[1])
        ffmpeg_extract_subclip(getVideoPath(), starttime, endtime,
                               targetname="SplitVideos/" + (str((i + 1)) + ".mp4"))
        i += 1

def getVideoPath():
    return "UnsplitVideo/unsplit.mp4"

def getVideoCount(segment):
    vidDuration = VideoFileClip(getVideoPath()).duration
    vidCal = (int(vidDuration) / segment)
    return vidCal

def getTimeSheet(segment):
    newTimeSheet = []
    start = 0
    end = segment
    for i in range(int(getVideoCount(segment))):
        newTimeSheet.append(f"{start}-{end}")
        start += segment
        end += segment
    return newTimeSheet


if __name__ == "__main__":
    main()

