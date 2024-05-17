from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from steamApp.forms import SteamUserForm
from steamApp.models import Product, SteamUser, Developer, Publisher


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
        self.assertTrue(Product.objects.get(name='Test Product').creatorUser == self.user)

    def test_product_creation_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        data = {}
        response = self.client.post(reverse('createProducts'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Product.objects.exists())

    def test_product_creation_unauthenticated_user(self):
        response = self.client.get(reverse('createProducts'))
        self.assertRedirects(response, '/accounts/login/?next=/createProducts/', status_code=302,
                             target_status_code=200)


class SteamUserCreationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_steam_user_form_valid(self):
        self.product1 = Product.objects.create(name='Product 1', creatorUser=self.user)
        self.product2 = Product.objects.create(name='Product 2', creatorUser=self.user)
        self.friend1 = SteamUser.objects.create(personaName='Friend 1', creatorUser=self.user)
        self.friend2 = SteamUser.objects.create(personaName='Friend 2', creatorUser=self.user)

        self.client.login(username='testuser', password='12345')
        data = {
            'steamID': 1234,
            'realName': 'Test User',
            'personaName': 'Test Persona',
            'country': 'Spain',
            'friends': [self.friend1.id, self.friend2.id],
            'products': [self.product1.id, self.product2.id],

        }
        response = self.client.post(reverse('createSteamUser'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SteamUser.objects.filter(realName='Test User').exists())
        self.assertTrue(SteamUser.objects.get(realName='Test User').creatorUser == self.user)

    def test_steam_user_creation_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        data = {}
        response = self.client.post(reverse('createSteamUser'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(SteamUser.objects.exists())

    def test_steam_user_creation_unauthenticated_user(self):
        response = self.client.get(reverse('createSteamUser'))
        self.assertRedirects(response, '/accounts/login/?next=/createSteamUser/', status_code=302,
                             target_status_code=200)


class CreateDeveloperTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_developer_form_valid(self):
        self.client.login(username='testuser', password='12345')
        self.product1 = Product.objects.create(name='Product 1', creatorUser=self.user)
        self.product2 = Product.objects.create(name='Product 2', creatorUser=self.user)

        data = {
            'name': 'Test Developer',
            'products': [self.product1.id, self.product2.id]
        }

        response = self.client.post(reverse('createDeveloper'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Developer.objects.filter(name='Test Developer').exists())

        self.assertTrue(Developer.objects.get(name='Test Developer').creatorUser == self.user)

    def test_developer_creation_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        data = {}
        response = self.client.post(reverse('createDeveloper'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Developer.objects.exists())

    def test_developer_creation_unauthenticated_user(self):
        response = self.client.get(reverse('createDeveloper'))
        self.assertRedirects(response, '/accounts/login/?next=/createDevelopers/', status_code=302,
                             target_status_code=200)


class CreatePublisherTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_publisher_form_valid(self):
        self.client.login(username='testuser', password='12345')
        self.product1 = Product.objects.create(name='Product 1', creatorUser=self.user)
        self.product2 = Product.objects.create(name='Product 2', creatorUser=self.user)

        data = {
            'name': 'Test Publisher',
            'products': [self.product1.id, self.product2.id]
        }

        response = self.client.post(reverse('createPublisher'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Publisher.objects.filter(name='Test Publisher').exists())

        self.assertTrue(Publisher.objects.get(name='Test Publisher').creatorUser == self.user)

    def test_publisher_creation_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        data = {}
        response = self.client.post(reverse('createPublisher'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Publisher.objects.exists())

    def test_publisher_creation_unauthenticated_user(self):
        response = self.client.get(reverse('createPublisher'))
        self.assertRedirects(response, '/accounts/login/?next=/createPublisher/', status_code=302,
                             target_status_code=200)


class ModifyProductTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.product = Product.objects.create(
            name='Test Product',
            appId=123,
            type='Test Type',
            age=18,
            free=True,
            recommendations='10',
            releaseDate='2024-05-17',
            categories='Test Category',
            genres='Test Genre',
            price=19.99,
            discount=10,
            languages='English',
            description='Test Description',
            creatorUser=self.user
        )

    def test_modify_product(self):
        self.client.login(username='testuser', password='12345')

        url = reverse('modifyProduct', kwargs={'id': self.product.id})

        data = {
            'name': 'Modified Test Product',
            'appId': '456',
            'type': 'Modified Test Type',
            'age': '21',
            'free': False,
            'recommendations': '20',
            'releaseDate': '2025-05-17',
            'categories': 'Modified Test Category',
            'genres': 'Modified Test Genre',
            'price': '29.99',
            'discount': '20',
            'languages': 'Spanish',
            'description': 'Modified Test Description'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)

        self.product.refresh_from_db()

        self.assertEqual(self.product.name, 'Modified Test Product')
        self.assertEqual(self.product.appId, 456)

    def test_product_modify_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('modifyProduct', kwargs={'id': self.product.id})
        data = {}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()

        self.assertEqual(self.product.appId, 123)

    def test_product_modify_unauthenticated_user(self):
        url = reverse('modifyProduct', kwargs={'id': self.product.id})
        data = {}
        response = self.client.post(url, data)
        self.assertRedirects(response, f'/accounts/login/?next={url}', status_code=302,
                             target_status_code=200)


class ModifySteamUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.steam_user = SteamUser.objects.create(
            steamID=1234,
            realName='Test User',
            personaName='Persona Name',
            country='Spain',
            creatorUser=self.user
        )

    def test_modify_steam_user(self):
        self.client.login(username='testuser', password='12345')

        url = reverse('modifySteamUser', kwargs={'id': self.steam_user.id})

        data = {
            'steamID': '5678',
            'realName': 'Modified Name',
            'personaName': 'Modified Persona',
            'country': 'USA',
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)

        self.steam_user.refresh_from_db()

        self.assertEqual(self.steam_user.realName, 'Modified Name')
        self.assertEqual(self.steam_user.steamID, 5678)


    def test_steam_user_modify_invalid_form(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('modifySteamUser', kwargs={'id': self.steam_user.id})
        data = {}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.steam_user.refresh_from_db()

        self.assertEqual(self.steam_user.steamID, 1234)

    def test_steam_user_modify_unauthenticated_user(self):
        url = reverse('modifySteamUser', kwargs={'id': self.steam_user.id})
        data = {}
        response = self.client.post(url, data)
        self.assertRedirects(response, f'/accounts/login/?next={url}', status_code=302,
                             target_status_code=200)

