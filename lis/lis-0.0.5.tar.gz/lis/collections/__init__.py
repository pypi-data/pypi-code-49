class ObjectView(object):
    def __init__(self, data: dict):
        self.__dict__ = data


def objectize(data, recursive=True):
    if not isinstance(data, dict):
        return data

    if recursive:
        return ObjectView(dict([(k, objectize(v)) for k, v in data.items()]))
    else:
        return ObjectView(data)
