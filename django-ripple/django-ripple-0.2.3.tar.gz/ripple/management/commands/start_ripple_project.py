from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Creating Ripple Project"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Creating Ripple Project")