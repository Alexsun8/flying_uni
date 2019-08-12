from django.shortcuts import render
from core.models import Course


# Create your views here.

def index_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'index.html', context={"courses": courses})


def home_view(request):
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'home.html', context={"courses": courses})
