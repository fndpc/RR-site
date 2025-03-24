from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.forms import UserForm
from django.contrib.auth import logout



# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def logout_user(request):
    logout(request)
    return redirect('/')