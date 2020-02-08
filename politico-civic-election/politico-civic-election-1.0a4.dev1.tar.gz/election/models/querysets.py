# Imports from Django.
from django.db.models import Q


# Imports from other dependencies.
from civic_utils.models.querysets import CivicBaseQuerySet
from geography.models import DivisionLevel
from government.models import Jurisdiction
import us


class RaceQuerySet(CivicBaseQuerySet):
    def filter_by_cycle(self, cycle_slug):
        return self.filter(cycle__slug=str(cycle_slug))

    def filter_by_body(self, body_name):
        try:
            FED_GOVT_ID = (
                Jurisdiction.objects.filter(name="U.S. Federal Government")
                .values_list("id", flat=True)
                .get()
            )
        except Jurisdiction.DoesNotExist:
            FED_GOVT_ID = 0

        if body_name == self.model.ELECTORAL_COLLEGE_CHOICE:
            return self.select_related(
                "office__body", "office__division__level"
            ).filter(
                office__body__isnull=True,
                office__division__level__slug=DivisionLevel.COUNTRY,
            )
        elif body_name == self.model.SENATE_CHOICE:
            return self.select_related("office__body").filter(
                office__body__jurisdiction_id=FED_GOVT_ID,
                office__body__slug="senate",
            )
        elif body_name == self.model.HOUSE_CHOICE:
            return self.select_related("office__body").filter(
                office__body__jurisdiction_id=FED_GOVT_ID,
                office__body__slug="house",
            )
        elif body_name == self.model.GOVERNOR_CHOICE:
            return self.select_related(
                "office__body", "office__division__level"
            ).filter(
                office__body__isnull=True,
                office__division__level__slug=DivisionLevel.STATE,
            )

        raise ValueError("Invalid body name.")

    def filter_by_state(self, state_raw):
        state_obj = us.states.lookup(state_raw)

        if state_obj is None:
            raise ValueError("Invalid state name.")

        state_fips = state_obj.fips

        electoral_college_statewide_query = dict(
            office__division__level__slug=DivisionLevel.COUNTRY,
            division__level__slug=DivisionLevel.STATE,
            division__code=state_fips,
        )
        electoral_college_district_query = dict(
            office__division__level__slug=DivisionLevel.COUNTRY,
            division__level__slug=DivisionLevel.DISTRICT,
            division__parent__code=state_fips,
        )
        senate_query = dict(
            office__division__level__slug=DivisionLevel.STATE,
            office__body__isnull=False,
            office__division__code=state_fips,
        )
        house_query = dict(
            office__division__level__slug=DivisionLevel.DISTRICT,
            office__division__parent__code=state_fips,
        )
        governor_query = dict(
            office__division__level__slug=DivisionLevel.STATE,
            office__body__isnull=True,
            office__division__code=state_fips,
        )

        return (
            self.select_related(
                "division",
                "division__level",
                "division__parent",
                "office",
                "office__body",
                "office__body__organization",
                "office__division",
                "office__division__level",
                "office__division__parent",
            )
            .filter(
                Q(**electoral_college_statewide_query)
                | Q(**electoral_college_district_query)
                | Q(**senate_query)
                | Q(**house_query)
                | Q(**governor_query)
            )
            .order_by(
                "office__short_label",
                "office__body__organization__founding_date",
                "-office__body__slug",
                "office__division__code",
            )
        )
