import logging

from django.db import ProgrammingError

logger = logging.getLogger(__name__)


class Operation_Stack:
    def get_first_item_of_tuple(self, tp):
        res, _ = tp
        return res

    def __init__(self):

        try:
            from kaf_pas.production.models.operations import Operations
            self.NOOP = self.get_first_item_of_tuple(Operations.objects.update_or_create(code='00', defaults=dict(
                name='Пустая операция',
                editing=False,
                deliting=False,
            )))


        except ProgrammingError as ex:
            logger.warning(ex)
