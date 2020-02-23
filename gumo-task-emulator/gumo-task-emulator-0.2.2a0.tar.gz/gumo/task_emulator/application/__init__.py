import datetime
import enum
import dataclasses

from injector import inject
from logging import getLogger

from gumo.datastore import EntityKey
from gumo.task_emulator.application.task.repository import TaskProcessRepository
from gumo.task_emulator.domain import GumoTaskProcess
from gumo.task_emulator.domain import TaskState
from gumo.task_emulator.domain import ProcessHistory
from gumo.task_emulator.application.task.encoder import TaskProcessJSONEncoder

logger = getLogger(__name__)


class TaskExecuteState(enum.Enum):
    RUN_AND_SUCCESS = 'run_and_success'
    RUN_AND_FAILED = 'run_and_failed'
    ALREADY_FINISHED = 'already_finished'
    OTHER_RUNNING = 'other_running'


@dataclasses.dataclass(frozen=True)
class TaskExecuteResult:
    state: TaskExecuteState
    task_process: GumoTaskProcess

    def to_json(self) -> dict:
        return {
            'state': self.state.value,
            'taskProcess': TaskProcessJSONEncoder(task_process=self.task_process).to_json(),
        }


class TaskExecuteRunner:
    def run(self, task_process: GumoTaskProcess) -> ProcessHistory:
        raise NotImplementedError()


class TaskExecuteService:
    @inject
    def __init__(
            self,
            task_process_repository: TaskProcessRepository,
            task_execute_runner: TaskExecuteRunner,
    ):
        self._task_process_repository = task_process_repository
        self._task_execute_runner = task_execute_runner

    def execute(self, key: EntityKey) -> TaskExecuteResult:
        task_process = self._task_process_repository.fetch_by_key(key=key)

        if task_process.state.is_finished():
            logger.info(f'TaskProcess.key={key} is already finished. Task execute has been skipped.')
            return TaskExecuteResult(
                state=TaskExecuteState.ALREADY_FINISHED,
                task_process=task_process,
            )

        # if task_process.state.is_processing():
        #     logger.info(f'TaskProcess.key={key} is in progress.')
        #     return TaskExecuteResult(
        #         state=TaskExecuteState.OTHER_RUNNING,
        #         task_process=task_process,
        #     )

        processing = task_process.with_processing()
        self._task_process_repository.save(task_process=processing)

        history = self._task_execute_runner.run(task_process=task_process)
        logger.info(history)

        if history.is_succeeded():
            finished = processing.with_succeeded(history=history)
        else:
            finished = processing.with_failed(history=history)
        self._task_process_repository.save(task_process=finished)

        return TaskExecuteResult(
            state=TaskExecuteState.RUN_AND_SUCCESS,
            task_process=finished,
        )


class TaskMarkAsFailedService:
    @inject
    def __init__(
            self,
            task_process_repository: TaskProcessRepository,
    ):
        self._task_process_repository = task_process_repository

    def execute(self, key: EntityKey) -> GumoTaskProcess:
        task_process = self._task_process_repository.fetch_by_key(key=key)

        if task_process.state.is_finished():
            return task_process

        now = datetime.datetime.utcnow()

        failed = task_process.with_failed(
            history=ProcessHistory(
                started_at=now,
                duration_seconds=0,
                method=task_process.method,
                url=task_process.relative_uri,
                data=None,
            ),
            force_failed=True,
        ).with_state(
            state=TaskState.FAILED,
        )

        self._task_process_repository.save(failed)

        return failed
