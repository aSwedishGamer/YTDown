from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)
print("Title:", yt.title)

fileSuccess = 0
while fileSuccess == 0:
    filetype = str(input("Filetype (mp4 or webm): "))
    if filetype == "mp4":
        fileSuccess = fileSuccess + 1
        filedown = yt.streams.get_highest_resolution()
    elif filetype == "webm":
        fileSuccess = fileSuccess + 1
        filedown = yt.streams.get_by_itag(251)
    else:
        print("Not one of the available filetypes(mp4 or webm), try again")

location = input("Download Location: ")

filedown.download(location)
