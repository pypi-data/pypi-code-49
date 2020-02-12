import os
import traceback
from typing import Callable, Any, Optional
from .event import Event

from zappa.async import run as zappa_run


def log_exception(name: str, description: str, trb: Optional[str] = None, function_name: Optional[str] = '') -> bool:
    """
    :param name: str
    :param description: str
    :param trb: any
    :param function_name: any
    :return: bool
    """
    init_kwargs = {
        "system_name": os.environ.get("SYSTEM_EVENT_NAME", ""),
        "system_url": os.environ.get("SYSTEM_EVENT_URL", ""),
        "execute_token": os.environ.get("SYSTEM_EVENT_TOKEN", ""),
        "em_notifier": os.environ.get("SYSTEM_EM_NOTIFIER", False),
        "debug": os.environ.get("SYSTEM_EM_NOTIFIER", False),
    }
    event = Event(**init_kwargs)
    if not trb:
        trb = str(traceback.format_exc()).replace('func_result = function', function_name)
    return event.log_exception(name, description, trb=trb)


def run(function: Callable[..., Any], **kwargs) -> any:
    """
    function must be a top level function, not class method, and not decorated function
    """
    if "kwargs" in kwargs:
        kwargs = kwargs["kwargs"]
    if not os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
        return function(**kwargs)
    zappa_run(function, kwargs=kwargs)
    return True
