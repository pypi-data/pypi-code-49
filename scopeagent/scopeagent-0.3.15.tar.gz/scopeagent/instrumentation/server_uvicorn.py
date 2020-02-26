import logging

import wrapt

from .wrappers.asgi import ASGIMiddleware
from . import run_once

logger = logging.getLogger(__name__)


@run_once
def patch(tracer):
    def wrapper(wrapped, instance, args, kwargs):
        resp = wrapped(*args, **kwargs)
        instance.loaded_app = ASGIMiddleware(instance.loaded_app, tracer)
        return resp

    try:
        logger.debug("patching module=uvicorn.config name=Config.load")
        wrapt.wrap_function_wrapper('uvicorn.config', 'Config.load', wrapper)
    except ImportError:
        logger.debug("module not found module=uvicorn.config")
