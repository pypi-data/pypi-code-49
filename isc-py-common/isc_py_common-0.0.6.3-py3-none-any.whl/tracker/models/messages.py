import hashlib
import logging

from django.db.models import DateTimeField
from django.forms import model_to_dict
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from isc_common import setAttr, getAttr, delAttr
from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_tree_grid_manager import CommonTreeGridManager
from isc_common.models.audit import AuditModel, AuditQuerySet
from tracker.models.messages_state import Messages_state
from tracker.models.messages_theme import Messages_theme

logger = logging.getLogger(__name__)


class MessagesQuerySet(AuditQuerySet):
    auto_tracks = ["auto_from_error", "item_maker"]

    def create(self, **kwargs):
        from tracker.models.messages_whom import Messages_whom

        obj = self.model(**kwargs)
        obj.message = f'<pre>{kwargs.get("message")}</pre>'
        obj.checksum = hashlib.md5(obj.message.encode()).hexdigest()

        self._for_write = True

        if obj.theme.code in self.auto_tracks:
            try:
                developer = User.objects.get(username='developer')
                obj = Messages.objects.get(checksum=obj.checksum, state=Messages_state.objects.get(code="new"))
                Messages_whom.objects.get_or_create(to_whom=developer, message=obj)
            except Messages.DoesNotExist:
                obj.save(force_insert=True, using=self.db)
        else:
            obj.save(force_insert=True, using=self.db)
        return obj


class MessagesManager(CommonTreeGridManager):

    @staticmethod
    def getRecord(record):
        from tracker.models.messages_whom import Messages_whom
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
            "to_whom": [item.to_whom.id for item in Messages_whom.objects.filter(message_id=record.id)]
        }
        return res

    def get_queryset(self):
        return MessagesQuerySet(self.model, using=self._db)

    def createAutoErrorFromRequest(self, request, printRequest=False, function=None):
        request = DSRequest(request=request)
        data = request.get_data()
        setAttr(data, 'state', Messages_state.objects.get(code="new"))
        setAttr(data, 'theme', Messages_theme.objects.get(code="auto_from_error"))
        message = getAttr(data, 'message', None)
        user_id = getAttr(data, 'user_id', None)
        setAttr(data, 'user', User.objects.get(id=user_id))

        if message and isinstance(message, list):
            message = '\n'.join(message)
            setAttr(data, 'message', message)
        return super().create(**data)

    def createFromRequest(self, request, printRequest=False, function=None):
        request = DSRequest(request=request)
        data = request.get_data()
        data_clone = data.copy()
        delAttr(data_clone, 'user__username')
        delAttr(data_clone, 'state__name')
        delAttr(data_clone, 'theme__name')
        delAttr(data_clone, 'isFolder')
        delAttr(data_clone, 'to_whom_id')
        delAttr(data_clone, 'to_whom__username')
        to_whom=data.get('to_whom')
        delAttr(data_clone, 'to_whom')
        message = super().create(**data_clone)
        if isinstance(to_whom, list):
            from tracker.models.messages_whom import Messages_whom
            for user_id in data.get('to_whom'):
                Messages_whom.objects.get_or_create(to_whom_id=user_id, message=message)

        res = model_to_dict(message)
        setAttr(data, 'isFolder', False)
        data.update(res)
        return data

    def updateFromRequest(self, request, printRequest=False):
        from tracker.models.messages_whom import Messages_whom

        request = DSRequest(request=request)
        data = request.get_data()
        data_clone = data.copy()
        delAttr(data_clone, 'user__username')
        delAttr(data_clone, 'user')

        delAttr(data_clone, 'to_whom__username')
        delAttr(data_clone, 'to_whom_id')
        delAttr(data_clone, 'to_whom')

        delAttr(data_clone, 'state__name')
        delAttr(data_clone, 'state')

        delAttr(data_clone, 'theme__name')
        delAttr(data_clone, 'theme')

        delAttr(data_clone, 'id')
        delAttr(data_clone, 'isFolder')
        delAttr(data_clone, 'parent')
        setAttr(data_clone, 'checksum', None)
        id = request.get_id()
        Messages_whom.objects.filter(message_id=id).delete()
        message = super().filter(id=id)
        message.update(**data_clone)

        if isinstance(data.get('to_whom'), list):
            for user_id in data.get('to_whom'):
                Messages_whom.objects.get_or_create(to_whom_id=user_id, message_id=id)

        return data


class Messages(AuditModel):
    checksum = CodeField(_('Checksum MD5'), null=True, blank=True)
    message = DescriptionField(_('Тело сообщения'), null=False, blank=False)
    date_create = DateTimeField(verbose_name='Дата записи', db_index=True, default=timezone.now)
    user = ForeignKeyCascade(User, related_name='user', default=None)
    state = ForeignKeyProtect(Messages_state, default=None)
    theme = ForeignKeyProtect(Messages_theme, default=None)
    parent = ForeignKeyProtect("self", blank=True, null=True)

    def __str__(self):
        return self.checksum

    objects = MessagesManager()

    class Meta:
        verbose_name = 'Сообщения'
