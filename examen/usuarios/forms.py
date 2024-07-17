from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

class UserEditForm(UserChangeForm):
    password = None  # Exclude password field in the form
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
