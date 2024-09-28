from django.views.generic import TemplateView


class first(TemplateView):
    template_name = 'class_template.html'


class second(TemplateView):
    template_name = 'func_template.html'
