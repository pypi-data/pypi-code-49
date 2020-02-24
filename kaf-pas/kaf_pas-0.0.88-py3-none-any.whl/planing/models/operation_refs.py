import logging

from bitfield import BitField
from django.db.models import CheckConstraint, Q, F, UniqueConstraint

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel
from isc_common.models.tree_audit import TreeAuditModelManager, TreeAuditModelQuerySet
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_refsQuerySet(TreeAuditModelQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def update(self, **kwargs):
        return super().update(**kwargs)

    def get_or_create(self, defaults=None, **kwargs):
        return super().get_or_create(defaults, **kwargs)

    def update_or_create(self, defaults=None, **kwargs):
        return super().update_or_create(defaults, **kwargs)


class Operation_refsManager(TreeAuditModelManager):

    @staticmethod
    def props():
        return BitField(flags=(
            ('inner_routing', 'Связь операций внутри товарной позиции'),  # 1
            ('outer_routing', 'Связь операций между товарными позициями'),  # 2
            ('product_order_routing', 'Связи в блоке заказы на производство'),  # 4
        ), default=0, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_refsQuerySet(self.model, using=self._db)


class Operation_refs(AuditModel):
    parent = ForeignKeyProtect(Operations, related_name='operation_parent', blank=True, null=True)
    parent_real = ForeignKeyProtect(Operations, related_name='operation_parent_real', blank=True, null=True)
    child = ForeignKeyProtect(Operations, related_name='operation_child')
    props = Operation_refsManager.props()

    objects = Operation_refsManager()

    def __str__(self):
        return f"ID:{self.id}, child: [{self.child}] , parent: [{self.parent}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица операций планирования'
        unique_together = ('child', 'parent', 'props')
        constraints = [
            CheckConstraint(check=~Q(child=F('parent')), name='Operation_refs_not_circulate_refs'),
            UniqueConstraint(fields=['child'], condition=Q(parent=None) & Q(parent_real=None), name='Operation_refs_unique_constraint_0'),
            UniqueConstraint(fields=['child', 'parent'], condition=Q(parent_real=None), name='Operation_refs_unique_constraint_1'),
            UniqueConstraint(fields=['child', 'parent_real'], condition=Q(parent=None), name='Operation_refs_unique_constraint_2'),
            UniqueConstraint(fields=['child', 'parent', 'parent_real'], name='Operation_refs_unique_constraint_3'),
        ]
