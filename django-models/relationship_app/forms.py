from django import forms
from django.contrib.auth.forms import UserCreationForm # Django's built-in form for creating users
from django.contrib.auth.models import User # Import the User model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email'] # You can customize fields here.
                                      # UserCreationForm provides username and password by default.
                                      # Adding email makes it available during registration.