# Imports from other dependencies.
from election.models import ElectionDay
from geography.models import Division
from geography.models import DivisionLevel
from rest_framework.exceptions import APIException
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Imports from election_loader.
from election_loader.serializers import StateListSerializer
from election_loader.serializers import StateSerializer
from election_loader.utils.api_auth import CsrfExemptSessionAuthentication
from election_loader.utils.api_auth import TokenAPIAuthentication


class StateMixin(object):
    def get_queryset(self):
        """
        Returns a queryset of all states holding a non-special election on
        a date.
        """
        try:
            date = ElectionDay.objects.get(date=self.kwargs["date"])
        except Exception:
            raise APIException(
                "No elections on {}.".format(self.kwargs["date"])
            )

        elections_for_day = date.election_events.filter()

        division_ids = []
        if len(elections_for_day) > 0:
            for event in date.election_events.all():
                if event.division.level.name == DivisionLevel.STATE:
                    division_ids.append(event.division.uid)
                elif event.division.level.name == DivisionLevel.DISTRICT:
                    division_ids.append(event.division.parent.uid)

        return Division.objects.filter(uid__in=division_ids)

    def get_serializer_context(self):
        """Adds ``election_day`` to serializer context."""
        context = super(StateMixin, self).get_serializer_context()
        context["election_date"] = self.kwargs["date"]
        return context


class StateList(StateMixin, generics.ListAPIView):
    authentication_classes = [
        CsrfExemptSessionAuthentication,
        TokenAPIAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = StateListSerializer


class StateDetail(StateMixin, generics.RetrieveAPIView):
    authentication_classes = [
        CsrfExemptSessionAuthentication,
        TokenAPIAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = StateSerializer
