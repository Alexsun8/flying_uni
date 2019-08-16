from django.shortcuts import render
from core.models import Course
from django.shortcuts import render_to_response

# Create your views here.

def index_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'index.html', context={"courses": courses})


def home_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'home.html', {'main': 'idea'})


def idea_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'idea/idea.html', {'main': 'home'})