from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from account.forms import UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
    #
    # def create_user(request):
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


@login_required
def profile_view(request, ProfileInfo):
    user = get_object_or_404(ProfileInfo, profile=ProfileInfo)
    return render(request, 'profile.html', {'profile': ProfileInfo})


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
                return render (request, 'idea.html')
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
    return render(request, 'logout.html')
# from django.contrib.auth.forms import UserCreationForm

#
# def register_view(respones):
#     if respones.method == 'POST':
#         form = UserCreationForm(respones.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('idea')
#     else:
#         form = UserCreationForm()
#
#     return render(respones, 'sign_up.html', {'form': form})


def register_view(request):
    registered = False
    if request.method == 'POST':
        print("wooooorks")
        user_form = UserForm(request.POST)
        # print("User:",  user_form.user.username)
        # print("Pass:", user_form.user.password)
        profile_form = ProfileForm(request.POST)
        # print("Prof:", profile_form.wishes)
        print("bool prof:", profile_form.is_valid())
        print("bool us:", user_form.is_valid())
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # if 'photo' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['photo']
            profile.save()
            registered = True
            # count = Course.objects.filter(status='done').count()
            # user = request.user
            # active = True
            # courses = Course.objects.all()
            return redirect('profile')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'sign_up.html',
                          {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})
