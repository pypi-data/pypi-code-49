# Imports from election.
from election.models.election_ballot import ElectionBallot


def load_election_metadata(election_data):
    """"""
    additional_election_data = {
        "early_vote_start": getattr(  # DateField.
            election_data, "early_voting_vip_start_date", None
        ),
        "early_vote_close": getattr(  # DateField.
            election_data, "early_voting_vip_close_date", None
        ),
        "vote_by_mail_application_deadline": getattr(  # DateField.
            election_data, "vote_by_mail_application_deadline", None
        ),
        "vote_by_mail_ballot_deadline": getattr(  # DateField.
            election_data, "early_voting_vbm_return_date", None
        ),
        "early_voting_notes": getattr(  # TextField.
            election_data, "early_voting_notes", None
        ),
        "online_registration_deadline": getattr(  # DateField.
            election_data, "registration_online_deadline", None
        ),
        "registration_deadline": getattr(  # DateField.
            election_data, "registration_deadline", None
        ),
        "registration_notes": getattr(  # TextField.
            election_data, "registration_notes", None
        ),
        "poll_closing_time": getattr(  # DateTimeField.
            election_data, "election_polls_close", None
        ),
        "who_can_vote": getattr(  # TextField.
            election_data, "who_can_vote", None
        ),
        "voters_register_by_party": getattr(  # NullBooleanField.
            election_data, "voters_register_by_party", None
        ),
        "party_reaffiliation_deadline_independent_voters": getattr(  # Date.
            election_data, "party_reaffil_deadline_indeps", None
        ),
        "party_reaffiliation_deadline_other_party_voters": getattr(  # Date.
            election_data, "party_reaffil_deadline_others", None
        ),
        "voting_reaffiliates_automatically": getattr(  # TextField.
            election_data, "voting_reaffiliates_automatically", None
        ),
    }

    raw_election_level = getattr(election_data, "election_level", "downticket")

    if raw_election_level == "president":
        offices_elected = ElectionBallot.PRESIDENTIAL_OFFICE
    elif raw_election_level == "all":
        offices_elected = ElectionBallot.ALL_OFFICES
    elif raw_election_level == "downticket":
        offices_elected = ElectionBallot.DOWNTICKET_OFFICES

    additional_election_data["offices_elected"] = offices_elected

    additional_election_data["overall_notes"] = (
        election_data.election_notes if election_data.election_notes else ""
    )

    return {k: v for k, v in additional_election_data.items() if v is not None}
