import logging

from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        from kaf_pas.planing.models.operations import OperationsManager
        OperationsManager.make_production_order(dict(user=2, id=17))
