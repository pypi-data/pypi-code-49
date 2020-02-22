# Imports from python.
import csv
from datetime import date
from datetime import datetime


# Imports from Django.
from django.core.management.base import BaseCommand


# Imports from other dependencies.
from elections import ElectionYear
from geography.models import Division
from government.models import Party
import pytz
import requests
from tqdm import tqdm
import us


# Imports from election.
from election.models.election_ballot import ElectionBallot
from election.models import ElectionCycle
from election.models import ElectionDay
from election.models import ElectionEvent
from election.models import ElectionType
from election.utils.election_metadata import load_election_metadata


class Command(BaseCommand):
    help = (
        "Create election event instances based off "
        "current elections in the database"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--cycle",
            action="store",
            dest="cycle",
            default="2018",
            help="Specify the election cycle you want to query against",
        )

    def handle(self, *args, **options):
        print(f"Loading elections for {options['cycle']}...")
        print("")

        election_year = ElectionYear(options["cycle"])
        self.cycle, cycle_was_created = ElectionCycle.objects.get_or_create(
            name=election_year.year
        )

        self.get_needed_election_types()

        democratic_party = Party.objects.get(ap_code="Dem")
        print("  - Creating Democratic primaries...")
        for elex_data in tqdm(election_year.elections.primaries.democratic):
            self.create_single_party_primary(elex_data, democratic_party)
        print("    Done!")
        print("")

        republican_party = Party.objects.get(ap_code="GOP")
        print("  - Creating Republican primaries...")
        for elex_data in tqdm(election_year.elections.primaries.republican):
            self.create_single_party_primary(elex_data, republican_party)
        print("    Done!")
        print("")

        top_two_primaries = [
            primary_elex
            for primary_elex in election_year.elections.primaries
            if primary_elex.election_variant == "top-two-primary"
        ]
        print("  - Creating top-two primaries...")
        for elex_data in tqdm(top_two_primaries):
            self.create_top_two_primary(elex_data)
        print("    Done!")
        print("")

        majority_elects_slug = "majority-elects-blanket-primary"
        majority_elects_blanket_primaries = [
            primary_elex
            for primary_elex in election_year.elections.primaries
            if primary_elex.election_variant == majority_elects_slug
        ]
        print("  - Creating 'majority-elects' blanket primaries...")
        for elex_data in tqdm(majority_elects_blanket_primaries):
            self.create_majority_elects_blanket_primary(elex_data)
        print("    Done!")
        print("")

        print("  - Creating general elections...")
        for elex_data in tqdm(election_year.elections.general_elections):
            self.create_general_election(elex_data)
        print("    Done!")
        print("")

    def get_needed_election_types(self):
        self.election_types = {
            "CAUCUS": ElectionType.objects.get_or_create(
                slug=ElectionType.PARTISAN_CAUCUS,
                defaults=dict(
                    label=dict(ElectionType.TYPES)[
                        ElectionType.PARTISAN_CAUCUS
                    ],
                    short_label="Caucus",
                ),
            )[0],
            "FIREHOUSE_CAUCUS": ElectionType.objects.get_or_create(
                slug=ElectionType.PARTISAN_FIREHOUSE_CAUCUS,
                defaults=dict(
                    label=dict(ElectionType.TYPES)[
                        ElectionType.PARTISAN_FIREHOUSE_CAUCUS
                    ],
                    short_label="Firehouse Caucus",
                ),
            )[0],
            "PRIMARY": ElectionType.objects.get_or_create(
                slug=ElectionType.PARTISAN_PRIMARY,
                defaults=dict(
                    label=dict(ElectionType.TYPES)[
                        ElectionType.PARTISAN_PRIMARY
                    ],
                    short_label="Primary",
                ),
            )[0],
            "TOP_TWO": ElectionType.objects.get_or_create(
                slug=ElectionType.TOP_TWO_PRIMARY,
                defaults=dict(
                    label=dict(ElectionType.TYPES)[
                        ElectionType.TOP_TWO_PRIMARY
                    ],
                    short_label="Top-two",
                ),
            )[0],
            "MAJORITY_ELECTS_BLANKET": ElectionType.objects.get_or_create(
                slug=ElectionType.MAJORITY_ELECTS_BLANKET_PRIMARY,
                defaults=dict(
                    label=dict(ElectionType.TYPES)[
                        ElectionType.MAJORITY_ELECTS_BLANKET_PRIMARY
                    ],
                    short_label="Majority-elects blanket",
                ),
            )[0],
            "GENERAL": ElectionType.objects.get_or_create(
                slug=ElectionType.GENERAL,
                defaults=dict(
                    label=dict(ElectionType.TYPES)[ElectionType.GENERAL],
                    short_label="General",
                ),
            )[0],
        }

    def create_single_party_primary(self, election_data, party):
        try:
            division = Division.objects.get(
                code_components__postal=election_data.state.abbr
            )
        except Division.DoesNotExist:
            division = None

        election_day, day_was_created = ElectionDay.objects.get_or_create(
            cycle=self.cycle, date=election_data.election_date
        )

        raw_election_type = getattr(
            election_data, "election_variant", election_data.election_type
        )

        if raw_election_type == "caucus":
            election_type_choice = self.election_types["CAUCUS"]
        elif raw_election_type == "firehouse-caucus":
            election_type_choice = self.election_types["FIREHOUSE_CAUCUS"]
        else:
            election_type_choice = self.election_types["PRIMARY"]

        election_event, evt_was_created = ElectionEvent.objects.get_or_create(
            division=division,
            election_day=election_day,
            election_type=election_type_choice,
            defaults=dict(notes=election_data.election_day_notes),
        )

        non_null_defaults = load_election_metadata(election_data)

        election_blt, blt_was_created = ElectionBallot.objects.get_or_create(
            election_event_id=election_event.id,
            party_id=party.id,
            defaults=non_null_defaults,
        )

    def create_top_two_primary(self, election_data):
        division = Division.objects.get(
            code_components__postal=election_data.state.abbr
        )

        election_day, day_was_created = ElectionDay.objects.get_or_create(
            cycle=self.cycle, date=election_data.election_date
        )

        election_event, evt_was_created = ElectionEvent.objects.get_or_create(
            division=division,
            election_day=election_day,
            election_type=self.election_types["TOP_TWO"],
            defaults=dict(notes=election_data.election_day_notes),
        )

        non_null_defaults = load_election_metadata(election_data)

        election_blt, blt_was_created = ElectionBallot.objects.get_or_create(
            election_event=election_event, defaults=non_null_defaults
        )

    def create_majority_elects_blanket_primary(self, election_data):
        division = Division.objects.get(
            code_components__postal=election_data.state.abbr
        )

        election_day, day_was_created = ElectionDay.objects.get_or_create(
            cycle=self.cycle, date=election_data.election_date
        )

        election_event, evt_was_created = ElectionEvent.objects.get_or_create(
            division=division,
            election_day=election_day,
            election_type=self.election_types["MAJORITY_ELECTS_BLANKET"],
            defaults=dict(notes=election_data.election_day_notes),
        )

        non_null_defaults = load_election_metadata(election_data)

        election_blt, blt_was_created = ElectionBallot.objects.get_or_create(
            election_event=election_event, defaults=non_null_defaults
        )

    def create_general_election(self, election_data):
        division = Division.objects.get(
            code_components__postal=election_data.state.abbr
        )

        election_day, day_was_created = ElectionDay.objects.get_or_create(
            cycle=self.cycle, date=election_data.election_date
        )

        election_event, evt_was_created = ElectionEvent.objects.get_or_create(
            division=division,
            election_day=election_day,
            election_type=self.election_types["GENERAL"],
            defaults=dict(notes=election_data.election_day_notes),
        )

        non_null_defaults = load_election_metadata(election_data)

        if election_data.state.abbr == "LA":
            non_null_defaults[
                "offices_elected"
            ] = ElectionBallot.PRESIDENTIAL_OFFICE
        else:
            non_null_defaults["offices_elected"] = ElectionBallot.ALL_OFFICES

        election_blt, blt_was_created = ElectionBallot.objects.get_or_create(
            election_event=election_event, defaults=non_null_defaults
        )
