from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=FplJcMLsmfE&ab_channel=LinYuC')
print(yt.title)
#print(yt.streams.all()) #查看視訊全部檔案格式
#yt.streams.filter(resolution="480p" ).all()
yt.streams.filter(resolution="720p", video_codec="vp9")[0]
#yt.streams.filter(resolution="720p").first()

