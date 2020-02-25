from model_bakery import baker

from huscy.appointments.models import Appointment, Invitation


def test_str_method():
    appointment = baker.prepare(Appointment, title='appointment title')
    pending = Invitation.STATUS.get_value('pending')
    invitation = Invitation(appointment=appointment, participant='participant name', status=pending)

    assert str(invitation) == 'appointment title -- participant name (Pending)'
