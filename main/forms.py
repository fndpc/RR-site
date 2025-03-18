from django import forms
from django.contrib.auth.models import User
from django.db import models


class UserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'username',
            'required': 'required',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'password',
            'required': 'required',
        })
    )