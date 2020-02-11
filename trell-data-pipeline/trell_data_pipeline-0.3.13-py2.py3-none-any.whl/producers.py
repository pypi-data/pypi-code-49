import asyncio
import logging
import json

from aiokafka import AIOKafkaProducer

from pipeline import settings


log = logging.getLogger(__name__)


class Producer():
    def __init__(self):
        self.hosts = settings.PRODUCER_HOSTS
        self.topic = settings.PRODUCER_TOPIC
        self.producer = None
        self.connected = False
        self.loop = asyncio.get_event_loop()

    async def connect(self) -> None:
        raise NotImplemented("No driver specified")

    async def disconnect(self) -> None:
        raise NotImplemented("No driver specified")

    async def produce_message(self, message: dict, topic: str=None) -> None:
        if not topic:
            topic = settings.PRODUCER_TOPIC


class MockProducer(Producer):
    async def connect(self) -> None:
        log.debug('Connected to mock producer')
        self.connected = True

    async def disconnect(self) -> None:
        self.connected = False

    async def produce_message(self, message: dict, topic: str=None) -> None:
        log.debug('Mocking a message on topic {topic}: {message}'.format(
            topic=topic,
            message=message,
        ))


class KafkaProducer(Producer):
    async def connect(self) -> None:
        log.debug('Connecting to Kafka stream.')
        self.producer = AIOKafkaProducer(
            loop=self.loop,
            bootstrap_servers=self.hosts
        )
        await self.producer.start()
        self.connected = True

    async def disconnect(self) -> None:
        await self.producer.stop()
        self.connected = False

    async def produce_message(self, message: dict, topic: str=None) -> None:
        log.debug('Trying to produce message: {msg}'.format(msg=message))

        if not self.connected:
            log.debug('Producer not connected')
            return

        await super().produce_message(message=message, topic=topic)
        await self.producer.send_and_wait(topic, json.dumps(message).encode())


def get_producer() -> Producer:
    driver = settings.PRODUCER_DRIVER
    
    if driver == 'kafka':
        return KafkaProducer()
    else:
        return MockProducer()

