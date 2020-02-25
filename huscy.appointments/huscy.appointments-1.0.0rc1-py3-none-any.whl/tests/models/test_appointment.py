from model_bakery import baker

from huscy.appointments.models import Appointment


def test_str_method():
    appointment = baker.prepare(Appointment, title='appointment title')

    assert str(appointment) == 'appointment title'
