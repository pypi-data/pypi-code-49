from datetime import datetime

import pytest

from huscy.appointments.services import create_appointment


@pytest.fixture
def start():
    return datetime(2000, 12, 24, 10)


@pytest.fixture
def end():
    return datetime(2000, 12, 24, 16)


def test_create_appointment(user, start, end, resource):
    appointment = create_appointment(user, start, end, resource=resource.name)

    assert appointment.start == start
    assert appointment.end == end
    assert appointment.resource == resource.name
    assert appointment.invitations.count() == 0
    assert list(appointment.invitations.all()) == []


def test_end_is_before_start(user, start):
    end = datetime(2000, 12, 24, 8)

    with pytest.raises(ValueError) as error:
        create_appointment(user, start, end)

    assert str(error.value) == 'End must be greater then start.'


def test_end_equals_with_start(user, start):
    with pytest.raises(ValueError) as error:
        create_appointment(user, start=start, end=start)

    assert str(error.value) == 'Start and end are the same.'


def test_resource_does_not_exist(user, start, end):
    with pytest.raises(ValueError) as error:
        create_appointment(user, start, end, resource='room1')

    assert str(error.value) == 'Resource: room1 does not exist'


def test_overlap_with_other_appointment_for_given_resource(user, start, end, resource):
    create_appointment(user, start, end, resource=resource.name)

    with pytest.raises(ValueError) as error:
        create_appointment(user, start, datetime(2000, 12, 24, 15), resource=resource.name)

    assert str(error.value) == 'Resource is already in use within this time.'


def test_create_with_participants(user, start, end):
    appointment = create_appointment(user, start, end, participants=['user1', 'user2'])

    assert appointment.invitations.count() == 2
    assert sorted(list(appointment.invitations.values_list('participant', flat=True))) == ['user1', 'user2']


def test_create_two_appoinments_without_resource(user, start, end):
    '''
    This test was implemented to prove a bug fix. The bug didn't allow to create two appointments
    without resource because create_appointments checked if there are appointments for this
    resource (no resource) and raised an error if there were any.
    '''
    create_appointment(user, start, end)
    create_appointment(user, start, end)
