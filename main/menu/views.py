from django.shortcuts import render
from django.views.generic import ListView

from models import Menu


class Menu(ListView):
    model = Menu

