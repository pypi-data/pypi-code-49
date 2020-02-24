import logging

from django.db.models import CheckConstraint, Q, F, UniqueConstraint

from isc_common.fields.code_field import CodeField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.tree_audit import TreeAuditModelManager
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class Lotsman_documents_hierarcy_refsQuerySet(AuditQuerySet):
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


class Lotsman_documents_hierarcy_refsManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Lotsman_documents_hierarcy_refsQuerySet(self.model, using=self._db)


class Lotsman_documents_hierarcy_refs(AuditModel):
    child = ForeignKeyProtect(Lotsman_documents_hierarcy, related_name='Lotsman_documents_hierarcy_child')
    parent = ForeignKeyProtect(Lotsman_documents_hierarcy, related_name='Lotsman_documents_hierarcy_parent', null=True, blank=True)

    section = CodeField(verbose_name="Раздел", null=True, blank=True)
    subsection = CodeField(verbose_name="Подраздел", null=True, blank=True)

    objects = Lotsman_documents_hierarcy_refsManager()
    objects_tree = TreeAuditModelManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
        constraints = [
            UniqueConstraint(fields=['child'], condition=Q(parent=None) & Q(section=None) & Q(subsection=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_0'),
            UniqueConstraint(fields=['child', 'parent'], condition=Q(section=None) & Q(subsection=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_1'),
            UniqueConstraint(fields=['child', 'section'], condition=Q(parent=None) & Q(subsection=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_2'),
            UniqueConstraint(fields=['child', 'parent', 'section'], condition=Q(subsection=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_3'),
            UniqueConstraint(fields=['child', 'subsection'], condition=Q(parent=None) & Q(section=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_4'),
            UniqueConstraint(fields=['child', 'parent', 'subsection'], condition=Q(section=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_5'),
            UniqueConstraint(fields=['child', 'section', 'subsection'], condition=Q(parent=None), name='Lotsman_documents_hierarcy_refs_unique_constraint_6'),
            UniqueConstraint(fields=['child', 'parent', 'section', 'subsection'], name='Lotsman_documents_hierarcy_refs_unique_constraint_7'),
            CheckConstraint(check=~Q(child=F('parent')), name='Lotsman_documents_hierarcy_not_circulate_refs')
        ]
