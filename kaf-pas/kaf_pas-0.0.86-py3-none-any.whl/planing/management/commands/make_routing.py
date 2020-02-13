import logging

from django.core.management import BaseCommand

from kaf_pas.planing.models.operations import OperationsManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = {'id': 17, 'code': 'Тест111/1', 'name': None, 'date': '2020-01-18T00:00:00.000', 'description': None, 'parent_id': None, 'demand_id': 38, 'demand__code': 'Тест111', 'demand__date': '2019-11-13T00:00:00.000', 'status_id': 3, 'status__code': 'formirovanie', 'status__name': 'Формирование', 'qty': 2, 'routing_made': False, 'isFolder': False, 'props': 0, 'editing': True, 'deliting': True, 'user_id': 2}
        OperationsManager.make_routing(data=data)
