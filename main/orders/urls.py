from django.urls import path

from .views import *

app_name = "orders"

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order')
]
