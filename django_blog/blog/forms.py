from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    """
    Extend default UserCreationForm to include email (required).
    """
    email = forms.EmailField(required=True, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    """
    For editing profile fields like profile_picture and bio.
    """
    class Meta:
        model = Profile
        fields = ("profile_picture", "bio")
