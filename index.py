from pytube import YouTube

link = input("Paste a link from Youtube")
video = YouTube(link)
quality = input("Choose the quality of the video (High/Low: " )

if quality == "High":
  output = video.streams.get_highest_resolution()
if quality =="Low":
  output = video.streams.get_lowest_resolution()
  