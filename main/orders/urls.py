from django.urls import path

from .views import *

urlpatterns = [
    # path('', OrderListView.as_view(), name='order'),
    path('', OrderItemListView.as_view(), name='order_info'),
]
