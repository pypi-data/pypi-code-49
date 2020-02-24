import logging

from kaf_pas.planing.models.operations import OperationsManager, OperationsQuerySet
from kaf_pas.planing.models.operations_view import Operations_view, Operations_viewManager

logger = logging.getLogger(__name__)


class Production_orderQuerySet(OperationsQuerySet):
    pass


class Production_orderManager(OperationsManager):
    @staticmethod
    def getRecord(record):
        return Operations_viewManager.getRecord(record)

    @staticmethod
    def get_resource_workshop(location_id):
        from kaf_pas.ckk.models.locations import Locations

        res = None
        for location in Locations.objects_tree.get_parents(id=location_id, child_id='id', include_self=False):
            if location.props.isWorkshop == True:
                res = dict(id=location.id, title=location.name, prompt=location.full_name)
                break

        if res == None:
            raise Exception(f'Не обнаружен цех, с признаком "Уровень цеха" для : {Locations.objects.get(id=location_id).full_name}')
        return res

    @staticmethod
    def getRecordLocations(record):
        return Production_orderManager.get_resource_workshop(record.get('resource__location_id'))

    @staticmethod
    def getRecordLevels(record):
        return dict(id=record.get('operation_level_id'), title=record.get('operation_level__name'))

    def get_queryset(self):
        return Production_orderQuerySet(self.model, using=self._db)


class Production_order(Operations_view):
    objects = Production_orderManager()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()

    class Meta:
        proxy = True
        verbose_name = 'Оприходования'
