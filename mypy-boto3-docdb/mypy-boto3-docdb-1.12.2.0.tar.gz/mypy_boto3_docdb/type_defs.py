"""
Main interface for docdb service type definitions.

Usage::

    from mypy_boto3.docdb.type_defs import ClientAddTagsToResourceTagsTypeDef

    data: ClientAddTagsToResourceTagsTypeDef = {...}
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
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    "ClientCopyDbClusterParameterGroupTagsTypeDef",
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    "ClientCopyDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    "ClientDescribeDbClusterParametersFiltersTypeDef",
    "ClientDescribeDbClusterParametersResponseParametersTypeDef",
    "ClientDescribeDbClusterParametersResponseTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    "ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseTypeDef",
    "ClientDescribeDbClustersFiltersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    "ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    "ClientDescribeDbClustersResponseTypeDef",
    "ClientDescribeDbEngineVersionsFiltersTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbSubnetGroupsFiltersTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    "ClientFailoverDbClusterResponseTypeDef",
    "ClientListTagsForResourceFiltersTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStartDbClusterResponseDBClusterTypeDef",
    "ClientStartDbClusterResponseTypeDef",
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStopDbClusterResponseDBClusterTypeDef",
    "ClientStopDbClusterResponseTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterRoleTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "DBClusterTypeDef",
    "DBClusterMessageTypeDef",
    "UpgradeTargetTypeDef",
    "DBEngineVersionTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "AvailabilityZoneTypeDef",
    "SubnetTypeDef",
    "DBSubnetGroupTypeDef",
    "EndpointTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingModifiedValuesTypeDef",
    "DBInstanceTypeDef",
    "DBInstanceMessageTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FilterTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)

ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)

ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

ClientCopyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)

ClientCopyDbClusterParameterGroupTagsTypeDef = TypedDict(
    "ClientCopyDbClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)

ClientCopyDbClusterSnapshotResponseTypeDef = TypedDict(
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)

ClientCopyDbClusterSnapshotTagsTypeDef = TypedDict(
    "ClientCopyDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

ClientCreateDbClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)

ClientCreateDbClusterParameterGroupTagsTypeDef = TypedDict(
    "ClientCreateDbClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientCreateDbClusterResponseTypeDef = TypedDict(
    "ClientCreateDbClusterResponseTypeDef",
    {"DBCluster": ClientCreateDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)

ClientCreateDbClusterSnapshotResponseTypeDef = TypedDict(
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)

ClientCreateDbClusterSnapshotTagsTypeDef = TypedDict(
    "ClientCreateDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbClusterTagsTypeDef = TypedDict(
    "ClientCreateDbClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

ClientCreateDbInstanceResponseTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseTypeDef",
    {"DBInstance": ClientCreateDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientCreateDbInstanceTagsTypeDef = TypedDict(
    "ClientCreateDbInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientCreateDbSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)

ClientCreateDbSubnetGroupTagsTypeDef = TypedDict(
    "ClientCreateDbSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientDeleteDbClusterResponseTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseTypeDef",
    {"DBCluster": ClientDeleteDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)

ClientDeleteDbClusterSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

ClientDeleteDbInstanceResponseTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseTypeDef",
    {"DBInstance": ClientDeleteDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

_RequiredClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeCertificatesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeCertificatesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeCertificatesFiltersTypeDef(
    _RequiredClientDescribeCertificatesFiltersTypeDef,
    _OptionalClientDescribeCertificatesFiltersTypeDef,
):
    pass


ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
    },
    total=False,
)

ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseTypeDef",
    {"Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef], "Marker": str},
    total=False,
)

_RequiredClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClusterParameterGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeDbClusterParameterGroupsFiltersTypeDef(
    _RequiredClientDescribeDbClusterParameterGroupsFiltersTypeDef,
    _OptionalClientDescribeDbClusterParameterGroupsFiltersTypeDef,
):
    pass


ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef = TypedDict(
    "ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

ClientDescribeDbClusterParameterGroupsResponseTypeDef = TypedDict(
    "ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List[
            ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClusterParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClusterParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbClusterParametersFiltersTypeDef(
    _RequiredClientDescribeDbClusterParametersFiltersTypeDef,
    _OptionalClientDescribeDbClusterParametersFiltersTypeDef,
):
    pass


ClientDescribeDbClusterParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeDbClusterParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)

ClientDescribeDbClusterParametersResponseTypeDef = TypedDict(
    "ClientDescribeDbClusterParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeDbClusterParametersResponseParametersTypeDef], "Marker": str},
    total=False,
)

ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)

ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbClusterSnapshotAttributesResponseTypeDef = TypedDict(
    "ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)

_RequiredClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClusterSnapshotsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClusterSnapshotsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbClusterSnapshotsFiltersTypeDef(
    _RequiredClientDescribeDbClusterSnapshotsFiltersTypeDef,
    _OptionalClientDescribeDbClusterSnapshotsFiltersTypeDef,
):
    pass


ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef = TypedDict(
    "ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)

ClientDescribeDbClusterSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeDbClusterSnapshotsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List[
            ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbClustersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbClustersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbClustersFiltersTypeDef(
    _RequiredClientDescribeDbClustersFiltersTypeDef, _OptionalClientDescribeDbClustersFiltersTypeDef
):
    pass


ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeDbClustersResponseDBClustersTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[
            ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientDescribeDbClustersResponseTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseTypeDef",
    {"Marker": str, "DBClusters": List[ClientDescribeDbClustersResponseDBClustersTypeDef]},
    total=False,
)

_RequiredClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbEngineVersionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbEngineVersionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbEngineVersionsFiltersTypeDef(
    _RequiredClientDescribeDbEngineVersionsFiltersTypeDef,
    _OptionalClientDescribeDbEngineVersionsFiltersTypeDef,
):
    pass


ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)

ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)

ClientDescribeDbEngineVersionsResponseTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List[ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef],
    },
    total=False,
)

_RequiredClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbInstancesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbInstancesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbInstancesFiltersTypeDef(
    _RequiredClientDescribeDbInstancesFiltersTypeDef,
    _OptionalClientDescribeDbInstancesFiltersTypeDef,
):
    pass


ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

ClientDescribeDbInstancesResponseTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseTypeDef",
    {"Marker": str, "DBInstances": List[ClientDescribeDbInstancesResponseDBInstancesTypeDef]},
    total=False,
)

_RequiredClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbSubnetGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbSubnetGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbSubnetGroupsFiltersTypeDef(
    _RequiredClientDescribeDbSubnetGroupsFiltersTypeDef,
    _OptionalClientDescribeDbSubnetGroupsFiltersTypeDef,
):
    pass


ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientDescribeDbSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List[ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef],
    },
    total=False,
)

_RequiredClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEngineDefaultClusterParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersFiltersTypeDef(
    _RequiredClientDescribeEngineDefaultClusterParametersFiltersTypeDef,
    _OptionalClientDescribeEngineDefaultClusterParametersFiltersTypeDef,
):
    pass


ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)

ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef = TypedDict(
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeEngineDefaultClusterParametersResponseTypeDef = TypedDict(
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    {"EngineDefaults": ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef},
    total=False,
)

_RequiredClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventCategoriesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventCategoriesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _RequiredClientDescribeEventCategoriesFiltersTypeDef,
    _OptionalClientDescribeEventCategoriesFiltersTypeDef,
):
    pass


ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)

ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoriesMapList": List[
            ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
        ]
    },
    total=False,
)

_RequiredClientDescribeEventsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventsFiltersTypeDef(
    _RequiredClientDescribeEventsFiltersTypeDef, _OptionalClientDescribeEventsFiltersTypeDef
):
    pass


ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

_RequiredClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeOrderableDbInstanceOptionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef(
    _RequiredClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
    _OptionalClientDescribeOrderableDbInstanceOptionsFiltersTypeDef,
):
    pass


ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "Vpc": bool,
    },
    total=False,
)

ClientDescribeOrderableDbInstanceOptionsResponseTypeDef = TypedDict(
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef,
    _OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef,
):
    pass


ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)

ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientFailoverDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientFailoverDbClusterResponseTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseTypeDef",
    {"DBCluster": ClientFailoverDbClusterResponseDBClusterTypeDef},
    total=False,
)

_RequiredClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_RequiredClientListTagsForResourceFiltersTypeDef", {"Name": str}
)
_OptionalClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_OptionalClientListTagsForResourceFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientListTagsForResourceFiltersTypeDef(
    _RequiredClientListTagsForResourceFiltersTypeDef,
    _OptionalClientListTagsForResourceFiltersTypeDef,
):
    pass


ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)

ClientModifyDbClusterParameterGroupParametersTypeDef = TypedDict(
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)

ClientModifyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)

ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientModifyDbClusterResponseTypeDef = TypedDict(
    "ClientModifyDbClusterResponseTypeDef",
    {"DBCluster": ClientModifyDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)

ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)

ClientModifyDbClusterSnapshotAttributeResponseTypeDef = TypedDict(
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

ClientModifyDbInstanceResponseTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseTypeDef",
    {"DBInstance": ClientModifyDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientModifyDbSubnetGroupResponseTypeDef = TypedDict(
    "ClientModifyDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

ClientRebootDbInstanceResponseTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseTypeDef",
    {"DBInstance": ClientRebootDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientResetDbClusterParameterGroupParametersTypeDef = TypedDict(
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)

ClientResetDbClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)

ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientRestoreDbClusterFromSnapshotResponseTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef},
    total=False,
)

ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientRestoreDbClusterToPointInTimeResponseTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef},
    total=False,
)

ClientRestoreDbClusterToPointInTimeTagsTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientStartDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientStartDbClusterResponseTypeDef = TypedDict(
    "ClientStartDbClusterResponseTypeDef",
    {"DBCluster": ClientStartDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientStopDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientStopDbClusterResponseTypeDef = TypedDict(
    "ClientStopDbClusterResponseTypeDef",
    {"DBCluster": ClientStopDbClusterResponseDBClusterTypeDef},
    total=False,
)

DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef", {"RoleArn": str, "Status": str}, total=False
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef", {"VpcSecurityGroupId": str, "Status": str}, total=False
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[DBClusterMemberTypeDef],
        "VpcSecurityGroups": List[VpcSecurityGroupMembershipTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[DBClusterRoleTypeDef],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef", {"Marker": str, "DBClusters": List[DBClusterTypeDef]}, total=False
)

UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)

DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List[UpgradeTargetTypeDef],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {"Marker": str, "DBEngineVersions": List[DBEngineVersionTypeDef]},
    total=False,
)

DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

AvailabilityZoneTypeDef = TypedDict("AvailabilityZoneTypeDef", {"Name": str}, total=False)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": AvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[SubnetTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef", {"Address": str, "Port": int, "HostedZoneId": str}, total=False
)

PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": PendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)

DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": EndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[VpcSecurityGroupMembershipTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": DBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": PendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[DBInstanceStatusInfoTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef", {"Marker": str, "DBInstances": List[DBInstanceTypeDef]}, total=False
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {"Marker": str, "DBSubnetGroups": List[DBSubnetGroupTypeDef]},
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef", {"Marker": str, "Events": List[EventTypeDef]}, total=False
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]})

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "Vpc": bool,
    },
    total=False,
)

OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {"OrderableDBInstanceOptions": List[OrderableDBInstanceOptionTypeDef], "Marker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
