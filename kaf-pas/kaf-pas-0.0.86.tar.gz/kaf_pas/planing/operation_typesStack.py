import logging

from django.db import ProgrammingError

logger = logging.getLogger(__name__)

class Operation_typesStack:
    def get_first_item_of_tuple(self, tp):
        res, _ = tp
        return res

    def __init__(self):
        from kaf_pas.planing.models.operation_types import Operation_types

        try:
            self.ASSEMBLY_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='AS_TSK', defaults=dict(
                props=Operation_types.props.plus,
                name='Задание на комплектацию',
                editing=False,
                deliting=False,
            )))

            self.PRODUCTION_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='PRD_TSK', defaults=dict(
                props=Operation_types.props.plus,
                name='Задание на производство',
                editing=False,
                deliting=False,
            )))

            self.POSTING_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='PST_TSK', defaults=dict(
                props=0,
                name='Оприходование',
                editing=True,
                deliting=True,
            )))

            self.POSTING_DETAIL_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='DETAIL_PST_TSK', defaults=dict(
                props=Operation_types.props.plus,
                name='Детализация Оприходывания',
                editing=True,
                deliting=True,
            )))

            self.WRITE_OFF_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='WRT_OFF_TSK', defaults=dict(
                props=0,
                name='Списание',
                editing=True,
                deliting=True,
            )))

            self.WRITE_DETAIL_OFF_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='DETAIL_WRT_OFF_TSK', defaults=dict(
                props=Operation_types.props.minus,
                name='Детализация Списания',
                editing=True,
                deliting=True,
            )))

            self.ROUTING_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='RT_TSK', defaults=dict(
                props=0,
                name='Маршрутизация',
                editing=False,
                deliting=False,
            )))
        except ProgrammingError as ex:
            logger.warning(ex)


