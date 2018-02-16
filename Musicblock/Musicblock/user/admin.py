from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class UserProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile


class UserProfileAdmin(UserAdmin):
    form = UserProfileForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
        'ssn','file','prvateKey','publicKey','address','token','gender'
        ,)}),
    )


admin.site.register(UserProfile, UserProfileAdmin)