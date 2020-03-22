#!/usr/bin/python
from pytube import YouTube
# YouTube('https://www.youtube.com/watch?v=Y-8wCNh3fOs&list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX&index=4').streams.filter(res='720p').first().download()
# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# yt.streams.filter(progressive=True, file_extension='mp4', res='720p').order_by('resolution').desc().first().download()
variation = YouTube('https://www.youtube.com/watch?v=Y-8wCNh3fOs&list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX&index=4')
hightqulity = variation.streams.filter(res='1080p')
hightqulity.first().download()
