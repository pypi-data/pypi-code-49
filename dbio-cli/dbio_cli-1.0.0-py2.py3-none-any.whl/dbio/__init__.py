from .config import DataBiosphereConfig, get_config, logger
from . import dss, auth


def clear_dbio_cache(args):
    """Clear the cached DataBiosphere API definitions. This can help resolve errors communicating with the API."""
    from dbio.util import SwaggerClient
    for swagger_client in SwaggerClient.__subclasses__():
        swagger_client().clear_cache()
