from django.urls import path

from .views import *

app_name = "orders"

urlpatterns = [
    path('', OrderItemListView.as_view(), name='order'),
]
