"""
Main interface for cloudtrail service type definitions.

Usage::

    from mypy_boto3.cloudtrail.type_defs import ClientAddTagsTagsListTypeDef

    data: ClientAddTagsTagsListTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsTagsListTypeDef",
    "ClientCreateTrailResponseTypeDef",
    "ClientCreateTrailTagsListTypeDef",
    "ClientDescribeTrailsResponsetrailListTypeDef",
    "ClientDescribeTrailsResponseTypeDef",
    "ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    "ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    "ClientGetEventSelectorsResponseTypeDef",
    "ClientGetInsightSelectorsResponseInsightSelectorsTypeDef",
    "ClientGetInsightSelectorsResponseTypeDef",
    "ClientGetTrailResponseTrailTypeDef",
    "ClientGetTrailResponseTypeDef",
    "ClientGetTrailStatusResponseTypeDef",
    "ClientListPublicKeysResponsePublicKeyListTypeDef",
    "ClientListPublicKeysResponseTypeDef",
    "ClientListTagsResponseResourceTagListTagsListTypeDef",
    "ClientListTagsResponseResourceTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListTrailsResponseTrailsTypeDef",
    "ClientListTrailsResponseTypeDef",
    "ClientLookupEventsLookupAttributesTypeDef",
    "ClientLookupEventsResponseEventsResourcesTypeDef",
    "ClientLookupEventsResponseEventsTypeDef",
    "ClientLookupEventsResponseTypeDef",
    "ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    "ClientPutEventSelectorsEventSelectorsTypeDef",
    "ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    "ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    "ClientPutEventSelectorsResponseTypeDef",
    "ClientPutInsightSelectorsInsightSelectorsTypeDef",
    "ClientPutInsightSelectorsResponseInsightSelectorsTypeDef",
    "ClientPutInsightSelectorsResponseTypeDef",
    "ClientRemoveTagsTagsListTypeDef",
    "ClientUpdateTrailResponseTypeDef",
    "PublicKeyTypeDef",
    "ListPublicKeysResponseTypeDef",
    "TagTypeDef",
    "ResourceTagTypeDef",
    "ListTagsResponseTypeDef",
    "TrailInfoTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupAttributeTypeDef",
    "ResourceTypeDef",
    "EventTypeDef",
    "LookupEventsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredClientAddTagsTagsListTypeDef = TypedDict(
    "_RequiredClientAddTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagsListTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsListTypeDef(
    _RequiredClientAddTagsTagsListTypeDef, _OptionalClientAddTagsTagsListTypeDef
):
    pass


ClientCreateTrailResponseTypeDef = TypedDict(
    "ClientCreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

_RequiredClientCreateTrailTagsListTypeDef = TypedDict(
    "_RequiredClientCreateTrailTagsListTypeDef", {"Key": str}
)
_OptionalClientCreateTrailTagsListTypeDef = TypedDict(
    "_OptionalClientCreateTrailTagsListTypeDef", {"Value": str}, total=False
)


class ClientCreateTrailTagsListTypeDef(
    _RequiredClientCreateTrailTagsListTypeDef, _OptionalClientCreateTrailTagsListTypeDef
):
    pass


ClientDescribeTrailsResponsetrailListTypeDef = TypedDict(
    "ClientDescribeTrailsResponsetrailListTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

ClientDescribeTrailsResponseTypeDef = TypedDict(
    "ClientDescribeTrailsResponseTypeDef",
    {"trailList": List[ClientDescribeTrailsResponsetrailListTypeDef]},
    total=False,
)

ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)

ClientGetEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

ClientGetEventSelectorsResponseTypeDef = TypedDict(
    "ClientGetEventSelectorsResponseTypeDef",
    {"TrailARN": str, "EventSelectors": List[ClientGetEventSelectorsResponseEventSelectorsTypeDef]},
    total=False,
)

ClientGetInsightSelectorsResponseInsightSelectorsTypeDef = TypedDict(
    "ClientGetInsightSelectorsResponseInsightSelectorsTypeDef", {"InsightType": str}, total=False
)

ClientGetInsightSelectorsResponseTypeDef = TypedDict(
    "ClientGetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[ClientGetInsightSelectorsResponseInsightSelectorsTypeDef],
    },
    total=False,
)

ClientGetTrailResponseTrailTypeDef = TypedDict(
    "ClientGetTrailResponseTrailTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

ClientGetTrailResponseTypeDef = TypedDict(
    "ClientGetTrailResponseTypeDef", {"Trail": ClientGetTrailResponseTrailTypeDef}, total=False
)

ClientGetTrailStatusResponseTypeDef = TypedDict(
    "ClientGetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
    },
    total=False,
)

ClientListPublicKeysResponsePublicKeyListTypeDef = TypedDict(
    "ClientListPublicKeysResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

ClientListPublicKeysResponseTypeDef = TypedDict(
    "ClientListPublicKeysResponseTypeDef",
    {"PublicKeyList": List[ClientListPublicKeysResponsePublicKeyListTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsResponseResourceTagListTagsListTypeDef = TypedDict(
    "ClientListTagsResponseResourceTagListTagsListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseResourceTagListTypeDef = TypedDict(
    "ClientListTagsResponseResourceTagListTypeDef",
    {"ResourceId": str, "TagsList": List[ClientListTagsResponseResourceTagListTagsListTypeDef]},
    total=False,
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"ResourceTagList": List[ClientListTagsResponseResourceTagListTypeDef], "NextToken": str},
    total=False,
)

ClientListTrailsResponseTrailsTypeDef = TypedDict(
    "ClientListTrailsResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)

ClientListTrailsResponseTypeDef = TypedDict(
    "ClientListTrailsResponseTypeDef",
    {"Trails": List[ClientListTrailsResponseTrailsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientLookupEventsLookupAttributesTypeDef = TypedDict(
    "_RequiredClientLookupEventsLookupAttributesTypeDef",
    {
        "AttributeKey": Literal[
            "EventId",
            "EventName",
            "ReadOnly",
            "Username",
            "ResourceType",
            "ResourceName",
            "EventSource",
            "AccessKeyId",
        ]
    },
)
_OptionalClientLookupEventsLookupAttributesTypeDef = TypedDict(
    "_OptionalClientLookupEventsLookupAttributesTypeDef", {"AttributeValue": str}, total=False
)


class ClientLookupEventsLookupAttributesTypeDef(
    _RequiredClientLookupEventsLookupAttributesTypeDef,
    _OptionalClientLookupEventsLookupAttributesTypeDef,
):
    pass


ClientLookupEventsResponseEventsResourcesTypeDef = TypedDict(
    "ClientLookupEventsResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)

ClientLookupEventsResponseEventsTypeDef = TypedDict(
    "ClientLookupEventsResponseEventsTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[ClientLookupEventsResponseEventsResourcesTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)

ClientLookupEventsResponseTypeDef = TypedDict(
    "ClientLookupEventsResponseTypeDef",
    {"Events": List[ClientLookupEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)

ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef = TypedDict(
    "ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)

ClientPutEventSelectorsEventSelectorsTypeDef = TypedDict(
    "ClientPutEventSelectorsEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)

ClientPutEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

ClientPutEventSelectorsResponseTypeDef = TypedDict(
    "ClientPutEventSelectorsResponseTypeDef",
    {"TrailARN": str, "EventSelectors": List[ClientPutEventSelectorsResponseEventSelectorsTypeDef]},
    total=False,
)

ClientPutInsightSelectorsInsightSelectorsTypeDef = TypedDict(
    "ClientPutInsightSelectorsInsightSelectorsTypeDef", {"InsightType": str}, total=False
)

ClientPutInsightSelectorsResponseInsightSelectorsTypeDef = TypedDict(
    "ClientPutInsightSelectorsResponseInsightSelectorsTypeDef", {"InsightType": str}, total=False
)

ClientPutInsightSelectorsResponseTypeDef = TypedDict(
    "ClientPutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[ClientPutInsightSelectorsResponseInsightSelectorsTypeDef],
    },
    total=False,
)

_RequiredClientRemoveTagsTagsListTypeDef = TypedDict(
    "_RequiredClientRemoveTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsTagsListTypeDef = TypedDict(
    "_OptionalClientRemoveTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsTagsListTypeDef(
    _RequiredClientRemoveTagsTagsListTypeDef, _OptionalClientRemoveTagsTagsListTypeDef
):
    pass


ClientUpdateTrailResponseTypeDef = TypedDict(
    "ClientUpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Value": Union[bytes, IO],
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {"PublicKeyList": List[PublicKeyTypeDef], "NextToken": str},
    total=False,
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef", {"ResourceId": str, "TagsList": List[TagTypeDef]}, total=False
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {"ResourceTagList": List[ResourceTagTypeDef], "NextToken": str},
    total=False,
)

TrailInfoTypeDef = TypedDict(
    "TrailInfoTypeDef", {"TrailARN": str, "Name": str, "HomeRegion": str}, total=False
)

ListTrailsResponseTypeDef = TypedDict(
    "ListTrailsResponseTypeDef", {"Trails": List[TrailInfoTypeDef], "NextToken": str}, total=False
)

LookupAttributeTypeDef = TypedDict(
    "LookupAttributeTypeDef",
    {
        "AttributeKey": Literal[
            "EventId",
            "EventName",
            "ReadOnly",
            "Username",
            "ResourceType",
            "ResourceName",
            "EventSource",
            "AccessKeyId",
        ],
        "AttributeValue": str,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef", {"ResourceType": str, "ResourceName": str}, total=False
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[ResourceTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)

LookupEventsResponseTypeDef = TypedDict(
    "LookupEventsResponseTypeDef", {"Events": List[EventTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
