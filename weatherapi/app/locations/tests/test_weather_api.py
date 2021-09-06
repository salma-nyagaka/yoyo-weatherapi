import json
from django.http import response
import pytest
from rest_framework import status
from .base_file import BaseTestCase

from django.test import TestCase
from rest_framework.serializers import ValidationError
from ..helpers.validate_params import validate_params



class TestWeatherApi(BaseTestCase):
    """Test class for the weather API"""

    def test_fetch_weather_data(self):
        """ Test to fetch weather data with correct params"""
        response = self.client.get(
            self.weather_api_url,
            self.right_params,
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

        assert response == ["'day' is required in params"]
