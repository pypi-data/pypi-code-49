"""
Main interface for mediaconnect service type definitions.

Usage::

    from mypy_boto3.mediaconnect.type_defs import ClientAddFlowOutputsOutputsEncryptionTypeDef

    data: ClientAddFlowOutputsOutputsEncryptionTypeDef = {...}
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
    "ClientAddFlowOutputsOutputsEncryptionTypeDef",
    "ClientAddFlowOutputsOutputsTypeDef",
    "ClientAddFlowOutputsResponseOutputsEncryptionTypeDef",
    "ClientAddFlowOutputsResponseOutputsTransportTypeDef",
    "ClientAddFlowOutputsResponseOutputsTypeDef",
    "ClientAddFlowOutputsResponseTypeDef",
    "ClientCreateFlowEntitlementsEncryptionTypeDef",
    "ClientCreateFlowEntitlementsTypeDef",
    "ClientCreateFlowOutputsEncryptionTypeDef",
    "ClientCreateFlowOutputsTypeDef",
    "ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef",
    "ClientCreateFlowResponseFlowEntitlementsTypeDef",
    "ClientCreateFlowResponseFlowOutputsEncryptionTypeDef",
    "ClientCreateFlowResponseFlowOutputsTransportTypeDef",
    "ClientCreateFlowResponseFlowOutputsTypeDef",
    "ClientCreateFlowResponseFlowSourceDecryptionTypeDef",
    "ClientCreateFlowResponseFlowSourceTransportTypeDef",
    "ClientCreateFlowResponseFlowSourceTypeDef",
    "ClientCreateFlowResponseFlowTypeDef",
    "ClientCreateFlowResponseTypeDef",
    "ClientCreateFlowSourceDecryptionTypeDef",
    "ClientCreateFlowSourceTypeDef",
    "ClientDeleteFlowResponseTypeDef",
    "ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef",
    "ClientDescribeFlowResponseFlowEntitlementsTypeDef",
    "ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef",
    "ClientDescribeFlowResponseFlowOutputsTransportTypeDef",
    "ClientDescribeFlowResponseFlowOutputsTypeDef",
    "ClientDescribeFlowResponseFlowSourceDecryptionTypeDef",
    "ClientDescribeFlowResponseFlowSourceTransportTypeDef",
    "ClientDescribeFlowResponseFlowSourceTypeDef",
    "ClientDescribeFlowResponseFlowTypeDef",
    "ClientDescribeFlowResponseMessagesTypeDef",
    "ClientDescribeFlowResponseTypeDef",
    "ClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef",
    "ClientGrantFlowEntitlementsEntitlementsTypeDef",
    "ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef",
    "ClientGrantFlowEntitlementsResponseEntitlementsTypeDef",
    "ClientGrantFlowEntitlementsResponseTypeDef",
    "ClientListEntitlementsResponseEntitlementsTypeDef",
    "ClientListEntitlementsResponseTypeDef",
    "ClientListFlowsResponseFlowsTypeDef",
    "ClientListFlowsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRemoveFlowOutputResponseTypeDef",
    "ClientRevokeFlowEntitlementResponseTypeDef",
    "ClientStartFlowResponseTypeDef",
    "ClientStopFlowResponseTypeDef",
    "ClientUpdateFlowEntitlementEncryptionTypeDef",
    "ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef",
    "ClientUpdateFlowEntitlementResponseEntitlementTypeDef",
    "ClientUpdateFlowEntitlementResponseTypeDef",
    "ClientUpdateFlowOutputEncryptionTypeDef",
    "ClientUpdateFlowOutputResponseOutputEncryptionTypeDef",
    "ClientUpdateFlowOutputResponseOutputTransportTypeDef",
    "ClientUpdateFlowOutputResponseOutputTypeDef",
    "ClientUpdateFlowOutputResponseTypeDef",
    "ClientUpdateFlowSourceDecryptionTypeDef",
    "ClientUpdateFlowSourceResponseSourceDecryptionTypeDef",
    "ClientUpdateFlowSourceResponseSourceTransportTypeDef",
    "ClientUpdateFlowSourceResponseSourceTypeDef",
    "ClientUpdateFlowSourceResponseTypeDef",
    "ListedEntitlementTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListedFlowTypeDef",
    "ListFlowsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAddFlowOutputsOutputsEncryptionTypeDef = TypedDict(
    "ClientAddFlowOutputsOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientAddFlowOutputsOutputsTypeDef = TypedDict(
    "ClientAddFlowOutputsOutputsTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": ClientAddFlowOutputsOutputsEncryptionTypeDef,
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientAddFlowOutputsResponseOutputsEncryptionTypeDef = TypedDict(
    "ClientAddFlowOutputsResponseOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientAddFlowOutputsResponseOutputsTransportTypeDef = TypedDict(
    "ClientAddFlowOutputsResponseOutputsTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientAddFlowOutputsResponseOutputsTypeDef = TypedDict(
    "ClientAddFlowOutputsResponseOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientAddFlowOutputsResponseOutputsEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientAddFlowOutputsResponseOutputsTransportTypeDef,
    },
    total=False,
)

ClientAddFlowOutputsResponseTypeDef = TypedDict(
    "ClientAddFlowOutputsResponseTypeDef",
    {"FlowArn": str, "Outputs": List[ClientAddFlowOutputsResponseOutputsTypeDef]},
    total=False,
)

_RequiredClientCreateFlowEntitlementsEncryptionTypeDef = TypedDict(
    "_RequiredClientCreateFlowEntitlementsEncryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalClientCreateFlowEntitlementsEncryptionTypeDef = TypedDict(
    "_OptionalClientCreateFlowEntitlementsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowEntitlementsEncryptionTypeDef(
    _RequiredClientCreateFlowEntitlementsEncryptionTypeDef,
    _OptionalClientCreateFlowEntitlementsEncryptionTypeDef,
):
    pass


ClientCreateFlowEntitlementsTypeDef = TypedDict(
    "ClientCreateFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientCreateFlowEntitlementsEncryptionTypeDef,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)

ClientCreateFlowOutputsEncryptionTypeDef = TypedDict(
    "ClientCreateFlowOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientCreateFlowOutputsTypeDef = TypedDict(
    "ClientCreateFlowOutputsTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": ClientCreateFlowOutputsEncryptionTypeDef,
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowEntitlementsTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)

ClientCreateFlowResponseFlowOutputsEncryptionTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowOutputsTransportTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowOutputsTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowOutputsTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientCreateFlowResponseFlowOutputsEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientCreateFlowResponseFlowOutputsTransportTypeDef,
    },
    total=False,
)

ClientCreateFlowResponseFlowSourceDecryptionTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowSourceTransportTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowSourceTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowSourceTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": ClientCreateFlowResponseFlowSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": ClientCreateFlowResponseFlowSourceTransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)

ClientCreateFlowResponseFlowTypeDef = TypedDict(
    "ClientCreateFlowResponseFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "EgressIp": str,
        "Entitlements": List[ClientCreateFlowResponseFlowEntitlementsTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[ClientCreateFlowResponseFlowOutputsTypeDef],
        "Source": ClientCreateFlowResponseFlowSourceTypeDef,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

ClientCreateFlowResponseTypeDef = TypedDict(
    "ClientCreateFlowResponseTypeDef", {"Flow": ClientCreateFlowResponseFlowTypeDef}, total=False
)

_RequiredClientCreateFlowSourceDecryptionTypeDef = TypedDict(
    "_RequiredClientCreateFlowSourceDecryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalClientCreateFlowSourceDecryptionTypeDef = TypedDict(
    "_OptionalClientCreateFlowSourceDecryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowSourceDecryptionTypeDef(
    _RequiredClientCreateFlowSourceDecryptionTypeDef,
    _OptionalClientCreateFlowSourceDecryptionTypeDef,
):
    pass


ClientCreateFlowSourceTypeDef = TypedDict(
    "ClientCreateFlowSourceTypeDef",
    {
        "Decryption": ClientCreateFlowSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "Name": str,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "StreamId": str,
        "WhitelistCidr": str,
    },
    total=False,
)

ClientDeleteFlowResponseTypeDef = TypedDict(
    "ClientDeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientDescribeFlowResponseFlowEntitlementsTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)

ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientDescribeFlowResponseFlowOutputsTransportTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowOutputsTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientDescribeFlowResponseFlowOutputsTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientDescribeFlowResponseFlowOutputsTransportTypeDef,
    },
    total=False,
)

ClientDescribeFlowResponseFlowSourceDecryptionTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientDescribeFlowResponseFlowSourceTransportTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowSourceTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientDescribeFlowResponseFlowSourceTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": ClientDescribeFlowResponseFlowSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": ClientDescribeFlowResponseFlowSourceTransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)

ClientDescribeFlowResponseFlowTypeDef = TypedDict(
    "ClientDescribeFlowResponseFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "EgressIp": str,
        "Entitlements": List[ClientDescribeFlowResponseFlowEntitlementsTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[ClientDescribeFlowResponseFlowOutputsTypeDef],
        "Source": ClientDescribeFlowResponseFlowSourceTypeDef,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

ClientDescribeFlowResponseMessagesTypeDef = TypedDict(
    "ClientDescribeFlowResponseMessagesTypeDef", {"Errors": List[str]}, total=False
)

ClientDescribeFlowResponseTypeDef = TypedDict(
    "ClientDescribeFlowResponseTypeDef",
    {
        "Flow": ClientDescribeFlowResponseFlowTypeDef,
        "Messages": ClientDescribeFlowResponseMessagesTypeDef,
    },
    total=False,
)

_RequiredClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef = TypedDict(
    "_RequiredClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef = TypedDict(
    "_OptionalClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef(
    _RequiredClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef,
    _OptionalClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef,
):
    pass


ClientGrantFlowEntitlementsEntitlementsTypeDef = TypedDict(
    "ClientGrantFlowEntitlementsEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)

ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef = TypedDict(
    "ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientGrantFlowEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "ClientGrantFlowEntitlementsResponseEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)

ClientGrantFlowEntitlementsResponseTypeDef = TypedDict(
    "ClientGrantFlowEntitlementsResponseTypeDef",
    {"Entitlements": List[ClientGrantFlowEntitlementsResponseEntitlementsTypeDef], "FlowArn": str},
    total=False,
)

ClientListEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "ClientListEntitlementsResponseEntitlementsTypeDef",
    {"DataTransferSubscriberFeePercent": int, "EntitlementArn": str, "EntitlementName": str},
    total=False,
)

ClientListEntitlementsResponseTypeDef = TypedDict(
    "ClientListEntitlementsResponseTypeDef",
    {"Entitlements": List[ClientListEntitlementsResponseEntitlementsTypeDef], "NextToken": str},
    total=False,
)

ClientListFlowsResponseFlowsTypeDef = TypedDict(
    "ClientListFlowsResponseFlowsTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": Literal["OWNED", "ENTITLED"],
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

ClientListFlowsResponseTypeDef = TypedDict(
    "ClientListFlowsResponseTypeDef",
    {"Flows": List[ClientListFlowsResponseFlowsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientRemoveFlowOutputResponseTypeDef = TypedDict(
    "ClientRemoveFlowOutputResponseTypeDef", {"FlowArn": str, "OutputArn": str}, total=False
)

ClientRevokeFlowEntitlementResponseTypeDef = TypedDict(
    "ClientRevokeFlowEntitlementResponseTypeDef",
    {"EntitlementArn": str, "FlowArn": str},
    total=False,
)

ClientStartFlowResponseTypeDef = TypedDict(
    "ClientStartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

ClientStopFlowResponseTypeDef = TypedDict(
    "ClientStopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

ClientUpdateFlowEntitlementEncryptionTypeDef = TypedDict(
    "ClientUpdateFlowEntitlementEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef = TypedDict(
    "ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientUpdateFlowEntitlementResponseEntitlementTypeDef = TypedDict(
    "ClientUpdateFlowEntitlementResponseEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)

ClientUpdateFlowEntitlementResponseTypeDef = TypedDict(
    "ClientUpdateFlowEntitlementResponseTypeDef",
    {"Entitlement": ClientUpdateFlowEntitlementResponseEntitlementTypeDef, "FlowArn": str},
    total=False,
)

ClientUpdateFlowOutputEncryptionTypeDef = TypedDict(
    "ClientUpdateFlowOutputEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientUpdateFlowOutputResponseOutputEncryptionTypeDef = TypedDict(
    "ClientUpdateFlowOutputResponseOutputEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientUpdateFlowOutputResponseOutputTransportTypeDef = TypedDict(
    "ClientUpdateFlowOutputResponseOutputTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientUpdateFlowOutputResponseOutputTypeDef = TypedDict(
    "ClientUpdateFlowOutputResponseOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientUpdateFlowOutputResponseOutputEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientUpdateFlowOutputResponseOutputTransportTypeDef,
    },
    total=False,
)

ClientUpdateFlowOutputResponseTypeDef = TypedDict(
    "ClientUpdateFlowOutputResponseTypeDef",
    {"FlowArn": str, "Output": ClientUpdateFlowOutputResponseOutputTypeDef},
    total=False,
)

ClientUpdateFlowSourceDecryptionTypeDef = TypedDict(
    "ClientUpdateFlowSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientUpdateFlowSourceResponseSourceDecryptionTypeDef = TypedDict(
    "ClientUpdateFlowSourceResponseSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

ClientUpdateFlowSourceResponseSourceTransportTypeDef = TypedDict(
    "ClientUpdateFlowSourceResponseSourceTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

ClientUpdateFlowSourceResponseSourceTypeDef = TypedDict(
    "ClientUpdateFlowSourceResponseSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": ClientUpdateFlowSourceResponseSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": ClientUpdateFlowSourceResponseSourceTransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)

ClientUpdateFlowSourceResponseTypeDef = TypedDict(
    "ClientUpdateFlowSourceResponseTypeDef",
    {"FlowArn": str, "Source": ClientUpdateFlowSourceResponseSourceTypeDef},
    total=False,
)

_RequiredListedEntitlementTypeDef = TypedDict(
    "_RequiredListedEntitlementTypeDef", {"EntitlementArn": str, "EntitlementName": str}
)
_OptionalListedEntitlementTypeDef = TypedDict(
    "_OptionalListedEntitlementTypeDef", {"DataTransferSubscriberFeePercent": int}, total=False
)


class ListedEntitlementTypeDef(
    _RequiredListedEntitlementTypeDef, _OptionalListedEntitlementTypeDef
):
    pass


ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {"Entitlements": List[ListedEntitlementTypeDef], "NextToken": str},
    total=False,
)

ListedFlowTypeDef = TypedDict(
    "ListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": Literal["OWNED", "ENTITLED"],
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef", {"Flows": List[ListedFlowTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
