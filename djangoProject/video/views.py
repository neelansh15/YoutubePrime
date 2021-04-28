# from django.shortcuts import render
# from .models import Video

# # Create your views here.
# def index(request):
#     video=Video.objects.all()
#     return render(request,"index.html",{"video":video})

from rest_framework.response import response
from rest_framework import generics
from . models import Video
from . serializers import VideoSerializer

class VideoView(generics.RetrieveAPIView):
    video=Video.object.all()

    def get(self,request,*args,**kwargs):
        video=self.get_video()
        serializer=VideoSerializer(video,many=TRUE)
        return response(serializer.data)