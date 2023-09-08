from django.db import models


class Customer(models.Model):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=50)

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
