from django.urls import path

from .views import OrderCreateView, OrderListView, OrderDetailView, SuccessTemplateView, remove_order

app_name = "orders"

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('success/', SuccessTemplateView.as_view(), name='success'),
    path('order/remove/<int:order_id>', remove_order, name='removed_order')
]
