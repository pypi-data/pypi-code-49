from container_hub import settings

import importlib

__all__ = ["container_terminal"]


def __getattr__(name):
    if name in __all__:
        carrier = settings.CONTAINER_CARRIER.lower()
        mod = f".{carrier}.{name}"
        return importlib.import_module(mod, __name__)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
