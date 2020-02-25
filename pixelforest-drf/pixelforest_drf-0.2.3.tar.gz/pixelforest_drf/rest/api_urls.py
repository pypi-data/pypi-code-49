# Imports ##############################################################################################################
from django.urls import path, include

urlpatterns = [
    path("countries/", include("pixelforest_drf.rest.countries.api_urls")),
    path("companies/", include("pixelforest_drf.rest.companies.api_urls")),
    path("users/", include("pixelforest_drf.rest.users.api_urls")),
]
