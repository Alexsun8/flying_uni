from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

from uni.blog.forms import UserForm, ProfileForm
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
    return render(request, 'home.html', locals())


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
