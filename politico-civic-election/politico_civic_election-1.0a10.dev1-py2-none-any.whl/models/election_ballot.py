# Imports from python.
import re


# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import CommonIdentifiersMixin
from government.models import Party


# Imports from election.
from election.models.election_type import ElectionType


PRIMARY_TYPE = ElectionType.PARTISAN_PRIMARY


class ElectionBallot(CommonIdentifiersMixin, CivicBaseModel):
    """A single statewide ballot, up for election on a single day."""

    natural_key_fields = ["election_event", "party"]
    uid_prefix = "electionballot"
    default_serializer = "election.serializers.ElectionBallotSerializer"

    PRESIDENTIAL_OFFICE = "president"
    ALL_OFFICES = "all"
    DOWNTICKET_OFFICES = "downticket"

    OFFICES_ELECTED_TYPES = (
        (PRESIDENTIAL_OFFICE, "Presidential race"),
        (ALL_OFFICES, "Presidential, Congressional & Statewide races"),
        (DOWNTICKET_OFFICES, "Congressional & Statewide races"),
    )

    ONLY_PARTY_MEMBERS_VOTE = "only_party_members"
    PARTY_MEMBERS_AND_INDEPENDENTS_VOTE = "party_members_and_independents"
    ALL_VOTERS_VOTE = "all_voters"

    WHO_CAN_VOTE_CHOICES = (
        (ONLY_PARTY_MEMBERS_VOTE, "Only party members"),
        (PARTY_MEMBERS_AND_INDEPENDENTS_VOTE, "Party members & independents"),
        (ALL_VOTERS_VOTE, "All voters"),
    )

    AUTOMATIC_REAFFILIATION = "yes"
    AUTOMATIC_REAFFILIATION_WITH_PETITION = "yes-unless-immediate-petition"
    NO_REAFFILIATION = "no"

    PARTY_REAFFILIATION_EFFECT_CHOICES = (
        (AUTOMATIC_REAFFILIATION, "Yes"),
        (
            AUTOMATIC_REAFFILIATION_WITH_PETITION,
            "Yes (unless voters file a petition when registering)",
        ),
        (NO_REAFFILIATION, "No"),
    )

    election_event = models.ForeignKey(
        "ElectionEvent", related_name="ballots", on_delete=models.PROTECT
    )
    party = models.ForeignKey(
        Party, null=True, blank=True, on_delete=models.PROTECT
    )
    offices_elected = models.SlugField(
        max_length=15,
        choices=OFFICES_ELECTED_TYPES,
        default=DOWNTICKET_OFFICES,
    )

    overall_notes = models.TextField(blank=True, null=True)

    early_vote_start = models.DateField(null=True, blank=True)
    early_vote_close = models.DateField(null=True, blank=True)
    vote_by_mail_application_deadline = models.DateField(null=True, blank=True)
    vote_by_mail_ballot_deadline = models.DateField(null=True, blank=True)
    early_voting_notes = models.TextField(blank=True, null=True)

    online_registration_deadline = models.DateField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    poll_closing_time = models.DateTimeField(null=True, blank=True)
    registration_notes = models.TextField(blank=True, null=True)

    who_can_vote = models.SlugField(
        max_length=50, choices=WHO_CAN_VOTE_CHOICES, blank=True, null=True
    )
    voters_register_by_party = models.BooleanField(blank=True, null=True)
    party_reaffiliation_deadline_independent_voters = models.DateField(
        blank=True, null=True
    )
    party_reaffiliation_deadline_other_party_voters = models.DateField(
        blank=True, null=True
    )

    voting_reaffiliates_automatically = models.SlugField(
        max_length=50,
        choices=PARTY_REAFFILIATION_EFFECT_CHOICES,
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ("election_event", "party")

    def __str__(self):
        formatted_elex_date = self.election_event.election_day.date.strftime(
            "%Y-%m-%d"
        )

        if (
            self.party
            and self.offices_elected == self.PRESIDENTIAL_OFFICE
            and self.election_event.election_type.is_partisan_primary()
        ):
            event_type_slug = self.election_event.election_type.slug

            if event_type_slug == ElectionType.PARTISAN_CAUCUS:
                return " ".join(
                    [
                        f"{self.election_event.division_label}",
                        f"{self.get_party_possessive()} Presidential Caucus",
                        f"({formatted_elex_date})",
                    ]
                )
            return " ".join(
                [
                    f"{self.election_event.division_label}",
                    f"{self.get_party_possessive()} Presidential Primary",
                    f"({formatted_elex_date})",
                ]
            )
        elif (
            self.party
            and self.offices_elected == self.ALL_OFFICES
            and self.election_event.election_type.is_partisan_primary()
        ):
            return " ".join(
                [
                    f"{self.election_event.division_label}",
                    f"{self.get_party_possessive()}",
                    "Presidential, Congressional & Statewide Primaries",
                    f"({formatted_elex_date})",
                ]
            )
        elif (
            self.party
            and self.election_event.election_type.is_partisan_primary()
        ):
            return " ".join(
                [
                    f"{self.election_event.division_label}",
                    f"{self.get_party_possessive()} Primary",
                    f"({formatted_elex_date})",
                ]
            )

        return f"{self.election_event.label} -- universal ballot"

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`electionevent:{event type}[({party types})]`
        **identifier**: :code:`<division uid>__<election day uid>__<this uid>`
        """
        self.generate_common_identifiers(
            always_overwrite_slug=True, always_overwrite_uid=True
        )

        super(ElectionBallot, self).save(*args, **kwargs)

    def get_uid_base_field(self):
        if self.party:
            return self.party.slug

        return "nonpartisan"

    def get_uid_prefix(self):
        return f"{self.election_event.uid}__{self.uid_prefix}"

    def get_party_possessive(self):
        if self.party:
            return re.sub(r"Party$", "", self.party.organization.name).strip()

        return "Nonpartisan"
