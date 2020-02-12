"""Provides the AbstractTask class."""
import logging
import traceback
from abc import ABC, abstractmethod

from ..ingest_db import IngestDB
from ..strategies.factory import STRATEGIES_MAP
from .. import utils

log = logging.getLogger(__name__)


class AbstractTask(ABC):
    """Provides a common interface for the different type of tasks."""
    can_retry = False

    def __init__(self, task, worker_config):
        self.task = task
        self.ingest_db = IngestDB(task.ingest_id, worker_config)
        self.ingest = None
        self.config = None

    @property
    def fw(self):
        """Get flywheel SDK client"""
        return utils.get_sdk_client(self.ingest.api_key)

    @abstractmethod
    def _execute(self):
        """Task specific implementation."""

    def _initialize(self):
        """Initialize the task before execution."""

    def _after_complete(self):
        """Called when the task completed successfully"""

    def _after_failed(self):
        """Called when the task ultimately failed"""

    def execute(self):
        """Execute the task."""
        try:
            self._load_ingest()
            self._initialize()
            self._execute()
            self.ingest_db.finish_task(self.task.id)
            self._run_safely(self._after_complete)
        except Exception as exc:  # pylint: disable=broad-except
            self._run_safely(self.handle_task_failure, exc)

    def handle_task_failure(self, exc):
        """Handle task failure, reschedule task if it is retriable"""
        log.debug(traceback.format_exc())
        if self.can_retry and self.task.retries < self.config.max_retries:
            self.ingest_db.retry_task(self.task.id)
            log.debug(f"Task failed, number of try: {self.task.retries + 1}")
        else:
            self.ingest_db.fail_task(
                self.task.id,
                error=str(exc),
            )
            self._after_failed()

    def _load_ingest(self):
        """Load ingest and parse configuration"""
        self.ingest = self.ingest_db.get_ingest()
        json_config = self.ingest.config
        strategy_cls = STRATEGIES_MAP.get(json_config["strategy_type"])
        if not strategy_cls:
            raise Exception(f"Invalid ingest strategy type: {json_config['strategy_type']}")
        self.config = strategy_cls.config_cls(**json_config)

    def _run_safely(self, func, *args, **kwargs):
        """Fail the ingest if exception raised during executing the given func"""
        try:
            func(*args, **kwargs)
        except Exception as exc:  # pylint: disable=broad-except
            log.exception(exc)
            # critical failure, prevent ingest to stuck in not terminal
            # status
            self.ingest_db.fail_ingest()
