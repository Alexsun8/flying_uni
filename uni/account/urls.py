from django.conf.urls import url
from account.views import register_view, profile_view, user_login, logout_view, teach_profile_view, stud_profile_view, \
    wish_profile_view, settings_profile_view
from django.urls import path

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
                  path(r'sign_in/', user_login, name='sign_in'),
                  url(r'^logout$', logout_view, name='logout'),
                  url(r'^sign_up/', register_view, name='sign_up'),
                  url(r'profile/$', profile_view, name='profile'),
                  url(r'profile/teach$', teach_profile_view, name='teach_profile'),
                  url(r'profile/learn$', stud_profile_view, name='stud_profile'),
                  url(r'profile/wishes$', wish_profile_view, name='wish_profile'),
                  url(r'profile/settings$', settings_profile_view, name='settings_profile'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
