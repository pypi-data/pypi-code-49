import datetime
from logging import getLogger

from injector import inject
from typing import List
from typing import Optional

from gumo.core.exceptions import ObjectNotoFoundError
from gumo.core import EntityKey
from gumo.datastore.infrastructure import DatastoreRepositoryMixin
from gumo.task.domain import GumoTask
from gumo.task.infrastructure.repository.mapper import DatastoreGumoTaskMapper

from gumo.task_emulator.domain import GumoTaskProcess
from gumo.task_emulator.domain import TaskState
from gumo.task_emulator.domain import TaskCount
from gumo.task_emulator.domain import QueueStatus
from gumo.task_emulator.domain import QueueStatusCollection
from gumo.task_emulator.application.task.repository import TaskRepository
from gumo.task_emulator.application.task.repository import TaskProcessRepository
from gumo.task_emulator.application.task.repository import TaskProcessSummaryRepository
from gumo.task_emulator.infrastructure.mapper import DatastoreGumoTaskProcessMapper

logger = getLogger(__name__)


class DatastoreTaskRepository(TaskRepository, DatastoreRepositoryMixin):
    @inject
    def __init__(
            self,
            gumo_task_mapper: DatastoreGumoTaskMapper,
    ):
        super(DatastoreTaskRepository, self).__init__()
        self._task_mapper = gumo_task_mapper

    def _build_query(self):
        return self.datastore_client.query(kind=GumoTask.KIND)

    def _fetch_list(self, query, limit: Optional[int] = None) -> List[GumoTask]:
        tasks = []

        for datastore_entity in query.fetch(limit=limit):
            tasks.append(self._task_mapper.to_entity(
                doc=datastore_entity,
            ))

        return tasks

    def fetch_tasks(self, limit: int = 10) -> List[GumoTask]:
        return self._fetch_list(query=self._build_query(), limit=limit)

    def fetch_default_routing_tasks(self, limit: int = 10) -> List[GumoTask]:
        query = self._build_query()
        query.add_filter('app_engine_routing.service', '=', None)
        query.add_filter('app_engine_routing.version', '=', None)
        query.add_filter('app_engine_routing.instance', '=', None)

        return self._fetch_list(query=query, limit=limit)

    def delete(self, key: EntityKey):
        datastore_key = self.entity_key_mapper.to_datastore_key(entity_key=key)
        self.datastore_client.delete(datastore_key)


class DatastoreTaskProcessRepository(TaskProcessRepository, DatastoreRepositoryMixin):
    @inject
    def __init__(
            self,
            task_process_mapper: DatastoreGumoTaskProcessMapper,
    ):
        super(DatastoreTaskProcessRepository, self).__init__()
        self._task_process_mapper = task_process_mapper

    def _build_query(self):
        return self.datastore_client.query(kind=GumoTaskProcess.KIND)

    def _fetch_query(self, query, limit) -> List[GumoTaskProcess]:
        task_processes = []
        for datastore_entity in query.fetch(limit=(limit or 10)):
            task_processes.append(
                self._task_process_mapper.to_entity(datastore_entity=datastore_entity)
            )

        return task_processes

    def fetch_by_key(self, key: EntityKey) -> GumoTaskProcess:
        datastore_key = self.entity_key_mapper.to_datastore_key(entity_key=key)
        datastore_entity = self.datastore_client.get(key=datastore_key)
        if datastore_entity is None:
            raise ObjectNotoFoundError(f'key={key} is not found.')

        entity = self._task_process_mapper.to_entity(datastore_entity=datastore_entity)
        return entity

    def fetch_tasks_by_state(self, state: TaskState, limit: Optional[int] = None) -> List[GumoTaskProcess]:
        now = datetime.datetime.utcnow().replace(microsecond=0)
        query = self._build_query()
        query.add_filter('state', '=', state.value)
        query.add_filter('run_at', '<=', now)
        query.order = ['run_at']

        task_processes = self._fetch_query(query=query, limit=limit)
        return task_processes

    def fetch_tasks(
            self,
            queue_name: Optional[str] = None,
            limit: Optional[int] = None,
    ) -> List[GumoTaskProcess]:
        query = self._build_query()

        if queue_name:
            query.add_filter('queue_name', '=', queue_name)

        task_processes = self._fetch_query(query=query, limit=limit)
        return task_processes

    def save(self, task_process: GumoTaskProcess):
        datastore_entity = self._task_process_mapper.to_datastore_entity(task_process=task_process)
        logger.debug(f'Datastore Put key={datastore_entity.key}')
        self.datastore_client.put(datastore_entity)

    def cleanup_finished_tasks(self):
        for state in [TaskState.SUCCEEDED.value, TaskState.FAILED.value]:
            query = self._build_query()
            query.add_filter('state', '=', state)
            query.keys_only()

            keys = [task.key for task in query.fetch()]
            logger.info(f'cleanup target keys={len(keys)} items')
            self.datastore_client.delete_multi(keys=keys)


class DatastoreTaskProcessSummaryRepository(TaskProcessSummaryRepository, DatastoreRepositoryMixin):
    def _build_query(self):
        return self.datastore_client.query(kind=GumoTaskProcess.KIND)

    def _fetch_queue_names(self) -> List[str]:
        query = self._build_query()
        query.distinct_on = ['queue_name']

        return [t.get('queue_name') for t in query.fetch()]

    def _fetch_task_count_by_status(self, queue_name: str, state: TaskState):
        query = self._build_query()
        query.add_filter('queue_name', '=', queue_name)
        query.add_filter('state', '=', state.value)
        query.keys_only()

        limit = 100
        result = [task for task in query.fetch(limit=limit + 1)]

        if len(result) >= limit + 1:
            return TaskCount(
                count=len(result) - 1,
                has_next=True,
            )
        else:
            return TaskCount(
                count=len(result),
                has_next=False,
            )

    def _fetch_oldest_task_by_queue(self, queue_name: str) -> Optional[datetime.datetime]:
        query = self._build_query()
        query.add_filter('queue_name', '=', queue_name)
        query.add_filter('state', '=', TaskState.QUEUED.value)
        query.order = ['schedule_time']

        for task in query.fetch(limit=1):
            return task.get('schedule_time')

        return None

    def _fetch_queue_status(self, queue_name: str) -> QueueStatus:
        return QueueStatus(
            queue_name=queue_name if queue_name else 'unknown-queue',
            queued_tasks_count=self._fetch_task_count_by_status(queue_name=queue_name, state=TaskState.QUEUED),
            processing_tasks_count=self._fetch_task_count_by_status(queue_name=queue_name, state=TaskState.PROCESSING),
            succeeded_tasks_count=self._fetch_task_count_by_status(queue_name=queue_name, state=TaskState.SUCCEEDED),
            failed_tasks_count=self._fetch_task_count_by_status(queue_name=queue_name, state=TaskState.FAILED),
            oldest_schedule_time=self._fetch_oldest_task_by_queue(queue_name=queue_name),
        )

    def fetch_summary(self) -> QueueStatusCollection:
        queue_names = self._fetch_queue_names()
        queue_statuses = []
        for queue_name in queue_names:
            queue_statuses.append(
                self._fetch_queue_status(queue_name=queue_name)
            )

        return QueueStatusCollection(queue_statuses=queue_statuses)
