from django import forms # импортируем модуль форм из пакета Django


class UserRegister(forms.Form): # создаем класс формы, наследуемый от Django.forms
    username = forms.CharField(label='username', max_length=30) # получаем данные от пользователя
    password = forms.CharField(label='password', widget=forms.PasswordInput, min_length=8)
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput, min_length=8)
    age = forms.CharField(label='age', max_length=3)

