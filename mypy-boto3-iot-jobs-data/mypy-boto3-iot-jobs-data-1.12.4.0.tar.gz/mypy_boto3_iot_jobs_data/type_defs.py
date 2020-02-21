"""
Main interface for iot-jobs-data service type definitions.

Usage::

    from mypy_boto3.iot_jobs_data.type_defs import ClientDescribeJobExecutionResponseexecutionTypeDef

    data: ClientDescribeJobExecutionResponseexecutionTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeJobExecutionResponseexecutionTypeDef",
    "ClientDescribeJobExecutionResponseTypeDef",
    "ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef",
    "ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef",
    "ClientGetPendingJobExecutionsResponseTypeDef",
    "ClientStartNextPendingJobExecutionResponseexecutionTypeDef",
    "ClientStartNextPendingJobExecutionResponseTypeDef",
    "ClientUpdateJobExecutionResponseexecutionStateTypeDef",
    "ClientUpdateJobExecutionResponseTypeDef",
)

ClientDescribeJobExecutionResponseexecutionTypeDef = TypedDict(
    "ClientDescribeJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)

ClientDescribeJobExecutionResponseTypeDef = TypedDict(
    "ClientDescribeJobExecutionResponseTypeDef",
    {"execution": ClientDescribeJobExecutionResponseexecutionTypeDef},
    total=False,
)

ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef = TypedDict(
    "ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)

ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef = TypedDict(
    "ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)

ClientGetPendingJobExecutionsResponseTypeDef = TypedDict(
    "ClientGetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List[ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef],
        "queuedJobs": List[ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef],
    },
    total=False,
)

ClientStartNextPendingJobExecutionResponseexecutionTypeDef = TypedDict(
    "ClientStartNextPendingJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)

ClientStartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "ClientStartNextPendingJobExecutionResponseTypeDef",
    {"execution": ClientStartNextPendingJobExecutionResponseexecutionTypeDef},
    total=False,
)

ClientUpdateJobExecutionResponseexecutionStateTypeDef = TypedDict(
    "ClientUpdateJobExecutionResponseexecutionStateTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "statusDetails": Dict[str, str],
        "versionNumber": int,
    },
    total=False,
)

ClientUpdateJobExecutionResponseTypeDef = TypedDict(
    "ClientUpdateJobExecutionResponseTypeDef",
    {"executionState": ClientUpdateJobExecutionResponseexecutionStateTypeDef, "jobDocument": str},
    total=False,
)
