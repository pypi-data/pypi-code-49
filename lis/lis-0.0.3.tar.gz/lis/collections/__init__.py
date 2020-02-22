class ObjectView(object):
    def __init__(self, data: dict):
        self.__dict__ = data


def objectize(dict_data: dict):
    assert isinstance(dict_data, dict), 'only dict type are supported'
    return ObjectView(dict_data)
