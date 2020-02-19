"""
Main interface for globalaccelerator service type definitions.

Usage::

    from mypy_boto3.globalaccelerator.type_defs import ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef

    data: ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientCreateAcceleratorResponseAcceleratorTypeDef",
    "ClientCreateAcceleratorResponseTypeDef",
    "ClientCreateEndpointGroupEndpointConfigurationsTypeDef",
    "ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientCreateEndpointGroupResponseEndpointGroupTypeDef",
    "ClientCreateEndpointGroupResponseTypeDef",
    "ClientCreateListenerPortRangesTypeDef",
    "ClientCreateListenerResponseListenerPortRangesTypeDef",
    "ClientCreateListenerResponseListenerTypeDef",
    "ClientCreateListenerResponseTypeDef",
    "ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    "ClientDescribeAcceleratorAttributesResponseTypeDef",
    "ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientDescribeAcceleratorResponseAcceleratorTypeDef",
    "ClientDescribeAcceleratorResponseTypeDef",
    "ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientDescribeEndpointGroupResponseEndpointGroupTypeDef",
    "ClientDescribeEndpointGroupResponseTypeDef",
    "ClientDescribeListenerResponseListenerPortRangesTypeDef",
    "ClientDescribeListenerResponseListenerTypeDef",
    "ClientDescribeListenerResponseTypeDef",
    "ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef",
    "ClientListAcceleratorsResponseAcceleratorsTypeDef",
    "ClientListAcceleratorsResponseTypeDef",
    "ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef",
    "ClientListEndpointGroupsResponseEndpointGroupsTypeDef",
    "ClientListEndpointGroupsResponseTypeDef",
    "ClientListListenersResponseListenersPortRangesTypeDef",
    "ClientListListenersResponseListenersTypeDef",
    "ClientListListenersResponseTypeDef",
    "ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    "ClientUpdateAcceleratorAttributesResponseTypeDef",
    "ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientUpdateAcceleratorResponseAcceleratorTypeDef",
    "ClientUpdateAcceleratorResponseTypeDef",
    "ClientUpdateEndpointGroupEndpointConfigurationsTypeDef",
    "ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientUpdateEndpointGroupResponseEndpointGroupTypeDef",
    "ClientUpdateEndpointGroupResponseTypeDef",
    "ClientUpdateListenerPortRangesTypeDef",
    "ClientUpdateListenerResponseListenerPortRangesTypeDef",
    "ClientUpdateListenerResponseListenerTypeDef",
    "ClientUpdateListenerResponseTypeDef",
    "IpSetTypeDef",
    "AcceleratorTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "PortRangeTypeDef",
    "ListenerTypeDef",
    "ListListenersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)

ClientCreateAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "ClientCreateAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientCreateAcceleratorResponseTypeDef = TypedDict(
    "ClientCreateAcceleratorResponseTypeDef",
    {"Accelerator": ClientCreateAcceleratorResponseAcceleratorTypeDef},
    total=False,
)

ClientCreateEndpointGroupEndpointConfigurationsTypeDef = TypedDict(
    "ClientCreateEndpointGroupEndpointConfigurationsTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)

ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

ClientCreateEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "ClientCreateEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)

ClientCreateEndpointGroupResponseTypeDef = TypedDict(
    "ClientCreateEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientCreateEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)

ClientCreateListenerPortRangesTypeDef = TypedDict(
    "ClientCreateListenerPortRangesTypeDef", {"FromPort": int, "ToPort": int}, total=False
)

ClientCreateListenerResponseListenerPortRangesTypeDef = TypedDict(
    "ClientCreateListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)

ClientCreateListenerResponseListenerTypeDef = TypedDict(
    "ClientCreateListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientCreateListenerResponseListenerPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)

ClientCreateListenerResponseTypeDef = TypedDict(
    "ClientCreateListenerResponseTypeDef",
    {"Listener": ClientCreateListenerResponseListenerTypeDef},
    total=False,
)

ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef = TypedDict(
    "ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)

ClientDescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef
    },
    total=False,
)

ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)

ClientDescribeAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "ClientDescribeAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientDescribeAcceleratorResponseTypeDef = TypedDict(
    "ClientDescribeAcceleratorResponseTypeDef",
    {"Accelerator": ClientDescribeAcceleratorResponseAcceleratorTypeDef},
    total=False,
)

ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

ClientDescribeEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "ClientDescribeEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)

ClientDescribeEndpointGroupResponseTypeDef = TypedDict(
    "ClientDescribeEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientDescribeEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)

ClientDescribeListenerResponseListenerPortRangesTypeDef = TypedDict(
    "ClientDescribeListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)

ClientDescribeListenerResponseListenerTypeDef = TypedDict(
    "ClientDescribeListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientDescribeListenerResponseListenerPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)

ClientDescribeListenerResponseTypeDef = TypedDict(
    "ClientDescribeListenerResponseTypeDef",
    {"Listener": ClientDescribeListenerResponseListenerTypeDef},
    total=False,
)

ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef = TypedDict(
    "ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)

ClientListAcceleratorsResponseAcceleratorsTypeDef = TypedDict(
    "ClientListAcceleratorsResponseAcceleratorsTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientListAcceleratorsResponseTypeDef = TypedDict(
    "ClientListAcceleratorsResponseTypeDef",
    {"Accelerators": List[ClientListAcceleratorsResponseAcceleratorsTypeDef], "NextToken": str},
    total=False,
)

ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef = TypedDict(
    "ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

ClientListEndpointGroupsResponseEndpointGroupsTypeDef = TypedDict(
    "ClientListEndpointGroupsResponseEndpointGroupsTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)

ClientListEndpointGroupsResponseTypeDef = TypedDict(
    "ClientListEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List[ClientListEndpointGroupsResponseEndpointGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListListenersResponseListenersPortRangesTypeDef = TypedDict(
    "ClientListListenersResponseListenersPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)

ClientListListenersResponseListenersTypeDef = TypedDict(
    "ClientListListenersResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientListListenersResponseListenersPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)

ClientListListenersResponseTypeDef = TypedDict(
    "ClientListListenersResponseTypeDef",
    {"Listeners": List[ClientListListenersResponseListenersTypeDef], "NextToken": str},
    total=False,
)

ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef = TypedDict(
    "ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)

ClientUpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "ClientUpdateAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef
    },
    total=False,
)

ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)

ClientUpdateAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "ClientUpdateAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientUpdateAcceleratorResponseTypeDef = TypedDict(
    "ClientUpdateAcceleratorResponseTypeDef",
    {"Accelerator": ClientUpdateAcceleratorResponseAcceleratorTypeDef},
    total=False,
)

ClientUpdateEndpointGroupEndpointConfigurationsTypeDef = TypedDict(
    "ClientUpdateEndpointGroupEndpointConfigurationsTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)

ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

ClientUpdateEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "ClientUpdateEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)

ClientUpdateEndpointGroupResponseTypeDef = TypedDict(
    "ClientUpdateEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientUpdateEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)

ClientUpdateListenerPortRangesTypeDef = TypedDict(
    "ClientUpdateListenerPortRangesTypeDef", {"FromPort": int, "ToPort": int}, total=False
)

ClientUpdateListenerResponseListenerPortRangesTypeDef = TypedDict(
    "ClientUpdateListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)

ClientUpdateListenerResponseListenerTypeDef = TypedDict(
    "ClientUpdateListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientUpdateListenerResponseListenerPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)

ClientUpdateListenerResponseTypeDef = TypedDict(
    "ClientUpdateListenerResponseTypeDef",
    {"Listener": ClientUpdateListenerResponseListenerTypeDef},
    total=False,
)

IpSetTypeDef = TypedDict("IpSetTypeDef", {"IpFamily": str, "IpAddresses": List[str]}, total=False)

AcceleratorTypeDef = TypedDict(
    "AcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
        "IpSets": List[IpSetTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ListAcceleratorsResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseTypeDef",
    {"Accelerators": List[AcceleratorTypeDef], "NextToken": str},
    total=False,
)

EndpointDescriptionTypeDef = TypedDict(
    "EndpointDescriptionTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

EndpointGroupTypeDef = TypedDict(
    "EndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[EndpointDescriptionTypeDef],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)

ListEndpointGroupsResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseTypeDef",
    {"EndpointGroups": List[EndpointGroupTypeDef], "NextToken": str},
    total=False,
)

PortRangeTypeDef = TypedDict("PortRangeTypeDef", {"FromPort": int, "ToPort": int}, total=False)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[PortRangeTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {"Listeners": List[ListenerTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
