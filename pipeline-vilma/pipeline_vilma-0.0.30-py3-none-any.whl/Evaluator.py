import json
import time
from pipelinevilma.Messager import Messager
from loguru import logger


class Evaluator:
    def __init__(self, queue_server, queue_input, queue_output):
        self.queue_server = queue_server
        self.input_queue = Messager(queue_server, queue_input)
        self.output_queue = Messager(queue_server, queue_output)
        self.evaluated = []
        self.current_best = None

    def evaluate_models(self, message):
        raise NotImplementedError("Should have implemented this")

    def include_evaluation_to_list(self, key, value):
        self.evaluated.append((key, value))

    def is_included_in_evaluation_list(self, key):
        d = dict(self.evaluated)
        if key in d:
            logger.info(f"Model {key} was already evaluated")
            return True

        logger.info(f"Model {key} has not been evaluated")
        return False

    def get_current_best_evaluated(self):
        if self.current_best is None:
            return (None, None)
        return (self.current_best[0], self.current_best[1])

    def set_current_best_evaluated(self, key, value):
        self.current_best = (key, value)

    def run(self, loop_interval=0.016):
        while True:
            logger.info("Waiting for messages...")
            message = self.input_queue.get_message()
            if message:
                model_definition, weight, mAP = self.evaluate_models(message)
                if model_definition and weight and mAP:
                    self.set_current_best_evaluated(weight, mAP)

                    key, value = self.get_current_best_evaluated()
                    response = {
                        "key": key,
                        "value": value,
                        "params": {
                            "modelDefinition": model_definition
                        }
                    }
                    logger.info(f"Sending message to {self.output_queue.queue_name}")
                    try:
                        self.forward(json.dumps(response))
                    except Exception as err:
                        logger.error(err)
                else:
                    logger.info(f"{weight} is still the best with mAP = {mAP}")
            time.sleep(loop_interval)

    def forward(self, message):
        self.output_queue.publish(message=message, validate=False)
