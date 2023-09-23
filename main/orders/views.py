from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

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


class OrderDetailView(DetailView):
    template_name = 'order/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - Заказ #{self.object.id}'
        context['orders'] = Basket.objects.filter(user=self.request.user)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(OrderDetailView, self).get_context_data(**kwargs)
    #     context['order'] = Basket.objects.filter()
    #     return context


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


def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Order.objects.get(id=order_id)
    order.update_after_payment()

# def createOrder(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         # print('Printing POST:',request.POST)
#         form = OrderForm(request.POST)
#         # form handles the process of saving to database/
#         if form.is_valid():
#             form.save()  # Here
#             return redirect('menu:main')
#     context = {'form': form,
#                'baskets': Basket.objects.filter(user=request.user) if request.user.is_authenticated else []}
#     return render(request, 'order/order_create.html', context)

# class OrderCreationView(View):
#     template_name = 'order/order_create.html'
#
#     def get(self, request):
#         context = {
#             'form': OrderForm()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = OrderForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user,)
#             messages.success(request, 'Заказ создан!')
#             return redirect('menu:main')
#         context = {
#             'form': form
#         }
#         messages.error(request, 'Провал при выполнении заказа!')
#         return render(request, self.template_name, context)

# def create_order(request):
#     if request.method == 'POST':
#         form
