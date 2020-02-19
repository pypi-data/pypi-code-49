import logging

from django.db.models import Model, BooleanField, BigAutoField, BigIntegerField, DateTimeField
from django.utils import timezone

from isc_common.managers.common_manager import CommonManager, CommonQuerySet

logger = logging.getLogger(__name__)


class AuditQuerySet(CommonQuerySet):
    def __init__(self, model=None, query=None, using=None, hints=None, alive_only=True):
        self.alive_only = alive_only
        super().__init__(model=model, query=query, using=using, hints=hints, alive_only=alive_only)

    def soft_delete(self, visibleMode="hide"):
        if visibleMode == "hide":
            res = super().update(deleted_at=timezone.now())
        elif visibleMode == "visible":
            res = super().update(deleted_at=None)

        return res

    def delete(self):
        res = super().delete()
        return res

    def hard_delete(self):
        res = super().delete()
        return res

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class AuditManager(CommonManager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return AuditQuerySet(model=self.model, alive_only=self.alive_only).filter(deleted_at=None)
        return AuditQuerySet(model=self.model, alive_only=self.alive_only)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def soft_delete(self):
        return self.get_queryset().soft_delete()

    def soft_restore(self):
        return self.get_queryset().soft_restore()

    # def deleteFromRequest(self, request):
    #     request = DSRequest(request=request)
    #     ids = request.get_ids()
    #     old_ids = request.get_old_ids()
    #     query = super().filter(id__in=ids)
    #     res = query.delete()
    #     query = super().filter(id__in=old_ids)
    #     res += query.delete()
    #     return res


class AuditModel(Model):
    id = BigAutoField(primary_key=True, verbose_name="Идентификатор")
    id_old = BigIntegerField(verbose_name="Идентификатор старый", null=True, blank=True)
    deleted_at = DateTimeField(verbose_name="Дата мягкого удаления", null=True, blank=True, db_index=True)
    editing = BooleanField(verbose_name="Возможность редактирования", default=True)
    deliting = BooleanField(verbose_name="Возможность удаления", default=True)
    lastmodified = DateTimeField(verbose_name='Последнее обновление', editable=False, db_index=True, default=timezone.now)

    class Meta:
        abstract = True

    def delete(self):
        super().delete()

    def delete_soft(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    objects = AuditManager()
    all_objects = AuditManager(alive_only=False)
