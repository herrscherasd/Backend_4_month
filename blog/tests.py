from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class ViewsTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))  
        excepted_data = "Hello"
        self.assertEqual(excepted_data, response.content.decode())
        self.assertEqual(500, response.status_code)
        self.assertEqual("Alex", response["name"])

    def test_about(self):
        response = self.client.get(reverse('about-views'))
        excepted_data = "Какая-нибудь строка"
        self.assertEqual(excepted_data, response.content.decode())

    def test_contacts(self):
        response = self.client.get(reverse('contacts-views'))
        excepted_data = 'Какая-нибудь строка 2'
        self.assertEqual(excepted_data, response.content.decode())

