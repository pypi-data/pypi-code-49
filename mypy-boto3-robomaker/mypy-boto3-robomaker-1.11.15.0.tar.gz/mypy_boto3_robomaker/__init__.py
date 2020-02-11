"""
Main interface for robomaker service.

Usage::

    import boto3
    from mypy_boto3.robomaker import (
        Client,
        ListDeploymentJobsPaginator,
        ListFleetsPaginator,
        ListRobotApplicationsPaginator,
        ListRobotsPaginator,
        ListSimulationApplicationsPaginator,
        ListSimulationJobBatchesPaginator,
        ListSimulationJobsPaginator,
        RoboMakerClient,
        )

    session = boto3.Session()

    client: RoboMakerClient = boto3.client("robomaker")
    session_client: RoboMakerClient = session.client("robomaker")

    list_deployment_jobs_paginator: ListDeploymentJobsPaginator = client.get_paginator("list_deployment_jobs")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_robot_applications_paginator: ListRobotApplicationsPaginator = client.get_paginator("list_robot_applications")
    list_robots_paginator: ListRobotsPaginator = client.get_paginator("list_robots")
    list_simulation_applications_paginator: ListSimulationApplicationsPaginator = client.get_paginator("list_simulation_applications")
    list_simulation_job_batches_paginator: ListSimulationJobBatchesPaginator = client.get_paginator("list_simulation_job_batches")
    list_simulation_jobs_paginator: ListSimulationJobsPaginator = client.get_paginator("list_simulation_jobs")
"""
from mypy_boto3_robomaker.client import RoboMakerClient as Client, RoboMakerClient
from mypy_boto3_robomaker.paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobBatchesPaginator,
    ListSimulationJobsPaginator,
)


__all__ = (
    "Client",
    "ListDeploymentJobsPaginator",
    "ListFleetsPaginator",
    "ListRobotApplicationsPaginator",
    "ListRobotsPaginator",
    "ListSimulationApplicationsPaginator",
    "ListSimulationJobBatchesPaginator",
    "ListSimulationJobsPaginator",
    "RoboMakerClient",
)
