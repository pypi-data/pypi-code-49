from datetime import datetime

from django.db import transaction

from huscy.appointments import models, validators


@transaction.atomic
def create_appointment(creator, start, end, title='', description='', resource=None, participants=[]):
    validators.validate_start_end(start, end)
    validators.validate_resource_exists(resource)

    if resource:
        appointments = get_appointments(from_time=start, to_time=end, resource=resource)
        if appointments.exists():
            raise ValueError("Resource is already in use within this time.")

    appointment = models.Appointment.objects.create(
        owner=creator,
        start=start,
        end=end,
        title=title,
        description=description,
        resource=resource or '',
    )

    if participants:
        set_participants(appointment, participants)

    return appointment


@transaction.atomic
def update_appointment(appointment, owner=None, title=None, description=None, resource=None,
                       start=None, end=None, participants=None):

    if start is not None and end is not None:
        validators.validate_start_end(start, end)
        appointment.start = start
        appointment.end = end
    elif start is not None:
        validators.validate_start_end(start, appointment.end)
        appointment.start = start
    elif end is not None:
        validators.validate_start_end(appointment.start, end)
        appointment.end = end

    if resource is not None:
        validators.validate_resource_exists(resource)
        appointment.resource = resource

    if resource:
        appointments = get_appointments(from_time=appointment.start, to_time=appointment.end,
                                        resource=appointment.resource)
        if appointments.exclude(pk=appointment.pk).exists():
            raise ValueError("Resource is already in use within this time.")

    appointment.owner = owner or appointment.owner
    appointment.title = title or appointment.title
    appointment.description = description or appointment.description

    appointment.save()

    # now proceed to set participants
    if participants is not None:
        set_participants(appointment, participants)

    return appointment


def remove_appointment(appointment):
    appointment.delete()


def get_appointments(from_time=datetime.min, to_time=datetime.max, resource=None, owner=None):
    qs = models.Appointment.objects
    qs = qs.exclude(start__gte=to_time)
    qs = qs.exclude(end__lte=from_time)
    if resource:
        if type(resource) == list:
            qs = qs.filter(resource__in=resource)
        else:
            qs = qs.filter(resource=resource)
    if owner:
        qs = qs.filter(owner=owner)
    qs = qs.order_by('-start')
    return qs


def get_participants(appointment):
    return dict(appointment.invitations.values_list('participant', 'status'))


def set_participants(appointment, participants):
    current_participants = set(appointment.invitations.values_list('participant', flat=True))

    # create new participants
    new_participants = set(participants) - set(current_participants)
    new_invitations = [models.Invitation(appointment=appointment, participant=participant)
                       for participant in new_participants]
    models.Invitation.objects.bulk_create(new_invitations)

    # remove participants
    qs = models.Invitation.objects.filter(appointment=appointment,
                                          participant__in=(
                                              set(current_participants)-set(participants)
                                          ))
    qs.delete()

    return appointment


def accept_appointment(appointment_id, participant):
    invitation = (models.Invitation.objects
                                   .select_related('appointment')
                                   .get(appointment_id=appointment_id, participant=participant))

    invitation.status = models.Invitation.STATUS.get_value('accepted')
    invitation.save()
    return invitation.appointment


def decline_appointment(appointment_id, participant):
    invitation = (models.Invitation.objects
                                   .select_related('appointment')
                                   .get(appointment_id=appointment_id, participant=participant))

    invitation.status = models.Invitation.STATUS.get_value('declined')
    invitation.save()
    return invitation.appointment


def get_resources():
    return models.Resource.objects.all()
