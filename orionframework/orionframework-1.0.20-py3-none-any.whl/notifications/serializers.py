from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from orionframework.notifications.models import Device


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        exclude = ('user',)
