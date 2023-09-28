from rest_framework import serializers, fields

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'initiator', 'email', 'hall', 'place')
