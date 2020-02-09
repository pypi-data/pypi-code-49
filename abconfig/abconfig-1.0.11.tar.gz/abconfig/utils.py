import warnings
from functools import wraps

from abconfig.common import Dict


def ignore_warnings(f):
    @wraps(f)
    def inner(*args, **kwargs):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("ignore")
            response = f(*args, **kwargs)
        return response
    return inner


class GetAttrs(Dict):
    def __init__(self, obj=None, settings=None):
        if not settings: settings = []
        super().__init__({
            str(k): v for k,v in self.is_type(obj).__dict__.items()
            if k[:1] != '_' or k in settings
        })


class Close(Dict):
    def __init__(self, obj: Dict):
        super().__init__(Dict(obj).fmap(self.set_default_type))

    @staticmethod
    def set_default_type(k, v):
        if Dict.is_dict(v):
            return (k, Close(v))
        elif Dict.is_list(v):
            return (k, Dict.is_type(v)([None if isinstance(i, type) else i for i in v]))
        else:
            return (k, None if isinstance(v, type) else v)


class Switch(type):
    def __call__(cls, obj: Dict) -> Dict:
        if cls.__target__.enabled(obj) is True:
            return obj.bind(cls.__target__)
        else:
            return obj
