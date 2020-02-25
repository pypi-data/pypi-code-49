import os
import logging
from .message_utils import produce_message_callback, consume_message_callback
from nubium_utils.metrics import start_pushing_metrics

LOGGER = logging.getLogger(__name__)


def init_ssl_configs():
    """
    Provides producer or consumer SSL configs.
    :return: config params
    :rtype: dict
    """
    if os.environ['USE_SSL'].lower() == 'true':
        LOGGER.info('Initializing producers and consumers with TLS configurations ENABLED.')
        return {
            "security.protocol": "ssl",
            "ssl.ca.location": os.environ["SSL_CA_LOCATION"],
            "ssl.certificate.location": os.environ["SSL_CERTIFICATE_LOCATION"],
            "ssl.key.location": os.environ["SSL_KEY_LOCATION"]}
    else:
        LOGGER.info('Initializing producers and consumers with TLS configurations DISABLED.')
    return {}


def init_schema_registry_configs():
    """
    Provides the avro schema config
    :return: dict, None
    """
    url = os.environ['SCHEMA_REGISTRY_URL']
    if url:
        LOGGER.info(f'Using the schema server at {url}')
        return {'schema.registry.url': url}
    else:
        LOGGER.info(f'No schema registry URL provided; schema registry usage DISABLED')
        return None


def init_producer_configs(ssl_configs=None, schema_registry_configs=None):
    """
    Provides producer config.
    :return: config params
    :rtype: dict
    """
    if not ssl_configs:
        ssl_configs = {}
    if not schema_registry_configs:
        schema_registry_configs = {}
    return {
        **ssl_configs,
        **schema_registry_configs,
        "bootstrap.servers": os.environ['KAFKA_CLUSTER'],
        "on_delivery": produce_message_callback,
        "acks": os.environ["KAFKA_ACK"]}


def init_consumer_configs(ssl_configs=None, schema_registry_configs=None):
    """
    Provides consumer config.
    :return: config params
    :rtype: dict
    """
    if not ssl_configs:
        ssl_configs = {}
    if not schema_registry_configs:
        schema_registry_configs = {}
    return {
        **ssl_configs,
        **schema_registry_configs,
        "bootstrap.servers": os.environ['KAFKA_CLUSTER'],
        "group.id": os.environ['APP_NAME'],
        "on_commit": consume_message_callback,
        "enable.auto.commit": "false"}


def init_metrics_pushing(metrics_manager):
    if os.environ['DO_METRICS_PUSHING'].lower() == 'true':
        LOGGER.info('Metric pushing to gateway ENABLED')
        start_pushing_metrics(metrics_manager, int(os.environ['METRICS_PUSH_RATE']))
    else:
        LOGGER.info('Metric pushing to gateway DISABLED')
