"Custom functions to use in expressions"
import datetime
from jmespath import functions


class Functions(functions.Functions):
    "Custom functions to use in expressions."

    @functions.signature({'types': ['string']}, {'types': ['string']})
    def _func_date(self, value, date_format):
        "Converts an string to a datetime.date object."
        date = datetime.datetime.strptime(value, date_format)
        return date.date()

    @functions.signature({'types': ['string']}, {'types': ['string']})
    def _func_time(self, value, date_format):
        "Converts an string to a datetime.time object."
        date = datetime.datetime.strptime(value, date_format)
        return date.time()

    @functions.signature({'types': ['string']}, {'types': ['string']})
    def _func_datetime(self, value, date_format):
        "Converts an string to a datetime.datetime object."
        date = datetime.datetime.strptime(value, date_format)
        return date

    @functions.signature({'types': []}, {'types': ['string']})
    def _func_format(self, value, fmt):
        if isinstance(value, (datetime.datetime, datetime.date, datetime.time)):
            return value.strftime(fmt)
        return fmt.format(value)

    @functions.signature({'types': ['boolean']}, {'types': []}, {'types': []})
    def _func_if(self, condition, then_value, else_value):
        if condition:
            return then_value
        else:
            return else_value
