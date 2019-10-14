from django.contrib.auth.models import User
from django.forms import forms
from django.forms import ModelForm

from core.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'wishes', 'studying', 'knowledge', 'teaching', 'birth_date', 'photo')
