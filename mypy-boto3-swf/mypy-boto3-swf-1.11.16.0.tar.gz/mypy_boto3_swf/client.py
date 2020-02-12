"""
Main interface for swf service client

Usage::

    import boto3
    from mypy_boto3.swf import SWFClient

    session = boto3.Session()

    client: SWFClient = boto3.client("swf")
    session_client: SWFClient = session.client("swf")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_swf.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_swf.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_swf.type_defs import (
    ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef,
    ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef,
    ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef,
    ClientCountClosedWorkflowExecutionsResponseTypeDef,
    ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef,
    ClientCountClosedWorkflowExecutionsTagFilterTypeDef,
    ClientCountClosedWorkflowExecutionsTypeFilterTypeDef,
    ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef,
    ClientCountOpenWorkflowExecutionsResponseTypeDef,
    ClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef,
    ClientCountOpenWorkflowExecutionsTagFilterTypeDef,
    ClientCountOpenWorkflowExecutionsTypeFilterTypeDef,
    ClientCountPendingActivityTasksResponseTypeDef,
    ClientCountPendingActivityTasksTaskListTypeDef,
    ClientCountPendingDecisionTasksResponseTypeDef,
    ClientCountPendingDecisionTasksTaskListTypeDef,
    ClientDeprecateActivityTypeActivityTypeTypeDef,
    ClientDeprecateWorkflowTypeWorkflowTypeTypeDef,
    ClientDescribeActivityTypeActivityTypeTypeDef,
    ClientDescribeActivityTypeResponseTypeDef,
    ClientDescribeDomainResponseTypeDef,
    ClientDescribeWorkflowExecutionExecutionTypeDef,
    ClientDescribeWorkflowExecutionResponseTypeDef,
    ClientDescribeWorkflowTypeResponseTypeDef,
    ClientDescribeWorkflowTypeWorkflowTypeTypeDef,
    ClientGetWorkflowExecutionHistoryExecutionTypeDef,
    ClientGetWorkflowExecutionHistoryResponseTypeDef,
    ClientListActivityTypesResponseTypeDef,
    ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef,
    ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef,
    ClientListClosedWorkflowExecutionsExecutionFilterTypeDef,
    ClientListClosedWorkflowExecutionsResponseTypeDef,
    ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef,
    ClientListClosedWorkflowExecutionsTagFilterTypeDef,
    ClientListClosedWorkflowExecutionsTypeFilterTypeDef,
    ClientListDomainsResponseTypeDef,
    ClientListOpenWorkflowExecutionsExecutionFilterTypeDef,
    ClientListOpenWorkflowExecutionsResponseTypeDef,
    ClientListOpenWorkflowExecutionsStartTimeFilterTypeDef,
    ClientListOpenWorkflowExecutionsTagFilterTypeDef,
    ClientListOpenWorkflowExecutionsTypeFilterTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWorkflowTypesResponseTypeDef,
    ClientPollForActivityTaskResponseTypeDef,
    ClientPollForActivityTaskTaskListTypeDef,
    ClientPollForDecisionTaskResponseTypeDef,
    ClientPollForDecisionTaskTaskListTypeDef,
    ClientRecordActivityTaskHeartbeatResponseTypeDef,
    ClientRegisterActivityTypeDefaultTaskListTypeDef,
    ClientRegisterDomainTagsTypeDef,
    ClientRegisterWorkflowTypeDefaultTaskListTypeDef,
    ClientRespondDecisionTaskCompletedDecisionsTypeDef,
    ClientStartWorkflowExecutionResponseTypeDef,
    ClientStartWorkflowExecutionTaskListTypeDef,
    ClientStartWorkflowExecutionWorkflowTypeTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUndeprecateActivityTypeActivityTypeTypeDef,
    ClientUndeprecateWorkflowTypeWorkflowTypeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SWFClient",)


class SWFClient:
    """
    [SWF.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.can_paginate)
        """

    def count_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef = None,
        closeTimeFilter: ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef = None,
        executionFilter: ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef = None,
        typeFilter: ClientCountClosedWorkflowExecutionsTypeFilterTypeDef = None,
        tagFilter: ClientCountClosedWorkflowExecutionsTagFilterTypeDef = None,
        closeStatusFilter: ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef = None,
    ) -> ClientCountClosedWorkflowExecutionsResponseTypeDef:
        """
        [Client.count_closed_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.count_closed_workflow_executions)
        """

    def count_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef,
        typeFilter: ClientCountOpenWorkflowExecutionsTypeFilterTypeDef = None,
        tagFilter: ClientCountOpenWorkflowExecutionsTagFilterTypeDef = None,
        executionFilter: ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef = None,
    ) -> ClientCountOpenWorkflowExecutionsResponseTypeDef:
        """
        [Client.count_open_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.count_open_workflow_executions)
        """

    def count_pending_activity_tasks(
        self, domain: str, taskList: ClientCountPendingActivityTasksTaskListTypeDef
    ) -> ClientCountPendingActivityTasksResponseTypeDef:
        """
        [Client.count_pending_activity_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.count_pending_activity_tasks)
        """

    def count_pending_decision_tasks(
        self, domain: str, taskList: ClientCountPendingDecisionTasksTaskListTypeDef
    ) -> ClientCountPendingDecisionTasksResponseTypeDef:
        """
        [Client.count_pending_decision_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.count_pending_decision_tasks)
        """

    def deprecate_activity_type(
        self, domain: str, activityType: ClientDeprecateActivityTypeActivityTypeTypeDef
    ) -> None:
        """
        [Client.deprecate_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.deprecate_activity_type)
        """

    def deprecate_domain(self, name: str) -> None:
        """
        [Client.deprecate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.deprecate_domain)
        """

    def deprecate_workflow_type(
        self, domain: str, workflowType: ClientDeprecateWorkflowTypeWorkflowTypeTypeDef
    ) -> None:
        """
        [Client.deprecate_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.deprecate_workflow_type)
        """

    def describe_activity_type(
        self, domain: str, activityType: ClientDescribeActivityTypeActivityTypeTypeDef
    ) -> ClientDescribeActivityTypeResponseTypeDef:
        """
        [Client.describe_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.describe_activity_type)
        """

    def describe_domain(self, name: str) -> ClientDescribeDomainResponseTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.describe_domain)
        """

    def describe_workflow_execution(
        self, domain: str, execution: ClientDescribeWorkflowExecutionExecutionTypeDef
    ) -> ClientDescribeWorkflowExecutionResponseTypeDef:
        """
        [Client.describe_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.describe_workflow_execution)
        """

    def describe_workflow_type(
        self, domain: str, workflowType: ClientDescribeWorkflowTypeWorkflowTypeTypeDef
    ) -> ClientDescribeWorkflowTypeResponseTypeDef:
        """
        [Client.describe_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.describe_workflow_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.generate_presigned_url)
        """

    def get_workflow_execution_history(
        self,
        domain: str,
        execution: ClientGetWorkflowExecutionHistoryExecutionTypeDef,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ClientGetWorkflowExecutionHistoryResponseTypeDef:
        """
        [Client.get_workflow_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.get_workflow_execution_history)
        """

    def list_activity_types(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ClientListActivityTypesResponseTypeDef:
        """
        [Client.list_activity_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.list_activity_types)
        """

    def list_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef = None,
        closeTimeFilter: ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef = None,
        executionFilter: ClientListClosedWorkflowExecutionsExecutionFilterTypeDef = None,
        closeStatusFilter: ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef = None,
        typeFilter: ClientListClosedWorkflowExecutionsTypeFilterTypeDef = None,
        tagFilter: ClientListClosedWorkflowExecutionsTagFilterTypeDef = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ClientListClosedWorkflowExecutionsResponseTypeDef:
        """
        [Client.list_closed_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.list_closed_workflow_executions)
        """

    def list_domains(
        self,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ClientListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.list_domains)
        """

    def list_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ClientListOpenWorkflowExecutionsStartTimeFilterTypeDef,
        typeFilter: ClientListOpenWorkflowExecutionsTypeFilterTypeDef = None,
        tagFilter: ClientListOpenWorkflowExecutionsTagFilterTypeDef = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
        executionFilter: ClientListOpenWorkflowExecutionsExecutionFilterTypeDef = None,
    ) -> ClientListOpenWorkflowExecutionsResponseTypeDef:
        """
        [Client.list_open_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.list_open_workflow_executions)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.list_tags_for_resource)
        """

    def list_workflow_types(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ClientListWorkflowTypesResponseTypeDef:
        """
        [Client.list_workflow_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.list_workflow_types)
        """

    def poll_for_activity_task(
        self, domain: str, taskList: ClientPollForActivityTaskTaskListTypeDef, identity: str = None
    ) -> ClientPollForActivityTaskResponseTypeDef:
        """
        [Client.poll_for_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.poll_for_activity_task)
        """

    def poll_for_decision_task(
        self,
        domain: str,
        taskList: ClientPollForDecisionTaskTaskListTypeDef,
        identity: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ClientPollForDecisionTaskResponseTypeDef:
        """
        [Client.poll_for_decision_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.poll_for_decision_task)
        """

    def record_activity_task_heartbeat(
        self, taskToken: str, details: str = None
    ) -> ClientRecordActivityTaskHeartbeatResponseTypeDef:
        """
        [Client.record_activity_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.record_activity_task_heartbeat)
        """

    def register_activity_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultTaskHeartbeatTimeout: str = None,
        defaultTaskList: ClientRegisterActivityTypeDefaultTaskListTypeDef = None,
        defaultTaskPriority: str = None,
        defaultTaskScheduleToStartTimeout: str = None,
        defaultTaskScheduleToCloseTimeout: str = None,
    ) -> None:
        """
        [Client.register_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.register_activity_type)
        """

    def register_domain(
        self,
        name: str,
        workflowExecutionRetentionPeriodInDays: str,
        description: str = None,
        tags: List[ClientRegisterDomainTagsTypeDef] = None,
    ) -> None:
        """
        [Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.register_domain)
        """

    def register_workflow_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultExecutionStartToCloseTimeout: str = None,
        defaultTaskList: ClientRegisterWorkflowTypeDefaultTaskListTypeDef = None,
        defaultTaskPriority: str = None,
        defaultChildPolicy: Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"] = None,
        defaultLambdaRole: str = None,
    ) -> None:
        """
        [Client.register_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.register_workflow_type)
        """

    def request_cancel_workflow_execution(
        self, domain: str, workflowId: str, runId: str = None
    ) -> None:
        """
        [Client.request_cancel_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.request_cancel_workflow_execution)
        """

    def respond_activity_task_canceled(self, taskToken: str, details: str = None) -> None:
        """
        [Client.respond_activity_task_canceled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.respond_activity_task_canceled)
        """

    def respond_activity_task_completed(self, taskToken: str, result: str = None) -> None:
        """
        [Client.respond_activity_task_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.respond_activity_task_completed)
        """

    def respond_activity_task_failed(
        self, taskToken: str, reason: str = None, details: str = None
    ) -> None:
        """
        [Client.respond_activity_task_failed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.respond_activity_task_failed)
        """

    def respond_decision_task_completed(
        self,
        taskToken: str,
        decisions: List[ClientRespondDecisionTaskCompletedDecisionsTypeDef] = None,
        executionContext: str = None,
    ) -> None:
        """
        [Client.respond_decision_task_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.respond_decision_task_completed)
        """

    def signal_workflow_execution(
        self, domain: str, workflowId: str, signalName: str, runId: str = None, input: str = None
    ) -> None:
        """
        [Client.signal_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.signal_workflow_execution)
        """

    def start_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        workflowType: ClientStartWorkflowExecutionWorkflowTypeTypeDef,
        taskList: ClientStartWorkflowExecutionTaskListTypeDef = None,
        taskPriority: str = None,
        input: str = None,
        executionStartToCloseTimeout: str = None,
        tagList: List[str] = None,
        taskStartToCloseTimeout: str = None,
        childPolicy: Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"] = None,
        lambdaRole: str = None,
    ) -> ClientStartWorkflowExecutionResponseTypeDef:
        """
        [Client.start_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.start_workflow_execution)
        """

    def tag_resource(self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.tag_resource)
        """

    def terminate_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        runId: str = None,
        reason: str = None,
        details: str = None,
        childPolicy: Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"] = None,
    ) -> None:
        """
        [Client.terminate_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.terminate_workflow_execution)
        """

    def undeprecate_activity_type(
        self, domain: str, activityType: ClientUndeprecateActivityTypeActivityTypeTypeDef
    ) -> None:
        """
        [Client.undeprecate_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.undeprecate_activity_type)
        """

    def undeprecate_domain(self, name: str) -> None:
        """
        [Client.undeprecate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.undeprecate_domain)
        """

    def undeprecate_workflow_type(
        self, domain: str, workflowType: ClientUndeprecateWorkflowTypeWorkflowTypeTypeDef
    ) -> None:
        """
        [Client.undeprecate_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.undeprecate_workflow_type)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_workflow_execution_history"]
    ) -> "paginator_scope.GetWorkflowExecutionHistoryPaginator":
        """
        [Paginator.GetWorkflowExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_activity_types"]
    ) -> "paginator_scope.ListActivityTypesPaginator":
        """
        [Paginator.ListActivityTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.ListActivityTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_closed_workflow_executions"]
    ) -> "paginator_scope.ListClosedWorkflowExecutionsPaginator":
        """
        [Paginator.ListClosedWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domains"]
    ) -> "paginator_scope.ListDomainsPaginator":
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.ListDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_open_workflow_executions"]
    ) -> "paginator_scope.ListOpenWorkflowExecutionsPaginator":
        """
        [Paginator.ListOpenWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_types"]
    ) -> "paginator_scope.ListWorkflowTypesPaginator":
        """
        [Paginator.ListWorkflowTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["poll_for_decision_task"]
    ) -> "paginator_scope.PollForDecisionTaskPaginator":
        """
        [Paginator.PollForDecisionTask documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DefaultUndefinedFault: Boto3ClientError
    DomainAlreadyExistsFault: Boto3ClientError
    DomainDeprecatedFault: Boto3ClientError
    LimitExceededFault: Boto3ClientError
    OperationNotPermittedFault: Boto3ClientError
    TooManyTagsFault: Boto3ClientError
    TypeAlreadyExistsFault: Boto3ClientError
    TypeDeprecatedFault: Boto3ClientError
    UnknownResourceFault: Boto3ClientError
    WorkflowExecutionAlreadyStartedFault: Boto3ClientError
