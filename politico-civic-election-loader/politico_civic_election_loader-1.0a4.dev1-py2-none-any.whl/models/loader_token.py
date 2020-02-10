# Imports from python.
import binascii
import os


# Imports from Django.
from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.utils import timezone


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import UniqueIdentifierMixin
from election.models import ElectionDay


class LoaderToken(UniqueIdentifierMixin, CivicBaseModel):
    """
    A specific contest in a race held on a specific day.
    """

    natural_key_fields = ["election_day", "slug"]
    uid_prefix = "loader_token"
    default_serializer = "election.serializers.LoaderTokenSerializer"

    election_day = models.ForeignKey(
        ElectionDay,
        on_delete=models.CASCADE,
        related_name="tokens",
        blank=True,
        null=True,
    )
    slug = models.SlugField(blank=True, max_length=255, editable=True)

    key = models.CharField(
        "API key", blank=True, max_length=40, primary_key=True
    )

    class Meta:
        unique_together = ("election_day", "slug")

    def __str__(self):
        if self.election_day:
            return f"{self.election_day.get_uid_base_field()} – {self.slug}"

        return f"Unbound key '{self.slug}'"

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`loader_token:{description}`
        **identifier**: :code:`<election_day uid>__<this uid>`
        """
        self.generate_unique_identifier(always_overwrite_uid=True)

        if not self.key:
            self.key = self.generate_key()
            self.created = timezone.now()

        super(LoaderToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def get_uid_prefix(self):
        if self.election_day:
            return f"{self.election_day.uid}__{self.uid_prefix}"

        return self.uid_prefix

    @property
    def user(self):
        return AnonymousUser
