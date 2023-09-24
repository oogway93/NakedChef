from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, View
from django.contrib.auth.decorators import login_required

from .models import Menu, Basket, Section
from utils.views import TitleMixin


class MenuListView(TitleMixin, ListView):
    model = Menu
    context_object_name = 'menu_list'
    template_name = 'menu/menu_list.html'
    title = 'Menu'


def mainPage(request):
    context = {'title': 'Вкусная еда каждому!'}
    return render(request, 'main.html', context=context)


@login_required
def basket(request):
    user = request.user
    context = {'baskets': Basket.objects.filter(user=user),
               'title': f'Корзина для {user}'}
    return render(request, 'menu/basket.html', context=context)


@login_required
def basket_add(request, menu_id):
    user = request.user
    Basket.create_or_update(menu_id, user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
