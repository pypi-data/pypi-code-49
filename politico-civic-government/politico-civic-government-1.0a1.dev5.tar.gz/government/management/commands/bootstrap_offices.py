# Imports from Django.
from django.core.management.base import BaseCommand


# Imports from other dependencies.
from elections import ElectionYear
from geography.models import Division
from geography.models import DivisionLevel
from tqdm import tqdm


# Imports from government.
from government.models import Body
from government.models import Jurisdiction
from government.models import Office


class Command(BaseCommand):
    help = "Creates federal and state offices."

    def add_arguments(self, parser):
        parser.add_argument(
            "--cycle",
            action="store",
            dest="cycle",
            default="2018",
            help="Specify the election cycle you want to query against",
        )

    def handle(self, *args, **options):
        print(f"Loading offices for {options['cycle']}...")
        print("")

        self.election_year = ElectionYear(options["cycle"])
        self.federal_government = Jurisdiction.objects.get(
            name="U.S. Federal Government"
        )

        print("  - Creating U.S. Senate offices...")
        self.build_senate_offices()
        print("    Done!")
        print("")

        print("  - Creating U.S. House offices...")
        self.build_house_offices()
        print("    Done!")
        print("")

        print("  - Creating U.S. Executive office...")
        self.build_presidency()
        print("    Done!")
        print("")

        print("  - Creating state gubernatorial offices...")
        self.build_governorships()
        print("    Done!")
        print("")

    def build_senate_offices(self):
        def translate_senate_class(s):
            if s == "I":
                return "1"
            if s == "II":
                return "2"
            if s == "III":
                return "3"
            return s

        senate_seats = self.election_year.federal.congress.seats.senate
        division_level = DivisionLevel.objects.get(name="state")
        body = Body.objects.get(
            slug="senate", jurisdiction_id=self.federal_government.pk
        )

        for seat in tqdm(senate_seats):
            division = Division.objects.get(
                level=division_level, code=seat.state.fips
            )

            Office.objects.update_or_create(
                division_id=division.pk,
                jurisdiction_id=self.federal_government.pk,
                body=body,
                senate_class=translate_senate_class(seat.senate_class),
                defaults=dict(label=seat.__str__(), name=seat.__str__()),
            )

    def build_house_offices(self):
        house_seats = self.election_year.federal.congress.seats.house
        division_level = DivisionLevel.objects.get(name="district")
        body = Body.objects.get(
            slug="house", jurisdiction_id=self.federal_government.pk
        )

        for seat in tqdm(house_seats):
            division = Division.objects.get(
                level=division_level,
                parent__code=seat.state.fips,
                code="00" if not seat.district else seat.district.zfill(2),
            )

            Office.objects.update_or_create(
                division_id=division.pk,
                jurisdiction_id=self.federal_government.pk,
                body=body,
                senate_class=None,
                defaults=dict(label=seat.__str__(), name=seat.__str__()),
            )

    def build_presidency(self):
        president_seat = self.election_year.federal.president

        if president_seat is not None:
            for i in tqdm(range(1)):
                Office.objects.update_or_create(
                    division_id=self.federal_government.division_id,
                    jurisdiction_id=self.federal_government.pk,
                    defaults=dict(
                        label="U.S. President",
                        name="President of the United States",
                        short_label="President",
                        slug="president",
                    ),
                )

    def build_governorships(self):
        governor_seats = [
            state.executive.chief
            for state in self.election_year.states
            if state.executive.chief is not None
        ]

        state_level = DivisionLevel.objects.get(name="state")

        for seat in tqdm(governor_seats):
            state_division = Division.objects.filter(
                level_id=state_level.id
            ).get(code_components__fips__state=seat.state.fips)

            state_government_jurisdiction = Jurisdiction.objects.filter(
                parent_id=self.federal_government.pk
            ).get(division_id=state_division.pk)

            office_name = f"{state_division.name} Governor"

            Office.objects.update_or_create(
                division_id=state_division.pk,
                jurisdiction_id=state_government_jurisdiction.pk,
                defaults=dict(label=office_name, name=office_name),
            )
