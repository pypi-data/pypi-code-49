import logging

from django.conf import settings
from django.db import transaction
from django.forms import model_to_dict

from isc_common import delAttr
from isc_common.http.DSRequest import DSRequest
from isc_common.number import DelProps
from kaf_pas.planing.models.operations import Operations, OperationsManager, OperationsQuerySet
from kaf_pas.planing.models.operations_view import Operations_view

logger = logging.getLogger(__name__)


class Write_off_itemsQuerySet(OperationsQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Write_off_itemsManager(OperationsManager):
    def createFromRequest(self, request, removed=None):
        from kaf_pas.accounting.models.tmp_buffer import Tmp_buffer
        from kaf_pas.planing.models.operation_color import Operation_color
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_locations import Operation_locations
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_value import Operation_value

        request = DSRequest(request=request)
        data = request.get_data()
        user_id = request.user_id
        delAttr(data, 'items')
        _data = data.copy()
        _data.setdefault('opertype', settings.OPERS_TYPES_STACK.WRITE_OFF_TASK)
        _data.setdefault('creator_id', user_id)

        with transaction.atomic():
            parent = Operations.objects.create(**_data)
            Operation_refs.objects.create(child=parent)

            for item in Tmp_buffer.objects.filter(value_off__isnull=False).exclude(value_off=0):
                child = dict()
                child.setdefault('date', parent.date)
                child.setdefault('creator_id', user_id)
                child.setdefault('description', item.description)
                child.setdefault('opertype', settings.OPERS_TYPES_STACK.WRITE_DETAIL_OFF_TASK)
                child = Operations.objects.create(**child)

                Operation_refs.objects.create(parent=parent, child=child)

                if item.location:
                    Operation_locations.objects.create(operation=child, location=item.location)

                if item.item:
                    Operation_item.objects.create(operation=child, item=item.item)

                if item.edizm:
                    Operation_value.objects.create(operation=child, value=item.value_off, edizm=item.edizm)

                if item.color:
                    Operation_color.objects.create(operation=child, color=item.color)

            Tmp_buffer.objects.filter(user_id=user_id).delete()

            parent = model_to_dict(parent)
            return DelProps(parent)

    def get_queryset(self):
        return Write_off_itemsQuerySet(self.model, using=self._db)


class Write_off_items(Operations_view):
    objects = Write_off_itemsManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        proxy = True
        verbose_name = 'Списания'
