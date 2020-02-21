import logging
import typing
from typing import Optional

from rasa.utils import endpoints

if typing.TYPE_CHECKING:
    from rasax.community.services.event_service import EventConsumer

logger = logging.getLogger(__name__)


def from_endpoint_config(
    broker_config: Optional[endpoints.EndpointConfig],
    should_run_liveness_endpoint: bool,
) -> "EventConsumer":
    """Instantiate an event consumer based on an endpoint config.

    Args:
        broker_config: Event consumer endpoint config.
        should_run_liveness_endpoint: If `True`, runs a simple Sanic server as a
            background process that can be used to probe liveness of this service.
            The service will be exposed at a port defined by the
            `SELF_PORT` environment variable (5673 by default).

    Returns:
        `KafkaEventConsumer` or `PikaEventConsumer` if valid endpoint config.
        was provided. `SQLiteEventConsumer` if no config was provided.
        `None` if an unknown type was requested.

    """

    if broker_config is None:
        from rasax.community.services.event_consumers.sqlite_consumer import (
            SQLiteEventConsumer,
        )

        return SQLiteEventConsumer(should_run_liveness_endpoint)
    elif broker_config.type.lower() == "pika" or broker_config.type is None:
        from rasax.community.services.event_consumers.pika_consumer import (
            PikaEventConsumer,
        )

        logging.getLogger("pika").setLevel(logging.WARNING)
        return PikaEventConsumer.from_endpoint_config(
            broker_config, should_run_liveness_endpoint
        )
    elif broker_config.type.lower() == "kafka":
        from rasax.community.services.event_consumers.kafka_consumer import (
            KafkaEventConsumer,
        )

        return KafkaEventConsumer.from_endpoint_config(
            broker_config, should_run_liveness_endpoint
        )

    raise ValueError(
        f"Found event broker `EndpointConfig` of type "
        f"'{broker_config.type}', which is not supported."
    )
