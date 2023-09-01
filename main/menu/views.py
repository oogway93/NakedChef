from django.shortcuts import render
from django.views.generic import ListView

from .models import Menu, Section


class MenuListView(ListView):
    model = Menu
    context_object_name = 'menu_list'
    template_name = 'menu/menu_list.html'


class SectionListView(ListView):
    model = Section
    context_object_name = 'section_list'
    template_name = 'menu/menu_list.html'


def mainPage(request):
    return render(request, 'main.html')
