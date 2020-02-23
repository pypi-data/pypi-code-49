from logging import getLogger
import flask.views

from gumo.core.injector import injector

from gumo.task_emulator.application.task.repository import TaskProcessSummaryRepository
from gumo.task_emulator.application.task.repository import TaskProcessRepository

logger = getLogger(__name__)
emulator_ui_blueprint = flask.Blueprint('task-emulator-ui', __name__, template_folder='template')


class QueueUI(flask.views.MethodView):
    _repository = injector.get(TaskProcessSummaryRepository)  # type: TaskProcessSummaryRepository

    def get(self):
        summary = self._repository.fetch_summary()

        return flask.render_template(
            'index.html',
            summary=summary.to_dict(),
        )


class QueueDetailUI(flask.views.MethodView):
    _repository = injector.get(TaskProcessRepository)  # type: TaskProcessRepository

    def get(self, queue_name):
        tasks = self._repository.fetch_tasks(queue_name=queue_name, limit=100)

        return flask.render_template(
            'detail.html',
            queue_name=queue_name,
            tasks=tasks
        )


emulator_ui_blueprint.add_url_rule(
    '/task_emulator/dashboard',
    view_func=QueueUI.as_view(name='dashboard'),
    methods=['GET']
)

emulator_ui_blueprint.add_url_rule(
    '/task_emulator/detail/<queue_name>',
    view_func=QueueDetailUI.as_view(name='dashboard/queue-detail'),
    methods=['GET']
)
