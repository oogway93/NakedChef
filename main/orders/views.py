from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer, Hall, Table, Order


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customer_list'


class HallListView(ListView):
    model = Hall
    context_object_name = 'hall_list'


class TableListView(ListView):
    model = Table
    context_object_name = 'table_list'
    template_name = 'order/order_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TableListView, self).get_context_data(**kwargs)
        context['test'] = 'TTTTTTTESSSSSSTTT'
        return context


class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'order/order_list.html'
