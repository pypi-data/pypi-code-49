"""
Main interface for stepfunctions service type definitions.

Usage::

    from mypy_boto3.stepfunctions.type_defs import ClientCreateActivityResponseTypeDef

    data: ClientCreateActivityResponseTypeDef = {...}
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
    "ClientCreateActivityResponseTypeDef",
    "ClientCreateActivityTagsTypeDef",
    "ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    "ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef",
    "ClientCreateStateMachineLoggingConfigurationTypeDef",
    "ClientCreateStateMachineResponseTypeDef",
    "ClientCreateStateMachineTagsTypeDef",
    "ClientDescribeActivityResponseTypeDef",
    "ClientDescribeExecutionResponseTypeDef",
    "ClientDescribeStateMachineForExecutionResponseTypeDef",
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef",
    "ClientDescribeStateMachineResponseloggingConfigurationTypeDef",
    "ClientDescribeStateMachineResponseTypeDef",
    "ClientGetActivityTaskResponseTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsTypeDef",
    "ClientGetExecutionHistoryResponseTypeDef",
    "ClientListActivitiesResponseactivitiesTypeDef",
    "ClientListActivitiesResponseTypeDef",
    "ClientListExecutionsResponseexecutionsTypeDef",
    "ClientListExecutionsResponseTypeDef",
    "ClientListStateMachinesResponsestateMachinesTypeDef",
    "ClientListStateMachinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartExecutionResponseTypeDef",
    "ClientStopExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    "ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef",
    "ClientUpdateStateMachineLoggingConfigurationTypeDef",
    "ClientUpdateStateMachineResponseTypeDef",
    "ActivityFailedEventDetailsTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "HistoryEventTypeDef",
    "GetExecutionHistoryOutputTypeDef",
    "ActivityListItemTypeDef",
    "ListActivitiesOutputTypeDef",
    "ExecutionListItemTypeDef",
    "ListExecutionsOutputTypeDef",
    "StateMachineListItemTypeDef",
    "ListStateMachinesOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateActivityResponseTypeDef = TypedDict(
    "ClientCreateActivityResponseTypeDef",
    {"activityArn": str, "creationDate": datetime},
    total=False,
)

ClientCreateActivityTagsTypeDef = TypedDict(
    "ClientCreateActivityTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)

ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef = TypedDict(
    "ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientCreateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)

ClientCreateStateMachineLoggingConfigurationTypeDef = TypedDict(
    "ClientCreateStateMachineLoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[ClientCreateStateMachineLoggingConfigurationdestinationsTypeDef],
    },
    total=False,
)

ClientCreateStateMachineResponseTypeDef = TypedDict(
    "ClientCreateStateMachineResponseTypeDef",
    {"stateMachineArn": str, "creationDate": datetime},
    total=False,
)

ClientCreateStateMachineTagsTypeDef = TypedDict(
    "ClientCreateStateMachineTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeActivityResponseTypeDef = TypedDict(
    "ClientDescribeActivityResponseTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)

ClientDescribeExecutionResponseTypeDef = TypedDict(
    "ClientDescribeExecutionResponseTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "output": str,
    },
    total=False,
)

ClientDescribeStateMachineForExecutionResponseTypeDef = TypedDict(
    "ClientDescribeStateMachineForExecutionResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
    },
    total=False,
)

ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)

ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientDescribeStateMachineResponseloggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)

ClientDescribeStateMachineResponseloggingConfigurationTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseloggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[
            ClientDescribeStateMachineResponseloggingConfigurationdestinationsTypeDef
        ],
    },
    total=False,
)

ClientDescribeStateMachineResponseTypeDef = TypedDict(
    "ClientDescribeStateMachineResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": Literal["ACTIVE", "DELETING"],
        "definition": str,
        "roleArn": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
        "loggingConfiguration": ClientDescribeStateMachineResponseloggingConfigurationTypeDef,
    },
    total=False,
)

ClientGetActivityTaskResponseTypeDef = TypedDict(
    "ClientGetActivityTaskResponseTypeDef", {"taskToken": str, "input": str}, total=False
)

ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)

ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)

ClientGetExecutionHistoryResponseeventsTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseeventsTypeDef",
    {
        "timestamp": datetime,
        "type": Literal[
            "ActivityFailed",
            "ActivityScheduled",
            "ActivityScheduleFailed",
            "ActivityStarted",
            "ActivitySucceeded",
            "ActivityTimedOut",
            "ChoiceStateEntered",
            "ChoiceStateExited",
            "ExecutionAborted",
            "ExecutionFailed",
            "ExecutionStarted",
            "ExecutionSucceeded",
            "ExecutionTimedOut",
            "FailStateEntered",
            "LambdaFunctionFailed",
            "LambdaFunctionScheduled",
            "LambdaFunctionScheduleFailed",
            "LambdaFunctionStarted",
            "LambdaFunctionStartFailed",
            "LambdaFunctionSucceeded",
            "LambdaFunctionTimedOut",
            "MapIterationAborted",
            "MapIterationFailed",
            "MapIterationStarted",
            "MapIterationSucceeded",
            "MapStateAborted",
            "MapStateEntered",
            "MapStateExited",
            "MapStateFailed",
            "MapStateStarted",
            "MapStateSucceeded",
            "ParallelStateAborted",
            "ParallelStateEntered",
            "ParallelStateExited",
            "ParallelStateFailed",
            "ParallelStateStarted",
            "ParallelStateSucceeded",
            "PassStateEntered",
            "PassStateExited",
            "SucceedStateEntered",
            "SucceedStateExited",
            "TaskFailed",
            "TaskScheduled",
            "TaskStarted",
            "TaskStartFailed",
            "TaskStateAborted",
            "TaskStateEntered",
            "TaskStateExited",
            "TaskSubmitFailed",
            "TaskSubmitted",
            "TaskSucceeded",
            "TaskTimedOut",
            "WaitStateAborted",
            "WaitStateEntered",
            "WaitStateExited",
        ],
        "id": int,
        "previousEventId": int,
        "activityFailedEventDetails": ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef,
        "mapIterationFailedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef,
    },
    total=False,
)

ClientGetExecutionHistoryResponseTypeDef = TypedDict(
    "ClientGetExecutionHistoryResponseTypeDef",
    {"events": List[ClientGetExecutionHistoryResponseeventsTypeDef], "nextToken": str},
    total=False,
)

ClientListActivitiesResponseactivitiesTypeDef = TypedDict(
    "ClientListActivitiesResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)

ClientListActivitiesResponseTypeDef = TypedDict(
    "ClientListActivitiesResponseTypeDef",
    {"activities": List[ClientListActivitiesResponseactivitiesTypeDef], "nextToken": str},
    total=False,
)

ClientListExecutionsResponseexecutionsTypeDef = TypedDict(
    "ClientListExecutionsResponseexecutionsTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
        "stopDate": datetime,
    },
    total=False,
)

ClientListExecutionsResponseTypeDef = TypedDict(
    "ClientListExecutionsResponseTypeDef",
    {"executions": List[ClientListExecutionsResponseexecutionsTypeDef], "nextToken": str},
    total=False,
)

ClientListStateMachinesResponsestateMachinesTypeDef = TypedDict(
    "ClientListStateMachinesResponsestateMachinesTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
    total=False,
)

ClientListStateMachinesResponseTypeDef = TypedDict(
    "ClientListStateMachinesResponseTypeDef",
    {"stateMachines": List[ClientListStateMachinesResponsestateMachinesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientStartExecutionResponseTypeDef = TypedDict(
    "ClientStartExecutionResponseTypeDef", {"executionArn": str, "startDate": datetime}, total=False
)

ClientStopExecutionResponseTypeDef = TypedDict(
    "ClientStopExecutionResponseTypeDef", {"stopDate": datetime}, total=False
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef = TypedDict(
    "ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef",
    {"logGroupArn": str},
    total=False,
)

ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef = TypedDict(
    "ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef",
    {
        "cloudWatchLogsLogGroup": ClientUpdateStateMachineLoggingConfigurationdestinationscloudWatchLogsLogGroupTypeDef
    },
    total=False,
)

ClientUpdateStateMachineLoggingConfigurationTypeDef = TypedDict(
    "ClientUpdateStateMachineLoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List[ClientUpdateStateMachineLoggingConfigurationdestinationsTypeDef],
    },
    total=False,
)

ClientUpdateStateMachineResponseTypeDef = TypedDict(
    "ClientUpdateStateMachineResponseTypeDef", {"updateDate": datetime}, total=False
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

_RequiredActivityScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredActivityScheduledEventDetailsTypeDef", {"resource": str}
)
_OptionalActivityScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalActivityScheduledEventDetailsTypeDef",
    {"input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)


class ActivityScheduledEventDetailsTypeDef(
    _RequiredActivityScheduledEventDetailsTypeDef, _OptionalActivityScheduledEventDetailsTypeDef
):
    pass


ActivityStartedEventDetailsTypeDef = TypedDict(
    "ActivityStartedEventDetailsTypeDef", {"workerName": str}, total=False
)

ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef", {"output": str}, total=False
)

ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef", {"input": str, "roleArn": str}, total=False
)

ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef", {"output": str}, total=False
)

ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

LambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

_RequiredLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventDetailsTypeDef", {"resource": str}
)
_OptionalLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventDetailsTypeDef",
    {"input": str, "timeoutInSeconds": int},
    total=False,
)


class LambdaFunctionScheduledEventDetailsTypeDef(
    _RequiredLambdaFunctionScheduledEventDetailsTypeDef,
    _OptionalLambdaFunctionScheduledEventDetailsTypeDef,
):
    pass


LambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionStartFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef", {"output": str}, total=False
)

LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef", {"name": str, "index": int}, total=False
)

MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef", {"length": int}, total=False
)

_RequiredStateEnteredEventDetailsTypeDef = TypedDict(
    "_RequiredStateEnteredEventDetailsTypeDef", {"name": str}
)
_OptionalStateEnteredEventDetailsTypeDef = TypedDict(
    "_OptionalStateEnteredEventDetailsTypeDef", {"input": str}, total=False
)


class StateEnteredEventDetailsTypeDef(
    _RequiredStateEnteredEventDetailsTypeDef, _OptionalStateEnteredEventDetailsTypeDef
):
    pass


_RequiredStateExitedEventDetailsTypeDef = TypedDict(
    "_RequiredStateExitedEventDetailsTypeDef", {"name": str}
)
_OptionalStateExitedEventDetailsTypeDef = TypedDict(
    "_OptionalStateExitedEventDetailsTypeDef", {"output": str}, total=False
)


class StateExitedEventDetailsTypeDef(
    _RequiredStateExitedEventDetailsTypeDef, _OptionalStateExitedEventDetailsTypeDef
):
    pass


_RequiredTaskFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskFailedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskFailedEventDetailsTypeDef(
    _RequiredTaskFailedEventDetailsTypeDef, _OptionalTaskFailedEventDetailsTypeDef
):
    pass


_RequiredTaskScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredTaskScheduledEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "region": str, "parameters": str},
)
_OptionalTaskScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalTaskScheduledEventDetailsTypeDef", {"timeoutInSeconds": int}, total=False
)


class TaskScheduledEventDetailsTypeDef(
    _RequiredTaskScheduledEventDetailsTypeDef, _OptionalTaskScheduledEventDetailsTypeDef
):
    pass


_RequiredTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskStartFailedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskStartFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskStartFailedEventDetailsTypeDef(
    _RequiredTaskStartFailedEventDetailsTypeDef, _OptionalTaskStartFailedEventDetailsTypeDef
):
    pass


TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)

_RequiredTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmitFailedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmitFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskSubmitFailedEventDetailsTypeDef(
    _RequiredTaskSubmitFailedEventDetailsTypeDef, _OptionalTaskSubmitFailedEventDetailsTypeDef
):
    pass


_RequiredTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmittedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmittedEventDetailsTypeDef", {"output": str}, total=False
)


class TaskSubmittedEventDetailsTypeDef(
    _RequiredTaskSubmittedEventDetailsTypeDef, _OptionalTaskSubmittedEventDetailsTypeDef
):
    pass


_RequiredTaskSucceededEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSucceededEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskSucceededEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSucceededEventDetailsTypeDef", {"output": str}, total=False
)


class TaskSucceededEventDetailsTypeDef(
    _RequiredTaskSucceededEventDetailsTypeDef, _OptionalTaskSucceededEventDetailsTypeDef
):
    pass


_RequiredTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_RequiredTaskTimedOutEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_OptionalTaskTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskTimedOutEventDetailsTypeDef(
    _RequiredTaskTimedOutEventDetailsTypeDef, _OptionalTaskTimedOutEventDetailsTypeDef
):
    pass


_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": Literal[
            "ActivityFailed",
            "ActivityScheduled",
            "ActivityScheduleFailed",
            "ActivityStarted",
            "ActivitySucceeded",
            "ActivityTimedOut",
            "ChoiceStateEntered",
            "ChoiceStateExited",
            "ExecutionAborted",
            "ExecutionFailed",
            "ExecutionStarted",
            "ExecutionSucceeded",
            "ExecutionTimedOut",
            "FailStateEntered",
            "LambdaFunctionFailed",
            "LambdaFunctionScheduled",
            "LambdaFunctionScheduleFailed",
            "LambdaFunctionStarted",
            "LambdaFunctionStartFailed",
            "LambdaFunctionSucceeded",
            "LambdaFunctionTimedOut",
            "MapIterationAborted",
            "MapIterationFailed",
            "MapIterationStarted",
            "MapIterationSucceeded",
            "MapStateAborted",
            "MapStateEntered",
            "MapStateExited",
            "MapStateFailed",
            "MapStateStarted",
            "MapStateSucceeded",
            "ParallelStateAborted",
            "ParallelStateEntered",
            "ParallelStateExited",
            "ParallelStateFailed",
            "ParallelStateStarted",
            "ParallelStateSucceeded",
            "PassStateEntered",
            "PassStateExited",
            "SucceedStateEntered",
            "SucceedStateExited",
            "TaskFailed",
            "TaskScheduled",
            "TaskStarted",
            "TaskStartFailed",
            "TaskStateAborted",
            "TaskStateEntered",
            "TaskStateExited",
            "TaskSubmitFailed",
            "TaskSubmitted",
            "TaskSucceeded",
            "TaskTimedOut",
            "WaitStateAborted",
            "WaitStateEntered",
            "WaitStateExited",
        ],
        "id": int,
    },
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "previousEventId": int,
        "activityFailedEventDetails": ActivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": ActivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": ActivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": ActivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": ActivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": ActivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": TaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": TaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": TaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": TaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": TaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": TaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": TaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": TaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": ExecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": ExecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": ExecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": ExecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": ExecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": MapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": MapIterationEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": MapIterationEventDetailsTypeDef,
        "mapIterationFailedEventDetails": MapIterationEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": MapIterationEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": LambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": LambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": LambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": LambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": LambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": LambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": StateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": StateExitedEventDetailsTypeDef,
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


_RequiredGetExecutionHistoryOutputTypeDef = TypedDict(
    "_RequiredGetExecutionHistoryOutputTypeDef", {"events": List[HistoryEventTypeDef]}
)
_OptionalGetExecutionHistoryOutputTypeDef = TypedDict(
    "_OptionalGetExecutionHistoryOutputTypeDef", {"nextToken": str}, total=False
)


class GetExecutionHistoryOutputTypeDef(
    _RequiredGetExecutionHistoryOutputTypeDef, _OptionalGetExecutionHistoryOutputTypeDef
):
    pass


ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef", {"activityArn": str, "name": str, "creationDate": datetime}
)

_RequiredListActivitiesOutputTypeDef = TypedDict(
    "_RequiredListActivitiesOutputTypeDef", {"activities": List[ActivityListItemTypeDef]}
)
_OptionalListActivitiesOutputTypeDef = TypedDict(
    "_OptionalListActivitiesOutputTypeDef", {"nextToken": str}, total=False
)


class ListActivitiesOutputTypeDef(
    _RequiredListActivitiesOutputTypeDef, _OptionalListActivitiesOutputTypeDef
):
    pass


_RequiredExecutionListItemTypeDef = TypedDict(
    "_RequiredExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
    },
)
_OptionalExecutionListItemTypeDef = TypedDict(
    "_OptionalExecutionListItemTypeDef", {"stopDate": datetime}, total=False
)


class ExecutionListItemTypeDef(
    _RequiredExecutionListItemTypeDef, _OptionalExecutionListItemTypeDef
):
    pass


_RequiredListExecutionsOutputTypeDef = TypedDict(
    "_RequiredListExecutionsOutputTypeDef", {"executions": List[ExecutionListItemTypeDef]}
)
_OptionalListExecutionsOutputTypeDef = TypedDict(
    "_OptionalListExecutionsOutputTypeDef", {"nextToken": str}, total=False
)


class ListExecutionsOutputTypeDef(
    _RequiredListExecutionsOutputTypeDef, _OptionalListExecutionsOutputTypeDef
):
    pass


StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
)

_RequiredListStateMachinesOutputTypeDef = TypedDict(
    "_RequiredListStateMachinesOutputTypeDef", {"stateMachines": List[StateMachineListItemTypeDef]}
)
_OptionalListStateMachinesOutputTypeDef = TypedDict(
    "_OptionalListStateMachinesOutputTypeDef", {"nextToken": str}, total=False
)


class ListStateMachinesOutputTypeDef(
    _RequiredListStateMachinesOutputTypeDef, _OptionalListStateMachinesOutputTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
