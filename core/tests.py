from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store.models import Customer
from core.models import User


class AccountTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new User object.
        """
        url = reverse('user-list')
        data = {'username': 'monUsername',
                'email': 'monEmail@gmail.com', 'password': "ilovedjango"}
        response = self.client.post(url, data, format='json')

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
