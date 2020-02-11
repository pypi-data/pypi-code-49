from datetime import datetime, date, time
from decimal import Decimal

from flask.json import JSONEncoder


class JsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode("ASCII")
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return datetime.strftime(obj, '%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return date.strftime(obj, '%Y-%m-%d')
        elif isinstance(obj, time):
            return time.strftime(obj, '%H:%M:%S')
        return JSONEncoder.default(self, obj)
