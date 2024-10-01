from django.shortcuts import render
from django.views.generic import TemplateView


class First(TemplateView):
    template_name = 'class_template.html'


def second(request):
    return render(request, 'func_template.html')
