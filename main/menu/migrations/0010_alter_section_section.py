# Generated by Django 4.2.4 on 2023-08-31 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_alter_menu_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section',
            field=models.CharField(max_length=30, verbose_name='Разделы кухни'),
        ),
    ]