from .hub import Hub
from .helpers import expose, subscribe_commands, auto_subscribe  # noqa

__version__ = "0.1.3-alpha"

pub = Hub()


def subscribe(topic):
    def _subscribe(func):
        pub.subscribe(func, topic)
        return func
    return _subscribe
