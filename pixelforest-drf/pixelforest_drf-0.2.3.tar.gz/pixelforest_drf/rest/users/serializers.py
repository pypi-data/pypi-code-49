# Imports ##############################################################################################################
from rest_framework import serializers

from pixelforest_drf.users.models import PFUser


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PFUser
