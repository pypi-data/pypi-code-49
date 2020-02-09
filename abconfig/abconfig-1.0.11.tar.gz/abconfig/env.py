from os import environ

from abconfig.common import Dict
from abconfig.utils import Switch


class OSEnviron(Dict):
    def __init__(self, obj: Dict):
        super().__init__(obj + self.read(obj, obj.get('__prefix__', None)))

    def read(self, obj: Dict, prefix: str) -> Dict:
        return Dict([self.env(prefix,k,v) for k,v in obj.items()])

    def env(self, prefix: str, k: str, v: any) -> tuple:
        if self.is_dict(v):
            return (k, self.read(v, self.concat(prefix,k)))

        var = environ.get(self.concat(prefix, k).upper(), None)
        if not var: return (k,v)
        if self.is_list(v):
            return (k, self.is_type(v)(var.split(',')))
        else:
            return (k, self.is_type(v)(var))

    @staticmethod
    def enabled(obj: Dict):
        return obj.get('__env__', True)

    @staticmethod
    def concat(*args: [str], **kwargs):
        s = kwargs.get('space', '_')
        return s.join(filter(lambda x: True if x else False, args))


class Environment(metaclass=Switch):
    __target__ = OSEnviron
