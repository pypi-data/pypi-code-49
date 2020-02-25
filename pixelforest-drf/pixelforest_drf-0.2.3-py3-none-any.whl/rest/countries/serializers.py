# Imports ##############################################################################################################
from rest_framework import serializers

from pixelforest_drf.countries.models import Region, SubRegion, Country


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Region


class SubRegionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SubRegion


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country
