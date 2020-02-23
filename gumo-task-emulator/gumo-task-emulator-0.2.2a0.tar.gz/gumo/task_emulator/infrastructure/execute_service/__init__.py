import urllib.request
import urllib.error
import json
import datetime
from logging import getLogger
from injector import inject

from gumo.task_emulator.application import TaskExecuteRunner
from gumo.task_emulator.domain.configuration import TaskEmulatorConfiguration
from gumo.task_emulator.domain import GumoTaskProcess
from gumo.task_emulator.domain import ProcessRequest
from gumo.task_emulator.domain import ProcessHistory

logger = getLogger(__name__)


class TaskExecuteRunnerImpl(TaskExecuteRunner):
    @inject
    def __init__(
            self,
            task_emulator_configuration: TaskEmulatorConfiguration,
    ):
        self._task_emulator_configuration = task_emulator_configuration

    def _build_request_headers(self, task_process: GumoTaskProcess) -> dict:
        headers = {
            'Content-Type': 'application/json',
            'X-AppEngine-QueueName': task_process.queue_name,
            'X-AppEngine-TaskName': task_process.key.name(),
            'X-AppEngine-TaskRetryCount': str(task_process.attempts),
            'X-AppEngine-TaskExecutionCount': str(task_process.attempts + 1),
            'X-AppEngine-TaskETA': str(int(task_process.run_at.timestamp())),
        }

        if len(task_process.histories) > 0:
            previous_history = task_process.histories[-1]
            headers['X-AppEngine-TaskPreviousResponse'] = str(previous_history.status_code)

        if isinstance(task_process.headers, dict):
            headers.update(task_process.headers)

        return headers

    def _build_request(self, task_process: GumoTaskProcess) -> ProcessRequest:
        target_url = 'http://{host}:{port}{relative_uri}'.format(
            host=self._task_emulator_configuration.server_host,
            port=self._task_emulator_configuration.server_port,
            relative_uri=task_process.relative_uri,
        )
        request_headers = self._build_request_headers(task_process=task_process)
        request_body = json.dumps(task_process.payload)

        return ProcessRequest(
            method=task_process.method,
            url=target_url,
            headers=request_headers,
            data=request_body,
        )

    def _run_request(self, process_request: ProcessRequest) -> ProcessHistory:
        request = urllib.request.Request(
            url=process_request.url,
            method=process_request.method,
            data=process_request.data_as_bytes(),
            headers=process_request.headers,
        )

        started_at = datetime.datetime.utcnow()

        status_code = None
        response_headers = None
        response_body = None
        error_message = None

        try:
            with urllib.request.urlopen(request) as response:
                status_code = response.status
                response_body = response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            status_code = e.code
            error_message = e
            response_body = e.read().decode('utf-8')
        except urllib.error.URLError as e:
            error_message = e
        except Exception as e:
            error_message = e

        finished_at = datetime.datetime.utcnow()

        return ProcessHistory(
            started_at=started_at,
            duration_seconds=(finished_at - started_at).total_seconds(),
            method=process_request.method,
            url=process_request.url,
            data=process_request.data,
            status_code=status_code,
            request_headers=process_request.headers,
            request_body=process_request.data,
            response_headers=response_headers,
            response_body=response_body,
            error_message=str(error_message) if error_message else None,
        )

    def run(self, task_process: GumoTaskProcess) -> ProcessHistory:
        request = self._build_request(task_process=task_process)
        history = self._run_request(process_request=request)

        return history
