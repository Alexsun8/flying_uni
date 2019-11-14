from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from account.admin import UserAdmin, ProfileInline
from account.models import Profile


# # Create your views here.
# def log_view(request):
#     return render(request, 'log.html')
#
#


# @login_required
# def register_view(request):
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return render(request, 'sign_up.html', {'new_user': new_user})
#     else:
#         user_form = UserCreationForm()
#     return render(request, 'sign_up.html', {'user_form': user_form})


class UserForm(object):
    pass


def register_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserAdmin(data=request.POST)
        # profile_form = ProfileInline(data=request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # if 'profile_pic' in request.FILES:
                # print('found it')
                # profile.profile_pic = request.FILES['profile_pic']
            # profile.save()
            registered = True
        else:
            # print(user_form.errors,profile_form.errors)
            print(user_form.errors)
    else:
        user_form = UserAdmin()
        # profile_form = ProfileInline()
    return render(request,'sign_up.html',
                          {'user_form':user_form,
                           # 'profile_form':profile_form,
                           'registered':registered})


# # user profile form
# @login_required
# def register_profile(request):
#     profile = Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = Profile(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return index(request)
#         else:
#             print form.errors
#     else:
#         form = UserProfileForm()
#     return render(request, 'howdidu/register_profile.html', {'form': form})

# profile page using user name as url
@login_required
def profile_view(request, UserAdmin):
    user = get_object_or_404(UserAdmin, profile=UserAdmin)
    return render(request, 'profile.html', {'profile': UserAdmin})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
