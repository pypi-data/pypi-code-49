from datetime import datetime
from json import JSONEncoder


class DataEncoder(JSONEncoder):
    def encode(self, o):
        if isinstance(o, datetime):
            return o.__str__()
        return super(DataEncoder, self).encode(o)
