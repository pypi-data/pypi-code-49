"""
Main interface for stepfunctions service client paginators.

Usage::

    import boto3
    from mypy_boto3.stepfunctions import (
        GetExecutionHistoryPaginator,
        ListActivitiesPaginator,
        ListExecutionsPaginator,
        ListStateMachinesPaginator,
    )

    client: SFNClient = boto3.client("stepfunctions")

    get_execution_history_paginator: GetExecutionHistoryPaginator = client.get_paginator("get_execution_history")
    list_activities_paginator: ListActivitiesPaginator = client.get_paginator("list_activities")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_state_machines_paginator: ListStateMachinesPaginator = client.get_paginator("list_state_machines")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_stepfunctions.type_defs import (
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListStateMachinesPaginator",
)


class GetExecutionHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
    """

    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetExecutionHistoryOutputTypeDef, None, None]:
        """
        [GetExecutionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory.paginate)
        """


class ListActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListActivitiesOutputTypeDef, None, None]:
        """
        [ListActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListActivities.paginate)
        """


class ListExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
    """

    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListExecutionsOutputTypeDef, None, None]:
        """
        [ListExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions.paginate)
        """


class ListStateMachinesPaginator(Boto3Paginator):
    """
    [Paginator.ListStateMachines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStateMachinesOutputTypeDef, None, None]:
        """
        [ListStateMachines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines.paginate)
        """
