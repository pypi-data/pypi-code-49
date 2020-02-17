import json
import logging
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from time import sleep
from typing import List

from kafka import KafkaAdminClient
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.admin import NewTopic

from watermill.message_brokers.kafka_message_broker import KafkaMessageBroker
from watermill.message_brokers.message_broker import EndOfStream
from watermill.mill import WaterMill


@dataclass(frozen=True, eq=True)
class GoodsItem:
    title: str
    quantity: int
    price: int


@dataclass(frozen=True, eq=True)
class UpdatedGoodsItem:
    title: str
    quantity: int
    price: int


def update_goods_price(goods_item: GoodsItem) -> UpdatedGoodsItem:
    return UpdatedGoodsItem(
        title=goods_item.title,
        quantity=goods_item.quantity,
        price=int(goods_item.price * 1.1)
    )


def kafka_stream_example_with_result():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('kafka')
    logger.setLevel(logging.WARNING)

    message_broker = KafkaMessageBroker(
        topic_names={
            GoodsItem: 'goods',
            UpdatedGoodsItem: 'updated_goods',
        },
        kafka_url='kafka:9092'
    )

    mill = WaterMill(
        broker=message_broker,
        process_func=update_goods_price,
        stream_cls=GoodsItem,
    )

    produce_goods_stream()

    mill.run()

    print('Fetching data from resulting stream')
    result_consumer = KafkaConsumer(
        bootstrap_servers='kafka:9092',
        group_id='result-consumer',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
    )
    result_consumer.subscribe(['updated_goods'])
    for result in result_consumer:
        result_item = json.loads(result.value.decode('utf8'))
        print(json.dumps(result_item))
        if 'eos__' in result_item:
            break


def produce_goods_stream():
    recreate_topics(['goods', 'updated_goods'])
    print('Sending data to input stream')

    kafka_producer = KafkaProducer(bootstrap_servers='kafka:9092')

    goods_file_path = Path(__file__).resolve().parent / 'samples' / 'goods.json'
    with goods_file_path.open('r') as f:
        goods = json.load(f)

    for goods_item in goods:
        print(goods_item)
        kafka_producer.send('goods', value=json.dumps(goods_item).encode('utf8'))

    kafka_producer.send('goods', value=json.dumps(asdict(EndOfStream())).encode('utf8'))
    kafka_producer.flush()


def recreate_topics(topics: List[str]):
    kafka_admin_client = KafkaAdminClient(
        bootstrap_servers='kafka:9092',
    )
    try:
        kafka_admin_client.delete_topics(topics)
    except Exception as exc:
        print(exc)
    sleep(0.1)
    try:
        kafka_admin_client.create_topics([NewTopic(name=topic, num_partitions=1, replication_factor=1) for topic in topics])
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    kafka_stream_example_with_result()
