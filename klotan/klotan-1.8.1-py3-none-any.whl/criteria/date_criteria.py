import dateutil.parser
from datetime import datetime

from klotan.criteria.core import fn_to_criteria


@fn_to_criteria
def is_date(date_format=None):
    def is_date_wrapper(date):
        if date_format is not None:
            try:
                datetime.strptime(date, date_format)
                return True
            except ValueError:
                return False
        else:
            try:
                dateutil.parser.parse(date)
                return True
            except ValueError:
                return False

    return is_date_wrapper
