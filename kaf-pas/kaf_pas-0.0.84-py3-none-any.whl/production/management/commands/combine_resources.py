import logging

from django.core.management import BaseCommand
from django.db import connection, transaction
from tqdm import tqdm

from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
from kaf_pas.production.models.operation_def_resources import Operation_def_resources
from kaf_pas.production.models.operation_resources import Operation_resources
from kaf_pas.production.models.resource import Resource
from kaf_pas.production.models.resource_users import Resource_users

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Удаление дубликатов товарных позиций"

    def handle(self, *args, **options):
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*), location_id, calendar_id
                                    from production_resource
                                    group by location_id, calendar_id
                                    having count(*) > 1
                                        ''')
                rows = cursor.fetchall()
                pbar = tqdm(total=len(rows))
                for row in rows:
                    count, location_id, calendar_id = row

                    first_step = True
                    _resource = None

                    for resource in Resource.objects.filter(location_id=location_id, calendar_id=calendar_id):
                        if not first_step:
                            for operation_resources in Operation_resources.objects.filter(resource=resource):
                                operation_resources.resource = _resource
                                operation_resources.save()

                            for operation_resources in Operation_def_resources.objects.filter(resource=resource):
                                operation_resources.resource = _resource
                                operation_resources.save()

                            for operation_resources in Launch_operation_resources.objects.filter(resource=resource):
                                operation_resources.resource = _resource
                                operation_resources.save()

                            for operation_resources in Resource_users.objects.filter(resource=resource):
                                operation_resources.resource = _resource
                                operation_resources.save()

                            resource.delete()
                        else:
                            _resource = resource
                            first_step = False
                    pbar.update()
                pbar.close()
