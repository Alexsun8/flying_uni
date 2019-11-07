from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# from account.views import  register_view,  create_view
from account.views import  register_view, profile_view
from django.contrib.auth import views
from django.urls import path


urlpatterns = [
    path(r'sign_in/', views.LoginView.as_view(), name='sign_in'),
    # url(r'^authorization$', views.LoginView.as_view(), name='login'),
    url(r'^sign_up$', register_view, name = 'sign_up'),
    # url(r'profile/(?P<profile>[a-zA-Z0-9]+)$', profile_view, name = 'profile')
    url(r'profile$', profile_view, name='profile'),

    # url(r'accounts/style.css',)

    # url(r'^create$', create_view, name='create_profile'),
]

