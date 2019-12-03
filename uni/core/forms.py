from django import forms
from core.models import News, Course, Location

class NewsForm(forms.ModelForm):
    class Meta():
        model = News
        fields = ('headline', 'message',)

class CourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ('name', 'type', 'status', 'teacher', 'location', 'group_president', 'information', 'date',)

class LocationForm(forms.ModelForm):
    class Meta():
        model = Location
        fields = ('address', 'name', 'contact',)


