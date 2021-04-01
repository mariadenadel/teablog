from django.shortcuts import render
from .models import Article

# Create your views here.

def teanews_home(request):
    news = Article.objects.order_by('-created_at')
    return render(request, 'teanews/teanews_home.html', {'news':news})