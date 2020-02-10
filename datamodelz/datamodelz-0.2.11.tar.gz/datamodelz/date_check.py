import logging
from datetime import datetime
from . import rule
from .timeseries_response import TimeseriesResponseField
from .field import DateField


class DateCheck(TimeseriesResponseField):
    def __init__(self):
        """
        :param metadata_fields: list of string names
        """
        super().__init__()
        self.name = "date checks"
        self.metadata.fields = [
            self.metadata.start_time,
            self.metadata.delay
        ]
        self.metadata.rules = [
            rule.has_field(self.metadata.start_time.name),
            rule.has_field(self.metadata.delay.name)
        ]
        self.data.rules = [
            rule.Rule("Check has valid date after start_time", lambda x: self.valid_date(x)),
            rule.Rule("Check has recent date", lambda x: self.recent_date(x)),
        ]

    def valid_date(self, data_lst):
        # running check on list of TimeseriesObjectField
        start_time = self.metadata.start_time
        for obj in data_lst:
            if obj.date.before(start_time):
                logging.error("TimeseriesDateCheck: date {} is before start_time {}"
                              .format(obj.date.value, start_time.value))
                return False
        return True

    def recent_date(self, data_lst):
        recent = DateField("now")
        recent.value = datetime.now() - datetime.fromtimestamp(self.metadata.delay // 1e9)
        for date_obj in data_lst[::-1]:
            if date_obj.after(recent):
                return True
        return False
