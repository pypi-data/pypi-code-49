import weakref
from inspect import getfullargspec, ismethod, isfunction


class PubSubError(Exception):
    pass


def callable_class(obj):
    # all classes have an implicity __call__ function!!!!
    # fer fuck's sake
    call_func = getattr(obj, "__call__", None)
    # we need to call bound on the obj to eliminate functions
    # we also need to eliminate functions as they can
    # have __call__ attributes
    return (
        call_func is not None
        and not isinstance(obj, type)
        and not isfunction(obj)
        and not bound(obj)
        and bound(call_func)
    )


def bound(obj):
    _self = getattr(obj, "__self__", None)
    return _self is not None


def has_self_arg(obj):
    # classes with __init__ methods have self
    if isinstance(obj, type):
        # this is a class - which is what we don't want
        return False
    # instances of classes will cause this to error
    try:
        return "self" in getfullargspec(obj).args
    except TypeError:  # noqa
        return False


def requires_weakref(obj):
    return (bound(obj) and has_self_arg(obj)) or callable_class(obj)


def acceptable(obj):
    # must be callable
    if not callable(obj):
        return False
    # must not be a class
    if isinstance(obj, type):
        return False

    if ismethod(obj):
        return True

    if callable_class(obj):
        return True

    if not bound(obj) and has_self_arg(obj):
        return False

    return True


def apply_ref(obj):

    if ismethod(obj):
        return weakref.WeakMethod(obj)

    return weakref.ref(obj)
