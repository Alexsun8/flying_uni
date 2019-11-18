from django import forms
from django.contrib.auth.forms import UserCreationForm

from account import models
from account.models import Profile
from django.contrib.auth.models import User
from core.models import Course


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    # wishes = forms.MultipleChoiceField(choices= Course, widget=forms.CheckboxSelectMultiple)
    # knowledge = forms.MultipleChoiceField(queryset= Course.objects.filter('name'))
    # knowledge = forms.MultipleChoiceField(queryset= Course.objects.all(),  widget=forms.CheckboxSelectMultiple)
    # birth_day = forms.SelectDateWidget(widget=forms.SelectDateWidget())
    class Meta():
        model = Profile
        # fields = ('bio','knowledge',  'contact', 'photo','birth_date', 'wishes')
        # fields = '__all__'
        fields = ('bio', 'wishes', 'knowledge', 'contact', 'birth_date', 'photo',)
