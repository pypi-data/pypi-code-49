import logging

from isc_common.fields.related import ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.number import DelProps
from kaf_pas.planing.models.operations import Operations, OperationsManager
from kaf_pas.production.models.launches import Launches

logger = logging.getLogger(__name__)


class Operation_launchesQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_launchesManager(AuditManager):

    def reCalcRoutesFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        data.setdefault('user', request.user)
        OperationsManager.make_routing(data=data)
        return data

    def cleanRoutesFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        data.setdefault('user', request.user)
        res = OperationsManager.clean_routing(data=data)
        return DelProps(res)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_launchesQuerySet(self.model, using=self._db)


class Operation_launches(AuditModel):
    operation = ForeignKeyCascade(Operations, related_name='planing_operation_launch')
    launch = ForeignKeyCascade(Launches, related_name='planing_resource_launch')

    objects = Operation_launchesManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
