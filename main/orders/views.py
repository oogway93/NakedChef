from django.views.generic import ListView, DetailView
from .models import Order, OrderItem


class OrderItemListView(ListView):
    model = OrderItem
    context_object_name = 'items'
    template_name = 'order/order_list.html'
