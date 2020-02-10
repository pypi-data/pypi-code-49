from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "email", "first_name", "last_name")


class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = "__all__"
        model = None
