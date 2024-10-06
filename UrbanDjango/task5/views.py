from django.http import HttpResponse # импортируем пакета обработки http запросов
from django.shortcuts import render # импортируем пакет отрисовки шаблонов
from .registration_form import UserRegister # импортируем django форму


def sign_up_by_html(request): # функция обработки html формы
    users = ['user1', 'user2', 'user3'] # объявляем список пользователей для сравнения
    info = {} # объявляем пустой словарь, в котором будут храниться ошибки с ключом 'error'
    errors = [] # объявляем пустой список для сбора ошибок

    if request.method == 'POST': # проверям какой тип запроса пришел, если POST получаем данные от пользователя
        username = request.POST.get('username') # получаем от пользоваателя имя
        password = request.POST.get('password') # получаем от пользоваателя пароль
        repeat_password = request.POST.get('repeat_password') # получаем от пользоваателя повтор пароля
        age = int(request.POST.get('age')) # получаем от пользоваателя возраст

        if password == repeat_password and age >= 18 and username not in users: # проверяем совпадают ли пароли, соответствует ли возраст и пользователя еще нет в базе
            return HttpResponse(f'Приветствуем, {username}!') # если ошибок нет, приветствует пользователя
        elif username in users:
            errors.append('Пользователь уже существует') # если пользователь есть в базе, фиксируем ошибку
        elif password != repeat_password:
            errors.append('Пароли не совпадают') # если пароли не совпадают, фиксируем ошибку
        elif age < 18:
            errors.append('Вы должны быть старше 18') # если возраст меньше допустимого, фиксируем ошибку
    info['error'] = errors # передаем список ошибок в словарь
    return render(request, 'registration_page.html', context=info) # отрисовываем шаблон и передаем
                                                                                # ошибки для отображения

def sign_up_by_django(request): # функция обработки django формы
    users = ['user1', 'user2', 'user3']  # объявляем список пользователей для сравнения
    info = {}  # объявляем пустой словарь, в котором будут храниться ошибки с ключом 'error'
    errors = []  # объявляем пустой список для сбора ошибок

    if request.method == 'POST': # проверям какой тип запроса пришел, если POST получаем данные от пользователя
        form = UserRegister(request.POST) # объявляем объект формы
        if form.is_valid(): # получаем данные формы и проверяем корректность данных для исключения обхода типов полей
            username = form.cleaned_data.get('username') # получаем от пользоваателя имя
            password = form.cleaned_data.get('password') # получаем от пользоваателя пароль
            repeat_password = form.cleaned_data.get('repeat_password') # получаем от пользоваателя повтор пароля
            age = int(form.cleaned_data.get('age')) # получаем от пользоваателя возраст

            if password == repeat_password and age >= 18 and username not in users: # проверяем совпадают ли пароли, соответствует ли возраст и пользователя еще нет в базе
                return HttpResponse(f'Приветствуем, {username}!') # если ошибок нет, приветствует пользователя
            elif username in users:
                errors.append('Пользователь уже существует') # если пользователь есть в базе, фиксируем ошибку
            elif password != repeat_password:
                errors.append('Пароли не совпадают') # если пароли не совпадают, фиксируем ошибку
            elif age < 18:
                errors.append('Вы должны быть старше 18') # если возраст меньше допустимого, фиксируем ошибку
    else:
        form = UserRegister() # если пришел GET запрос показываем пустую форму

    info['error'] = errors # передаем список ошибок в словарь
    return render(request, 'registration_page.html', {'form': form, 'info': info})
    # отрисовываем шаблон и передаем в него форму и ошибки для отображения

