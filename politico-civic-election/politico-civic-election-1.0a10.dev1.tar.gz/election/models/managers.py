# Imports from other dependencies.
from civic_utils.models.managers import CivicBaseManager


# Imports from election.
from election.models.querysets import RaceQuerySet


class RaceManager(CivicBaseManager):
    def get_queryset(self):
        return RaceQuerySet(self.model, using=self._db)

    def filter_by_cycle(self, cycle_slug):
        return self.get_queryset().filter_by_cycle(cycle_slug)

    def filter_by_body(self, body_name):
        return self.get_queryset().filter_by_body(body_name)

    def filter_by_state(self, state_raw):
        return self.get_queryset().filter_by_state(state_raw)
