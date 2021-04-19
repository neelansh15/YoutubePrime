from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Index</h1>')

def home(request):
    return HttpResponse('<h1>Hello there</h1>')

