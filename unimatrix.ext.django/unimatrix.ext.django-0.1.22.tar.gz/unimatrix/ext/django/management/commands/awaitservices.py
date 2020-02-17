import logging
import time

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waits for services to become ready."
    logger = logging.getLogger('django')
    default_interval = 5.0

    def handle(self, *args, **options):
        self.await_databases()

    def await_databases(self, interval=5.0):
        attempts = 0
        awaiting = set([x for x in connections])
        connected = set()
        while awaiting != connected:
            attempts += 1
            for alias in connections:
                connection = connections[alias]
                try:
                    cursor = connection.cursor()
                except OperationalError as e:
                    msg = str.split(e.args[0], '\n')[0]
                    self.logger.error(
                        "Database connection '%s' not ready (%s)",
                        alias, msg
                    )
                    continue
                connected.add(alias)

            # If the databases were already up, check again here
            # so we don't wait unnecessarily.
            if awaiting == connected:
                break
            time.sleep(interval)
