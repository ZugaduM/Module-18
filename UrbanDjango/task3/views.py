from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


class Second(TemplateView):
    template_name = 'second_page.html'

class Third(TemplateView):
    template_name = 'third_page.html'

