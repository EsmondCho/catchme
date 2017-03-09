from django import forms
from django.contrib.auth.models import User
from software.models import Profile


class UserForm(forms.ModelForm):
    model = User
    field = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    model = Profile
    field = ['is_freshman']
    exclude = ['user']
