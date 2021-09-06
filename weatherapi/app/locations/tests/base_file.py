from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase
import pdb


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the project"""

    def setUp(self):
        self.client = APIClient()

        self.weather_api_url = reverse(
            "locations:weather-api", args=['Nairobi'])

        self.wrong_key = {
            "key": "80ce3cec537b476a86b161602210599",
            "q": "Nairobi",
            "days": "1"
        }
        self.right_params = {
            "key": "80ce3cec537b476a86b161602210509",
            "q": "Nairobi",
            "days": "1"
        }

        self.no_location_in_params = {
            "days": "1"
        }
        self.no_days_in_params = {
            "q": "Nairobi",
        }
