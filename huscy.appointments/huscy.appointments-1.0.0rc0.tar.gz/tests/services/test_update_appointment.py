from datetime import datetime
from itertools import cycle

import pytest
from model_bakery import baker

from huscy.appointments.services import get_participants, update_appointment


@pytest.mark.freeze_time('2000-12-24T10:00:00')
def test_update_start(appointment):
    start = datetime(2000, 12, 24)
    update_appointment(appointment, start=start)

    appointment.refresh_from_db()
    assert appointment.start == datetime(2000, 12, 24)


@pytest.mark.freeze_time('2000-12-24T10:00:00')
def test_update_start_before_end(appointment):
    with pytest.raises(ValueError) as error:
        update_appointment(appointment, start=datetime(2000, 12, 24, 15))

    assert str(error.value) == 'End must be greater then start.'


@pytest.mark.freeze_time('2000-12-24T10:00:00')
def test_update_start_equals_with_end(appointment):
    with pytest.raises(ValueError) as error:
        update_appointment(appointment, start=appointment.end)

    assert str(error.value) == 'Start and end are the same.'


@pytest.mark.freeze_time('2000-12-24T10:00:00')
def test_update_end(appointment):
    end = datetime(2000, 12, 24, 17)
    update_appointment(appointment, end=end)

    appointment.refresh_from_db()
    assert appointment.end == datetime(2000, 12, 24, 17)


@pytest.mark.freeze_time('2000-12-24T10:00:00')
def test_update_end_before_start(appointment):
    with pytest.raises(ValueError) as error:
        update_appointment(appointment, end=datetime(2000, 12, 24, 9))

    assert str(error.value) == 'End must be greater then start.'


@pytest.mark.freeze_time('2000-12-24T10:00:00')
def test_update_end_equals_with_start(appointment):
    with pytest.raises(ValueError) as error:
        update_appointment(appointment, end=appointment.start)

    assert str(error.value) == 'Start and end are the same.'


def test_update_start_and_end(appointment):
    start = datetime(2000, 12, 24)
    end = datetime(2000, 12, 24, 17)
    update_appointment(appointment, start=start, end=end)

    appointment.refresh_from_db()
    appointment.start = start
    appointment.end = end


def test_update_start_and_end_but_end_is_before_start(appointment):
    with pytest.raises(ValueError) as error:
        update_appointment(appointment,
                           start=datetime(2000, 12, 24, 15), end=datetime(2000, 12, 24, 9))

    assert str(error.value) == 'End must be greater then start.'


def test_update_start_and_end_but_end_equals_with_start(appointment):
    with pytest.raises(ValueError) as error:
        update_appointment(appointment,
                           start=datetime(2000, 12, 24, 10), end=datetime(2000, 12, 24, 10))

    assert str(error.value) == 'Start and end are the same.'


def test_update_resource(appointment):
    resource = baker.make('appointments.Resource', name='C106')
    update_appointment(appointment, resource=resource.name)

    appointment.refresh_from_db()
    assert appointment.resource == resource.name


def test_resource_already_in_use(appointment):
    resource = baker.make('appointments.Resource', name='C106')
    second_appointment = baker.make('appointments.Appointment', start=appointment.start,
                                    end=appointment.end, resource=resource)

    with pytest.raises(ValueError) as error:
        update_appointment(second_appointment, resource=appointment.resource)

    assert str(error.value) == 'Resource is already in use within this time.'


def test_update_owner(appointment, django_user_model):
    user = baker.make(django_user_model)
    update_appointment(appointment, owner=user)

    appointment.refresh_from_db()
    assert appointment.owner == user


def test_update_title(appointment):
    update_appointment(appointment, title='updated title')

    appointment.refresh_from_db()
    assert appointment.title == 'updated title'


def test_update_description(appointment):
    update_appointment(appointment, description='updated description')

    appointment.refresh_from_db()
    assert appointment.description == 'updated description'


def test_add_participants(appointment):
    baker.make('appointments.Invitation', appointment=appointment, participant='Ken Guru', status=1)

    participants = ['Ken Guru', 'Lars Agne', 'Ela Stisch']
    update_appointment(appointment, participants=participants)

    expected_participants = {'Ken Guru': 1, 'Lars Agne': 0, 'Ela Stisch': 0}
    assert get_participants(appointment) == expected_participants


def test_remove_participants(appointment):
    participants = ['Ken Guru', 'Lars Agne', 'Ela Stisch']
    baker.make('appointments.Invitation', appointment=appointment, participant=cycle(participants),
               status=1, _quantity=3)

    update_appointment(appointment, participants=['Ken Guru'])

    assert get_participants(appointment) == {'Ken Guru': 1}


def test_update_appointment_to_no_resource(appointment):
    '''
    This test was implemented to prove a bug fix. The bug didn't allow to update an appointment to
    no resource if another appointment with no resource exists, because update_appointments checked
    if there are appointments for this resource (no resource) and raised an error if there were any.
    '''
    baker.make('appointments.Appointment', start=appointment.start, end=appointment.end)

    update_appointment(appointment, resource='')
