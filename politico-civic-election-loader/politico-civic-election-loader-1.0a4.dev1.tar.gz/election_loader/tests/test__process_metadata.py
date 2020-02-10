# Imports from python.
import json


# Imports from Django.
from django.test import TestCase


# Imports from other dependencies.
from election.models import Candidate
from election.models import CandidateElection
from election.models import Election
from election.models import ElectionCycle
from election.models import ElectionDay
from election.models import ElectionType
from election.models import Race
from entity.models import Person


# Imports from election_loader.
from election_loader.tasks.process_metadata import process_election_metadata
from election_loader.utils.lookups.government import get_house_office


class TestHydrateFromAPI(TestCase):
    fixtures = ["test_process_metadata_fixtures.json"]

    @classmethod
    def setUpTestData(cls):
        with open(
            "election_loader/tests/data/general.house.json"
        ) as json_file:
            test_data = json.load(json_file)
            cls.HOUSE_FIXTURE = test_data[100]
            process_election_metadata.delay(test_data)

        with open(
            "election_loader/tests/data/general.senate.json"
        ) as json_file:
            test_data = json.load(json_file)
            cls.SENATE_FIXTURE = test_data[0]
            process_election_metadata.delay(test_data)

        with open(
            "election_loader/tests/data/general.governor.json"
        ) as json_file:
            test_data = json.load(json_file)
            cls.GOVERNOR_FIXTURE = test_data[0]
            process_election_metadata.delay(test_data)

    def test_election_cycle(self):
        cycle_year = self.HOUSE_FIXTURE["electiondate"][:4]
        self.assertTrue(ElectionCycle.objects.filter(name=cycle_year).exists())

    def test_election_day(self):
        election_day = self.HOUSE_FIXTURE["electiondate"]
        self.assertTrue(ElectionDay.objects.filter(date=election_day).exists())

    def test_race(self):
        office = get_house_office(
            state_id=self.HOUSE_FIXTURE["statepostal"],
            seat_num=self.HOUSE_FIXTURE["seatnum"].zfill(2),
        )
        race = Race.objects.filter(office=office)
        self.assertTrue(race.exists())

    def test_election_type(self):
        election_type = ElectionType.objects.filter(
            slug=ElectionType.GENERAL, label="General"
        )
        self.assertTrue(election_type.exists())

    def test_person(self):
        person = Person.objects.filter(
            first_name=self.HOUSE_FIXTURE["first"],
            last_name=self.HOUSE_FIXTURE["last"],
        )
        self.assertTrue(person.exists())

    def test_candidate(self):
        candidate = Candidate.objects.filter(
            ap_candidate_id="polnum-{}".format(self.HOUSE_FIXTURE["polnum"])
        )
        self.assertTrue(candidate.exists())

    def test_election(self):
        office = get_house_office(
            state_id=self.HOUSE_FIXTURE["statepostal"],
            seat_num=self.HOUSE_FIXTURE["seatnum"].zfill(2),
        )
        race = Race.objects.get(office=office)
        election = Election.objects.filter(race=race)
        self.assertTrue(election.exists())

    def test_candidate_election(self):
        office = get_house_office(
            state_id=self.HOUSE_FIXTURE["statepostal"],
            seat_num=self.HOUSE_FIXTURE["seatnum"].zfill(2),
        )
        race = Race.objects.get(office=office)
        election = Election.objects.get(race=race)
        candidate = Candidate.objects.get(
            ap_candidate_id="polnum-{}".format(self.HOUSE_FIXTURE["polnum"])
        )
        candidate_election = CandidateElection.objects.filter(
            election=election, candidate=candidate
        )
        self.assertTrue(candidate_election.exists())
