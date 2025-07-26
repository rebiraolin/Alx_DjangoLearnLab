from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings # Keep this, as it's good practice to refer to AUTH_USER_MODEL via settings

class UserRegisterForm(UserCreationForm):
    # Add the custom fields from your CustomUser model
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = settings.AUTH_USER_MODEL # This will now correctly resolve to 'bookshelf.CustomUser'
        fields = [
            'username',
            'email',
            'date_of_birth',   # Include your custom fields
            'profile_photo'    # Include your custom fields
        ]
        # UserCreationForm provides username and password by default.
        # Adding email makes it available during registration.
        # Ensure all fields you expect to register are listed here.