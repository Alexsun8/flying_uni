import profile

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.checks import messages
from django.db import transaction
# from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404

from core.models import Course, News, Location, President


def course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course.html', {'course': course})

def index_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    courses = Course.objects.all()
    return render(request, 'index.html', locals())


def idea_view(request):
    count = Course.objects.filter(status='done').count()
    # if request.method == 'POST':
    # logout = request.POST.get('submit')
    # if logout:
    # logout(request)
    # active = False
    # return render(request, 'idea.html', locals())
    # logout = False
    user = request.user
    active = user.is_active
    return render(request, 'idea.html', locals())


def home_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    news = News.objects.all()
    # var = {'main': 'idea'}
    return render(request, 'home.html', locals())

# class Offer_news(LoginRequiredMixin, home_view):
#     model = News.objects.all()
#     def get_quaryset(self):
#         if self.request.user.is_staff:
#             return render(request, add_new)
