# coding: utf-8

import json
from google.cloud import pubsub_v1


class Pubsub:
    PROJECT_ID = "bbc-data-science"
    TOPIC_NAME = "framl-model-monitoring"

    def __init__(self):
        batch_settings = pubsub_v1.types.BatchSettings(
            max_bytes=1024,
            max_latency=10,
        )
        self.publisher = pubsub_v1.PublisherClient(batch_settings)
        self.topic_path = self.publisher.topic_path(self.PROJECT_ID, self.TOPIC_NAME)

    def publish_message(self, message: dict) -> None:
        if not message:
            raise Exception("Empty message ")

        data = json.dumps(message)
        data = data.encode('utf-8')
        self.publisher.publish(self.topic_path, data=data)
