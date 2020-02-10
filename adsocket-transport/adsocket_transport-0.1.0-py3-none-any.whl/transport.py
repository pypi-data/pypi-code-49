from .broker import BaseBroker
from .exceptions import ADSocketException
from .message import Message
from . utils import import_driver
from typing import Union

__all__ = [
    'ADSocketTransport',
    'ADSocketAsyncTransport'
]


class ADSocketTransport:
    """

    """
    _broker = None
    """
    :var broker.BaseBroker: Broker instance
    """

    def __init__(self, driver, **driver_options):
        self._initialize_broker(driver, driver_options)

    def _initialize_broker(self, driver, driver_options):
        try:
            driver_class = import_driver(driver)
        except (ImportError, AttributeError) as e:
            raise ADSocketException("Could not import broker driver "
                                    "in broker folder")

        if not issubclass(driver_class, BaseBroker):
            raise ADSocketException("Broker class must be subclass of "
                                    "adsocket_transport.broker.BaseBroker")

        driver_options = driver_options or {}
        broker = driver_class(**driver_options)
        self._broker = broker

    def _validate_channel(self, channel: Union[str, list, tuple, dict]):
        if isinstance(channel, (list, tuple, dict)):
            if len(channel) != 2:
                raise ADSocketException(
                    f"Unknown channel data {channel}. "
                    f"I except list or tuple in format "
                    f"[channel_name, channel_id] "
                    f"or dict {'name': name, 'id': id}")

    def send_data(self, data: dict, channels: Union[str, list, tuple, dict],
                  message_type: str = 'publish') -> None:
        """

        :param data: Data to be send to WebSocket broker
        :type data: str, dict, list
        :param channels: To which channel(s) should be message published to
        :type channels: str, list, tuple
        :param message_type: which command should be executed to
                            WebSocket part. Default is `publish`
        :type message_type: str
        :return: void
        :rtype: void
        """
        if not isinstance(channels, (list, tuple)):
            channels = [channels]

        for channel in channels:
            self._validate_channel(channel)
            self.send(Message(
                type=message_type,
                data=data,
                channel=channel['name'],
                channel_id=channel['id']
                )
            )

    def send(self, message: Message) -> None:
        """
        Publish message to broker

        :param message: Message instance to be send
        :type message: Message
        :return: void
        :rtype: void
        """
        if not isinstance(message, Message):
            raise ADSocketException(
                "Message must be adsocket_`transport.Message` instance. "
                "If you want to send raw data use `send_data` method")

        self._broker.publish(message)

    def store_credentials(self, key: str, data: dict, ttl: int = None) -> None:
        """
        Store credentials or any other data ia broker

        :param key: Key of stored data
        :type key: str
        :param data: data itself
        :type data: dict
        :param ttl: for how long data should be visible in WebSocket
        :type ttl: int
        :return: void
        :rtype: None
        """
        self._broker.store_credentials(key, data, ttl)


class ADSocketAsyncTransport(ADSocketTransport):

    async def send_data(self, data: dict,
                        channels: Union[str, list, tuple, dict],
                        message_type: str = 'publish') -> None:
        """
        :param data: Data to be send to WebSocket broker
        :type data: str, dict, list
        :param channels: To which channel(s) should be message published to
        :type channels: str, list, tuple
        :param message_type: which command should be executed to
                            WebSocket part. Default is `publish`
        :type message_type: str
        :return: void
        :rtype: void
        """
        if not isinstance(channels, (list, tuple)):
            channels = [channels]

        for channel in channels:
            self._validate_channel(channel)
            await self.send(Message(
                type=message_type,
                data=data,
                channel=channel['name'],
                channel_id=channel['id']
                )
            )

    async def store_credentials(self, key: str, data: dict, ttl: int = None) -> None:
        """
        Store credentials or any other data ia broker

        :param key: Key of stored data
        :type key: str
        :param data: data itself
        :type data: dict
        :param ttl: for how long data should be visible in WebSocket
        :type ttl: int
        :return: void
        :rtype: Nont
        """
        await self._broker.store_credentials(key, data, ttl)

    async def send(self, message: Message) -> None:
        """
        Publish message to broker

        :param message: Message instance to be send
        :type message: Message
        :return: void
        :rtype: void
        """
        if not isinstance(message, Message):
            raise ADSocketException(
                "Message must be adsocket_`transport.Message` instance. "
                "If you want to send raw data use `send_data` method")

        await self._broker.publish(message)
