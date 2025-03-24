from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from .forms import UserForm
from django.contrib import messages

class LoginFormView(FormView):
    template_name = 'login/login.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        user_username = form.cleaned_data['username']
        user_password = form.cleaned_data['password']
        try:
            user = User.objects.get(username=user_username)
        except User.DoesNotExist:
            form.add_error(None, 'Такого пользователя не существует.')
            return self.form_invalid(form)
        
        user = authenticate(self.request, username=user_username, password=user_password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error('password', 'Неверный пароль')
            return self.form_invalid(form)




    def form_invalid(self, form):
        return super().form_invalid(form)