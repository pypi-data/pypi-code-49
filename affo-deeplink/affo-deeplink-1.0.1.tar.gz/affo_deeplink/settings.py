import sys  # noqa

from dynaconf import LazySettings

settings = LazySettings(ENVVAR_PREFIX_FOR_DYNACONF="AFFO_DL", ENVVAR_FOR_DYNACONF="AFFO_DL_SETTINGS")

# DEEPLINK SECRET CONFIGURATION
DEEPLINK_SECRET_KEY = getattr(settings, "DEEPLINK_SECRET_KEY", "")

settings.populate_obj(sys.modules[__name__])
