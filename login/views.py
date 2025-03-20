from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm

def becameviperr(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Такого пользователя не существует!")
            #     User.objects.create_user(username=username, password=password)
            #     user = authenticate(request, username=username, password=password)
            #     login(request, user)
            #     return redirect('/')
    else:
        form = UserForm()
    
    return render(request, 'login/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'login/login.html', {'form': form})