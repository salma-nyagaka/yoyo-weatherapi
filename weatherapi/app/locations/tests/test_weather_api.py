import os
import json
import pytest
from rest_framework import status

from .base_file import BaseTestCase
from ..helpers.perform_computations import add
from django.conf import settings


class TestWeatherApi(BaseTestCase):
    """Test class for the weather API"""

    def test_fetch_weather_data(self):
        """ Test to fetch weather data with correct params"""
        response = self.client.get(
            self.weather_api_url,
            self.params,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_validate_params(self):
        """ Test to validate days in params """

        days_response = self.client.get(
            self.weather_api_url,
            self.no_days_in_params,
            format="json"
        )

        response = json.loads(days_response.content)

        assert response == {'status': False,
                            "error": [
                                'days is required in params'
                            ]
                            }

    def test_no_key(self):
        """ Test to check for response
        when no key is passed"""
        settings.API_KEY = ''
        response = self.client.get(
            self.weather_api_url,
            self.params,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_wrong_key(self):
        """ Test to check for response
        when wrong key is passed"""
        settings.API_KEY = 'trestrestgett'
        response = self.client.get(
            self.weather_api_url,
            self.params,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sum(self):
        """ Test sum of two numbers """
        result = add(3, 3)
        self.assertEquals(6, result)

    def teardown_method(self, method):
        settings.API_KEY = os.getenv('API_KEY')
