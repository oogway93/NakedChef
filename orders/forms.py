from django import forms
from django.core.validators import EmailValidator

from orders.models import Order


class OrderForm(forms.ModelForm):
    CATEGORIES_HALL = [
        ('Зал 1', 'Зал 1'),
        ('Зал 2', 'Зал 2'),
        ('VIP lounge', 'VIP lounge'),
        ('Тераса', 'Тераса'),
    ]
    TABLES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
    ]
    first_name = forms.CharField(min_length=2, max_length=64, validators=[],
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(min_length=4,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    email = forms.EmailField(validators=[EmailValidator],
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
    hall = forms.ChoiceField(choices=CATEGORIES_HALL)
    place = forms.ChoiceField(choices=TABLES)

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'hall', 'place')
