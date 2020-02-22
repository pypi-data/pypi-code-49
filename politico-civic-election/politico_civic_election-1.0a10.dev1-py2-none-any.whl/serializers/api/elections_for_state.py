# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer
from geography.models import Division
from rest_framework import serializers


# Imports from election.
from election.serializers.api.election_event import ElectionEventAPISerializer


class StatewiseElectionAPISerializer(CommandLineListSerializer):
    fips = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()

    def get_fips(self, obj):
        return obj.code_components.get("fips", {"state": "-"}).get("state")

    def get_elections(self, obj):
        return ElectionEventAPISerializer(
            obj.election_events.all(), many=True
        ).data

    class Meta(CommandLineListSerializer.Meta):
        model = Division
        fields = ("name", "fips", "slug", "elections")
