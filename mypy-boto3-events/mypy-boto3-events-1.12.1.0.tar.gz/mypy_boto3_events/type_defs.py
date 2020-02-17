"""
Main interface for events service type definitions.

Usage::

    from mypy_boto3.events.type_defs import ClientCreateEventBusResponseTypeDef

    data: ClientCreateEventBusResponseTypeDef = {...}
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
    "ClientCreateEventBusResponseTypeDef",
    "ClientCreatePartnerEventSourceResponseTypeDef",
    "ClientDescribeEventBusResponseTypeDef",
    "ClientDescribeEventSourceResponseTypeDef",
    "ClientDescribePartnerEventSourceResponseTypeDef",
    "ClientDescribeRuleResponseTypeDef",
    "ClientListEventBusesResponseEventBusesTypeDef",
    "ClientListEventBusesResponseTypeDef",
    "ClientListEventSourcesResponseEventSourcesTypeDef",
    "ClientListEventSourcesResponseTypeDef",
    "ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    "ClientListPartnerEventSourceAccountsResponseTypeDef",
    "ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    "ClientListPartnerEventSourcesResponseTypeDef",
    "ClientListRuleNamesByTargetResponseTypeDef",
    "ClientListRulesResponseRulesTypeDef",
    "ClientListRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    "ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsTypeDef",
    "ClientListTargetsByRuleResponseTypeDef",
    "ClientPutEventsEntriesTypeDef",
    "ClientPutEventsResponseEntriesTypeDef",
    "ClientPutEventsResponseTypeDef",
    "ClientPutPartnerEventsEntriesTypeDef",
    "ClientPutPartnerEventsResponseEntriesTypeDef",
    "ClientPutPartnerEventsResponseTypeDef",
    "ClientPutPermissionConditionTypeDef",
    "ClientPutRuleResponseTypeDef",
    "ClientPutRuleTagsTypeDef",
    "ClientPutTargetsResponseFailedEntriesTypeDef",
    "ClientPutTargetsResponseTypeDef",
    "ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef",
    "ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef",
    "ClientPutTargetsTargetsBatchParametersTypeDef",
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    "ClientPutTargetsTargetsEcsParametersTypeDef",
    "ClientPutTargetsTargetsInputTransformerTypeDef",
    "ClientPutTargetsTargetsKinesisParametersTypeDef",
    "ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ClientPutTargetsTargetsRunCommandParametersTypeDef",
    "ClientPutTargetsTargetsSqsParametersTypeDef",
    "ClientPutTargetsTargetsTypeDef",
    "ClientRemoveTargetsResponseFailedEntriesTypeDef",
    "ClientRemoveTargetsResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestEventPatternResponseTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "RuleTypeDef",
    "ListRulesResponseTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchRetryStrategyTypeDef",
    "BatchParametersTypeDef",
    "AwsVpcConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "EcsParametersTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "RunCommandTargetTypeDef",
    "RunCommandParametersTypeDef",
    "SqsParametersTypeDef",
    "TargetTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateEventBusResponseTypeDef = TypedDict(
    "ClientCreateEventBusResponseTypeDef", {"EventBusArn": str}, total=False
)

ClientCreatePartnerEventSourceResponseTypeDef = TypedDict(
    "ClientCreatePartnerEventSourceResponseTypeDef", {"EventSourceArn": str}, total=False
)

ClientDescribeEventBusResponseTypeDef = TypedDict(
    "ClientDescribeEventBusResponseTypeDef", {"Name": str, "Arn": str, "Policy": str}, total=False
)

ClientDescribeEventSourceResponseTypeDef = TypedDict(
    "ClientDescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

ClientDescribePartnerEventSourceResponseTypeDef = TypedDict(
    "ClientDescribePartnerEventSourceResponseTypeDef", {"Arn": str, "Name": str}, total=False
)

ClientDescribeRuleResponseTypeDef = TypedDict(
    "ClientDescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ClientListEventBusesResponseEventBusesTypeDef = TypedDict(
    "ClientListEventBusesResponseEventBusesTypeDef",
    {"Name": str, "Arn": str, "Policy": str},
    total=False,
)

ClientListEventBusesResponseTypeDef = TypedDict(
    "ClientListEventBusesResponseTypeDef",
    {"EventBuses": List[ClientListEventBusesResponseEventBusesTypeDef], "NextToken": str},
    total=False,
)

ClientListEventSourcesResponseEventSourcesTypeDef = TypedDict(
    "ClientListEventSourcesResponseEventSourcesTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

ClientListEventSourcesResponseTypeDef = TypedDict(
    "ClientListEventSourcesResponseTypeDef",
    {"EventSources": List[ClientListEventSourcesResponseEventSourcesTypeDef], "NextToken": str},
    total=False,
)

ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef = TypedDict(
    "ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

ClientListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ClientListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List[
            ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef = TypedDict(
    "ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    {"Arn": str, "Name": str},
    total=False,
)

ClientListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ClientListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List[
            ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ClientListRuleNamesByTargetResponseTypeDef",
    {"RuleNames": List[str], "NextToken": str},
    total=False,
)

ClientListRulesResponseRulesTypeDef = TypedDict(
    "ClientListRulesResponseRulesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ClientListRulesResponseTypeDef = TypedDict(
    "ClientListRulesResponseTypeDef",
    {"Rules": List[ClientListRulesResponseRulesTypeDef], "NextToken": str},
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

ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)

ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)

ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)

ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)

ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)

ClientListTargetsByRuleResponseTargetsTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef,
        "KinesisParameters": ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef,
        "EcsParameters": ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef,
        "BatchParameters": ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef,
        "SqsParameters": ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef,
    },
    total=False,
)

ClientListTargetsByRuleResponseTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTypeDef",
    {"Targets": List[ClientListTargetsByRuleResponseTargetsTypeDef], "NextToken": str},
    total=False,
)

ClientPutEventsEntriesTypeDef = TypedDict(
    "ClientPutEventsEntriesTypeDef",
    {
        "Time": datetime,
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
    },
    total=False,
)

ClientPutEventsResponseEntriesTypeDef = TypedDict(
    "ClientPutEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutEventsResponseTypeDef = TypedDict(
    "ClientPutEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutEventsResponseEntriesTypeDef]},
    total=False,
)

ClientPutPartnerEventsEntriesTypeDef = TypedDict(
    "ClientPutPartnerEventsEntriesTypeDef",
    {"Time": datetime, "Source": str, "Resources": List[str], "DetailType": str, "Detail": str},
    total=False,
)

ClientPutPartnerEventsResponseEntriesTypeDef = TypedDict(
    "ClientPutPartnerEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutPartnerEventsResponseTypeDef = TypedDict(
    "ClientPutPartnerEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutPartnerEventsResponseEntriesTypeDef]},
    total=False,
)

_RequiredClientPutPermissionConditionTypeDef = TypedDict(
    "_RequiredClientPutPermissionConditionTypeDef", {"Type": str}
)
_OptionalClientPutPermissionConditionTypeDef = TypedDict(
    "_OptionalClientPutPermissionConditionTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutPermissionConditionTypeDef(
    _RequiredClientPutPermissionConditionTypeDef, _OptionalClientPutPermissionConditionTypeDef
):
    pass


ClientPutRuleResponseTypeDef = TypedDict(
    "ClientPutRuleResponseTypeDef", {"RuleArn": str}, total=False
)

_RequiredClientPutRuleTagsTypeDef = TypedDict("_RequiredClientPutRuleTagsTypeDef", {"Key": str})
_OptionalClientPutRuleTagsTypeDef = TypedDict(
    "_OptionalClientPutRuleTagsTypeDef", {"Value": str}, total=False
)


class ClientPutRuleTagsTypeDef(
    _RequiredClientPutRuleTagsTypeDef, _OptionalClientPutRuleTagsTypeDef
):
    pass


ClientPutTargetsResponseFailedEntriesTypeDef = TypedDict(
    "ClientPutTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutTargetsResponseTypeDef = TypedDict(
    "ClientPutTargetsResponseTypeDef",
    {"FailedEntryCount": int, "FailedEntries": List[ClientPutTargetsResponseFailedEntriesTypeDef]},
    total=False,
)

ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef", {"Size": int}, total=False
)

ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef", {"Attempts": int}, total=False
)

ClientPutTargetsTargetsBatchParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)

ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientPutTargetsTargetsEcsParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)

ClientPutTargetsTargetsInputTransformerTypeDef = TypedDict(
    "ClientPutTargetsTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)

ClientPutTargetsTargetsKinesisParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsKinesisParametersTypeDef", {"PartitionKeyPath": str}, total=False
)

ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientPutTargetsTargetsRunCommandParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)

ClientPutTargetsTargetsSqsParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsSqsParametersTypeDef", {"MessageGroupId": str}, total=False
)

_RequiredClientPutTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientPutTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ClientPutTargetsTargetsInputTransformerTypeDef,
        "KinesisParameters": ClientPutTargetsTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ClientPutTargetsTargetsRunCommandParametersTypeDef,
        "EcsParameters": ClientPutTargetsTargetsEcsParametersTypeDef,
        "BatchParameters": ClientPutTargetsTargetsBatchParametersTypeDef,
        "SqsParameters": ClientPutTargetsTargetsSqsParametersTypeDef,
    },
    total=False,
)


class ClientPutTargetsTargetsTypeDef(
    _RequiredClientPutTargetsTargetsTypeDef, _OptionalClientPutTargetsTargetsTypeDef
):
    pass


ClientRemoveTargetsResponseFailedEntriesTypeDef = TypedDict(
    "ClientRemoveTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientRemoveTargetsResponseTypeDef = TypedDict(
    "ClientRemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[ClientRemoveTargetsResponseFailedEntriesTypeDef],
    },
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


ClientTestEventPatternResponseTypeDef = TypedDict(
    "ClientTestEventPatternResponseTypeDef", {"Result": bool}, total=False
)

ListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseTypeDef", {"RuleNames": List[str], "NextToken": str}, total=False
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef", {"Rules": List[RuleTypeDef], "NextToken": str}, total=False
)

BatchArrayPropertiesTypeDef = TypedDict("BatchArrayPropertiesTypeDef", {"Size": int}, total=False)

BatchRetryStrategyTypeDef = TypedDict("BatchRetryStrategyTypeDef", {"Attempts": int}, total=False)

_RequiredBatchParametersTypeDef = TypedDict(
    "_RequiredBatchParametersTypeDef", {"JobDefinition": str, "JobName": str}
)
_OptionalBatchParametersTypeDef = TypedDict(
    "_OptionalBatchParametersTypeDef",
    {"ArrayProperties": BatchArrayPropertiesTypeDef, "RetryStrategy": BatchRetryStrategyTypeDef},
    total=False,
)


class BatchParametersTypeDef(_RequiredBatchParametersTypeDef, _OptionalBatchParametersTypeDef):
    pass


_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef", {"Subnets": List[str]}
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {"SecurityGroups": List[str], "AssignPublicIp": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass


NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef", {"awsvpcConfiguration": AwsVpcConfigurationTypeDef}, total=False
)

_RequiredEcsParametersTypeDef = TypedDict(
    "_RequiredEcsParametersTypeDef", {"TaskDefinitionArn": str}
)
_OptionalEcsParametersTypeDef = TypedDict(
    "_OptionalEcsParametersTypeDef",
    {
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)


class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass


_RequiredInputTransformerTypeDef = TypedDict(
    "_RequiredInputTransformerTypeDef", {"InputTemplate": str}
)
_OptionalInputTransformerTypeDef = TypedDict(
    "_OptionalInputTransformerTypeDef", {"InputPathsMap": Dict[str, str]}, total=False
)


class InputTransformerTypeDef(_RequiredInputTransformerTypeDef, _OptionalInputTransformerTypeDef):
    pass


KinesisParametersTypeDef = TypedDict("KinesisParametersTypeDef", {"PartitionKeyPath": str})

RunCommandTargetTypeDef = TypedDict("RunCommandTargetTypeDef", {"Key": str, "Values": List[str]})

RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef", {"RunCommandTargets": List[RunCommandTargetTypeDef]}
)

SqsParametersTypeDef = TypedDict("SqsParametersTypeDef", {"MessageGroupId": str}, total=False)

_RequiredTargetTypeDef = TypedDict("_RequiredTargetTypeDef", {"Id": str, "Arn": str})
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": InputTransformerTypeDef,
        "KinesisParameters": KinesisParametersTypeDef,
        "RunCommandParameters": RunCommandParametersTypeDef,
        "EcsParameters": EcsParametersTypeDef,
        "BatchParameters": BatchParametersTypeDef,
        "SqsParameters": SqsParametersTypeDef,
    },
    total=False,
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


ListTargetsByRuleResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseTypeDef",
    {"Targets": List[TargetTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
