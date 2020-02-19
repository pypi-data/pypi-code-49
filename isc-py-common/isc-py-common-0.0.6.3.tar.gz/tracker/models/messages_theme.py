import logging

from django.db.models import BooleanField

from isc_common.fields.related import ForeignKeyProtect
from isc_common.managers.common_tree_grid_manager import CommonTreeGridManager
from isc_common.models.base_ref import BaseRef, BaseRefHierarcy

logger = logging.getLogger(__name__)


class Messages_theme_Manager(CommonTreeGridManager):
    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "code": record.code,
            "name": record.name,
            "description": record.description,
            "parent_id": record.parent_id,
            "lastmodified": record.lastmodified,
            "editing": record.editing,
            "deliting": record.deliting,
        }
        return res


class Messages_theme(BaseRefHierarcy):
    def __str__(self):
        return f"{self.code}: {self.name}"

    objects = Messages_theme_Manager()

    class Meta:
        verbose_name = 'Темы сообщений'
