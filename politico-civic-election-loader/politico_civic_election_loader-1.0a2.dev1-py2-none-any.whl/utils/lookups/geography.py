# Imports from other dependencies.
from geography.models import Division
from geography.models import DivisionLevel
import us


# DivisionLevels
def get_federal_level():
    return DivisionLevel.objects.get(name=DivisionLevel.COUNTRY)


def get_state_level():
    return DivisionLevel.objects.get(name=DivisionLevel.STATE)


def get_district_level():
    return DivisionLevel.objects.get(name=DivisionLevel.DISTRICT)


# Divisions
def get_federal_division():
    return Division.objects.get(level=get_federal_level())


def get_state_division(state_id):
    state = us.states.lookup(state_id)
    return Division.objects.get(level=get_state_level(), code=state.fips)


def get_district_division(state_id, district_code):
    state_divisions = Division.objects.filter(
        parent=get_state_division(state_id), level=get_district_level()
    )
    # If only one at-large district, return it and nevermind the AP's
    # silly code...
    if state_divisions.count() == 1:
        return state_divisions[0]
    # ... otherwise, use the code
    return state_divisions.get(code=district_code)
