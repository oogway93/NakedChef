from django.urls import path
from .views import MenuListView, mainPage, SectionListView

urlpatterns = [
    path('', mainPage, name='main'),
    path('menu/', MenuListView.as_view(), name='menu'),
]
