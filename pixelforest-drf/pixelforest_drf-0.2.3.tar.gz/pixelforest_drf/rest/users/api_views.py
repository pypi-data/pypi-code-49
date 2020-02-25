# Imports #############################################################################################################
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from pixelforest_drf.users.models import PFUser

from .serializers import UsersSerializer
from ..permissions import FullDjangoModelPermissions

User = get_user_model()

if User is not PFUser:
    raise ImproperlyConfigured("Pf User is not the User model")


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [FullDjangoModelPermissions]

    @action(detail=False, methods=['get'], url_path="me", url_name="me", permission_classes=[IsAuthenticated])
    def me(self, request):
        """ Return only the related Api User fields"""
        queryset = self.get_queryset().filter(pk=request.user.pk)
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)
