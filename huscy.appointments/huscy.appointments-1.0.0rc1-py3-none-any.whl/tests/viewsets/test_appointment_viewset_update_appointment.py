from datetime import datetime
from itertools import cycle

from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse

from huscy.appointments.models import Appointment, Invitation


def test_admin_can_update_appointment(admin_client, appointment):
    response = update_appointment(admin_client, appointment)

    assert status.HTTP_200_OK == response.status_code, response.json()


def test_user_without_permission_can_update_appointment(client, appointment):
    response = update_appointment(client, appointment)

    assert status.HTTP_200_OK == response.status_code, response.json()


def test_user_cannot_update_appointment_from_different_owner(client, django_user_model):
    appointment = baker.make(Appointment, owner=baker.make(django_user_model))

    response = update_appointment(client, appointment)

    assert status.HTTP_404_NOT_FOUND == response.status_code, response.json()


def test_anonymous_user_cannot_update_appointment(anonymous_client, appointment):
    response = update_appointment(anonymous_client, appointment)

    assert status.HTTP_403_FORBIDDEN == response.status_code, response.json()


def test_update_owner(client, django_user_model, appointment):
    new_owner = baker.make(django_user_model)

    response = update_appointment(client, appointment, owner=new_owner.pk)

    assert new_owner.pk == response.json()['owner'], response.json()


def test_add_participants(client, django_user_model, appointment):
    users = baker.make(django_user_model, username=cycle(['user2', 'user3']), _quantity=2)
    usernames = [user.username for user in users]

    assert Invitation.objects.count() == 0

    response = update_appointment(client, appointment, participants=usernames)

    expected_participants = dict.fromkeys(usernames, Invitation.STATUS.get_value('pending'))
    assert expected_participants == response.json()['participants']

    assert Invitation.objects.filter(appointment=appointment, participant='user2').exists()
    assert Invitation.objects.filter(appointment=appointment, participant='user3').exists()


def test_remove_participants(client, django_user_model, appointment):
    users = baker.make(django_user_model, username=cycle(['user2', 'user3']), _quantity=2)
    usernames = [user.username for user in users]
    baker.make(Invitation, appointment=appointment, participant=cycle(usernames), _quantity=2)

    assert Invitation.objects.count() == 2

    response = update_appointment(client, appointment)

    assert {} == response.json()['participants']
    assert Invitation.objects.filter(appointment=appointment).count() == 0


def update_appointment(client, appointment, owner=None, participants=[]):
    return client.put(
        reverse('appointment-detail', kwargs=dict(pk=appointment.pk)),
        data=dict(
            end=datetime(2000, 1, 1, 12),
            owner=owner or appointment.owner.pk,
            participants=participants,
            start=datetime(2000, 1, 1),
        ),
    )
