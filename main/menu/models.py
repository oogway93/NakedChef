from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Validator:

    @staticmethod
    def validatorCapitalizeAndMinLengthTitle(title: str):
        if len(title) <= 2 and not title.capitalize():
            raise ValidationError("Min length must be more than 2 symbols and first letter is upper")


class Section(models.Model):
    sectionChoices = [('Main dishes', 'Main dishes'),
                      ('Appetizers', 'Appetizers'),
                      ('Soups', 'Soups'),
                      ('Salads', 'Salads'),
                      ('Steaks', 'Steaks'),
                      ('Desserts ', 'Desserts'),
                      ('Beverages', 'Beverages'), ]

    section = models.CharField(
        verbose_name="Разделы кухни",
        choices=sectionChoices,
        null=False,
        default=sectionChoices[0][0])

    class Meta:
        db_table = 'Section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return f'{self.section}'


class Menu(models.Model):
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE, null=False)
    title = models.CharField(verbose_name='Название блюда',
                             validators=[Validator.validatorCapitalizeAndMinLengthTitle],
                             null=False)

    class Meta:
        db_table = 'Menu'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.section}: {self.title}'
