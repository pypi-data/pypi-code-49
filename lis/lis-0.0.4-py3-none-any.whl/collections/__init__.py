class ObjectView(object):
    def __init__(self, data: dict):
        self.__dict__ = data


def objectize(data):
    if not isinstance(data, dict):
        return data
    return ObjectView(dict([(k, objectize(v)) for k, v in data.items()]))
