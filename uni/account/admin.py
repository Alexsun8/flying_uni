from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from account.models import Profile


class ProfileInfo(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    filter_horizontal = ('wishes', 'studying', 'knowledge', 'teaching',)


class UserAdmin(UserAdmin):
    inlines = (ProfileInfo,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
