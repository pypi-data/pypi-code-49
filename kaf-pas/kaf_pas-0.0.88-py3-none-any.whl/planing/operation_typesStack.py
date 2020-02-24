import logging

from django.db import ProgrammingError

logger = logging.getLogger(__name__)


class Operation_typesStack:
    def get_first_item_of_tuple(self, tp):
        res, _ = tp
        return res

    def __init__(self):
        from kaf_pas.planing.models.operation_types import Operation_types
        from kaf_pas.planing.models.status_operation_types import Status_operation_typesManager

        try:
            self.ASSEMBLY_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='AS_TSK', defaults=dict(
                props=Operation_types.props.plus,
                name='Задание на комплектацию',
                editing=False,
                deliting=False,
            )))

            self.ASSEMBLY_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.ASSEMBLY_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.ASSEMBLY_DETAIL_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='DETAIL_AS_TSK', defaults=dict(
                props=0,
                name='Детализация Задания на комплектацию',
                editing=False,
                deliting=False,
                parent=self.ASSEMBLY_TASK
            )))

            self.ASSEMBLY_DETAIL_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.ASSEMBLY_DETAIL_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.PRODUCTION_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='PRD_TSK', defaults=dict(
                props=0,
                name='Задание на производство',
                editing=False,
                deliting=False,
            )))

            self.PRODUCTION_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.PRODUCTION_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.PRODUCTION_DETAIL_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='DETAIL_PRD_TSK', defaults=dict(
                props=0,
                name='Детализация Задания на производство',
                editing=False,
                deliting=False,
                parent=self.PRODUCTION_TASK
            )))

            self.PRODUCTION_DETAIL_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.PRODUCTION_DETAIL_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.CALC_TASKS = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='CLC_TSK', defaults=dict(
                props=0,
                name='Учет',
                editing=False,
                deliting=False,
            )))

            self.CALC_TASKS_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.CALC_TASKS,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.POSTING_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='PST_TSK', defaults=dict(
                props=0,
                name='Оприходование',
                editing=False,
                deliting=False,
                parent=self.CALC_TASKS
            )))

            self.POSTING_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.POSTING_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.POSTING_DETAIL_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='DETAIL_PST_TSK', defaults=dict(
                props=Operation_types.props.plus,
                name='Детализация Оприходывания',
                editing=False,
                deliting=False,
                parent=self.CALC_TASKS
            )))

            self.POSTING_DETAIL_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.POSTING_DETAIL_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.WRITE_OFF_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='WRT_OFF_TSK', defaults=dict(
                props=0,
                name='Списание',
                editing=False,
                deliting=False,
                parent=self.CALC_TASKS
            )))

            self.WRITE_OFF_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.WRITE_OFF_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.WRITE_DETAIL_OFF_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='DETAIL_WRT_OFF_TSK', defaults=dict(
                props=Operation_types.props.minus,
                name='Детализация Списания',
                editing=False,
                deliting=False,
                parent=self.CALC_TASKS
            )))

            self.WRITE_DETAIL_OFF_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.WRITE_DETAIL_OFF_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )

            self.ROUTING_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='RT_TSK', defaults=dict(
                props=0,
                name='Маршрутизация',
                editing=False,
                deliting=False,
            )))

            self.ROUTING_TASK_STATUSES = Status_operation_typesManager.make_statuses(
                opertype=self.ROUTING_TASK,
                status_map=[
                    dict(code='new', name='Новый'),
                ]
            )


        except ProgrammingError as ex:
            logger.warning(ex)
