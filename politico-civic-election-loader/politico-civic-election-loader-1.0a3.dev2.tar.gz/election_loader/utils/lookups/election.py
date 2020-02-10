# Imports from other dependencies.
from election.models import ElectionType


AP_TO_ELECTION_TYPE_SLUG_MAP = {
    # tuple(['', 'G']): ElectionType.GENERAL,
    tuple(["General", "G"]): ElectionType.GENERAL,
    tuple(["Primary", "D"]): ElectionType.PARTISAN_PRIMARY,
    tuple(["Primary", "R"]): ElectionType.PARTISAN_PRIMARY,
    tuple(["Caucus", "E"]): ElectionType.PARTISAN_CAUCUS,
    tuple(["Caucus", "S"]): ElectionType.PARTISAN_CAUCUS,
    tuple(["Runoff", "D"]): ElectionType.PRIMARY_RUNOFF,
    tuple(["Runoff", "R"]): ElectionType.PRIMARY_RUNOFF,
    tuple(["Runoff", "G"]): ElectionType.GENERAL_RUNOFF,
    tuple(["Open Primary", "X"]): ElectionType.TOP_TWO_PRIMARY,
    tuple(["Primary", "G"]): ElectionType.MAJORITY_ELECTS_BLANKET_PRIMARY,
}


def get_election_type_slug(race_type, race_type_id):
    slug_key = tuple([race_type, race_type_id])

    if slug_key in AP_TO_ELECTION_TYPE_SLUG_MAP:
        return AP_TO_ELECTION_TYPE_SLUG_MAP[slug_key]

    return None
