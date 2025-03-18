from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserForm
from django.contrib.auth import authenticate, login



# Create your views here.

def main(request):
    me = request.user

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                login(request, user)
                print('Вы авторизованы')
                return redirect('/snippets')  # Убедитесь, что 'snippets' правильно настроен в urls.py
            else:
                print('Вы не находитесь в БД или неверный пароль')
        else:
            print('Форма не валидна:', form.errors)  # Вывод ошибок формы для отладки

    form = UserForm()  # Создаем форму для GET-запроса
    data = {'me': me}
    return render(request, 'main/main.html', data)