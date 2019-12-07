import os
from django.apps import AppConfig
from uni.settings import BASE_DIR


class AuthConfig(AppConfig):
    name = 'account'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'uni/account/static/',
]
