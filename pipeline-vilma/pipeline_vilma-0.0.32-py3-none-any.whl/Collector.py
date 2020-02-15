import json
import datetime
import random
from loguru import logger
from pipelinevilma.Messager import Messager
from pipelinevilma.CollectorDataApi import CollectorDataApi


class Collector:

    def __init__(self,  bypass, ratio, queue_server, queue_input, queue_output, data_api_config):
        self.bypass = bypass
        self.ratio = ratio
        self.queue_output = queue_output
        self.receiver = Messager(queue_server, queue_input)
        self.delivery = Messager(queue_server, queue_output)
        self.data_api = CollectorDataApi(data_api_config)

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self):
        self.receive(self.on_new_message)

    def on_new_message(self, ch, method, properties, body):
        # Callback function
        logger.info("Message received!")
        message = json.loads(body)
        sensor_id = message['x']['sensorId']
        # data_type = message['x']['dataType']

        if ch.is_open:
            ch.basic_ack(method.delivery_tag)
            random_number = random.random()
            logger.debug(f"Ratio: {self.ratio} Random: {random_number}")
            if not self.bypass and random_number <= self.ratio:
                logger.warning("Persisting item on the database...")
                if self.data_api.add_item(message):
                    logger.info("Item stored!")
                else:
                    logger.error("Error storing item!")

            queue_name = f"{self.queue_output}-{sensor_id}"
            logger.info(f"Forwarding message to queue {queue_name}")
            self.forward(queue_name, body)

            logger.info("Item forwarded!")

    def receive(self, callback):
        self.receiver.consume(callback)

    def forward(self, sensor_id, message):
        self.delivery.publish_to_sibling_queue(message, sensor_id)
