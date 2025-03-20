from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from login.forms import UserForm

# Create your views here.
class RegisterFormView(FormView):
    template_name = 'register/register.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        User.objects.create_user(username=username, password=password)
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)