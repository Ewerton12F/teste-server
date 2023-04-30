from django.test import TestCase

from .models import Services


class ModelTesting(TestCase):
    def setUp(self):
        self.api = Services.objects.create(
            title="Test", smalldesc="Test", largedesc="Test", icon="test.svg"
        )

    def test_api_model(self):
        api = self.api
        self.assertTrue(isinstance(api, Services))
        self.assertEqual(str(api), "Test")
