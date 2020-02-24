import logging

from django.core.management import BaseCommand

from kaf_pas.planing.models.levels import Levels
from kaf_pas.planing.models.routing import RoutingManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for level in Levels.objects.all():
            print('\n\n')
            for a in RoutingManager.make_resourcesLevel(launch_id=30, level_id=16, location_id=64):
                print(a)
