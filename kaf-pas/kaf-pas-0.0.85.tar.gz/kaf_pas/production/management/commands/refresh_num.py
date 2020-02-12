import logging

from django.core.management import BaseCommand

from kaf_pas.production.models.operations_item import Operations_itemManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование"

    def handle(self, *args, **options):
        Operations_itemManager.refresh_num1()
