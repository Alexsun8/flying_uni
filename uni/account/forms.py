from django import forms
from django.contrib.auth.models import User
from account.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(help_text="год-месяц-число")

    class Meta():
        model = Profile
        fields = ('bio', 'contact', 'birth_date')
