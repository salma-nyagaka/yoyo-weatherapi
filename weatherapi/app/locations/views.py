import json
from statistics import median
import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

from .helpers.constants import SUCCESS_MESSAGE, FORBIDDEN_MESSAGE
from .helpers.validate_params import validate_params
from .helpers.perform_computations import perform_computations


class WeatherDataRetrieveApiView(generics.RetrieveAPIView):
    """ Class to fetch weather data"""

    def get(self, request, city_name):
        """ Function to fetch weather data from
        external weather API"""

        url = settings.API_URL
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
 
            maximum, minimum, average, median = perform_computations(response_data)

            computation_data = {
                "maximum": maximum,
                "minimum": minimum,
                "average": average,
                "median": median
            }

            return_message = {
                "message": SUCCESS_MESSAGE.format("Weather data fetched"),
                "data": computation_data
            }
            return Response(return_message, status=status.HTTP_200_OK)
        return_message = {
            "message": FORBIDDEN_MESSAGE
        }
        return Response(return_message, status=status.HTTP_403_FORBIDDEN)
        