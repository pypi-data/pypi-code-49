import time
from pipelinevilma.Messager import Messager
from pipelinevilma.packer.BasePackage import BasePackage
import json


class Provider:
    def __init__(self, queue_server, queue_output, sensor_id):
        self.queue = Messager(queue_server, queue_output)
        self.sensor_id = sensor_id

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def pack_data(self, data_type, content):
        raw_data = BasePackage(data_type, content, self.sensor_id)
        return raw_data.pack()

    def run(self, loop_interval=0.016):
        raise NotImplementedError("Should have implemented this")

    def forward(self, message):
        self.queue.publish(message=message)
