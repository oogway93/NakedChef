from django.shortcuts import render
from django.views.generic import ListView

from .models import Menu, Section


class MenuListView(ListView):
    model = Menu
    context_object_name = 'menu_list'
    template_name = 'menu/menu_list.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['dish'] = Section.objects.filter(pk=context['menu_list'][0])
    #     return context


def mainPage(request):
    return render(request, 'main.html')
