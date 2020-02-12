"""Provides factory method to create tasks."""

from .finalize import FinalizeTask
from .prepare import PrepareTask
from .upload import UploadTask
from .resolve import ResolveTask
from .scan import ScanTask


TASK_MAP = {
    "scan": ScanTask,
    "resolve": ResolveTask,
    "prepare": PrepareTask,
    "upload": UploadTask,
    "finalize": FinalizeTask,
}


def create_task(task, worker_config):
    """Create executable task from task object"""
    task_cls = TASK_MAP.get(task.type)
    if not task_cls:
        raise Exception(f"Invalid task type: {task.type}")
    return task_cls(task, worker_config)
