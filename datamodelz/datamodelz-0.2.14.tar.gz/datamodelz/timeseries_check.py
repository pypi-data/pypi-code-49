import logging
from . import rule
from .error import Error
from .field import Field
from .company import CompanyField
from .timeseries_metadata import TimeseriesMetadataField
from .data_list import DataList


class TimeseriesCheck(Field):
    def __init__(self):
        """
        :param metadata_names:
        :param rules: list of Rule objects
        """
        super().__init__()
        self.name = "Timeseries Check"
        self.value = {}

        self.metadata = TimeseriesMetadataField()
        self.company = CompanyField()
        self.data = DataList()
        self.reference = ""  # TODO
        self.api_call = ""  # TODO
        self.fields = [self.metadata, self.company, self.data]  # will add fields when needed for use case
        self.rules = [rule.has_field(x.name) for x in self.fields]

    def set(self, value):
        self.value = value
        self.run_rules()
        if self.errors:  # returns any errors
            return self.errors
        self.metadata.rules = []  # default
        self.set_fields(self.fields)
        logging.debug("TimeseriesCheck: data field is set as {}".format(self.data))
        return self.errors

    def fill_in_error(self, error, new_check):
        error.timeseries_code = self.metadata.id.value
        error.check_name = new_check.name
        error.company = self.company.id.value
        error.reference = self.reference
        error.api_call = self.api_call
        self.error(error)

    def run_check(self, new_check, metadata_names=[], other_data = None):
        """
        Returns errors only from that check
        :param other_data:
        :param new_check:
        :param metadata_names:
        :return:
        """
        self.metadata.rules = [rule.has_field(name) for name in metadata_names]
        errors = self.validate_field(self.metadata)  # automatically adds new errors to self.errors
        if errors:  # new errors from check
            return
        error = new_check.run(self.data.value, self.metadata, other_data)
        if error is None:
            return
        if type(error) == Error and not error.empty():
            self.fill_in_error(error, new_check)
        if type(error) == list and error:
            for err in error:  # allows functions to return a list of Error objects
                if not err.empty():
                    self.fill_in_error(err, new_check)
        return

    def error(self, err: Error):
        logging.error(err)  # ERROR:root:error message
        self.errors.append(err)
        return

    def error_many(self, error_lst: list):
        if error_lst:
            self.errors += error_lst
        return

