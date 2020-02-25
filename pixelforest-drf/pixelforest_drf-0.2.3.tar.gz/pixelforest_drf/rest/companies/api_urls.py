# Imports ##############################################################################################################
from django.urls import path, include

from rest_framework import routers

from .api_views import CompanyGroupViewSet, CompanyViewSet, SubsidiaryViewSet, ServiceViewSet


router = routers.SimpleRouter()
router.register(r'company_group', CompanyGroupViewSet, 'company_group')
router.register(r'company', CompanyViewSet, 'company')
router.register(r'subsidiary', SubsidiaryViewSet, 'subsidiary')
router.register(r'service', ServiceViewSet, 'service')

urlpatterns = [
    path("", include(router.urls)),
]