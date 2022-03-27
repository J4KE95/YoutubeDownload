import pytube
import time

def downloader () :
    print("Please Wait For Video To Download...")
    get_video = pytube.YouTube(url)
    streams = get_video.streams.first()
    streams.download()
    print("Download Complete!")
    print("Downloads Can Be Found In The YoutubeDownload Folder.")

def converter () :
    print("Please Wait For Video To Download...")
    get_video = pytube.YouTube(url)
    streams = get_video.streams.filter(only_audio=True).first()
    print(streams.url)
    streams.download()
    print("Download Complete!")
    print("Downloads Can Be Found In The Folder Where The main.py File Is Stored.")

print("Welcome To YoutubeDownload!")
url = input("Please Paste Link To Youtube Video: ")

def select () :
    print(f"You Have Selected: {pytube.YouTube(url).title}")
    print("Press 1 To Download Youtube Video")
    print("Press 2 To Convert Youtube Video To Audio Format And Download")
    selection = input("Please Choose An Option: ")
    if selection == "1" :
        downloader()
    elif selection == "2" :
        converter()
    else :
        print("Invalid Selection!")
        select()
select()
