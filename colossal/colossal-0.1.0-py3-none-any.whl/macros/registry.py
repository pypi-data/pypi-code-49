_registry = {}


def register(macro_name):
    def decorator(func):
        _registry[macro_name] = func
        return func
    return decorator


def get_macro(macro_name):
    return _registry[macro_name]
