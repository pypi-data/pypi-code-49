# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import CommonIdentifiersMixin
from geography.models import Division
from government.models import Body


# Imports from election.
from election.models import ElectionDay
from election.models.election_type import ElectionType


class ElectionEvent(CommonIdentifiersMixin, CivicBaseModel):
    """A statewide election event"""

    natural_key_fields = ["division", "election_day", "election_type"]
    uid_prefix = "electionevent"
    default_serializer = "election.serializers.ElectionEventSerializer"

    UPCOMING_MODE = "upcoming"
    IN_PROGRESS_MODE = "in-progress"
    PAST_MODE = "past"

    ELECTION_MODE_CHOICES = (
        (UPCOMING_MODE, "Upcoming"),
        (IN_PROGRESS_MODE, "In progress"),
        (PAST_MODE, "Past"),
    )

    division = models.ForeignKey(
        Division,
        related_name="election_events",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    election_day = models.ForeignKey(
        ElectionDay, related_name="election_events", on_delete=models.PROTECT
    )
    election_type = models.ForeignKey(
        ElectionType,
        related_name="election_events",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    election_mode = models.SlugField(
        max_length=50, choices=ELECTION_MODE_CHOICES, default=UPCOMING_MODE
    )

    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("division", "election_day", "election_type")

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`electionevent:{event type}[({party types})]`
        **identifier**: :code:`<division uid>__<election day uid>__<this uid>`
        """
        self.generate_common_identifiers(
            always_overwrite_slug=True, always_overwrite_uid=True
        )

        super(ElectionEvent, self).save(*args, **kwargs)

    def get_uid_base_field(self):
        return self.election_type.slug

    def get_uid_prefix(self):
        if self.division:
            return "__".join(
                [
                    f"{self.division.uid}",
                    f"{self.election_day.uid}",
                    f"{self.uid_prefix}",
                ]
            )

        return "__".join(
            [
                "division:unknown",
                f"{self.election_day.uid}",
                f"{self.uid_prefix}",
            ]
        )

    @property
    def division_label(self):
        if self.division:
            return self.division.label
        else:
            return "[Unknown area]"

    @property
    def label(self):
        return " ".join(
            [
                f"{self.division_label}",
                f"{self.election_type.get_slug_display()}",
                f"({self.election_day.date.strftime('%Y-%m-%d')})",
            ]
        )

    # def get_statewide_offices(self):
    #     statewide_elections = Election.objects.filter(
    #         election_day=self.election_day, division=self.division
    #     )
    #
    #     offices = []
    #     for election in statewide_elections:
    #         offices.append(election.race.office)
    #
    #     return set(offices)
    #
    # def get_district_offices(self):
    #     district_elections = Election.objects.filter(
    #         election_day=self.election_day, division__parent=self.division
    #     )
    #
    #     offices = []
    #     for election in district_elections:
    #         offices.append(election.race.office)
    #
    #     return set(offices)
    #
    # def has_senate_election(self):
    #     offices = self.get_statewide_offices()
    #     senate = Body.objects.get(label="U.S. Senate")
    #
    #     for office in offices:
    #         if office.body == senate:
    #             return True
    #
    #     return False
    #
    # def has_house_election(self):
    #     offices = self.get_district_offices()
    #     house = Body.objects.get(label="U.S. House of Representatives")
    #
    #     for office in offices:
    #         if office.body == house:
    #             return True
    #
    #     return False
    #
    # def has_governor_election(self):
    #     offices = self.get_statewide_offices()
    #     for office in offices:
    #         if office.slug.endswith("governor"):
    #             return True
    #
    #     return False
