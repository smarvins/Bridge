from django.shortcuts import render
from .models import app
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def timeline(request):
    posts = app.objects.all().order_by('date');
    return render(request,'timeline.html',{'posts':posts})

def profile(request):
    return render(request,'profile.html')

def search(request):
    return render(request,'search.html')

def home(request):
    return render(request,'home.html')

def signup(request):
    form = UserCreationForm()
    return render(request,'home.html', { 'form': form })
