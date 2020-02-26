"""Provides IngestWorker class."""
import importlib
import logging
import os
import time
import signal
from multiprocessing import Event, Process

from .ingest_db import IngestDB
from .tasks import create_task

log = logging.getLogger(__name__)


class IngestWorkerPool:
    """Ingest worker pool"""

    def __init__(self, config):
        self._config = config
        self._work_processes = []
        self._running = False

    def start(self):
        """Start the worker with N processes. Noop if the worker already started."""
        if self._running:
            return

        self._running = True
        for _ in range(self._config.jobs):
            self._start_single_worker()

    def _start_single_worker(self):
        """Start a worker process."""
        p_name = f"{self._config.worker_name}-{len(self._work_processes)}"
        shutdown_event = Event()
        target = IngestWorker(self._config, p_name, shutdown_event).run
        proc = Process(target=target, name=p_name, daemon=True)
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


class IngestWorker:  # pylint: disable=too-few-public-methods
    """Ingest worker, wait for task and execute it"""

    def __init__(self, config, name=None, shutdown=None):
        self.config = config
        self.name = name or config.worker_name
        self.shutdown = shutdown or Event()

    def run(self):
        """Run the worker"""
        original_sigint_handler = signal.getsignal(signal.SIGINT)
        original_sigterm_handler = signal.getsignal(signal.SIGTERM)
        def _catch_first(signum, *_):
            log.info(f"{self.name} received {signum}, shutting down gracefully")
            self.shutdown.set()
            signal.signal(signal.SIGINT, original_sigint_handler)
            signal.signal(signal.SIGTERM, original_sigterm_handler)
        signal.signal(signal.SIGINT, _catch_first)
        signal.signal(signal.SIGTERM, _catch_first)

        # Optional Signal handler for PDB
        if os.environ.get('ENABLE_SIGINT_PDB') == 'true':
            def _handle_pdb(_sig, frame):
                import pdb  # pylint: disable=import-outside-toplevel
                pdb.Pdb().set_trace(frame)
            signal.signal(signal.SIGINT, _handle_pdb)

        log.debug(f"{self.name} worker started, wating for connection...")
        engine = IngestDB.create_engine(self.config.db_url)
        while not self.shutdown.is_set():
            if IngestDB.check_connection(self.config.db_url):
                break
            time.sleep(self.config.sleep_time)

        if self.config.db_check_fn is not None:
            # Load the db_check_fn and wait until it returns True
            log.debug(f"{self.name}: waiting for schema - {self.config.db_check_fn}...")
            module_name, _, function_name = self.config.db_check_fn.rpartition('.')
            module = importlib.import_module(module_name)
            check_fn = getattr(module, function_name)

            # check_fn takes an engine instance and returns bool
            while not self.shutdown.is_set():
                if check_fn(engine):
                    break
                time.sleep(self.config.sleep_time)

            log.debug(f"{self.name}: schema is up to date")
        else:
            log.debug(f"{self.name}: skipping schema check - none specified")

        log.debug(f"{self.name} worker connected, waiting for tasks...")
        while not self.shutdown.is_set():
            task = None
            try:
                task = IngestDB.get_task(self.config, self.name)
                if task:
                    log.debug(f"{self.name} executing task {task.ingest_id}/{task.type}/{task.id}")
                    _task = create_task(task, self.config)
                    _task.execute()
                    log.debug(f"{self.name} executing task completed {task.ingest_id}/{task.type}/{task.id}")
                    continue
            except KeyboardInterrupt as exc:
                if task:
                    _task = create_task(task, self.config)
                    _task.handle_task_failure(exc)
                    log.debug(f"killed {self.name} worker while it worked on a task: {task.ingest_id}/{task.type}/{task.id}")

            try:
                time.sleep(self.config.sleep_time)
            except KeyboardInterrupt:
                log.debug(f"killed {self.name} worker process, but it didn't work on any task")
                return

        log.debug(f"{self.name} worker process exited gracefully")
