from django.urls import include, path
from .views import WeatherDataRetrieveApiView


urlpatterns = [
    path('', WeatherDataRetrieveApiView.as_view(), name='weather-api'),

]
