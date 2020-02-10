# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import CommonIdentifiersMixin

# from geography.models import Division
# from government.models import Body


# Imports from election.
# from election.models import ElectionEvent

# from election.models.election_type import ElectionType


class ElectionDataURL(CommonIdentifiersMixin, CivicBaseModel):
    """A statewide election event"""

    natural_key_fields = ["election_event", "url_descriptor"]
    uid_prefix = "electiondataurl"
    default_serializer = "election.serializers.ElectionDataURLSerializer"

    METADATA_URL_TYPE = "metadata"
    POLLED_URL_TYPE = "polled"

    URL_TYPE_CHOICES = (
        (METADATA_URL_TYPE, "Metadata"),
        (POLLED_URL_TYPE, "Frequently-updated data"),
    )

    election_event = models.ForeignKey(
        "ElectionEvent", related_name="data_urls", on_delete=models.PROTECT
    )

    url_type = models.SlugField(
        max_length=15, choices=URL_TYPE_CHOICES, default=POLLED_URL_TYPE
    )
    url_descriptor = models.SlugField(max_length=25)
    url_path = models.URLField()

    class Meta:
        unique_together = ("election_event", "url_descriptor")

    def __str__(self):
        return f'{self.election_event.label}: "{self.url_descriptor}" URL'

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`electionevent:{event type}[({party types})]`
        **identifier**: :code:`<division uid>__<election day uid>__<this uid>`
        """
        self.generate_common_identifiers(
            always_overwrite_slug=True, always_overwrite_uid=True
        )

        super(ElectionDataURL, self).save(*args, **kwargs)

    def get_uid_base_field(self):
        return self.url_descriptor

    def get_uid_prefix(self):
        return "__".join([f"{self.election_event.uid}", f"{self.uid_prefix}"])
