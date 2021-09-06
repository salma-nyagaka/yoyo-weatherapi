from django.urls import include, path
from .views import WeatherDataRetrieveApiView


urlpatterns = [
    path('<str:city_name>/', WeatherDataRetrieveApiView.as_view(), name='weather-api'),

]
