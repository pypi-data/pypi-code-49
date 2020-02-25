# Imports #############################################################################################################
from ..base_api_views import BaseModelViewSet
from pixelforest_drf.countries.models import Region, SubRegion, Country
from .serializers import RegionSerializer, SubRegionSerializer, CountriesSerializer


class RegionViewSet(BaseModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class SubRegionViewSet(BaseModelViewSet):
    queryset = SubRegion.objects.all()
    serializer_class = SubRegionSerializer


class CountriesViewSet(BaseModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer
