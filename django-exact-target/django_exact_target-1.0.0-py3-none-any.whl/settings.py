from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .constants import DEFAULT_IGNORED_CODES


def overridable(name, default=None, required=False):
    if required:
        if not hasattr(settings, name) or not getattr(settings, name):
            raise ImproperlyConfigured("%s must be defined in Django settings" % name)
    return getattr(settings, name, default)


EXACT_TARGET_CLIENT_ID = overridable('EXACT_TARGET_CLIENT_ID', required=True)
EXACT_TARGET_CLIENT_SECRET = overridable('EXACT_TARGET_CLIENT_SECRET', required=True)
ET_IGNORED_ERROR_CODES = overridable('ET_IGNORED_ERROR_CODES', required=False, default=DEFAULT_IGNORED_CODES)
