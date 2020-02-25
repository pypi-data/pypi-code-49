from functools import wraps
from .boa_obj import to_boa

json = None
yaml = None


def make_json_load(json_loads):
    def load(stream, **kw):
        """
            ``stream`` is ``string`` or have ``.read()`` like an ``fp``
            :return: the corresponding Python object
        """
        if hasattr(stream, 'read'):
            stream = stream.read()
        return to_boa(json_loads(stream, **kw))
    return load


def yaml_decorate_boa(fun, Loader):
    @wraps(fun)
    def dec(stream):
        return to_boa(fun(stream, Loader=Loader))
    return dec


try:
    import json
    json.load = make_json_load(json.loads)
    json.loads = json.load
except ImportError:
    pass

try:
    import yaml
    load = yaml.load
    load_all = yaml.load_all

    yaml.load = yaml_decorate_boa(load, Loader=yaml.SafeLoader)  # make safe_load the default
    yaml.load_all = yaml_decorate_boa(load_all, Loader=yaml.SafeLoader)  # make safe_load the default

    yaml.safe_load = yaml_decorate_boa(load, Loader=yaml.SafeLoader)
    yaml.unsafe_load = yaml_decorate_boa(load, Loader=yaml.UnsafeLoader)
    yaml.full_load = yaml_decorate_boa(load, Loader=yaml.FullLoader)
except ImportError:
    pass
