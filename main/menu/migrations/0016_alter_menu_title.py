# Generated by Django 3.2.20 on 2023-09-08 17:20

import django.core.validators
from django.db import migrations, models
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_alter_menu_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=50, unique=True, validators=[menu.models.Validator.validatorTitleIsCapitalize, django.core.validators.MinLengthValidator(2, message='Min length must be more than 2 letters'), django.core.validators.MaxLengthValidator(30, message='Too much... Give a title shorter')], verbose_name='Название блюда'),
        ),
    ]
