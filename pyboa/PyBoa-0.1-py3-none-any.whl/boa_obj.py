import random
import functools


class Dict(dict):
    def __init__(self, d):
        for k, v in d.items():
            d[k] = to_boa(v)
        super().__init__(d)

    def __getattribute__(self, name):
        """get, if exist, ``dict`` data then ``dict`` attribut"""
        if name in dict.keys(self):
            return dict.get(self, name)
        return super(Dict, self).__getattribute__(name)

    def __setattr__(self, name, value):
        boa = to_boa(value)
        dict.update(self, {name: boa})

    def __setitem__(self, key, value):
        boa = to_boa(value)
        dict.update(self, {key: boa})

    def toPython(self):
        return to_py(self)


class List(list):
    def __init__(self, li):
        super().__init__(map(to_boa, li))

    def map(self, fun):
        return List(map(fun, self))

    def reduce(self, fun):
        return functools.reduce(fun, self)

    def filter(self, fun):
        return List(filter(fun, self))

    def index(self, elem, *args, raise_exception=False):
        try:
            return super().index(elem, *args)
        except ValueError as e:
            if raise_exception:
                raise e
            return None

    def reverse(self):
        return List(self[::-1])

    def shuffle(self):
        li = self[:]
        random.shuffle(li)
        return li

    def randomTake(self):
        return random.choice(self)

    def copy(self):
        return List(self[:])

    def append(self, el):
        list.append(self, to_boa(el))

    def toPython(self):
        return to_py(self)


def to_boa(data):
    """
        transforme recursively a Python ``dict``, ``list`` into a Boa
        :param data: insert any Python data
        :return: the corresponding Boa data
    """
    if isinstance(data, list) or isinstance(data, tuple):
        return List(map(to_boa, data))
    elif isinstance(data, dict):
        return Dict(data)
    else:
        return data


def to_py(data):
    if isinstance(data, List):
        return list(map(to_py, data))
    elif isinstance(data, Dict):
        for k in data:
            data[k] = to_py(data[k])
        return dict(data)
    else:
        return data
