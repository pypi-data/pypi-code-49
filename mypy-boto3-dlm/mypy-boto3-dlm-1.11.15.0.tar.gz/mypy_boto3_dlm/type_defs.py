"""
Main interface for dlm service type definitions.

Usage::

    from mypy_boto3.dlm.type_defs import ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef

    data: ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef = {...}
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
    "ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsTypeDef",
    "ClientCreateLifecyclePolicyResponseTypeDef",
    "ClientGetLifecyclePoliciesResponsePoliciesTypeDef",
    "ClientGetLifecyclePoliciesResponseTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsTypeDef",
)

ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef",
    {"Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef",
    {
        "TargetRegion": str,
        "Encrypted": bool,
        "CmkArn": str,
        "CopyTags": bool,
        "RetainRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef,
    },
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"],
        "AvailabilityZones": List[str],
    },
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef],
        "VariableTags": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef],
        "CreateRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
        "FastRestoreRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef,
        "CrossRegionCopyRules": List[
            ClientCreateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef
        ],
    },
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateLifecyclePolicyPolicyDetailsTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List[ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)

ClientCreateLifecyclePolicyResponseTypeDef = TypedDict(
    "ClientCreateLifecyclePolicyResponseTypeDef", {"PolicyId": str}, total=False
)

ClientGetLifecyclePoliciesResponsePoliciesTypeDef = TypedDict(
    "ClientGetLifecyclePoliciesResponsePoliciesTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": Literal["ENABLED", "DISABLED", "ERROR"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetLifecyclePoliciesResponseTypeDef = TypedDict(
    "ClientGetLifecyclePoliciesResponseTypeDef",
    {"Policies": List[ClientGetLifecyclePoliciesResponsePoliciesTypeDef]},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef",
    {"Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef",
    {
        "TargetRegion": str,
        "Encrypted": bool,
        "CmkArn": str,
        "CopyTags": bool,
        "RetainRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef,
    },
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"],
        "AvailabilityZones": List[str],
    },
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef
        ],
        "VariableTags": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef
        ],
        "CreateRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
        "FastRestoreRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef,
        "CrossRegionCopyRules": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef
        ],
    },
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List[ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)

ClientGetLifecyclePolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": Literal["ENABLED", "DISABLED", "ERROR"],
        "StatusMessage": str,
        "ExecutionRoleArn": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "PolicyDetails": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef,
        "Tags": Dict[str, str],
        "PolicyArn": str,
    },
    total=False,
)

ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponseTypeDef",
    {"Policy": ClientGetLifecyclePolicyResponsePolicyTypeDef},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef",
    {"Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef",
    {
        "TargetRegion": str,
        "Encrypted": bool,
        "CmkArn": str,
        "CopyTags": bool,
        "RetainRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesRetainRuleTypeDef,
    },
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"],
        "AvailabilityZones": List[str],
    },
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef],
        "VariableTags": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef],
        "CreateRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
        "FastRestoreRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef,
        "CrossRegionCopyRules": List[
            ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCrossRegionCopyRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateLifecyclePolicyPolicyDetailsTypeDef = TypedDict(
    "ClientUpdateLifecyclePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List[ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)
