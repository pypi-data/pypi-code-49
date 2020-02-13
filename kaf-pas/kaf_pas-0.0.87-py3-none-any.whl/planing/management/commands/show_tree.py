import logging

from django.core.management import BaseCommand

from kaf_pas.planing.models.launch_item_refs_timing import Launch_item_refs_timingManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = {'id': 15, 'code': '1', 'name': None, 'date': '2019-12-04T00:00:00.000', 'description': None, 'parent_id': None, 'demand_id': 34, 'demand__code': 'Тестовый №2', 'demand__date': '2019-10-31T00:00:00.000', 'status_id': 3, 'status__code': 'formirovanie', 'status__name': 'Формирование',
                'qty': 2, 'isFolder': False, 'editing': True, 'deliting': True, 'user_id': 2}
        Launch_item_refs_timingManager.make_timing(data=data)
