from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer, Hall, Table


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customer_list'


class HallListView(ListView):
    model = Hall
    context_object_name = 'hall_list'


class TableListView(ListView):
    model = Table
    context_object_name = 'table_list'





