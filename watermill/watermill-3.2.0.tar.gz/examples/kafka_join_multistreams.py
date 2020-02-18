import json
import math
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from time import sleep
from typing import List
from typing import Mapping

from kafka import KafkaAdminClient
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.admin import NewTopic

from watermill.expressions import get_field
from watermill.message_brokers.kafka_message_broker import KafkaMessageBroker
from watermill.message_brokers.message_broker import EndOfStream
from watermill.mill import WaterMill
from watermill.stream_join import JoinWith
from watermill.stream_join import join_streams


@dataclass(frozen=True, eq=True)
class RobotLocation:
    time: int
    x: int
    y: int


@dataclass(frozen=True, eq=True)
class RobotLocationNextStep:
    time: int
    x: int
    y: int


@dataclass(frozen=True, eq=True)
class RobotSpeed:
    time_from: int
    time_to: int
    speed: float


@dataclass(frozen=True, eq=True)
class RobotSpeedError:
    time_from: int
    time_to: int
    speed_error_percent: float


def check_robot_speed(
        prev_location: RobotLocation,
        next_locations: Mapping[RobotLocation, List[RobotLocationNextStep]],
        calculated_speeds: Mapping[RobotLocation, List[RobotSpeed]]
) -> RobotSpeedError:
    next_location = next_locations[prev_location][0]
    calculated_speed = calculated_speeds[prev_location][0]
    actual_speed = math.sqrt(math.pow(next_location.x - prev_location.x, 2) + math.pow(next_location.y - prev_location.y, 2))

    return RobotSpeedError(
        time_from=prev_location.time,
        time_to=next_location.time,
        speed_error_percent=abs(calculated_speed.speed - actual_speed) / actual_speed * 100
    )


def kafka_join_multistreams():
    message_broker = KafkaMessageBroker(
        topic_names={
            RobotLocation: 'robot-locations',
            RobotLocationNextStep: 'robot-locations',
            RobotSpeed: 'robot-speed',
            RobotSpeedError: 'robot-speed-error',
        },
        kafka_url='kafka:9092',
        data_timeout=1000
    )

    mill = WaterMill(
        broker=message_broker,
        process_func=check_robot_speed,
        join_tree=join_streams(
            RobotLocation,
            JoinWith(
                with_type=RobotLocationNextStep,
                left_expression=get_field('time') + 10,
                right_expression=get_field('time')
            ),
            JoinWith(
                with_type=RobotSpeed,
                left_expression=get_field('time'),
                right_expression=get_field('time_from')
            ),
        ),
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
    result_consumer.subscribe(['robot-speed-error'])
    for result in result_consumer:
        result_item = json.loads(result.value.decode('utf8'))
        print(json.dumps(result_item))
        if 'eos__' in result_item:
            break


def produce_goods_stream():
    recreate_topics(['robot-locations', 'robot-speed', 'robot-speed-error'])
    print('Sending data to input stream')

    kafka_producer = KafkaProducer(bootstrap_servers='kafka:9092')

    locations_file_path = Path(__file__).resolve().parent / 'samples' / 'robot-locations.json'
    with locations_file_path.open('r') as f:
        locations = json.load(f)

    for location_item in locations:
        print(location_item)
        kafka_producer.send('robot-locations', value=json.dumps(location_item).encode('utf8'))

    kafka_producer.send('robot-locations', value=json.dumps(asdict(EndOfStream())).encode('utf8'))
    kafka_producer.flush()

    speed_file_path = Path(__file__).resolve().parent / 'samples' / 'robot-speed.json'
    with speed_file_path.open('r') as f:
        speed_items = json.load(f)

    for speed in speed_items:
        print(speed)
        kafka_producer.send('robot-speed', value=json.dumps(speed).encode('utf8'))

    kafka_producer.send('robot-speed', value=json.dumps(asdict(EndOfStream())).encode('utf8'))
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
    kafka_join_multistreams()
