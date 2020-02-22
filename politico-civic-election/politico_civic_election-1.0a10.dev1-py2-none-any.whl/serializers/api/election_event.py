# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer
from rest_framework import serializers


# Imports from election.
from election.models import ElectionDataURL
from election.models import ElectionEvent
from election.serializers.api.election_ballot import (
    ElectionBallotAPISerializer,
)
from election.serializers.api.election_data_url import (
    ElectionDataURLAPISerializer,
)


class ElectionEventAPISerializer(CommandLineListSerializer):
    date = serializers.SerializerMethodField()
    election_type = serializers.SerializerMethodField()
    ballots = serializers.SerializerMethodField()
    metadata_urls = serializers.SerializerMethodField()
    polled_data_urls = serializers.SerializerMethodField()

    def get_date(self, obj):
        return obj.election_day.date.strftime("%Y-%m-%d")

    def get_election_type(self, obj):
        return obj.election_type.slug

    def get_ballots(self, obj):
        return ElectionBallotAPISerializer(obj.ballots.all(), many=True).data

    def get_metadata_urls(self, obj):
        serialized_data = ElectionDataURLAPISerializer(
            obj.metadata_urls, many=True
        ).data
        return {
            serialized_url["url_descriptor"]: serialized_url["url_path"]
            for serialized_url in serialized_data
        }

    def get_polled_data_urls(self, obj):
        serialized_data = ElectionDataURLAPISerializer(
            obj.polled_urls, many=True
        ).data
        return {
            serialized_url["url_descriptor"]: serialized_url["url_path"]
            for serialized_url in serialized_data
        }

    class Meta(CommandLineListSerializer.Meta):
        model = ElectionEvent
        fields = (
            "date",
            "election_type",
            "election_mode",
            "ballots",
            "metadata_urls",
            "polled_data_urls",
            "notes",
        )
