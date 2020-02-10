import logging

from django.core.management import BaseCommand
from django.db import connection, transaction
from tqdm import tqdm

from kaf_pas.production.models.operation_material import Operation_material
from kaf_pas.production.models.operation_resources import Operation_resources
from kaf_pas.production.models.operations_item import Operations_item
from kaf_pas.production.models.resource_users import Resource_users

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Удаление дубликатов товарных позиций"

    def handle(self, *args, **options):
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*), item_id, operation_id
                                    from production_operations_item
                                    group by item_id, operation_id
                                    having count(*) > 1
                                        ''')
                rows = cursor.fetchall()
                pbar = tqdm(total=len(rows))
                for row in rows:
                    count, item_id, operation_id = row

                    first_step = True
                    _operations_item = None

                    for operations_item in Operations_item.objects.filter(item_id=item_id, operation_id=operation_id):
                        if not first_step:
                            for operation_resources in Operation_resources.objects.filter(operationitem=operations_item):
                                operation_resources.operations_item = _operations_item
                                operation_resources.save()

                            for operation_resources in Operation_material.objects.filter(operationitem=operations_item):
                                operation_resources.operations_item = _operations_item
                                operation_resources.save()

                            operations_item.delete()
                        else:
                            _operations_item = operations_item
                            first_step = False
                    pbar.update()
                pbar.close()
