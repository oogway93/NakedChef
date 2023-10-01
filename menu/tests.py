from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from menu.models import Section, Menu


class MainTest(TestCase):
    def test_main(self):
        response = self.client.get(f'{reverse("menu:main")}')
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context['title'], 'Вкусная еда каждому!')


class MenuTest(TestCase):
    def test_menu_urls(self) -> None:
        response = self.client.get(f'{reverse("menu:menu")}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(f'{reverse("menu:basket")}')
        self.assertEqual(response2.status_code, status.HTTP_302_FOUND)

    def test_menu_views(self):
        response = self.client.get(f'{reverse("menu:menu")}')
        self.assertTemplateUsed(response, 'menu/menu_list.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_menu_models(self):
        section = Section.objects.create(section='Meat')
        section.save()
        section = Section.objects.create(section='Salads')
        section.save()

        dish = Menu.objects.create(section=section, title='Баранье каре', the_dish='Свиные ребра, специи', price=700,
                                   weight=300)
        dish.save()

        dish2 = Menu.objects.create(section=section, title='Филе миньона', the_dish='Мясо говяжье', price=1550,
                                    weight=700)
        dish2.save()

        new_item = {'section': section, 'title': 'Цезарь',
                    'the_dish': 'chicken, cabbage, pomidor, sauce',
                    'price': 550, 'weight': 300}
        dish3 = Menu.objects.create(**new_item)
        dish3.save()

        list_menu = Menu.objects.all()
        self.assertEqual(list_menu.count(), 3)
        self.assertEqual(Menu._meta.db_table, 'Menu')
