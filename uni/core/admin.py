from django.contrib import admin
from .models import Course, Location


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'location')


admin.site.register(Course, CourseAdmin)
admin.site.register(Location)
