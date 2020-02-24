import logging

from django.core.management import BaseCommand
from django.db import transaction

from kaf_pas.production.models.ready_2_launch import Ready_2_launchManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование"

    def add_arguments(self, parser):
        parser.add_argument('--demand_id', type=int)
        parser.add_argument('--user_id', type=int)

    def handle(self, *args, **options):
        demand_id = options.get('demand_id')
        user_id = options.get('user_id')

        with transaction.atomic():
            Ready_2_launchManager.make(demand=demand_id, user=user_id)
        print('Done')
