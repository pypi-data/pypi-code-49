from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse

from huscy.appointments.models import Appointment
from huscy.appointments.serializers import AppointmentSerializer


def test_admin_user_can_view_appointments(admin_client):
    response = admin_client.get(reverse('appointment-list'))

    assert status.HTTP_200_OK == response.status_code


def test_user_without_permissions_can_view_appointments(client):
    response = client.get(reverse('appointment-list'))

    assert status.HTTP_200_OK == response.status_code


def test_user_can_only_view_own_appointments(client, appointment, django_user_model):
    baker.make(Appointment, owner=baker.make(django_user_model))

    response = client.get(reverse('appointment-list'))

    assert AppointmentSerializer([appointment], many=True).data == response.json()


def test_anonymous_user_cannot_view_appointments(anonymous_client):
    response = anonymous_client.get(reverse('appointment-list'))

    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_retrieve_not_allowed(client):
    response = client.get(reverse('appointment-detail', kwargs=dict(pk=1)))

    assert status.HTTP_405_METHOD_NOT_ALLOWED == response.status_code
