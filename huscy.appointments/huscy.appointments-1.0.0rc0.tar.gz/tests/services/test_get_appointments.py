from datetime import datetime, timedelta
from operator import attrgetter

import pytest
from model_bakery import baker

from huscy.appointments.services import get_appointments


@pytest.fixture
def appointments(user):
    return list(create_appointments(user))


def test_get_all_appointments(appointments):
    result = list(get_appointments())

    assert sorted(appointments, key=attrgetter('start'), reverse=True) == result


def test_get_appointments_for_resource(appointments):
    result = list(get_appointments(resource='A110'))

    assert sorted(appointments[:39], key=attrgetter('start'), reverse=True) == result


def test_get_appointments_with_multiple_resources(appointments):
    expected_appointments = (appointments[11:13] + appointments[21:26] + appointments[31:39] +
                             appointments[50:52] + appointments[60:65] + appointments[70:78])

    result = list(get_appointments(resource=['A110', 'C206'], from_time=datetime(2000, 1, 1, 15)))

    assert sorted(expected_appointments, key=attrgetter('start'), reverse=True) == result


def test_get_appointments_within_time_range(appointments):
    expected_appointments = (appointments[5:11] + appointments[15:24] + appointments[26:37] +
                             appointments[44:50] + appointments[54:63] + appointments[65:76])

    result = list(get_appointments(from_time=datetime(2000, 1, 1, 12),
                                   to_time=datetime(2000, 1, 1, 14, 30)))

    assert sorted(expected_appointments, key=attrgetter('start'), reverse=True) == result


def test_get_appointments_within_time_range_and_for_resource(appointments):
    expected_appointments = (appointments[5:11] + appointments[15:24] + appointments[26:37])

    result = list(get_appointments(from_time=datetime(2000, 1, 1, 12),
                                   to_time=datetime(2000, 1, 1, 14, 30),
                                   resource='A110'))

    assert sorted(expected_appointments, key=attrgetter('start'), reverse=True) == result


def test_get_appointments_for_owner(appointments, user):
    result = list(get_appointments(owner=user.id))

    assert sorted(appointments, key=attrgetter('start'), reverse=True) == result

    result = get_appointments(owner=2)

    assert [] == list(result)


@pytest.mark.freeze_time('2000-01-01T10:00:00')
@pytest.mark.parametrize('from_time, duration_in_hours, count', [
    # timeframe is somewhere before appointment.start
    (datetime(1999, 12, 31, 10), 2, 0),     # to_time = 1999-12-31T12:00
    # to_time equals with appointment.start
    (datetime(2000, 1, 1, 8), 2, 0),        # to_time = 2000-01-01T10:00
    # timeframe overlaps appointment.start
    (datetime(2000, 1, 1, 9), 2, 1),        # to_time = 2000-01-01T11:00
    # from_time equals with appointment.start
    (datetime(2000, 1, 1, 10), 2, 1),       # to_time = 2000-01-01T12:00

    # timeframe is between appointment.start and appointment.end
    (datetime(2000, 1, 1, 10, 30), 2, 1),   # to_time = 2000-01-01T12:30

    # to_time equals with appointment.end
    (datetime(2000, 1, 1, 11), 2, 1),       # to_time = 2000-01-01T13:00
    # timeframe overlaps appointment.end
    (datetime(2000, 1, 1, 12), 2, 1),       # to_time = 2000-01-01T14:00
    # from_time equals with appointment.end
    (datetime(2000, 1, 1, 13), 2, 0),       # to_time = 2000-01-01T15:00
    # timeframe is somewene after appointment.end
    (datetime(2000, 1, 2, 20), 2, 0),       # to_time = 2000-01-02T22:00

    # timeframe equals appointment
    (datetime(2000, 1, 1, 10), 3, 1),       # to_time = 2000-01-01T13:00

    # timeframe starts before appointment.start but to_time equals with appointment.end
    (datetime(2000, 1, 1, 9), 4, 1),        # to_time = 2000-01-01T13:00
    # timeframe starts at appointment.start but overlaps appointment.end
    (datetime(2000, 1, 1, 10), 4, 1),       # to_time = 2000-01-01T14:00
    # timeframe starts before appointment.start and ends after appointment.end
    (datetime(2000, 1, 1, 9), 5, 1),        # to_time = 2000-01-01T14:00
])
def test_get_single_appointment(appointment, from_time, duration_in_hours, count):
    ''' appointment is from 10:00 to 13:00 '''
    to_time = from_time + timedelta(hours=duration_in_hours)
    assert count == len(get_appointments(from_time=from_time, to_time=to_time))


def create_appointments(user):
    """
    This function creates appointments for the rooms A110 and C206. For each room, there are
    appointments that last one, two and a half and four hours. For every duration there's a start
    time from 09:00 to 15:00 every half an hour.
    We know, that it is impossible to have such a scenario with overlapping appointments for one
    resource. It's just for testing purposes to see, if this function returns all the appointments
    within the given timerange
    The table below lists all appointments with their start and end time.

    Duration:   one hour                two and a half hours    four hours
    Room A110    1 - 09:00-10:00        14 - 09:00-11:30        27 - 09:00-13:00
                 2 - 09:30-10:30        15 - 09:30-12:00        28 - 09:30-13:30
                 3 - 10:00-11:00        16 - 10:00-12:30        29 - 10:00-14:00
                 4 - 10:30-11:30        17 - 10:30-13:00        30 - 10:30-14:30
                 5 - 11:00-12:00        18 - 11:00-13:30        31 - 11:00-15:00
                 6 - 11:30-12:30        19 - 11:30-14:00        32 - 11:30-15:30
                             ...                     ...                     ...
                10 - 13:30-14:30        23 - 13:30-16:00        36 - 13:30-17:30
                11 - 14:00-15:00        24 - 14:00-16:30        37 - 14:00-18:00
                12 - 14:30-15:30        25 - 14:30-17:00        38 - 14:30-18:30
                13 - 15:00-16:00        26 - 15:00-17:30        39 - 15:00-19:00

    Room C206   40 - 09:00-10:00        53 - 09:00-11:30        66 - 09:00-13:00
                41 - 09:30-10:30        54 - 09:30-12:00        67 - 09:30-13:30
                42 - 10:00-11:00        55 - 10:00-12:30        68 - 10:00-14:00
                43 - 10:30-11:30        56 - 10:30-13:00        69 - 10:30-14:30
                44 - 11:00-12:00        57 - 11:00-13:30        70 - 11:00-15:00
                45 - 11:30-12:30        58 - 11:30-14:00        71 - 11:30-15:30
                             ...                     ...                     ...
                49 - 13:30-14:30        62 - 13:30-16:00        75 - 13:30-17:30
                50 - 14:00-15:00        63 - 14:00-16:30        76 - 14:00-18:00
                51 - 14:30-15:30        64 - 14:30-17:00        77 - 14:30-18:30
                52 - 15:00-16:00        65 - 15:00-17:30        78 - 15:00-19:00
    """
    for resource in ['A110', 'C206']:
        for duration in [timedelta(hours=1), timedelta(hours=2, minutes=30), timedelta(hours=4)]:
            start = datetime(2000, 1, 1, 9)
            for delta in [timedelta(minutes=minutes) for minutes in range(0, 6*60+1, 30)]:
                yield baker.make('appointments.Appointment', start=start+delta,
                                 end=start+delta+duration, resource=resource, owner_id=user.id)
