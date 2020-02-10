# Imports from other dependencies.
from election.models import Election
from election.models import ElectionBallot
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
    uid = serializers.SerializerMethodField()
    elections = serializers.SerializerMethodField()
    parties = serializers.SerializerMethodField()
    division = serializers.SerializerMethodField()

    def get_uid(self, obj):
        """Division UID, without 'division:division:' duplication."""
        return obj.uid.replace("division:division:", "division:")

    def get_parties(self, obj):
        """All parties."""
        return PartySerializer(Party.objects.all(), many=True).data

    def get_division(self, obj):
        """Division."""
        if obj.level.name == DivisionLevel.DISTRICT:
            return DivisionSerializer(obj.parent).data

        return DivisionSerializer(obj).data

    def get_elections(self, obj):
        """All elections in a division on a given day."""
        election_day = ElectionDay.objects.get(
            date=self.context["election_date"]
        )

        overall_event_ids = election_day.election_events.filter(
            division_id=obj.pk
        ).values_list("id", flat=True)

        overall_ballot_ids = ElectionBallot.objects.filter(
            election_event_id__in=overall_event_ids
        ).values_list("id", flat=True)

        print(overall_ballot_ids)

        elections = list(
            Election.objects.filter(election_ballot_id__in=overall_ballot_ids)
        )

        district = DivisionLevel.objects.get(name=DivisionLevel.DISTRICT)
        for district in obj.children.filter(level=district):
            district_event_ids = election_day.election_events.filter(
                division_id=district.pk
            ).values_list("id", flat=True)

            district_ballot_ids = ElectionBallot.objects.filter(
                election_event_id__in=district_event_ids
            ).values_list("id", flat=True)

            elections.extend(
                list(
                    Election.objects.filter(
                        election_ballot_id__in=district_ballot_ids
                    )
                )
            )

        return ElectionSerializer(elections, many=True).data

    class Meta:
        model = Division
        fields = ("uid", "elections", "parties", "division")
