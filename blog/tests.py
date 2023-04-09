from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class ViewsTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("index-page"))  
        self.assertTemplateUsed(response, "blog/index.html")



    def test_about(self):
        response = self.client.get(reverse('about-view'))
        self.assertTemplateUsed(response, "blog/about.html")



    def test_contacts(self):
        response = self.client.get(reverse('contacts-view'))
        self.assertTemplateUsed(response, "blog/contacts.html")


    def test_post_create(self):
        response = self.client.get(reverse('post_create-view'))
        self.assertEqual(200, response.status_code)

    def test_post_update(self):
        response = self.client.get(reverse('post_update-view'))
        self.assertEqual(200, response.status_code)