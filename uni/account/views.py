from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from account.forms import UserForm, ProfileForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import Group

# def register_view(request):
#     if request.method == "POST":
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             username = request.username
#             password = request.password
#             this_user = authenticate(request, username=username, password=password)
#             post = form.save(commit=False)
#             post.user = this_user
#             # post.user = request.User
#             post.user.username = request.user.username
#             post.bio = request.bio
#             post.wishes = request.wishes
#             post.knowledge = request.knowledge
#             post.contact = request.contact
#             post.birth_date = request.birth_date
#             post.photo = request.photo
#             post.save()
#             return redirect('profile', pk=post.pk)
#     else:
#         form = ProfileForm()
#     return render(request, 'sign_up.html', {'form': form})
#
from core.models import Course


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required()
def profile_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    if not user.is_authenticated:
        raise Http404("Ur not logim!")
    return render(request, 'profile.html', locals())


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            print("User is valid")
            if user.is_active:
                login(request, user)
                print("User is valid, active and authenticated")
                return redirect('/accounts/profile')
              # return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    count = Course.objects.filter(status='done').count()
    return render(request, 'logout.html', locals())


def register_view(request):
    logout(request)
    registered = False
    count = Course.objects.filter(status='done').count()
    if request.method == 'POST':
        print("wooooorks")
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print("bool prof:", profile_form.is_valid())
        print("bool us:", user_form.is_valid())
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # profile.birth_date = birth.save(commit=False)
            # if 'photo' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['photo']
            profile.save()
            group = Group.objects.get(name='Students')
            user.groups.add(group)
            registered = True
            login(request, user)
            return redirect('/accounts/profile', user=user)
            # return render(request, 'profile.html', locals())
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'sign_up.html',locals())

@login_required
def teach_profile_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    courses = Course.objects.all()
    title = "Список преподаваемых курсов"
    if not user.is_authenticated:
        raise Http404("Ur not logim!")
    courses = []
    for cou in Course.objects.all():
        if cou in user.profile.teaching.all():
            courses.append(cou)
    return render(request, 'index.html', locals())


@login_required
def stud_profile_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    stu = True
    courses = Course.objects.all()
    title = "Список изучаемых курсов"
    if not user.is_authenticated:
        raise Http404("Ur not logim!")
    courses = []
    for cou in Course.objects.all():
        if cou in user.profile.studying.all():
            courses.append(cou)
    return render(request, 'index.html', locals())


@login_required
def wish_profile_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    wi = True
    active = user.is_active
    courses = Course.objects.all()
    title = "Список желаний"
    if not user.is_authenticated:
        raise Http404("Ur not logim!")
    courses = []
    for cou in Course.objects.all():
        if cou in user.profile.wishes.all():
            courses.append(cou)
    return render(request, 'index.html', locals())


@login_required
def settings_profile_view(request):
    count = Course.objects.filter(status='done').count()
    user = request.user
    active = user.is_active
    if not active:
        raise Http404("Ur not login!")
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('/accounts/profile/')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserUpdateForm(instance=user)
        # prof_form = ProfileForm(request.user.profile.pk)
        # profile_form = ProfileForm(prof_form)
        profile_form = ProfileForm(instance=request.user.profile)
        # profile_form = ProfileForm(instance=user.profile.objects.all())
    return render(request, 'sign_up.html',
                  locals())
