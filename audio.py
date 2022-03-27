import pytube
import os

while True:
    url = input("Enter URL: ")
    print("Please Wait For Video To Download...")
    get_video = pytube.YouTube(url)
    streams = get_video.streams.filter(only_audio=True).first()
    print(streams.url)
    name = streams.download()
    name = name.strip(".mp4")
    os.rename(f"{name}.mp4", f"{name}.mp3")
    print("Download Complete!")
