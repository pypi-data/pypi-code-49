"""Provides the ScanTask class."""

import json

from ....util import custom_json_serializer
from .task_status import TaskStatus


class ScanTask:
    """Represents a task in the scan queue.

    Attributes:
        task_id (int): A unique id of the scan task.
        ingest_id (int): The associated ingest id.
        path (str): The path to the folder that needs to be scanned.
        context (dict): The partial context of the folder.
        scanner_type (str): The type of scan to perform (e.g. dicom).
        actor_id (str): A unique identifier of the actor that has claimed this task.
        status (str): The current status of the given task.
    """

    def __init__(self, task_id=None, ingest_id=None, path=None, context=None,
                 scanner_type=None, actor_id=None, status=None):
        """Create an ScanTask"""
        self.task_id = task_id
        self.ingest_id = ingest_id
        self.path = path
        self.context = context
        self.scanner_type = scanner_type
        self.actor_id = actor_id
        self.status = status

    @staticmethod
    def map_field(key, value):
        """Convert from object to map for serialization"""
        if key == 'context' and value is not None:
            if isinstance(value, dict):
                return json.dumps(value, default=custom_json_serializer)
            return value
        if key == 'status' and isinstance(value, TaskStatus):
            return value.value
        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into ScanTask.

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            ScanTask: The deserialized ingest item
        """
        result = ScanTask(**kwargs)
        if result.context is not None:
            result.context = json.loads(result.context)
        if result.status is not None:
            result.status = TaskStatus(result.status)
        return result

    def __repr__(self):
        return f"ScanTask(scanner_type={self.scanner_type},path={self.path})"
