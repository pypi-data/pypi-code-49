# Imports ##############################################################################################################
from django.urls import path, include

from .api_views import RegionViewSet, SubRegionViewSet, CountriesViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'region', RegionViewSet, 'region')
router.register(r'sub_region', SubRegionViewSet, 'sub_region')
router.register(r'countries', CountriesViewSet, 'countries')

urlpatterns = [
    path("", include(router.urls)),
]