from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def index(request):
    index_dictionary = {
        'title': 'Головна сторінка',
    }
    return render(request, 'blog/index.html', index_dictionary)

def about(request):
    variety_of_tea = {
        'teas': [
            'Зелений чай',
            'Чорний чай',
            'Білий чай',
            'Червоний чай',
            'Травяний чай'
        ]
    }
    return render(request, 'blog/about.html', variety_of_tea)
