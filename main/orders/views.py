from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import OrderForm
from .models import Order, OrderItem
from menu.models import Basket


class OrderListView(ListView):
    template_name = 'order/order_list.html'
    queryset = Order.objects.all()
    ordering = ('-order_number',)
    model = Order

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(initiator=self.request.user)
        return context


class OrderDetailView(DetailView):
    template_name = 'order/order.html'
    model = Order

    # def get_context_data(self, **kwargs):
    #     context = super(OrderDetailView, self).get_context_data(**kwargs)
    #     return context


class OrderCreateView(CreateView):
    template_name = 'order/order_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user) if self.request.user.is_authenticated else []
        return context

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse("menu:main"))

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
