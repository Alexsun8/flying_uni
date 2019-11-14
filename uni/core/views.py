import profile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.db import transaction
# from django.http import request
from django.shortcuts import render, redirect
from django.views import View

from core.models import Course, News, Location, President


# Cre   ate your views here.


def index_view(request):
    count = Course.objects.filter(status='done').count()
    courses = Course.objects.all()
    # if request.method == 'POST':
    return render(request, 'index.html', locals())


# class idea_view(LoginRequiredMixin, View):
def idea_view(request):
    count = Course.objects.filter(status='done').count()
    # if request.method == 'POST':
    # if self.request.user.is_staff:
    #     return render(request, 'idea/idea.html', {'main': 'home'}, {'log' : 'my profile'}, param = 'profile.html')
    # return render(request, 'idea/idea.html', {'main': 'home'}, {'log' : 'log in'}, param = 'login.html')
    return render(request, 'idea.html', locals())
    # def get(request, self):
    #     main = 'home'
    #     if self.request.user.is_staff:
    #         log = "my profile"
    #         return render(request, 'idea/idea.html', locals())
    #     log = 'log in'
    #     return render(request, "idea/idea.html", locals())


def home_view(request):
    count = Course.objects.filter(status='done').count()
    news = News.objects.all()
    # var = {'main': 'idea'}
    return render(request, 'home.html', locals())

# class Offer_news(LoginRequiredMixin, home_view):
#     model = News.objects.all()
#     def get_quaryset(self):
#         if self.request.user.is_staff:
#             return render(request, add_new)

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect('settings:profile')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#
#     return render(request, 'profiles/edit.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
