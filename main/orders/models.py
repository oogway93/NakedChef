import uuid

from django.core.validators import EmailValidator
from django.db import models

from menu.models import Menu, Basket
from users.models import User


class Customer(models.Model):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Почта", validators=[EmailValidator], default="example@example.com")

    class Meta:
        db_table = 'Customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Hall(models.Model):
    category_hall = [
        ('Зал 1', 'Зал 1'),
        ('Зал 2', 'Зал 2'),
        ('VIP lounge', 'VIP lounge'),
        ('Тераса', 'Тераса'),
    ]
    hall = models.CharField('Hall', max_length=20, default='Зал 1', choices=category_hall, unique=True)

    class Meta:
        db_table = 'Hall'
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls'

    def __str__(self) -> None:
        return f"{self.hall}"


class Table(models.Model):
    table_id = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
    ]
    hall_id = models.ForeignKey(to=Hall, on_delete=models.CASCADE, default='Зал 1')
    place = models.CharField('ID стола', max_length=20, default='A1', choices=table_id)

    class Meta:
        db_table = 'Table'
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def __str__(self) -> str:
        return f"{self.hall_id}/{self.place}"


class Order(models.Model):
    category_status = (
        ('Заказано', 'Заказано'),
        ('Готовится', 'Готовится'),
        ('Блюда в зале', 'Блюда в зале'),
    )
    number = 0
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    order_number = models.AutoField(primary_key=True, editable=False, default=1)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    basket_history = models.JSONField(default=dict)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=100, choices=category_status, default=category_status[0][0])
    # waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, null=True, blank=True)
    total_payment = models.IntegerField(default=0)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True)

    # tips = models.ForeignKey(Tips, on_delete=models.SET_NULL, null=True, blank=True)

    def get_status(self):
        return self.category_status

    def update_basket_after_order(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.category_status[1]
        self.basket_history = {
            'ordered_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum())
        }
        baskets.delete()
        self.save()

    def get_total(self):
        return self.quantity * self.menu.price

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Order.objects.all().aggregate(largest=models.Max('order_number'))['largest']
            if last_id is not None:
                self.order_number = last_id + 1
        super(Order, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-date_ordered']

    def __str__(self) -> str:
        return f"{self.order_number}"


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.id}"
