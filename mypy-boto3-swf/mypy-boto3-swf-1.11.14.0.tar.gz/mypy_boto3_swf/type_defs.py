"""
Main interface for swf service type definitions.

Usage::

    from mypy_boto3.swf.type_defs import ActivityTypeTypeDef

    data: ActivityTypeTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityTypeTypeDef",
    "ActivityTypeInfoTypeDef",
    "ActivityTypeInfosTypeDef",
    "ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef",
    "ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef",
    "ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef",
    "ClientCountClosedWorkflowExecutionsResponseTypeDef",
    "ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef",
    "ClientCountClosedWorkflowExecutionsTagFilterTypeDef",
    "ClientCountClosedWorkflowExecutionsTypeFilterTypeDef",
    "ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef",
    "ClientCountOpenWorkflowExecutionsResponseTypeDef",
    "ClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef",
    "ClientCountOpenWorkflowExecutionsTagFilterTypeDef",
    "ClientCountOpenWorkflowExecutionsTypeFilterTypeDef",
    "ClientCountPendingActivityTasksResponseTypeDef",
    "ClientCountPendingActivityTasksTaskListTypeDef",
    "ClientCountPendingDecisionTasksResponseTypeDef",
    "ClientCountPendingDecisionTasksTaskListTypeDef",
    "ClientDeprecateActivityTypeActivityTypeTypeDef",
    "ClientDeprecateWorkflowTypeWorkflowTypeTypeDef",
    "ClientDescribeActivityTypeActivityTypeTypeDef",
    "ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef",
    "ClientDescribeActivityTypeResponseconfigurationTypeDef",
    "ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef",
    "ClientDescribeActivityTypeResponsetypeInfoTypeDef",
    "ClientDescribeActivityTypeResponseTypeDef",
    "ClientDescribeDomainResponseconfigurationTypeDef",
    "ClientDescribeDomainResponsedomainInfoTypeDef",
    "ClientDescribeDomainResponseTypeDef",
    "ClientDescribeWorkflowExecutionExecutionTypeDef",
    "ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef",
    "ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef",
    "ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef",
    "ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef",
    "ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef",
    "ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef",
    "ClientDescribeWorkflowExecutionResponseopenCountsTypeDef",
    "ClientDescribeWorkflowExecutionResponseTypeDef",
    "ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef",
    "ClientDescribeWorkflowTypeResponseconfigurationTypeDef",
    "ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef",
    "ClientDescribeWorkflowTypeResponsetypeInfoTypeDef",
    "ClientDescribeWorkflowTypeResponseTypeDef",
    "ClientDescribeWorkflowTypeWorkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseeventsTypeDef",
    "ClientGetWorkflowExecutionHistoryResponseTypeDef",
    "ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef",
    "ClientListActivityTypesResponsetypeInfosTypeDef",
    "ClientListActivityTypesResponseTypeDef",
    "ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef",
    "ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef",
    "ClientListClosedWorkflowExecutionsExecutionFilterTypeDef",
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef",
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef",
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef",
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef",
    "ClientListClosedWorkflowExecutionsResponseTypeDef",
    "ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef",
    "ClientListClosedWorkflowExecutionsTagFilterTypeDef",
    "ClientListClosedWorkflowExecutionsTypeFilterTypeDef",
    "ClientListDomainsResponsedomainInfosTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListOpenWorkflowExecutionsExecutionFilterTypeDef",
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef",
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef",
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef",
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef",
    "ClientListOpenWorkflowExecutionsResponseTypeDef",
    "ClientListOpenWorkflowExecutionsStartTimeFilterTypeDef",
    "ClientListOpenWorkflowExecutionsTagFilterTypeDef",
    "ClientListOpenWorkflowExecutionsTypeFilterTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef",
    "ClientListWorkflowTypesResponsetypeInfosTypeDef",
    "ClientListWorkflowTypesResponseTypeDef",
    "ClientPollForActivityTaskResponseactivityTypeTypeDef",
    "ClientPollForActivityTaskResponseworkflowExecutionTypeDef",
    "ClientPollForActivityTaskResponseTypeDef",
    "ClientPollForActivityTaskTaskListTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    "ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    "ClientPollForDecisionTaskResponseeventsTypeDef",
    "ClientPollForDecisionTaskResponseworkflowExecutionTypeDef",
    "ClientPollForDecisionTaskResponseworkflowTypeTypeDef",
    "ClientPollForDecisionTaskResponseTypeDef",
    "ClientPollForDecisionTaskTaskListTypeDef",
    "ClientRecordActivityTaskHeartbeatResponseTypeDef",
    "ClientRegisterActivityTypeDefaultTaskListTypeDef",
    "ClientRegisterDomainTagsTypeDef",
    "ClientRegisterWorkflowTypeDefaultTaskListTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef",
    "ClientRespondDecisionTaskCompletedDecisionsTypeDef",
    "ClientStartWorkflowExecutionResponseTypeDef",
    "ClientStartWorkflowExecutionTaskListTypeDef",
    "ClientStartWorkflowExecutionWorkflowTypeTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUndeprecateActivityTypeActivityTypeTypeDef",
    "ClientUndeprecateWorkflowTypeWorkflowTypeTypeDef",
    "CloseStatusFilterTypeDef",
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    "ActivityTaskCanceledEventAttributesTypeDef",
    "ActivityTaskCompletedEventAttributesTypeDef",
    "ActivityTaskFailedEventAttributesTypeDef",
    "TaskListTypeDef",
    "ActivityTaskScheduledEventAttributesTypeDef",
    "ActivityTaskStartedEventAttributesTypeDef",
    "ActivityTaskTimedOutEventAttributesTypeDef",
    "CancelTimerFailedEventAttributesTypeDef",
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowExecutionTypeDef",
    "WorkflowTypeTypeDef",
    "ChildWorkflowExecutionCanceledEventAttributesTypeDef",
    "ChildWorkflowExecutionCompletedEventAttributesTypeDef",
    "ChildWorkflowExecutionFailedEventAttributesTypeDef",
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "DecisionTaskCompletedEventAttributesTypeDef",
    "DecisionTaskScheduledEventAttributesTypeDef",
    "DecisionTaskStartedEventAttributesTypeDef",
    "DecisionTaskTimedOutEventAttributesTypeDef",
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    "LambdaFunctionCompletedEventAttributesTypeDef",
    "LambdaFunctionFailedEventAttributesTypeDef",
    "LambdaFunctionScheduledEventAttributesTypeDef",
    "LambdaFunctionStartedEventAttributesTypeDef",
    "LambdaFunctionTimedOutEventAttributesTypeDef",
    "MarkerRecordedEventAttributesTypeDef",
    "RecordMarkerFailedEventAttributesTypeDef",
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    "StartTimerFailedEventAttributesTypeDef",
    "TimerCanceledEventAttributesTypeDef",
    "TimerFiredEventAttributesTypeDef",
    "TimerStartedEventAttributesTypeDef",
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "WorkflowExecutionCanceledEventAttributesTypeDef",
    "WorkflowExecutionCompletedEventAttributesTypeDef",
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "WorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    "WorkflowExecutionStartedEventAttributesTypeDef",
    "WorkflowExecutionTerminatedEventAttributesTypeDef",
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    "HistoryEventTypeDef",
    "DecisionTaskTypeDef",
    "DomainInfoTypeDef",
    "DomainInfosTypeDef",
    "ExecutionTimeFilterTypeDef",
    "HistoryTypeDef",
    "PaginatorConfigTypeDef",
    "TagFilterTypeDef",
    "WorkflowExecutionFilterTypeDef",
    "WorkflowExecutionInfoTypeDef",
    "WorkflowExecutionInfosTypeDef",
    "WorkflowTypeFilterTypeDef",
    "WorkflowTypeInfoTypeDef",
    "WorkflowTypeInfosTypeDef",
)

ActivityTypeTypeDef = TypedDict("ActivityTypeTypeDef", {"name": str, "version": str})

_RequiredActivityTypeInfoTypeDef = TypedDict(
    "_RequiredActivityTypeInfoTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "creationDate": datetime,
    },
)
_OptionalActivityTypeInfoTypeDef = TypedDict(
    "_OptionalActivityTypeInfoTypeDef",
    {"description": str, "deprecationDate": datetime},
    total=False,
)


class ActivityTypeInfoTypeDef(_RequiredActivityTypeInfoTypeDef, _OptionalActivityTypeInfoTypeDef):
    pass


_RequiredActivityTypeInfosTypeDef = TypedDict(
    "_RequiredActivityTypeInfosTypeDef", {"typeInfos": List[ActivityTypeInfoTypeDef]}
)
_OptionalActivityTypeInfosTypeDef = TypedDict(
    "_OptionalActivityTypeInfosTypeDef", {"nextPageToken": str}, total=False
)


class ActivityTypeInfosTypeDef(
    _RequiredActivityTypeInfosTypeDef, _OptionalActivityTypeInfosTypeDef
):
    pass


ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsCloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
    total=False,
)

ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsCloseTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientCountClosedWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsResponseTypeDef",
    {"count": int, "truncated": bool},
    total=False,
)

ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsStartTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientCountClosedWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientCountClosedWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientCountClosedWorkflowExecutionsTypeFilterTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientCountOpenWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsResponseTypeDef",
    {"count": int, "truncated": bool},
    total=False,
)

_RequiredClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_RequiredClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_OptionalClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef",
    {"latestDate": datetime},
    total=False,
)


class ClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef(
    _RequiredClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef,
    _OptionalClientCountOpenWorkflowExecutionsStartTimeFilterTypeDef,
):
    pass


ClientCountOpenWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientCountOpenWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientCountOpenWorkflowExecutionsTypeFilterTypeDef", {"name": str, "version": str}, total=False
)

ClientCountPendingActivityTasksResponseTypeDef = TypedDict(
    "ClientCountPendingActivityTasksResponseTypeDef", {"count": int, "truncated": bool}, total=False
)

ClientCountPendingActivityTasksTaskListTypeDef = TypedDict(
    "ClientCountPendingActivityTasksTaskListTypeDef", {"name": str}
)

ClientCountPendingDecisionTasksResponseTypeDef = TypedDict(
    "ClientCountPendingDecisionTasksResponseTypeDef", {"count": int, "truncated": bool}, total=False
)

ClientCountPendingDecisionTasksTaskListTypeDef = TypedDict(
    "ClientCountPendingDecisionTasksTaskListTypeDef", {"name": str}
)

_RequiredClientDeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_RequiredClientDeprecateActivityTypeActivityTypeTypeDef", {"name": str}
)
_OptionalClientDeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_OptionalClientDeprecateActivityTypeActivityTypeTypeDef", {"version": str}, total=False
)


class ClientDeprecateActivityTypeActivityTypeTypeDef(
    _RequiredClientDeprecateActivityTypeActivityTypeTypeDef,
    _OptionalClientDeprecateActivityTypeActivityTypeTypeDef,
):
    pass


_RequiredClientDeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientDeprecateWorkflowTypeWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientDeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientDeprecateWorkflowTypeWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientDeprecateWorkflowTypeWorkflowTypeTypeDef(
    _RequiredClientDeprecateWorkflowTypeWorkflowTypeTypeDef,
    _OptionalClientDeprecateWorkflowTypeWorkflowTypeTypeDef,
):
    pass


_RequiredClientDescribeActivityTypeActivityTypeTypeDef = TypedDict(
    "_RequiredClientDescribeActivityTypeActivityTypeTypeDef", {"name": str}
)
_OptionalClientDescribeActivityTypeActivityTypeTypeDef = TypedDict(
    "_OptionalClientDescribeActivityTypeActivityTypeTypeDef", {"version": str}, total=False
)


class ClientDescribeActivityTypeActivityTypeTypeDef(
    _RequiredClientDescribeActivityTypeActivityTypeTypeDef,
    _OptionalClientDescribeActivityTypeActivityTypeTypeDef,
):
    pass


ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeActivityTypeResponseconfigurationTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponseconfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": str,
        "defaultTaskHeartbeatTimeout": str,
        "defaultTaskList": ClientDescribeActivityTypeResponseconfigurationdefaultTaskListTypeDef,
        "defaultTaskPriority": str,
        "defaultTaskScheduleToStartTimeout": str,
        "defaultTaskScheduleToCloseTimeout": str,
    },
    total=False,
)

ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeActivityTypeResponsetypeInfoTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponsetypeInfoTypeDef",
    {
        "activityType": ClientDescribeActivityTypeResponsetypeInfoactivityTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientDescribeActivityTypeResponseTypeDef = TypedDict(
    "ClientDescribeActivityTypeResponseTypeDef",
    {
        "typeInfo": ClientDescribeActivityTypeResponsetypeInfoTypeDef,
        "configuration": ClientDescribeActivityTypeResponseconfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDomainResponseconfigurationTypeDef = TypedDict(
    "ClientDescribeDomainResponseconfigurationTypeDef",
    {"workflowExecutionRetentionPeriodInDays": str},
    total=False,
)

ClientDescribeDomainResponsedomainInfoTypeDef = TypedDict(
    "ClientDescribeDomainResponsedomainInfoTypeDef",
    {"name": str, "status": Literal["REGISTERED", "DEPRECATED"], "description": str, "arn": str},
    total=False,
)

ClientDescribeDomainResponseTypeDef = TypedDict(
    "ClientDescribeDomainResponseTypeDef",
    {
        "domainInfo": ClientDescribeDomainResponsedomainInfoTypeDef,
        "configuration": ClientDescribeDomainResponseconfigurationTypeDef,
    },
    total=False,
)

_RequiredClientDescribeWorkflowExecutionExecutionTypeDef = TypedDict(
    "_RequiredClientDescribeWorkflowExecutionExecutionTypeDef", {"workflowId": str}
)
_OptionalClientDescribeWorkflowExecutionExecutionTypeDef = TypedDict(
    "_OptionalClientDescribeWorkflowExecutionExecutionTypeDef", {"runId": str}, total=False
)


class ClientDescribeWorkflowExecutionExecutionTypeDef(
    _RequiredClientDescribeWorkflowExecutionExecutionTypeDef,
    _OptionalClientDescribeWorkflowExecutionExecutionTypeDef,
):
    pass


ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef",
    {
        "taskStartToCloseTimeout": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientDescribeWorkflowExecutionResponseexecutionConfigurationtaskListTypeDef,
        "taskPriority": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "lambdaRole": str,
    },
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef",
    {
        "execution": ClientDescribeWorkflowExecutionResponseexecutionInfoexecutionTypeDef,
        "workflowType": ClientDescribeWorkflowExecutionResponseexecutionInfoworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ClientDescribeWorkflowExecutionResponseexecutionInfoparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ClientDescribeWorkflowExecutionResponseopenCountsTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseopenCountsTypeDef",
    {
        "openActivityTasks": int,
        "openDecisionTasks": int,
        "openTimers": int,
        "openChildWorkflowExecutions": int,
        "openLambdaFunctions": int,
    },
    total=False,
)

ClientDescribeWorkflowExecutionResponseTypeDef = TypedDict(
    "ClientDescribeWorkflowExecutionResponseTypeDef",
    {
        "executionInfo": ClientDescribeWorkflowExecutionResponseexecutionInfoTypeDef,
        "executionConfiguration": ClientDescribeWorkflowExecutionResponseexecutionConfigurationTypeDef,
        "openCounts": ClientDescribeWorkflowExecutionResponseopenCountsTypeDef,
        "latestActivityTaskTimestamp": datetime,
        "latestExecutionContext": str,
    },
    total=False,
)

ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeWorkflowTypeResponseconfigurationTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponseconfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": str,
        "defaultExecutionStartToCloseTimeout": str,
        "defaultTaskList": ClientDescribeWorkflowTypeResponseconfigurationdefaultTaskListTypeDef,
        "defaultTaskPriority": str,
        "defaultChildPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "defaultLambdaRole": str,
    },
    total=False,
)

ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeWorkflowTypeResponsetypeInfoTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponsetypeInfoTypeDef",
    {
        "workflowType": ClientDescribeWorkflowTypeResponsetypeInfoworkflowTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientDescribeWorkflowTypeResponseTypeDef = TypedDict(
    "ClientDescribeWorkflowTypeResponseTypeDef",
    {
        "typeInfo": ClientDescribeWorkflowTypeResponsetypeInfoTypeDef,
        "configuration": ClientDescribeWorkflowTypeResponseconfigurationTypeDef,
    },
    total=False,
)

_RequiredClientDescribeWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientDescribeWorkflowTypeWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientDescribeWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientDescribeWorkflowTypeWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientDescribeWorkflowTypeWorkflowTypeTypeDef(
    _RequiredClientDescribeWorkflowTypeWorkflowTypeTypeDef,
    _OptionalClientDescribeWorkflowTypeWorkflowTypeTypeDef,
):
    pass


_RequiredClientGetWorkflowExecutionHistoryExecutionTypeDef = TypedDict(
    "_RequiredClientGetWorkflowExecutionHistoryExecutionTypeDef", {"workflowId": str}
)
_OptionalClientGetWorkflowExecutionHistoryExecutionTypeDef = TypedDict(
    "_OptionalClientGetWorkflowExecutionHistoryExecutionTypeDef", {"runId": str}, total=False
)


class ClientGetWorkflowExecutionHistoryExecutionTypeDef(
    _RequiredClientGetWorkflowExecutionHistoryExecutionTypeDef,
    _OptionalClientGetWorkflowExecutionHistoryExecutionTypeDef,
):
    pass


ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    {
        "details": str,
        "scheduledEventId": int,
        "startedEventId": int,
        "latestCancelRequestedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    {"result": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "heartbeatTimeout": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
        "details": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef,
        "result": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "reason": str,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef,
        "timeoutType": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    {"executionContext": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "startToCloseTimeout": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "result": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "reason": str, "details": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": str,
        "input": str,
        "startToCloseTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    {"scheduledEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "timeoutType": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    {"markerName": str, "cause": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "runId": str, "decisionTaskCompletedEventId": int, "control": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "signalName": str,
        "input": str,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": str, "message": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "control": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    {"details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    {"result": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef,
        "lambdaRole": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": str,
        "externalWorkflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "workflowType": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseeventsTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseeventsTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
        "workflowExecutionStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsdecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsworkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsmarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventstimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventstimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventstimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventscancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventslambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": ClientGetWorkflowExecutionHistoryResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)

ClientGetWorkflowExecutionHistoryResponseTypeDef = TypedDict(
    "ClientGetWorkflowExecutionHistoryResponseTypeDef",
    {"events": List[ClientGetWorkflowExecutionHistoryResponseeventsTypeDef], "nextPageToken": str},
    total=False,
)

ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef = TypedDict(
    "ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListActivityTypesResponsetypeInfosTypeDef = TypedDict(
    "ClientListActivityTypesResponsetypeInfosTypeDef",
    {
        "activityType": ClientListActivityTypesResponsetypeInfosactivityTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientListActivityTypesResponseTypeDef = TypedDict(
    "ClientListActivityTypesResponseTypeDef",
    {"typeInfos": List[ClientListActivityTypesResponsetypeInfosTypeDef], "nextPageToken": str},
    total=False,
)

ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsCloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
    total=False,
)

ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsCloseTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientListClosedWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef",
    {
        "execution": ClientListClosedWorkflowExecutionsResponseexecutionInfosexecutionTypeDef,
        "workflowType": ClientListClosedWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ClientListClosedWorkflowExecutionsResponseexecutionInfosparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ClientListClosedWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsResponseTypeDef",
    {
        "executionInfos": List[ClientListClosedWorkflowExecutionsResponseexecutionInfosTypeDef],
        "nextPageToken": str,
    },
    total=False,
)

ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsStartTimeFilterTypeDef",
    {"oldestDate": datetime, "latestDate": datetime},
    total=False,
)

ClientListClosedWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientListClosedWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientListClosedWorkflowExecutionsTypeFilterTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListDomainsResponsedomainInfosTypeDef = TypedDict(
    "ClientListDomainsResponsedomainInfosTypeDef",
    {"name": str, "status": Literal["REGISTERED", "DEPRECATED"], "description": str, "arn": str},
    total=False,
)

ClientListDomainsResponseTypeDef = TypedDict(
    "ClientListDomainsResponseTypeDef",
    {"domainInfos": List[ClientListDomainsResponsedomainInfosTypeDef], "nextPageToken": str},
    total=False,
)

ClientListOpenWorkflowExecutionsExecutionFilterTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsExecutionFilterTypeDef", {"workflowId": str}, total=False
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef",
    {
        "execution": ClientListOpenWorkflowExecutionsResponseexecutionInfosexecutionTypeDef,
        "workflowType": ClientListOpenWorkflowExecutionsResponseexecutionInfosworkflowTypeTypeDef,
        "startTimestamp": datetime,
        "closeTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": ClientListOpenWorkflowExecutionsResponseexecutionInfosparentTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)

ClientListOpenWorkflowExecutionsResponseTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsResponseTypeDef",
    {
        "executionInfos": List[ClientListOpenWorkflowExecutionsResponseexecutionInfosTypeDef],
        "nextPageToken": str,
    },
    total=False,
)

_RequiredClientListOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_RequiredClientListOpenWorkflowExecutionsStartTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalClientListOpenWorkflowExecutionsStartTimeFilterTypeDef = TypedDict(
    "_OptionalClientListOpenWorkflowExecutionsStartTimeFilterTypeDef",
    {"latestDate": datetime},
    total=False,
)


class ClientListOpenWorkflowExecutionsStartTimeFilterTypeDef(
    _RequiredClientListOpenWorkflowExecutionsStartTimeFilterTypeDef,
    _OptionalClientListOpenWorkflowExecutionsStartTimeFilterTypeDef,
):
    pass


ClientListOpenWorkflowExecutionsTagFilterTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsTagFilterTypeDef", {"tag": str}, total=False
)

ClientListOpenWorkflowExecutionsTypeFilterTypeDef = TypedDict(
    "ClientListOpenWorkflowExecutionsTypeFilterTypeDef", {"name": str, "version": str}, total=False
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef = TypedDict(
    "ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientListWorkflowTypesResponsetypeInfosTypeDef = TypedDict(
    "ClientListWorkflowTypesResponsetypeInfosTypeDef",
    {
        "workflowType": ClientListWorkflowTypesResponsetypeInfosworkflowTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "description": str,
        "creationDate": datetime,
        "deprecationDate": datetime,
    },
    total=False,
)

ClientListWorkflowTypesResponseTypeDef = TypedDict(
    "ClientListWorkflowTypesResponseTypeDef",
    {"typeInfos": List[ClientListWorkflowTypesResponsetypeInfosTypeDef], "nextPageToken": str},
    total=False,
)

ClientPollForActivityTaskResponseactivityTypeTypeDef = TypedDict(
    "ClientPollForActivityTaskResponseactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForActivityTaskResponseworkflowExecutionTypeDef = TypedDict(
    "ClientPollForActivityTaskResponseworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForActivityTaskResponseTypeDef = TypedDict(
    "ClientPollForActivityTaskResponseTypeDef",
    {
        "taskToken": str,
        "activityId": str,
        "startedEventId": int,
        "workflowExecution": ClientPollForActivityTaskResponseworkflowExecutionTypeDef,
        "activityType": ClientPollForActivityTaskResponseactivityTypeTypeDef,
        "input": str,
    },
    total=False,
)

ClientPollForActivityTaskTaskListTypeDef = TypedDict(
    "ClientPollForActivityTaskTaskListTypeDef", {"name": str}
)

ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef",
    {
        "details": str,
        "scheduledEventId": int,
        "startedEventId": int,
        "latestCancelRequestedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef",
    {"result": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskList": ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "heartbeatTimeout": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
        "details": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesworkflowTypeTypeDef,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesworkflowTypeTypeDef,
        "result": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "reason": str,
        "details": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesworkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesworkflowTypeTypeDef,
        "timeoutType": str,
        "initiatedEventId": int,
        "startedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef",
    {"executionContext": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributestaskListTypeDef,
        "taskPriority": str,
        "startToCloseTimeout": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef",
    {"identity": str, "scheduledEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "scheduledEventId": int, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesworkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "result": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "reason": str, "details": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": str,
        "input": str,
        "startToCloseTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef",
    {"scheduledEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int, "timeoutType": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef",
    {"markerName": str, "cause": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "runId": str, "decisionTaskCompletedEventId": int, "control": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesactivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "runId": str,
        "signalName": str,
        "input": str,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesworkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesworkflowTypeTypeDef,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": str, "message": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "control": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef",
    {"details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef",
    {"result": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowType": ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesworkflowTypeTypeDef,
        "lambdaRole": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str, "decisionTaskCompletedEventId": int},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": str,
        "externalWorkflowExecution": ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesexternalWorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributestaskListTypeDef,
        "taskPriority": str,
        "workflowType": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesworkflowTypeTypeDef,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesparentWorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)

ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef",
    {"timeoutType": str, "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
    total=False,
)

ClientPollForDecisionTaskResponseeventsTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseeventsTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
        "workflowExecutionStartedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventscompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsfailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventscancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventscontinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventsdecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": ClientPollForDecisionTaskResponseeventsactivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": ClientPollForDecisionTaskResponseeventsworkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": ClientPollForDecisionTaskResponseeventsmarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": ClientPollForDecisionTaskResponseeventsrecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": ClientPollForDecisionTaskResponseeventstimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": ClientPollForDecisionTaskResponseeventstimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": ClientPollForDecisionTaskResponseeventstimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": ClientPollForDecisionTaskResponseeventschildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventssignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": ClientPollForDecisionTaskResponseeventsexternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsrequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": ClientPollForDecisionTaskResponseeventsscheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": ClientPollForDecisionTaskResponseeventsrequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": ClientPollForDecisionTaskResponseeventsstartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": ClientPollForDecisionTaskResponseeventscancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsstartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": ClientPollForDecisionTaskResponseeventslambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsscheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": ClientPollForDecisionTaskResponseeventsstartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)

ClientPollForDecisionTaskResponseworkflowExecutionTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseworkflowExecutionTypeDef",
    {"workflowId": str, "runId": str},
    total=False,
)

ClientPollForDecisionTaskResponseworkflowTypeTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientPollForDecisionTaskResponseTypeDef = TypedDict(
    "ClientPollForDecisionTaskResponseTypeDef",
    {
        "taskToken": str,
        "startedEventId": int,
        "workflowExecution": ClientPollForDecisionTaskResponseworkflowExecutionTypeDef,
        "workflowType": ClientPollForDecisionTaskResponseworkflowTypeTypeDef,
        "events": List[ClientPollForDecisionTaskResponseeventsTypeDef],
        "nextPageToken": str,
        "previousStartedEventId": int,
    },
    total=False,
)

ClientPollForDecisionTaskTaskListTypeDef = TypedDict(
    "ClientPollForDecisionTaskTaskListTypeDef", {"name": str}
)

ClientRecordActivityTaskHeartbeatResponseTypeDef = TypedDict(
    "ClientRecordActivityTaskHeartbeatResponseTypeDef", {"cancelRequested": bool}, total=False
)

ClientRegisterActivityTypeDefaultTaskListTypeDef = TypedDict(
    "ClientRegisterActivityTypeDefaultTaskListTypeDef", {"name": str}
)

_RequiredClientRegisterDomainTagsTypeDef = TypedDict(
    "_RequiredClientRegisterDomainTagsTypeDef", {"key": str}
)
_OptionalClientRegisterDomainTagsTypeDef = TypedDict(
    "_OptionalClientRegisterDomainTagsTypeDef", {"value": str}, total=False
)


class ClientRegisterDomainTagsTypeDef(
    _RequiredClientRegisterDomainTagsTypeDef, _OptionalClientRegisterDomainTagsTypeDef
):
    pass


ClientRegisterWorkflowTypeDefaultTaskListTypeDef = TypedDict(
    "ClientRegisterWorkflowTypeDefaultTaskListTypeDef", {"name": str}
)

ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef",
    {"timerId": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef",
    {"details": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef",
    {"result": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowTypeVersion": str,
        "lambdaRole": str,
    },
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef",
    {"markerName": str, "details": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef",
    {"activityId": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowId": str, "runId": str, "control": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef",
    {
        "activityType": ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesactivityTypeTypeDef,
        "activityId": str,
        "control": str,
        "input": str,
        "scheduleToCloseTimeout": str,
        "taskList": ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributestaskListTypeDef,
        "taskPriority": str,
        "scheduleToStartTimeout": str,
        "startToCloseTimeout": str,
        "heartbeatTimeout": str,
    },
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef",
    {"id": str, "name": str, "control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowId": str, "runId": str, "signalName": str, "input": str, "control": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef",
    {"name": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowType": ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesworkflowTypeTypeDef,
        "workflowId": str,
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributestaskListTypeDef,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef",
    {"timerId": str, "control": str, "startToFireTimeout": str},
    total=False,
)

ClientRespondDecisionTaskCompletedDecisionsTypeDef = TypedDict(
    "ClientRespondDecisionTaskCompletedDecisionsTypeDef",
    {
        "decisionType": Literal[
            "ScheduleActivityTask",
            "RequestCancelActivityTask",
            "CompleteWorkflowExecution",
            "FailWorkflowExecution",
            "CancelWorkflowExecution",
            "ContinueAsNewWorkflowExecution",
            "RecordMarker",
            "StartTimer",
            "CancelTimer",
            "SignalExternalWorkflowExecution",
            "RequestCancelExternalWorkflowExecution",
            "StartChildWorkflowExecution",
            "ScheduleLambdaFunction",
        ],
        "scheduleActivityTaskDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsscheduleActivityTaskDecisionAttributesTypeDef,
        "requestCancelActivityTaskDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsrequestCancelActivityTaskDecisionAttributesTypeDef,
        "completeWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscompleteWorkflowExecutionDecisionAttributesTypeDef,
        "failWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsfailWorkflowExecutionDecisionAttributesTypeDef,
        "cancelWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscancelWorkflowExecutionDecisionAttributesTypeDef,
        "continueAsNewWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscontinueAsNewWorkflowExecutionDecisionAttributesTypeDef,
        "recordMarkerDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsrecordMarkerDecisionAttributesTypeDef,
        "startTimerDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsstartTimerDecisionAttributesTypeDef,
        "cancelTimerDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionscancelTimerDecisionAttributesTypeDef,
        "signalExternalWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionssignalExternalWorkflowExecutionDecisionAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsrequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef,
        "startChildWorkflowExecutionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsstartChildWorkflowExecutionDecisionAttributesTypeDef,
        "scheduleLambdaFunctionDecisionAttributes": ClientRespondDecisionTaskCompletedDecisionsscheduleLambdaFunctionDecisionAttributesTypeDef,
    },
    total=False,
)

ClientStartWorkflowExecutionResponseTypeDef = TypedDict(
    "ClientStartWorkflowExecutionResponseTypeDef", {"runId": str}, total=False
)

ClientStartWorkflowExecutionTaskListTypeDef = TypedDict(
    "ClientStartWorkflowExecutionTaskListTypeDef", {"name": str}, total=False
)

_RequiredClientStartWorkflowExecutionWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientStartWorkflowExecutionWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientStartWorkflowExecutionWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientStartWorkflowExecutionWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientStartWorkflowExecutionWorkflowTypeTypeDef(
    _RequiredClientStartWorkflowExecutionWorkflowTypeTypeDef,
    _OptionalClientStartWorkflowExecutionWorkflowTypeTypeDef,
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


_RequiredClientUndeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_RequiredClientUndeprecateActivityTypeActivityTypeTypeDef", {"name": str}
)
_OptionalClientUndeprecateActivityTypeActivityTypeTypeDef = TypedDict(
    "_OptionalClientUndeprecateActivityTypeActivityTypeTypeDef", {"version": str}, total=False
)


class ClientUndeprecateActivityTypeActivityTypeTypeDef(
    _RequiredClientUndeprecateActivityTypeActivityTypeTypeDef,
    _OptionalClientUndeprecateActivityTypeActivityTypeTypeDef,
):
    pass


_RequiredClientUndeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_RequiredClientUndeprecateWorkflowTypeWorkflowTypeTypeDef", {"name": str}
)
_OptionalClientUndeprecateWorkflowTypeWorkflowTypeTypeDef = TypedDict(
    "_OptionalClientUndeprecateWorkflowTypeWorkflowTypeTypeDef", {"version": str}, total=False
)


class ClientUndeprecateWorkflowTypeWorkflowTypeTypeDef(
    _RequiredClientUndeprecateWorkflowTypeWorkflowTypeTypeDef,
    _OptionalClientUndeprecateWorkflowTypeWorkflowTypeTypeDef,
):
    pass


CloseStatusFilterTypeDef = TypedDict(
    "CloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
)

ActivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
)

_RequiredActivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskCanceledEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalActivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskCanceledEventAttributesTypeDef",
    {"details": str, "latestCancelRequestedEventId": int},
    total=False,
)


class ActivityTaskCanceledEventAttributesTypeDef(
    _RequiredActivityTaskCanceledEventAttributesTypeDef,
    _OptionalActivityTaskCanceledEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalActivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class ActivityTaskCompletedEventAttributesTypeDef(
    _RequiredActivityTaskCompletedEventAttributesTypeDef,
    _OptionalActivityTaskCompletedEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class ActivityTaskFailedEventAttributesTypeDef(
    _RequiredActivityTaskFailedEventAttributesTypeDef,
    _OptionalActivityTaskFailedEventAttributesTypeDef,
):
    pass


TaskListTypeDef = TypedDict("TaskListTypeDef", {"name": str})

_RequiredActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "taskList": TaskListTypeDef,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskScheduledEventAttributesTypeDef",
    {
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskPriority": str,
        "heartbeatTimeout": str,
    },
    total=False,
)


class ActivityTaskScheduledEventAttributesTypeDef(
    _RequiredActivityTaskScheduledEventAttributesTypeDef,
    _OptionalActivityTaskScheduledEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskStartedEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskStartedEventAttributesTypeDef", {"scheduledEventId": int}
)
_OptionalActivityTaskStartedEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskStartedEventAttributesTypeDef", {"identity": str}, total=False
)


class ActivityTaskStartedEventAttributesTypeDef(
    _RequiredActivityTaskStartedEventAttributesTypeDef,
    _OptionalActivityTaskStartedEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
    },
)
_OptionalActivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskTimedOutEventAttributesTypeDef", {"details": str}, total=False
)


class ActivityTaskTimedOutEventAttributesTypeDef(
    _RequiredActivityTaskTimedOutEventAttributesTypeDef,
    _OptionalActivityTaskTimedOutEventAttributesTypeDef,
):
    pass


CancelTimerFailedEventAttributesTypeDef = TypedDict(
    "CancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

CancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

WorkflowExecutionTypeDef = TypedDict("WorkflowExecutionTypeDef", {"workflowId": str, "runId": str})

WorkflowTypeTypeDef = TypedDict("WorkflowTypeTypeDef", {"name": str, "version": str})

_RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
_OptionalChildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_OptionalChildWorkflowExecutionCanceledEventAttributesTypeDef", {"details": str}, total=False
)


class ChildWorkflowExecutionCanceledEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef,
    _OptionalChildWorkflowExecutionCanceledEventAttributesTypeDef,
):
    pass


_RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
_OptionalChildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalChildWorkflowExecutionCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class ChildWorkflowExecutionCompletedEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef,
    _OptionalChildWorkflowExecutionCompletedEventAttributesTypeDef,
):
    pass


_RequiredChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
_OptionalChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalChildWorkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class ChildWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalChildWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


ChildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
    },
)

ChildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
)

ChildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "timeoutType": Literal["START_TO_CLOSE"],
        "initiatedEventId": int,
        "startedEventId": int,
    },
)

CompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredDecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredDecisionTaskCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalDecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalDecisionTaskCompletedEventAttributesTypeDef", {"executionContext": str}, total=False
)


class DecisionTaskCompletedEventAttributesTypeDef(
    _RequiredDecisionTaskCompletedEventAttributesTypeDef,
    _OptionalDecisionTaskCompletedEventAttributesTypeDef,
):
    pass


_RequiredDecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredDecisionTaskScheduledEventAttributesTypeDef", {"taskList": TaskListTypeDef}
)
_OptionalDecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalDecisionTaskScheduledEventAttributesTypeDef",
    {"taskPriority": str, "startToCloseTimeout": str},
    total=False,
)


class DecisionTaskScheduledEventAttributesTypeDef(
    _RequiredDecisionTaskScheduledEventAttributesTypeDef,
    _OptionalDecisionTaskScheduledEventAttributesTypeDef,
):
    pass


_RequiredDecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "_RequiredDecisionTaskStartedEventAttributesTypeDef", {"scheduledEventId": int}
)
_OptionalDecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "_OptionalDecisionTaskStartedEventAttributesTypeDef", {"identity": str}, total=False
)


class DecisionTaskStartedEventAttributesTypeDef(
    _RequiredDecisionTaskStartedEventAttributesTypeDef,
    _OptionalDecisionTaskStartedEventAttributesTypeDef,
):
    pass


DecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "DecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": Literal["START_TO_CLOSE"], "scheduledEventId": int, "startedEventId": int},
)

ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {"workflowExecution": WorkflowExecutionTypeDef, "initiatedEventId": int},
)

ExternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {"workflowExecution": WorkflowExecutionTypeDef, "initiatedEventId": int},
)

FailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredLambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalLambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class LambdaFunctionCompletedEventAttributesTypeDef(
    _RequiredLambdaFunctionCompletedEventAttributesTypeDef,
    _OptionalLambdaFunctionCompletedEventAttributesTypeDef,
):
    pass


_RequiredLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class LambdaFunctionFailedEventAttributesTypeDef(
    _RequiredLambdaFunctionFailedEventAttributesTypeDef,
    _OptionalLambdaFunctionFailedEventAttributesTypeDef,
):
    pass


_RequiredLambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventAttributesTypeDef",
    {"id": str, "name": str, "decisionTaskCompletedEventId": int},
)
_OptionalLambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventAttributesTypeDef",
    {"control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)


class LambdaFunctionScheduledEventAttributesTypeDef(
    _RequiredLambdaFunctionScheduledEventAttributesTypeDef,
    _OptionalLambdaFunctionScheduledEventAttributesTypeDef,
):
    pass


LambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "LambdaFunctionStartedEventAttributesTypeDef", {"scheduledEventId": int}
)

_RequiredLambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalLambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionTimedOutEventAttributesTypeDef",
    {"timeoutType": Literal["START_TO_CLOSE"]},
    total=False,
)


class LambdaFunctionTimedOutEventAttributesTypeDef(
    _RequiredLambdaFunctionTimedOutEventAttributesTypeDef,
    _OptionalLambdaFunctionTimedOutEventAttributesTypeDef,
):
    pass


_RequiredMarkerRecordedEventAttributesTypeDef = TypedDict(
    "_RequiredMarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "decisionTaskCompletedEventId": int},
)
_OptionalMarkerRecordedEventAttributesTypeDef = TypedDict(
    "_OptionalMarkerRecordedEventAttributesTypeDef", {"details": str}, total=False
)


class MarkerRecordedEventAttributesTypeDef(
    _RequiredMarkerRecordedEventAttributesTypeDef, _OptionalMarkerRecordedEventAttributesTypeDef
):
    pass


RecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "RecordMarkerFailedEventAttributesTypeDef",
    {
        "markerName": str,
        "cause": Literal["OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

RequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "decisionTaskCompletedEventId": int},
)
_OptionalRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


ScheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

ScheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalSignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "signalName": str, "decisionTaskCompletedEventId": int},
)
_OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"runId": str, "input": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


_RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": WorkflowTypeTypeDef,
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalStartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {"control": str},
    total=False,
)


class StartChildWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": WorkflowTypeTypeDef,
        "taskList": TaskListTypeDef,
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
    },
)
_OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class StartChildWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


StartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": Literal["ASSUME_ROLE_FAILED"], "message": str},
    total=False,
)

StartTimerFailedEventAttributesTypeDef = TypedDict(
    "StartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

TimerCanceledEventAttributesTypeDef = TypedDict(
    "TimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
)

TimerFiredEventAttributesTypeDef = TypedDict(
    "TimerFiredEventAttributesTypeDef", {"timerId": str, "startedEventId": int}
)

_RequiredTimerStartedEventAttributesTypeDef = TypedDict(
    "_RequiredTimerStartedEventAttributesTypeDef",
    {"timerId": str, "startToFireTimeout": str, "decisionTaskCompletedEventId": int},
)
_OptionalTimerStartedEventAttributesTypeDef = TypedDict(
    "_OptionalTimerStartedEventAttributesTypeDef", {"control": str}, total=False
)


class TimerStartedEventAttributesTypeDef(
    _RequiredTimerStartedEventAttributesTypeDef, _OptionalTimerStartedEventAttributesTypeDef
):
    pass


WorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": WorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
        "cause": Literal["CHILD_POLICY_APPLIED"],
    },
    total=False,
)

_RequiredWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionCanceledEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int},
)
_OptionalWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionCanceledEventAttributesTypeDef", {"details": str}, total=False
)


class WorkflowExecutionCanceledEventAttributesTypeDef(
    _RequiredWorkflowExecutionCanceledEventAttributesTypeDef,
    _OptionalWorkflowExecutionCanceledEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionCompletedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int},
)
_OptionalWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class WorkflowExecutionCompletedEventAttributesTypeDef(
    _RequiredWorkflowExecutionCompletedEventAttributesTypeDef,
    _OptionalWorkflowExecutionCompletedEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "taskList": TaskListTypeDef,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "workflowType": WorkflowTypeTypeDef,
    },
)
_OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class WorkflowExecutionContinuedAsNewEventAttributesTypeDef(
    _RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef,
    _OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionFailedEventAttributesTypeDef", {"decisionTaskCompletedEventId": int}
)
_OptionalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class WorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionSignaledEventAttributesTypeDef", {"signalName": str}
)
_OptionalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "input": str,
        "externalWorkflowExecution": WorkflowExecutionTypeDef,
        "externalInitiatedEventId": int,
    },
    total=False,
)


class WorkflowExecutionSignaledEventAttributesTypeDef(
    _RequiredWorkflowExecutionSignaledEventAttributesTypeDef,
    _OptionalWorkflowExecutionSignaledEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": TaskListTypeDef,
        "workflowType": WorkflowTypeTypeDef,
    },
)
_OptionalWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "taskPriority": str,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": WorkflowExecutionTypeDef,
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)


class WorkflowExecutionStartedEventAttributesTypeDef(
    _RequiredWorkflowExecutionStartedEventAttributesTypeDef,
    _OptionalWorkflowExecutionStartedEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionTerminatedEventAttributesTypeDef",
    {"childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
)
_OptionalWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)


class WorkflowExecutionTerminatedEventAttributesTypeDef(
    _RequiredWorkflowExecutionTerminatedEventAttributesTypeDef,
    _OptionalWorkflowExecutionTerminatedEventAttributesTypeDef,
):
    pass


WorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal["START_TO_CLOSE"],
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
    },
)

_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
    },
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "workflowExecutionStartedEventAttributes": WorkflowExecutionStartedEventAttributesTypeDef,
        "workflowExecutionCompletedEventAttributes": WorkflowExecutionCompletedEventAttributesTypeDef,
        "completeWorkflowExecutionFailedEventAttributes": CompleteWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionFailedEventAttributes": WorkflowExecutionFailedEventAttributesTypeDef,
        "failWorkflowExecutionFailedEventAttributes": FailWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTimedOutEventAttributes": WorkflowExecutionTimedOutEventAttributesTypeDef,
        "workflowExecutionCanceledEventAttributes": WorkflowExecutionCanceledEventAttributesTypeDef,
        "cancelWorkflowExecutionFailedEventAttributes": CancelWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionContinuedAsNewEventAttributes": WorkflowExecutionContinuedAsNewEventAttributesTypeDef,
        "continueAsNewWorkflowExecutionFailedEventAttributes": ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef,
        "workflowExecutionTerminatedEventAttributes": WorkflowExecutionTerminatedEventAttributesTypeDef,
        "workflowExecutionCancelRequestedEventAttributes": WorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "decisionTaskScheduledEventAttributes": DecisionTaskScheduledEventAttributesTypeDef,
        "decisionTaskStartedEventAttributes": DecisionTaskStartedEventAttributesTypeDef,
        "decisionTaskCompletedEventAttributes": DecisionTaskCompletedEventAttributesTypeDef,
        "decisionTaskTimedOutEventAttributes": DecisionTaskTimedOutEventAttributesTypeDef,
        "activityTaskScheduledEventAttributes": ActivityTaskScheduledEventAttributesTypeDef,
        "activityTaskStartedEventAttributes": ActivityTaskStartedEventAttributesTypeDef,
        "activityTaskCompletedEventAttributes": ActivityTaskCompletedEventAttributesTypeDef,
        "activityTaskFailedEventAttributes": ActivityTaskFailedEventAttributesTypeDef,
        "activityTaskTimedOutEventAttributes": ActivityTaskTimedOutEventAttributesTypeDef,
        "activityTaskCanceledEventAttributes": ActivityTaskCanceledEventAttributesTypeDef,
        "activityTaskCancelRequestedEventAttributes": ActivityTaskCancelRequestedEventAttributesTypeDef,
        "workflowExecutionSignaledEventAttributes": WorkflowExecutionSignaledEventAttributesTypeDef,
        "markerRecordedEventAttributes": MarkerRecordedEventAttributesTypeDef,
        "recordMarkerFailedEventAttributes": RecordMarkerFailedEventAttributesTypeDef,
        "timerStartedEventAttributes": TimerStartedEventAttributesTypeDef,
        "timerFiredEventAttributes": TimerFiredEventAttributesTypeDef,
        "timerCanceledEventAttributes": TimerCanceledEventAttributesTypeDef,
        "startChildWorkflowExecutionInitiatedEventAttributes": StartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
        "childWorkflowExecutionStartedEventAttributes": ChildWorkflowExecutionStartedEventAttributesTypeDef,
        "childWorkflowExecutionCompletedEventAttributes": ChildWorkflowExecutionCompletedEventAttributesTypeDef,
        "childWorkflowExecutionFailedEventAttributes": ChildWorkflowExecutionFailedEventAttributesTypeDef,
        "childWorkflowExecutionTimedOutEventAttributes": ChildWorkflowExecutionTimedOutEventAttributesTypeDef,
        "childWorkflowExecutionCanceledEventAttributes": ChildWorkflowExecutionCanceledEventAttributesTypeDef,
        "childWorkflowExecutionTerminatedEventAttributes": ChildWorkflowExecutionTerminatedEventAttributesTypeDef,
        "signalExternalWorkflowExecutionInitiatedEventAttributes": SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "externalWorkflowExecutionSignaledEventAttributes": ExternalWorkflowExecutionSignaledEventAttributesTypeDef,
        "signalExternalWorkflowExecutionFailedEventAttributes": SignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "externalWorkflowExecutionCancelRequestedEventAttributes": ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
        "scheduleActivityTaskFailedEventAttributes": ScheduleActivityTaskFailedEventAttributesTypeDef,
        "requestCancelActivityTaskFailedEventAttributes": RequestCancelActivityTaskFailedEventAttributesTypeDef,
        "startTimerFailedEventAttributes": StartTimerFailedEventAttributesTypeDef,
        "cancelTimerFailedEventAttributes": CancelTimerFailedEventAttributesTypeDef,
        "startChildWorkflowExecutionFailedEventAttributes": StartChildWorkflowExecutionFailedEventAttributesTypeDef,
        "lambdaFunctionScheduledEventAttributes": LambdaFunctionScheduledEventAttributesTypeDef,
        "lambdaFunctionStartedEventAttributes": LambdaFunctionStartedEventAttributesTypeDef,
        "lambdaFunctionCompletedEventAttributes": LambdaFunctionCompletedEventAttributesTypeDef,
        "lambdaFunctionFailedEventAttributes": LambdaFunctionFailedEventAttributesTypeDef,
        "lambdaFunctionTimedOutEventAttributes": LambdaFunctionTimedOutEventAttributesTypeDef,
        "scheduleLambdaFunctionFailedEventAttributes": ScheduleLambdaFunctionFailedEventAttributesTypeDef,
        "startLambdaFunctionFailedEventAttributes": StartLambdaFunctionFailedEventAttributesTypeDef,
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


_RequiredDecisionTaskTypeDef = TypedDict(
    "_RequiredDecisionTaskTypeDef",
    {
        "taskToken": str,
        "startedEventId": int,
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "events": List[HistoryEventTypeDef],
    },
)
_OptionalDecisionTaskTypeDef = TypedDict(
    "_OptionalDecisionTaskTypeDef",
    {"nextPageToken": str, "previousStartedEventId": int},
    total=False,
)


class DecisionTaskTypeDef(_RequiredDecisionTaskTypeDef, _OptionalDecisionTaskTypeDef):
    pass


_RequiredDomainInfoTypeDef = TypedDict(
    "_RequiredDomainInfoTypeDef", {"name": str, "status": Literal["REGISTERED", "DEPRECATED"]}
)
_OptionalDomainInfoTypeDef = TypedDict(
    "_OptionalDomainInfoTypeDef", {"description": str, "arn": str}, total=False
)


class DomainInfoTypeDef(_RequiredDomainInfoTypeDef, _OptionalDomainInfoTypeDef):
    pass


_RequiredDomainInfosTypeDef = TypedDict(
    "_RequiredDomainInfosTypeDef", {"domainInfos": List[DomainInfoTypeDef]}
)
_OptionalDomainInfosTypeDef = TypedDict(
    "_OptionalDomainInfosTypeDef", {"nextPageToken": str}, total=False
)


class DomainInfosTypeDef(_RequiredDomainInfosTypeDef, _OptionalDomainInfosTypeDef):
    pass


_RequiredExecutionTimeFilterTypeDef = TypedDict(
    "_RequiredExecutionTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalExecutionTimeFilterTypeDef = TypedDict(
    "_OptionalExecutionTimeFilterTypeDef", {"latestDate": datetime}, total=False
)


class ExecutionTimeFilterTypeDef(
    _RequiredExecutionTimeFilterTypeDef, _OptionalExecutionTimeFilterTypeDef
):
    pass


_RequiredHistoryTypeDef = TypedDict(
    "_RequiredHistoryTypeDef", {"events": List[HistoryEventTypeDef]}
)
_OptionalHistoryTypeDef = TypedDict("_OptionalHistoryTypeDef", {"nextPageToken": str}, total=False)


class HistoryTypeDef(_RequiredHistoryTypeDef, _OptionalHistoryTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"tag": str})

WorkflowExecutionFilterTypeDef = TypedDict("WorkflowExecutionFilterTypeDef", {"workflowId": str})

_RequiredWorkflowExecutionInfoTypeDef = TypedDict(
    "_RequiredWorkflowExecutionInfoTypeDef",
    {
        "execution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "startTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
    },
)
_OptionalWorkflowExecutionInfoTypeDef = TypedDict(
    "_OptionalWorkflowExecutionInfoTypeDef",
    {
        "closeTimestamp": datetime,
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": WorkflowExecutionTypeDef,
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)


class WorkflowExecutionInfoTypeDef(
    _RequiredWorkflowExecutionInfoTypeDef, _OptionalWorkflowExecutionInfoTypeDef
):
    pass


_RequiredWorkflowExecutionInfosTypeDef = TypedDict(
    "_RequiredWorkflowExecutionInfosTypeDef", {"executionInfos": List[WorkflowExecutionInfoTypeDef]}
)
_OptionalWorkflowExecutionInfosTypeDef = TypedDict(
    "_OptionalWorkflowExecutionInfosTypeDef", {"nextPageToken": str}, total=False
)


class WorkflowExecutionInfosTypeDef(
    _RequiredWorkflowExecutionInfosTypeDef, _OptionalWorkflowExecutionInfosTypeDef
):
    pass


_RequiredWorkflowTypeFilterTypeDef = TypedDict("_RequiredWorkflowTypeFilterTypeDef", {"name": str})
_OptionalWorkflowTypeFilterTypeDef = TypedDict(
    "_OptionalWorkflowTypeFilterTypeDef", {"version": str}, total=False
)


class WorkflowTypeFilterTypeDef(
    _RequiredWorkflowTypeFilterTypeDef, _OptionalWorkflowTypeFilterTypeDef
):
    pass


_RequiredWorkflowTypeInfoTypeDef = TypedDict(
    "_RequiredWorkflowTypeInfoTypeDef",
    {
        "workflowType": WorkflowTypeTypeDef,
        "status": Literal["REGISTERED", "DEPRECATED"],
        "creationDate": datetime,
    },
)
_OptionalWorkflowTypeInfoTypeDef = TypedDict(
    "_OptionalWorkflowTypeInfoTypeDef",
    {"description": str, "deprecationDate": datetime},
    total=False,
)


class WorkflowTypeInfoTypeDef(_RequiredWorkflowTypeInfoTypeDef, _OptionalWorkflowTypeInfoTypeDef):
    pass


_RequiredWorkflowTypeInfosTypeDef = TypedDict(
    "_RequiredWorkflowTypeInfosTypeDef", {"typeInfos": List[WorkflowTypeInfoTypeDef]}
)
_OptionalWorkflowTypeInfosTypeDef = TypedDict(
    "_OptionalWorkflowTypeInfosTypeDef", {"nextPageToken": str}, total=False
)


class WorkflowTypeInfosTypeDef(
    _RequiredWorkflowTypeInfosTypeDef, _OptionalWorkflowTypeInfosTypeDef
):
    pass
