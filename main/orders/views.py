from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import OrderForm
from .models import Order, OrderItem
from menu.models import Basket


class OrderItemListView(ListView):
    model = OrderItem
    context_object_name = 'items'
    template_name = 'order/order_list.html'


class OrderDetailView(DetailView):
    template_name = 'order/order.html'
    model = Order


class OrderCreateView(CreateView):
    template_name = 'order/order_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)

        return HttpResponseRedirect(reverse("menu:main"))

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

