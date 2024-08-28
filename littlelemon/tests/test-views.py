from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient

        self.menu1 = Menu.objects.create(name="pizza", description="Delicius pizza", price=10.99)
        self.menu2 = Menu.objects.create(name="pasta", description="italian pasta", price=8.99)

    def test_getall(self):

        response = self.client.get(reverse('menu/'))
        menus = Menu.objects.all()
        expected_data = [{"id":menu.id, "name": menu.name, "description": menu.description, "price": str(menu.price)} for menu in menus]


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
