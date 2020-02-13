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
        data = {'demand__date': '2019-09-25T00:00:00.000', 'demand__code': '19/407-1', 'code': '1', 'date': '2019-11-17', 'qty': 2, 'demand_id': 38, 'description': '11111111'}
        # demand_id = options.get('demand_id')
        user_id = options.get('user_id')
        setAttr(data, 'user_id', user_id)
        print(f'data: {data}')

        LaunchesManager.make_launch(data=data)

        print('Done')
