import logging
import typing
from typing import Text, Optional, Union

from ragex.community.services.event_consumers.event_consumer import EventConsumer

import ragex.community.config as rasa_x_config
from rasa.utils import endpoints

if typing.TYPE_CHECKING:
    from pika import BasicProperties
    from pika.adapters.blocking_connection import BlockingChannel
    from pika.spec import Basic

logger = logging.getLogger(__name__)


class PikaEventConsumer(EventConsumer):
    type_name = "pika"

    def __init__(
        self,
        host: Text,
        username: Text,
        password: Text,
        port: Optional[Union[Text, int]] = 5672,
        queue: Text = "rasa_production_events",
        should_run_liveness_endpoint: bool = False,
    ):
        """Pika event consumer.

        Args:
            host: RabbitMQ host.
            username: RabbitMQ username.
            password: RabbitMQ password.
            port: RabbitMQ port.
            queue: RabbitMQ queue to be consumed.
            should_run_liveness_endpoint: If `True`, runs a simple Sanic server as a
                background process that can be used to probe liveness of this service.
                The service will be exposed at a port defined by the
                `SELF_PORT` environment variable (5673 by default).

        """
        from rasa.core.brokers import pika

        self.queue = queue
        self.host = host
        self.channel = pika.initialise_pika_channel(
            host, queue, username, password, port
        )
        super().__init__(should_run_liveness_endpoint)

    @classmethod
    def from_endpoint_config(
        cls,
        consumer_config: Optional[endpoints.EndpointConfig],
        should_run_liveness_endpoint: bool,
    ) -> Optional["PikaEventConsumer"]:
        if consumer_config is None:
            logger.debug(
                "Could not initialise `PikaEventConsumer` from endpoint config."
            )
            return None

        return cls(
            consumer_config.url,
            **consumer_config.kwargs,
            should_run_liveness_endpoint=should_run_liveness_endpoint,
        )

    @staticmethod
    def origin_from_message_property(pika_properties: "BasicProperties") -> Text:
        """Fetch message origin from the `app_id` attribute of the message
        properties.

        Args:
            pika_properties: Pika message properties.

        Returns:
            The message property's `app_id` property if set, otherwise
            `ragex.community.constants.DEFAULT_RASA_ENVIRONMENT`.

        """

        from ragex.community.constants import DEFAULT_RASA_ENVIRONMENT

        return pika_properties.app_id or DEFAULT_RASA_ENVIRONMENT

    # noinspection PyUnusedLocal
    def _callback(
        self,
        ch: "BlockingChannel",
        method: "Basic.Deliver",
        properties: "BasicProperties",
        body: bytes,
    ):
        self.log_event(body, origin=self.origin_from_message_property(properties))

    def consume(self):
        logger.info(f"Start consuming queue '{self.queue}' on pika host '{self.host}'.")
        self.channel.basic_consume(self.queue, self._callback, auto_ack=True)
        self.channel.start_consuming()
