import logging
from . import rule
from .timeseries_metadata import TimeseriesMetadataField
from .data_list import DataList
from .field import Field

class TimeseriesBusinessCheck(Field):
    def __init__(self):
        """
        :param metadata_names:
        :param rules: list of Rule objects
        """
        super().__init__()
        self.name = "Timeseries Check"
        self.value = {}

        self.data = DataList()
        self.fields = [self.data]  # will add fields when needed for use case
        self.rules = [rule.has_field(x.name) for x in self.fields]
        self.errors = {}

    def error(self, dct: dict):
        logging.error(dct)  # ERROR:root:error message
        for k, v in dct.items():
            if type(v) == str:
                v = [v]
            if k not in self.errors:
                self.errors[k] = v  # add new error list
            else:
                self.errors[k] = self.errors[k] + v  # append to old error list
        return

    def error_many(self, msgs: list):
        # msgs is a list of dictionaries
        if msgs:
            for msg in msgs:
                self.error(msg)
        return

    def run_check(self, new_check, condition=None):
        """
        Returns errors only from that check
        :param condition:
        :param new_check:
        :return:
        """
        error = new_check.run(self.data.value, condition)
        if error:
            self.error({new_check.name: error})
        return
