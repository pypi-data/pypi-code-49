# Imports from other dependencies.
from election.models import ElectionDay
from geography.models import Division
from geography.models import DivisionLevel
from government.models import Party
from rest_framework import serializers
from rest_framework.reverse import reverse


# Imports from election_loader.
from election_loader.serializers.division import DivisionSerializer
from election_loader.serializers.election import ElectionSerializer
from election_loader.serializers.party import PartySerializer


class StateListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse(
            "electionnight_api_state-election-detail",
            request=self.context["request"],
            kwargs={"pk": obj.pk, "date": self.context["election_date"]},
        )

    class Meta:
        model = Division
        fields = ("url", "uid", "name")


class StateSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()

    def get_division(self, obj):
        """Division."""
        if obj.level.name == DivisionLevel.DISTRICT:
            return DivisionSerializer(obj.parent).data

        return DivisionSerializer(obj).data

    def get_parties(self, obj):
        """All parties."""
        return PartySerializer(Party.objects.all(), many=True).data

    def get_elections(self, obj):
        """All elections in division."""
        election_day = ElectionDay.objects.get(
            date=self.context["election_date"]
        )

        elections = list(obj.elections.filter(election_day=election_day))
        district = DivisionLevel.objects.get(name=DivisionLevel.DISTRICT)
        for district in obj.children.filter(level=district):
            elections.extend(
                list(district.elections.filter(election_day=election_day))
            )

        return ElectionSerializer(elections, many=True).data

    class Meta:
        model = Division
        fields = ("uid", "elections", "parties", "division")
