from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import Menu, Basket


class MenuListView(ListView):
    model = Menu
    context_object_name = 'menu_list'
    template_name = 'menu/menu_list.html'


def mainPage(request):
    return render(request, 'main.html')


@login_required
def basket(request):
    user = request.user
    context = {'baskets': Basket.objects.filter(user=user)}
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
