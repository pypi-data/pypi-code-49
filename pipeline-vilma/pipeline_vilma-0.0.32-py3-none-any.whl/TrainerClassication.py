import json
import time
from pipelinevilma.Messager import Messager
from loguru import logger


class TrainerClassification:
    def __init__(self, queue_server, queue_input, queue_output):
        self.queue_server = queue_server
        self.input_queue = Messager(queue_server, queue_input)
        self.output_queue = Messager(queue_server, queue_output)

    def check_for_new_training_items(self):
        message = self.input_queue.get_message()

        if message:
            return message

        return False

    def train(self, pretrained):
        raise NotImplementedError("Should have implemented this")

    def shuffle_train_test_dataset(self, data_path):
        raise NotImplementedError("Should have implemented this")

    def create_train_and_valid_files(self, message):

        logger.debug(message['x'])
        files, num_val, num_train = self.shuffle_train_test_dataset(message['x'])
        training_files = files[: num_train]
        validation_files = files[num_train:]
        logger.debug(training_files)
        logger.debug(validation_files)

        with open(TRAIN_PATH, 'w') as f:
            for item in training_files:
                f.write("%s\n" % item)
        with open(VALID_PATH, 'w') as f:
            for item in validation_files:
                f.write("%s\n" % item)

        logger.info("Start the retraining process...")

    def get_latest_pretrained_weights(self):
        raise NotImplementedError("Should have implemented this")
    
    def send_weights_to_evaluator(self):
        raise NotImplementedError("Should have implemented this")

    def run(self, loop_interval=0.016):

        os.makedirs("output", exist_ok=True)
        os.makedirs("checkpoints", exist_ok=True)

        while True:
            logger.info("Waiting for new data")
            message = self.check_for_new_training_items()
            if message:
                logger.info(message)
                create_train_and_valid_files(json.loads(message))
                pretrained = self.get_latest_pretrained_weights()
                logger.debug(pretrained)
                self.train(pretrained)
                
            time.sleep(loop_interval)

    def forward(self, message):
        self.output_queue.publish(message=message, validate=False)
