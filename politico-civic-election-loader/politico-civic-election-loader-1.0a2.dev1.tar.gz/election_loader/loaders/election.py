# Imports from python.
from datetime import datetime


# Imports from other dependencies.
from election.models import Candidate
from election.models import CandidateElection
from election.models import Election
from election.models import ElectionBallot
from election.models import ElectionCycle
from election.models import ElectionDay
from election.models import ElectionEvent
from election.models import ElectionType
from election.models import Race
from entity.models import Person


# Imports from election_loader.
from election_loader.utils.lookups.election import get_election_type_slug
from election_loader.utils.lookups.geography import get_state_division
from election_loader.utils.lookups.geography import get_district_division
from election_loader.utils.lookups.government import get_governor_office
from election_loader.utils.lookups.government import get_house_office
from election_loader.utils.lookups.government import get_office_for_race
from election_loader.utils.lookups.government import get_party
from election_loader.utils.lookups.government import get_president_office
from election_loader.utils.lookups.government import get_senate_office


def create_election_cycle(race):
    year = race["electiondate"][:4]
    cycle, created = ElectionCycle.objects.get_or_create(name=year)
    return cycle


def create_election_day(race):
    date = datetime.strptime(race["electiondate"], "%Y-%m-%d")
    cycle = create_election_cycle(race)

    day, created = ElectionDay.objects.get_or_create(cycle=cycle, date=date)

    return day


def create_race(race):
    election_cycle = create_election_cycle(race)

    if race["officeid"] == "H":
        if not race["seatnum"]:
            race["seatnum"] = ""

    office = get_office_for_race(race)

    race_params = dict(
        office=office,
        cycle=election_cycle,
        special=race["seatname"] == "Unexpired Term"
        or race["racetype"].startswith("Special"),
    )

    if race["officeid"] == "P":
        if race["seatnum"]:
            race_params["division"] = get_district_division(
                race["statepostal"], race["seatnum"].zfill(2)
            )
        else:
            race_params["division"] = get_state_division(race["statepostal"])

    race, created = Race.objects.get_or_create(**race_params)
    return race


def create_election_type(race):
    if race["racetype"].startswith("Special "):
        formatted_race_type = race["racetype"].lstrip("Special ")
    else:
        formatted_race_type = race["racetype"]

    type_slug = get_election_type_slug(formatted_race_type, race["racetypeid"])

    if type_slug is None:
        return None

    election_type, created = ElectionType.objects.get_or_create(slug=type_slug)

    if created:
        election_type.save()

    return election_type


def create_person(race):
    person, created = Person.objects.get_or_create(
        first_name=race["first"],
        last_name=race["last"],
        identifiers={"ap_polid": race["polid"]},
    )
    return person


def create_candidate(race):
    candidate, created = Candidate.objects.get_or_create(
        cycle=create_election_cycle(race),
        office=get_office_for_race(race),
        person=create_person(race),
        party=get_party(race["party"]),
        ap_candidate_id="polid-{}".format(race["polid"]),
        incumbent=race["incumbent"],
    )

    return candidate


def create_election_event(race):
    election_type = create_election_type(race)

    if election_type is None:
        return None

    election_event, created = ElectionEvent.objects.get_or_create(
        division=get_state_division(race["statepostal"]),
        election_day=create_election_day(race),
        election_type=election_type,
    )

    return election_event


def create_election_ballot(race):
    election_event = create_election_event(race)

    if election_event is None:
        return None

    # In traditional primaries and caucuses, this election will be tied to one
    # party's ballot.
    party = None
    if race["racetype"] == "Open Primary" and race["racetypeid"] == "X":
        pass
    elif "Primary" in race["racetype"] or "Caucus" in race["racetype"]:
        party = get_party(race["party"])

    # If this is the first time the given election ballot is seen, set the
    # initial value of 'offices_elected' to reflect whether the current race is
    # a presidential or downticket contest.
    if race["officeid"] == "P":
        initial_offices_elected = ElectionBallot.PRESIDENTIAL_OFFICE
    else:
        initial_offices_elected = ElectionBallot.DOWNTICKET_OFFICES

    election_ballot, created = ElectionBallot.objects.get_or_create(
        election_event=election_event,
        party=party,
        defaults=dict(offices_elected=initial_offices_elected),
    )

    # If this election ballot was already created for another race, see whether
    # the ballot's 'offices_elected' value is different from this round's
    # would-be initial value.

    # This difference will only happen when a ballot has already been created
    # as part of a presidential race, but is then linked when creating a
    # non-presidential race in this repetition — or vice versa.

    # In this case, the ballot's actual 'offices_elected' value will now be set
    # to "All races".
    if not created:
        if election_ballot.offices_elected != initial_offices_elected:
            ElectionBallot.objects.filter(pk=election_ballot.pk).update(
                offices_elected=ElectionBallot.ALL_OFFICES
            )

    return election_ballot


def create_election(race):
    election_ballot = create_election_ballot(race)

    if election_ballot is None:
        return None

    election, created = Election.objects.get_or_create(
        election_ballot=election_ballot,
        race=create_race(race),
        ap_election_id=race["raceid"],
    )

    return election


def create_candidate_election(race):
    election = create_election(race)

    if election is None:
        print(f"NOT CREATING ITEM WITH TYPE {race['racetypeid']}.")
        return None

    party = get_party(race["party"])
    candidate_election, created = CandidateElection.objects.get_or_create(
        ap_candidate_number=("polnum-{}".format(race["polnum"])),
        candidate=create_candidate(race),
        election=election,
        uncontested=race["uncontested"],
        aggregable=party.aggregate_candidates,
    )

    return candidate_election
