# Imports #############################################################################################################
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .permissions import FullDjangoModelPermissions


class BaseModelViewSet(viewsets.ModelViewSet):

    permission_classes = [
        IsAuthenticated,
        FullDjangoModelPermissions,
    ]

    authentication_classes = [
        SessionAuthentication,
    ]
