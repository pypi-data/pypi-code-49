import asyncio
import atexit
import logging
from typing import Optional

import msgpack
import uuid
import time
from kafka import KafkaConsumer, KafkaProducer

from .errors import KafkaTransportError

logger = logging.getLogger('kafka_transport')

kafka_host = None
producer = None
sleep_timeout = 0.01
consumers = []


def encode_key(key) -> Optional[bytes]:
    if key is None:
        return None

    if type(key) is int:
        key = str(key)

    return key.encode('utf8')


def decode_key(key) -> Optional[str]:
    if key is None:
        return None

    if type(key) is int:
        return key

    return key.decode('utf8')


async def init(host, timeout=0.01):
    global kafka_host
    global producer
    global sleep_timeout

    kafka_host = host
    sleep_timeout = timeout

    if producer is not None:
        await finalize()

    producer = KafkaProducer(
        bootstrap_servers=[host], value_serializer=msgpack.dumps)

    # while not producer.bootstrap_connected():
    #    await asyncio.sleep(0.01)


async def finalize():
    if producer:
        producer.close()
    for consumer in consumers:
        consumer.close()


def close():
    if producer is not None:
        try:
            loop = asyncio.get_event_loop()
            if loop.is_closed():
                logger.warning('Event loop already closed')
            else:
                loop.run_until_complete(finalize())
        except Exception as e:
            logger.exception(str(e))


atexit.register(close)


async def subscribe(topic, callback, consumer_options=None):
    consumer = await init_consumer(topic, consumer_options)
    await consume_messages(consumer, callback)


async def init_consumer(topic, consumer_options=None):
    consumer = KafkaConsumer(topic, bootstrap_servers=[
                             kafka_host])

    # while not consumer.bootstrap_connected():
    #    await asyncio.sleep(0.01)

    consumers.append(consumer)

    return consumer


async def consume_messages(consumer, callback):

    while True:
        await asyncio.sleep(sleep_timeout)
        partitions = consumer.poll()

        for records in partitions.values():
            for record in records:
                try:
                    value = msgpack.unpackb(record.value, raw=False, strict_map_key=False)
                except Exception as e:
                    print(str(e))
                    logger.warning("Not binary data: %s", str(record.value))
                    continue

                try:
                    result = callback(
                        {"key": decode_key(record.key), "value": value})

                    if asyncio.iscoroutine(result):
                        asyncio.ensure_future(result)
                except:
                    logger.warning(
                        "Error during calling handler with data: %s", str(value))


async def push(topic, value, key=None):
    producer.send(topic, value, key=encode_key(key)).get()


async def fetch(to, _from, value, timeout_ms=600 * 1000):
    id = str(uuid.uuid4())

    consumer = KafkaConsumer(_from, bootstrap_servers=[
                             kafka_host])

    # await consumer.start()
    await asyncio.sleep(0.5)

    await push(to, value, id)

    try:
        end_time = time.time() + timeout_ms / 1000

        while time.time() <= end_time:
            await asyncio.sleep(sleep_timeout)
            result = consumer.poll()
            for records in result.values():
                for msg in records:
                    key = decode_key(msg.key)
                    if key == id:
                        consumer.close()
                        return msgpack.unpackb(msg.value, raw=False, strict_map_key=False)
    finally:
        consumer.close()

    raise KafkaTransportError("Fetch timeout")
