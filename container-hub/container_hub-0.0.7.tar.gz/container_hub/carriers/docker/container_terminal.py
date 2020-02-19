# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
import logging
from typing import List, Dict
from pathlib import Path

from docker import DockerClient
from docker.models.containers import Container
from docker.errors import DockerException
from docker.errors import APIError
from docker.errors import ContainerError
from docker.errors import NotFound
from docker.types import Mount

from container_hub.exceptions import CarrierError
from container_hub import settings

logger = logging.getLogger(__name__)

client = DockerClient(base_url=settings.CLIENT_URL)


def _list_containers(filters=None) -> List[Container]:
    return client.containers.list(filters=filters)


def container_list() -> List[str]:
    """
    Returns a list of simulation_ids
    """
    lc = _list_containers(filters={"label": "simulation_id"})
    return [x.name.lstrip("simulation-") for x in lc]


def container_hosts() -> Dict:
    return {}


def container_ips() -> Dict[str, str]:
    d = {}
    containers = _list_containers(filters={"label": "simulation_id"})
    for container in containers:
        try:
            ip_address = container.attrs["NetworkSettings"]["Networks"][
                settings.NETWORK_NAME
            ]["IPAddress"]
        except KeyError:
            continue
        d[container.name] = ip_address
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

    """
    Create container based on simulation and threedimodel.

    :returns the container id
    """
    name = f"simulation-{sim_uid}"
    result_path = Path(settings.BASE_RESULT_PATH, name)
    labels.update({"simulation_id": f"{sim_uid}"})

    _envs = [f"{key}={value}" for key, value in envs.items()]
    _envs.append(f"RESULT_PATH={result_path.as_posix()}")

    # Sentry environment variables for container
    if hasattr(settings, "SENTRY_DSN"):
        release = getattr(settings, "SENTRY_RELEASE", "")
        _envs += [f"SENTRY_DSN={settings.SENTRY_DSN}", f"RELEASE={release}"]

    if hasattr(settings, "CONTAINER_LOG_LEVEL"):
        _envs += [f"LOG_LEVEL={settings.CONTAINER_LOG_LEVEL}"]

    cmd = f"python service.py {settings.REDIS_HOST} {model_config} {sim_uid} {sim_ref_datetime} {end_time} {duration} {start_mode}"
    logger.debug("cmd %s", cmd)
    logger.debug("Envs %s", _envs)

    mounts = []
    for local_path, mount_setting in settings.DOCKER_MOUNT_POINTS.items():
        mounts.append(
            Mount(
                mount_setting["bind"],
                local_path,
                type="bind",
                read_only=mount_setting["ro"],
            )
        )

    client = DockerClient(base_url=settings.CLIENT_URL)

    try:
        container = client.containers.run(
            image=settings.IMAGE_NAME,
            command=cmd,
            name=name,
            network=settings.NETWORK_NAME,
            mounts=mounts,
            environment=_envs,
            detach=True,
            labels=labels,
        )
    except (DockerException, APIError, ContainerError) as err:
        logger.error(err)
        raise CarrierError(err)

    # double check everything went right
    try:
        client.containers.get(container.id)
    except (APIError, NotFound) as err:
        logger.error(
            f"simulation container exited prematurely. Could not retrieve "
            f"the container if though it should be running {err}"
        )
        raise CarrierError(err)

    logger.info(f"Started simulation container {container.name}")
    return container.id


def down(sim_uid: str):

    try:
        container = client.containers.get(f"simulation-{sim_uid}")
        container_id = container.id
    except (APIError, NotFound) as err:
        logger.error(
            f"Could not get the simulation container, error message: {err}"
        )
        raise CarrierError(err)
    try:
        if settings.DEBUG is False:
            container.remove(force=True)
        else:
            container.kill()
    except APIError as err:
        logger.error(
            f"Could not kill/remove the "
            f"simulation container, error message: {err}"
        )
        raise CarrierError(err)
    logger.info(f"Removed container for simulation {sim_uid}")
    return container_id
