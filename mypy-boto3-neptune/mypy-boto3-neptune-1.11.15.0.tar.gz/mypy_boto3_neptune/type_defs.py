"""
Main interface for neptune service type definitions.

Usage::

    from mypy_boto3.neptune.type_defs import ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef

    data: ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef = {...}
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
    "ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    "ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
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
    "ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCopyDbParameterGroupResponseTypeDef",
    "ClientCopyDbParameterGroupTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCreateDbParameterGroupResponseTypeDef",
    "ClientCreateDbParameterGroupTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
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
    "ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    "ClientDescribeDbClustersResponseTypeDef",
    "ClientDescribeDbEngineVersionsFiltersTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbParameterGroupsFiltersTypeDef",
    "ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    "ClientDescribeDbParameterGroupsResponseTypeDef",
    "ClientDescribeDbParametersFiltersTypeDef",
    "ClientDescribeDbParametersResponseParametersTypeDef",
    "ClientDescribeDbParametersResponseTypeDef",
    "ClientDescribeDbSubnetGroupsFiltersTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEngineDefaultParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
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
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
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
    "ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbParameterGroupParametersTypeDef",
    "ClientModifyDbParameterGroupResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientResetDbParameterGroupParametersTypeDef",
    "ClientResetDbParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterRoleTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "DBClusterTypeDef",
    "DBClusterMessageTypeDef",
    "ParameterTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "CharacterSetTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "DBEngineVersionTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "AvailabilityZoneTypeDef",
    "SubnetTypeDef",
    "DBSubnetGroupTypeDef",
    "DomainMembershipTypeDef",
    "EndpointTypeDef",
    "OptionGroupMembershipTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingModifiedValuesTypeDef",
    "DBInstanceTypeDef",
    "DBInstanceMessageTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "EngineDefaultsTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FilterTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

ClientAddSourceIdentifierToSubscriptionResponseTypeDef = TypedDict(
    "ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
    {"EventSubscription": ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
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
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
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

ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef = TypedDict(
    "ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

ClientCopyDbParameterGroupResponseTypeDef = TypedDict(
    "ClientCopyDbParameterGroupResponseTypeDef",
    {"DBParameterGroup": ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef},
    total=False,
)

ClientCopyDbParameterGroupTagsTypeDef = TypedDict(
    "ClientCopyDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
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

ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
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

ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
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

ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
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

ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef = TypedDict(
    "ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

ClientCreateDbParameterGroupResponseTypeDef = TypedDict(
    "ClientCreateDbParameterGroupResponseTypeDef",
    {"DBParameterGroup": ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef},
    total=False,
)

ClientCreateDbParameterGroupTagsTypeDef = TypedDict(
    "ClientCreateDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
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

ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
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

ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

ClientDeleteDbClusterSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
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

ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientDeleteDbInstanceResponseTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseTypeDef",
    {"DBInstance": ClientDeleteDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "ClientDeleteEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef},
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
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
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

ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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


ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)

ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)

ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef",
    {"TimezoneName": str},
    total=False,
)

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
        "DefaultCharacterSet": ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef,
        "SupportedCharacterSets": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef
        ],
        "ValidUpgradeTarget": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "SupportedTimezones": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
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


ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

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

ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientDescribeDbInstancesResponseTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseTypeDef",
    {"Marker": str, "DBInstances": List[ClientDescribeDbInstancesResponseDBInstancesTypeDef]},
    total=False,
)

_RequiredClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbParameterGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbParameterGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbParameterGroupsFiltersTypeDef(
    _RequiredClientDescribeDbParameterGroupsFiltersTypeDef,
    _OptionalClientDescribeDbParameterGroupsFiltersTypeDef,
):
    pass


ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef = TypedDict(
    "ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

ClientDescribeDbParameterGroupsResponseTypeDef = TypedDict(
    "ClientDescribeDbParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List[ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef],
    },
    total=False,
)

_RequiredClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeDbParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeDbParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeDbParametersFiltersTypeDef(
    _RequiredClientDescribeDbParametersFiltersTypeDef,
    _OptionalClientDescribeDbParametersFiltersTypeDef,
):
    pass


ClientDescribeDbParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeDbParametersResponseParametersTypeDef",
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

ClientDescribeDbParametersResponseTypeDef = TypedDict(
    "ClientDescribeDbParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeDbParametersResponseParametersTypeDef], "Marker": str},
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

_RequiredClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEngineDefaultParametersFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEngineDefaultParametersFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeEngineDefaultParametersFiltersTypeDef(
    _RequiredClientDescribeEngineDefaultParametersFiltersTypeDef,
    _OptionalClientDescribeEngineDefaultParametersFiltersTypeDef,
):
    pass


ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
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

ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeEngineDefaultParametersResponseTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    {"EngineDefaults": ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef},
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

_RequiredClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventSubscriptionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventSubscriptionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _RequiredClientDescribeEventSubscriptionsFiltersTypeDef,
    _OptionalClientDescribeEventSubscriptionsFiltersTypeDef,
):
    pass


ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
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
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
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

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    {"From": float, "To": float},
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    {"From": int, "To": int, "Step": int},
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    {"From": int, "To": int, "Step": int},
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    {
        "StorageType": str,
        "StorageSize": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef
        ],
        "ProvisionedIops": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef
        ],
        "IopsToStorageRatio": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef
        ],
    },
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
        ]
    },
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    {
        "ValidDBInstanceModificationsMessage": ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef
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

ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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

ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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

ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
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

ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientModifyDbInstanceResponseTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseTypeDef",
    {"DBInstance": ClientModifyDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientModifyDbParameterGroupParametersTypeDef = TypedDict(
    "ClientModifyDbParameterGroupParametersTypeDef",
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

ClientModifyDbParameterGroupResponseTypeDef = TypedDict(
    "ClientModifyDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
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

ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    {"DBCluster": ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
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

ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

ClientRebootDbInstanceResponseTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseTypeDef",
    {"DBInstance": ClientRebootDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef = TypedDict(
    "ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef
    },
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

ClientResetDbParameterGroupParametersTypeDef = TypedDict(
    "ClientResetDbParameterGroupParametersTypeDef",
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

ClientResetDbParameterGroupResponseTypeDef = TypedDict(
    "ClientResetDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
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

ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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

ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
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

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
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
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List[DBClusterOptionGroupStatusTypeDef],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[DBClusterMemberTypeDef],
        "VpcSecurityGroups": List[VpcSecurityGroupMembershipTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[DBClusterRoleTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef", {"Marker": str, "DBClusters": List[DBClusterTypeDef]}, total=False
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
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

DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {"Parameters": List[ParameterTypeDef], "Marker": str},
    total=False,
)

DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {"Marker": str, "DBClusterParameterGroups": List[DBClusterParameterGroupTypeDef]},
    total=False,
)

DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {"Marker": str, "DBClusterSnapshots": List[DBClusterSnapshotTypeDef]},
    total=False,
)

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef", {"CharacterSetName": str, "CharacterSetDescription": str}, total=False
)

TimezoneTypeDef = TypedDict("TimezoneTypeDef", {"TimezoneName": str}, total=False)

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
        "DefaultCharacterSet": CharacterSetTypeDef,
        "SupportedCharacterSets": List[CharacterSetTypeDef],
        "ValidUpgradeTarget": List[UpgradeTargetTypeDef],
        "SupportedTimezones": List[TimezoneTypeDef],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
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

DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef", {"DBSecurityGroupName": str, "Status": str}, total=False
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

DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef", {"Address": str, "Port": int, "HostedZoneId": str}, total=False
)

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef", {"OptionGroupName": str, "Status": str}, total=False
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": EndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[DBSecurityGroupMembershipTypeDef],
        "VpcSecurityGroups": List[VpcSecurityGroupMembershipTypeDef],
        "DBParameterGroups": List[DBParameterGroupStatusTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": DBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": PendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[OptionGroupMembershipTypeDef],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[DBInstanceStatusInfoTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[DomainMembershipTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef", {"Marker": str, "DBInstances": List[DBInstanceTypeDef]}, total=False
)

DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {"Parameters": List[ParameterTypeDef], "Marker": str},
    total=False,
)

DBParameterGroupTypeDef = TypedDict(
    "DBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {"Marker": str, "DBParameterGroups": List[DBParameterGroupTypeDef]},
    total=False,
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {"Marker": str, "DBSubnetGroups": List[DBSubnetGroupTypeDef]},
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {"DBParameterGroupFamily": str, "Marker": str, "Parameters": List[ParameterTypeDef]},
    total=False,
)

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {"EngineDefaults": EngineDefaultsTypeDef},
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {"Marker": str, "EventSubscriptionsList": List[EventSubscriptionTypeDef]},
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
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
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

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
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

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[PendingMaintenanceActionTypeDef],
    },
    total=False,
)

PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {"PendingMaintenanceActions": List[ResourcePendingMaintenanceActionsTypeDef], "Marker": str},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
