# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import CommonIdentifiersMixin
from geography.models import Division
from government.models import Office


# Imports from election.
from election.models.managers import RaceManager


class Race(CommonIdentifiersMixin, CivicBaseModel):
    """
    A race for an office, comprising one or many elections.
    """

    ELECTORAL_COLLEGE_CHOICE = "electoral-college"
    SENATE_CHOICE = "senate"
    HOUSE_CHOICE = "house"
    GOVERNOR_CHOICE = "governorships"

    BODY_CHOICES = (
        (ELECTORAL_COLLEGE_CHOICE, "ElectoralCollege"),
        (SENATE_CHOICE, "Senate"),
        (HOUSE_CHOICE, "House"),
        (GOVERNOR_CHOICE, "Governorships"),
    )

    SPECIAL_RACE_SLUG = "Special"
    STANDARD_RACE_SLUG = "Standard"

    natural_key_fields = ["office", "cycle", "division", "special"]
    uid_prefix = "race"
    default_serializer = "election.serializers.RaceSerializer"

    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    office = models.ForeignKey(
        Office, related_name="races", on_delete=models.PROTECT
    )
    cycle = models.ForeignKey(
        "ElectionCycle", related_name="races", on_delete=models.PROTECT
    )
    division = models.ForeignKey(
        Division,
        related_name="races",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="Generally, only used for the presidency.",
    )
    electoral_votes = models.IntegerField(
        blank=True,
        null=True,
        help_text="The number of presidential electors this area awards.",
    )
    special = models.BooleanField(default=False)

    objects = RaceManager()

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`race:{'standard' or 'special'}`
        **identifier**: :code:`<office uid>__<cycle uid>__<this uid>`
        """
        name_label = f"{self.cycle.name} {self.office.label}"

        if self.special:
            name_label = f"{name_label} {self.SPECIAL_RACE_SLUG}"

        if self.division:
            name_label = f"{name_label} {self.division.label}"

        self.label = name_label

        self.generate_common_identifiers(
            always_overwrite_slug=False, always_overwrite_uid=True
        )

        super(Race, self).save(*args, **kwargs)

    def get_uid_base_field(self):
        return self.label

    def get_uid_prefix(self):
        if self.division:
            return f"{self.office.uid}__{self.cycle.uid}__{self.division.uid}__{self.uid_prefix}"
        return f"{self.office.uid}__{self.cycle.uid}__{self.uid_prefix}"

    def get_uid_suffix(self):
        if self.special:
            return self.SPECIAL_RACE_SLUG.lower()

        return self.STANDARD_RACE_SLUG.lower()
