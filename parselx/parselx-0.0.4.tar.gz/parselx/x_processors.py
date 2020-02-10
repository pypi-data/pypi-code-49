from .x_filters import filters as default_filters


class x:
    """ x are used to spawn field processing functions.
    """

    filters = default_filters

    @classmethod
    def register(cls, name=None):
        def decorator(target):
            key = name or target.__name__
            cls.filters[key] = target
            return target

        return decorator

    @classmethod
    def use(cls, func_dict):
        cls.filters.update(func_dict)

    @staticmethod
    def map(func):
        def _f(values):
            return [func(v) for v in values]

        return _f

    @staticmethod
    def filter(func=bool):
        def _f(values):
            return [v for v in values if func(v)]

        return _f

    @staticmethod
    def default(default, fn=bool):
        def _f(value):
            if bool(value):
                return value
            else:
                return default

        return _f
