from django.urls import path

from .views import TableListView, OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='table'),
]
