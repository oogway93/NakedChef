from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderItemListView.as_view(), name='order'),
]
