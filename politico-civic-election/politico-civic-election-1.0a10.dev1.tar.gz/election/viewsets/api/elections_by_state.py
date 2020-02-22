# Imports from Django.
from django.db.models import Prefetch


# Imports from other dependencies.
from geography.models import Division
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet


# Imports from elections.
from election.models import ElectionBallot
from election.models import ElectionCycle
from election.models import ElectionDataURL
from election.models import ElectionEvent
from election.models import ElectionType
from election.serializers.api import StatewiseElectionAPISerializer
from election.utils.api_auth import CsrfExemptSessionAuthentication
from election.utils.api_auth import SimpleAuthentication


class StatewiseElectionsViewSet(ReadOnlyModelViewSet):
    """"""

    ALL_PRIMARIES_CHOICE = "all-primaries"
    GENERAL_ELECTIONS_CHOICE = "general-elections"

    ELECTION_TYPE_CHOICES = [
        (ALL_PRIMARIES_CHOICE, "All primaries"),
        (GENERAL_ELECTIONS_CHOICE, "All general elections"),
        *ElectionType.TYPES,
    ]

    GROUPED_ELECTION_TYPE_CROSSWALK = {
        ALL_PRIMARIES_CHOICE: [
            ElectionType.PARTISAN_CAUCUS,
            ElectionType.PARTISAN_FIREHOUSE_CAUCUS,
            ElectionType.PARTISAN_PRIMARY,
            ElectionType.TOP_TWO_PRIMARY,
            ElectionType.MAJORITY_ELECTS_BLANKET_PRIMARY,
        ],
        GENERAL_ELECTIONS_CHOICE: [ElectionType.GENERAL],
    }

    authentication_classes = [
        CsrfExemptSessionAuthentication,
        SimpleAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    queryset = Division.objects.all()
    serializer_class = StatewiseElectionAPISerializer

    def get_queryset(self):
        election_type_filter = {}

        election_type_querystring = self.request.query_params.get(
            "election_type", None
        )

        if (
            election_type_querystring
            and election_type_querystring
            not in dict(self.ELECTION_TYPE_CHOICES).keys()
        ):
            raise APIException(
                f"Invalid election type '{election_type_querystring}'. "
                "Please choose a valid type."
            )
        elif (
            election_type_querystring
            and election_type_querystring in dict(ElectionType.TYPES).keys()
        ):
            election_type_filter[
                "election_type__slug"
            ] = election_type_querystring
        elif election_type_querystring:
            election_type_filter[
                "election_type__slug__in"
            ] = self.GROUPED_ELECTION_TYPE_CROSSWALK[election_type_querystring]

        selected_cycle = ElectionCycle.objects.get(name=self.kwargs["year"])

        cycle_day_ids = selected_cycle.elections_days.values_list(
            "id", flat=True
        )

        cycle_event_division_ids = (
            ElectionEvent.objects.filter(election_day_id__in=cycle_day_ids)
            .values_list("division_id", flat=True)
            .distinct()
        )

        return (
            Division.objects.filter(id__in=cycle_event_division_ids)
            .prefetch_related(
                Prefetch(
                    "election_events",
                    queryset=ElectionEvent.objects.filter(
                        election_day__cycle_id=selected_cycle.pk,
                        **election_type_filter,
                    )
                    .prefetch_related(
                        Prefetch(
                            "ballots",
                            queryset=ElectionBallot.objects.select_related(
                                "party"
                            ).order_by("party__ap_code"),
                        ),
                        Prefetch(
                            "data_urls",
                            queryset=ElectionDataURL.objects.filter(
                                url_type=ElectionDataURL.METADATA_URL_TYPE
                            ),
                            to_attr="metadata_urls",
                        ),
                        Prefetch(
                            "data_urls",
                            queryset=ElectionDataURL.objects.filter(
                                url_type=ElectionDataURL.POLLED_URL_TYPE
                            ),
                            to_attr="polled_urls",
                        ),
                    )
                    .select_related("election_day", "election_type")
                    .order_by("election_day__date", "election_type__slug"),
                )
            )
            .select_related(
                # TK
            )
            .order_by("name")
        )
