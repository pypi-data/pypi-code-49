from logging import getLogger
import flask.views

from gumo.core.injector import injector

from gumo.core import EntityKeyFactory

from gumo.task_emulator.application import TaskExecuteService
from gumo.task_emulator.application import TaskMarkAsFailedService
from gumo.task_emulator.application.task import TaskProcessBulkCreateService
from gumo.task_emulator.application.task.encoder import TaskJSONEncoder
from gumo.task_emulator.application.task.encoder import TaskProcessJSONEncoder
from gumo.task_emulator.application.task.repository import TaskRepository
from gumo.task_emulator.application.task.repository import TaskProcessRepository
from gumo.task_emulator.application.task.repository import TaskProcessSummaryRepository
from gumo.task_emulator.domain import TaskState

logger = getLogger(__name__)
emulator_api_blueprint = flask.Blueprint('task-emulator', __name__)


class TasksView(flask.views.MethodView):
    _repository = injector.get(TaskRepository)  # type: TaskRepository

    def get(self):
        tasks = self._repository.fetch_tasks(limit=100)

        return flask.jsonify({
            'results': [TaskJSONEncoder(task).to_json() for task in tasks]
        })

    def post(self):
        return 'ok'


class TaskDetailView(flask.views.MethodView):
    _repository = injector.get(TaskProcessRepository)  # type: TaskProcessRepository

    def get(self, key):
        task = self._repository.fetch_by_key(
            key=EntityKeyFactory().build_from_key_path(key)
        )

        return flask.jsonify(TaskProcessJSONEncoder(task).to_json())


class TasksEmulatorEnqueue(flask.views.MethodView):
    _task_process_create_service = injector.get(TaskProcessBulkCreateService)  # type: TaskProcessBulkCreateService

    def get(self):
        result = self._task_process_create_service.execute()
        return flask.jsonify(result)

    def post(self):
        result = self._task_process_create_service.execute()
        return flask.jsonify(result)


class TaskProcessesView(flask.views.MethodView):
    _repository = injector.get(TaskProcessRepository)  # type: TaskProcessRepository

    def get(self):
        task_processes = self._repository.fetch_tasks()

        return flask.jsonify({
            'tasks': [
                TaskProcessJSONEncoder(task_process=task_process).to_json()
                for task_process in task_processes
            ]
        })


class TaskSummaryView(flask.views.MethodView):
    _repository = injector.get(TaskProcessSummaryRepository)  # type: TaskProcessSummaryRepository

    def get(self):
        summary = self._repository.fetch_summary()

        return flask.jsonify({
            'summary': summary.to_dict(),
        })


class QueuedTasksView(flask.views.MethodView):
    _repository = injector.get(TaskProcessRepository)  # type: TaskProcessRepository

    def get(self):
        task_processes = self._repository.fetch_tasks_by_state(state=TaskState.QUEUED)

        return flask.jsonify({
            'tasks': [
                TaskProcessJSONEncoder(task_process).to_json()
                for task_process in task_processes
            ]
        })


class ExecuteTaskView(flask.views.MethodView):
    _service = injector.get(TaskExecuteService)  # type: TaskExecuteService

    def get(self, key):
        result = self._service.execute(key=EntityKeyFactory().build_from_key_path(key_path=key))
        return flask.jsonify(result.to_json())


class TaskRemoveView(flask.views.MethodView):
    _service = injector.get(TaskMarkAsFailedService)  # type: TaskMarkAsFailedService

    def get(self, key):
        task = self._service.execute(
            key=EntityKeyFactory().build_from_key_path(key)
        )

        return flask.jsonify(TaskProcessJSONEncoder(task).to_json())


class TaskCleanupView(flask.views.MethodView):
    _repository = injector.get(TaskProcessRepository)  # type: TaskProcessRepository

    def get(self):
        self._repository.cleanup_finished_tasks()

        return flask.jsonify({'cleanup': 'ok'})


emulator_api_blueprint.add_url_rule(
    '/api/tasks',
    view_func=TasksView.as_view(name='tasks'),
    methods=['GET', 'POST']
)

emulator_api_blueprint.add_url_rule(
    '/api/tasks/<key>',
    view_func=TaskDetailView.as_view(name='tasks/detail'),
    methods=['GET']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/enqueue',
    view_func=TasksEmulatorEnqueue.as_view(name='task_emulator/enqueue'),
    methods=['GET', 'POST']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/tasks',
    view_func=TaskProcessesView.as_view(name='task_emulator/tasks'),
    methods=['GET']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/tasks/summary',
    view_func=TaskSummaryView.as_view(name='task_emulator/tasks/summary'),
    methods=['GET']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/tasks/queued',
    view_func=QueuedTasksView.as_view(name='task_emulator/tasks/queued'),
    methods=['GET']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/tasks/<key>/execute',
    view_func=ExecuteTaskView.as_view(name='task_emulator/tasks/execute'),
    methods=['GET']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/tasks/<key>/remove',
    view_func=TaskRemoveView.as_view(name='task_emulator/tasks/remove'),
    methods=['GET']
)

emulator_api_blueprint.add_url_rule(
    '/api/task_emulator/cleanup',
    view_func=TaskCleanupView.as_view(name='task_emulator/cleanup'),
    methods=['GET']
)
