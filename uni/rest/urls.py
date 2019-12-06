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
