from enum import Enum
import secrets

from django.conf import settings
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import PositiveSmallIntegerField
from django.db.models import TextField
from django.utils.translation import gettext_lazy as _


class Appointment(Model):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name=_('Owner'))
    title = CharField(max_length=255, blank=True, default=_('New appointment'),
                      verbose_name=_('Title'))
    description = TextField(blank=True, default='', verbose_name=_('Description'))
    start = DateTimeField(verbose_name=_('Start'))
    end = DateTimeField(verbose_name=_('End'))
    resource = CharField(max_length=128, blank=True, default='', verbose_name=_('Resource'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')


class Invitation(Model):
    class STATUS(Enum):
        pending = (0, _('Pending'))
        accepted = (1, _('Accepted'))
        declined = (2, _('Declined'))

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    appointment = ForeignKey(Appointment, on_delete=CASCADE, related_name='invitations',
                             verbose_name=_('Appointment'))
    participant = CharField(max_length=128, verbose_name=_('Participant'))
    status = PositiveSmallIntegerField(choices=[x.value for x in STATUS],
                                       default=STATUS.get_value('pending'),
                                       verbose_name=_('Status'))

    def __str__(self):
        return f'{self.appointment.title} -- {self.participant} ({self.get_status_display()})'

    class Meta:
        verbose_name = _('Invitation')
        verbose_name_plural = _('Invitations')


class Reminder(Model):
    appointment = ForeignKey(Appointment, on_delete=CASCADE, related_name='reminders',
                             verbose_name=_('Appointment'))
    remind_at = DateTimeField(verbose_name=_('Remind at'))

    class Meta:
        verbose_name = _('Reminder')
        verbose_name_plural = _('Reminders')


class Resource(Model):
    name = CharField(max_length=128, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')


def create_token():
    return secrets.token_urlsafe(64)


class Token(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name=_('User'))
    key = CharField(max_length=64, unique=True, default=create_token, verbose_name=_('Key'))

    class Meta:
        verbose_name = _('Token')
        verbose_name_plural = _('Tokens')
