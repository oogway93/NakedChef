# Generated by Django 4.2.4 on 2023-09-01 16:39

import django.core.validators
from django.db import migrations, models
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_alter_section_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(validators=[menu.models.Validator.validatorTitleIsCapitalize, django.core.validators.MinLengthValidator(2, message='Min length must be more than 2 letters'), django.core.validators.MaxLengthValidator(30, message='Too much... Give a title shorter')], verbose_name='Название блюда'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section',
            field=models.CharField(help_text='Choose: Main  dishes, Appetizers, Soups, Salads, Steaks, Desserts or Beverages', max_length=30, unique=True, validators=[menu.models.Validator.validatorCheckFirstLetterInASection, menu.models.Validator.validatorCheckUniquenessTheSection, django.core.validators.MinLengthValidator(3, message='Min length must be more than 3 letters')], verbose_name='Разделы кухни'),
        ),
    ]
