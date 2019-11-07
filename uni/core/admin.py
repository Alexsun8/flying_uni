from django.contrib import admin
from core.models import Course, Location, President, News
admin.site.register(News)
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from core.models import Profile


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'location', 'group_president', 'date', 'information')
    list_filter = ('name', 'status', 'location', 'group_president', 'date')


admin.site.register(Course, CourseAdmin)
admin.site.register(Location)
admin.site.register(President)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
#
# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
