from django.shortcuts import render

# Create your views here.
def timeline(request):
    return render(request,'timeline.html')

def profile(request):
    return render(request,'profile.html')
