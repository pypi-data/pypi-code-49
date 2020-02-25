from huscy.appointments.models import Appointment
from huscy.appointments.services import remove_appointment


def test_remove_appointment(appointment):
    remove_appointment(appointment)

    assert not Appointment.objects.exists()
