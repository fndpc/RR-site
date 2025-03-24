from django import forms
from .models import Snipet

class SnipetsForm(forms.ModelForm):
    class Meta:
        model = Snipet
        fields = ['title', 'author', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Класс Bootstrap для стилей
                'placeholder': 'Введите заголовок снипета',  # Плейсхолдер
                'required': 'required',  # Обязательное поле
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя автора',
                'required': 'required',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',  # Для файлов
                'accept': 'image/*',  # Ограничение на тип файлов (изображения)
            }),
        }