from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class HelloViewTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))  
        excepted_data = "Hello"
        self.assertEqual(excepted_data, response.context.decode())
        self.assertEqual(500, response.status_code)