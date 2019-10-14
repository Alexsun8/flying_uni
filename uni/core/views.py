from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import render, redirect

from core.models import Course, News, Location, President


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
    return render(request, 'home.html', locals())

