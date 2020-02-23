import datetime
from typing import Optional

from gumo.task.domain import GumoTask
from gumo.task_emulator.domain import GumoTaskProcess
from gumo.task_emulator.domain import ProcessHistory


class TaskJSONEncoder:
    def __init__(
            self,
            task: GumoTask,
    ):
        self._task = task

    def datetime_to_json(self, t: datetime.datetime) -> Optional[str]:
        if t is None:
            return
        return t.isoformat()

    def to_json(self) -> dict:
        j = {
            'key': self._task.key.key_path(),
            'keyLiteral': self._task.key.key_literal(),
            'relativeURI': self._task.relative_uri,
            'method': self._task.method,
            'payload': self._task.payload,
            'scheduleTime': self.datetime_to_json(self._task.schedule_time),
            'createdAt': self.datetime_to_json(self._task.created_at),
            'queueName': self._task.queue_name,
        }
        return j


class TaskProcessJSONEncoder:
    def __init__(
            self,
            task_process: GumoTaskProcess,
    ):
        self._task_process = task_process

    def datetime_to_json(self, t: datetime.datetime) -> Optional[str]:
        if t is None:
            return
        return t.isoformat()

    def to_json(self) -> dict:
        j = {
            'key': self._task_process.key.key_path(),
            'keyLiteral': self._task_process.key.key_literal(),
            'relativeURI': self._task_process.relative_uri,
            'method': self._task_process.method,
            'payload': self._task_process.payload,
            'scheduleTime': self.datetime_to_json(self._task_process.schedule_time),
            'createdAt': self.datetime_to_json(self._task_process.created_at),
            'updatedAt': self.datetime_to_json(self._task_process.updated_at),
            'queueName': self._task_process.queue_name,
            'state': self._task_process.state.value,
            'attempts': self._task_process.attempts,
            'lastRunAt': self.datetime_to_json(self._task_process.last_run_at),
            'runAt': self.datetime_to_json(self._task_process.run_at),
            'lockedAt': self.datetime_to_json(self._task_process.locked_at),
            'succeededAt': self.datetime_to_json(self._task_process.succeeded_at),
            'failedAt': self.datetime_to_json(self._task_process.failed_at),
            'histories': [
                self._history_to_json(history=history) for history in self._task_process.histories
            ],
        }
        return j

    def _history_to_json(self, history: ProcessHistory) -> dict:
        j = {
            'startedAt': self.datetime_to_json(history.started_at),
            'durationSeconds': history.duration_seconds,
            'statusCode': history.status_code,
            'requestHeaders': history.request_headers,
            'requestBody': history.request_body,
            'responseHeaders': history.response_headers,
            'responseBody': history.response_body,
            'errorMessage': history.error_message,
        }
        return j
