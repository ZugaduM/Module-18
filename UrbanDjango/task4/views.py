from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    pagename = 'Главная страница'
    sub_name = 'Реферальные переходы'
    context = {
        'pagename': pagename,
        'sub_name': sub_name,
    }
    return render(request, 'index.html', context)

def menu(request):
    return render(request, 'menu.html')

def second(request):
    urls = {
        'company': ['Ozone',
                    'Wildberries',
                    'Я.Маркет'],
        'url': ['https://www.ozon.ru/',
                'https://www.wildberries.ru/',
                'https://market.yandex.ru/']
    }
    zipped_urls = zip(urls['company'], urls['url'])
    context = {
        'zipped_urls': zipped_urls,
    }
    return render(request, 'second_page.html', context)

class Third(TemplateView):
    template_name = 'third_page.html'
    extra_context = {
        'pagename': 'Статистика',
        'sub_name': 'Under construction!'
    }

