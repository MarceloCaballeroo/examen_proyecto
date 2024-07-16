from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['region', 'comuna']

class UserEditForm(UserChangeForm):
    password = None  # Exclude password field in the form
    class Meta:
        model = User
        fields = ['username', 'email']