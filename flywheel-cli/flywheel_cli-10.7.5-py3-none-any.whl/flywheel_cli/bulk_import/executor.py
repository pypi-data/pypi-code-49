"""Provides BulkImportExecutor class."""
import logging
import time
import signal
from abc import ABC, abstractmethod
from multiprocessing import Event, Process, current_process

log = logging.getLogger(__name__)


class BulkImportExecutor:
    """Executor for bulk import which can consume multiple queues and manage worker processes."""

    def __init__(self):
        self._queues = {}
        self._work_processes = []
        self._running = False

    def add_queue(self, name, queue_obj):
        """Add a queue.

        Arguments:
            name {str} -- Name of the queue
            queue_obj {AbstractQueue} -- Queue that should be consumed
        """
        if not isinstance(queue_obj, AbstractQueue):
            raise Exception("Should add queue which implements AbstractQueue")
        self._queues[name] = queue_obj

    def start(self, worker_count=1):
        """Start the executor with N workers. Noop if the worker already started."""
        if self._running:
            return

        self._running = True
        for _ in range(worker_count):
            self._start_single_worker()

    def _start_single_worker(self):
        """Start a worker process.

        The processes will assign themselfs to a queue according to the desired process counts.
        """

        p_name = f"bulk_import-worker-{len(self._work_processes)}"
        log.debug(p_name)
        shutdown_event = Event()
        args = (
            shutdown_event,
            self._queues,
        )
        proc = Process(target=self._do_work, name=p_name, daemon=True, args=args)
        proc.start()
        self._work_processes.append((proc, shutdown_event))

    def join(self):
        """Wait until all worker processes terminate"""
        for proc, _ in self._work_processes:
            proc.join()

    def shutdown(self):
        """Shutdown the executor.

        Send shutdown event for every worker processes and wait until all of them terminate.
        """
        for _, shutdown_event in self._work_processes:
            shutdown_event.set()
        self.join()

    @staticmethod
    def _do_work(shutdown_event, queues):
        """Do the actual work. Work until shutdown event is not set.

        Arguments:
            shutdown_event {Event} -- Shutdown event. Terminate if it is set
            queues {dict} -- Queues that need to be consumed
        """
        BulkImportExecutor._init_worker()
        while not shutdown_event.is_set():
            task = BulkImportExecutor._get_task(queues)
            if not task:
                log.debug("No task, take a nap....")
                time.sleep(1)
                continue
            log.debug(task)
            task.execute()
        log.debug(f"{current_process().name} worker process exiting")

    @staticmethod
    def _init_worker():
        """Initialize worker process"""
        original_handler = signal.getsignal(signal.SIGINT)
        def _ignore_first(*_):
            signal.signal(signal.SIGINT, original_handler)
        signal.signal(signal.SIGINT, _ignore_first)

    @staticmethod
    def _get_task(queues):
        """Get task. Tries to get task from every queue in order.

        Arguments:
            queues {dict} -- Secondary queues

        Returns:
            Task -- Task to execute or None if no task
        """

        for queue in queues.values():
            task = queue.get()
            if task:
                return task
        return None


class Task(ABC):  # pylint: disable=too-few-public-methods
    """Abstract class that represents a task in the queue."""
    @abstractmethod
    def execute(self):
        """Execute the given task"""


class AbstractQueue(ABC):  # pylint: disable=too-few-public-methods
    """Abstract queue interface that needs for the executor"""

    @abstractmethod
    def get(self):
        """Get a task."""
