#!/usr/bin/env python3

from functools import wraps
import datetime as dt
import inspect
import json
import uuid

from dcyd.utils.async_logger import async_logger
from dcyd.utils.async_publisher import async_publisher
import dcyd.utils.constants as constants
from dcyd.utils.utils import (
    get_project_id,
    get_account_data,
    get_mpm_client_data,
    make_json_serializable
)

logger = async_logger()
publisher = async_publisher()

def mpm(func=None, **custom_kwargs): # decorator factory
    def decorator(func):
        """Decorator that logs function inputs and outputs
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            payload = format_payload(func, args, kwargs, custom_kwargs)

            # Log the request.
            logger.info('mpm-request', payload)

            # Call the actual function.
            response = func(*args, **kwargs)

            # Log the response.
            payload = add_response(payload, response)
            logger.info('mpm-response', payload)
            publish_payload(payload)

            return response

        return wrapper

    if func:
        return decorator(func)

    return decorator


def add_response(payload, response):
    payload['request'].update({
        'request_response': make_json_serializable(response),
        'request_response_timestamp': dt.datetime.utcnow().isoformat()
    })

    return payload


def publish_payload(payload):
    publisher.publish(
        publisher.topic_path(get_project_id(), constants.MPM_PUBSUB_TOPIC),
        data=json.dumps(payload).encode('utf-8')
    )


def format_payload(func, func_args, func_kwargs, custom_kwargs):
    """
    """
    # bind arguments
    ba = inspect.signature(func).bind(*func_args, **func_kwargs)
    ba.apply_defaults()

    """If func is a method, its first argument is the class it belongs to, which
    needs to be excised since it isn't json serializable.

    We infer that func is a method if func's name is an attribute of the first
    argument. This is compelling but not airtight."""

    if ba.arguments and hasattr(list(ba.arguments.values())[0], func.__name__):
        ba.arguments.popitem(last=False)
        function_type = 'method'
    else:
        function_type = 'function'

    payload = {
        'function': {
            'function_name': func.__name__,
            'function_qualname': func.__qualname__,
            'function_module': func.__module__,
            'function_sourcefile': inspect.getsourcefile(func),
            'function_type': function_type
        },
        'request': {
            'request_id': str(uuid.uuid4()),
            'request_timestamp': dt.datetime.utcnow().isoformat(),
            'request_arguments': make_json_serializable(ba.arguments),
            'request_parameters': {
                k: str(v.kind) for k, v in ba.signature.parameters.items()
            }
        },
        'account': get_account_data(),
        'mpm_client': get_mpm_client_data(),
        'custom_data': make_json_serializable(custom_kwargs)
    }

    return payload
