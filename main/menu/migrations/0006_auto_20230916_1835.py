# Generated by Django 3.2.20 on 2023-09-16 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Basket', 'verbose_name_plural': 'Baskets'},
        ),
        migrations.AlterModelTable(
            name='basket',
            table='Basket',
        ),
    ]
