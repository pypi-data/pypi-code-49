"""
Main interface for accessanalyzer service type definitions.

Usage::

    from mypy_boto3.accessanalyzer.type_defs import ClientCreateAnalyzerArchiveRulesfilterTypeDef

    data: ClientCreateAnalyzerArchiveRulesfilterTypeDef = {...}
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
    "ClientCreateAnalyzerArchiveRulesfilterTypeDef",
    "ClientCreateAnalyzerArchiveRulesTypeDef",
    "ClientCreateAnalyzerResponseTypeDef",
    "ClientCreateArchiveRuleFilterTypeDef",
    "ClientGetAnalyzedResourceResponseresourceTypeDef",
    "ClientGetAnalyzedResourceResponseTypeDef",
    "ClientGetAnalyzerResponseanalyzerTypeDef",
    "ClientGetAnalyzerResponseTypeDef",
    "ClientGetArchiveRuleResponsearchiveRulefilterTypeDef",
    "ClientGetArchiveRuleResponsearchiveRuleTypeDef",
    "ClientGetArchiveRuleResponseTypeDef",
    "ClientGetFindingResponsefindingTypeDef",
    "ClientGetFindingResponseTypeDef",
    "ClientListAnalyzedResourcesResponseanalyzedResourcesTypeDef",
    "ClientListAnalyzedResourcesResponseTypeDef",
    "ClientListAnalyzersResponseanalyzersTypeDef",
    "ClientListAnalyzersResponseTypeDef",
    "ClientListArchiveRulesResponsearchiveRulesfilterTypeDef",
    "ClientListArchiveRulesResponsearchiveRulesTypeDef",
    "ClientListArchiveRulesResponseTypeDef",
    "ClientListFindingsFilterTypeDef",
    "ClientListFindingsResponsefindingsTypeDef",
    "ClientListFindingsResponseTypeDef",
    "ClientListFindingsSortTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateArchiveRuleFilterTypeDef",
)

ClientCreateAnalyzerArchiveRulesfilterTypeDef = TypedDict(
    "ClientCreateAnalyzerArchiveRulesfilterTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

_RequiredClientCreateAnalyzerArchiveRulesTypeDef = TypedDict(
    "_RequiredClientCreateAnalyzerArchiveRulesTypeDef",
    {"filter": Dict[str, ClientCreateAnalyzerArchiveRulesfilterTypeDef]},
)
_OptionalClientCreateAnalyzerArchiveRulesTypeDef = TypedDict(
    "_OptionalClientCreateAnalyzerArchiveRulesTypeDef", {"ruleName": str}, total=False
)


class ClientCreateAnalyzerArchiveRulesTypeDef(
    _RequiredClientCreateAnalyzerArchiveRulesTypeDef,
    _OptionalClientCreateAnalyzerArchiveRulesTypeDef,
):
    pass


ClientCreateAnalyzerResponseTypeDef = TypedDict(
    "ClientCreateAnalyzerResponseTypeDef", {"arn": str}, total=False
)

ClientCreateArchiveRuleFilterTypeDef = TypedDict(
    "ClientCreateArchiveRuleFilterTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

ClientGetAnalyzedResourceResponseresourceTypeDef = TypedDict(
    "ClientGetAnalyzedResourceResponseresourceTypeDef",
    {
        "actions": List[str],
        "analyzedAt": datetime,
        "createdAt": datetime,
        "error": str,
        "isPublic": bool,
        "resourceArn": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
        "sharedVia": List[str],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
    total=False,
)

ClientGetAnalyzedResourceResponseTypeDef = TypedDict(
    "ClientGetAnalyzedResourceResponseTypeDef",
    {"resource": ClientGetAnalyzedResourceResponseresourceTypeDef},
    total=False,
)

ClientGetAnalyzerResponseanalyzerTypeDef = TypedDict(
    "ClientGetAnalyzerResponseanalyzerTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "name": str,
        "tags": Dict[str, str],
        "type": str,
    },
    total=False,
)

ClientGetAnalyzerResponseTypeDef = TypedDict(
    "ClientGetAnalyzerResponseTypeDef",
    {"analyzer": ClientGetAnalyzerResponseanalyzerTypeDef},
    total=False,
)

ClientGetArchiveRuleResponsearchiveRulefilterTypeDef = TypedDict(
    "ClientGetArchiveRuleResponsearchiveRulefilterTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

ClientGetArchiveRuleResponsearchiveRuleTypeDef = TypedDict(
    "ClientGetArchiveRuleResponsearchiveRuleTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, ClientGetArchiveRuleResponsearchiveRulefilterTypeDef],
        "ruleName": str,
        "updatedAt": datetime,
    },
    total=False,
)

ClientGetArchiveRuleResponseTypeDef = TypedDict(
    "ClientGetArchiveRuleResponseTypeDef",
    {"archiveRule": ClientGetArchiveRuleResponsearchiveRuleTypeDef},
    total=False,
)

ClientGetFindingResponsefindingTypeDef = TypedDict(
    "ClientGetFindingResponsefindingTypeDef",
    {
        "action": List[str],
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "error": str,
        "id": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
    total=False,
)

ClientGetFindingResponseTypeDef = TypedDict(
    "ClientGetFindingResponseTypeDef",
    {"finding": ClientGetFindingResponsefindingTypeDef},
    total=False,
)

ClientListAnalyzedResourcesResponseanalyzedResourcesTypeDef = TypedDict(
    "ClientListAnalyzedResourcesResponseanalyzedResourcesTypeDef",
    {
        "resourceArn": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
    },
    total=False,
)

ClientListAnalyzedResourcesResponseTypeDef = TypedDict(
    "ClientListAnalyzedResourcesResponseTypeDef",
    {
        "analyzedResources": List[ClientListAnalyzedResourcesResponseanalyzedResourcesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListAnalyzersResponseanalyzersTypeDef = TypedDict(
    "ClientListAnalyzersResponseanalyzersTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "name": str,
        "tags": Dict[str, str],
        "type": str,
    },
    total=False,
)

ClientListAnalyzersResponseTypeDef = TypedDict(
    "ClientListAnalyzersResponseTypeDef",
    {"analyzers": List[ClientListAnalyzersResponseanalyzersTypeDef], "nextToken": str},
    total=False,
)

ClientListArchiveRulesResponsearchiveRulesfilterTypeDef = TypedDict(
    "ClientListArchiveRulesResponsearchiveRulesfilterTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

ClientListArchiveRulesResponsearchiveRulesTypeDef = TypedDict(
    "ClientListArchiveRulesResponsearchiveRulesTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, ClientListArchiveRulesResponsearchiveRulesfilterTypeDef],
        "ruleName": str,
        "updatedAt": datetime,
    },
    total=False,
)

ClientListArchiveRulesResponseTypeDef = TypedDict(
    "ClientListArchiveRulesResponseTypeDef",
    {"archiveRules": List[ClientListArchiveRulesResponsearchiveRulesTypeDef], "nextToken": str},
    total=False,
)

ClientListFindingsFilterTypeDef = TypedDict(
    "ClientListFindingsFilterTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)

ClientListFindingsResponsefindingsTypeDef = TypedDict(
    "ClientListFindingsResponsefindingsTypeDef",
    {
        "action": List[str],
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "error": str,
        "id": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "resourceType": Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ],
        "status": Literal["ACTIVE", "ARCHIVED", "RESOLVED"],
        "updatedAt": datetime,
    },
    total=False,
)

ClientListFindingsResponseTypeDef = TypedDict(
    "ClientListFindingsResponseTypeDef",
    {"findings": List[ClientListFindingsResponsefindingsTypeDef], "nextToken": str},
    total=False,
)

ClientListFindingsSortTypeDef = TypedDict(
    "ClientListFindingsSortTypeDef",
    {"attributeName": str, "orderBy": Literal["ASC", "DESC"]},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientUpdateArchiveRuleFilterTypeDef = TypedDict(
    "ClientUpdateArchiveRuleFilterTypeDef",
    {"contains": List[str], "eq": List[str], "exists": bool, "neq": List[str]},
    total=False,
)
