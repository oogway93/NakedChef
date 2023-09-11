from django.shortcuts import render
from .utils import cart_data
from orders.models import Table


def cart(request):
    data = cart_data(request)
    tables = Table.objects.all()

    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cart_items': cart_items, 'tables': tables}
    return render(request, 'cart/cart.html', context)
