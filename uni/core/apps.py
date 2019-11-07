import os

from django.apps import AppConfig

from uni.settings import BASE_DIR


class CoreConfig(AppConfig):
    name = 'core'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'uni/core/static/',
]
