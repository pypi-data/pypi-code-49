"""
Main interface for kinesisvideo service type definitions.

Usage::

    from mypy_boto3.kinesisvideo.type_defs import ChannelNameConditionTypeDef

    data: ChannelNameConditionTypeDef = {...}
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
    "ChannelNameConditionTypeDef",
    "ClientCreateSignalingChannelResponseTypeDef",
    "ClientCreateSignalingChannelSingleMasterConfigurationTypeDef",
    "ClientCreateSignalingChannelTagsTypeDef",
    "ClientCreateStreamResponseTypeDef",
    "ClientDescribeSignalingChannelResponseChannelInfoSingleMasterConfigurationTypeDef",
    "ClientDescribeSignalingChannelResponseChannelInfoTypeDef",
    "ClientDescribeSignalingChannelResponseTypeDef",
    "ClientDescribeStreamResponseStreamInfoTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientGetDataEndpointResponseTypeDef",
    "ClientGetSignalingChannelEndpointResponseResourceEndpointListTypeDef",
    "ClientGetSignalingChannelEndpointResponseTypeDef",
    "ClientGetSignalingChannelEndpointSingleMasterChannelEndpointConfigurationTypeDef",
    "ClientListSignalingChannelsChannelNameConditionTypeDef",
    "ClientListSignalingChannelsResponseChannelInfoListSingleMasterConfigurationTypeDef",
    "ClientListSignalingChannelsResponseChannelInfoListTypeDef",
    "ClientListSignalingChannelsResponseTypeDef",
    "ClientListStreamsResponseStreamInfoListTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListStreamsStreamNameConditionTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTagsForStreamResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateSignalingChannelSingleMasterConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "ChannelInfoTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "StreamInfoTypeDef",
    "ListStreamsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "StreamNameConditionTypeDef",
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {"ComparisonOperator": Literal["BEGINS_WITH"], "ComparisonValue": str},
    total=False,
)

ClientCreateSignalingChannelResponseTypeDef = TypedDict(
    "ClientCreateSignalingChannelResponseTypeDef", {"ChannelARN": str}, total=False
)

ClientCreateSignalingChannelSingleMasterConfigurationTypeDef = TypedDict(
    "ClientCreateSignalingChannelSingleMasterConfigurationTypeDef",
    {"MessageTtlSeconds": int},
    total=False,
)

_RequiredClientCreateSignalingChannelTagsTypeDef = TypedDict(
    "_RequiredClientCreateSignalingChannelTagsTypeDef", {"Key": str}
)
_OptionalClientCreateSignalingChannelTagsTypeDef = TypedDict(
    "_OptionalClientCreateSignalingChannelTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateSignalingChannelTagsTypeDef(
    _RequiredClientCreateSignalingChannelTagsTypeDef,
    _OptionalClientCreateSignalingChannelTagsTypeDef,
):
    pass


ClientCreateStreamResponseTypeDef = TypedDict(
    "ClientCreateStreamResponseTypeDef", {"StreamARN": str}, total=False
)

ClientDescribeSignalingChannelResponseChannelInfoSingleMasterConfigurationTypeDef = TypedDict(
    "ClientDescribeSignalingChannelResponseChannelInfoSingleMasterConfigurationTypeDef",
    {"MessageTtlSeconds": int},
    total=False,
)

ClientDescribeSignalingChannelResponseChannelInfoTypeDef = TypedDict(
    "ClientDescribeSignalingChannelResponseChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": str,
        "ChannelStatus": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "SingleMasterConfiguration": ClientDescribeSignalingChannelResponseChannelInfoSingleMasterConfigurationTypeDef,
        "Version": str,
    },
    total=False,
)

ClientDescribeSignalingChannelResponseTypeDef = TypedDict(
    "ClientDescribeSignalingChannelResponseTypeDef",
    {"ChannelInfo": ClientDescribeSignalingChannelResponseChannelInfoTypeDef},
    total=False,
)

ClientDescribeStreamResponseStreamInfoTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

ClientDescribeStreamResponseTypeDef = TypedDict(
    "ClientDescribeStreamResponseTypeDef",
    {"StreamInfo": ClientDescribeStreamResponseStreamInfoTypeDef},
    total=False,
)

ClientGetDataEndpointResponseTypeDef = TypedDict(
    "ClientGetDataEndpointResponseTypeDef", {"DataEndpoint": str}, total=False
)

ClientGetSignalingChannelEndpointResponseResourceEndpointListTypeDef = TypedDict(
    "ClientGetSignalingChannelEndpointResponseResourceEndpointListTypeDef",
    {"Protocol": Literal["WSS", "HTTPS"], "ResourceEndpoint": str},
    total=False,
)

ClientGetSignalingChannelEndpointResponseTypeDef = TypedDict(
    "ClientGetSignalingChannelEndpointResponseTypeDef",
    {
        "ResourceEndpointList": List[
            ClientGetSignalingChannelEndpointResponseResourceEndpointListTypeDef
        ]
    },
    total=False,
)

ClientGetSignalingChannelEndpointSingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "ClientGetSignalingChannelEndpointSingleMasterChannelEndpointConfigurationTypeDef",
    {"Protocols": List[Literal["WSS", "HTTPS"]], "Role": Literal["MASTER", "VIEWER"]},
    total=False,
)

ClientListSignalingChannelsChannelNameConditionTypeDef = TypedDict(
    "ClientListSignalingChannelsChannelNameConditionTypeDef",
    {"ComparisonOperator": str, "ComparisonValue": str},
    total=False,
)

ClientListSignalingChannelsResponseChannelInfoListSingleMasterConfigurationTypeDef = TypedDict(
    "ClientListSignalingChannelsResponseChannelInfoListSingleMasterConfigurationTypeDef",
    {"MessageTtlSeconds": int},
    total=False,
)

ClientListSignalingChannelsResponseChannelInfoListTypeDef = TypedDict(
    "ClientListSignalingChannelsResponseChannelInfoListTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": str,
        "ChannelStatus": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "SingleMasterConfiguration": ClientListSignalingChannelsResponseChannelInfoListSingleMasterConfigurationTypeDef,
        "Version": str,
    },
    total=False,
)

ClientListSignalingChannelsResponseTypeDef = TypedDict(
    "ClientListSignalingChannelsResponseTypeDef",
    {
        "ChannelInfoList": List[ClientListSignalingChannelsResponseChannelInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListStreamsResponseStreamInfoListTypeDef = TypedDict(
    "ClientListStreamsResponseStreamInfoListTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

ClientListStreamsResponseTypeDef = TypedDict(
    "ClientListStreamsResponseTypeDef",
    {"StreamInfoList": List[ClientListStreamsResponseStreamInfoListTypeDef], "NextToken": str},
    total=False,
)

ClientListStreamsStreamNameConditionTypeDef = TypedDict(
    "ClientListStreamsStreamNameConditionTypeDef",
    {"ComparisonOperator": str, "ComparisonValue": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"NextToken": str, "Tags": Dict[str, str]},
    total=False,
)

ClientListTagsForStreamResponseTypeDef = TypedDict(
    "ClientListTagsForStreamResponseTypeDef",
    {"NextToken": str, "Tags": Dict[str, str]},
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


ClientUpdateSignalingChannelSingleMasterConfigurationTypeDef = TypedDict(
    "ClientUpdateSignalingChannelSingleMasterConfigurationTypeDef",
    {"MessageTtlSeconds": int},
    total=False,
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef", {"MessageTtlSeconds": int}, total=False
)

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": Literal["SINGLE_MASTER"],
        "ChannelStatus": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "SingleMasterConfiguration": SingleMasterConfigurationTypeDef,
        "Version": str,
    },
    total=False,
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {"ChannelInfoList": List[ChannelInfoTypeDef], "NextToken": str},
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {"StreamInfoList": List[StreamInfoTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {"ComparisonOperator": Literal["BEGINS_WITH"], "ComparisonValue": str},
    total=False,
)
