"""
Main interface for stepfunctions service client

Usage::

    import boto3
    from mypy_boto3.stepfunctions import SFNClient

    session = boto3.Session()

    client: SFNClient = boto3.client("stepfunctions")
    session_client: SFNClient = session.client("stepfunctions")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_stepfunctions.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_stepfunctions.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_stepfunctions.type_defs import (
    ClientCreateActivityResponseTypeDef,
    ClientCreateActivityTagsTypeDef,
    ClientCreateStateMachineLoggingConfigurationTypeDef,
    ClientCreateStateMachineResponseTypeDef,
    ClientCreateStateMachineTagsTypeDef,
    ClientDescribeActivityResponseTypeDef,
    ClientDescribeExecutionResponseTypeDef,
    ClientDescribeStateMachineForExecutionResponseTypeDef,
    ClientDescribeStateMachineResponseTypeDef,
    ClientGetActivityTaskResponseTypeDef,
    ClientGetExecutionHistoryResponseTypeDef,
    ClientListActivitiesResponseTypeDef,
    ClientListExecutionsResponseTypeDef,
    ClientListStateMachinesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientStartExecutionResponseTypeDef,
    ClientStopExecutionResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateStateMachineLoggingConfigurationTypeDef,
    ClientUpdateStateMachineResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SFNClient",)


class SFNClient:
    """
    [SFN.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.can_paginate)
        """

    def create_activity(
        self, name: str, tags: List[ClientCreateActivityTagsTypeDef] = None
    ) -> ClientCreateActivityResponseTypeDef:
        """
        [Client.create_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.create_activity)
        """

    def create_state_machine(
        self,
        name: str,
        definition: str,
        roleArn: str,
        type: Literal["STANDARD", "EXPRESS"] = None,
        loggingConfiguration: ClientCreateStateMachineLoggingConfigurationTypeDef = None,
        tags: List[ClientCreateStateMachineTagsTypeDef] = None,
    ) -> ClientCreateStateMachineResponseTypeDef:
        """
        [Client.create_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.create_state_machine)
        """

    def delete_activity(self, activityArn: str) -> Dict[str, Any]:
        """
        [Client.delete_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.delete_activity)
        """

    def delete_state_machine(self, stateMachineArn: str) -> Dict[str, Any]:
        """
        [Client.delete_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)
        """

    def describe_activity(self, activityArn: str) -> ClientDescribeActivityResponseTypeDef:
        """
        [Client.describe_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.describe_activity)
        """

    def describe_execution(self, executionArn: str) -> ClientDescribeExecutionResponseTypeDef:
        """
        [Client.describe_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.describe_execution)
        """

    def describe_state_machine(
        self, stateMachineArn: str
    ) -> ClientDescribeStateMachineResponseTypeDef:
        """
        [Client.describe_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)
        """

    def describe_state_machine_for_execution(
        self, executionArn: str
    ) -> ClientDescribeStateMachineForExecutionResponseTypeDef:
        """
        [Client.describe_state_machine_for_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)
        """

    def get_activity_task(
        self, activityArn: str, workerName: str = None
    ) -> ClientGetActivityTaskResponseTypeDef:
        """
        [Client.get_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.get_activity_task)
        """

    def get_execution_history(
        self,
        executionArn: str,
        maxResults: int = None,
        reverseOrder: bool = None,
        nextToken: str = None,
    ) -> ClientGetExecutionHistoryResponseTypeDef:
        """
        [Client.get_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.get_execution_history)
        """

    def list_activities(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListActivitiesResponseTypeDef:
        """
        [Client.list_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.list_activities)
        """

    def list_executions(
        self,
        stateMachineArn: str,
        statusFilter: Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListExecutionsResponseTypeDef:
        """
        [Client.list_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.list_executions)
        """

    def list_state_machines(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListStateMachinesResponseTypeDef:
        """
        [Client.list_state_machines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.list_state_machines)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)
        """

    def send_task_failure(
        self, taskToken: str, error: str = None, cause: str = None
    ) -> Dict[str, Any]:
        """
        [Client.send_task_failure documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.send_task_failure)
        """

    def send_task_heartbeat(self, taskToken: str) -> Dict[str, Any]:
        """
        [Client.send_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)
        """

    def send_task_success(self, taskToken: str, output: str) -> Dict[str, Any]:
        """
        [Client.send_task_success documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.send_task_success)
        """

    def start_execution(
        self, stateMachineArn: str, name: str = None, input: str = None
    ) -> ClientStartExecutionResponseTypeDef:
        """
        [Client.start_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.start_execution)
        """

    def stop_execution(
        self, executionArn: str, error: str = None, cause: str = None
    ) -> ClientStopExecutionResponseTypeDef:
        """
        [Client.stop_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.stop_execution)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.untag_resource)
        """

    def update_state_machine(
        self,
        stateMachineArn: str,
        definition: str = None,
        roleArn: str = None,
        loggingConfiguration: ClientUpdateStateMachineLoggingConfigurationTypeDef = None,
    ) -> ClientUpdateStateMachineResponseTypeDef:
        """
        [Client.update_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Client.update_state_machine)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_execution_history"]
    ) -> "paginator_scope.GetExecutionHistoryPaginator":
        """
        [Paginator.GetExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_activities"]
    ) -> "paginator_scope.ListActivitiesPaginator":
        """
        [Paginator.ListActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_executions"]
    ) -> "paginator_scope.ListExecutionsPaginator":
        """
        [Paginator.ListExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_state_machines"]
    ) -> "paginator_scope.ListStateMachinesPaginator":
        """
        [Paginator.ListStateMachines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
        """


class Exceptions:
    ActivityDoesNotExist: Boto3ClientError
    ActivityLimitExceeded: Boto3ClientError
    ActivityWorkerLimitExceeded: Boto3ClientError
    ClientError: Boto3ClientError
    ExecutionAlreadyExists: Boto3ClientError
    ExecutionDoesNotExist: Boto3ClientError
    ExecutionLimitExceeded: Boto3ClientError
    InvalidArn: Boto3ClientError
    InvalidDefinition: Boto3ClientError
    InvalidExecutionInput: Boto3ClientError
    InvalidLoggingConfiguration: Boto3ClientError
    InvalidName: Boto3ClientError
    InvalidOutput: Boto3ClientError
    InvalidToken: Boto3ClientError
    MissingRequiredParameter: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    StateMachineAlreadyExists: Boto3ClientError
    StateMachineDeleting: Boto3ClientError
    StateMachineDoesNotExist: Boto3ClientError
    StateMachineLimitExceeded: Boto3ClientError
    StateMachineTypeNotSupported: Boto3ClientError
    TaskDoesNotExist: Boto3ClientError
    TaskTimedOut: Boto3ClientError
    TooManyTags: Boto3ClientError
