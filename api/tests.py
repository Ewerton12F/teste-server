from .models import Services
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ModelTesting(TestCase):
    def setUp(self):
        self.api = Services.objects.create(
            title="Test", smalldesc="Test", largedesc="Test", icon="test.svg"
        )

    def test_api_model(self):
        api = self.api
        self.assertTrue(isinstance(api, Services))
        self.assertEqual(str(api), "Test")


class ServiceTests(APITestCase):
    def test_view_service(self):
        url = reverse("api:services-list")
        response = self.client.get(url, format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #
    # def create_service(self):
    #     data = {
    #         "title": "Test Service Title",
    #         "smalldesc": "Test Small Description",
    #         "largedesc": "Test Large Description",
    #         "icon": "Test_icon.svg",
    #     }
    #     url = reverse("api:services-list")
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
