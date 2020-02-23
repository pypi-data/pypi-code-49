from logging import getLogger

from injector import inject

from gumo.core.exceptions import ObjectNotoFoundError
from gumo.datastore import datastore_transaction
from gumo.task.domain import GumoTask

from gumo.task_emulator.domain import GumoTaskProcess
from gumo.task_emulator.domain import GumoTaskProcessFactory
from gumo.task_emulator.application.task.repository import TaskRepository
from gumo.task_emulator.application.task.repository import TaskProcessRepository

logger = getLogger(__name__)


class TaskProcessBulkCreateService:
    @inject
    def __init__(
            self,
            task_repository: TaskRepository,
            task_process_repository: TaskProcessRepository,
            task_process_factory: GumoTaskProcessFactory,
    ):
        self._task_repository = task_repository
        self._task_process_repository = task_process_repository
        self._task_process_factory = task_process_factory

    def execute(self) -> dict:
        tasks = self._task_repository.fetch_default_routing_tasks(limit=50)
        converted_tasks = []
        convert_skipped_tasks = []

        for task in tasks:
            logger.debug(f'Convert start Task.key={task.key}')
            task_process = self._build_task_process(task=task)

            if self._convert_task_process(task=task, task_process=task_process):
                converted_tasks.append(task_process)
            else:
                convert_skipped_tasks.append(task_process)

        return {
            'converted_tasks': len(converted_tasks),
            'convert_skipped_tasks': len(convert_skipped_tasks)
        }

    def _build_task_process(self, task: GumoTask) -> GumoTaskProcess:
        return self._task_process_factory.build_from_task(task=task)

    @datastore_transaction()
    def _convert_task_process(self, task: GumoTask, task_process: GumoTaskProcess) -> bool:
        created = self._create_task_process_if_not_exists(task_process=task_process)
        self._task_repository.delete(key=task.key)

        return created

    def _create_task_process_if_not_exists(self, task_process: GumoTaskProcess) -> bool:
        try:
            self._task_process_repository.fetch_by_key(key=task_process.key)
            created = False
        except ObjectNotoFoundError:
            self._task_process_repository.save(task_process=task_process)
            created = True

        return created
