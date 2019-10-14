from django.contrib import admin
from core.models import Course, Location, President, News


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'location', 'group_president', 'date', 'information')
    list_filter = ('name', 'status', 'location', 'group_president', 'date')


admin.site.register(Course, CourseAdmin)
admin.site.register(Location)
admin.site.register(President)
admin.site.register(News)
