from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, News


# Cre   ate your views here.


def index_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'index.html', {'main': 'home'})


def idea_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'idea/idea.html', {'main': 'home'})


def home_view(request):
    news = News.objects.all()
    {'main': 'idea'}
    return render(request, 'home.html',  locals())
