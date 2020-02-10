# Imports from Django.
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Calls all upstream bootstrap commands and election commands"

    def add_arguments(self, parser):
        parser.add_argument(
            "--cycle",
            action="store",
            dest="cycle",
            default="2018",
            help="Specify the election cycle you want to query against",
        )

    def handle(self, *args, **options):
        print(f"Bootstrapping elections in year {options['cycle']}...")
        print("")

        call_command("bootstrap_geography")
        call_command("bootstrap_jurisdictions")
        call_command("bootstrap_fed")
        call_command("bootstrap_offices", cycle=options["cycle"])
        call_command("bootstrap_parties")
        call_command("bootstrap_election_events", cycle=options["cycle"])
        call_command("schedule_elections")
