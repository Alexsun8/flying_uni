from django.contrib import admin
# from django.contrib.auth import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models

from account.models import Profile
# from django.Forms import User


# Register your models here.
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

# class ProfileAdmin(admin.ModelAdmin):
    # list_display = ("Wishes","Studying", "Knowledge", "Teaching")

class ProfileInfo(admin.StackedInline):
    # inlines = (ProfileAdmin, )
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    filter_horizontal = ('wishes', 'studying', 'knowledge', 'teaching',)

        # filter_horizontal = [i.name for i in models.Rule._meta.get_fields() if i.name.startswith("Course")] + [
        #     "Wishes","Studying", "Knowledge", "Teaching"]
        # list_display = ("Wishes","Studying", "Knowledge", "Teaching")
    # filter_horizontal = ("Wishes","Studying", "Knowledge", "Teaching")
# #
# #
# # # Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInfo, )

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #     disabled_fields = set()  # type: Set[str]
    #     if not is_superuser:
    #         disabled_fields |= {
    #             'username',
    #             'is_superuser',
    #             'user_permissions',
    #         }
    #     # Prevent non-superusers from editing their own permissions
    #     if (
    #             not is_superuser
    #             and obj is not None
    #             and obj == request.user
    #     ):
    #         disabled_fields |= {
    #             'is_staff',
    #             'is_superuser',
    #             'groups',
    #             'user_permissions',
    #         }
    #     for f in disabled_fields:
    #         if f in form.base_fields:
    #             form.base_fields[f].disabled = True

    # list_display = ("Wishes","Studying", "Knowledge", "Teaching")

# class ProfileAdmin(admin.ModelAdmin):
    # filter_horizontal = [i.name for i in Profile._meta.get_fields() if i.name.startswith("Course")] + [
        # "Wishes","Studying", "Knowledge", "Teaching"]
    # list_display = ("Wishes","Studying", "Knowledge", "Teaching")
    # filter_horizontal = ('wishes', 'studying', 'knowledge', 'teaching',)

# admin.site.register(Profile, ProfileAdmin)
#
#
# # Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)
