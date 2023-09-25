from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

from menu.models import Menu
from menu.serializers import MenuSerializer


class MenuModelViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    # def get_permissions(self):
    #     if self.action in ('create', 'update', 'destroy'):
    #         self.permission_classes = (IsAdminUser,)
    #     return super(MenuModelViewSet, self).get_permissions()
