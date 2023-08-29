from django.db import models
from django.core.exceptions import ValidationError


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
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название блюда',
                             validators=[Validator.validatorCapitalizeAndMinLengthTitle])
    the_dish = models.TextField(verbose_name='Состав блюда', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, default=0)
    weight = models.IntegerField(verbose_name='Вес', default=100)
    img = models.ImageField(verbose_name='Картинка', upload_to=f'menu_images/',
                            default="https://nakedchef-fmr.ru/images/logo.png")

    class Meta:
        db_table = 'Menu'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.section}: {self.title}'
