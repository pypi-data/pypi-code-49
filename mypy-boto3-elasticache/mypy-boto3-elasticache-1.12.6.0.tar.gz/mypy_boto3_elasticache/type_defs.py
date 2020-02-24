"""
Main interface for elasticache service type definitions.

Usage::

    from mypy_boto3.elasticache.type_defs import EndpointTypeDef

    data: EndpointTypeDef = {...}
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
    "EndpointTypeDef",
    "CacheNodeTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "NotificationConfigurationTypeDef",
    "PendingModifiedValuesTypeDef",
    "SecurityGroupMembershipTypeDef",
    "CacheClusterTypeDef",
    "CacheClusterMessageTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheEngineVersionMessageTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "ParameterTypeDef",
    "CacheParameterGroupDetailsTypeDef",
    "CacheParameterGroupTypeDef",
    "CacheParameterGroupsMessageTypeDef",
    "EC2SecurityGroupTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheSecurityGroupMessageTypeDef",
    "AvailabilityZoneTypeDef",
    "SubnetTypeDef",
    "CacheSubnetGroupTypeDef",
    "CacheSubnetGroupMessageTypeDef",
    "ClientAddTagsToResourceResponseTagListTypeDef",
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    "ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
    "ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    "ClientBatchApplyUpdateActionResponseTypeDef",
    "ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
    "ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    "ClientBatchStopUpdateActionResponseTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupTypeDef",
    "ClientCompleteMigrationResponseTypeDef",
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientCopySnapshotResponseSnapshotTypeDef",
    "ClientCopySnapshotResponseTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterTypeDef",
    "ClientCreateCacheClusterResponseTypeDef",
    "ClientCreateCacheClusterTagsTypeDef",
    "ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    "ClientCreateCacheParameterGroupResponseTypeDef",
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
    "ClientCreateCacheSecurityGroupResponseTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    "ClientCreateCacheSubnetGroupResponseTypeDef",
    "ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
    "ClientCreateReplicationGroupResponseTypeDef",
    "ClientCreateReplicationGroupTagsTypeDef",
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientCreateSnapshotResponseSnapshotTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
    "ClientDecreaseReplicaCountResponseTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterTypeDef",
    "ClientDeleteCacheClusterResponseTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
    "ClientDeleteReplicationGroupResponseTypeDef",
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientDeleteSnapshotResponseSnapshotTypeDef",
    "ClientDeleteSnapshotResponseTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersTypeDef",
    "ClientDescribeCacheClustersResponseTypeDef",
    "ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    "ClientDescribeCacheEngineVersionsResponseTypeDef",
    "ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    "ClientDescribeCacheParameterGroupsResponseTypeDef",
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
    "ClientDescribeCacheParametersResponseParametersTypeDef",
    "ClientDescribeCacheParametersResponseTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
    "ClientDescribeReplicationGroupsResponseTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef",
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef",
    "ClientDescribeReservedCacheNodesResponseTypeDef",
    "ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
    "ClientDescribeServiceUpdatesResponseTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
    "ClientDescribeUpdateActionsResponseTypeDef",
    "ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    "ClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
    "ClientIncreaseReplicaCountResponseTypeDef",
    "ClientListAllowedNodeTypeModificationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterTypeDef",
    "ClientModifyCacheClusterResponseTypeDef",
    "ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    "ClientModifyCacheParameterGroupResponseTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    "ClientModifyCacheSubnetGroupResponseTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
    "ClientModifyReplicationGroupResponseTypeDef",
    "ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterTypeDef",
    "ClientRebootCacheClusterResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTagListTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    "ClientResetCacheParameterGroupResponseTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    "ClientStartMigrationCustomerNodeEndpointListTypeDef",
    "ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientStartMigrationResponseReplicationGroupTypeDef",
    "ClientStartMigrationResponseTypeDef",
    "ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientTestFailoverResponseReplicationGroupTypeDef",
    "ClientTestFailoverResponseTypeDef",
    "EngineDefaultsTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeSnapshotTypeDef",
    "SnapshotTypeDef",
    "DescribeSnapshotsListMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "NodeGroupMemberTypeDef",
    "NodeGroupTypeDef",
    "SlotMigrationTypeDef",
    "ReshardingStatusTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "ReplicationGroupTypeDef",
    "ReplicationGroupMessageTypeDef",
    "RecurringChargeTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodeMessageTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ReservedCacheNodesOfferingMessageTypeDef",
    "ServiceUpdateTypeDef",
    "ServiceUpdatesMessageTypeDef",
    "TimeRangeFilterTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "UpdateActionTypeDef",
    "UpdateActionsMessageTypeDef",
    "WaiterConfigTypeDef",
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "Port": int}, total=False)

CacheNodeTypeDef = TypedDict(
    "CacheNodeTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": EndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)

CacheParameterGroupStatusTypeDef = TypedDict(
    "CacheParameterGroupStatusTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

CacheSecurityGroupMembershipTypeDef = TypedDict(
    "CacheSecurityGroupMembershipTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef", {"TopicArn": str, "TopicStatus": str}, total=False
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef", {"SecurityGroupId": str, "Status": str}, total=False
)

CacheClusterTypeDef = TypedDict(
    "CacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": EndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": PendingModifiedValuesTypeDef,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[CacheSecurityGroupMembershipTypeDef],
        "CacheParameterGroup": CacheParameterGroupStatusTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[CacheNodeTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[SecurityGroupMembershipTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)

CacheClusterMessageTypeDef = TypedDict(
    "CacheClusterMessageTypeDef",
    {"Marker": str, "CacheClusters": List[CacheClusterTypeDef]},
    total=False,
)

CacheEngineVersionTypeDef = TypedDict(
    "CacheEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)

CacheEngineVersionMessageTypeDef = TypedDict(
    "CacheEngineVersionMessageTypeDef",
    {"Marker": str, "CacheEngineVersions": List[CacheEngineVersionTypeDef]},
    total=False,
)

CacheNodeTypeSpecificValueTypeDef = TypedDict(
    "CacheNodeTypeSpecificValueTypeDef", {"CacheNodeType": str, "Value": str}, total=False
)

CacheNodeTypeSpecificParameterTypeDef = TypedDict(
    "CacheNodeTypeSpecificParameterTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[CacheNodeTypeSpecificValueTypeDef],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)

CacheParameterGroupDetailsTypeDef = TypedDict(
    "CacheParameterGroupDetailsTypeDef",
    {
        "Marker": str,
        "Parameters": List[ParameterTypeDef],
        "CacheNodeTypeSpecificParameters": List[CacheNodeTypeSpecificParameterTypeDef],
    },
    total=False,
)

CacheParameterGroupTypeDef = TypedDict(
    "CacheParameterGroupTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)

CacheParameterGroupsMessageTypeDef = TypedDict(
    "CacheParameterGroupsMessageTypeDef",
    {"Marker": str, "CacheParameterGroups": List[CacheParameterGroupTypeDef]},
    total=False,
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

CacheSecurityGroupTypeDef = TypedDict(
    "CacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[EC2SecurityGroupTypeDef],
    },
    total=False,
)

CacheSecurityGroupMessageTypeDef = TypedDict(
    "CacheSecurityGroupMessageTypeDef",
    {"Marker": str, "CacheSecurityGroups": List[CacheSecurityGroupTypeDef]},
    total=False,
)

AvailabilityZoneTypeDef = TypedDict("AvailabilityZoneTypeDef", {"Name": str}, total=False)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": AvailabilityZoneTypeDef},
    total=False,
)

CacheSubnetGroupTypeDef = TypedDict(
    "CacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[SubnetTypeDef],
    },
    total=False,
)

CacheSubnetGroupMessageTypeDef = TypedDict(
    "CacheSubnetGroupMessageTypeDef",
    {"Marker": str, "CacheSubnetGroups": List[CacheSubnetGroupTypeDef]},
    total=False,
)

ClientAddTagsToResourceResponseTagListTypeDef = TypedDict(
    "ClientAddTagsToResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "ClientAddTagsToResourceResponseTypeDef",
    {"TagList": List[ClientAddTagsToResourceResponseTagListTypeDef]},
    total=False,
)

ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    {
        "CacheSecurityGroup": ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
    },
    total=False,
)

ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
    },
    total=False,
)

ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchApplyUpdateActionResponseTypeDef = TypedDict(
    "ClientBatchApplyUpdateActionResponseTypeDef",
    {
        "ProcessedUpdateActions": List[
            ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef
        ],
        "UnprocessedUpdateActions": List[
            ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef
        ],
    },
    total=False,
)

ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
    },
    total=False,
)

ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchStopUpdateActionResponseTypeDef = TypedDict(
    "ClientBatchStopUpdateActionResponseTypeDef",
    {
        "ProcessedUpdateActions": List[
            ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef
        ],
        "UnprocessedUpdateActions": List[
            ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef
        ],
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientCompleteMigrationResponseReplicationGroupTypeDef = TypedDict(
    "ClientCompleteMigrationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientCompleteMigrationResponseTypeDef = TypedDict(
    "ClientCompleteMigrationResponseTypeDef",
    {"ReplicationGroup": ClientCompleteMigrationResponseReplicationGroupTypeDef},
    total=False,
)

ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

ClientCopySnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientCopySnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)

ClientCopySnapshotResponseTypeDef = TypedDict(
    "ClientCopySnapshotResponseTypeDef",
    {"Snapshot": ClientCopySnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)

ClientCreateCacheClusterResponseTypeDef = TypedDict(
    "ClientCreateCacheClusterResponseTypeDef",
    {"CacheCluster": ClientCreateCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientCreateCacheClusterTagsTypeDef = TypedDict(
    "ClientCreateCacheClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef = TypedDict(
    "ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)

ClientCreateCacheParameterGroupResponseTypeDef = TypedDict(
    "ClientCreateCacheParameterGroupResponseTypeDef",
    {"CacheParameterGroup": ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef},
    total=False,
)

ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef = TypedDict(
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientCreateCacheSecurityGroupResponseTypeDef = TypedDict(
    "ClientCreateCacheSecurityGroupResponseTypeDef",
    {"CacheSecurityGroup": ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef},
    total=False,
)

ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef],
    },
    total=False,
)

ClientCreateCacheSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)

ClientCreateReplicationGroupNodeGroupConfigurationTypeDef = TypedDict(
    "ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientCreateReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateReplicationGroupResponseTypeDef = TypedDict(
    "ClientCreateReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientCreateReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)

ClientCreateReplicationGroupTagsTypeDef = TypedDict(
    "ClientCreateReplicationGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

ClientCreateSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientCreateSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateSnapshotResponseTypeDef = TypedDict(
    "ClientCreateSnapshotResponseTypeDef",
    {"Snapshot": ClientCreateSnapshotResponseSnapshotTypeDef},
    total=False,
)

_RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef", {"NodeGroupId": str}
)
_OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    {"NewReplicaCount": int, "PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientDecreaseReplicaCountReplicaConfigurationTypeDef(
    _RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef,
    _OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef,
):
    pass


ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDecreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDecreaseReplicaCountResponseTypeDef = TypedDict(
    "ClientDecreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientDecreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)

ClientDeleteCacheClusterResponseTypeDef = TypedDict(
    "ClientDeleteCacheClusterResponseTypeDef",
    {"CacheCluster": ClientDeleteCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDeleteReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDeleteReplicationGroupResponseTypeDef = TypedDict(
    "ClientDeleteReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientDeleteReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)

ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

ClientDeleteSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)

ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseTypeDef",
    {"Snapshot": ClientDeleteSnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeCacheClustersResponseCacheClustersTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseCacheClustersTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)

ClientDescribeCacheClustersResponseTypeDef = TypedDict(
    "ClientDescribeCacheClustersResponseTypeDef",
    {"Marker": str, "CacheClusters": List[ClientDescribeCacheClustersResponseCacheClustersTypeDef]},
    total=False,
)

ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef = TypedDict(
    "ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)

ClientDescribeCacheEngineVersionsResponseTypeDef = TypedDict(
    "ClientDescribeCacheEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List[
            ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef = TypedDict(
    "ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    {"CacheParameterGroupName": str, "CacheParameterGroupFamily": str, "Description": str},
    total=False,
)

ClientDescribeCacheParameterGroupsResponseTypeDef = TypedDict(
    "ClientDescribeCacheParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List[
            ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)

ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)

ClientDescribeCacheParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)

ClientDescribeCacheParametersResponseTypeDef = TypedDict(
    "ClientDescribeCacheParametersResponseTypeDef",
    {
        "Marker": str,
        "Parameters": List[ClientDescribeCacheParametersResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheSecurityGroupsResponseTypeDef = TypedDict(
    "ClientDescribeCacheSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)

ClientDescribeCacheSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeCacheSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List[ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef],
    },
    total=False,
)

ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)

ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)

ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": Literal["immediate", "requires-reboot"],
    },
    total=False,
)

ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
        ],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeEngineDefaultParametersResponseTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    {"EngineDefaults": ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef},
    total=False,
)

ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeReplicationGroupsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List[ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef],
    },
    total=False,
)

ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedCacheNodesOfferingsResponseTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[
            ClientDescribeReservedCacheNodesResponseReservedCacheNodesRecurringChargesTypeDef
        ],
        "ReservationARN": str,
    },
    total=False,
)

ClientDescribeReservedCacheNodesResponseTypeDef = TypedDict(
    "ClientDescribeReservedCacheNodesResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List[
            ClientDescribeReservedCacheNodesResponseReservedCacheNodesTypeDef
        ],
    },
    total=False,
)

ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef = TypedDict(
    "ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": str,
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)

ClientDescribeServiceUpdatesResponseTypeDef = TypedDict(
    "ClientDescribeServiceUpdatesResponseTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List[ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef],
    },
    total=False,
)

ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseTypeDef",
    {"Marker": str, "Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef]},
    total=False,
)

ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)

ClientDescribeUpdateActionsResponseUpdateActionsTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": str,
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": Literal["yes", "no", "n/a"],
        "NodeGroupUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef
        ],
        "CacheNodeUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef
        ],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)

ClientDescribeUpdateActionsResponseTypeDef = TypedDict(
    "ClientDescribeUpdateActionsResponseTypeDef",
    {"Marker": str, "UpdateActions": List[ClientDescribeUpdateActionsResponseUpdateActionsTypeDef]},
    total=False,
)

ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef = TypedDict(
    "ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

_RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef", {"NodeGroupId": str}
)
_OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    {"NewReplicaCount": int, "PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientIncreaseReplicaCountReplicaConfigurationTypeDef(
    _RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef,
    _OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef,
):
    pass


ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientIncreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientIncreaseReplicaCountResponseTypeDef = TypedDict(
    "ClientIncreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientIncreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)

ClientListAllowedNodeTypeModificationsResponseTypeDef = TypedDict(
    "ClientListAllowedNodeTypeModificationsResponseTypeDef",
    {"ScaleUpModifications": List[str], "ScaleDownModifications": List[str]},
    total=False,
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)

ClientModifyCacheClusterResponseTypeDef = TypedDict(
    "ClientModifyCacheClusterResponseTypeDef",
    {"CacheCluster": ClientModifyCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientModifyCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientModifyCacheParameterGroupResponseTypeDef = TypedDict(
    "ClientModifyCacheParameterGroupResponseTypeDef", {"CacheParameterGroupName": str}, total=False
)

ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)

ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef],
    },
    total=False,
)

ClientModifyCacheSubnetGroupResponseTypeDef = TypedDict(
    "ClientModifyCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientModifyReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientModifyReplicationGroupResponseTypeDef = TypedDict(
    "ClientModifyReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientModifyReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    {"NodeGroupId": str, "PreferredAvailabilityZones": List[str]},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientModifyReplicationGroupShardConfigurationResponseTypeDef = TypedDict(
    "ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    {
        "ReplicationGroup": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef
    },
    total=False,
)

ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef = TypedDict(
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef = TypedDict(
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[
            ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef
        ],
        "ReservationARN": str,
    },
    total=False,
)

ClientPurchaseReservedCacheNodesOfferingResponseTypeDef = TypedDict(
    "ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    {"ReservedCacheNode": ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)

ClientRebootCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)

ClientRebootCacheClusterResponseTypeDef = TypedDict(
    "ClientRebootCacheClusterResponseTypeDef",
    {"CacheCluster": ClientRebootCacheClusterResponseCacheClusterTypeDef},
    total=False,
)

ClientRemoveTagsFromResourceResponseTagListTypeDef = TypedDict(
    "ClientRemoveTagsFromResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "ClientRemoveTagsFromResourceResponseTypeDef",
    {"TagList": List[ClientRemoveTagsFromResourceResponseTagListTypeDef]},
    total=False,
)

ClientResetCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientResetCacheParameterGroupResponseTypeDef = TypedDict(
    "ClientResetCacheParameterGroupResponseTypeDef", {"CacheParameterGroupName": str}, total=False
)

ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)

ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientRevokeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    {"CacheSecurityGroup": ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef},
    total=False,
)

ClientStartMigrationCustomerNodeEndpointListTypeDef = TypedDict(
    "ClientStartMigrationCustomerNodeEndpointListTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientStartMigrationResponseReplicationGroupTypeDef = TypedDict(
    "ClientStartMigrationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientStartMigrationResponseTypeDef = TypedDict(
    "ClientStartMigrationResponseTypeDef",
    {"ReplicationGroup": ClientStartMigrationResponseReplicationGroupTypeDef},
    total=False,
)

ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)

ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ClientTestFailoverResponseReplicationGroupTypeDef = TypedDict(
    "ClientTestFailoverResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ClientTestFailoverResponseTypeDef = TypedDict(
    "ClientTestFailoverResponseTypeDef",
    {"ReplicationGroup": ClientTestFailoverResponseReplicationGroupTypeDef},
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[ParameterTypeDef],
        "CacheNodeTypeSpecificParameters": List[CacheNodeTypeSpecificParameterTypeDef],
    },
    total=False,
)

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {"EngineDefaults": EngineDefaultsTypeDef},
    total=False,
)

NodeGroupConfigurationTypeDef = TypedDict(
    "NodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)

NodeSnapshotTypeDef = TypedDict(
    "NodeSnapshotTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": NodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "NodeSnapshots": List[NodeSnapshotTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)

DescribeSnapshotsListMessageTypeDef = TypedDict(
    "DescribeSnapshotsListMessageTypeDef",
    {"Marker": str, "Snapshots": List[SnapshotTypeDef]},
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef", {"Marker": str, "Events": List[EventTypeDef]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

NodeGroupMemberTypeDef = TypedDict(
    "NodeGroupMemberTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": EndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)

NodeGroupTypeDef = TypedDict(
    "NodeGroupTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": EndpointTypeDef,
        "ReaderEndpoint": EndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[NodeGroupMemberTypeDef],
    },
    total=False,
)

SlotMigrationTypeDef = TypedDict("SlotMigrationTypeDef", {"ProgressPercentage": float}, total=False)

ReshardingStatusTypeDef = TypedDict(
    "ReshardingStatusTypeDef", {"SlotMigration": SlotMigrationTypeDef}, total=False
)

ReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": Literal["enabled", "disabled"],
        "Resharding": ReshardingStatusTypeDef,
        "AuthTokenStatus": Literal["SETTING", "ROTATING"],
    },
    total=False,
)

ReplicationGroupTypeDef = TypedDict(
    "ReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[NodeGroupTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": Literal["enabled", "disabled", "enabling", "disabling"],
        "ConfigurationEndpoint": EndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ReplicationGroupMessageTypeDef = TypedDict(
    "ReplicationGroupMessageTypeDef",
    {"Marker": str, "ReplicationGroups": List[ReplicationGroupTypeDef]},
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedCacheNodeTypeDef = TypedDict(
    "ReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[RecurringChargeTypeDef],
        "ReservationARN": str,
    },
    total=False,
)

ReservedCacheNodeMessageTypeDef = TypedDict(
    "ReservedCacheNodeMessageTypeDef",
    {"Marker": str, "ReservedCacheNodes": List[ReservedCacheNodeTypeDef]},
    total=False,
)

ReservedCacheNodesOfferingTypeDef = TypedDict(
    "ReservedCacheNodesOfferingTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List[RecurringChargeTypeDef],
    },
    total=False,
)

ReservedCacheNodesOfferingMessageTypeDef = TypedDict(
    "ReservedCacheNodesOfferingMessageTypeDef",
    {"Marker": str, "ReservedCacheNodesOfferings": List[ReservedCacheNodesOfferingTypeDef]},
    total=False,
)

ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": Literal["security-update"],
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)

ServiceUpdatesMessageTypeDef = TypedDict(
    "ServiceUpdatesMessageTypeDef",
    {"Marker": str, "ServiceUpdates": List[ServiceUpdateTypeDef]},
    total=False,
)

TimeRangeFilterTypeDef = TypedDict(
    "TimeRangeFilterTypeDef", {"StartTime": datetime, "EndTime": datetime}, total=False
)

CacheNodeUpdateStatusTypeDef = TypedDict(
    "CacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

NodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "NodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": Literal["system", "customer"],
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

NodeGroupUpdateStatusTypeDef = TypedDict(
    "NodeGroupUpdateStatusTypeDef",
    {"NodeGroupId": str, "NodeGroupMemberUpdateStatus": List[NodeGroupMemberUpdateStatusTypeDef]},
    total=False,
)

UpdateActionTypeDef = TypedDict(
    "UpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": Literal["critical", "important", "medium", "low"],
        "ServiceUpdateStatus": Literal["available", "cancelled", "expired"],
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": Literal["security-update"],
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": Literal[
            "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
        ],
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": Literal["yes", "no", "n/a"],
        "NodeGroupUpdateStatus": List[NodeGroupUpdateStatusTypeDef],
        "CacheNodeUpdateStatus": List[CacheNodeUpdateStatusTypeDef],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)

UpdateActionsMessageTypeDef = TypedDict(
    "UpdateActionsMessageTypeDef",
    {"Marker": str, "UpdateActions": List[UpdateActionTypeDef]},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
