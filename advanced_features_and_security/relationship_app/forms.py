from django import forms
from django.contrib.auth.forms import UserCreationForm # Django's built-in form for creating users
from django.conf import settings  # Import the User model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['username', 'email'] # You can customize fields here.
                                      # UserCreationForm provides username and password by default.
                                      # Adding email makes it available during registration.