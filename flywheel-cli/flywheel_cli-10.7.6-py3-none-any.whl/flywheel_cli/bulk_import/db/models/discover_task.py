"""Provides the DiscoverTask class."""

from .task_status import TaskStatus


class DiscoverTask:
    """Represents a task in the discover queue.

    Attributes:
        task_id (int): A unique id of the discover task.
        ingest_id (int): The id of the ingest this item belongs to.
        actor_id (str): A unique identifier of the actor that has claimed this task.
        status (str): The current status of the given task.
    """

    def __init__(self, task_id=None, ingest_id=None, actor_id=None, status=None):
        """Create an DiscoverTask"""
        self.task_id = task_id
        self.ingest_id = ingest_id
        self.actor_id = actor_id
        self.status = status

    @staticmethod
    def map_field(key, value):
        """Convert from object to map for serialization"""
        if key == 'status' and isinstance(value, TaskStatus):
            return value.value
        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into DiscoverTask.

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            DiscoverTask: The deserialized ingest item
        """
        result = DiscoverTask(**kwargs)
        if result.status is not None:
            result.status = TaskStatus(result.status)
        return result

    def __repr__(self):
        return f"DiscoverTask(task_id={self.task_id},status={self.status})"
