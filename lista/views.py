from django.shortcuts import render
from os import listdir
# Create your views here.


def index(request):
    videos = []
    
    for id in listdir('lista/static/lista/video'):
        data = open(r"C:/Users/Wojciech Janus/Documents/video_site/sesja_rady/lista/static/lista/video/"+ id + "/dane.txt", "r")
        
        videos.append({
        'id': id,
        'title': data.readline(),
        'link': r"C:/Users/Wojciech Janus/Documents/video_site/sesja_rady/lista/static/lista/video/"+ id + "/nagranie.mp4",
        'date': data.readline()
        })
        data.close()

    return render(request, 'lista/index.html',{
        'videos': videos
    })

def view_video(request, video_id):
    for id in listdir('lista/static/lista/video'):
        if id == video_id:
            data = open(r"C:/Users/Wojciech Janus/Documents/video_site/sesja_rady/lista/static/lista/video/"+ id + "/dane.txt", "r")
        
            selected_video = {
            'id': id,
            'title': data.readline(),
            'link': r"lista/video/"+ id + "/nagranie.mp4",
            'date': data.readline()
            }
            data.close()

    return render(request, 'lista/view_video.html', {
        'video_title': selected_video['title'],
        'video_link': selected_video['link'],
        'video_id': selected_video['id']
    })
