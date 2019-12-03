"""uni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from rest.views import CoursesJsonView, CourseJsonView, ProfileJsonView, ProfilePersonalView, UserListView, Logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken import views


urlpatterns = [
    path('courses/', CoursesJsonView.as_view()),
    url('course/(?P<pk>\d+)', CourseJsonView.as_view()),
    url('user/(?P<pk>\d+)', ProfileJsonView.as_view()),
    url('profile/', ProfilePersonalView.as_view()),
    url('user_list/', UserListView.as_view()),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', Logout.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
