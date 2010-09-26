from django.test import TestCase
from django.test.client import Client


class UrlTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_I18NRedirection(self):
        # Issue a GET request.
        response = self.client.get('/')
        self.assertRedirects(response, '/en')

    def test_I18NOldRedirection(self):
        # Issue a GET request.
        response = self.client.get('/fre',)
        self.assertRedirects(
            response,
            '/fr',
            status_code=301
        )
