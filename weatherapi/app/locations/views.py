import json
import requests
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from rest_framework_api_key.permissions import HasAPIKey

from .helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from .helpers.validate_params import validate_params


class WeatherDataRetrieveApiView(generics.RetrieveAPIView):
    """ Class to fetch weather data"""
    def get(self, request, city_name):
        """ Function to fetch weather data from
        external weather API"""
        url = 'https://api.weatherapi.com/v1/forecast.json'
        params = request.query_params
        key = settings.API_KEY 

        if key is not None:
            # Convert QueryDict to Python Dict
            params_dict = params.dict()

            # Insert values to params 
            params_dict['key'] = key
            params_dict['q'] = city_name
            
            validate_params(params_dict)

            data = requests.get(url, params=params_dict)
            response_data = json.loads(data.content)

            return_message = {
                "message": SUCCESS_MESSAGE.format("Weather data fetched"),
                "data": response_data
            }
            return Response(return_message, status=status.HTTP_200_OK)
        return_message = {
            "message": FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)