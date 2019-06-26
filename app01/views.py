from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from app01.models import Img,Video,Background_img
# Create your views here.
from .models import Actor
# Create your views here.
def index(request):
    actor_obj=Actor.objects.filter(id=2)
    print(type(actor_obj))
    for u in actor_obj:
        print(u.actor_name)
        
        print(u.actor_occupation)
        imgs=Img.objects.filter(img_actor_id=u.id)
        videos=Video.objects.filter(video_actor_id=u.id)
        Backgrounds=Background_img.objects.filter(Background_actor_id=u.id)
    for i in imgs:
        print(i.address)
    content={
         'imgs':imgs,
         "videos":videos,
         "actors":actor_obj,
         "Backgrounds":Backgrounds,
        }
    
    return render(request,"index.html",content)


