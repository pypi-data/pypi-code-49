# Imports from Django.
from django.contrib import admin


# Imports from election.
# from election.models import CandidateElection
# from election.models import ElectionDay
from election.models.election_type import ElectionType


PRIMARY_TYPE = ElectionType.PARTISAN_PRIMARY


class ElectionBallotAdmin(admin.ModelAdmin):
    autocomplete_fields = ["election_event"]
    list_display = (
        "get_election_event_name",
        "get_party_name",
        "get_election_event_date",
        "offices_elected",
    )
    list_select_related = (
        "election_event",
        "election_event__division",
        "election_event__election_day",
        "election_event__election_type",
        "party",
        # "election_ballot__election_event",
        # "election_ballot__election_event__election_day",
        # "election_ballot__election_event__election_type",
        # "race",
        # "race__office",
    )
    readonly_fields = ("uid", "slug")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "election_event",
                    "party",
                    "offices_elected",
                    "overall_notes",
                )
            },
        ),
        (
            "Voter registration",
            {
                "fields": (
                    "online_registration_deadline",
                    "registration_deadline",
                    "registration_notes",
                )
            },
        ),
        (
            "Early voting",
            {
                "fields": (
                    "early_vote_start",
                    "early_vote_close",
                    "early_voting_notes",
                )
            },
        ),
        (
            "Voting by mail",
            {
                "fields": (
                    "vote_by_mail_application_deadline",
                    "vote_by_mail_ballot_deadline",
                )
            },
        ),
        (
            "Primary openness",
            {
                "fields": (
                    "who_can_vote",
                    "voters_register_by_party",
                    "party_reaffiliation_deadline_independent_voters",
                    "party_reaffiliation_deadline_other_party_voters",
                    "voting_reaffiliates_automatically",
                )
            },
        ),
        ("Election day information", {"fields": ("poll_closing_time",)}),
        ("Record locators", {"fields": ("uid", "slug")}),
    )

    def get_election_event_name(self, obj):
        return " ".join(
            [
                f"{obj.election_event.division_label}",
                f"{obj.election_event.election_type.get_slug_display()}",
            ]
        )

    get_election_event_name.short_description = "Election event"
    get_election_event_name.admin_order_field = (
        "election_event__division__slug"
    )

    def get_party_name(self, obj):
        if obj.party:
            return obj.party.label

        return "-"

    get_party_name.short_description = "Party"
    get_party_name.admin_order_field = "party"

    def get_election_event_date(self, obj):
        return obj.election_event.election_day.date.strftime("%Y-%m-%d")

    get_election_event_date.short_description = "Date"
    get_election_event_date.admin_order_field = (
        "election_event__election_day__date"
    )
