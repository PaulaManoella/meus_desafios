from pytube import YouTube

url = input("cade o link")
video = YouTube(url)

video.streams.get_lowest_resolution().download()