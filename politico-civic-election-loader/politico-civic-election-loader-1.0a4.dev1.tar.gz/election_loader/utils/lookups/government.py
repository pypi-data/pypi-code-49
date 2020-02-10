# Imports from other dependencies.
from government.models import Body
from government.models import Jurisdiction
from government.models import Office
from government.models import Party


# Imports from election_loader.
from election_loader.utils.lookups.geography import get_district_division
from election_loader.utils.lookups.geography import get_federal_division
from election_loader.utils.lookups.geography import get_state_division


# Jurisdictions
def get_federal_jurisdiction():
    return Jurisdiction.objects.get(division=get_federal_division())


def get_state_jurisdiction(state_id):
    return Jurisdiction.objects.get(division=get_state_division(state_id))


# Bodies
def get_federal_house():
    return Body.objects.get(
        jurisdiction=get_federal_jurisdiction(), slug="house"
    )


def get_federal_senate():
    return Body.objects.get(
        jurisdiction=get_federal_jurisdiction(), slug="senate"
    )


# Offices
def get_house_office(state_id, seat_num):
    return Office.objects.get(
        body=get_federal_house(),
        jurisdiction=get_federal_jurisdiction(),
        division=get_district_division(state_id, district_code=seat_num),
    )


def get_senate_office(state_id, senate_class):
    # Reformat AP-style senate class
    if senate_class.upper() == "CLASS I":
        senate_class = Office.FIRST_CLASS
    elif senate_class.upper() == "CLASS II":
        senate_class = Office.SECOND_CLASS
    elif senate_class.upper() == "CLASS III":
        senate_class = Office.THIRD_CLASS
    return Office.objects.get(
        body=get_federal_senate(),
        jurisdiction=get_federal_jurisdiction(),
        division=get_state_division(state_id),
        senate_class=senate_class,
    )


def get_governor_office(state_id):
    return Office.objects.get(
        body=None,
        division=get_state_division(state_id),
        jurisdiction=get_state_jurisdiction(state_id),
    )


def get_president_office():
    return Office.objects.get(
        body=None,
        division=get_federal_division(),
        jurisdiction=get_federal_jurisdiction(),
    )


def get_office_for_race(race):
    office = None

    if race["officeid"] == "H":
        office = get_house_office(
            state_id=race["statepostal"], seat_num=race["seatnum"].zfill(2)
        )
    elif race["officeid"] == "S":
        office = get_senate_office(
            state_id=race["statepostal"], senate_class=race["description"]
        )
    elif race["officeid"] == "P":
        office = get_president_office()
    elif race["officeid"] == "G":
        office = get_governor_office(state_id=race["statepostal"])

    return office


# Party
def get_party(ap_party_code):
    return Party.objects.get(ap_code=ap_party_code)
