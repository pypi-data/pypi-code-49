import logging

from django.db.models import DateTimeField, BooleanField
from django.forms import model_to_dict
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from isc_common import delAttr, setAttr
from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditModel
from tracker.models.messages import MessagesManager, MessagesQuerySet, Messages
from tracker.models.messages_state import Messages_state
from tracker.models.messages_theme import Messages_theme
from tracker.models.messages_whom import Messages_whom

logger = logging.getLogger(__name__)


class Messages_viewQuerySet(MessagesQuerySet):
    ...


class Messages_viewManager(MessagesManager):

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "checksum": record.checksum,
            "message": record.message,
            "lastmodified": record.lastmodified,
            "date_create": record.date_create,
            "editing": record.editing,
            "deliting": record.deliting,
            "user_id": record.user.id if record.user else None,
            "parent_id": record.parent_id,
            "user__username": record.user.username if record.user else None,
            "state_id": record.state.id if record.state else None,
            "state__name": record.state.name if record.state else None,
            "theme_id": record.theme.id if record.theme else None,
            "theme__name": record.theme.name if record.theme else None,
            "isFolder": record.isFolder,
            "to_whom": [item.to_whom.id for item in Messages_whom.objects.filter(message_id=record.id)]
        }
        return res

    def get_queryset(self):
        return Messages_viewQuerySet(self.model, using=self._db)


class Messages_view(AuditModel):
    checksum = CodeField(_('Checksum MD5'), unique=True)
    message = DescriptionField(_('Тело сообщения'), null=False, blank=False)
    date_create = DateTimeField(verbose_name='Дата записи', db_index=True, default=timezone.now)
    user = ForeignKeyCascade(User, related_name='user_view', default=None)
    state = ForeignKeyProtect(Messages_state, default=None)
    theme = ForeignKeyProtect(Messages_theme, default=None)
    parent = ForeignKeyProtect("self", blank=True, null=True)
    isFolder = BooleanField(default=False)

    def __str__(self):
        return self.checksum

    objects = Messages_viewManager()

    class Meta:
        managed = False
        db_table = 'tracker_messages_view'
        verbose_name = 'Сообщения'
