import logging

from django.core.management import BaseCommand

from kaf_pas.planing.models.operation_operation import Operation_operation
from kaf_pas.planing.models.operation_refs import Operation_refs
from kaf_pas.planing.models.operations_view import Operations_view

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 1
        # for operation in Operations_view.objects.filter(item_id=3379400, launch_id=30, operation_level_id=9).distinct():
        #     print(f'\n======Prod ({i})======')
        #     print(f'ID: {operation.id}, PARENT_ID: {operation.parent_id}')
        #     if operation.parent_id:
        #         print(Operation_operation.objects.get(operation_id=operation.parent_id).production_operation)
        #     print(operation.operation_level)
        #     print(operation.production_operation)
        #     print(operation.resource)
        #     print(operation.edizm)
        #     print(operation.value)
        #     i += 1
        #     print('======End Prod======\n')

        for operation in Operation_refs.objects.get_descendants(id=26745, order_by_clause='order by level'):
            print(f'\n======Prod ({i})======')
            print(operation)
            # print(f'ID: {operation.id}, PARENT_ID: {operation.parent_id}')
            # if operation.parent_id:
            #     print(f'parent production_operation: {Operation_operation.objects.get(operation_id=operation.parent_id).production_operation}')
            # print(f'operation_level: {operation.operation_level}')
            # print(f'production_operation: {operation.production_operation}')
            # print(f'resource: {operation.resource}')
            # print(f'edizm: {operation.edizm}')
            # print(f'value: {operation.value}')
            i += 1
            print('======End Prod======\n')

        # for operation in Operation_refs.objects.get_parents(id=23219, order_by_clause='order by level desc'):
        #     for prod_operation in Operation_operation.objects.filter(operation=operation.child):
        #         print('\n======Prod======')
        #         print(prod_operation)
        #         print('======End Prod======\n')
        #     print(operation)

        # for operation in Operations_view.objects.filter(id=23219):
        #     print(operation)
