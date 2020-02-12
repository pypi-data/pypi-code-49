"""
Main interface for neptune service client

Usage::

    import boto3
    from mypy_boto3.neptune import NeptuneClient

    session = boto3.Session()

    client: NeptuneClient = boto3.client("neptune")
    session_client: NeptuneClient = session.client("neptune")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_neptune.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_neptune.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_neptune.type_defs import (
    ClientAddSourceIdentifierToSubscriptionResponseTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientApplyPendingMaintenanceActionResponseTypeDef,
    ClientCopyDbClusterParameterGroupResponseTypeDef,
    ClientCopyDbClusterParameterGroupTagsTypeDef,
    ClientCopyDbClusterSnapshotResponseTypeDef,
    ClientCopyDbClusterSnapshotTagsTypeDef,
    ClientCopyDbParameterGroupResponseTypeDef,
    ClientCopyDbParameterGroupTagsTypeDef,
    ClientCreateDbClusterParameterGroupResponseTypeDef,
    ClientCreateDbClusterParameterGroupTagsTypeDef,
    ClientCreateDbClusterResponseTypeDef,
    ClientCreateDbClusterSnapshotResponseTypeDef,
    ClientCreateDbClusterSnapshotTagsTypeDef,
    ClientCreateDbClusterTagsTypeDef,
    ClientCreateDbInstanceResponseTypeDef,
    ClientCreateDbInstanceTagsTypeDef,
    ClientCreateDbParameterGroupResponseTypeDef,
    ClientCreateDbParameterGroupTagsTypeDef,
    ClientCreateDbSubnetGroupResponseTypeDef,
    ClientCreateDbSubnetGroupTagsTypeDef,
    ClientCreateEventSubscriptionResponseTypeDef,
    ClientCreateEventSubscriptionTagsTypeDef,
    ClientDeleteDbClusterResponseTypeDef,
    ClientDeleteDbClusterSnapshotResponseTypeDef,
    ClientDeleteDbInstanceResponseTypeDef,
    ClientDeleteEventSubscriptionResponseTypeDef,
    ClientDescribeDbClusterParameterGroupsFiltersTypeDef,
    ClientDescribeDbClusterParameterGroupsResponseTypeDef,
    ClientDescribeDbClusterParametersFiltersTypeDef,
    ClientDescribeDbClusterParametersResponseTypeDef,
    ClientDescribeDbClusterSnapshotAttributesResponseTypeDef,
    ClientDescribeDbClusterSnapshotsFiltersTypeDef,
    ClientDescribeDbClusterSnapshotsResponseTypeDef,
    ClientDescribeDbClustersFiltersTypeDef,
    ClientDescribeDbClustersResponseTypeDef,
    ClientDescribeDbEngineVersionsFiltersTypeDef,
    ClientDescribeDbEngineVersionsResponseTypeDef,
    ClientDescribeDbInstancesFiltersTypeDef,
    ClientDescribeDbInstancesResponseTypeDef,
    ClientDescribeDbParameterGroupsFiltersTypeDef,
    ClientDescribeDbParameterGroupsResponseTypeDef,
    ClientDescribeDbParametersFiltersTypeDef,
    ClientDescribeDbParametersResponseTypeDef,
    ClientDescribeDbSubnetGroupsFiltersTypeDef,
    ClientDescribeDbSubnetGroupsResponseTypeDef,
    ClientDescribeEngineDefaultClusterParametersFiltersTypeDef,
    ClientDescribeEngineDefaultClusterParametersResponseTypeDef,
    ClientDescribeEngineDefaultParametersFiltersTypeDef,
    ClientDescribeEngineDefaultParametersResponseTypeDef,
    ClientDescribeEventCategoriesFiltersTypeDef,
    ClientDescribeEventCategoriesResponseTypeDef,
    ClientDescribeEventSubscriptionsFiltersTypeDef,
    ClientDescribeEventSubscriptionsResponseTypeDef,
    ClientDescribeEventsFiltersTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
    ClientDescribeOrderableDbInstanceOptionsResponseTypeDef,
    ClientDescribePendingMaintenanceActionsFiltersTypeDef,
    ClientDescribePendingMaintenanceActionsResponseTypeDef,
    ClientDescribeValidDbInstanceModificationsResponseTypeDef,
    ClientFailoverDbClusterResponseTypeDef,
    ClientListTagsForResourceFiltersTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef,
    ClientModifyDbClusterParameterGroupParametersTypeDef,
    ClientModifyDbClusterParameterGroupResponseTypeDef,
    ClientModifyDbClusterResponseTypeDef,
    ClientModifyDbClusterSnapshotAttributeResponseTypeDef,
    ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef,
    ClientModifyDbInstanceResponseTypeDef,
    ClientModifyDbParameterGroupParametersTypeDef,
    ClientModifyDbParameterGroupResponseTypeDef,
    ClientModifyDbSubnetGroupResponseTypeDef,
    ClientModifyEventSubscriptionResponseTypeDef,
    ClientPromoteReadReplicaDbClusterResponseTypeDef,
    ClientRebootDbInstanceResponseTypeDef,
    ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef,
    ClientResetDbClusterParameterGroupParametersTypeDef,
    ClientResetDbClusterParameterGroupResponseTypeDef,
    ClientResetDbParameterGroupParametersTypeDef,
    ClientResetDbParameterGroupResponseTypeDef,
    ClientRestoreDbClusterFromSnapshotResponseTypeDef,
    ClientRestoreDbClusterFromSnapshotTagsTypeDef,
    ClientRestoreDbClusterToPointInTimeResponseTypeDef,
    ClientRestoreDbClusterToPointInTimeTagsTypeDef,
    ClientStartDbClusterResponseTypeDef,
    ClientStopDbClusterResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_neptune.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NeptuneClient",)


class NeptuneClient:
    """
    [Neptune.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_role_to_db_cluster(self, DBClusterIdentifier: str, RoleArn: str) -> None:
        """
        [Client.add_role_to_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.add_role_to_db_cluster)
        """

    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> ClientAddSourceIdentifierToSubscriptionResponseTypeDef:
        """
        [Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, ResourceName: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ClientApplyPendingMaintenanceActionResponseTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.apply_pending_maintenance_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.can_paginate)
        """

    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List[ClientCopyDbClusterParameterGroupTagsTypeDef] = None,
    ) -> ClientCopyDbClusterParameterGroupResponseTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List[ClientCopyDbClusterSnapshotTagsTypeDef] = None,
        SourceRegion: str = None,
    ) -> ClientCopyDbClusterSnapshotResponseTypeDef:
        """
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: List[ClientCopyDbParameterGroupTagsTypeDef] = None,
    ) -> ClientCopyDbParameterGroupResponseTypeDef:
        """
        [Client.copy_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.copy_db_parameter_group)
        """

    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        ReplicationSourceIdentifier: str = None,
        Tags: List[ClientCreateDbClusterTagsTypeDef] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        SourceRegion: str = None,
    ) -> ClientCreateDbClusterResponseTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_db_cluster)
        """

    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[ClientCreateDbClusterParameterGroupTagsTypeDef] = None,
    ) -> ClientCreateDbClusterParameterGroupResponseTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List[ClientCreateDbClusterSnapshotTagsTypeDef] = None,
    ) -> ClientCreateDbClusterSnapshotResponseTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_db_cluster_snapshot)
        """

    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CharacterSetName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[ClientCreateDbInstanceTagsTypeDef] = None,
        DBClusterIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        Timezone: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> ClientCreateDbInstanceResponseTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_db_instance)
        """

    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[ClientCreateDbParameterGroupTagsTypeDef] = None,
    ) -> ClientCreateDbParameterGroupResponseTypeDef:
        """
        [Client.create_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_db_parameter_group)
        """

    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[ClientCreateDbSubnetGroupTagsTypeDef] = None,
    ) -> ClientCreateDbSubnetGroupResponseTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_db_subnet_group)
        """

    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List[ClientCreateEventSubscriptionTagsTypeDef] = None,
    ) -> ClientCreateEventSubscriptionResponseTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.create_event_subscription)
        """

    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> ClientDeleteDbClusterResponseTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_db_cluster)
        """

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> ClientDeleteDbClusterSnapshotResponseTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> ClientDeleteDbInstanceResponseTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_db_instance)
        """

    def delete_db_parameter_group(self, DBParameterGroupName: str) -> None:
        """
        [Client.delete_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_db_parameter_group)
        """

    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> ClientDeleteEventSubscriptionResponseTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.delete_event_subscription)
        """

    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[ClientDescribeDbClusterParameterGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterParameterGroupsResponseTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[ClientDescribeDbClusterParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterParametersResponseTypeDef:
        """
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> ClientDescribeDbClusterSnapshotAttributesResponseTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[ClientDescribeDbClusterSnapshotsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> ClientDescribeDbClusterSnapshotsResponseTypeDef:
        """
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[ClientDescribeDbClustersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClustersResponseTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_clusters)
        """

    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[ClientDescribeDbEngineVersionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
    ) -> ClientDescribeDbEngineVersionsResponseTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_engine_versions)
        """

    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[ClientDescribeDbInstancesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbInstancesResponseTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_instances)
        """

    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: str = None,
        Filters: List[ClientDescribeDbParameterGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbParameterGroupsResponseTypeDef:
        """
        [Client.describe_db_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_parameter_groups)
        """

    def describe_db_parameters(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[ClientDescribeDbParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbParametersResponseTypeDef:
        """
        [Client.describe_db_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_parameters)
        """

    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[ClientDescribeDbSubnetGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbSubnetGroupsResponseTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[ClientDescribeEngineDefaultClusterParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEngineDefaultClusterParametersResponseTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[ClientDescribeEngineDefaultParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEngineDefaultParametersResponseTypeDef:
        """
        [Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_engine_default_parameters)
        """

    def describe_event_categories(
        self,
        SourceType: str = None,
        Filters: List[ClientDescribeEventCategoriesFiltersTypeDef] = None,
    ) -> ClientDescribeEventCategoriesResponseTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[ClientDescribeEventSubscriptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventSubscriptionsResponseTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_event_subscriptions)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[ClientDescribeEventsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_events)
        """

    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeOrderableDbInstanceOptionsResponseTypeDef:
        """
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[ClientDescribePendingMaintenanceActionsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribePendingMaintenanceActionsResponseTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_pending_maintenance_actions)
        """

    def describe_valid_db_instance_modifications(
        self, DBInstanceIdentifier: str
    ) -> ClientDescribeValidDbInstanceModificationsResponseTypeDef:
        """
        [Client.describe_valid_db_instance_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.describe_valid_db_instance_modifications)
        """

    def failover_db_cluster(
        self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
    ) -> ClientFailoverDbClusterResponseTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.failover_db_cluster)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[ClientListTagsForResourceFiltersTypeDef] = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.list_tags_for_resource)
        """

    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        CloudwatchLogsExportConfiguration: ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
    ) -> ClientModifyDbClusterResponseTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_db_cluster)
        """

    def modify_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        Parameters: List[ClientModifyDbClusterParameterGroupParametersTypeDef],
    ) -> ClientModifyDbClusterParameterGroupResponseTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ClientModifyDbClusterSnapshotAttributeResponseTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        AllocatedStorage: int = None,
        DBInstanceClass: str = None,
        DBSubnetGroupName: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ApplyImmediately: bool = None,
        MasterUserPassword: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        NewDBInstanceIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        CACertificateIdentifier: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        DBPortNumber: int = None,
        PubliclyAccessible: bool = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        CloudwatchLogsExportConfiguration: ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef = None,
        DeletionProtection: bool = None,
    ) -> ClientModifyDbInstanceResponseTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_db_instance)
        """

    def modify_db_parameter_group(
        self,
        DBParameterGroupName: str,
        Parameters: List[ClientModifyDbParameterGroupParametersTypeDef],
    ) -> ClientModifyDbParameterGroupResponseTypeDef:
        """
        [Client.modify_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_db_parameter_group)
        """

    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ClientModifyDbSubnetGroupResponseTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_db_subnet_group)
        """

    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ClientModifyEventSubscriptionResponseTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.modify_event_subscription)
        """

    def promote_read_replica_db_cluster(
        self, DBClusterIdentifier: str
    ) -> ClientPromoteReadReplicaDbClusterResponseTypeDef:
        """
        [Client.promote_read_replica_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.promote_read_replica_db_cluster)
        """

    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> ClientRebootDbInstanceResponseTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.reboot_db_instance)
        """

    def remove_role_from_db_cluster(self, DBClusterIdentifier: str, RoleArn: str) -> None:
        """
        [Client.remove_role_from_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.remove_role_from_db_cluster)
        """

    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef:
        """
        [Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ClientResetDbClusterParameterGroupParametersTypeDef] = None,
    ) -> ClientResetDbClusterParameterGroupResponseTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ClientResetDbParameterGroupParametersTypeDef] = None,
    ) -> ClientResetDbParameterGroupResponseTypeDef:
        """
        [Client.reset_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.reset_db_parameter_group)
        """

    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        DatabaseName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[ClientRestoreDbClusterFromSnapshotTagsTypeDef] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> ClientRestoreDbClusterFromSnapshotResponseTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str = None,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[ClientRestoreDbClusterToPointInTimeTagsTypeDef] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> ClientRestoreDbClusterToPointInTimeResponseTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.restore_db_cluster_to_point_in_time)
        """

    def start_db_cluster(self, DBClusterIdentifier: str) -> ClientStartDbClusterResponseTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.start_db_cluster)
        """

    def stop_db_cluster(self, DBClusterIdentifier: str) -> ClientStopDbClusterResponseTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Client.stop_db_cluster)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> "paginator_scope.DescribeDBClusterParameterGroupsPaginator":
        """
        [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> "paginator_scope.DescribeDBClusterParametersPaginator":
        """
        [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> "paginator_scope.DescribeDBClusterSnapshotsPaginator":
        """
        [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> "paginator_scope.DescribeDBClustersPaginator":
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> "paginator_scope.DescribeDBEngineVersionsPaginator":
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> "paginator_scope.DescribeDBInstancesPaginator":
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> "paginator_scope.DescribeDBParameterGroupsPaginator":
        """
        [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> "paginator_scope.DescribeDBParametersPaginator":
        """
        [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> "paginator_scope.DescribeDBSubnetGroupsPaginator":
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> "paginator_scope.DescribeEngineDefaultParametersPaginator":
        """
        [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> "paginator_scope.DescribeEventSubscriptionsPaginator":
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> "paginator_scope.DescribeOrderableDBInstanceOptionsPaginator":
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> "paginator_scope.DescribePendingMaintenanceActionsPaginator":
        """
        [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> "waiter_scope.DBInstanceAvailableWaiter":
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Waiter.DBInstanceAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> "waiter_scope.DBInstanceDeletedWaiter":
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/neptune.html#Neptune.Waiter.DBInstanceDeleted)
        """


class Exceptions:
    AuthorizationNotFoundFault: Boto3ClientError
    CertificateNotFoundFault: Boto3ClientError
    ClientError: Boto3ClientError
    DBClusterAlreadyExistsFault: Boto3ClientError
    DBClusterNotFoundFault: Boto3ClientError
    DBClusterParameterGroupNotFoundFault: Boto3ClientError
    DBClusterQuotaExceededFault: Boto3ClientError
    DBClusterRoleAlreadyExistsFault: Boto3ClientError
    DBClusterRoleNotFoundFault: Boto3ClientError
    DBClusterRoleQuotaExceededFault: Boto3ClientError
    DBClusterSnapshotAlreadyExistsFault: Boto3ClientError
    DBClusterSnapshotNotFoundFault: Boto3ClientError
    DBInstanceAlreadyExistsFault: Boto3ClientError
    DBInstanceNotFoundFault: Boto3ClientError
    DBParameterGroupAlreadyExistsFault: Boto3ClientError
    DBParameterGroupNotFoundFault: Boto3ClientError
    DBParameterGroupQuotaExceededFault: Boto3ClientError
    DBSecurityGroupNotFoundFault: Boto3ClientError
    DBSnapshotAlreadyExistsFault: Boto3ClientError
    DBSnapshotNotFoundFault: Boto3ClientError
    DBSubnetGroupAlreadyExistsFault: Boto3ClientError
    DBSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    DBSubnetGroupNotFoundFault: Boto3ClientError
    DBSubnetGroupQuotaExceededFault: Boto3ClientError
    DBSubnetQuotaExceededFault: Boto3ClientError
    DBUpgradeDependencyFailureFault: Boto3ClientError
    DomainNotFoundFault: Boto3ClientError
    EventSubscriptionQuotaExceededFault: Boto3ClientError
    InstanceQuotaExceededFault: Boto3ClientError
    InsufficientDBClusterCapacityFault: Boto3ClientError
    InsufficientDBInstanceCapacityFault: Boto3ClientError
    InsufficientStorageClusterCapacityFault: Boto3ClientError
    InvalidDBClusterSnapshotStateFault: Boto3ClientError
    InvalidDBClusterStateFault: Boto3ClientError
    InvalidDBInstanceStateFault: Boto3ClientError
    InvalidDBParameterGroupStateFault: Boto3ClientError
    InvalidDBSecurityGroupStateFault: Boto3ClientError
    InvalidDBSnapshotStateFault: Boto3ClientError
    InvalidDBSubnetGroupStateFault: Boto3ClientError
    InvalidDBSubnetStateFault: Boto3ClientError
    InvalidEventSubscriptionStateFault: Boto3ClientError
    InvalidRestoreFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    OptionGroupNotFoundFault: Boto3ClientError
    ProvisionedIopsNotAvailableInAZFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    SNSInvalidTopicFault: Boto3ClientError
    SNSNoAuthorizationFault: Boto3ClientError
    SNSTopicArnNotFoundFault: Boto3ClientError
    SharedSnapshotQuotaExceededFault: Boto3ClientError
    SnapshotQuotaExceededFault: Boto3ClientError
    SourceNotFoundFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    StorageTypeNotSupportedFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
    SubscriptionAlreadyExistFault: Boto3ClientError
    SubscriptionCategoryNotFoundFault: Boto3ClientError
    SubscriptionNotFoundFault: Boto3ClientError
