"""
Main interface for rds service client

Usage::

    import boto3
    from mypy_boto3.rds import RDSClient

    session = boto3.Session()

    client: RDSClient = boto3.client("rds")
    session_client: RDSClient = session.client("rds")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rds.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rds.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_rds.type_defs import (
    ClientAddSourceIdentifierToSubscriptionResponseTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientApplyPendingMaintenanceActionResponseTypeDef,
    ClientAuthorizeDbSecurityGroupIngressResponseTypeDef,
    ClientBacktrackDbClusterResponseTypeDef,
    ClientCancelExportTaskResponseTypeDef,
    ClientCopyDbClusterParameterGroupResponseTypeDef,
    ClientCopyDbClusterParameterGroupTagsTypeDef,
    ClientCopyDbClusterSnapshotResponseTypeDef,
    ClientCopyDbClusterSnapshotTagsTypeDef,
    ClientCopyDbParameterGroupResponseTypeDef,
    ClientCopyDbParameterGroupTagsTypeDef,
    ClientCopyDbSnapshotResponseTypeDef,
    ClientCopyDbSnapshotTagsTypeDef,
    ClientCopyOptionGroupResponseTypeDef,
    ClientCopyOptionGroupTagsTypeDef,
    ClientCreateCustomAvailabilityZoneResponseTypeDef,
    ClientCreateDbClusterEndpointResponseTypeDef,
    ClientCreateDbClusterEndpointTagsTypeDef,
    ClientCreateDbClusterParameterGroupResponseTypeDef,
    ClientCreateDbClusterParameterGroupTagsTypeDef,
    ClientCreateDbClusterResponseTypeDef,
    ClientCreateDbClusterScalingConfigurationTypeDef,
    ClientCreateDbClusterSnapshotResponseTypeDef,
    ClientCreateDbClusterSnapshotTagsTypeDef,
    ClientCreateDbClusterTagsTypeDef,
    ClientCreateDbInstanceProcessorFeaturesTypeDef,
    ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef,
    ClientCreateDbInstanceReadReplicaResponseTypeDef,
    ClientCreateDbInstanceReadReplicaTagsTypeDef,
    ClientCreateDbInstanceResponseTypeDef,
    ClientCreateDbInstanceTagsTypeDef,
    ClientCreateDbParameterGroupResponseTypeDef,
    ClientCreateDbParameterGroupTagsTypeDef,
    ClientCreateDbProxyAuthTypeDef,
    ClientCreateDbProxyResponseTypeDef,
    ClientCreateDbProxyTagsTypeDef,
    ClientCreateDbSecurityGroupResponseTypeDef,
    ClientCreateDbSecurityGroupTagsTypeDef,
    ClientCreateDbSnapshotResponseTypeDef,
    ClientCreateDbSnapshotTagsTypeDef,
    ClientCreateDbSubnetGroupResponseTypeDef,
    ClientCreateDbSubnetGroupTagsTypeDef,
    ClientCreateEventSubscriptionResponseTypeDef,
    ClientCreateEventSubscriptionTagsTypeDef,
    ClientCreateGlobalClusterResponseTypeDef,
    ClientCreateOptionGroupResponseTypeDef,
    ClientCreateOptionGroupTagsTypeDef,
    ClientDeleteCustomAvailabilityZoneResponseTypeDef,
    ClientDeleteDbClusterEndpointResponseTypeDef,
    ClientDeleteDbClusterResponseTypeDef,
    ClientDeleteDbClusterSnapshotResponseTypeDef,
    ClientDeleteDbInstanceAutomatedBackupResponseTypeDef,
    ClientDeleteDbInstanceResponseTypeDef,
    ClientDeleteDbProxyResponseTypeDef,
    ClientDeleteDbSnapshotResponseTypeDef,
    ClientDeleteEventSubscriptionResponseTypeDef,
    ClientDeleteGlobalClusterResponseTypeDef,
    ClientDeleteInstallationMediaResponseTypeDef,
    ClientDescribeAccountAttributesResponseTypeDef,
    ClientDescribeCertificatesFiltersTypeDef,
    ClientDescribeCertificatesResponseTypeDef,
    ClientDescribeCustomAvailabilityZonesFiltersTypeDef,
    ClientDescribeCustomAvailabilityZonesResponseTypeDef,
    ClientDescribeDbClusterBacktracksFiltersTypeDef,
    ClientDescribeDbClusterBacktracksResponseTypeDef,
    ClientDescribeDbClusterEndpointsFiltersTypeDef,
    ClientDescribeDbClusterEndpointsResponseTypeDef,
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
    ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef,
    ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef,
    ClientDescribeDbInstancesFiltersTypeDef,
    ClientDescribeDbInstancesResponseTypeDef,
    ClientDescribeDbLogFilesFiltersTypeDef,
    ClientDescribeDbLogFilesResponseTypeDef,
    ClientDescribeDbParameterGroupsFiltersTypeDef,
    ClientDescribeDbParameterGroupsResponseTypeDef,
    ClientDescribeDbParametersFiltersTypeDef,
    ClientDescribeDbParametersResponseTypeDef,
    ClientDescribeDbProxiesFiltersTypeDef,
    ClientDescribeDbProxiesResponseTypeDef,
    ClientDescribeDbProxyTargetGroupsFiltersTypeDef,
    ClientDescribeDbProxyTargetGroupsResponseTypeDef,
    ClientDescribeDbProxyTargetsFiltersTypeDef,
    ClientDescribeDbProxyTargetsResponseTypeDef,
    ClientDescribeDbSecurityGroupsFiltersTypeDef,
    ClientDescribeDbSecurityGroupsResponseTypeDef,
    ClientDescribeDbSnapshotAttributesResponseTypeDef,
    ClientDescribeDbSnapshotsFiltersTypeDef,
    ClientDescribeDbSnapshotsResponseTypeDef,
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
    ClientDescribeExportTasksFiltersTypeDef,
    ClientDescribeExportTasksResponseTypeDef,
    ClientDescribeGlobalClustersFiltersTypeDef,
    ClientDescribeGlobalClustersResponseTypeDef,
    ClientDescribeInstallationMediaFiltersTypeDef,
    ClientDescribeInstallationMediaResponseTypeDef,
    ClientDescribeOptionGroupOptionsFiltersTypeDef,
    ClientDescribeOptionGroupOptionsResponseTypeDef,
    ClientDescribeOptionGroupsFiltersTypeDef,
    ClientDescribeOptionGroupsResponseTypeDef,
    ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
    ClientDescribeOrderableDbInstanceOptionsResponseTypeDef,
    ClientDescribePendingMaintenanceActionsFiltersTypeDef,
    ClientDescribePendingMaintenanceActionsResponseTypeDef,
    ClientDescribeReservedDbInstancesFiltersTypeDef,
    ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef,
    ClientDescribeReservedDbInstancesOfferingsResponseTypeDef,
    ClientDescribeReservedDbInstancesResponseTypeDef,
    ClientDescribeSourceRegionsFiltersTypeDef,
    ClientDescribeSourceRegionsResponseTypeDef,
    ClientDescribeValidDbInstanceModificationsResponseTypeDef,
    ClientDownloadDbLogFilePortionResponseTypeDef,
    ClientFailoverDbClusterResponseTypeDef,
    ClientImportInstallationMediaResponseTypeDef,
    ClientListTagsForResourceFiltersTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyCertificatesResponseTypeDef,
    ClientModifyCurrentDbClusterCapacityResponseTypeDef,
    ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef,
    ClientModifyDbClusterEndpointResponseTypeDef,
    ClientModifyDbClusterParameterGroupParametersTypeDef,
    ClientModifyDbClusterParameterGroupResponseTypeDef,
    ClientModifyDbClusterResponseTypeDef,
    ClientModifyDbClusterScalingConfigurationTypeDef,
    ClientModifyDbClusterSnapshotAttributeResponseTypeDef,
    ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef,
    ClientModifyDbInstanceProcessorFeaturesTypeDef,
    ClientModifyDbInstanceResponseTypeDef,
    ClientModifyDbParameterGroupParametersTypeDef,
    ClientModifyDbParameterGroupResponseTypeDef,
    ClientModifyDbProxyAuthTypeDef,
    ClientModifyDbProxyResponseTypeDef,
    ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef,
    ClientModifyDbProxyTargetGroupResponseTypeDef,
    ClientModifyDbSnapshotAttributeResponseTypeDef,
    ClientModifyDbSnapshotResponseTypeDef,
    ClientModifyDbSubnetGroupResponseTypeDef,
    ClientModifyEventSubscriptionResponseTypeDef,
    ClientModifyGlobalClusterResponseTypeDef,
    ClientModifyOptionGroupOptionsToIncludeTypeDef,
    ClientModifyOptionGroupResponseTypeDef,
    ClientPromoteReadReplicaDbClusterResponseTypeDef,
    ClientPromoteReadReplicaResponseTypeDef,
    ClientPurchaseReservedDbInstancesOfferingResponseTypeDef,
    ClientPurchaseReservedDbInstancesOfferingTagsTypeDef,
    ClientRebootDbInstanceResponseTypeDef,
    ClientRegisterDbProxyTargetsResponseTypeDef,
    ClientRemoveFromGlobalClusterResponseTypeDef,
    ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef,
    ClientResetDbClusterParameterGroupParametersTypeDef,
    ClientResetDbClusterParameterGroupResponseTypeDef,
    ClientResetDbParameterGroupParametersTypeDef,
    ClientResetDbParameterGroupResponseTypeDef,
    ClientRestoreDbClusterFromS3ResponseTypeDef,
    ClientRestoreDbClusterFromS3TagsTypeDef,
    ClientRestoreDbClusterFromSnapshotResponseTypeDef,
    ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef,
    ClientRestoreDbClusterFromSnapshotTagsTypeDef,
    ClientRestoreDbClusterToPointInTimeResponseTypeDef,
    ClientRestoreDbClusterToPointInTimeTagsTypeDef,
    ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef,
    ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef,
    ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef,
    ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef,
    ClientRestoreDbInstanceFromS3ResponseTypeDef,
    ClientRestoreDbInstanceFromS3TagsTypeDef,
    ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef,
    ClientRestoreDbInstanceToPointInTimeResponseTypeDef,
    ClientRestoreDbInstanceToPointInTimeTagsTypeDef,
    ClientRevokeDbSecurityGroupIngressResponseTypeDef,
    ClientStartActivityStreamResponseTypeDef,
    ClientStartDbClusterResponseTypeDef,
    ClientStartDbInstanceResponseTypeDef,
    ClientStartExportTaskResponseTypeDef,
    ClientStopActivityStreamResponseTypeDef,
    ClientStopDbClusterResponseTypeDef,
    ClientStopDbInstanceResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rds.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RDSClient",)


class RDSClient:
    """
    [RDS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_role_to_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        """
        [Client.add_role_to_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.add_role_to_db_cluster)
        """

    def add_role_to_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        """
        [Client.add_role_to_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.add_role_to_db_instance)
        """

    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> ClientAddSourceIdentifierToSubscriptionResponseTypeDef:
        """
        [Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, ResourceName: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ClientApplyPendingMaintenanceActionResponseTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.apply_pending_maintenance_action)
        """

    def authorize_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> ClientAuthorizeDbSecurityGroupIngressResponseTypeDef:
        """
        [Client.authorize_db_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.authorize_db_security_group_ingress)
        """

    def backtrack_db_cluster(
        self,
        DBClusterIdentifier: str,
        BacktrackTo: datetime,
        Force: bool = None,
        UseEarliestTimeOnPointInTimeUnavailable: bool = None,
    ) -> ClientBacktrackDbClusterResponseTypeDef:
        """
        [Client.backtrack_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.backtrack_db_cluster)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.can_paginate)
        """

    def cancel_export_task(
        self, ExportTaskIdentifier: str
    ) -> ClientCancelExportTaskResponseTypeDef:
        """
        [Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.cancel_export_task)
        """

    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List[ClientCopyDbClusterParameterGroupTagsTypeDef] = None,
    ) -> ClientCopyDbClusterParameterGroupResponseTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.copy_db_cluster_parameter_group)
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
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: List[ClientCopyDbParameterGroupTagsTypeDef] = None,
    ) -> ClientCopyDbParameterGroupResponseTypeDef:
        """
        [Client.copy_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.copy_db_parameter_group)
        """

    def copy_db_snapshot(
        self,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: str = None,
        Tags: List[ClientCopyDbSnapshotTagsTypeDef] = None,
        CopyTags: bool = None,
        PreSignedUrl: str = None,
        OptionGroupName: str = None,
        SourceRegion: str = None,
    ) -> ClientCopyDbSnapshotResponseTypeDef:
        """
        [Client.copy_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.copy_db_snapshot)
        """

    def copy_option_group(
        self,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: List[ClientCopyOptionGroupTagsTypeDef] = None,
    ) -> ClientCopyOptionGroupResponseTypeDef:
        """
        [Client.copy_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.copy_option_group)
        """

    def create_custom_availability_zone(
        self,
        CustomAvailabilityZoneName: str,
        ExistingVpnId: str = None,
        NewVpnTunnelName: str = None,
        VpnTunnelOriginatorIP: str = None,
    ) -> ClientCreateCustomAvailabilityZoneResponseTypeDef:
        """
        [Client.create_custom_availability_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_custom_availability_zone)
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
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        EngineMode: str = None,
        ScalingConfiguration: ClientCreateDbClusterScalingConfigurationTypeDef = None,
        DeletionProtection: bool = None,
        GlobalClusterIdentifier: str = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
        SourceRegion: str = None,
    ) -> ClientCreateDbClusterResponseTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_cluster)
        """

    def create_db_cluster_endpoint(
        self,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: List[str] = None,
        ExcludedMembers: List[str] = None,
        Tags: List[ClientCreateDbClusterEndpointTagsTypeDef] = None,
    ) -> ClientCreateDbClusterEndpointResponseTypeDef:
        """
        [Client.create_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_cluster_endpoint)
        """

    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[ClientCreateDbClusterParameterGroupTagsTypeDef] = None,
    ) -> ClientCreateDbClusterParameterGroupResponseTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List[ClientCreateDbClusterSnapshotTagsTypeDef] = None,
    ) -> ClientCreateDbClusterSnapshotResponseTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_cluster_snapshot)
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
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ClientCreateDbInstanceProcessorFeaturesTypeDef] = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
    ) -> ClientCreateDbInstanceResponseTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_instance)
        """

    def create_db_instance_read_replica(
        self,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        AvailabilityZone: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        Iops: int = None,
        OptionGroupName: str = None,
        DBParameterGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[ClientCreateDbInstanceReadReplicaTagsTypeDef] = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        StorageType: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        SourceRegion: str = None,
    ) -> ClientCreateDbInstanceReadReplicaResponseTypeDef:
        """
        [Client.create_db_instance_read_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_instance_read_replica)
        """

    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[ClientCreateDbParameterGroupTagsTypeDef] = None,
    ) -> ClientCreateDbParameterGroupResponseTypeDef:
        """
        [Client.create_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_parameter_group)
        """

    def create_db_proxy(
        self,
        DBProxyName: str,
        EngineFamily: str,
        Auth: List[ClientCreateDbProxyAuthTypeDef],
        RoleArn: str,
        VpcSubnetIds: List[str],
        VpcSecurityGroupIds: List[str] = None,
        RequireTLS: bool = None,
        IdleClientTimeout: int = None,
        DebugLogging: bool = None,
        Tags: List[ClientCreateDbProxyTagsTypeDef] = None,
    ) -> ClientCreateDbProxyResponseTypeDef:
        """
        [Client.create_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_proxy)
        """

    def create_db_security_group(
        self,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: List[ClientCreateDbSecurityGroupTagsTypeDef] = None,
    ) -> ClientCreateDbSecurityGroupResponseTypeDef:
        """
        [Client.create_db_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_security_group)
        """

    def create_db_snapshot(
        self,
        DBSnapshotIdentifier: str,
        DBInstanceIdentifier: str,
        Tags: List[ClientCreateDbSnapshotTagsTypeDef] = None,
    ) -> ClientCreateDbSnapshotResponseTypeDef:
        """
        [Client.create_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_snapshot)
        """

    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[ClientCreateDbSubnetGroupTagsTypeDef] = None,
    ) -> ClientCreateDbSubnetGroupResponseTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_db_subnet_group)
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
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_event_subscription)
        """

    def create_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        SourceDBClusterIdentifier: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
        DatabaseName: str = None,
        StorageEncrypted: bool = None,
    ) -> ClientCreateGlobalClusterResponseTypeDef:
        """
        [Client.create_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_global_cluster)
        """

    def create_option_group(
        self,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: List[ClientCreateOptionGroupTagsTypeDef] = None,
    ) -> ClientCreateOptionGroupResponseTypeDef:
        """
        [Client.create_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.create_option_group)
        """

    def delete_custom_availability_zone(
        self, CustomAvailabilityZoneId: str
    ) -> ClientDeleteCustomAvailabilityZoneResponseTypeDef:
        """
        [Client.delete_custom_availability_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_custom_availability_zone)
        """

    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> ClientDeleteDbClusterResponseTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_cluster)
        """

    def delete_db_cluster_endpoint(
        self, DBClusterEndpointIdentifier: str
    ) -> ClientDeleteDbClusterEndpointResponseTypeDef:
        """
        [Client.delete_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_cluster_endpoint)
        """

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> ClientDeleteDbClusterSnapshotResponseTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
        DeleteAutomatedBackups: bool = None,
    ) -> ClientDeleteDbInstanceResponseTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_instance)
        """

    def delete_db_instance_automated_backup(
        self, DbiResourceId: str
    ) -> ClientDeleteDbInstanceAutomatedBackupResponseTypeDef:
        """
        [Client.delete_db_instance_automated_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_instance_automated_backup)
        """

    def delete_db_parameter_group(self, DBParameterGroupName: str) -> None:
        """
        [Client.delete_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_parameter_group)
        """

    def delete_db_proxy(self, DBProxyName: str) -> ClientDeleteDbProxyResponseTypeDef:
        """
        [Client.delete_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_proxy)
        """

    def delete_db_security_group(self, DBSecurityGroupName: str) -> None:
        """
        [Client.delete_db_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_security_group)
        """

    def delete_db_snapshot(
        self, DBSnapshotIdentifier: str
    ) -> ClientDeleteDbSnapshotResponseTypeDef:
        """
        [Client.delete_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_snapshot)
        """

    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> ClientDeleteEventSubscriptionResponseTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_event_subscription)
        """

    def delete_global_cluster(
        self, GlobalClusterIdentifier: str
    ) -> ClientDeleteGlobalClusterResponseTypeDef:
        """
        [Client.delete_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_global_cluster)
        """

    def delete_installation_media(
        self, InstallationMediaId: str
    ) -> ClientDeleteInstallationMediaResponseTypeDef:
        """
        [Client.delete_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_installation_media)
        """

    def delete_option_group(self, OptionGroupName: str) -> None:
        """
        [Client.delete_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.delete_option_group)
        """

    def deregister_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        DBInstanceIdentifiers: List[str] = None,
        DBClusterIdentifiers: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.deregister_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
        """

    def describe_account_attributes(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_account_attributes)
        """

    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[ClientDescribeCertificatesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCertificatesResponseTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_certificates)
        """

    def describe_custom_availability_zones(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[ClientDescribeCustomAvailabilityZonesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCustomAvailabilityZonesResponseTypeDef:
        """
        [Client.describe_custom_availability_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_custom_availability_zones)
        """

    def describe_db_cluster_backtracks(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[ClientDescribeDbClusterBacktracksFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterBacktracksResponseTypeDef:
        """
        [Client.describe_db_cluster_backtracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_cluster_backtracks)
        """

    def describe_db_cluster_endpoints(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[ClientDescribeDbClusterEndpointsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterEndpointsResponseTypeDef:
        """
        [Client.describe_db_cluster_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_cluster_endpoints)
        """

    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[ClientDescribeDbClusterParameterGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbClusterParameterGroupsResponseTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups)
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
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> ClientDescribeDbClusterSnapshotAttributesResponseTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshot_attributes)
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
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[ClientDescribeDbClustersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
    ) -> ClientDescribeDbClustersResponseTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_clusters)
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
        IncludeAll: bool = None,
    ) -> ClientDescribeDbEngineVersionsResponseTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_engine_versions)
        """

    def describe_db_instance_automated_backups(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef:
        """
        [Client.describe_db_instance_automated_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_instance_automated_backups)
        """

    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[ClientDescribeDbInstancesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbInstancesResponseTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_instances)
        """

    def describe_db_log_files(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[ClientDescribeDbLogFilesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbLogFilesResponseTypeDef:
        """
        [Client.describe_db_log_files documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_log_files)
        """

    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: str = None,
        Filters: List[ClientDescribeDbParameterGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbParameterGroupsResponseTypeDef:
        """
        [Client.describe_db_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_parameter_groups)
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
        [Client.describe_db_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_parameters)
        """

    def describe_db_proxies(
        self,
        DBProxyName: str = None,
        Filters: List[ClientDescribeDbProxiesFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribeDbProxiesResponseTypeDef:
        """
        [Client.describe_db_proxies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_proxies)
        """

    def describe_db_proxy_target_groups(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[ClientDescribeDbProxyTargetGroupsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribeDbProxyTargetGroupsResponseTypeDef:
        """
        [Client.describe_db_proxy_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_proxy_target_groups)
        """

    def describe_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[ClientDescribeDbProxyTargetsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribeDbProxyTargetsResponseTypeDef:
        """
        [Client.describe_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_proxy_targets)
        """

    def describe_db_security_groups(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[ClientDescribeDbSecurityGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbSecurityGroupsResponseTypeDef:
        """
        [Client.describe_db_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_security_groups)
        """

    def describe_db_snapshot_attributes(
        self, DBSnapshotIdentifier: str
    ) -> ClientDescribeDbSnapshotAttributesResponseTypeDef:
        """
        [Client.describe_db_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_snapshot_attributes)
        """

    def describe_db_snapshots(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[ClientDescribeDbSnapshotsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
    ) -> ClientDescribeDbSnapshotsResponseTypeDef:
        """
        [Client.describe_db_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_snapshots)
        """

    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[ClientDescribeDbSubnetGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeDbSubnetGroupsResponseTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[ClientDescribeEngineDefaultClusterParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEngineDefaultClusterParametersResponseTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[ClientDescribeEngineDefaultParametersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEngineDefaultParametersResponseTypeDef:
        """
        [Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_engine_default_parameters)
        """

    def describe_event_categories(
        self,
        SourceType: str = None,
        Filters: List[ClientDescribeEventCategoriesFiltersTypeDef] = None,
    ) -> ClientDescribeEventCategoriesResponseTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[ClientDescribeEventSubscriptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventSubscriptionsResponseTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_event_subscriptions)
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
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_events)
        """

    def describe_export_tasks(
        self,
        ExportTaskIdentifier: str = None,
        SourceArn: str = None,
        Filters: List[ClientDescribeExportTasksFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: str = None,
    ) -> ClientDescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_export_tasks)
        """

    def describe_global_clusters(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[ClientDescribeGlobalClustersFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeGlobalClustersResponseTypeDef:
        """
        [Client.describe_global_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_global_clusters)
        """

    def describe_installation_media(
        self,
        InstallationMediaId: str = None,
        Filters: List[ClientDescribeInstallationMediaFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeInstallationMediaResponseTypeDef:
        """
        [Client.describe_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_installation_media)
        """

    def describe_option_group_options(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[ClientDescribeOptionGroupOptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeOptionGroupOptionsResponseTypeDef:
        """
        [Client.describe_option_group_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_option_group_options)
        """

    def describe_option_groups(
        self,
        OptionGroupName: str = None,
        Filters: List[ClientDescribeOptionGroupsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
    ) -> ClientDescribeOptionGroupsResponseTypeDef:
        """
        [Client.describe_option_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_option_groups)
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
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[ClientDescribePendingMaintenanceActionsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribePendingMaintenanceActionsResponseTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_pending_maintenance_actions)
        """

    def describe_reserved_db_instances(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[ClientDescribeReservedDbInstancesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReservedDbInstancesResponseTypeDef:
        """
        [Client.describe_reserved_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_reserved_db_instances)
        """

    def describe_reserved_db_instances_offerings(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReservedDbInstancesOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_db_instances_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_reserved_db_instances_offerings)
        """

    def describe_source_regions(
        self,
        RegionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[ClientDescribeSourceRegionsFiltersTypeDef] = None,
    ) -> ClientDescribeSourceRegionsResponseTypeDef:
        """
        [Client.describe_source_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_source_regions)
        """

    def describe_valid_db_instance_modifications(
        self, DBInstanceIdentifier: str
    ) -> ClientDescribeValidDbInstanceModificationsResponseTypeDef:
        """
        [Client.describe_valid_db_instance_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.describe_valid_db_instance_modifications)
        """

    def download_db_log_file_portion(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: str = None,
        NumberOfLines: int = None,
    ) -> ClientDownloadDbLogFilePortionResponseTypeDef:
        """
        [Client.download_db_log_file_portion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.download_db_log_file_portion)
        """

    def failover_db_cluster(
        self, DBClusterIdentifier: str, TargetDBInstanceIdentifier: str = None
    ) -> ClientFailoverDbClusterResponseTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.failover_db_cluster)
        """

    def generate_db_auth_token(
        self, DBHostname: str, Port: int, DBUsername: str, Region: str = None
    ) -> None:
        """
        [Client.generate_db_auth_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.generate_db_auth_token)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.generate_presigned_url)
        """

    def import_installation_media(
        self,
        CustomAvailabilityZoneId: str,
        Engine: str,
        EngineVersion: str,
        EngineInstallationMediaPath: str,
        OSInstallationMediaPath: str,
    ) -> ClientImportInstallationMediaResponseTypeDef:
        """
        [Client.import_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.import_installation_media)
        """

    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[ClientListTagsForResourceFiltersTypeDef] = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.list_tags_for_resource)
        """

    def modify_certificates(
        self, CertificateIdentifier: str = None, RemoveCustomerOverride: bool = None
    ) -> ClientModifyCertificatesResponseTypeDef:
        """
        [Client.modify_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_certificates)
        """

    def modify_current_db_cluster_capacity(
        self,
        DBClusterIdentifier: str,
        Capacity: int = None,
        SecondsBeforeTimeout: int = None,
        TimeoutAction: str = None,
    ) -> ClientModifyCurrentDbClusterCapacityResponseTypeDef:
        """
        [Client.modify_current_db_cluster_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_current_db_cluster_capacity)
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
        BacktrackWindow: int = None,
        CloudwatchLogsExportConfiguration: ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        DBInstanceParameterGroupName: str = None,
        ScalingConfiguration: ClientModifyDbClusterScalingConfigurationTypeDef = None,
        DeletionProtection: bool = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> ClientModifyDbClusterResponseTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_cluster)
        """

    def modify_db_cluster_endpoint(
        self,
        DBClusterEndpointIdentifier: str,
        EndpointType: str = None,
        StaticMembers: List[str] = None,
        ExcludedMembers: List[str] = None,
    ) -> ClientModifyDbClusterEndpointResponseTypeDef:
        """
        [Client.modify_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_cluster_endpoint)
        """

    def modify_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        Parameters: List[ClientModifyDbClusterParameterGroupParametersTypeDef],
    ) -> ClientModifyDbClusterParameterGroupResponseTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ClientModifyDbClusterSnapshotAttributeResponseTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_cluster_snapshot_attribute)
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
        PerformanceInsightsRetentionPeriod: int = None,
        CloudwatchLogsExportConfiguration: ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef = None,
        ProcessorFeatures: List[ClientModifyDbInstanceProcessorFeaturesTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
        CertificateRotationRestart: bool = None,
    ) -> ClientModifyDbInstanceResponseTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_instance)
        """

    def modify_db_parameter_group(
        self,
        DBParameterGroupName: str,
        Parameters: List[ClientModifyDbParameterGroupParametersTypeDef],
    ) -> ClientModifyDbParameterGroupResponseTypeDef:
        """
        [Client.modify_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_parameter_group)
        """

    def modify_db_proxy(
        self,
        DBProxyName: str,
        NewDBProxyName: str = None,
        Auth: List[ClientModifyDbProxyAuthTypeDef] = None,
        RequireTLS: bool = None,
        IdleClientTimeout: int = None,
        DebugLogging: bool = None,
        RoleArn: str = None,
        SecurityGroups: List[str] = None,
    ) -> ClientModifyDbProxyResponseTypeDef:
        """
        [Client.modify_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_proxy)
        """

    def modify_db_proxy_target_group(
        self,
        TargetGroupName: str,
        DBProxyName: str,
        ConnectionPoolConfig: ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef = None,
        NewName: str = None,
    ) -> ClientModifyDbProxyTargetGroupResponseTypeDef:
        """
        [Client.modify_db_proxy_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
        """

    def modify_db_snapshot(
        self, DBSnapshotIdentifier: str, EngineVersion: str = None, OptionGroupName: str = None
    ) -> ClientModifyDbSnapshotResponseTypeDef:
        """
        [Client.modify_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_snapshot)
        """

    def modify_db_snapshot_attribute(
        self,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ClientModifyDbSnapshotAttributeResponseTypeDef:
        """
        [Client.modify_db_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_snapshot_attribute)
        """

    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ClientModifyDbSubnetGroupResponseTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_db_subnet_group)
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
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_event_subscription)
        """

    def modify_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        NewGlobalClusterIdentifier: str = None,
        DeletionProtection: bool = None,
    ) -> ClientModifyGlobalClusterResponseTypeDef:
        """
        [Client.modify_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_global_cluster)
        """

    def modify_option_group(
        self,
        OptionGroupName: str,
        OptionsToInclude: List[ClientModifyOptionGroupOptionsToIncludeTypeDef] = None,
        OptionsToRemove: List[str] = None,
        ApplyImmediately: bool = None,
    ) -> ClientModifyOptionGroupResponseTypeDef:
        """
        [Client.modify_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.modify_option_group)
        """

    def promote_read_replica(
        self,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
    ) -> ClientPromoteReadReplicaResponseTypeDef:
        """
        [Client.promote_read_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.promote_read_replica)
        """

    def promote_read_replica_db_cluster(
        self, DBClusterIdentifier: str
    ) -> ClientPromoteReadReplicaDbClusterResponseTypeDef:
        """
        [Client.promote_read_replica_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.promote_read_replica_db_cluster)
        """

    def purchase_reserved_db_instances_offering(
        self,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: str = None,
        DBInstanceCount: int = None,
        Tags: List[ClientPurchaseReservedDbInstancesOfferingTagsTypeDef] = None,
    ) -> ClientPurchaseReservedDbInstancesOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_db_instances_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.purchase_reserved_db_instances_offering)
        """

    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> ClientRebootDbInstanceResponseTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.reboot_db_instance)
        """

    def register_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        DBInstanceIdentifiers: List[str] = None,
        DBClusterIdentifiers: List[str] = None,
    ) -> ClientRegisterDbProxyTargetsResponseTypeDef:
        """
        [Client.register_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
        """

    def remove_from_global_cluster(
        self, GlobalClusterIdentifier: str = None, DbClusterIdentifier: str = None
    ) -> ClientRemoveFromGlobalClusterResponseTypeDef:
        """
        [Client.remove_from_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.remove_from_global_cluster)
        """

    def remove_role_from_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        """
        [Client.remove_role_from_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.remove_role_from_db_cluster)
        """

    def remove_role_from_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        """
        [Client.remove_role_from_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.remove_role_from_db_instance)
        """

    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef:
        """
        [Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ClientResetDbClusterParameterGroupParametersTypeDef] = None,
    ) -> ClientResetDbClusterParameterGroupResponseTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ClientResetDbParameterGroupParametersTypeDef] = None,
    ) -> ClientResetDbParameterGroupResponseTypeDef:
        """
        [Client.reset_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.reset_db_parameter_group)
        """

    def restore_db_cluster_from_s3(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List[ClientRestoreDbClusterFromS3TagsTypeDef] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> ClientRestoreDbClusterFromS3ResponseTypeDef:
        """
        [Client.restore_db_cluster_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.restore_db_cluster_from_s3)
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
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        EngineMode: str = None,
        ScalingConfiguration: ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> ClientRestoreDbClusterFromSnapshotResponseTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.restore_db_cluster_from_snapshot)
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
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> ClientRestoreDbClusterToPointInTimeResponseTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.restore_db_cluster_to_point_in_time)
        """

    def restore_db_instance_from_db_snapshot(
        self,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        Tags: List[ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[
            ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef
        ] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef:
        """
        [Client.restore_db_instance_from_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.restore_db_instance_from_db_snapshot)
        """

    def restore_db_instance_from_s3(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
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
        PubliclyAccessible: bool = None,
        Tags: List[ClientRestoreDbInstanceFromS3TagsTypeDef] = None,
        StorageType: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
    ) -> ClientRestoreDbInstanceFromS3ResponseTypeDef:
        """
        [Client.restore_db_instance_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.restore_db_instance_from_s3)
        """

    def restore_db_instance_to_point_in_time(
        self,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str = None,
        RestoreTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CopyTagsToSnapshot: bool = None,
        Tags: List[ClientRestoreDbInstanceToPointInTimeTagsTypeDef] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[
            ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef
        ] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
        SourceDbiResourceId: str = None,
    ) -> ClientRestoreDbInstanceToPointInTimeResponseTypeDef:
        """
        [Client.restore_db_instance_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.restore_db_instance_to_point_in_time)
        """

    def revoke_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> ClientRevokeDbSecurityGroupIngressResponseTypeDef:
        """
        [Client.revoke_db_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.revoke_db_security_group_ingress)
        """

    def start_activity_stream(
        self,
        ResourceArn: str,
        Mode: Literal["sync", "async"],
        KmsKeyId: str,
        ApplyImmediately: bool = None,
    ) -> ClientStartActivityStreamResponseTypeDef:
        """
        [Client.start_activity_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.start_activity_stream)
        """

    def start_db_cluster(self, DBClusterIdentifier: str) -> ClientStartDbClusterResponseTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.start_db_cluster)
        """

    def start_db_instance(self, DBInstanceIdentifier: str) -> ClientStartDbInstanceResponseTypeDef:
        """
        [Client.start_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.start_db_instance)
        """

    def start_export_task(
        self,
        ExportTaskIdentifier: str,
        SourceArn: str,
        S3BucketName: str,
        IamRoleArn: str,
        KmsKeyId: str,
        S3Prefix: str = None,
        ExportOnly: List[str] = None,
    ) -> ClientStartExportTaskResponseTypeDef:
        """
        [Client.start_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.start_export_task)
        """

    def stop_activity_stream(
        self, ResourceArn: str, ApplyImmediately: bool = None
    ) -> ClientStopActivityStreamResponseTypeDef:
        """
        [Client.stop_activity_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.stop_activity_stream)
        """

    def stop_db_cluster(self, DBClusterIdentifier: str) -> ClientStopDbClusterResponseTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.stop_db_cluster)
        """

    def stop_db_instance(
        self, DBInstanceIdentifier: str, DBSnapshotIdentifier: str = None
    ) -> ClientStopDbInstanceResponseTypeDef:
        """
        [Client.stop_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Client.stop_db_instance)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> "paginator_scope.DescribeCertificatesPaginator":
        """
        [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_custom_availability_zones"]
    ) -> "paginator_scope.DescribeCustomAvailabilityZonesPaginator":
        """
        [Paginator.DescribeCustomAvailabilityZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_backtracks"]
    ) -> "paginator_scope.DescribeDBClusterBacktracksPaginator":
        """
        [Paginator.DescribeDBClusterBacktracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> "paginator_scope.DescribeDBClusterEndpointsPaginator":
        """
        [Paginator.DescribeDBClusterEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> "paginator_scope.DescribeDBClusterParameterGroupsPaginator":
        """
        [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> "paginator_scope.DescribeDBClusterParametersPaginator":
        """
        [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> "paginator_scope.DescribeDBClusterSnapshotsPaginator":
        """
        [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> "paginator_scope.DescribeDBClustersPaginator":
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> "paginator_scope.DescribeDBEngineVersionsPaginator":
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instance_automated_backups"]
    ) -> "paginator_scope.DescribeDBInstanceAutomatedBackupsPaginator":
        """
        [Paginator.DescribeDBInstanceAutomatedBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> "paginator_scope.DescribeDBInstancesPaginator":
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_log_files"]
    ) -> "paginator_scope.DescribeDBLogFilesPaginator":
        """
        [Paginator.DescribeDBLogFiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> "paginator_scope.DescribeDBParameterGroupsPaginator":
        """
        [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> "paginator_scope.DescribeDBParametersPaginator":
        """
        [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxies"]
    ) -> "paginator_scope.DescribeDBProxiesPaginator":
        """
        [Paginator.DescribeDBProxies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBProxies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_target_groups"]
    ) -> "paginator_scope.DescribeDBProxyTargetGroupsPaginator":
        """
        [Paginator.DescribeDBProxyTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_targets"]
    ) -> "paginator_scope.DescribeDBProxyTargetsPaginator":
        """
        [Paginator.DescribeDBProxyTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_security_groups"]
    ) -> "paginator_scope.DescribeDBSecurityGroupsPaginator":
        """
        [Paginator.DescribeDBSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshots"]
    ) -> "paginator_scope.DescribeDBSnapshotsPaginator":
        """
        [Paginator.DescribeDBSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> "paginator_scope.DescribeDBSubnetGroupsPaginator":
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_cluster_parameters"]
    ) -> "paginator_scope.DescribeEngineDefaultClusterParametersPaginator":
        """
        [Paginator.DescribeEngineDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> "paginator_scope.DescribeEngineDefaultParametersPaginator":
        """
        [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> "paginator_scope.DescribeEventSubscriptionsPaginator":
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> "paginator_scope.DescribeExportTasksPaginator":
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeExportTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_clusters"]
    ) -> "paginator_scope.DescribeGlobalClustersPaginator":
        """
        [Paginator.DescribeGlobalClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_installation_media"]
    ) -> "paginator_scope.DescribeInstallationMediaPaginator":
        """
        [Paginator.DescribeInstallationMedia documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_group_options"]
    ) -> "paginator_scope.DescribeOptionGroupOptionsPaginator":
        """
        [Paginator.DescribeOptionGroupOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_groups"]
    ) -> "paginator_scope.DescribeOptionGroupsPaginator":
        """
        [Paginator.DescribeOptionGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> "paginator_scope.DescribeOrderableDBInstanceOptionsPaginator":
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> "paginator_scope.DescribePendingMaintenanceActionsPaginator":
        """
        [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances"]
    ) -> "paginator_scope.DescribeReservedDBInstancesPaginator":
        """
        [Paginator.DescribeReservedDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances_offerings"]
    ) -> "paginator_scope.DescribeReservedDBInstancesOfferingsPaginator":
        """
        [Paginator.DescribeReservedDBInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_regions"]
    ) -> "paginator_scope.DescribeSourceRegionsPaginator":
        """
        [Paginator.DescribeSourceRegions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["download_db_log_file_portion"]
    ) -> "paginator_scope.DownloadDBLogFilePortionPaginator":
        """
        [Paginator.DownloadDBLogFilePortion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_available"]
    ) -> "waiter_scope.DBClusterSnapshotAvailableWaiter":
        """
        [Waiter.DBClusterSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_deleted"]
    ) -> "waiter_scope.DBClusterSnapshotDeletedWaiter":
        """
        [Waiter.DBClusterSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> "waiter_scope.DBInstanceAvailableWaiter":
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBInstanceAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> "waiter_scope.DBInstanceDeletedWaiter":
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBInstanceDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_available"]
    ) -> "waiter_scope.DBSnapshotAvailableWaiter":
        """
        [Waiter.DBSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBSnapshotAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_completed"]
    ) -> "waiter_scope.DBSnapshotCompletedWaiter":
        """
        [Waiter.DBSnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBSnapshotCompleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_deleted"]
    ) -> "waiter_scope.DBSnapshotDeletedWaiter":
        """
        [Waiter.DBSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/rds.html#RDS.Waiter.DBSnapshotDeleted)
        """


class Exceptions:
    AuthorizationAlreadyExistsFault: Boto3ClientError
    AuthorizationNotFoundFault: Boto3ClientError
    AuthorizationQuotaExceededFault: Boto3ClientError
    BackupPolicyNotFoundFault: Boto3ClientError
    CertificateNotFoundFault: Boto3ClientError
    ClientError: Boto3ClientError
    CustomAvailabilityZoneAlreadyExistsFault: Boto3ClientError
    CustomAvailabilityZoneNotFoundFault: Boto3ClientError
    CustomAvailabilityZoneQuotaExceededFault: Boto3ClientError
    DBClusterAlreadyExistsFault: Boto3ClientError
    DBClusterBacktrackNotFoundFault: Boto3ClientError
    DBClusterEndpointAlreadyExistsFault: Boto3ClientError
    DBClusterEndpointNotFoundFault: Boto3ClientError
    DBClusterEndpointQuotaExceededFault: Boto3ClientError
    DBClusterNotFoundFault: Boto3ClientError
    DBClusterParameterGroupNotFoundFault: Boto3ClientError
    DBClusterQuotaExceededFault: Boto3ClientError
    DBClusterRoleAlreadyExistsFault: Boto3ClientError
    DBClusterRoleNotFoundFault: Boto3ClientError
    DBClusterRoleQuotaExceededFault: Boto3ClientError
    DBClusterSnapshotAlreadyExistsFault: Boto3ClientError
    DBClusterSnapshotNotFoundFault: Boto3ClientError
    DBInstanceAlreadyExistsFault: Boto3ClientError
    DBInstanceAutomatedBackupNotFoundFault: Boto3ClientError
    DBInstanceAutomatedBackupQuotaExceededFault: Boto3ClientError
    DBInstanceNotFoundFault: Boto3ClientError
    DBInstanceRoleAlreadyExistsFault: Boto3ClientError
    DBInstanceRoleNotFoundFault: Boto3ClientError
    DBInstanceRoleQuotaExceededFault: Boto3ClientError
    DBLogFileNotFoundFault: Boto3ClientError
    DBParameterGroupAlreadyExistsFault: Boto3ClientError
    DBParameterGroupNotFoundFault: Boto3ClientError
    DBParameterGroupQuotaExceededFault: Boto3ClientError
    DBProxyAlreadyExistsFault: Boto3ClientError
    DBProxyNotFoundFault: Boto3ClientError
    DBProxyQuotaExceededFault: Boto3ClientError
    DBProxyTargetAlreadyRegisteredFault: Boto3ClientError
    DBProxyTargetGroupNotFoundFault: Boto3ClientError
    DBProxyTargetNotFoundFault: Boto3ClientError
    DBSecurityGroupAlreadyExistsFault: Boto3ClientError
    DBSecurityGroupNotFoundFault: Boto3ClientError
    DBSecurityGroupNotSupportedFault: Boto3ClientError
    DBSecurityGroupQuotaExceededFault: Boto3ClientError
    DBSnapshotAlreadyExistsFault: Boto3ClientError
    DBSnapshotNotFoundFault: Boto3ClientError
    DBSubnetGroupAlreadyExistsFault: Boto3ClientError
    DBSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    DBSubnetGroupNotAllowedFault: Boto3ClientError
    DBSubnetGroupNotFoundFault: Boto3ClientError
    DBSubnetGroupQuotaExceededFault: Boto3ClientError
    DBSubnetQuotaExceededFault: Boto3ClientError
    DBUpgradeDependencyFailureFault: Boto3ClientError
    DomainNotFoundFault: Boto3ClientError
    EventSubscriptionQuotaExceededFault: Boto3ClientError
    ExportTaskAlreadyExistsFault: Boto3ClientError
    ExportTaskNotFoundFault: Boto3ClientError
    GlobalClusterAlreadyExistsFault: Boto3ClientError
    GlobalClusterNotFoundFault: Boto3ClientError
    GlobalClusterQuotaExceededFault: Boto3ClientError
    IamRoleMissingPermissionsFault: Boto3ClientError
    IamRoleNotFoundFault: Boto3ClientError
    InstallationMediaAlreadyExistsFault: Boto3ClientError
    InstallationMediaNotFoundFault: Boto3ClientError
    InstanceQuotaExceededFault: Boto3ClientError
    InsufficientDBClusterCapacityFault: Boto3ClientError
    InsufficientDBInstanceCapacityFault: Boto3ClientError
    InsufficientStorageClusterCapacityFault: Boto3ClientError
    InvalidDBClusterCapacityFault: Boto3ClientError
    InvalidDBClusterEndpointStateFault: Boto3ClientError
    InvalidDBClusterSnapshotStateFault: Boto3ClientError
    InvalidDBClusterStateFault: Boto3ClientError
    InvalidDBInstanceAutomatedBackupStateFault: Boto3ClientError
    InvalidDBInstanceStateFault: Boto3ClientError
    InvalidDBParameterGroupStateFault: Boto3ClientError
    InvalidDBProxyStateFault: Boto3ClientError
    InvalidDBSecurityGroupStateFault: Boto3ClientError
    InvalidDBSnapshotStateFault: Boto3ClientError
    InvalidDBSubnetGroupFault: Boto3ClientError
    InvalidDBSubnetGroupStateFault: Boto3ClientError
    InvalidDBSubnetStateFault: Boto3ClientError
    InvalidEventSubscriptionStateFault: Boto3ClientError
    InvalidExportOnlyFault: Boto3ClientError
    InvalidExportSourceStateFault: Boto3ClientError
    InvalidExportTaskStateFault: Boto3ClientError
    InvalidGlobalClusterStateFault: Boto3ClientError
    InvalidOptionGroupStateFault: Boto3ClientError
    InvalidRestoreFault: Boto3ClientError
    InvalidS3BucketFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    OptionGroupAlreadyExistsFault: Boto3ClientError
    OptionGroupNotFoundFault: Boto3ClientError
    OptionGroupQuotaExceededFault: Boto3ClientError
    PointInTimeRestoreNotEnabledFault: Boto3ClientError
    ProvisionedIopsNotAvailableInAZFault: Boto3ClientError
    ReservedDBInstanceAlreadyExistsFault: Boto3ClientError
    ReservedDBInstanceNotFoundFault: Boto3ClientError
    ReservedDBInstanceQuotaExceededFault: Boto3ClientError
    ReservedDBInstancesOfferingNotFoundFault: Boto3ClientError
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
