from harpo.util import ParametricSingleton


class User(metaclass=ParametricSingleton):
    def __init__(self, name: str, key_fingerprint: str, **_):
        self.name = name
        self.key_fingerprint = key_fingerprint

    def dict(self):
        wanted_keys = ['name', 'key_fingerprint']
        return dict((k, self.__dict__[k]) for k in wanted_keys if k in self.__dict__)

    def __repr__(self):
        return self.name
