"""
Main interface for dax service type definitions.

Usage::

    from mypy_boto3.dax.type_defs import ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef

    data: ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientCreateClusterResponseClusterNodesEndpointTypeDef",
    "ClientCreateClusterResponseClusterNodesTypeDef",
    "ClientCreateClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientCreateClusterResponseClusterParameterGroupTypeDef",
    "ClientCreateClusterResponseClusterSSEDescriptionTypeDef",
    "ClientCreateClusterResponseClusterSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSSESpecificationTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateParameterGroupResponseParameterGroupTypeDef",
    "ClientCreateParameterGroupResponseTypeDef",
    "ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    "ClientCreateSubnetGroupResponseSubnetGroupTypeDef",
    "ClientCreateSubnetGroupResponseTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNodesTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterTypeDef",
    "ClientDecreaseReplicationFactorResponseTypeDef",
    "ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientDeleteClusterResponseClusterNodesEndpointTypeDef",
    "ClientDeleteClusterResponseClusterNodesTypeDef",
    "ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientDeleteClusterResponseClusterParameterGroupTypeDef",
    "ClientDeleteClusterResponseClusterSSEDescriptionTypeDef",
    "ClientDeleteClusterResponseClusterSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteParameterGroupResponseTypeDef",
    "ClientDeleteSubnetGroupResponseTypeDef",
    "ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef",
    "ClientDescribeClustersResponseClustersNodesEndpointTypeDef",
    "ClientDescribeClustersResponseClustersNodesTypeDef",
    "ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef",
    "ClientDescribeClustersResponseClustersParameterGroupTypeDef",
    "ClientDescribeClustersResponseClustersSSEDescriptionTypeDef",
    "ClientDescribeClustersResponseClustersSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    "ClientDescribeDefaultParametersResponseParametersTypeDef",
    "ClientDescribeDefaultParametersResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeParameterGroupsResponseParameterGroupsTypeDef",
    "ClientDescribeParameterGroupsResponseTypeDef",
    "ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    "ClientDescribeParametersResponseParametersTypeDef",
    "ClientDescribeParametersResponseTypeDef",
    "ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef",
    "ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef",
    "ClientDescribeSubnetGroupsResponseTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNodesTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterTypeDef",
    "ClientIncreaseReplicationFactorResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientRebootNodeResponseClusterNodesEndpointTypeDef",
    "ClientRebootNodeResponseClusterNodesTypeDef",
    "ClientRebootNodeResponseClusterNotificationConfigurationTypeDef",
    "ClientRebootNodeResponseClusterParameterGroupTypeDef",
    "ClientRebootNodeResponseClusterSSEDescriptionTypeDef",
    "ClientRebootNodeResponseClusterSecurityGroupsTypeDef",
    "ClientRebootNodeResponseClusterTypeDef",
    "ClientRebootNodeResponseTypeDef",
    "ClientTagResourceResponseTagsTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUntagResourceResponseTagsTypeDef",
    "ClientUntagResourceResponseTypeDef",
    "ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientUpdateClusterResponseClusterNodesEndpointTypeDef",
    "ClientUpdateClusterResponseClusterNodesTypeDef",
    "ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientUpdateClusterResponseClusterParameterGroupTypeDef",
    "ClientUpdateClusterResponseClusterSSEDescriptionTypeDef",
    "ClientUpdateClusterResponseClusterSecurityGroupsTypeDef",
    "ClientUpdateClusterResponseClusterTypeDef",
    "ClientUpdateClusterResponseTypeDef",
    "ClientUpdateParameterGroupParameterNameValuesTypeDef",
    "ClientUpdateParameterGroupResponseParameterGroupTypeDef",
    "ClientUpdateParameterGroupResponseTypeDef",
    "ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    "ClientUpdateSubnetGroupResponseSubnetGroupTypeDef",
    "ClientUpdateSubnetGroupResponseTypeDef",
    "EndpointTypeDef",
    "NodeTypeDef",
    "NotificationConfigurationTypeDef",
    "ParameterGroupStatusTypeDef",
    "SSEDescriptionTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ClusterTypeDef",
    "DescribeClustersResponseTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "ParameterTypeDef",
    "DescribeDefaultParametersResponseTypeDef",
    "EventTypeDef",
    "DescribeEventsResponseTypeDef",
    "ParameterGroupTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersResponseTypeDef",
    "SubnetTypeDef",
    "SubnetGroupTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "TagTypeDef",
    "ListTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateClusterResponseClusterNodesTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientCreateClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientCreateClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientCreateClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientCreateClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientCreateClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientCreateClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientCreateClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientCreateClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientCreateClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)

ClientCreateClusterSSESpecificationTypeDef = TypedDict(
    "ClientCreateClusterSSESpecificationTypeDef", {"Enabled": bool}
)

ClientCreateClusterTagsTypeDef = TypedDict(
    "ClientCreateClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateParameterGroupResponseParameterGroupTypeDef = TypedDict(
    "ClientCreateParameterGroupResponseParameterGroupTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)

ClientCreateParameterGroupResponseTypeDef = TypedDict(
    "ClientCreateParameterGroupResponseTypeDef",
    {"ParameterGroup": ClientCreateParameterGroupResponseParameterGroupTypeDef},
    total=False,
)

ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)

ClientCreateSubnetGroupResponseSubnetGroupTypeDef = TypedDict(
    "ClientCreateSubnetGroupResponseSubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef],
    },
    total=False,
)

ClientCreateSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateSubnetGroupResponseTypeDef",
    {"SubnetGroup": ClientCreateSubnetGroupResponseSubnetGroupTypeDef},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterNodesTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientDecreaseReplicationFactorResponseClusterTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDecreaseReplicationFactorResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)

ClientDecreaseReplicationFactorResponseTypeDef = TypedDict(
    "ClientDecreaseReplicationFactorResponseTypeDef",
    {"Cluster": ClientDecreaseReplicationFactorResponseClusterTypeDef},
    total=False,
)

ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteClusterResponseClusterNodesTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDeleteClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDeleteClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientDeleteClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientDeleteClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDeleteClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDeleteClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDeleteClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientDeleteClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)

ClientDeleteParameterGroupResponseTypeDef = TypedDict(
    "ClientDeleteParameterGroupResponseTypeDef", {"DeletionMessage": str}, total=False
)

ClientDeleteSubnetGroupResponseTypeDef = TypedDict(
    "ClientDeleteSubnetGroupResponseTypeDef", {"DeletionMessage": str}, total=False
)

ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeClustersResponseClustersNodesEndpointTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeClustersResponseClustersNodesTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDescribeClustersResponseClustersNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDescribeClustersResponseClustersParameterGroupTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientDescribeClustersResponseClustersSSEDescriptionTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientDescribeClustersResponseClustersSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDescribeClustersResponseClustersNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDescribeClustersResponseClustersSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDescribeClustersResponseClustersParameterGroupTypeDef,
        "SSEDescription": ClientDescribeClustersResponseClustersSSEDescriptionTypeDef,
    },
    total=False,
)

ClientDescribeClustersResponseTypeDef = TypedDict(
    "ClientDescribeClustersResponseTypeDef",
    {"NextToken": str, "Clusters": List[ClientDescribeClustersResponseClustersTypeDef]},
    total=False,
)

ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)

ClientDescribeDefaultParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeDefaultParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)

ClientDescribeDefaultParametersResponseTypeDef = TypedDict(
    "ClientDescribeDefaultParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List[ClientDescribeDefaultParametersResponseParametersTypeDef],
    },
    total=False,
)

ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceName": str,
        "SourceType": Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"NextToken": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

ClientDescribeParameterGroupsResponseParameterGroupsTypeDef = TypedDict(
    "ClientDescribeParameterGroupsResponseParameterGroupsTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)

ClientDescribeParameterGroupsResponseTypeDef = TypedDict(
    "ClientDescribeParameterGroupsResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List[ClientDescribeParameterGroupsResponseParameterGroupsTypeDef],
    },
    total=False,
)

ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)

ClientDescribeParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)

ClientDescribeParametersResponseTypeDef = TypedDict(
    "ClientDescribeParametersResponseTypeDef",
    {"NextToken": str, "Parameters": List[ClientDescribeParametersResponseParametersTypeDef]},
    total=False,
)

ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)

ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)

ClientDescribeSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeSubnetGroupsResponseTypeDef",
    {"NextToken": str, "SubnetGroups": List[ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef]},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterNodesTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientIncreaseReplicationFactorResponseClusterTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientIncreaseReplicationFactorResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)

ClientIncreaseReplicationFactorResponseTypeDef = TypedDict(
    "ClientIncreaseReplicationFactorResponseTypeDef",
    {"Cluster": ClientIncreaseReplicationFactorResponseClusterTypeDef},
    total=False,
)

ClientListTagsResponseTagsTypeDef = TypedDict(
    "ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRebootNodeResponseClusterNodesEndpointTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRebootNodeResponseClusterNodesTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientRebootNodeResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientRebootNodeResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientRebootNodeResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientRebootNodeResponseClusterSSEDescriptionTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientRebootNodeResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientRebootNodeResponseClusterTypeDef = TypedDict(
    "ClientRebootNodeResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientRebootNodeResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientRebootNodeResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientRebootNodeResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientRebootNodeResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientRebootNodeResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)

ClientRebootNodeResponseTypeDef = TypedDict(
    "ClientRebootNodeResponseTypeDef",
    {"Cluster": ClientRebootNodeResponseClusterTypeDef},
    total=False,
)

ClientTagResourceResponseTagsTypeDef = TypedDict(
    "ClientTagResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientTagResourceResponseTypeDef = TypedDict(
    "ClientTagResourceResponseTypeDef",
    {"Tags": List[ClientTagResourceResponseTagsTypeDef]},
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUntagResourceResponseTagsTypeDef = TypedDict(
    "ClientUntagResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUntagResourceResponseTypeDef = TypedDict(
    "ClientUntagResourceResponseTypeDef",
    {"Tags": List[ClientUntagResourceResponseTagsTypeDef]},
    total=False,
)

ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientUpdateClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientUpdateClusterResponseClusterNodesTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientUpdateClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientUpdateClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

ClientUpdateClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

ClientUpdateClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)

ClientUpdateClusterResponseClusterTypeDef = TypedDict(
    "ClientUpdateClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientUpdateClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientUpdateClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientUpdateClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientUpdateClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)

ClientUpdateClusterResponseTypeDef = TypedDict(
    "ClientUpdateClusterResponseTypeDef",
    {"Cluster": ClientUpdateClusterResponseClusterTypeDef},
    total=False,
)

ClientUpdateParameterGroupParameterNameValuesTypeDef = TypedDict(
    "ClientUpdateParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientUpdateParameterGroupResponseParameterGroupTypeDef = TypedDict(
    "ClientUpdateParameterGroupResponseParameterGroupTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)

ClientUpdateParameterGroupResponseTypeDef = TypedDict(
    "ClientUpdateParameterGroupResponseTypeDef",
    {"ParameterGroup": ClientUpdateParameterGroupResponseParameterGroupTypeDef},
    total=False,
)

ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)

ClientUpdateSubnetGroupResponseSubnetGroupTypeDef = TypedDict(
    "ClientUpdateSubnetGroupResponseSubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef],
    },
    total=False,
)

ClientUpdateSubnetGroupResponseTypeDef = TypedDict(
    "ClientUpdateSubnetGroupResponseTypeDef",
    {"SubnetGroup": ClientUpdateSubnetGroupResponseSubnetGroupTypeDef},
    total=False,
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "Port": int}, total=False)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NodeId": str,
        "Endpoint": EndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef", {"TopicArn": str, "TopicStatus": str}, total=False
)

ParameterGroupStatusTypeDef = TypedDict(
    "ParameterGroupStatusTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef", {"SecurityGroupIdentifier": str, "Status": str}, total=False
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": EndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[NodeTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[SecurityGroupMembershipTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ParameterGroupStatusTypeDef,
        "SSEDescription": SSEDescriptionTypeDef,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {"NextToken": str, "Clusters": List[ClusterTypeDef]},
    total=False,
)

NodeTypeSpecificValueTypeDef = TypedDict(
    "NodeTypeSpecificValueTypeDef", {"NodeType": str, "Value": str}, total=False
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[NodeTypeSpecificValueTypeDef],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)

DescribeDefaultParametersResponseTypeDef = TypedDict(
    "DescribeDefaultParametersResponseTypeDef",
    {"NextToken": str, "Parameters": List[ParameterTypeDef]},
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceName": str,
        "SourceType": Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef", {"NextToken": str, "Events": List[EventTypeDef]}, total=False
)

ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef", {"ParameterGroupName": str, "Description": str}, total=False
)

DescribeParameterGroupsResponseTypeDef = TypedDict(
    "DescribeParameterGroupsResponseTypeDef",
    {"NextToken": str, "ParameterGroups": List[ParameterGroupTypeDef]},
    total=False,
)

DescribeParametersResponseTypeDef = TypedDict(
    "DescribeParametersResponseTypeDef",
    {"NextToken": str, "Parameters": List[ParameterTypeDef]},
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef", {"SubnetIdentifier": str, "SubnetAvailabilityZone": str}, total=False
)

SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {"SubnetGroupName": str, "Description": str, "VpcId": str, "Subnets": List[SubnetTypeDef]},
    total=False,
)

DescribeSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeSubnetGroupsResponseTypeDef",
    {"NextToken": str, "SubnetGroups": List[SubnetGroupTypeDef]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
