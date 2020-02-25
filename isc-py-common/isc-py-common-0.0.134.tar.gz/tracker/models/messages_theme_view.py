import logging

from django.db.models import BooleanField

from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyCascade
from isc_common.managers.common_tree_grid_manager import CommonTreeGridManager
from isc_common.models.base_ref import BaseRefHierarcy

logger = logging.getLogger(__name__)


class Messages_theme_view_Manager(CommonTreeGridManager):
    @staticmethod
    def getRecord(record):
        res = {
            'id': record.get("id"),
            'code': record.get("code"),
            'name': record.get("name"),
            # 'full_name': record.get("full_name"),
            'description': record.get("description"),
            'parent_id': record.get("parent_id"),
            'lastmodified': record.get("lastmodified"),
            'isFolder': record.get("isFolder"),
            'editing': record.get("editing"),
            'deliting': record.get("deliting"),
        }
        return res

class Messages_theme_view(BaseRefHierarcy):
    user = ForeignKeyCascade(User, null=True, blank=True, related_name='user_theme')
    creator = ForeignKeyCascade(User, null=True, blank=True, related_name='creator_theme')
    isFolder = BooleanField(default=False)

    def __str__(self):
        return f'{self.code}: {self.name}'

    objects = Messages_theme_view_Manager()

    class Meta:
        verbose_name = 'Темы задач'
        managed = False
        db_table = 'tracker_messages_theme_view'
