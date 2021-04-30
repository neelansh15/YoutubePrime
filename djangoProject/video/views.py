from django.shortcuts import render
from . models import Video
from rest_framework.response import Response
from . serializer import VideoSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FileUploadParser

# Create your views here.
def index(request):
    video=Video.objects.all()
    return render(request,"index.html",{"video":video})

class VideoView(generics.RetrieveAPIView):
    
    queryset = Video.objects.all()
    

    def get(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=VideoSerializer(queryset,many=True)
        return Response(serializer.data)
    
# class VideoView(APIView):
#     parser_class = (FileUploadParser, MultiPartParser,)

#     def post(self, request, *args, **kwargs):

#       video_serializer = VideoSerializer(data=request.data)

#       if video_serializer.is_valid():
#           video_serializer.save()
#           return Response(video_serializer.data, status=status.HTTP_201_CREATED)
#       else:
#           return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

