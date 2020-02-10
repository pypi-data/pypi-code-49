
from posthoganalytics.version import VERSION
from posthoganalytics.client import Client
from typing import Optional, Dict, Callable

__version__ = VERSION

"""Settings."""
write_key: str = None
host: str = None
on_error: Callable = None
debug: bool = False
send: bool = True
sync_mode:bool = False

default_client = None


def capture(distinct_id: str, event: str, properties: Optional[Dict]=None, context: Optional[Dict]=None,
              timestamp: Optional[str]=None, message_id: Optional[str]=None) -> None:
    """Send a capture call."""
    _proxy('capture', distinct_id=distinct_id, event=event, properties=properties, context=context, timestamp=timestamp, message_id=message_id)

def identify(distinct_id: str, properties: Optional[Dict]=None, context: Optional[Dict]=None, timestamp: Optional[str]=None,
                message_id=None) -> None:
    """Send a identify call."""
    _proxy('identify', distinct_id=distinct_id, properties=properties, context=context, timestamp=timestamp, message_id=message_id)

def group(*args, **kwargs):
    """Send a group call."""
    _proxy('group', *args, **kwargs)


def alias(previous_id: str, distinct_id: str, context: Optional[Dict]=None, timestamp: Optional[str]=None, message_id: Optional[str]=None) -> None:
    """Send a alias call."""
    _proxy('alias', previous_id=previous_id, distinct_id=distinct_id, context=context, timestamp=timestamp, message_id=message_id)


def page(*args, **kwargs):
    """Send a page call."""
    _proxy('page', *args, **kwargs)


def screen(*args, **kwargs):
    """Send a screen call."""
    _proxy('screen', *args, **kwargs)


def flush():
    """Tell the client to flush."""
    _proxy('flush')


def join():
    """Block program until the client clears the queue"""
    _proxy('join')


def shutdown():
    """Flush all messages and cleanly shutdown the client"""
    _proxy('flush')
    _proxy('join')


def _proxy(method, *args, **kwargs):
    """Create an analytics client if one doesn't exist and send to it."""
    global default_client
    if not default_client:
        default_client = Client(write_key, host=host, debug=debug,
                                on_error=on_error, send=send,
                                sync_mode=sync_mode)

    fn = getattr(default_client, method)
    fn(*args, **kwargs)
