# Generated by Django 3.2.20 on 2023-09-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_alter_menu_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
