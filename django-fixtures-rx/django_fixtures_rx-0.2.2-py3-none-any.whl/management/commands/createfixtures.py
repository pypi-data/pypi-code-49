from argparse import ArgumentParser

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.test.utils import setup_databases, teardown_databases

from django_fixtures.utilities import get_fixtures


class Command(BaseCommand):
    help = 'Used to create a fixtures.'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            'args', metavar='app_label[.FixtureName]', nargs='*',
            help='Create fixtures for the specified app_label or app_label.FixtureName.'
        )

    def handle(self, *accessors, **options):
        old_config = setup_databases(0, False)

        try:
            for fixture in get_fixtures(*accessors):
                fixture.create(), call_command('flush', verbosity=0, interactive=False)
                self.stdout.write(f'Fixture {fixture.name} has been created.')
        except Exception as exception:
            self.stderr.write(str(exception))
        finally:
            teardown_databases(old_config, 0)
