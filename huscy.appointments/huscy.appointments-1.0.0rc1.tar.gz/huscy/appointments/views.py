from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from huscy.appointments import filters, serializers, services


class AppointmentsViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                          mixins.UpdateModelMixin, viewsets.GenericViewSet):
    filterset_class = filters.AppointmentFilter
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return services.get_appointments()
        return services.get_appointments(owner=user)

    @action(detail=True, methods=['GET'], name='participants')
    def participants(self, request, *args, **kwargs):
        participants = services.get_participants(self.get_object())
        return Response(participants)

    @action(detail=True, methods=['POST'], name='accept appointment')
    def accept(self, request, *args, **kwargs):
        appointment = self.get_object()
        participant = request.data['participant']
        if appointment and participant:
            app = services.accept_appointment(appointment_id=appointment.id, participant=participant)
            return Response(serializers.AppointmentSerializer(app).data)
        return Response("Something was going wrong!")

    @action(detail=True, methods=['POST'], name='decline appointment')
    def decline(self, request, *args, **kwargs):
        appointment = self.get_object()
        participant = request.data['participant']
        if appointment and participant:
            app = services.decline_appointment(appointment_id=appointment.id, participant=participant)
            return Response(serializers.AppointmentSerializer(app).data)
        return Response("Something was going wrong!")

    def perform_destroy(self, instance):
        services.remove_appointment(instance)


class ResourcesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = services.get_resources()
    serializer_class = serializers.ResourceSerializer
