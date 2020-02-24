import logging

from bitfield import BitField
from django.contrib.postgres.fields import JSONField
from django.db.models import CheckConstraint, Q, F, UniqueConstraint, TextField, DecimalField, FloatField

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.tree_audit import TreeAuditModelManager
from isc_common.number import DelProps
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.item_refs import Item_refs
from kaf_pas.production.models.launches import Launches

logger = logging.getLogger(__name__)


class Launch_item_refsQuerySet(AuditQuerySet):
    pass


class Launch_item_refsManager(AuditManager):

    @staticmethod
    def props():
        return BitField(flags=(
            ('enabled', 'Доступность в данной производственной спецификации'),  # 1
        ), default=1, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'props': record.props._value,
            'enabled': record.props.enabled,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return DelProps(res)

    def get_queryset(self):
        return Launch_item_refsQuerySet(self.model, using=self._db)


class Launch_item_refs(AuditModel):
    child = ForeignKeyProtect(Item, related_name='launch_child')
    item_refs = ForeignKeyProtect(Item_refs)
    launch = ForeignKeyProtect(Launches)
    parent = ForeignKeyProtect(Item, related_name='launch_parent', blank=True, null=True)
    props = Launch_item_refsManager.props()
    item_full_name = TextField()
    item_full_name_obj = JSONField(default=dict)
    qty = FloatField()

    objects = Launch_item_refsManager()
    tree_objects = TreeAuditModelManager()

    def __str__(self):
        return f"ID: {self.id}, " \
               f"child: [{self.child}], " \
               f"parent: [{self.parent}], " \
               f"item_refs: [{self.item_refs}], " \
               f"launch: [{self.launch}], " \
               f"props: {self.props}"

    def __repr__(self):
        return f"ID: {self.id}, " \
               f"child: [{self.child}], " \
               f"parent: [{self.parent}]"

    class Meta:
        verbose_name = 'Древо производственной спецификации'
        constraints = [
            CheckConstraint(check=~Q(child=F('parent')), name='Launch_item_refs_not_circulate_refs'),
            UniqueConstraint(fields=['child', 'launch'], condition=Q(parent=None), name='Launch_item_refs_unique_constraint_0'),
            UniqueConstraint(fields=['child', 'launch', 'parent'], name='Launch_item_refs_unique_constraint_1'),
        ]
