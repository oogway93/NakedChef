# Generated by Django 4.2.4 on 2023-08-29 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_alter_menu_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={},
        ),
        migrations.RemoveField(
            model_name='section',
            name='section',
        ),
        migrations.AlterModelTable(
            name='section',
            table=None,
        ),
    ]
