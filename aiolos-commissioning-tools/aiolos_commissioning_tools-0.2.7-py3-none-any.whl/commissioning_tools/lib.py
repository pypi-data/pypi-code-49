import inspect


def get_defaults(func):
    args, varargs, keywords, defaults = inspect.getargspec(func)
    return dict(zip(args[-len(defaults):], defaults))

