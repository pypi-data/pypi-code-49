# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import UniqueIdentifierMixin


class ElectionType(UniqueIdentifierMixin, CivicBaseModel):
    """
    e.g., "General", "Primary"
    """

    natural_key_fields = ["slug"]
    uid_prefix = "electiontype"
    default_serializer = "election.serializers.ElectionTypeSerializer"

    GENERAL = "general"
    PARTISAN_CAUCUS = "partisan-caucus"
    PARTISAN_FIREHOUSE_CAUCUS = "partisan-firehouse-caucus"
    PARTISAN_PRIMARY = "partisan-primary"
    PRIMARY_RUNOFF = "primary-runoff"
    GENERAL_RUNOFF = "general-runoff"

    # Top-two primaries:
    #   - All candidates from all parties appear on the same ballot.
    #   - The top-two finishers advance to a general election.
    #   - These candidates can be from the same party.
    #   - Mainly used in California and Washington.
    TOP_TWO_PRIMARY = "top-two-primary"

    # "Majority-elects" blanket primaries:
    #   - All candidates from all parties appear on the same ballot.
    #   - A candidate is elected outright if they win over 50%.
    #   - Otherwise, a runoff is held between the top-two finshers.
    #   - Mainly used in Louisiana and Mississippi.
    MAJORITY_ELECTS_BLANKET_PRIMARY = "majority-elects-blanket-primary"

    TYPES = (
        (GENERAL, "General election"),
        (PARTISAN_CAUCUS, "Caucus"),
        (PARTISAN_FIREHOUSE_CAUCUS, "Firehouse Caucus"),
        (PARTISAN_PRIMARY, "Primary"),
        (PRIMARY_RUNOFF, "Primary Runoff"),
        (GENERAL_RUNOFF, "General Runoff"),
        (TOP_TWO_PRIMARY, "Top-two Primary"),
        (MAJORITY_ELECTS_BLANKET_PRIMARY, "Majority-elects blanket primary"),
    )

    slug = models.SlugField(
        blank=True, max_length=255, unique=True, choices=TYPES
    )

    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    ap_code = models.CharField(max_length=1, null=True, blank=True)
    number_of_winners = models.PositiveSmallIntegerField(default=1)
    winning_threshold = models.DecimalField(
        decimal_places=3, max_digits=5, null=True, blank=True
    )

    def __str__(self):
        return self.uid

    def save(self, *args, **kwargs):
        """
        **uid field/identifier**: :code:`electiontype:{slug}`
        """
        if not self.label and self.slug != "":
            type_dict = dict(self.TYPES)
            if self.slug in type_dict:
                self.label = type_dict[self.slug]

        self.generate_unique_identifier(always_overwrite_uid=True)

        super(ElectionType, self).save(*args, **kwargs)

    def is_partisan_primary(self):
        if self.slug in [
            self.PARTISAN_PRIMARY,
            self.PARTISAN_CAUCUS,
            # self.TOP_TWO_PRIMARY,
            # self.MAJORITY_ELECTS_BLANKET_PRIMARY,
        ]:
            return True
        else:
            return False

    def is_primary(self):
        if self.slug in [
            self.PARTISAN_PRIMARY,
            self.PARTISAN_CAUCUS,
            self.TOP_TWO_PRIMARY,
            self.MAJORITY_ELECTS_BLANKET_PRIMARY,
        ]:
            return True
        else:
            return False

    def is_runoff(self):
        if self.slug in [self.PRIMARY_RUNOFF, self.GENERAL_RUNOFF]:
            return True
        else:
            return False
