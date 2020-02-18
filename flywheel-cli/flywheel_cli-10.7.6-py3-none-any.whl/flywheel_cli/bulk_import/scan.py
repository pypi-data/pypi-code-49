"""Provides ScanQueue class."""

import logging
from multiprocessing import current_process

from .executor import AbstractQueue
from .scanners.factory import create_scanner_task

log = logging.getLogger(__name__)


class ScanQueue(AbstractQueue):  # pylint: disable=too-few-public-methods
    """Class that wraps a ScanQueueMapper object and provides methods that necessary for the MultiQueueConsumer."""

    def __init__(self, context):
        self.context = context

    def get(self):
        """Get an item from the scan queue table.

        Returns:
            Task -- Task object that can be executed.
        """
        worker_id = current_process().name
        task_item = self.context.scan_queue_mapper.get(worker_id)
        if task_item is not None:
            return create_scanner_task(task_item,
                                       self.context.ingest_factory,
                                       self.context.config)
        return None
