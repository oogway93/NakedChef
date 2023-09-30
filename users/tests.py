import status
from django.test import TestCase, Client
from django.urls import reverse

from users.models import User


class UserTest(TestCase):
    def test_login(self):
        c = Client()
        response = self.client.post(f"/users/login/", {'username': 'root', 'password': '12345'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

