# advanced_features_and_security/bookshelf/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager # Consolidated imports
from django.utils.translation import gettext_lazy as _ # Good practice for verbose names

# --- START CustomUserManager and CustomUser definitions ---

class CustomUserManager(UserManager):
    # If you want to use email as the primary login, you can adjust create_user/superuser
    # to make email required and set USERNAME_FIELD = 'email' in CustomUser.
    # For now, keeping it as it was for username-based AbstractUser.
    def create_user(self, username, email=None, password=None, **extra_fields):
        # Ensure email is normalized if it's used as a unique identifier
        if email:
            email = self.normalize_email(email)
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return super().create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

# --- END CustomUserManager and CustomUser definitions ---


# Existing Book Model (ensure this remains as it was, now below CustomUser)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
            # Add the new permissions for Task 1, Step 1 if you haven't yet
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"

# If you have Author, Library, Librarian, UserProfile models in relationship_app/models.py,
# they should NOT be duplicated here unless bookshelf specifically needs its own versions.
# Based on your previous relationship_app/models.py, those models belong there.
# Only include models here that are specifically part of the 'bookshelf' app's domain.
# I'm assuming for now that the Author, Library, Librarian, UserProfile are only in relationship_app.