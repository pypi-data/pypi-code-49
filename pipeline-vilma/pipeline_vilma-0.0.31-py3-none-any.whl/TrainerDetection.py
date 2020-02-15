import json
import time
from pipelinevilma.Messager import Messager
from loguru import logger


class TrainerDetection:
    def __init__(self, queue_server, queue_input, queue_output):
        self.queue_server = queue_server
        self.input_queue = Messager(queue_server, queue_input)
        self.output_queue = Messager(queue_server, queue_output)

    def get_new_training_samples(self):
        message = self.input_queue.get_message()

        if message:
            return message

        return False

    def train(self, pretrained):
        raise NotImplementedError("Should have implemented this")

    def create_train_and_validation_files(self, message):
        raise NotImplementedError("Should have implemented this")

    def get_latest_pretrained_weights(self):
        raise NotImplementedError("Should have implemented this")

    def send_weights_to_evaluator(self):
        raise NotImplementedError("Should have implemented this")

    def run(self, loop_interval=0.016):

        while True:
            logger.info("Waiting for new data")
            message = self.get_new_training_samples()
            if message:
                logger.info(message)
                self.create_train_and_validation_files(json.loads(message))
                pretrained = self.get_latest_pretrained_weights()
                logger.debug(pretrained)

                self.train(pretrained)

            time.sleep(loop_interval)

    def forward(self, message):
        self.output_queue.publish(message=message, validate=False)
