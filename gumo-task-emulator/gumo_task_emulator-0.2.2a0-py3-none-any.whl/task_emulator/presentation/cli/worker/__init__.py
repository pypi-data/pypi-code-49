import threading
import time
import logging

from typing import Optional
from gumo.core.injector import injector

from gumo.task_emulator.application import TaskExecuteService
from gumo.task_emulator.application.task import TaskProcessBulkCreateService
from gumo.task_emulator.application.task.repository import TaskProcessRepository
from gumo.task_emulator.domain import TaskState


logger = logging.getLogger(__name__)


class RoutineWorkerStop(RuntimeError):
    pass


class RoutineWorker:
    def __init__(self, interval_seconds: int = 1):
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self.loop)
        self._interval_seconds = interval_seconds
        self._started = False

        self._worker_name = f'RoutineWorker({self.__class__.__name__})'

    def start(self, daemon: bool = False, interval_seconds: Optional[int] = None):
        if self._started:
            logger.debug(f'{self._worker_name} is already started.')
            return

        if interval_seconds:
            self._interval_seconds = interval_seconds

        self._stop_event.clear()
        self._thread.setDaemon(daemon)
        self._thread.start()
        logger.debug(f'{self._worker_name} is starting with interval = {self._interval_seconds}sec.')

    def stop(self, wait=True):
        self._stop_event.set()
        if wait:
            self._thread.join()

    def loop(self):
        try:
            while True:
                self.run()

                for i in range(self._interval_seconds):
                    time.sleep(1)
                    self.check_stop()
        except RoutineWorkerStop:
            logger.debug(f'{self._worker_name} is stopped by signals.')

    def check_stop(self):
        if self._stop_event.is_set():
            raise RoutineWorkerStop('Received stop event.')

    def run(self):
        raise NotImplementedError()


class NoopTask(RoutineWorker):
    def run(self):
        time.sleep(1)


class WatchNewTask(RoutineWorker):
    def run(self):
        service = injector.get(TaskProcessBulkCreateService)  # type: TaskProcessBulkCreateService
        service.execute()


class ExecuteTask(RoutineWorker):
    def run(self):
        repository = injector.get(TaskProcessRepository)  # type: TaskProcessRepository
        execute_service = injector.get(TaskExecuteService)  # type: TaskExecuteService

        task_processes = repository.fetch_tasks_by_state(state=TaskState.QUEUED)

        for task in task_processes:
            logger.debug(f'task.key={task.key} is executing')
            execute_service.execute(key=task.key)
            self.check_stop()


class BackgroundWorker:
    _instance = None

    @classmethod
    def get_instance(cls, verbose_log: bool = False):
        if cls._instance is None:
            cls._instance = cls(verbose_log=verbose_log)

        return cls._instance

    def __init__(self, verbose_log: bool = False):
        if verbose_log:
            logger.setLevel(level=logging.INFO)
        else:
            logger.setLevel(level=logging.DEBUG)

        self._noop_worker = NoopTask()
        self._watch_new_task_worker = WatchNewTask()
        self._execute_task_worker = ExecuteTask()

        self._started = False

    def start(self, verbose: bool = False):
        if self._started:
            if verbose:
                logger.debug(f'{self} is already started.')
            return

        self._started = True
        self._noop_worker.start(daemon=False, interval_seconds=100)
        self._watch_new_task_worker.start(daemon=False, interval_seconds=2)
        self._execute_task_worker.start(daemon=False, interval_seconds=3)

    def stop(self):
        if not self._started:
            return

        self._watch_new_task_worker.stop(wait=False)
        self._execute_task_worker.stop(wait=False)

        self._watch_new_task_worker.stop(wait=True)
        self._execute_task_worker.stop(wait=True)
        self._noop_worker.stop(wait=True)

        self._started = False
