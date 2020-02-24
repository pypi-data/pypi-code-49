__all__ = []

try:
    from .middleware import DjangoUserMiddleware
    __all__.append('DjangoUserMiddleware')
except ImportError:
    # Does not install django middleware if django is missing
    pass

from .wsgi import WSGIMiddleware
__all__.append('WSGIMiddleware')

from .defines import DRHTTP_HEADER_USER, DRHTTP_HEADER_DEVICE
__all__.append(DRHTTP_HEADER_USER)
__all__.append(DRHTTP_HEADER_DEVICE)