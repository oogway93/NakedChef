from django.urls import path
from .views import MenuListView, mainPage, basket_add, basket

app_name = 'menu'

urlpatterns = [
    path('', mainPage, name='main'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('basket/add/<int:menu_id>/', basket_add, name='basket_add'),
    path('basket/', basket, name='basket'),
]
