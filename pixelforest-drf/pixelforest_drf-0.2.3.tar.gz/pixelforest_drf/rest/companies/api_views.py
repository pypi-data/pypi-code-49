# Imports ##############################################################################################################
from pixelforest_drf.companies.models import CompanyGroup, Company, Subsidiary, Service
from .serializers import CompanyGroupSerializer, CompanySerializer, SubsidiarySerializer, ServiceSerializer
from ..base_api_views import BaseModelViewSet


class CompanyGroupViewSet(BaseModelViewSet):
    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupSerializer


class CompanyViewSet(BaseModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class SubsidiaryViewSet(BaseModelViewSet):
    queryset = Subsidiary.objects.all()
    serializer_class = SubsidiarySerializer


class ServiceViewSet(BaseModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

