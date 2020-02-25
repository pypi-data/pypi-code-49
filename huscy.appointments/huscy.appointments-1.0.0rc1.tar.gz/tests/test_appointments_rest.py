from itertools import cycle

import pytest
from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse

from huscy.appointments.models import Invitation
from huscy.appointments.serializers import AppointmentSerializer

STATUS_PENDING = Invitation.STATUS.get_value('pending')


@pytest.mark.django_db
def test_user_gets_participants_of_appointment(client, user, appointment):
    baker.make(Invitation, status=0, participant=cycle(['Asterix', 'Obelix']),
               appointment=appointment, _quantity=2)

    response = client.get(reverse('appointment-participants', kwargs={'pk': appointment.id}),
                          content_type='application/json')

    assert status.HTTP_200_OK == response.status_code
    assert {'Asterix': STATUS_PENDING, 'Obelix': STATUS_PENDING} == response.json()


@pytest.mark.django_db
def test_user_accepts_appointment(client, user, appointment):
    baker.make(Invitation, appointment=appointment, participant='Tester', status=0)

    response = client.post(reverse('appointment-accept', kwargs={'pk': appointment.id}),
                           data={'participant': 'Tester'})
    json_response = response.json()

    assert status.HTTP_200_OK == response.status_code
    assert AppointmentSerializer(appointment).data == json_response

    invitation = Invitation.objects.get(appointment_id=appointment.id, participant='Tester')
    assert invitation.status == Invitation.STATUS.get_value('accepted')


@pytest.mark.django_db
def test_user_declines_appointment(client, user, appointment):
    baker.make(Invitation, appointment=appointment, participant='Tester', status=0)

    response = client.post(reverse('appointment-decline', kwargs={'pk': appointment.id}),
                           data={'participant': 'Tester'})
    json_response = response.json()

    assert status.HTTP_200_OK == response.status_code
    assert AppointmentSerializer(appointment).data == json_response

    invitation = Invitation.objects.get(appointment_id=appointment.id, participant='Tester')
    assert invitation.status == Invitation.STATUS.get_value('declined')
