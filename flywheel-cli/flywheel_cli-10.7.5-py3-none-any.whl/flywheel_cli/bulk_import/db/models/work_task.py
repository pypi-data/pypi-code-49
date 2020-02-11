"""Provides the WorkTask class."""

import json

from ....util import custom_json_serializer
from .task_status import TaskStatus


class WorkTask:
    """Represents a task in the work queue.

    Attributes:
        task_id (int): A unique id of the work task.
        item_id (int): Foreign key to the Items table.
        ingest_id (int): The id of the ingest this item belongs to.
        context (dict): Updated context for this work item (Currently not used).
        actor_id (str): A unique identifier of the actor that has claimed this task.
        status (str): The current status of the given task.
    """

    def __init__(self, task_id=None, item_id=None, ingest_id=None, context=None, actor_id=None, status=None):
        """Create an WorkTask"""
        self.task_id = task_id
        self.item_id = item_id
        self.ingest_id = ingest_id
        self.context = context
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
            WorkTask: The deserialized ingest item
        """
        result = WorkTask(**kwargs)
        if result.context is not None:
            result.context = json.loads(result.context)
        if result.status is not None:
            result.status = TaskStatus(result.status)
        return result

    def __repr__(self):
        return f"WorkTask(task_id={self.task_id},status={self.status})"
