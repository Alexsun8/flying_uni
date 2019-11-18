from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from account.models import Profile
# from django.Forms import User


# Register your models here.
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInfo(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
#
#
# # Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInfo,)
#
#
# # Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)
