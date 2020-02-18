"""
Main interface for application-insights service type definitions.

Usage::

    from mypy_boto3.application_insights.type_defs import ClientCreateApplicationResponseApplicationInfoTypeDef

    data: ClientCreateApplicationResponseApplicationInfoTypeDef = {...}
"""
from datetime import datetime
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
    "ClientCreateApplicationResponseApplicationInfoTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateLogPatternResponseLogPatternTypeDef",
    "ClientCreateLogPatternResponseTypeDef",
    "ClientDescribeApplicationResponseApplicationInfoTypeDef",
    "ClientDescribeApplicationResponseTypeDef",
    "ClientDescribeComponentConfigurationRecommendationResponseTypeDef",
    "ClientDescribeComponentConfigurationResponseTypeDef",
    "ClientDescribeComponentResponseApplicationComponentTypeDef",
    "ClientDescribeComponentResponseTypeDef",
    "ClientDescribeLogPatternResponseLogPatternTypeDef",
    "ClientDescribeLogPatternResponseTypeDef",
    "ClientDescribeObservationResponseObservationTypeDef",
    "ClientDescribeObservationResponseTypeDef",
    "ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef",
    "ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef",
    "ClientDescribeProblemObservationsResponseTypeDef",
    "ClientDescribeProblemResponseProblemTypeDef",
    "ClientDescribeProblemResponseTypeDef",
    "ClientListApplicationsResponseApplicationInfoListTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListComponentsResponseApplicationComponentListTypeDef",
    "ClientListComponentsResponseTypeDef",
    "ClientListConfigurationHistoryResponseEventListTypeDef",
    "ClientListConfigurationHistoryResponseTypeDef",
    "ClientListLogPatternSetsResponseTypeDef",
    "ClientListLogPatternsResponseLogPatternsTypeDef",
    "ClientListLogPatternsResponseTypeDef",
    "ClientListProblemsResponseProblemListTypeDef",
    "ClientListProblemsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateApplicationResponseApplicationInfoTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ClientUpdateLogPatternResponseLogPatternTypeDef",
    "ClientUpdateLogPatternResponseTypeDef",
)

ClientCreateApplicationResponseApplicationInfoTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef",
    {"ApplicationInfo": ClientCreateApplicationResponseApplicationInfoTypeDef},
    total=False,
)

_RequiredClientCreateApplicationTagsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationTagsTypeDef", {"Key": str}
)
_OptionalClientCreateApplicationTagsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(
    _RequiredClientCreateApplicationTagsTypeDef, _OptionalClientCreateApplicationTagsTypeDef
):
    pass


ClientCreateLogPatternResponseLogPatternTypeDef = TypedDict(
    "ClientCreateLogPatternResponseLogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)

ClientCreateLogPatternResponseTypeDef = TypedDict(
    "ClientCreateLogPatternResponseTypeDef",
    {"LogPattern": ClientCreateLogPatternResponseLogPatternTypeDef, "ResourceGroupName": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationInfoTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ClientDescribeApplicationResponseTypeDef = TypedDict(
    "ClientDescribeApplicationResponseTypeDef",
    {"ApplicationInfo": ClientDescribeApplicationResponseApplicationInfoTypeDef},
    total=False,
)

ClientDescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "ClientDescribeComponentConfigurationRecommendationResponseTypeDef",
    {"ComponentConfiguration": str},
    total=False,
)

ClientDescribeComponentConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeComponentConfigurationResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
        "ComponentConfiguration": str,
    },
    total=False,
)

ClientDescribeComponentResponseApplicationComponentTypeDef = TypedDict(
    "ClientDescribeComponentResponseApplicationComponentTypeDef",
    {
        "ComponentName": str,
        "ResourceType": str,
        "Tier": Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
        "Monitor": bool,
    },
    total=False,
)

ClientDescribeComponentResponseTypeDef = TypedDict(
    "ClientDescribeComponentResponseTypeDef",
    {
        "ApplicationComponent": ClientDescribeComponentResponseApplicationComponentTypeDef,
        "ResourceList": List[str],
    },
    total=False,
)

ClientDescribeLogPatternResponseLogPatternTypeDef = TypedDict(
    "ClientDescribeLogPatternResponseLogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)

ClientDescribeLogPatternResponseTypeDef = TypedDict(
    "ClientDescribeLogPatternResponseTypeDef",
    {"ResourceGroupName": str, "LogPattern": ClientDescribeLogPatternResponseLogPatternTypeDef},
    total=False,
)

ClientDescribeObservationResponseObservationTypeDef = TypedDict(
    "ClientDescribeObservationResponseObservationTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": Literal["ERROR", "WARN", "INFO"],
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
    },
    total=False,
)

ClientDescribeObservationResponseTypeDef = TypedDict(
    "ClientDescribeObservationResponseTypeDef",
    {"Observation": ClientDescribeObservationResponseObservationTypeDef},
    total=False,
)

ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef = TypedDict(
    "ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": Literal["ERROR", "WARN", "INFO"],
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
    },
    total=False,
)

ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef = TypedDict(
    "ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef",
    {
        "ObservationList": List[
            ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef
        ]
    },
    total=False,
)

ClientDescribeProblemObservationsResponseTypeDef = TypedDict(
    "ClientDescribeProblemObservationsResponseTypeDef",
    {"RelatedObservations": ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef},
    total=False,
)

ClientDescribeProblemResponseProblemTypeDef = TypedDict(
    "ClientDescribeProblemResponseProblemTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": Literal["IGNORE", "RESOLVED", "PENDING"],
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": Literal["Low", "Medium", "High"],
        "ResourceGroupName": str,
        "Feedback": Dict[str, Literal["NOT_SPECIFIED", "USEFUL", "NOT_USEFUL"]],
    },
    total=False,
)

ClientDescribeProblemResponseTypeDef = TypedDict(
    "ClientDescribeProblemResponseTypeDef",
    {"Problem": ClientDescribeProblemResponseProblemTypeDef},
    total=False,
)

ClientListApplicationsResponseApplicationInfoListTypeDef = TypedDict(
    "ClientListApplicationsResponseApplicationInfoListTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ClientListApplicationsResponseTypeDef = TypedDict(
    "ClientListApplicationsResponseTypeDef",
    {
        "ApplicationInfoList": List[ClientListApplicationsResponseApplicationInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListComponentsResponseApplicationComponentListTypeDef = TypedDict(
    "ClientListComponentsResponseApplicationComponentListTypeDef",
    {
        "ComponentName": str,
        "ResourceType": str,
        "Tier": Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
        "Monitor": bool,
    },
    total=False,
)

ClientListComponentsResponseTypeDef = TypedDict(
    "ClientListComponentsResponseTypeDef",
    {
        "ApplicationComponentList": List[
            ClientListComponentsResponseApplicationComponentListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListConfigurationHistoryResponseEventListTypeDef = TypedDict(
    "ClientListConfigurationHistoryResponseEventListTypeDef",
    {
        "MonitoredResourceARN": str,
        "EventStatus": Literal["INFO", "WARN", "ERROR"],
        "EventResourceType": Literal["CLOUDWATCH_ALARM", "CLOUDFORMATION", "SSM_ASSOCIATION"],
        "EventTime": datetime,
        "EventDetail": str,
        "EventResourceName": str,
    },
    total=False,
)

ClientListConfigurationHistoryResponseTypeDef = TypedDict(
    "ClientListConfigurationHistoryResponseTypeDef",
    {"EventList": List[ClientListConfigurationHistoryResponseEventListTypeDef], "NextToken": str},
    total=False,
)

ClientListLogPatternSetsResponseTypeDef = TypedDict(
    "ClientListLogPatternSetsResponseTypeDef",
    {"ResourceGroupName": str, "LogPatternSets": List[str], "NextToken": str},
    total=False,
)

ClientListLogPatternsResponseLogPatternsTypeDef = TypedDict(
    "ClientListLogPatternsResponseLogPatternsTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)

ClientListLogPatternsResponseTypeDef = TypedDict(
    "ClientListLogPatternsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatterns": List[ClientListLogPatternsResponseLogPatternsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListProblemsResponseProblemListTypeDef = TypedDict(
    "ClientListProblemsResponseProblemListTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": Literal["IGNORE", "RESOLVED", "PENDING"],
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": Literal["Low", "Medium", "High"],
        "ResourceGroupName": str,
        "Feedback": Dict[str, Literal["NOT_SPECIFIED", "USEFUL", "NOT_USEFUL"]],
    },
    total=False,
)

ClientListProblemsResponseTypeDef = TypedDict(
    "ClientListProblemsResponseTypeDef",
    {"ProblemList": List[ClientListProblemsResponseProblemListTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateApplicationResponseApplicationInfoTypeDef = TypedDict(
    "ClientUpdateApplicationResponseApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ClientUpdateApplicationResponseTypeDef = TypedDict(
    "ClientUpdateApplicationResponseTypeDef",
    {"ApplicationInfo": ClientUpdateApplicationResponseApplicationInfoTypeDef},
    total=False,
)

ClientUpdateLogPatternResponseLogPatternTypeDef = TypedDict(
    "ClientUpdateLogPatternResponseLogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)

ClientUpdateLogPatternResponseTypeDef = TypedDict(
    "ClientUpdateLogPatternResponseTypeDef",
    {"ResourceGroupName": str, "LogPattern": ClientUpdateLogPatternResponseLogPatternTypeDef},
    total=False,
)
