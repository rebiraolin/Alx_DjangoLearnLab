# advanced_features_and_security/users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (('Personal Info'), {'fields': ('date_of_birth', 'profile_photo')}), # <--- MUST BE profile_photo
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Personal Info'), {'fields': ('date_of_birth', 'profile_photo')}), # <--- MUST BE profile_photo
    )

admin.site.register(CustomUser, CustomUserAdmin)