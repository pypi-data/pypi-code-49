"""
Main interface for stepfunctions service.

Usage::

    import boto3
    from mypy_boto3.stepfunctions import (
        Client,
        GetExecutionHistoryPaginator,
        ListActivitiesPaginator,
        ListExecutionsPaginator,
        ListStateMachinesPaginator,
        SFNClient,
        )

    session = boto3.Session()

    client: SFNClient = boto3.client("stepfunctions")
    session_client: SFNClient = session.client("stepfunctions")

    get_execution_history_paginator: GetExecutionHistoryPaginator = client.get_paginator("get_execution_history")
    list_activities_paginator: ListActivitiesPaginator = client.get_paginator("list_activities")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_state_machines_paginator: ListStateMachinesPaginator = client.get_paginator("list_state_machines")
"""
from mypy_boto3_stepfunctions.client import SFNClient as Client, SFNClient
from mypy_boto3_stepfunctions.paginator import (
    GetExecutionHistoryPaginator,
    ListActivitiesPaginator,
    ListExecutionsPaginator,
    ListStateMachinesPaginator,
)


__all__ = (
    "Client",
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListStateMachinesPaginator",
    "SFNClient",
)
