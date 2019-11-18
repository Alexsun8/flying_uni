from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# from account.views import  register_view,  create_view
from account.views import register_view, profile_view, user_login, logout_view
from django.contrib.auth import views
from django.urls import path

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
                  path(r'sign_in/', user_login, name='sign_in'),
                  # path(r'sign_in/', user_login, name='create_profile'),
                  url(r'^logout$', logout_view, name='logout'),
                  url(r'^sign_up/', register_view, name='sign_up'),
                  # url(r'profile/(?P<profile>[a-zA-Z0-9]+)$', profile_view, name = 'profile')
                  url(r'profile$', profile_view, name='profile'),
                  # url(r'^create_user$', create_user, name = 'sign_in')
                  # url(r'accounts/style.css',)

                  # url(r'^create$', create_view, name='create_profile'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
