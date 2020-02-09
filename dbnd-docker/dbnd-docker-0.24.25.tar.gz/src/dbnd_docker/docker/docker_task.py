from __future__ import absolute_import

import logging

from dbnd import parameter
from dbnd._core.configuration.config_path import from_task_env
from dbnd.tasks import Task
from dbnd_docker.container_engine_config import ContainerEngineConfig
from dbnd_docker.docker_ctrl import DockerRunCtrl


logger = logging.getLogger(__name__)


class DockerRunTask(Task):
    # _conf__task_family = "docker_cmd"

    image = parameter(
        description="Docker image from which to create the container."
        "If image tag is omitted, 'latest' will be used."
    )[str]
    command = parameter(description="Command to be run in the container. (templated)")[
        str
    ]

    docker_engine = parameter(config_path=from_task_env("docker_engine"))[
        ContainerEngineConfig
    ]

    docker_ctrl = None  # type: DockerRunCtrl

    def _task_submit(self):
        if hasattr(self.ctrl, "airflow_op"):
            airflow_context = self.current_task_run.airflow_context
            self.command = self.ctrl.airflow_op.render_template(
                self.command, airflow_context
            )

        self.log_metric("docker command", self.command)
        self.docker_ctrl = self.docker_engine.get_docker_ctrl(
            self.current_task_run
        )  # type: DockerRunCtrl
        self.docker_ctrl.docker_run()

    def _should_resubmit(self, task_run):
        """
        We don't want to resubmit if it's dockerized run and we running with the same engine
        """
        if self.docker_engine.task_name == task_run.task_engine.task_name:
            return False
        super(DockerRunTask, self)._should_resubmit(task_run)

    def on_kill(self):
        if self.docker_ctrl is not None:
            logger.error("Killing submitted docker for %s", self.task_id)
            return self.docker_ctrl.on_kill()
