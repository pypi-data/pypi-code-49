from django.contrib.auth import get_user_model
from rest_framework import serializers

from huscy.appointments import models, services


User = get_user_model()


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invitation
        fields = (
            "participant",
        )


class AppointmentSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    participants = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = models.Appointment
        fields = (
            'creator',
            "description",
            "end",
            "id",
            "owner",
            "participants",
            "resource",
            "start",
            "title",
        )

    def to_representation(self, appointment):
        response = super().to_representation(appointment)
        response['participants'] = services.get_participants(appointment)
        return response

    def create(self, validated_data):
        validated_data.pop('owner', None)
        try:
            return services.create_appointment(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(str(e))

    def update(self, appointment, validated_data):
        validated_data.pop('creator', None)
        if 'participants' not in validated_data:
            validated_data['participants'] = []
        try:
            return services.update_appointment(appointment=appointment, **validated_data)
        except Exception as e:
            raise serializers.ValidationError(str(e))


class InvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Invitation
        fields = (
            "appointment",
            "id",
            "participant",
            "status",
        )


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resource
        fields = (
            "id",
            "name",
        )
