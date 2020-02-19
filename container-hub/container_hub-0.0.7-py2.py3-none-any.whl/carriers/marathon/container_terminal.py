# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from typing import Dict, List
from typing import Iterator
from typing import Tuple
import marathon.exceptions
from marathon import MarathonApp
from marathon.models.app import MarathonTask
from marathon.models.container import MarathonContainer
from marathon.models.container import MarathonContainerVolume
from marathon.models.container import MarathonDockerContainer
from marathon.models.constraint import MarathonConstraint
from marathon import MarathonClient

from container_hub.exceptions import CarrierError
from container_hub import settings

logger = logging.getLogger(__name__)

client = MarathonClient(settings.CLIENT_URL)


class MachineManagerException(Exception):
    pass


def container_list() -> List[str]:
    sim_uids = []
    apps = client.list_apps()
    for app in apps:
        # v3 apps all have a simulation id label
        sim_uid = app.labels.get("simulation_id")
        if not sim_uid:
            continue
        sim_uids.append(sim_uid)
    return sim_uids


def _task_generator() -> Iterator[Tuple[MarathonTask, str]]:
    tasks = client.list_tasks()
    for task in tasks:
        app_name = task.app_id.strip("/")
        yield task, app_name


def container_hosts() -> Dict[str, str]:
    d = {}
    for task, app_name in _task_generator():
        d[app_name] = task.host
    return d


def container_ips() -> Dict[str, str]:
    d = {}
    for task, app_name in _task_generator():
        _ip = task.ip_addresses[0]
        d[app_name] = _ip.ip_address
    return d


def up(
    sim_uid: str,
    sim_ref_datetime: str,
    end_time: int,
    duration: int,
    start_mode: str,
    model_config: str,
    session_memory: int,
    envs: Dict,
    labels: Dict,
) -> str:

    """Create a MarathonApp instance."""
    image = settings.IMAGE_NAME
    name = f"simulation-{sim_uid}"
    labels.update({"simulation_id": f"{sim_uid}"})

    docker_container = MarathonDockerContainer(
        image=image,
        network="BRIDGE",
        parameters=[{"key": "network", "value": settings.NETWORK_NAME}],
    )

    volumes = []  # == mounts

    for local_path, mount_setting in settings.DOCKER_MOUNT_POINTS.items():
        volumes.append(
            MarathonContainerVolume(
                container_path=mount_setting["bind"],
                host_path=local_path,
                mode="RO" if mount_setting["ro"] else "RW",
            )
        )

    logger.debug("Volumes %s", volumes)

    # docker container with volumes
    container = MarathonContainer(docker=docker_container, volumes=volumes)
    result_path = Path(settings.BASE_RESULT_PATH, name)
    # environment variables for container
    envs.update({"RESULT_PATH": result_path.as_posix()})

    # Sentry environment variables for container
    if hasattr(settings, "SENTRY_DSN"):
        envs.update(
            {
                "SENTRY_DSN": settings.SENTRY_DSN,
                "RELEASE": getattr(settings, "SENTRY_RELEASE", ""),
            }
        )

    if hasattr(settings, "CONTAINER_LOG_LEVEL"):
        envs.update({"LOG_LEVEL": settings.CONTAINER_LOG_LEVEL})

    constraints = []

    if hasattr(settings, "MARATHON_CONSTRAINTS"):
        constraints = [
            MarathonConstraint(param, operator, value)
            for param, operator, value in settings.MARATHON_CONSTRAINTS
        ]

    args = [
        "python",
        "service.py",
        settings.REDIS_HOST,
        model_config,
        sim_uid,
        sim_ref_datetime,
        end_time,
        duration,
        start_mode,
    ]

    marathon_app_definition = MarathonApp(
        args=args,
        container=container,
        mem=session_memory,
        cpus=settings.CONTAINER_CPUS,
        env=envs,
        labels=labels,
        constraints=constraints,
    )

    try:
        app = client.create_app(name, marathon_app_definition)
    except marathon.exceptions.MarathonHttpError as err:
        logger.exception("Failed to create app %s with error %s", name, err)
        raise CarrierError(err)
    logger.info(f"App {app.id} started")
    return app.id


def _del_app(app_name: str) -> bool:
    """
    wrapper around the ``client.delete_app`` call

    :returns True if the app has been deleted, False otherwise
    """
    try:
        client.delete_app(app_name, force=True)
    except marathon.exceptions.NotFoundError:
        # not found; assume that the app is deleted
        logger.exception("Failed to delete app %s.", app_name)
        return False
    return True


def down(sim_uid: str):
    """Remove the given app."""

    app_name = f"simulation-{sim_uid}"

    # should return a single marathon.models.app.MarathonApp instance
    apps = client.list_apps(app_id=app_name)
    if not apps:
        logger.warning(
            "App not found; assuming that the app has already been deleted"
        )
        return

    if len(apps) > 1:
        msg = (
            f"Found more than one app that matches the name {app_name}. "
            f"Trying to delete all of them now..."
        )
        logger.warning(msg)
        for app in apps:
            _del_app(app.id)
        return

    app = apps[0]
    if _del_app(app.id):
        logger.info("Deleted app %s.", app_name)
