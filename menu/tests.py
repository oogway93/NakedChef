import status
from django.test import TestCase
from django.urls import reverse, resolve

from menu.models import Section, Menu
from menu.views import MenuListView


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

        response2 = self.client.get(f'{reverse("menu:main")}')
        self.assertTemplateUsed(response2, 'main.html')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.context['title'], 'Вкусная еда каждому!')

    def test_menu_models(self):
        section = Section.objects.create(section='Meat')
        section.save()
        dish = Menu.objects.create(section=section, title='Баранье каре', the_dish='Свиные ребра, специи', price=700,
                                   weight=300)
        dish.save()

        dish2 = Menu.objects.create(section=section, title='Филе миньона', the_dish='Мясо говяжье', price=1550,
                                    weight=700)
        dish2.save()

        list_menu = Menu.objects.all()
        self.assertEqual(list_menu.count(), 2)
        self.assertEqual(Menu._meta.db_table, 'Menu')
