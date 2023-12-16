from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import Menu, Basket
from utils.views import TitleMixin


# @method_decorator(cache_page(timeout=60 * 30), name='dispatch')
class MenuListView(TitleMixin, ListView):
    model = Menu
    context_object_name = 'menu_list'
    paginate_by = 3
    template_name = 'menu/menu_list.html'
    title = 'Menu'


# @cache_page(timeout=60 * 15)
def mainPage(request):
    context = {'title': 'Вкусная еда каждому!'}
    return render(request, 'main.html', context=context)


@cache_page(timeout=60 * 5)
@login_required
def basket(request):
    user = request.user
    context = {'baskets': Basket.objects.filter(user=user),
               'title': f'Корзина для {user}'}
    return render(request, 'menu/basket.html', context=context)


@cache_page(timeout=60 * 5)
@login_required
def basket_add(request, menu_id: int):
    user = request.user
    Basket.create_or_update(menu_id, user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id: int):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
