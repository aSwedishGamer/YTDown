from pytube import YouTube

link = input("Link: ")
location = input("Location: ")
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()
yd.download(location)
