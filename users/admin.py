from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('birthdate', 'phone')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('birthdate', 'phone')}),)


admin.site.register(CustomUser)