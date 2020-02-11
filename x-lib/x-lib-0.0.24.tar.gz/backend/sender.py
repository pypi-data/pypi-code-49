from kafka import KafkaProducer
from backend.encoder import JsonEncoder
import json
import os


def send_message(topic, input_dict, partition=0):
    producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA_SERVER'),
                             value_serializer=lambda v: json.dumps(v, cls=JsonEncoder).encode('utf-8'))
    if partition > 0:
        future = producer.send(topic, input_dict, partition=partition)
    else:
        future = producer.send(topic, input_dict)
    future.get(timeout=int(os.getenv('KAFKA_TIME_OUT')))
