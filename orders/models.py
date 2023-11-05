from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator
from django.db import models

from users.models import User


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

    first_name = models.CharField("Имя", max_length=64,
                                  validators=[
                                      MinLengthValidator(2, message='The first name should contains min 2 letters')])
    last_name = models.CharField("Фамилия", max_length=64,
                                 validators=[MinLengthValidator(4, 'The last name should contains min 4 letters')])
    email = models.EmailField(max_length=256, validators=[EmailValidator], default="example@example.com")
    created = models.DateTimeField(auto_now_add=True)
    place = models.CharField('ID стола', max_length=20, default=TABLES[0][0], choices=TABLES,
                             help_text="A(1-3) или B(1-3)")
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
