from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Order, OrderItem


# class CustomerListView(ListView):
#     model = Customer
#     context_object_name = 'customer_list'
#
#
# class HallListView(ListView):
#     model = Hall
#     context_object_name = 'hall_list'
#
#
# class TableListView(ListView):
#     model = Table
#     context_object_name = 'table_list'
#     template_name = 'order/order_list.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(TableListView, self).get_context_data(**kwargs)
#         context['test'] = 'TTTTTTTESSSSSSTTT'
#         return context


class OrderItemListView(ListView):
    model = OrderItem
    context_object_name = 'items'
    template_name = 'order/order_list.html'
