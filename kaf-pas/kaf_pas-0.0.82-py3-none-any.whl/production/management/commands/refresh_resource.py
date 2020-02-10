import logging

from django.core.management import BaseCommand

from kaf_pas.production.models.launch_operation_resources import Launch_operation_resourcesManager
from kaf_pas.production.models.operation_resources import Operation_resourcesManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование"

    def handle(self, *args, **options):
        Launch_operation_resourcesManager.refresh_resource()
        Operation_resourcesManager.refresh_resource()
