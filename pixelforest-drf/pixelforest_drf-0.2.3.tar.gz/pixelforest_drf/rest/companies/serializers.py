# Imports ##############################################################################################################
from rest_framework import serializers

from pixelforest_drf.companies.models import CompanyGroup, Company, Subsidiary, Service


class CompanyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CompanyGroup


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Company


class SubsidiarySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subsidiary


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Service
