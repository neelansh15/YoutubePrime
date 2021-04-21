from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import createUserForm

# Create your views here.
def index(request):
    return HttpResponse('<h1>Index</h1>')

def home(request):
    return HttpResponse('<h1>Hello there</h1>')

def login(request):
    return render(request, 'Accounts/login.html')

@csrf_exempt
def register(request):
    form = createUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
    context={"form": form}
    return render(request, 'Accounts/register.html', context)

