from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from steamApp.models import Product


# Create your tests here.

class ProductCreationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_product_creation_valid_form(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'name': 'Test Product',
            'appId': '123',
            'type': 'Test Type',
            'age': '18',
            'free': True,
            'recommendations': '10',
            'releaseDate': '2024-05-17',
            'categories': 'Test Category',
            'genres': 'Test Genre',
            'price': '19.99',
            'discount': '10',
            'languages': 'English',
            'description': 'Test Description'
        }
        response = self.client.post(reverse('createProducts'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Test Product').exists())

    def test_product_creation_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        data = {}  # Empty data, should fail form validation
        response = self.client.post(reverse('createProducts'), data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertFalse(Product.objects.exists())

    def test_product_creation_unauthenticated_user(self):
        response = self.client.get(reverse('createProducts'))
        self.assertRedirects(response, '/accounts/login/?next=/createProducts/', status_code=302, target_status_code=200)