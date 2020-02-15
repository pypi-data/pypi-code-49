import datetime
import json
import time
from loguru import logger
from pipelinevilma.Messager import Messager
from pipelinevilma.packer.Instance import Instance


class Instancer:
    def __init__(self, queue_server, queue_input_prefix, sensors, queue_output):
        sensors = sensors.split(" ")
        self.number_of_providers = len(sensors)
        self.queue_input_prefix = queue_input_prefix
        self.queue_inputs = []

        # Transform a string to a list of sensors
        for sensorId in sensors:
            queue = f"{queue_input_prefix}-{sensorId}"
            self.queue_inputs.append(Messager(queue_server, queue))
        self.queue_output = Messager(queue_server, queue_output)

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self, loop_interval=0.016):
        raise NotImplementedError("Should have implemented this")

    def create_custom_instance(self):
        raise NotImplementedError("Should have implemented this")

    def create_simple_instance(self):
        MAX_RETRIES = 10
        for i in range(self.number_of_providers):
            message = False
            retries = 0
            while not message and retries < MAX_RETRIES:
                retries += 1
                message = self.queue_inputs[i].get_message()

            if retries < 10:
                logger.info("Message received")
                instance_message = Instance(json.loads(message))
                # pack into instance
                self.forward(instance_message.pack())

    def create_instance_by_time_window(self, sensor_id, time_window_s):
        MAX_RETRIES = 10
        messages = []

        body = False
        retries = 0
        while not body and retries < MAX_RETRIES:
            retries += 1
            body = self.queue_inputs[sensor_id-1].get_message(self.queue_input + str(sensor_id))
            logger.debug(f"[{retries}] Getting the first message...")

        if retries == 0:
            print(f"Did not get the first message after retries")
            return False

        message = json.loads(body)
        time_window_begin = message['createdAt']
        logger.info(f"Got the first message! Time window begins at {time_window_begin}")
        logger.info(f"Aggregating the messages in the next {time_window_s}s")

        actual_time = time_window_begin
        limit_time = time_window_begin + time_window_s
        while actual_time < limit_time:
            body = self.queue_inputs[sensor_id-1].get_message(self.queue_input + str(sensor_id))
            if body:
                message = json.loads(body)
                messages.append(message)
                actual_time = message['createdAt']

        return messages

    def create_instance_by_repetition(self, sensor_id, number_of_messages):
        messages = []
        for i in range(number_of_messages):
            messages.append(self.queue_inputs[sensor_id-1].get_message(self.queue_input + str(sensor_id)))

        return messages

    def create_instance_by_syncing_all_providers(self):
        messages = []
        for i in range(self.number_of_providers):
            message = False
            while not message:
                message = self.queue_inputs[i].get_message()
            messages.append(message)

    def forward(self, message):
        self.queue_output.publish(message)
