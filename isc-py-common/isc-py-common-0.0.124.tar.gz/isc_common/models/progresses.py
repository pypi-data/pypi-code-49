import logging
import uuid

from bitfield import BitField
from django.db.models import TextField, PositiveIntegerField, UUIDField

from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeStrictField
from isc_common.fields.related import ForeignKeyCascade
from isc_common.models.audit import AuditQuerySet, AuditManager, AuditModel
from isc_common.number import DelProps

logger = logging.getLogger(__name__)


class ProgressesQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class ProgressesManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
            'props': record.props
        }
        return DelProps(res)

    def get_queryset(self):
        return ProgressesQuerySet(self.model, using=self._db)


class Progresses(AuditModel):
    cnt = PositiveIntegerField()
    id_progress = CodeStrictField()
    label_contents = TextField()
    message = TextField()
    qty = PositiveIntegerField()
    props = BitField(flags=(
        ('showCancel', 'Показать кнопку отменить процесс'),
    ), default=0, db_index=True)
    title = TextField()
    path = CodeStrictField(default='progress')
    user = ForeignKeyCascade(User)

    objects = ProgressesManager()

    def __str__(self):
        return f'ID:{self.id}, title: {self.title}, qty: {self.qty}, cnt: {self.cnt}, id_progress: {self.id_progress}, guid: {str(self.guid)} user: [{self.user}]'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Отражение запущенных процессов'
        unique_together = (('user', 'id_progress'),)
