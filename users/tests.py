from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from users.models import User


class UserTest(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Ivan', 'last_name': 'Ivanov',
            'username': 'ivan', 'email': 'ivan.ivanov@yandex.ru',
            'password': 'User123456',
        }
        self.path = reverse('users:register')
        self.path_login = reverse('users:login')

    def test_login_post(self):
        username = {'username': 'root'}
        response = self.client.post(self.path_login, {'username': 'root', 'password': '12345'})
        response2 = self.client.post(self.path_login,
                                     {'username': self.data['username'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response2, 'registration/login.html')

    def test_user_registration_post(self):
        User.objects.create(username=self.data['username'])

        response = self.client.post(self.path, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'registration/register.html')
