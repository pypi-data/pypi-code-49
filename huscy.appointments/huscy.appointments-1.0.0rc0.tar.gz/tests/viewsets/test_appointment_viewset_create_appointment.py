from datetime import datetime
from itertools import cycle

from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse

from huscy.appointments.models import Invitation


def test_admin_can_create_appointment(admin_client):
    response = create_appointment(admin_client)

    assert status.HTTP_201_CREATED == response.status_code, response.json()


def test_user_without_permission_can_create_appointment(client):
    response = create_appointment(client)

    assert status.HTTP_201_CREATED == response.status_code, response.json()


def test_anonymous_user_cannot_create_appointment(anonymous_client):
    response = create_appointment(anonymous_client)

    assert status.HTTP_403_FORBIDDEN == response.status_code, response.json()


def test_creator_is_user_of_the_appointment(client, user):
    response = create_appointment(client)

    assert user.id == response.json()['owner']


def test_create_appointment_with_participants(client, django_user_model):
    users = baker.make(django_user_model, username=cycle(['user2', 'user3']), _quantity=2)
    usernames = [user.username for user in users]

    response = create_appointment(client, usernames)
    appointment = response.json()

    expected_participants = dict.fromkeys(usernames, Invitation.STATUS.get_value('pending'))
    assert expected_participants == appointment['participants']

    assert Invitation.objects.filter(appointment_id=appointment['id'], participant='user2').exists()
    assert Invitation.objects.filter(appointment_id=appointment['id'], participant='user3').exists()


def create_appointment(client, participants=[]):
    return client.post(
        reverse('appointment-list'),
        data=dict(
            end=datetime(2000, 1, 1, 12),
            participants=participants,
            start=datetime(2000, 1, 1),
        ),
    )
