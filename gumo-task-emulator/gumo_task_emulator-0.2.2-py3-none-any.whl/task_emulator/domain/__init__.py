import dataclasses
import enum
import datetime
import random

from typing import Optional
from typing import List

from gumo.datastore import EntityKey
from gumo.datastore import EntityKeyFactory
from gumo.task.domain import GumoTask


class TaskState(enum.Enum):
    QUEUED = 'queued'
    PROCESSING = 'processing'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'

    def is_finished(self):
        return self == self.SUCCEEDED or self == self.FAILED

    def is_processing(self):
        return self == self.PROCESSING

    def is_queued(self):
        return self == self.QUEUED

    @classmethod
    def get(cls, value: str):
        try:
            return cls(value)
        except ValueError:
            return cls.QUEUED


@dataclasses.dataclass(frozen=True)
class ProcessRequest:
    method: str
    url: str
    data: Optional[str]
    headers: Optional[dict]

    def data_as_bytes(self) -> Optional[bytes]:
        if self.data is None:
            return
        return self.data.encode('utf-8')


@dataclasses.dataclass(frozen=True)
class ProcessHistory:
    started_at: datetime.datetime
    duration_seconds: float
    method: str
    url: str
    data: Optional[str]
    status_code: Optional[int] = None
    request_headers: Optional[dict] = None
    request_body: Optional[str] = None
    response_headers: Optional[str] = None
    response_body: Optional[str] = None
    error_message: Optional[str] = None

    def is_succeeded(self) -> bool:
        if self.status_code is None:
            return False
        if self.error_message is not None:
            return False

        return 200 <= self.status_code < 400


@dataclasses.dataclass(frozen=True)
class GumoTaskProcess:
    KIND = 'GumoTaskProcess'
    MAX_RETRY_COUNT = 15

    key: EntityKey
    relative_uri: str
    method: str = 'POST'
    payload: Optional[dict] = dataclasses.field(default_factory=dict)
    headers: Optional[dict] = dataclasses.field(default_factory=dict)
    schedule_time: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)
    created_at: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)
    queue_name: Optional[str] = None
    state: TaskState = TaskState.QUEUED
    attempts: int = 0
    last_run_at: Optional[datetime.datetime] = None
    run_at: Optional[datetime.datetime] = None
    locked_at: Optional[datetime.datetime] = None
    succeeded_at: Optional[datetime.datetime] = None
    failed_at: Optional[datetime.datetime] = None
    histories: List[ProcessHistory] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        if self.key.kind() != self.KIND:
            raise ValueError(f'key KIND must be a {self.KIND}, but got: {self.key.kind()}')

    def _clone(self, **changes):
        """
        一部の attributes を変更した、自身のオブジェクトの複製を返す

        :param changes: 変更する attributes
        :return: 一部の attributes が変更された、新しい TextExtractionJob オブジェクト
        :rtype: GumoTaskProcess
        """
        return dataclasses.replace(self, **changes)

    def with_history(self, history: ProcessHistory):
        """
        :rtype: GumoTaskProcess
        """
        histories = self.histories
        histories.append(history)

        return self._clone(histories=histories)

    def with_state(self, state: TaskState):
        """
        :rtype: GumoTaskProcess
        """
        return self._clone(state=state)

    def with_processing(self):
        return self.with_state(
            state=TaskState.PROCESSING
        )._clone(
            locked_at=datetime.datetime.utcnow(),
        )

    def with_succeeded(self, history: ProcessHistory):
        return self.with_state(
            state=TaskState.SUCCEEDED
        ).with_history(
            history=history
        )._clone(
            succeeded_at=datetime.datetime.utcnow(),
            locked_at=None,
        )

    def reach_max_retries(self):
        return self.attempts > self.MAX_RETRY_COUNT

    def with_failed(self, history: ProcessHistory, force_failed: bool = False):
        if self.reach_max_retries() or force_failed:
            return self._with_failed_permanent(history=history)
        else:
            return self._with_failed_to_retry(history=history)

    def _with_failed_to_retry(self, history: ProcessHistory):
        return self.with_state(
            state=TaskState.QUEUED
        ).with_history(
            history=history
        )._clone(
            attempts=self.attempts + 1,
            last_run_at=history.started_at,
            run_at=self._rescheduled_at(time=self.run_at, attempts_count=self.attempts + 1),
            locked_at=None,
        )

    def _with_failed_permanent(self, history: ProcessHistory):
        return self.with_state(
            state=TaskState.FAILED
        ).with_history(
            history=history
        )._clone(
            attempts=self.attempts + 1,
            last_run_at=history.started_at,
            failed_at=datetime.datetime.utcnow(),
            locked_at=None,
        )

    def _rescheduled_at(self, time: datetime.datetime, attempts_count) -> datetime.datetime:
        base_offset = 1
        random_offset = random.random() * 5
        exponential_offset = pow(attempts_count, 4)
        delta = datetime.timedelta(seconds=base_offset + random_offset + exponential_offset)

        return time + delta


class GumoTaskProcessFactory:
    def build_from_task(self, task: GumoTask) -> GumoTaskProcess:
        now = datetime.datetime.utcnow().replace(microsecond=0)
        run_at = task.schedule_time if task.schedule_time else now

        return GumoTaskProcess(
            key=EntityKeyFactory().build(kind=GumoTaskProcess.KIND, name=task.key.name()),
            relative_uri=task.relative_uri,
            method=task.method,
            payload=task.payload,
            headers=task.headers,
            schedule_time=task.schedule_time,
            created_at=task.created_at,
            updated_at=now,
            queue_name=task.queue_name,
            state=TaskState.QUEUED,
            attempts=0,
            last_run_at=None,
            run_at=run_at,
            failed_at=None,
            histories=[],
        )

    def build_with_new_history(
            self,
            task_process: GumoTaskProcess,
            history: ProcessHistory
    ) -> GumoTaskProcess:
        histories = task_process.histories
        histories.append(history)
        return dataclasses.replace(task_process, histories=histories)


@dataclasses.dataclass(frozen=True)
class TaskCount:
    count: int
    has_next: bool

    def __str__(self):
        if self.has_next:
            return f'{self.count}+'
        else:
            return f'{self.count}'


@dataclasses.dataclass(frozen=True)
class QueueStatus:
    queue_name: str
    queued_tasks_count: TaskCount
    processing_tasks_count: TaskCount
    succeeded_tasks_count: TaskCount
    failed_tasks_count: TaskCount
    oldest_schedule_time: Optional[datetime.datetime]

    def to_dict(self) -> dict:
        return {
            'queue_name': self.queue_name,
            'queued_tasks_count': str(self.queued_tasks_count),
            'processing_tasks_count': str(self.processing_tasks_count),
            'succeeded_tasks_count': str(self.succeeded_tasks_count),
            'failed_tasks_count': str(self.failed_tasks_count),
            'oldest_schedule_time': self.oldest_schedule_time.isoformat() if self.oldest_schedule_time else None,
        }


@dataclasses.dataclass(frozen=True)
class QueueStatusCollection:
    queue_statuses: List[QueueStatus]

    def to_dict(self) -> List[dict]:
        return [
            q.to_dict() for q in self.queue_statuses
        ]
