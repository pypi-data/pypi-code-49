from collections import namedtuple

_entry = namedtuple(
    "Entry",
    (
        "entry_id category_id category "
        "incident_id incident note "
        "start_time minutes hours"
    ),
)


class ViewEntry(_entry):

    __slots__ = ()

    def to_view(self):
        return (self.start_time, self.minutes, self.category, self.incident, self.note)

    def __str__(self):
        return (
            "   Category: {0.category}\n"
            "   Incident: {0.incident}\n"
            "       Note: {0.note}\n"
            " Start time: {0.start_time}\n"
            "   Duration: {0.minutes}\n"
        ).format(self)


def calc_hours(minutes):
    hours = minutes / 60.0
    return round(hours, 2)
