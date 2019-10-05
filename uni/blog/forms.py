from django.contrib.auth.models import User
from django.forms import forms
from django.forms import ModelForm

from uni.core.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'bio', 'want_study_courses', 'already_studing', 'can_teach', 'already_teaching', 'birth_date')
