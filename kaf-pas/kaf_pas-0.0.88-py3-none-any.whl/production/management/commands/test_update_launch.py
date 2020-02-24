import logging

from django.core.management import BaseCommand

from isc_common import setAttr
from kaf_pas.production.models.launches import LaunchesManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование запуск"

    def add_arguments(self, parser):
        # parser.add_argument('--demand_id', type=int)
        parser.add_argument('--user_id', type=int)

    def handle(self, *args, **options):
        data = {'id': 6, 'code': '1', 'name': None, 'date': '2019-11-20T00:00:00.000', 'description': None, 'parent_id': None, 'demand_id': 34, 'demand__code': 'Тестовый №2', 'demand__date': '2019-10-31T00:00:00.000', 'status_id': 1, 'status__code': 'formirovanie', 'status__name': 'Формирование', 'qty': 5, 'isFolder': False, 'user_id': 2}
        # demand_id = options.get('demand_id')
        user_id = options.get('user_id')
        setAttr(data, 'user_id', user_id)

        LaunchesManager.update_launch(data=data)

        print('Done')
