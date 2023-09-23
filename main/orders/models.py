import uuid

from django.core.validators import EmailValidator
from django.db import models

from menu.models import Menu, Basket
from users.models import User


# class Customer(models.Model):
#     first_name = models.CharField("Имя", max_length=30)
#     last_name = models.CharField("Фамилия", max_length=50)
#     email = models.EmailField("Почта", validators=[EmailValidator], default="example@example.com")
#
#     class Meta:
#         db_table = 'Customer'
#         verbose_name = 'Customer'
#         verbose_name_plural = 'Customers'
#
#     def __str__(self) -> str:
#         return f"{self.first_name} {self.last_name}"


#
# class Hall(models.Model):
#     category_hall = [
#         ('Зал 1', 'Зал 1'),
#         ('Зал 2', 'Зал 2'),
#         ('VIP lounge', 'VIP lounge'),
#         ('Тераса', 'Тераса'),
#     ]
#     hall = models.CharField('Hall', max_length=20, default='Зал 1', choices=category_hall,
#                             help_text="Зал 1/Зал2/VIP lounge/Тераса",
#                             unique=True)
#
#     class Meta:
#         db_table = 'Hall'
#         verbose_name = 'Hall'
#         verbose_name_plural = 'Halls'
#
#     def __str__(self) -> None:
#         return f"{self.hall}"
#
#
# class Table(models.Model):
#     table_id = [
#         ('A1', 'A1'),
#         ('A2', 'A2'),
#         ('A3', 'A3'),
#         ('B1', 'B1'),
#         ('B2', 'B2'),
#         ('B3', 'B3'),
#     ]
#     hall_id = models.ForeignKey(to=Hall, on_delete=models.CASCADE, default='Зал 1')
#     place = models.CharField('ID стола', max_length=20, default='A1', choices=table_id, help_text="A(1-3) или B(1-3)")
#
#     class Meta:
#         db_table = 'Table'
#         verbose_name = 'Table'
#         verbose_name_plural = 'Tables'
#
#     def __str__(self) -> str:
#         return f"{self.hall_id}/{self.place}"


class Order(models.Model):
    CATEGORIES_HALL = [
        ('Зал 1', 'Зал 1'),
        ('Зал 2', 'Зал 2'),
        ('VIP lounge', 'VIP lounge'),
        ('Тераса', 'Тераса'),
    ]
    TABLES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
    ]

    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField("Имя", max_length=64)
    last_name = models.CharField("Фамилия", max_length=64)
    email = models.EmailField(max_length=256, default="example@example.com")
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    place = models.CharField('ID стола', max_length=20, default=TABLES[0][0], choices=TABLES, help_text="A(1-3) или B(1-3)")
    hall = models.CharField('Место', max_length=20, default=CATEGORIES_HALL[0][0],
                            choices=CATEGORIES_HALL,
                            help_text="Зал 1/Зал2/VIP lounge/Тераса")
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def get_status(self):
        return self.status



    class Meta:
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created']

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'
