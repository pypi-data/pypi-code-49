"""
Main interface for codeguruprofiler service type definitions.

Usage::

    from mypy_boto3.codeguruprofiler.type_defs import ClientConfigureAgentResponseconfigurationTypeDef

    data: ClientConfigureAgentResponseconfigurationTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientConfigureAgentResponseconfigurationTypeDef",
    "ClientConfigureAgentResponseTypeDef",
    "ClientCreateProfilingGroupAgentOrchestrationConfigTypeDef",
    "ClientCreateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef",
    "ClientCreateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef",
    "ClientCreateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef",
    "ClientCreateProfilingGroupResponseprofilingGroupTypeDef",
    "ClientCreateProfilingGroupResponseTypeDef",
    "ClientDescribeProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef",
    "ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef",
    "ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatusTypeDef",
    "ClientDescribeProfilingGroupResponseprofilingGroupTypeDef",
    "ClientDescribeProfilingGroupResponseTypeDef",
    "ClientGetProfileResponseTypeDef",
    "ClientListProfileTimesResponseprofileTimesTypeDef",
    "ClientListProfileTimesResponseTypeDef",
    "ClientListProfilingGroupsResponseprofilingGroupsagentOrchestrationConfigTypeDef",
    "ClientListProfilingGroupsResponseprofilingGroupsprofilingStatuslatestAggregatedProfileTypeDef",
    "ClientListProfilingGroupsResponseprofilingGroupsprofilingStatusTypeDef",
    "ClientListProfilingGroupsResponseprofilingGroupsTypeDef",
    "ClientListProfilingGroupsResponseTypeDef",
    "ClientUpdateProfilingGroupAgentOrchestrationConfigTypeDef",
    "ClientUpdateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef",
    "ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef",
    "ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef",
    "ClientUpdateProfilingGroupResponseprofilingGroupTypeDef",
    "ClientUpdateProfilingGroupResponseTypeDef",
)

ClientConfigureAgentResponseconfigurationTypeDef = TypedDict(
    "ClientConfigureAgentResponseconfigurationTypeDef",
    {"periodInSeconds": int, "shouldProfile": bool},
    total=False,
)

ClientConfigureAgentResponseTypeDef = TypedDict(
    "ClientConfigureAgentResponseTypeDef",
    {"configuration": ClientConfigureAgentResponseconfigurationTypeDef},
    total=False,
)

ClientCreateProfilingGroupAgentOrchestrationConfigTypeDef = TypedDict(
    "ClientCreateProfilingGroupAgentOrchestrationConfigTypeDef", {"profilingEnabled": bool}
)

ClientCreateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef = TypedDict(
    "ClientCreateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef",
    {"profilingEnabled": bool},
    total=False,
)

ClientCreateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef = TypedDict(
    "ClientCreateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef",
    {"period": Literal["P1D", "PT1H", "PT5M"], "start": datetime},
    total=False,
)

ClientCreateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef = TypedDict(
    "ClientCreateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": datetime,
        "latestAgentProfileReportedAt": datetime,
        "latestAggregatedProfile": ClientCreateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef,
    },
    total=False,
)

ClientCreateProfilingGroupResponseprofilingGroupTypeDef = TypedDict(
    "ClientCreateProfilingGroupResponseprofilingGroupTypeDef",
    {
        "agentOrchestrationConfig": ClientCreateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef,
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "profilingStatus": ClientCreateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef,
        "updatedAt": datetime,
    },
    total=False,
)

ClientCreateProfilingGroupResponseTypeDef = TypedDict(
    "ClientCreateProfilingGroupResponseTypeDef",
    {"profilingGroup": ClientCreateProfilingGroupResponseprofilingGroupTypeDef},
    total=False,
)

ClientDescribeProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef = TypedDict(
    "ClientDescribeProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef",
    {"profilingEnabled": bool},
    total=False,
)

ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef = TypedDict(
    "ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef",
    {"period": Literal["P1D", "PT1H", "PT5M"], "start": datetime},
    total=False,
)

ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatusTypeDef = TypedDict(
    "ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": datetime,
        "latestAgentProfileReportedAt": datetime,
        "latestAggregatedProfile": ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef,
    },
    total=False,
)

ClientDescribeProfilingGroupResponseprofilingGroupTypeDef = TypedDict(
    "ClientDescribeProfilingGroupResponseprofilingGroupTypeDef",
    {
        "agentOrchestrationConfig": ClientDescribeProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef,
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "profilingStatus": ClientDescribeProfilingGroupResponseprofilingGroupprofilingStatusTypeDef,
        "updatedAt": datetime,
    },
    total=False,
)

ClientDescribeProfilingGroupResponseTypeDef = TypedDict(
    "ClientDescribeProfilingGroupResponseTypeDef",
    {"profilingGroup": ClientDescribeProfilingGroupResponseprofilingGroupTypeDef},
    total=False,
)

ClientGetProfileResponseTypeDef = TypedDict(
    "ClientGetProfileResponseTypeDef",
    {"contentEncoding": str, "contentType": str, "profile": StreamingBody},
    total=False,
)

ClientListProfileTimesResponseprofileTimesTypeDef = TypedDict(
    "ClientListProfileTimesResponseprofileTimesTypeDef", {"start": datetime}, total=False
)

ClientListProfileTimesResponseTypeDef = TypedDict(
    "ClientListProfileTimesResponseTypeDef",
    {"nextToken": str, "profileTimes": List[ClientListProfileTimesResponseprofileTimesTypeDef]},
    total=False,
)

ClientListProfilingGroupsResponseprofilingGroupsagentOrchestrationConfigTypeDef = TypedDict(
    "ClientListProfilingGroupsResponseprofilingGroupsagentOrchestrationConfigTypeDef",
    {"profilingEnabled": bool},
    total=False,
)

ClientListProfilingGroupsResponseprofilingGroupsprofilingStatuslatestAggregatedProfileTypeDef = TypedDict(
    "ClientListProfilingGroupsResponseprofilingGroupsprofilingStatuslatestAggregatedProfileTypeDef",
    {"period": Literal["P1D", "PT1H", "PT5M"], "start": datetime},
    total=False,
)

ClientListProfilingGroupsResponseprofilingGroupsprofilingStatusTypeDef = TypedDict(
    "ClientListProfilingGroupsResponseprofilingGroupsprofilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": datetime,
        "latestAgentProfileReportedAt": datetime,
        "latestAggregatedProfile": ClientListProfilingGroupsResponseprofilingGroupsprofilingStatuslatestAggregatedProfileTypeDef,
    },
    total=False,
)

ClientListProfilingGroupsResponseprofilingGroupsTypeDef = TypedDict(
    "ClientListProfilingGroupsResponseprofilingGroupsTypeDef",
    {
        "agentOrchestrationConfig": ClientListProfilingGroupsResponseprofilingGroupsagentOrchestrationConfigTypeDef,
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "profilingStatus": ClientListProfilingGroupsResponseprofilingGroupsprofilingStatusTypeDef,
        "updatedAt": datetime,
    },
    total=False,
)

ClientListProfilingGroupsResponseTypeDef = TypedDict(
    "ClientListProfilingGroupsResponseTypeDef",
    {
        "nextToken": str,
        "profilingGroupNames": List[str],
        "profilingGroups": List[ClientListProfilingGroupsResponseprofilingGroupsTypeDef],
    },
    total=False,
)

ClientUpdateProfilingGroupAgentOrchestrationConfigTypeDef = TypedDict(
    "ClientUpdateProfilingGroupAgentOrchestrationConfigTypeDef", {"profilingEnabled": bool}
)

ClientUpdateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef = TypedDict(
    "ClientUpdateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef",
    {"profilingEnabled": bool},
    total=False,
)

ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef = TypedDict(
    "ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef",
    {"period": Literal["P1D", "PT1H", "PT5M"], "start": datetime},
    total=False,
)

ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef = TypedDict(
    "ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": datetime,
        "latestAgentProfileReportedAt": datetime,
        "latestAggregatedProfile": ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatuslatestAggregatedProfileTypeDef,
    },
    total=False,
)

ClientUpdateProfilingGroupResponseprofilingGroupTypeDef = TypedDict(
    "ClientUpdateProfilingGroupResponseprofilingGroupTypeDef",
    {
        "agentOrchestrationConfig": ClientUpdateProfilingGroupResponseprofilingGroupagentOrchestrationConfigTypeDef,
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "profilingStatus": ClientUpdateProfilingGroupResponseprofilingGroupprofilingStatusTypeDef,
        "updatedAt": datetime,
    },
    total=False,
)

ClientUpdateProfilingGroupResponseTypeDef = TypedDict(
    "ClientUpdateProfilingGroupResponseTypeDef",
    {"profilingGroup": ClientUpdateProfilingGroupResponseprofilingGroupTypeDef},
    total=False,
)
