from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse

from huscy.appointments.models import Appointment


def test_admin_can_delete_appointment(admin_client, appointment):
    response = delete_appointment(admin_client, appointment)

    assert status.HTTP_204_NO_CONTENT == response.status_code, response.json()


def test_user_without_permission_can_delete_appointment(client, appointment):
    response = delete_appointment(client, appointment)

    assert status.HTTP_204_NO_CONTENT == response.status_code, response.json()


def test_user_cannot_delete_appointment_from_different_owner(client, django_user_model):
    appointment = baker.make(Appointment, owner=baker.make(django_user_model))

    response = delete_appointment(client, appointment)

    assert status.HTTP_404_NOT_FOUND == response.status_code, response.json()


def test_anonymous_user_cannot_delete_appointment(anonymous_client, appointment):
    response = delete_appointment(anonymous_client, appointment)

    assert status.HTTP_403_FORBIDDEN == response.status_code, response.json()


def delete_appointment(client, appointment):
    return client.delete(reverse('appointment-detail', kwargs=dict(pk=appointment.pk)))
