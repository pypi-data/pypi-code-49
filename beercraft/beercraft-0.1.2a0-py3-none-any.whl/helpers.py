import re
import logging
import warnings
from inspect import getmembers
from functools import wraps
from .types import PubSubError
from .hub import Hub


log = logging.getLogger("beercraft")


INTERP_RX = re.compile(r"\{\d?\}")


def topic_formatter(topic_string):

    requires_sub = len(INTERP_RX.findall(topic_string)) > 0

    def _topic_formatter(substitution=None):
        if requires_sub:
            if not substitution:
                err_msg = "Topic `{0}` must be supplied a frame id!"
                raise PubSubError(err_msg.format(topic_string))
            return topic_string.format(substitution)
        return topic_string

    return _topic_formatter


def expose(topic, logger=None):

    if not isinstance(topic, str):
        raise PubSubError("A beercraft topic must be string!")

    topic = topic_formatter(topic)

    if logger:
        _log = logger
    else:
        _log = log

    if not hasattr(_log, "debug"):
        raise PubSubError("logger must have a `debug` method.")

    def expose_decorator(func):
        """Wraps the base method
        """

        @wraps(func)
        def wrapper_(*args, **kwargs):
            _log.debug(str(func))
            return func(*args, **kwargs)

        wrapper_.topic = topic
        wrapper_.pubsub = True
        return wrapper_

    return expose_decorator


def subscribe_commands(obj):
    """Scan objects for methods that have been decorated with the
    ExposeCommand and subscribe them to pubsub.

    """
    pubsubhub = Hub()
    pub_id = getattr(obj, "__pub_id__", "")

    if getattr(obj, "__auto_subscribed__", False) is True:
        klass = type(obj).__name__
        msg = (
            "Class {} is decorated with the beercraft.auto_subcribe "
            "function. Calling `subscribe_commands` is redundant."
        )
        warnings.warn(msg.format(klass), category=RuntimeWarning)
        return

    def is_exposed(obj):
        return hasattr(obj, "pubsub") and getattr(obj, "pubsub") is True

    exposed_mems = [name for name, inst in getmembers(obj) if is_exposed(inst)]
    exposed_mems.sort()
    log.debug("beercraft.subscrib_commands({})".format(obj))
    log.debug("   object id: {}".format(pub_id))
    for mem_name in exposed_mems:
        log.debug(f"   subscribing member `{mem_name}` of {mem_name}")
        inst = getattr(obj, mem_name)
        topic = inst.topic(pub_id)
        pubsubhub.subscribe(inst, topic)


def auto_subscribe(type_name=None):
    def _auto_subscribe(klass):
        """Class decorator that automates the subscription
        of new instances of a class.
        """
        if not isinstance(klass, type):
            raise PubSubError(
                "The `auto_subscribe` class decorator "
                "can only be applied to a type. "
                "Received `{}`".format(klass)
            )
        pub = Hub()
        org_init = klass.__init__

        def __init__(self, *args, **kwargs):

            if not hasattr(self, "__pub_id__") and type_name:
                self.__pub_id__ = pub.oid.last(type_name)

            org_init(self, *args, **kwargs)

            subscribe_commands(self)

            self.__auto_subscribed__ = True

        klass.__auto_subscribed__ = False

        klass.__init__ = __init__
        return klass

    return _auto_subscribe
