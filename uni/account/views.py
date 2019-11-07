from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View

from account.models import Profile


# # Create your views here.
# def log_view(request):
#     return render(request, 'log.html')
#
#


@login_required
def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'progressive-sign-up/dist/index.html', {'new_user': new_user})
    else:
        user_form = UserCreationForm()
    return render(request, 'progressive-sign-up/dist/index.html', {'user_form': user_form})


# user profile form
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
def profile_view(request, User):
    user = get_object_or_404(User, profile=User)
    return render(request, 'profile/profile.html', {'profile': user})
