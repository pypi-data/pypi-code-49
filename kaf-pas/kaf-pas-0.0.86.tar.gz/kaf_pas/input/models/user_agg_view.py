import logging

from django.db.models import EmailField

from isc_common.fields.code_field import CodeField
from isc_common.fields.name_field import NameField
from isc_common.models.audit import AuditQuerySet, AuditManager, AuditModel

logger = logging.getLogger(__name__)


class User_agg_viewQuerySet(AuditQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class User_agg_viewManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'username': record.username,
            'first_name': record.first_name,
            'last_name': record.last_name,
            'email': record.email,
            'middle_name': record.middle_name,
            'location_position': record.location_position,
        }
        return res

    def get_queryset(self):
        return User_agg_viewQuerySet(self.model, using=self._db)


class User_agg_view(AuditModel):
    username = CodeField()
    first_name = NameField()
    last_name = NameField()
    email = EmailField(blank=True, null=True)
    middle_name = NameField()
    location_position = NameField()

    objects = User_agg_viewManager()

    def __str__(self):
        return f"ID: {self.id} username {self.username}"

    class Meta:
        verbose_name = 'Пользователи'
        db_table = 'user_agg_view'
        managed = False
