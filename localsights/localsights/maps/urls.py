from django.urls import path
from .views import *


urlpatterns = [
    path("home", HomeView.as_view(), name='home'),
    path("maps", MapView.as_view(), name='maps'),
    path("geocoding/<int:pk>", GeocodingView.as_view(), name='geocoding'),
]
