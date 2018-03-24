from pytube import YouTube
import shutil
import os
import fnmatch
import moviepy.editor as mp
import imageio
imageio.plugins.ffmpeg.download()


def move_file(filename):
    shutil.copy(filename, "C://Users/tonym/Desktop/Videos")
    os.unlink(filename)


def files_downloaded():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.mp4'):
            return file


def download_video(url):
    YouTube(url).streams.first().download()
    move_file(files_downloaded())


def download_audio(url):
    YouTube(url).streams.first().download()
    move_file(files_downloaded())
    for file in os.listdir('C://Users/tonym/Desktop/Videos/'):
        if fnmatch.fnmatch(file, '*.mp4'):
            file
    clip = mp.VideoFileClip("C://Users/tonym/Desktop/Videos/"+ str(file)).subclip(0, 20)
    clip.audio.write_audiofile("audio.mp3")


URL = ""
#download_video(URL)
download_audio(URL)

