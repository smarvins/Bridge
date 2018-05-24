from django.shortcuts import render, redirect
from .models import app,Comment,profile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .import forms


# Create your views here.

@login_required(login_url='/accounts/login/')
def timeline(request):
    posts = app.objects.all().order_by('date');
    postcomment = Comment.objects.all().order_by('post_on');
    return render(request,'timeline.html',{'posts':posts})
    return render(request,'timeline.html',{'postcomment':postcomment})

###########################################################################

def profile(request):
    profile = profile.objects.all().order_by('date');
    return render(request,'profile.html', {'profile':profile})

###########################################################################

def search(request):
    return render(request,'search.html')

###########################################################################

def home(request):
    return render(request,'home.html')

###########################################################################


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:timeline')
    else:
      form = UserCreationForm()
    return render(request,'home.html', { 'form': form })

###########################################################################

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
               return redirect(request.POST.get('next'))
            else:
               return redirect('app:timeline')
    else:
      form = AuthenticationForm()
    return render(request,'home.html', { 'form': form })

###########################################################################

def logout(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'home.html')

###########################################################################

@login_required(login_url="home")
def newpost(request):
    if request.method == 'POST':
        form = forms.newpost(request.POST, request.newpost)
        if form.is_valid():
            return redirect('profile.htnl')
    else:
        form = forms.newpost()

    return render(request,'profile.html', )
