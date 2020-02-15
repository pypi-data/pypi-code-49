import json
import time
from loguru import logger
from pipelinevilma.Messager import Messager
from pipelinevilma.CollectorDataApi import CollectorDataApi


class FileManager:
    def __init__(self, queue_server, output_queue, retrain_counter, api_options):
        self.output_queue = Messager(queue_server, output_queue)
        self.retrain_counter = retrain_counter
        self.data_api = CollectorDataApi(api_options)

    def run(self, loop_interval=0.016):
        while True:
            counter_labeled_data = self.data_api.count_labeled()
            logger.info(f"{counter_labeled_data}/{self.retrain_counter}")

            if (counter_labeled_data > 0 and counter_labeled_data % self.retrain_counter == 0) or counter_labeled_data > self.retrain_counter:
                logger.debug("Downloading images and labels")
                items_ids = self._download_data_and_labels()

                items, labels = self.get_dataset_paths()

                logger.debug("Forwarding paths to trainer")
                message = {
                    'x': items,
                    'y': labels,
                }
                self.forward_to_trainer(json.dumps(message))
                self.mark_data_as_included_in_the_training_process(items_ids)

            time.sleep(loop_interval)

    def mark_data_as_included_in_the_training_process(self, items_ids):
        logger.debug(f"Marking items: {len(items_ids)}")
        for item_id in items_ids:
            res = self.data_api.mark_trained(item_id, "includedOnDataset")
            logger.debug(res)

    def _download_data_and_labels(self):
        dataset_ids = self.data_api.get_training_data()
        logger.debug(len(dataset_ids))
        for item_id in dataset_ids:
            x, y = self.data_api.get_item(item_id)
            self.store_on_filemanager(item_id, x=x, y=y)

        return dataset_ids

    def get_dataset_paths(self):
        raise NotImplementedError("Should have implemented this")

    def store_on_filemanager(self, name, x, y):
        raise NotImplementedError("Should have implemented this")

    def forward_to_trainer(self, message):
        try:
            self.output_queue.publish(message, validate=False)
            logger.debug("Message published")
        except Exception as err:
            logger.error(f"Error: {err}")
