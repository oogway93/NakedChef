from rest_framework.test import APITestCase
from api.views import MenuModelViewSet, OrderModelViewSet


class TestAPI(APITestCase):
    def test_serializers(self):
        self.assertTrue(MenuModelViewSet.serializer_class)
        self.assertTrue(OrderModelViewSet.serializer_class)
