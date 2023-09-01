import string

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Validator:
    @staticmethod
    def validatorTitleIsCapitalize(title: str):
        if title.strip()[0] not in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            raise ValidationError("First letter isn`t upper")

    @staticmethod
    def validatorCheckFirstLetterInASection(section: str):
        if section.strip()[0] not in string.ascii_uppercase:
            raise ValidationError("First Letter must be upper")

    @staticmethod
    def validatorCheckUniquenessTheSection(section: str):
        data = Section.objects.all()
        list_data = list(data)
        for d in list_data:
            if str(d)[:9].lower() == section.lower():
                raise ValidationError("The section must be unique")


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
        max_length=30,
        unique=True,
        validators=[Validator.validatorCheckFirstLetterInASection,
                    Validator.validatorCheckUniquenessTheSection,
                    MinLengthValidator(3, message="Min length must be more than 3 letters")],
        help_text="Choose: Main  dishes, Appetizers, Soups, Salads, Steaks, Desserts or Beverages")

    class Meta:
        db_table = 'Section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return f'{self.section}'


class Menu(models.Model):
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название блюда',
                             validators=[Validator.validatorTitleIsCapitalize,
                                         MinLengthValidator(2, message="Min length must be more than 2 letters"),
                                         MaxLengthValidator(30, message="Too much... Give a title shorter")])
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
