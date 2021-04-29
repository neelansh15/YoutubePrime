from django.shortcuts import render
from django.conf import settings
from django.contrib import auth

# Create your views here.
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer


from rest_framework.permissions import IsAuthenticated
class PostView(generics.RetrieveAPIView):
    # this is so that users can access the api without log in 
    permission_classes = (IsAuthenticated, )


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer







# https://stackoverflow.com/questions/50405425/django-jwt-get-user-info#:~:text=You%20can%20simply%20create%20a,id%2C%20...%20%7D%20%7D


