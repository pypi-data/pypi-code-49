# Imports ##############################################################################################################
from django.urls import path, include

from rest_framework import routers

from .api_views import UsersViewSet

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, 'user')

urlpatterns = [
    path("", include(router.urls)),
]