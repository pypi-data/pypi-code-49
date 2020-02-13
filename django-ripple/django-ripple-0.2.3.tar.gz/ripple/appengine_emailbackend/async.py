
from django.core.exceptions import ImproperlyConfigured

try:
    import default
except ImportError as err:
    raise ImproperlyConfigured(('Failed to import App Engine libraries: %s'
                                % err))


class EmailBackend(default.EmailBackend):
    can_defer = True