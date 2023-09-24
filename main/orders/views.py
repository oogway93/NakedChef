from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views import View
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from utils.views import TitleMixin
from .forms import OrderForm
from .models import Order
from menu.models import Basket


class OrderListView(TitleMixin, ListView):
    template_name = 'order/order_list.html'
    title = 'Store - Заказы'
    queryset = Order.objects.all()
    ordering = ('-created')

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'order/success.html'
    title = 'NakedChef - Спасибо за заказ!'


# class CanceledTemplateView(TitleMixin, TemplateView):
#     template_name = ''


class OrderDetailView(DetailView):
    template_name = 'order/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - Заказ #{self.object.id}'
        context['orders'] = Basket.objects.filter(user=self.request.user)
        return context


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'order/order_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user) if self.request.user.is_authenticated else []
        return context

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        return redirect('orders:success')


@login_required
def remove_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Order.objects.get(id=order_id)
    order.update_after_payment()
