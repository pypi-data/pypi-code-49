import logging
from nubium_utils import parse_headers
from nubium_utils.metrics import MetricsManager
from nubium_utils.custom_exceptions import ProduceHeadersException
from os import environ

LOGGER = logging.getLogger(__name__)


def produce_message(producer, producer_kwargs: dict, metrics_manager: MetricsManager,
                    consumed_msg_headers_passthrough: tuple = ()):
    """
    Helper for producing a message with confluent_kafka producers; primarily handles headers passthrough and enforcing
    all required headers fields exist before producing.
    You can pass in the previous message headers via 'consumed_msg_headers_passthrough', which extracts the headers.
    Then, if you wish to overwrite any of them, you can provide your own "headers" keyword in 'producer_kwargs'
    which will take that dict and overwrite any matching key in the 'consumed_msg_headers_passthrough' argument.
    You can also provide a None value for a key to remove it entirely.
    :param producer: A confluent_kafka producer
    :type: confluent_kafka.Producer or confluent_kafka.avro.AvroProducer
    :param producer_kwargs: the kwargs to pass into the producer instance
    :type producer_kwargs: dict
    :param metrics_manager: a MetricsManager object instance
    :type metrics_manager: MetricsManager
    :param consumed_msg_headers_passthrough: confluent_kafka Message.headers() from a consumed msg; will add all to new message
    :type consumed_msg_headers_passthrough: tuple
    """
    required_fields = ['guid', 'last_updated_by']

    if 'header' in producer_kwargs:
        raise KeyError('"header" is not the appropriate key for producing message headers; use "headers" instead')

    headers_out = parse_headers(consumed_msg_headers_passthrough)
    headers_out.update(producer_kwargs.get('headers', {}))
    headers_out = {key: value for key, value in headers_out.items() if value is not None}
    missing_required_keys = [key for key in required_fields if key not in headers_out]
    if missing_required_keys:
        raise ProduceHeadersException(f'Message headers are missing the required key(s): {missing_required_keys}')
    producer_kwargs['headers'] = headers_out

    LOGGER.debug(f'Producing a message to topic {producer_kwargs["topic"]}')
    producer.produce(**producer_kwargs)
    metrics_manager.inc_messages_produced(1)
    LOGGER.info(f'Produced a message with GUID {headers_out.get("guid")}')


def produce_retry_message(message, producer, error):
    """
    Produces a message to the correct retry topic with an updated header

    The message header should contain a `kafka_retry_count` field,
    which is an integer representation of how many times the message has
    been tried for the current topic.
    If greater than the allowed maximum, produces to the retry topic.
    If less than the allowed maximum, produces to the current topic.
    """

    message_headers = dict(message.headers())
    kafka_retry_count = int(message_headers.get('kafka_retry_count', '0'))

    # If less than the retry max, produce onto the original topic
    if kafka_retry_count < int(environ['RETRY_COUNT_MAX']):
        message_headers['kafka_retry_count'] = str(kafka_retry_count + 1)
        producer.produce(
            topic=environ['CONSUME_TOPICS'],
            value=message.value(),
            key=message.key(),
            headers=message_headers
        )

    # Otherwise, reset the retry count and produce to the retry topic
    else:
        message_headers['kafka_retry_count'] = '0'
        producer.produce(
            topic=environ['PRODUCE_RETRY_TOPICS'],
            value=message.value(),
            key=message.key(),
            headers=message_headers)


def produce_failure_message(message, producer, exception=None, headers=None):
    """
    Produces a message onto a deadletter queue
    """
    if not headers:
        headers = {}
    if exception:
        LOGGER.error(exception)
        headers.update({"exception": {"name": type(exception).__name__, "description": str(exception)}})
    LOGGER.info('Producing message to deadletter/failure topic')
    producer.produce(
        topic=environ['PRODUCE_FAILURE_TOPICS'],
        value=message.value(),
        key=message.key(),
        headers=headers)
    LOGGER.info('Produced message to deadletter/failure topic')
