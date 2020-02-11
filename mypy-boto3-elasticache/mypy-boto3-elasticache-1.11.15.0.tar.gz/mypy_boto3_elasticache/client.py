"""
Main interface for elasticache service client

Usage::

    import boto3
    from mypy_boto3.elasticache import ElastiCacheClient

    session = boto3.Session()

    client: ElastiCacheClient = boto3.client("elasticache")
    session_client: ElastiCacheClient = session.client("elasticache")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elasticache.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elasticache.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_elasticache.type_defs import (
    ClientAddTagsToResourceResponseTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef,
    ClientBatchApplyUpdateActionResponseTypeDef,
    ClientBatchStopUpdateActionResponseTypeDef,
    ClientCompleteMigrationResponseTypeDef,
    ClientCopySnapshotResponseTypeDef,
    ClientCreateCacheClusterResponseTypeDef,
    ClientCreateCacheClusterTagsTypeDef,
    ClientCreateCacheParameterGroupResponseTypeDef,
    ClientCreateCacheSecurityGroupResponseTypeDef,
    ClientCreateCacheSubnetGroupResponseTypeDef,
    ClientCreateReplicationGroupNodeGroupConfigurationTypeDef,
    ClientCreateReplicationGroupResponseTypeDef,
    ClientCreateReplicationGroupTagsTypeDef,
    ClientCreateSnapshotResponseTypeDef,
    ClientDecreaseReplicaCountReplicaConfigurationTypeDef,
    ClientDecreaseReplicaCountResponseTypeDef,
    ClientDeleteCacheClusterResponseTypeDef,
    ClientDeleteReplicationGroupResponseTypeDef,
    ClientDeleteSnapshotResponseTypeDef,
    ClientDescribeCacheClustersResponseTypeDef,
    ClientDescribeCacheEngineVersionsResponseTypeDef,
    ClientDescribeCacheParameterGroupsResponseTypeDef,
    ClientDescribeCacheParametersResponseTypeDef,
    ClientDescribeCacheSecurityGroupsResponseTypeDef,
    ClientDescribeCacheSubnetGroupsResponseTypeDef,
    ClientDescribeEngineDefaultParametersResponseTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeReplicationGroupsResponseTypeDef,
    ClientDescribeReservedCacheNodesOfferingsResponseTypeDef,
    ClientDescribeReservedCacheNodesResponseTypeDef,
    ClientDescribeServiceUpdatesResponseTypeDef,
    ClientDescribeSnapshotsResponseTypeDef,
    ClientDescribeUpdateActionsResponseTypeDef,
    ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef,
    ClientIncreaseReplicaCountReplicaConfigurationTypeDef,
    ClientIncreaseReplicaCountResponseTypeDef,
    ClientListAllowedNodeTypeModificationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyCacheClusterResponseTypeDef,
    ClientModifyCacheParameterGroupParameterNameValuesTypeDef,
    ClientModifyCacheParameterGroupResponseTypeDef,
    ClientModifyCacheSubnetGroupResponseTypeDef,
    ClientModifyReplicationGroupResponseTypeDef,
    ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef,
    ClientModifyReplicationGroupShardConfigurationResponseTypeDef,
    ClientPurchaseReservedCacheNodesOfferingResponseTypeDef,
    ClientRebootCacheClusterResponseTypeDef,
    ClientRemoveTagsFromResourceResponseTypeDef,
    ClientResetCacheParameterGroupParameterNameValuesTypeDef,
    ClientResetCacheParameterGroupResponseTypeDef,
    ClientRevokeCacheSecurityGroupIngressResponseTypeDef,
    ClientStartMigrationCustomerNodeEndpointListTypeDef,
    ClientStartMigrationResponseTypeDef,
    ClientTestFailoverResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elasticache.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElastiCacheClient",)


class ElastiCacheClient:
    """
    [ElastiCache.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags_to_resource(
        self, ResourceName: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> ClientAddTagsToResourceResponseTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.add_tags_to_resource)
        """

    def authorize_cache_security_group_ingress(
        self, CacheSecurityGroupName: str, EC2SecurityGroupName: str, EC2SecurityGroupOwnerId: str
    ) -> ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef:
        """
        [Client.authorize_cache_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.authorize_cache_security_group_ingress)
        """

    def batch_apply_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
    ) -> ClientBatchApplyUpdateActionResponseTypeDef:
        """
        [Client.batch_apply_update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.batch_apply_update_action)
        """

    def batch_stop_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
    ) -> ClientBatchStopUpdateActionResponseTypeDef:
        """
        [Client.batch_stop_update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.batch_stop_update_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.can_paginate)
        """

    def complete_migration(
        self, ReplicationGroupId: str, Force: bool = None
    ) -> ClientCompleteMigrationResponseTypeDef:
        """
        [Client.complete_migration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.complete_migration)
        """

    def copy_snapshot(
        self,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: str = None,
        KmsKeyId: str = None,
    ) -> ClientCopySnapshotResponseTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.copy_snapshot)
        """

    def create_cache_cluster(
        self,
        CacheClusterId: str,
        ReplicationGroupId: str = None,
        AZMode: Literal["single-az", "cross-az"] = None,
        PreferredAvailabilityZone: str = None,
        PreferredAvailabilityZones: List[str] = None,
        NumCacheNodes: int = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateCacheClusterTagsTypeDef] = None,
        SnapshotArns: List[str] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
    ) -> ClientCreateCacheClusterResponseTypeDef:
        """
        [Client.create_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.create_cache_cluster)
        """

    def create_cache_parameter_group(
        self, CacheParameterGroupName: str, CacheParameterGroupFamily: str, Description: str
    ) -> ClientCreateCacheParameterGroupResponseTypeDef:
        """
        [Client.create_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.create_cache_parameter_group)
        """

    def create_cache_security_group(
        self, CacheSecurityGroupName: str, Description: str
    ) -> ClientCreateCacheSecurityGroupResponseTypeDef:
        """
        [Client.create_cache_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.create_cache_security_group)
        """

    def create_cache_subnet_group(
        self, CacheSubnetGroupName: str, CacheSubnetGroupDescription: str, SubnetIds: List[str]
    ) -> ClientCreateCacheSubnetGroupResponseTypeDef:
        """
        [Client.create_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.create_cache_subnet_group)
        """

    def create_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str,
        PrimaryClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        NumCacheClusters: int = None,
        PreferredCacheClusterAZs: List[str] = None,
        NumNodeGroups: int = None,
        ReplicasPerNodeGroup: int = None,
        NodeGroupConfiguration: List[
            ClientCreateReplicationGroupNodeGroupConfigurationTypeDef
        ] = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateReplicationGroupTagsTypeDef] = None,
        SnapshotArns: List[str] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
        TransitEncryptionEnabled: bool = None,
        AtRestEncryptionEnabled: bool = None,
        KmsKeyId: str = None,
    ) -> ClientCreateReplicationGroupResponseTypeDef:
        """
        [Client.create_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.create_replication_group)
        """

    def create_snapshot(
        self,
        SnapshotName: str,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        KmsKeyId: str = None,
    ) -> ClientCreateSnapshotResponseTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.create_snapshot)
        """

    def decrease_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[ClientDecreaseReplicaCountReplicaConfigurationTypeDef] = None,
        ReplicasToRemove: List[str] = None,
    ) -> ClientDecreaseReplicaCountResponseTypeDef:
        """
        [Client.decrease_replica_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.decrease_replica_count)
        """

    def delete_cache_cluster(
        self, CacheClusterId: str, FinalSnapshotIdentifier: str = None
    ) -> ClientDeleteCacheClusterResponseTypeDef:
        """
        [Client.delete_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.delete_cache_cluster)
        """

    def delete_cache_parameter_group(self, CacheParameterGroupName: str) -> None:
        """
        [Client.delete_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.delete_cache_parameter_group)
        """

    def delete_cache_security_group(self, CacheSecurityGroupName: str) -> None:
        """
        [Client.delete_cache_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.delete_cache_security_group)
        """

    def delete_cache_subnet_group(self, CacheSubnetGroupName: str) -> None:
        """
        [Client.delete_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.delete_cache_subnet_group)
        """

    def delete_replication_group(
        self,
        ReplicationGroupId: str,
        RetainPrimaryCluster: bool = None,
        FinalSnapshotIdentifier: str = None,
    ) -> ClientDeleteReplicationGroupResponseTypeDef:
        """
        [Client.delete_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.delete_replication_group)
        """

    def delete_snapshot(self, SnapshotName: str) -> ClientDeleteSnapshotResponseTypeDef:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.delete_snapshot)
        """

    def describe_cache_clusters(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
    ) -> ClientDescribeCacheClustersResponseTypeDef:
        """
        [Client.describe_cache_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_cache_clusters)
        """

    def describe_cache_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
    ) -> ClientDescribeCacheEngineVersionsResponseTypeDef:
        """
        [Client.describe_cache_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_cache_engine_versions)
        """

    def describe_cache_parameter_groups(
        self, CacheParameterGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeCacheParameterGroupsResponseTypeDef:
        """
        [Client.describe_cache_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameter_groups)
        """

    def describe_cache_parameters(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCacheParametersResponseTypeDef:
        """
        [Client.describe_cache_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameters)
        """

    def describe_cache_security_groups(
        self, CacheSecurityGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeCacheSecurityGroupsResponseTypeDef:
        """
        [Client.describe_cache_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_cache_security_groups)
        """

    def describe_cache_subnet_groups(
        self, CacheSubnetGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeCacheSubnetGroupsResponseTypeDef:
        """
        [Client.describe_cache_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_cache_subnet_groups)
        """

    def describe_engine_default_parameters(
        self, CacheParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeEngineDefaultParametersResponseTypeDef:
        """
        [Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_engine_default_parameters)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_events)
        """

    def describe_replication_groups(
        self, ReplicationGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeReplicationGroupsResponseTypeDef:
        """
        [Client.describe_replication_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_replication_groups)
        """

    def describe_reserved_cache_nodes(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReservedCacheNodesResponseTypeDef:
        """
        [Client.describe_reserved_cache_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes)
        """

    def describe_reserved_cache_nodes_offerings(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReservedCacheNodesOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_cache_nodes_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes_offerings)
        """

    def describe_service_updates(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeServiceUpdatesResponseTypeDef:
        """
        [Client.describe_service_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_service_updates)
        """

    def describe_snapshots(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        Marker: str = None,
        MaxRecords: int = None,
        ShowNodeGroupConfig: bool = None,
    ) -> ClientDescribeSnapshotsResponseTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_snapshots)
        """

    def describe_update_actions(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        ServiceUpdateTimeRange: ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef = None,
        UpdateActionStatus: List[
            Literal[
                "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
            ]
        ] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeUpdateActionsResponseTypeDef:
        """
        [Client.describe_update_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.describe_update_actions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.generate_presigned_url)
        """

    def increase_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[ClientIncreaseReplicaCountReplicaConfigurationTypeDef] = None,
    ) -> ClientIncreaseReplicaCountResponseTypeDef:
        """
        [Client.increase_replica_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.increase_replica_count)
        """

    def list_allowed_node_type_modifications(
        self, CacheClusterId: str = None, ReplicationGroupId: str = None
    ) -> ClientListAllowedNodeTypeModificationsResponseTypeDef:
        """
        [Client.list_allowed_node_type_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.list_allowed_node_type_modifications)
        """

    def list_tags_for_resource(self, ResourceName: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.list_tags_for_resource)
        """

    def modify_cache_cluster(
        self,
        CacheClusterId: str,
        NumCacheNodes: int = None,
        CacheNodeIdsToRemove: List[str] = None,
        AZMode: Literal["single-az", "cross-az"] = None,
        NewAvailabilityZones: List[str] = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: Literal["SET", "ROTATE"] = None,
    ) -> ClientModifyCacheClusterResponseTypeDef:
        """
        [Client.modify_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.modify_cache_cluster)
        """

    def modify_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ParameterNameValues: List[ClientModifyCacheParameterGroupParameterNameValuesTypeDef],
    ) -> ClientModifyCacheParameterGroupResponseTypeDef:
        """
        [Client.modify_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.modify_cache_parameter_group)
        """

    def modify_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str = None,
        SubnetIds: List[str] = None,
    ) -> ClientModifyCacheSubnetGroupResponseTypeDef:
        """
        [Client.modify_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.modify_cache_subnet_group)
        """

    def modify_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str = None,
        PrimaryClusterId: str = None,
        SnapshottingClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        NodeGroupId: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: Literal["SET", "ROTATE"] = None,
    ) -> ClientModifyReplicationGroupResponseTypeDef:
        """
        [Client.modify_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group)
        """

    def modify_replication_group_shard_configuration(
        self,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: List[
            ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef
        ] = None,
        NodeGroupsToRemove: List[str] = None,
        NodeGroupsToRetain: List[str] = None,
    ) -> ClientModifyReplicationGroupShardConfigurationResponseTypeDef:
        """
        [Client.modify_replication_group_shard_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group_shard_configuration)
        """

    def purchase_reserved_cache_nodes_offering(
        self,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: str = None,
        CacheNodeCount: int = None,
    ) -> ClientPurchaseReservedCacheNodesOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_cache_nodes_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.purchase_reserved_cache_nodes_offering)
        """

    def reboot_cache_cluster(
        self, CacheClusterId: str, CacheNodeIdsToReboot: List[str]
    ) -> ClientRebootCacheClusterResponseTypeDef:
        """
        [Client.reboot_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.reboot_cache_cluster)
        """

    def remove_tags_from_resource(
        self, ResourceName: str, TagKeys: List[str]
    ) -> ClientRemoveTagsFromResourceResponseTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.remove_tags_from_resource)
        """

    def reset_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ResetAllParameters: bool = None,
        ParameterNameValues: List[ClientResetCacheParameterGroupParameterNameValuesTypeDef] = None,
    ) -> ClientResetCacheParameterGroupResponseTypeDef:
        """
        [Client.reset_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.reset_cache_parameter_group)
        """

    def revoke_cache_security_group_ingress(
        self, CacheSecurityGroupName: str, EC2SecurityGroupName: str, EC2SecurityGroupOwnerId: str
    ) -> ClientRevokeCacheSecurityGroupIngressResponseTypeDef:
        """
        [Client.revoke_cache_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.revoke_cache_security_group_ingress)
        """

    def start_migration(
        self,
        ReplicationGroupId: str,
        CustomerNodeEndpointList: List[ClientStartMigrationCustomerNodeEndpointListTypeDef],
    ) -> ClientStartMigrationResponseTypeDef:
        """
        [Client.start_migration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.start_migration)
        """

    def test_failover(
        self, ReplicationGroupId: str, NodeGroupId: str
    ) -> ClientTestFailoverResponseTypeDef:
        """
        [Client.test_failover documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Client.test_failover)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_clusters"]
    ) -> "paginator_scope.DescribeCacheClustersPaginator":
        """
        [Paginator.DescribeCacheClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_engine_versions"]
    ) -> "paginator_scope.DescribeCacheEngineVersionsPaginator":
        """
        [Paginator.DescribeCacheEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameter_groups"]
    ) -> "paginator_scope.DescribeCacheParameterGroupsPaginator":
        """
        [Paginator.DescribeCacheParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameters"]
    ) -> "paginator_scope.DescribeCacheParametersPaginator":
        """
        [Paginator.DescribeCacheParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_security_groups"]
    ) -> "paginator_scope.DescribeCacheSecurityGroupsPaginator":
        """
        [Paginator.DescribeCacheSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_subnet_groups"]
    ) -> "paginator_scope.DescribeCacheSubnetGroupsPaginator":
        """
        [Paginator.DescribeCacheSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> "paginator_scope.DescribeEngineDefaultParametersPaginator":
        """
        [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_groups"]
    ) -> "paginator_scope.DescribeReplicationGroupsPaginator":
        """
        [Paginator.DescribeReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes"]
    ) -> "paginator_scope.DescribeReservedCacheNodesPaginator":
        """
        [Paginator.DescribeReservedCacheNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes_offerings"]
    ) -> "paginator_scope.DescribeReservedCacheNodesOfferingsPaginator":
        """
        [Paginator.DescribeReservedCacheNodesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_service_updates"]
    ) -> "paginator_scope.DescribeServiceUpdatesPaginator":
        """
        [Paginator.DescribeServiceUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> "paginator_scope.DescribeSnapshotsPaginator":
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_update_actions"]
    ) -> "paginator_scope.DescribeUpdateActionsPaginator":
        """
        [Paginator.DescribeUpdateActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_available"]
    ) -> "waiter_scope.CacheClusterAvailableWaiter":
        """
        [Waiter.CacheClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_deleted"]
    ) -> "waiter_scope.CacheClusterDeletedWaiter":
        """
        [Waiter.CacheClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_group_available"]
    ) -> "waiter_scope.ReplicationGroupAvailableWaiter":
        """
        [Waiter.ReplicationGroupAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_group_deleted"]
    ) -> "waiter_scope.ReplicationGroupDeletedWaiter":
        """
        [Waiter.ReplicationGroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted)
        """


class Exceptions:
    APICallRateForCustomerExceededFault: Boto3ClientError
    AuthorizationAlreadyExistsFault: Boto3ClientError
    AuthorizationNotFoundFault: Boto3ClientError
    CacheClusterAlreadyExistsFault: Boto3ClientError
    CacheClusterNotFoundFault: Boto3ClientError
    CacheParameterGroupAlreadyExistsFault: Boto3ClientError
    CacheParameterGroupNotFoundFault: Boto3ClientError
    CacheParameterGroupQuotaExceededFault: Boto3ClientError
    CacheSecurityGroupAlreadyExistsFault: Boto3ClientError
    CacheSecurityGroupNotFoundFault: Boto3ClientError
    CacheSecurityGroupQuotaExceededFault: Boto3ClientError
    CacheSubnetGroupAlreadyExistsFault: Boto3ClientError
    CacheSubnetGroupInUse: Boto3ClientError
    CacheSubnetGroupNotFoundFault: Boto3ClientError
    CacheSubnetGroupQuotaExceededFault: Boto3ClientError
    CacheSubnetQuotaExceededFault: Boto3ClientError
    ClientError: Boto3ClientError
    ClusterQuotaForCustomerExceededFault: Boto3ClientError
    InsufficientCacheClusterCapacityFault: Boto3ClientError
    InvalidARNFault: Boto3ClientError
    InvalidCacheClusterStateFault: Boto3ClientError
    InvalidCacheParameterGroupStateFault: Boto3ClientError
    InvalidCacheSecurityGroupStateFault: Boto3ClientError
    InvalidKMSKeyFault: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidReplicationGroupStateFault: Boto3ClientError
    InvalidSnapshotStateFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    NoOperationFault: Boto3ClientError
    NodeGroupNotFoundFault: Boto3ClientError
    NodeGroupsPerReplicationGroupQuotaExceededFault: Boto3ClientError
    NodeQuotaForClusterExceededFault: Boto3ClientError
    NodeQuotaForCustomerExceededFault: Boto3ClientError
    ReplicationGroupAlreadyExistsFault: Boto3ClientError
    ReplicationGroupAlreadyUnderMigrationFault: Boto3ClientError
    ReplicationGroupNotFoundFault: Boto3ClientError
    ReplicationGroupNotUnderMigrationFault: Boto3ClientError
    ReservedCacheNodeAlreadyExistsFault: Boto3ClientError
    ReservedCacheNodeNotFoundFault: Boto3ClientError
    ReservedCacheNodeQuotaExceededFault: Boto3ClientError
    ReservedCacheNodesOfferingNotFoundFault: Boto3ClientError
    ServiceLinkedRoleNotFoundFault: Boto3ClientError
    ServiceUpdateNotFoundFault: Boto3ClientError
    SnapshotAlreadyExistsFault: Boto3ClientError
    SnapshotFeatureNotSupportedFault: Boto3ClientError
    SnapshotNotFoundFault: Boto3ClientError
    SnapshotQuotaExceededFault: Boto3ClientError
    SubnetInUse: Boto3ClientError
    TagNotFoundFault: Boto3ClientError
    TagQuotaPerResourceExceeded: Boto3ClientError
    TestFailoverNotAvailableFault: Boto3ClientError
