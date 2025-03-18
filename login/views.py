from urllib import request
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from main.forms import UserForm
from django.shortcuts import render, redirect

# Create your views here.
def becameviperr(request):
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
    data = {'form': form}
    return render(request, 'login/login.html', data)