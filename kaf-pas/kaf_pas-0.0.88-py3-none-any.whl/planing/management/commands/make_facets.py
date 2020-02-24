import logging

from django.core.management import BaseCommand

from kaf_pas.planing.models.routing import RoutingManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # print(RoutingManager.make_levels(launch_id=30))
        for item in RoutingManager.make_levels(launch_id=44):
            print(item)
