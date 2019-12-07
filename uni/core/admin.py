from django.contrib import admin
from core.models import Course, Location, News, Categories

admin.site.register(News)

admin.site.register(Course)

admin.site.register(Location)

admin.site.register(Categories)
