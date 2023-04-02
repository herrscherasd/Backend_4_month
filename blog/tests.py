from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class HelloViewTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))  
        excepted_data = "Hello"
        self.assertEqual(excepted_data, response.content.decode())
        self.assertEqual(500, response.status_code)

class AboutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about(self):
        response = self.client.get(reverse('about-views'))
        excepted_data = "Какая-нибудь строка 2"
        self.assertEqual(excepted_data, response.content.decode())

class ContactsViewTestCase(TestCase):
    def setup(self):
        self.client = Client()
    
    def test_contacts(self):
        response = self.client.get(reverse('contacts-views'))
        excepted_data = 'Какая-нибудь строка'
        self.assertEqual(excepted_data, response.content.decode())