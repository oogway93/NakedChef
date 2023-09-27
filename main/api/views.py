from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from menu.models import Menu, Section
from menu.serializers import MenuSerializer, SectionSerializer
from orders.models import Order
from orders.serializers import OrderSerializer


class MenuModelViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = (IsAdminUser,)
        return super(MenuModelViewSet, self).get_permissions()


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = (IsAdminUser,)
        return super(OrderModelViewSet, self).get_permissions()


class SectionModelViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            self.permission_classes = (IsAdminUser,)
        return super(SectionModelViewSet, self).get_permissions()
