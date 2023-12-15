import string

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from users.models import User


class Validator:
    @staticmethod
    def validatorStringIsCapitalize(string_: str):
        if string_[0] in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" or string_[0] in string.ascii_uppercase:
            print('Success')
        else:
            print('Some wrongs')
            raise ValidationError("First letter isn`t upper")

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
        validators=[Validator.validatorStringIsCapitalize,
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
                             max_length=30,
                             validators=[Validator.validatorStringIsCapitalize,
                                         MinLengthValidator(2, message="Min length must be more than 2 letters"),
                                         MaxLengthValidator(30, message="Too much... Give a title shorter")],
                             unique=True)
    the_dish = models.TextField(verbose_name='Состав блюда', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, default=0,
                                help_text="Prices in RUB")
    weight = models.IntegerField(verbose_name='Вес', default=100, help_text="Mention in grammes")
    img = models.URLField(verbose_name='Картинка',
                          default="https://nakedchef-fmr.ru/images/logo.png")

    class Meta:
        db_table = 'Menu'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.section}: {self.title}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    class Meta:
        db_table = 'Basket'
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.menu.title}'

    def sum(self):
        return self.menu.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.menu.title,
            'quantity': self.quantity,
            'price': float(self.menu.price),
            'sum': float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, menu_id, user):
        baskets = Basket.objects.filter(user=user, menu_id=menu_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, menu_id=menu_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated
