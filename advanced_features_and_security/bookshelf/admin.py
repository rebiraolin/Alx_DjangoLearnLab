# advanced_features_and_security/bookshelf/admin.py

from django.contrib import admin
from .models import Book, CustomUser # Import CustomUser from this app's models.py
from django.contrib.auth.admin import UserAdmin

# Your existing BookAdmin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)

# --- START of CustomUserAdmin to be added/moved ---
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (('Personal Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Personal Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# --- END of CustomUserAdmin to be added/moved ---