from django import forms
from django.contrib.auth.models import User
from django.db import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']