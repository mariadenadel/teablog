from django.shortcuts import render

# Create your views here.

def teanews_home(request):
    return render(request, 'teanews/teanews_home.html')