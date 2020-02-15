import pika
import json
from loguru import logger


class Messager:
    def __init__(self, server_url, queue_name):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(server_url, heartbeat=0)
        )
        self.queue_name = queue_name
        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def validate(self, message):
        obj = json.loads(message)
        if 'x' not in obj:
            logger.error('object x is not included in the message!')
            return False
        if 'sensorId' not in obj['x']:
            logger.error('sensorId is not included in the messsage')
            return False
        if 'metaType' not in obj['x']:
            logger.error('metaType is not included in the message')
            return False
        if 'dataType' not in obj['x']:
            logger.error('dataType is not included in the message')
            return False
        if 'description' not in obj['x']:
            logger.error('description is not included in the message')
            return False
        if 'data' not in obj['x']:
            logger.error('data is not included in the message')
            return False
        if 'y' not in obj:
            logger.error('object y is not included in the message')
            return False
        if 'true' not in obj['y']:
            logger.error('list of true is not included in the message')
            return False
        if 'pred' not in obj['y']:
            logger.error('list of pred is not included in the message')
            return False

        return True

    def publish_to_sibling_queue(self, message, unique_id, validate=True):
        queue = f"{self.queue_name}-{unique_id}"
        if validate:
            if self.validate(message):
                logger.info(f"Publishing with validation to queue {queue}")
                self.channel.basic_publish(exchange='',
                                           routing_key=queue,
                                           body=message)
            else:
                raise Exception("Message does not follow the schema!")
        else:
            logger.info(f"Publishing WITHOUT validation to queue {queue}")
                
            self.channel.basic_publish(exchange='',
                                       routing_key=queue,
                                       body=message)

    def publish(self, message, exchange='', validate=True):
        if validate:
            if self.validate(message):
                self.channel.basic_publish(exchange=exchange,
                                           routing_key=self.queue_name,
                                           body=message)
            else:
                raise Exception("Message does not follow the schema!")
        else:
            self.channel.basic_publish(exchange=exchange,
                                       routing_key=self.queue_name,
                                       body=message)

    def get_message(self):
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return body
        else:
            return False

    def consume(self, callback):
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=callback,
                                   auto_ack=False)
        self.channel.start_consuming()
