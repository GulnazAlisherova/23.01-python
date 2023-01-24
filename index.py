from pytube import YouTube

link = input("Paste a link from Youtube")
video = YouTube(link)
quality = input("Choose the quality of the video (High/Low: " )