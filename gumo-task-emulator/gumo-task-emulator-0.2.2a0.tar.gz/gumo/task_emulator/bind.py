from gumo.task_emulator.application.task.repository import TaskRepository
from gumo.task_emulator.infrastructure.repository import DatastoreTaskRepository

from gumo.task_emulator.application.task.repository import TaskProcessRepository
from gumo.task_emulator.infrastructure.repository import DatastoreTaskProcessRepository

from gumo.task_emulator.application import TaskExecuteRunner
from gumo.task_emulator.infrastructure.execute_service import TaskExecuteRunnerImpl

from gumo.task_emulator.application.task.repository import TaskProcessSummaryRepository
from gumo.task_emulator.infrastructure.repository import DatastoreTaskProcessSummaryRepository


def task_emulator_bind(binder):
    binder.bind(TaskRepository, to=DatastoreTaskRepository)
    binder.bind(TaskProcessRepository, to=DatastoreTaskProcessRepository)
    binder.bind(TaskExecuteRunner, to=TaskExecuteRunnerImpl)
    binder.bind(TaskProcessSummaryRepository, to=DatastoreTaskProcessSummaryRepository)
