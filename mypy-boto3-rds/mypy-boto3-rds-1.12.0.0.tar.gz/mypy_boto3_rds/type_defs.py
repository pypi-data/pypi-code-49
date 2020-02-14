"""
Main interface for rds service type definitions.

Usage::

    from mypy_boto3.rds.type_defs import CertificateTypeDef

    data: CertificateTypeDef = {...}
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
    "CertificateTypeDef",
    "CertificateMessageTypeDef",
    "ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    "ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    "ClientAuthorizeDbSecurityGroupIngressResponseTypeDef",
    "ClientBacktrackDbClusterResponseTypeDef",
    "ClientCancelExportTaskResponseTypeDef",
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    "ClientCopyDbClusterParameterGroupTagsTypeDef",
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    "ClientCopyDbClusterSnapshotTagsTypeDef",
    "ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCopyDbParameterGroupResponseTypeDef",
    "ClientCopyDbParameterGroupTagsTypeDef",
    "ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientCopyDbSnapshotResponseDBSnapshotTypeDef",
    "ClientCopyDbSnapshotResponseTypeDef",
    "ClientCopyDbSnapshotTagsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef",
    "ClientCopyOptionGroupResponseOptionGroupTypeDef",
    "ClientCopyOptionGroupResponseTypeDef",
    "ClientCopyOptionGroupTagsTypeDef",
    "ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    "ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    "ClientCreateCustomAvailabilityZoneResponseTypeDef",
    "ClientCreateDbClusterEndpointResponseTypeDef",
    "ClientCreateDbClusterEndpointTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterScalingConfigurationTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceReadReplicaResponseTypeDef",
    "ClientCreateDbInstanceReadReplicaTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCreateDbParameterGroupResponseTypeDef",
    "ClientCreateDbParameterGroupTagsTypeDef",
    "ClientCreateDbProxyAuthTypeDef",
    "ClientCreateDbProxyResponseDBProxyAuthTypeDef",
    "ClientCreateDbProxyResponseDBProxyTypeDef",
    "ClientCreateDbProxyResponseTypeDef",
    "ClientCreateDbProxyTagsTypeDef",
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef",
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef",
    "ClientCreateDbSecurityGroupResponseTypeDef",
    "ClientCreateDbSecurityGroupTagsTypeDef",
    "ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientCreateDbSnapshotResponseDBSnapshotTypeDef",
    "ClientCreateDbSnapshotResponseTypeDef",
    "ClientCreateDbSnapshotTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientCreateGlobalClusterResponseGlobalClusterTypeDef",
    "ClientCreateGlobalClusterResponseTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef",
    "ClientCreateOptionGroupResponseOptionGroupTypeDef",
    "ClientCreateOptionGroupResponseTypeDef",
    "ClientCreateOptionGroupTagsTypeDef",
    "ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    "ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    "ClientDeleteCustomAvailabilityZoneResponseTypeDef",
    "ClientDeleteDbClusterEndpointResponseTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef",
    "ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef",
    "ClientDeleteDbInstanceAutomatedBackupResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDeleteDbProxyResponseDBProxyAuthTypeDef",
    "ClientDeleteDbProxyResponseDBProxyTypeDef",
    "ClientDeleteDbProxyResponseTypeDef",
    "ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientDeleteDbSnapshotResponseDBSnapshotTypeDef",
    "ClientDeleteDbSnapshotResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
    "ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientDeleteGlobalClusterResponseGlobalClusterTypeDef",
    "ClientDeleteGlobalClusterResponseTypeDef",
    "ClientDeleteInstallationMediaResponseFailureCauseTypeDef",
    "ClientDeleteInstallationMediaResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeCustomAvailabilityZonesFiltersTypeDef",
    "ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef",
    "ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef",
    "ClientDescribeCustomAvailabilityZonesResponseTypeDef",
    "ClientDescribeDbClusterBacktracksFiltersTypeDef",
    "ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef",
    "ClientDescribeDbClusterBacktracksResponseTypeDef",
    "ClientDescribeDbClusterEndpointsFiltersTypeDef",
    "ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef",
    "ClientDescribeDbClusterEndpointsResponseTypeDef",
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
    "ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef",
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
    "ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef",
    "ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef",
    "ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef",
    "ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbLogFilesFiltersTypeDef",
    "ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef",
    "ClientDescribeDbLogFilesResponseTypeDef",
    "ClientDescribeDbParameterGroupsFiltersTypeDef",
    "ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    "ClientDescribeDbParameterGroupsResponseTypeDef",
    "ClientDescribeDbParametersFiltersTypeDef",
    "ClientDescribeDbParametersResponseParametersTypeDef",
    "ClientDescribeDbParametersResponseTypeDef",
    "ClientDescribeDbProxiesFiltersTypeDef",
    "ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef",
    "ClientDescribeDbProxiesResponseDBProxiesTypeDef",
    "ClientDescribeDbProxiesResponseTypeDef",
    "ClientDescribeDbProxyTargetGroupsFiltersTypeDef",
    "ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef",
    "ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef",
    "ClientDescribeDbProxyTargetGroupsResponseTypeDef",
    "ClientDescribeDbProxyTargetsFiltersTypeDef",
    "ClientDescribeDbProxyTargetsResponseTargetsTypeDef",
    "ClientDescribeDbProxyTargetsResponseTypeDef",
    "ClientDescribeDbSecurityGroupsFiltersTypeDef",
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef",
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef",
    "ClientDescribeDbSecurityGroupsResponseTypeDef",
    "ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    "ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef",
    "ClientDescribeDbSnapshotAttributesResponseTypeDef",
    "ClientDescribeDbSnapshotsFiltersTypeDef",
    "ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef",
    "ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef",
    "ClientDescribeDbSnapshotsResponseTypeDef",
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
    "ClientDescribeExportTasksFiltersTypeDef",
    "ClientDescribeExportTasksResponseExportTasksTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeGlobalClustersFiltersTypeDef",
    "ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef",
    "ClientDescribeGlobalClustersResponseGlobalClustersTypeDef",
    "ClientDescribeGlobalClustersResponseTypeDef",
    "ClientDescribeInstallationMediaFiltersTypeDef",
    "ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef",
    "ClientDescribeInstallationMediaResponseInstallationMediaTypeDef",
    "ClientDescribeInstallationMediaResponseTypeDef",
    "ClientDescribeOptionGroupOptionsFiltersTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef",
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef",
    "ClientDescribeOptionGroupOptionsResponseTypeDef",
    "ClientDescribeOptionGroupsFiltersTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef",
    "ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef",
    "ClientDescribeOptionGroupsResponseTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientDescribeReservedDbInstancesFiltersTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef",
    "ClientDescribeReservedDbInstancesOfferingsResponseTypeDef",
    "ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef",
    "ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef",
    "ClientDescribeReservedDbInstancesResponseTypeDef",
    "ClientDescribeSourceRegionsFiltersTypeDef",
    "ClientDescribeSourceRegionsResponseSourceRegionsTypeDef",
    "ClientDescribeSourceRegionsResponseTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    "ClientDownloadDbLogFilePortionResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    "ClientFailoverDbClusterResponseTypeDef",
    "ClientImportInstallationMediaResponseFailureCauseTypeDef",
    "ClientImportInstallationMediaResponseTypeDef",
    "ClientListTagsForResourceFiltersTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyCertificatesResponseCertificateTypeDef",
    "ClientModifyCertificatesResponseTypeDef",
    "ClientModifyCurrentDbClusterCapacityResponseTypeDef",
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbClusterEndpointResponseTypeDef",
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterScalingConfigurationTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbInstanceProcessorFeaturesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbParameterGroupParametersTypeDef",
    "ClientModifyDbParameterGroupResponseTypeDef",
    "ClientModifyDbProxyAuthTypeDef",
    "ClientModifyDbProxyResponseDBProxyAuthTypeDef",
    "ClientModifyDbProxyResponseDBProxyTypeDef",
    "ClientModifyDbProxyResponseTypeDef",
    "ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef",
    "ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef",
    "ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef",
    "ClientModifyDbProxyTargetGroupResponseTypeDef",
    "ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    "ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef",
    "ClientModifyDbSnapshotAttributeResponseTypeDef",
    "ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    "ClientModifyDbSnapshotResponseDBSnapshotTypeDef",
    "ClientModifyDbSnapshotResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientModifyGlobalClusterResponseGlobalClusterTypeDef",
    "ClientModifyGlobalClusterResponseTypeDef",
    "ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef",
    "ClientModifyOptionGroupOptionsToIncludeTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef",
    "ClientModifyOptionGroupResponseOptionGroupTypeDef",
    "ClientModifyOptionGroupResponseTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaResponseDBInstanceTypeDef",
    "ClientPromoteReadReplicaResponseTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingResponseTypeDef",
    "ClientPurchaseReservedDbInstancesOfferingTagsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef",
    "ClientRegisterDbProxyTargetsResponseTypeDef",
    "ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    "ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef",
    "ClientRemoveFromGlobalClusterResponseTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientResetDbParameterGroupParametersTypeDef",
    "ClientResetDbParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromS3ResponseTypeDef",
    "ClientRestoreDbClusterFromS3TagsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef",
    "ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef",
    "ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef",
    "ClientRestoreDbInstanceFromS3ResponseTypeDef",
    "ClientRestoreDbInstanceFromS3TagsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef",
    "ClientRestoreDbInstanceToPointInTimeResponseTypeDef",
    "ClientRestoreDbInstanceToPointInTimeTagsTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    "ClientRevokeDbSecurityGroupIngressResponseTypeDef",
    "ClientStartActivityStreamResponseTypeDef",
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStartDbClusterResponseDBClusterTypeDef",
    "ClientStartDbClusterResponseTypeDef",
    "ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientStartDbInstanceResponseDBInstanceTypeDef",
    "ClientStartDbInstanceResponseTypeDef",
    "ClientStartExportTaskResponseTypeDef",
    "ClientStopActivityStreamResponseTypeDef",
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    "ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStopDbClusterResponseDBClusterTypeDef",
    "ClientStopDbClusterResponseTypeDef",
    "ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    "ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    "ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientStopDbInstanceResponseDBInstanceTypeDef",
    "ClientStopDbInstanceResponseTypeDef",
    "VpnDetailsTypeDef",
    "CustomAvailabilityZoneTypeDef",
    "CustomAvailabilityZoneMessageTypeDef",
    "DBClusterBacktrackTypeDef",
    "DBClusterBacktrackMessageTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterRoleTypeDef",
    "ScalingConfigurationInfoTypeDef",
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
    "RestoreWindowTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBInstanceAutomatedBackupMessageTypeDef",
    "DBInstanceRoleTypeDef",
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
    "ProcessorFeatureTypeDef",
    "PendingModifiedValuesTypeDef",
    "DBInstanceTypeDef",
    "DBInstanceMessageTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "EC2SecurityGroupTypeDef",
    "IPRangeTypeDef",
    "DBSecurityGroupTypeDef",
    "DBSecurityGroupMessageTypeDef",
    "DBSnapshotTypeDef",
    "DBSnapshotMessageTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBLogFilesResponseTypeDef",
    "UserAuthConfigInfoTypeDef",
    "DBProxyTypeDef",
    "DescribeDBProxiesResponseTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "DBProxyTargetGroupTypeDef",
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    "DBProxyTargetTypeDef",
    "DescribeDBProxyTargetsResponseTypeDef",
    "EngineDefaultsTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DownloadDBLogFilePortionDetailsTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "ExportTaskTypeDef",
    "ExportTasksMessageTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "InstallationMediaFailureCauseTypeDef",
    "InstallationMediaTypeDef",
    "InstallationMediaMessageTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "OptionVersionTypeDef",
    "OptionGroupOptionTypeDef",
    "OptionGroupOptionsMessageTypeDef",
    "OptionSettingTypeDef",
    "OptionTypeDef",
    "OptionGroupTypeDef",
    "OptionGroupsTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "RecurringChargeTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstanceMessageTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ReservedDBInstancesOfferingMessageTypeDef",
    "SourceRegionTypeDef",
    "SourceRegionMessageTypeDef",
    "WaiterConfigTypeDef",
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
        "CustomerOverride": bool,
        "CustomerOverrideValidTill": datetime,
    },
    total=False,
)

CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {"Certificates": List[CertificateTypeDef], "Marker": str},
    total=False,
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

ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef = TypedDict(
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)

ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef = TypedDict(
    "ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef
        ],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

ClientAuthorizeDbSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientAuthorizeDbSecurityGroupIngressResponseTypeDef",
    {"DBSecurityGroup": ClientAuthorizeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef},
    total=False,
)

ClientBacktrackDbClusterResponseTypeDef = TypedDict(
    "ClientBacktrackDbClusterResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)

ClientCancelExportTaskResponseTypeDef = TypedDict(
    "ClientCancelExportTaskResponseTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
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

ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCopyDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "ClientCopyDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientCopyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)

ClientCopyDbSnapshotResponseTypeDef = TypedDict(
    "ClientCopyDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientCopyDbSnapshotResponseDBSnapshotTypeDef},
    total=False,
)

ClientCopyDbSnapshotTagsTypeDef = TypedDict(
    "ClientCopyDbSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef = TypedDict(
    "ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef = TypedDict(
    "ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientCopyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientCopyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientCopyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)

ClientCopyOptionGroupResponseOptionGroupTypeDef = TypedDict(
    "ClientCopyOptionGroupResponseOptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientCopyOptionGroupResponseOptionGroupOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)

ClientCopyOptionGroupResponseTypeDef = TypedDict(
    "ClientCopyOptionGroupResponseTypeDef",
    {"OptionGroup": ClientCopyOptionGroupResponseOptionGroupTypeDef},
    total=False,
)

ClientCopyOptionGroupTagsTypeDef = TypedDict(
    "ClientCopyOptionGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef = TypedDict(
    "ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)

ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef,
    },
    total=False,
)

ClientCreateCustomAvailabilityZoneResponseTypeDef = TypedDict(
    "ClientCreateCustomAvailabilityZoneResponseTypeDef",
    {
        "CustomAvailabilityZone": ClientCreateCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef
    },
    total=False,
)

ClientCreateDbClusterEndpointResponseTypeDef = TypedDict(
    "ClientCreateDbClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)

ClientCreateDbClusterEndpointTagsTypeDef = TypedDict(
    "ClientCreateDbClusterEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
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
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientCreateDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientCreateDbClusterResponseTypeDef = TypedDict(
    "ClientCreateDbClusterResponseTypeDef",
    {"DBCluster": ClientCreateDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientCreateDbClusterScalingConfigurationTypeDef = TypedDict(
    "ClientCreateDbClusterScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
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

ClientCreateDbInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbInstanceProcessorFeaturesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateDbInstanceReadReplicaResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceReadReplicaResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceReadReplicaResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientCreateDbInstanceReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceReadReplicaResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientCreateDbInstanceReadReplicaResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientCreateDbInstanceReadReplicaResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientCreateDbInstanceReadReplicaResponseTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaResponseTypeDef",
    {"DBInstance": ClientCreateDbInstanceReadReplicaResponseDBInstanceTypeDef},
    total=False,
)

ClientCreateDbInstanceReadReplicaTagsTypeDef = TypedDict(
    "ClientCreateDbInstanceReadReplicaTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
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

ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef",
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

ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "ProcessorFeatures": List[
            ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientCreateDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientCreateDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientCreateDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
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

ClientCreateDbProxyAuthTypeDef = TypedDict(
    "ClientCreateDbProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

ClientCreateDbProxyResponseDBProxyAuthTypeDef = TypedDict(
    "ClientCreateDbProxyResponseDBProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

ClientCreateDbProxyResponseDBProxyTypeDef = TypedDict(
    "ClientCreateDbProxyResponseDBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientCreateDbProxyResponseDBProxyAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

ClientCreateDbProxyResponseTypeDef = TypedDict(
    "ClientCreateDbProxyResponseTypeDef",
    {"DBProxy": ClientCreateDbProxyResponseDBProxyTypeDef},
    total=False,
)

ClientCreateDbProxyTagsTypeDef = TypedDict(
    "ClientCreateDbProxyTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef = TypedDict(
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)

ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef = TypedDict(
    "ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientCreateDbSecurityGroupResponseDBSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[ClientCreateDbSecurityGroupResponseDBSecurityGroupIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

ClientCreateDbSecurityGroupResponseTypeDef = TypedDict(
    "ClientCreateDbSecurityGroupResponseTypeDef",
    {"DBSecurityGroup": ClientCreateDbSecurityGroupResponseDBSecurityGroupTypeDef},
    total=False,
)

ClientCreateDbSecurityGroupTagsTypeDef = TypedDict(
    "ClientCreateDbSecurityGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "ClientCreateDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientCreateDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)

ClientCreateDbSnapshotResponseTypeDef = TypedDict(
    "ClientCreateDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientCreateDbSnapshotResponseDBSnapshotTypeDef},
    total=False,
)

ClientCreateDbSnapshotTagsTypeDef = TypedDict(
    "ClientCreateDbSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
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

ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)

ClientCreateGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "ClientCreateGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientCreateGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)

ClientCreateGlobalClusterResponseTypeDef = TypedDict(
    "ClientCreateGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientCreateGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)

ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef = TypedDict(
    "ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef = TypedDict(
    "ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientCreateOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientCreateOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientCreateOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)

ClientCreateOptionGroupResponseOptionGroupTypeDef = TypedDict(
    "ClientCreateOptionGroupResponseOptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientCreateOptionGroupResponseOptionGroupOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)

ClientCreateOptionGroupResponseTypeDef = TypedDict(
    "ClientCreateOptionGroupResponseTypeDef",
    {"OptionGroup": ClientCreateOptionGroupResponseOptionGroupTypeDef},
    total=False,
)

ClientCreateOptionGroupTagsTypeDef = TypedDict(
    "ClientCreateOptionGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef = TypedDict(
    "ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)

ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef = TypedDict(
    "ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneVpnDetailsTypeDef,
    },
    total=False,
)

ClientDeleteCustomAvailabilityZoneResponseTypeDef = TypedDict(
    "ClientDeleteCustomAvailabilityZoneResponseTypeDef",
    {
        "CustomAvailabilityZone": ClientDeleteCustomAvailabilityZoneResponseCustomAvailabilityZoneTypeDef
    },
    total=False,
)

ClientDeleteDbClusterEndpointResponseTypeDef = TypedDict(
    "ClientDeleteDbClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)

ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientDeleteDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
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

ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef = TypedDict(
    "ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef",
    {"EarliestTime": datetime, "LatestTime": datetime},
    total=False,
)

ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef = TypedDict(
    "ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupRestoreWindowTypeDef,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

ClientDeleteDbInstanceAutomatedBackupResponseTypeDef = TypedDict(
    "ClientDeleteDbInstanceAutomatedBackupResponseTypeDef",
    {
        "DBInstanceAutomatedBackup": ClientDeleteDbInstanceAutomatedBackupResponseDBInstanceAutomatedBackupTypeDef
    },
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
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

ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef",
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

ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "ProcessorFeatures": List[
            ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientDeleteDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientDeleteDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientDeleteDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientDeleteDbInstanceResponseTypeDef = TypedDict(
    "ClientDeleteDbInstanceResponseTypeDef",
    {"DBInstance": ClientDeleteDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientDeleteDbProxyResponseDBProxyAuthTypeDef = TypedDict(
    "ClientDeleteDbProxyResponseDBProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

ClientDeleteDbProxyResponseDBProxyTypeDef = TypedDict(
    "ClientDeleteDbProxyResponseDBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientDeleteDbProxyResponseDBProxyAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

ClientDeleteDbProxyResponseTypeDef = TypedDict(
    "ClientDeleteDbProxyResponseTypeDef",
    {"DBProxy": ClientDeleteDbProxyResponseDBProxyTypeDef},
    total=False,
)

ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDeleteDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "ClientDeleteDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientDeleteDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)

ClientDeleteDbSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientDeleteDbSnapshotResponseDBSnapshotTypeDef},
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

ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)

ClientDeleteGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "ClientDeleteGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientDeleteGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)

ClientDeleteGlobalClusterResponseTypeDef = TypedDict(
    "ClientDeleteGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientDeleteGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)

ClientDeleteInstallationMediaResponseFailureCauseTypeDef = TypedDict(
    "ClientDeleteInstallationMediaResponseFailureCauseTypeDef", {"Message": str}, total=False
)

ClientDeleteInstallationMediaResponseTypeDef = TypedDict(
    "ClientDeleteInstallationMediaResponseTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": ClientDeleteInstallationMediaResponseFailureCauseTypeDef,
    },
    total=False,
)

ClientDescribeAccountAttributesResponseAccountQuotasTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    {"AccountQuotaName": str, "Used": int, "Max": int},
    total=False,
)

ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseTypeDef",
    {"AccountQuotas": List[ClientDescribeAccountAttributesResponseAccountQuotasTypeDef]},
    total=False,
)

ClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "ClientDescribeCertificatesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
        "CustomerOverride": bool,
        "CustomerOverrideValidTill": datetime,
    },
    total=False,
)

ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseTypeDef",
    {"Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef], "Marker": str},
    total=False,
)

ClientDescribeCustomAvailabilityZonesFiltersTypeDef = TypedDict(
    "ClientDescribeCustomAvailabilityZonesFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef = TypedDict(
    "ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)

ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef = TypedDict(
    "ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesVpnDetailsTypeDef,
    },
    total=False,
)

ClientDescribeCustomAvailabilityZonesResponseTypeDef = TypedDict(
    "ClientDescribeCustomAvailabilityZonesResponseTypeDef",
    {
        "Marker": str,
        "CustomAvailabilityZones": List[
            ClientDescribeCustomAvailabilityZonesResponseCustomAvailabilityZonesTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbClusterBacktracksFiltersTypeDef = TypedDict(
    "ClientDescribeDbClusterBacktracksFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef = TypedDict(
    "ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)

ClientDescribeDbClusterBacktracksResponseTypeDef = TypedDict(
    "ClientDescribeDbClusterBacktracksResponseTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List[
            ClientDescribeDbClusterBacktracksResponseDBClusterBacktracksTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbClusterEndpointsFiltersTypeDef = TypedDict(
    "ClientDescribeDbClusterEndpointsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef = TypedDict(
    "ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)

ClientDescribeDbClusterEndpointsResponseTypeDef = TypedDict(
    "ClientDescribeDbClusterEndpointsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List[
            ClientDescribeDbClusterEndpointsResponseDBClusterEndpointsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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

ClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "ClientDescribeDbClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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
        "SupportedEngineModes": List[str],
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

ClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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

ClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "ClientDescribeDbClustersFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientDescribeDbClustersResponseDBClustersScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientDescribeDbClustersResponseTypeDef = TypedDict(
    "ClientDescribeDbClustersResponseTypeDef",
    {"Marker": str, "DBClusters": List[ClientDescribeDbClustersResponseDBClustersTypeDef]},
    total=False,
)

ClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "ClientDescribeDbEngineVersionsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

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
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
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

ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef = TypedDict(
    "ClientDescribeDbInstanceAutomatedBackupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef = TypedDict(
    "ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef",
    {"EarliestTime": datetime, "LatestTime": datetime},
    total=False,
)

ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef = TypedDict(
    "ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsRestoreWindowTypeDef,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef = TypedDict(
    "ClientDescribeDbInstanceAutomatedBackupsResponseTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List[
            ClientDescribeDbInstanceAutomatedBackupsResponseDBInstanceAutomatedBackupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "ClientDescribeDbInstancesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

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

ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef",
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

ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "ProcessorFeatures": List[
            ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientDescribeDbInstancesResponseDBInstancesProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientDescribeDbInstancesResponseDBInstancesAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientDescribeDbInstancesResponseDBInstancesListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientDescribeDbInstancesResponseTypeDef = TypedDict(
    "ClientDescribeDbInstancesResponseTypeDef",
    {"Marker": str, "DBInstances": List[ClientDescribeDbInstancesResponseDBInstancesTypeDef]},
    total=False,
)

ClientDescribeDbLogFilesFiltersTypeDef = TypedDict(
    "ClientDescribeDbLogFilesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef = TypedDict(
    "ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef",
    {"LogFileName": str, "LastWritten": int, "Size": int},
    total=False,
)

ClientDescribeDbLogFilesResponseTypeDef = TypedDict(
    "ClientDescribeDbLogFilesResponseTypeDef",
    {
        "DescribeDBLogFiles": List[ClientDescribeDbLogFilesResponseDescribeDBLogFilesTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "ClientDescribeDbParameterGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

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

ClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "ClientDescribeDbParametersFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

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
        "SupportedEngineModes": List[str],
    },
    total=False,
)

ClientDescribeDbParametersResponseTypeDef = TypedDict(
    "ClientDescribeDbParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeDbParametersResponseParametersTypeDef], "Marker": str},
    total=False,
)

ClientDescribeDbProxiesFiltersTypeDef = TypedDict(
    "ClientDescribeDbProxiesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef = TypedDict(
    "ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

ClientDescribeDbProxiesResponseDBProxiesTypeDef = TypedDict(
    "ClientDescribeDbProxiesResponseDBProxiesTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientDescribeDbProxiesResponseDBProxiesAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

ClientDescribeDbProxiesResponseTypeDef = TypedDict(
    "ClientDescribeDbProxiesResponseTypeDef",
    {"DBProxies": List[ClientDescribeDbProxiesResponseDBProxiesTypeDef], "Marker": str},
    total=False,
)

ClientDescribeDbProxyTargetGroupsFiltersTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": ClientDescribeDbProxyTargetGroupsResponseTargetGroupsConnectionPoolConfigTypeDef,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

ClientDescribeDbProxyTargetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List[ClientDescribeDbProxyTargetGroupsResponseTargetGroupsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeDbProxyTargetsFiltersTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbProxyTargetsResponseTargetsTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetsResponseTargetsTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"],
    },
    total=False,
)

ClientDescribeDbProxyTargetsResponseTypeDef = TypedDict(
    "ClientDescribeDbProxyTargetsResponseTypeDef",
    {"Targets": List[ClientDescribeDbProxyTargetsResponseTargetsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeDbSecurityGroupsFiltersTypeDef = TypedDict(
    "ClientDescribeDbSecurityGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef = TypedDict(
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)

ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

ClientDescribeDbSecurityGroupsResponseTypeDef = TypedDict(
    "ClientDescribeDbSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List[ClientDescribeDbSecurityGroupsResponseDBSecurityGroupsTypeDef],
    },
    total=False,
)

ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef = TypedDict(
    "ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)

ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef = TypedDict(
    "ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBSnapshotAttributes": List[
            ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef
        ],
    },
    total=False,
)

ClientDescribeDbSnapshotAttributesResponseTypeDef = TypedDict(
    "ClientDescribeDbSnapshotAttributesResponseTypeDef",
    {
        "DBSnapshotAttributesResult": ClientDescribeDbSnapshotAttributesResponseDBSnapshotAttributesResultTypeDef
    },
    total=False,
)

ClientDescribeDbSnapshotsFiltersTypeDef = TypedDict(
    "ClientDescribeDbSnapshotsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef = TypedDict(
    "ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef = TypedDict(
    "ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[
            ClientDescribeDbSnapshotsResponseDBSnapshotsProcessorFeaturesTypeDef
        ],
        "DbiResourceId": str,
    },
    total=False,
)

ClientDescribeDbSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeDbSnapshotsResponseTypeDef",
    {"Marker": str, "DBSnapshots": List[ClientDescribeDbSnapshotsResponseDBSnapshotsTypeDef]},
    total=False,
)

ClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "ClientDescribeDbSubnetGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

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

ClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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
        "SupportedEngineModes": List[str],
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

ClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "ClientDescribeEngineDefaultParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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
        "SupportedEngineModes": List[str],
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

ClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "ClientDescribeEventCategoriesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

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

ClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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

ClientDescribeEventsFiltersTypeDef = TypedDict(
    "ClientDescribeEventsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

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

ClientDescribeExportTasksFiltersTypeDef = TypedDict(
    "ClientDescribeExportTasksFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeExportTasksResponseExportTasksTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseExportTasksTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
    },
    total=False,
)

ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseTypeDef",
    {"Marker": str, "ExportTasks": List[ClientDescribeExportTasksResponseExportTasksTypeDef]},
    total=False,
)

ClientDescribeGlobalClustersFiltersTypeDef = TypedDict(
    "ClientDescribeGlobalClustersFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef = TypedDict(
    "ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)

ClientDescribeGlobalClustersResponseGlobalClustersTypeDef = TypedDict(
    "ClientDescribeGlobalClustersResponseGlobalClustersTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientDescribeGlobalClustersResponseGlobalClustersGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalClustersResponseTypeDef = TypedDict(
    "ClientDescribeGlobalClustersResponseTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List[ClientDescribeGlobalClustersResponseGlobalClustersTypeDef],
    },
    total=False,
)

ClientDescribeInstallationMediaFiltersTypeDef = TypedDict(
    "ClientDescribeInstallationMediaFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef = TypedDict(
    "ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef",
    {"Message": str},
    total=False,
)

ClientDescribeInstallationMediaResponseInstallationMediaTypeDef = TypedDict(
    "ClientDescribeInstallationMediaResponseInstallationMediaTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": ClientDescribeInstallationMediaResponseInstallationMediaFailureCauseTypeDef,
    },
    total=False,
)

ClientDescribeInstallationMediaResponseTypeDef = TypedDict(
    "ClientDescribeInstallationMediaResponseTypeDef",
    {
        "Marker": str,
        "InstallationMedia": List[ClientDescribeInstallationMediaResponseInstallationMediaTypeDef],
    },
    total=False,
)

ClientDescribeOptionGroupOptionsFiltersTypeDef = TypedDict(
    "ClientDescribeOptionGroupOptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef",
    {"AllowedValue": str, "MinimumEngineVersion": str},
    total=False,
)

ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef = TypedDict(
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef",
    {
        "SettingName": str,
        "SettingDescription": str,
        "DefaultValue": str,
        "ApplyType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsRequired": bool,
        "MinimumEngineVersionPerAllowedValue": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsMinimumEngineVersionPerAllowedValueTypeDef
        ],
    },
    total=False,
)

ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef = TypedDict(
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef",
    {"Version": str, "IsDefault": bool},
    total=False,
)

ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef = TypedDict(
    "ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef",
    {
        "Name": str,
        "Description": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "MinimumRequiredMinorEngineVersion": str,
        "PortRequired": bool,
        "DefaultPort": int,
        "OptionsDependedOn": List[str],
        "OptionsConflictsWith": List[str],
        "Persistent": bool,
        "Permanent": bool,
        "RequiresAutoMinorEngineVersionUpgrade": bool,
        "VpcOnly": bool,
        "SupportsOptionVersionDowngrade": bool,
        "OptionGroupOptionSettings": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionSettingsTypeDef
        ],
        "OptionGroupOptionVersions": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsOptionGroupOptionVersionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeOptionGroupOptionsResponseTypeDef = TypedDict(
    "ClientDescribeOptionGroupOptionsResponseTypeDef",
    {
        "OptionGroupOptions": List[
            ClientDescribeOptionGroupOptionsResponseOptionGroupOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeOptionGroupsFiltersTypeDef = TypedDict(
    "ClientDescribeOptionGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef = TypedDict(
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef = TypedDict(
    "ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientDescribeOptionGroupsResponseOptionGroupsListOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientDescribeOptionGroupsResponseOptionGroupsListOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientDescribeOptionGroupsResponseOptionGroupsListOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)

ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef = TypedDict(
    "ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientDescribeOptionGroupsResponseOptionGroupsListOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)

ClientDescribeOptionGroupsResponseTypeDef = TypedDict(
    "ClientDescribeOptionGroupsResponseTypeDef",
    {
        "OptionGroupsList": List[ClientDescribeOptionGroupsResponseOptionGroupsListTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef = TypedDict(
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef",
    {"Name": str, "DefaultValue": str, "AllowedValues": str},
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
        "AvailableProcessorFeatures": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailableProcessorFeaturesTypeDef
        ],
        "SupportedEngineModes": List[str],
        "SupportsStorageAutoscaling": bool,
        "SupportsKerberosAuthentication": bool,
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

ClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

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

ClientDescribeReservedDbInstancesFiltersTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesOfferingsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "RecurringCharges": List[
            ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedDbInstancesOfferingsResponseTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List[
            ClientDescribeReservedDbInstancesOfferingsResponseReservedDBInstancesOfferingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List[
            ClientDescribeReservedDbInstancesResponseReservedDBInstancesRecurringChargesTypeDef
        ],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)

ClientDescribeReservedDbInstancesResponseTypeDef = TypedDict(
    "ClientDescribeReservedDbInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List[
            ClientDescribeReservedDbInstancesResponseReservedDBInstancesTypeDef
        ],
    },
    total=False,
)

ClientDescribeSourceRegionsFiltersTypeDef = TypedDict(
    "ClientDescribeSourceRegionsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeSourceRegionsResponseSourceRegionsTypeDef = TypedDict(
    "ClientDescribeSourceRegionsResponseSourceRegionsTypeDef",
    {"RegionName": str, "Endpoint": str, "Status": str},
    total=False,
)

ClientDescribeSourceRegionsResponseTypeDef = TypedDict(
    "ClientDescribeSourceRegionsResponseTypeDef",
    {"Marker": str, "SourceRegions": List[ClientDescribeSourceRegionsResponseSourceRegionsTypeDef]},
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
        "SupportsStorageAutoscaling": bool,
    },
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef",
    {"Name": str, "DefaultValue": str, "AllowedValues": str},
    total=False,
)

ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
        ],
        "ValidProcessorFeatures": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageValidProcessorFeaturesTypeDef
        ],
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

ClientDownloadDbLogFilePortionResponseTypeDef = TypedDict(
    "ClientDownloadDbLogFilePortionResponseTypeDef",
    {"LogFileData": str, "Marker": str, "AdditionalDataPending": bool},
    total=False,
)

ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientFailoverDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientFailoverDbClusterResponseTypeDef = TypedDict(
    "ClientFailoverDbClusterResponseTypeDef",
    {"DBCluster": ClientFailoverDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientImportInstallationMediaResponseFailureCauseTypeDef = TypedDict(
    "ClientImportInstallationMediaResponseFailureCauseTypeDef", {"Message": str}, total=False
)

ClientImportInstallationMediaResponseTypeDef = TypedDict(
    "ClientImportInstallationMediaResponseTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": ClientImportInstallationMediaResponseFailureCauseTypeDef,
    },
    total=False,
)

ClientListTagsForResourceFiltersTypeDef = TypedDict(
    "ClientListTagsForResourceFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyCertificatesResponseCertificateTypeDef = TypedDict(
    "ClientModifyCertificatesResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
        "CustomerOverride": bool,
        "CustomerOverrideValidTill": datetime,
    },
    total=False,
)

ClientModifyCertificatesResponseTypeDef = TypedDict(
    "ClientModifyCertificatesResponseTypeDef",
    {"Certificate": ClientModifyCertificatesResponseCertificateTypeDef},
    total=False,
)

ClientModifyCurrentDbClusterCapacityResponseTypeDef = TypedDict(
    "ClientModifyCurrentDbClusterCapacityResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
    },
    total=False,
)

ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)

ClientModifyDbClusterEndpointResponseTypeDef = TypedDict(
    "ClientModifyDbClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
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
        "SupportedEngineModes": List[str],
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
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientModifyDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientModifyDbClusterResponseTypeDef = TypedDict(
    "ClientModifyDbClusterResponseTypeDef",
    {"DBCluster": ClientModifyDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientModifyDbClusterScalingConfigurationTypeDef = TypedDict(
    "ClientModifyDbClusterScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
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

ClientModifyDbInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientModifyDbInstanceProcessorFeaturesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
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

ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef",
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

ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "ProcessorFeatures": List[
            ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientModifyDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientModifyDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientModifyDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)

ClientModifyDbParameterGroupResponseTypeDef = TypedDict(
    "ClientModifyDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
)

ClientModifyDbProxyAuthTypeDef = TypedDict(
    "ClientModifyDbProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

ClientModifyDbProxyResponseDBProxyAuthTypeDef = TypedDict(
    "ClientModifyDbProxyResponseDBProxyAuthTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": str,
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

ClientModifyDbProxyResponseDBProxyTypeDef = TypedDict(
    "ClientModifyDbProxyResponseDBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[ClientModifyDbProxyResponseDBProxyAuthTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

ClientModifyDbProxyResponseTypeDef = TypedDict(
    "ClientModifyDbProxyResponseTypeDef",
    {"DBProxy": ClientModifyDbProxyResponseDBProxyTypeDef},
    total=False,
)

ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef = TypedDict(
    "ClientModifyDbProxyTargetGroupConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef = TypedDict(
    "ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef = TypedDict(
    "ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupConnectionPoolConfigTypeDef,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

ClientModifyDbProxyTargetGroupResponseTypeDef = TypedDict(
    "ClientModifyDbProxyTargetGroupResponseTypeDef",
    {"DBProxyTargetGroup": ClientModifyDbProxyTargetGroupResponseDBProxyTargetGroupTypeDef},
    total=False,
)

ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef = TypedDict(
    "ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)

ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef = TypedDict(
    "ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBSnapshotAttributes": List[
            ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultDBSnapshotAttributesTypeDef
        ],
    },
    total=False,
)

ClientModifyDbSnapshotAttributeResponseTypeDef = TypedDict(
    "ClientModifyDbSnapshotAttributeResponseTypeDef",
    {
        "DBSnapshotAttributesResult": ClientModifyDbSnapshotAttributeResponseDBSnapshotAttributesResultTypeDef
    },
    total=False,
)

ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef = TypedDict(
    "ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientModifyDbSnapshotResponseDBSnapshotTypeDef = TypedDict(
    "ClientModifyDbSnapshotResponseDBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ClientModifyDbSnapshotResponseDBSnapshotProcessorFeaturesTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)

ClientModifyDbSnapshotResponseTypeDef = TypedDict(
    "ClientModifyDbSnapshotResponseTypeDef",
    {"DBSnapshot": ClientModifyDbSnapshotResponseDBSnapshotTypeDef},
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

ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)

ClientModifyGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "ClientModifyGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientModifyGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)

ClientModifyGlobalClusterResponseTypeDef = TypedDict(
    "ClientModifyGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientModifyGlobalClusterResponseGlobalClusterTypeDef},
    total=False,
)

ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef = TypedDict(
    "ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

_RequiredClientModifyOptionGroupOptionsToIncludeTypeDef = TypedDict(
    "_RequiredClientModifyOptionGroupOptionsToIncludeTypeDef", {"OptionName": str}
)
_OptionalClientModifyOptionGroupOptionsToIncludeTypeDef = TypedDict(
    "_OptionalClientModifyOptionGroupOptionsToIncludeTypeDef",
    {
        "Port": int,
        "OptionVersion": str,
        "DBSecurityGroupMemberships": List[str],
        "VpcSecurityGroupMemberships": List[str],
        "OptionSettings": List[ClientModifyOptionGroupOptionsToIncludeOptionSettingsTypeDef],
    },
    total=False,
)


class ClientModifyOptionGroupOptionsToIncludeTypeDef(
    _RequiredClientModifyOptionGroupOptionsToIncludeTypeDef,
    _OptionalClientModifyOptionGroupOptionsToIncludeTypeDef,
):
    pass


ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef = TypedDict(
    "ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef = TypedDict(
    "ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef = TypedDict(
    "ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[
            ClientModifyOptionGroupResponseOptionGroupOptionsOptionSettingsTypeDef
        ],
        "DBSecurityGroupMemberships": List[
            ClientModifyOptionGroupResponseOptionGroupOptionsDBSecurityGroupMembershipsTypeDef
        ],
        "VpcSecurityGroupMemberships": List[
            ClientModifyOptionGroupResponseOptionGroupOptionsVpcSecurityGroupMembershipsTypeDef
        ],
    },
    total=False,
)

ClientModifyOptionGroupResponseOptionGroupTypeDef = TypedDict(
    "ClientModifyOptionGroupResponseOptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[ClientModifyOptionGroupResponseOptionGroupOptionsTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)

ClientModifyOptionGroupResponseTypeDef = TypedDict(
    "ClientModifyOptionGroupResponseTypeDef",
    {"OptionGroup": ClientModifyOptionGroupResponseOptionGroupTypeDef},
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientPromoteReadReplicaDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientPromoteReadReplicaDbClusterResponseTypeDef = TypedDict(
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    {"DBCluster": ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientPromoteReadReplicaResponseDBInstanceTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientPromoteReadReplicaResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientPromoteReadReplicaResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[
            ClientPromoteReadReplicaResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientPromoteReadReplicaResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientPromoteReadReplicaResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientPromoteReadReplicaResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientPromoteReadReplicaResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientPromoteReadReplicaResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientPromoteReadReplicaResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientPromoteReadReplicaResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientPromoteReadReplicaResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientPromoteReadReplicaResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientPromoteReadReplicaResponseTypeDef = TypedDict(
    "ClientPromoteReadReplicaResponseTypeDef",
    {"DBInstance": ClientPromoteReadReplicaResponseDBInstanceTypeDef},
    total=False,
)

ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef = TypedDict(
    "ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef = TypedDict(
    "ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List[
            ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceRecurringChargesTypeDef
        ],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)

ClientPurchaseReservedDbInstancesOfferingResponseTypeDef = TypedDict(
    "ClientPurchaseReservedDbInstancesOfferingResponseTypeDef",
    {
        "ReservedDBInstance": ClientPurchaseReservedDbInstancesOfferingResponseReservedDBInstanceTypeDef
    },
    total=False,
)

ClientPurchaseReservedDbInstancesOfferingTagsTypeDef = TypedDict(
    "ClientPurchaseReservedDbInstancesOfferingTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
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

ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef",
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

ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "ProcessorFeatures": List[
            ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientRebootDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientRebootDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientRebootDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientRebootDbInstanceResponseTypeDef = TypedDict(
    "ClientRebootDbInstanceResponseTypeDef",
    {"DBInstance": ClientRebootDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef = TypedDict(
    "ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"],
    },
    total=False,
)

ClientRegisterDbProxyTargetsResponseTypeDef = TypedDict(
    "ClientRegisterDbProxyTargetsResponseTypeDef",
    {"DBProxyTargets": List[ClientRegisterDbProxyTargetsResponseDBProxyTargetsTypeDef]},
    total=False,
)

ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef = TypedDict(
    "ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)

ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef = TypedDict(
    "ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[
            ClientRemoveFromGlobalClusterResponseGlobalClusterGlobalClusterMembersTypeDef
        ],
    },
    total=False,
)

ClientRemoveFromGlobalClusterResponseTypeDef = TypedDict(
    "ClientRemoveFromGlobalClusterResponseTypeDef",
    {"GlobalCluster": ClientRemoveFromGlobalClusterResponseGlobalClusterTypeDef},
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
        "SupportedEngineModes": List[str],
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
        "SupportedEngineModes": List[str],
    },
    total=False,
)

ClientResetDbParameterGroupResponseTypeDef = TypedDict(
    "ClientResetDbParameterGroupResponseTypeDef", {"DBParameterGroupName": str}, total=False
)

ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
    total=False,
)

ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)

ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef",
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
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterFromS3ResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientRestoreDbClusterFromS3ResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientRestoreDbClusterFromS3ResponseTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3ResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromS3ResponseDBClusterTypeDef},
    total=False,
)

ClientRestoreDbClusterFromS3TagsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromS3TagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientRestoreDbClusterFromSnapshotResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientRestoreDbClusterFromSnapshotResponseTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef},
    total=False,
)

ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)

ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientRestoreDbClusterToPointInTimeResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
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

ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceStatusInfosTypeDef
        ],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotResponseTypeDef",
    {"DBInstance": ClientRestoreDbInstanceFromDbSnapshotResponseDBInstanceTypeDef},
    total=False,
)

ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromDbSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreDbInstanceFromS3ResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRestoreDbInstanceFromS3ResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreDbInstanceFromS3ResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientRestoreDbInstanceFromS3ResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRestoreDbInstanceFromS3ResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientRestoreDbInstanceFromS3ResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientRestoreDbInstanceFromS3ResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientRestoreDbInstanceFromS3ResponseTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3ResponseTypeDef",
    {"DBInstance": ClientRestoreDbInstanceFromS3ResponseDBInstanceTypeDef},
    total=False,
)

ClientRestoreDbInstanceFromS3TagsTypeDef = TypedDict(
    "ClientRestoreDbInstanceFromS3TagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreDbInstanceToPointInTimeResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceStatusInfosTypeDef
        ],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceDomainMembershipsTypeDef
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceProcessorFeaturesTypeDef
        ],
        "DeletionProtection": bool,
        "AssociatedRoles": List[
            ClientRestoreDbInstanceToPointInTimeResponseDBInstanceAssociatedRolesTypeDef
        ],
        "ListenerEndpoint": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientRestoreDbInstanceToPointInTimeResponseTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeResponseTypeDef",
    {"DBInstance": ClientRestoreDbInstanceToPointInTimeResponseDBInstanceTypeDef},
    total=False,
)

ClientRestoreDbInstanceToPointInTimeTagsTypeDef = TypedDict(
    "ClientRestoreDbInstanceToPointInTimeTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef = TypedDict(
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef",
    {"Status": str, "CIDRIP": str},
    total=False,
)

ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef = TypedDict(
    "ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[
            ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupIPRangesTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

ClientRevokeDbSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientRevokeDbSecurityGroupIngressResponseTypeDef",
    {"DBSecurityGroup": ClientRevokeDbSecurityGroupIngressResponseDBSecurityGroupTypeDef},
    total=False,
)

ClientStartActivityStreamResponseTypeDef = TypedDict(
    "ClientStartActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": Literal["stopped", "starting", "started", "stopping"],
        "Mode": Literal["sync", "async"],
        "ApplyImmediately": bool,
    },
    total=False,
)

ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)

ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientStartDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientStartDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientStartDbClusterResponseTypeDef = TypedDict(
    "ClientStartDbClusterResponseTypeDef",
    {"DBCluster": ClientStartDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientStartDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientStartDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientStartDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientStartDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "ClientStartDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientStartDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientStartDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientStartDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientStartDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientStartDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientStartDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientStartDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientStartDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientStartDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientStartDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientStartDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientStartDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientStartDbInstanceResponseTypeDef = TypedDict(
    "ClientStartDbInstanceResponseTypeDef",
    {"DBInstance": ClientStartDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

ClientStartExportTaskResponseTypeDef = TypedDict(
    "ClientStartExportTaskResponseTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
    },
    total=False,
)

ClientStopActivityStreamResponseTypeDef = TypedDict(
    "ClientStopActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": Literal["stopped", "starting", "started", "stopping"],
    },
    total=False,
)

ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str, "FeatureName": str},
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

ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)

ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef = TypedDict(
    "ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
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
        "CustomEndpoints": List[str],
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientStopDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef],
        "VpcSecurityGroups": List[ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ClientStopDbClusterResponseDBClusterScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
    },
    total=False,
)

ClientStopDbClusterResponseTypeDef = TypedDict(
    "ClientStopDbClusterResponseTypeDef",
    {"DBCluster": ClientStopDbClusterResponseDBClusterTypeDef},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientStopDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
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
        "PendingCloudwatchLogsExports": ClientStopDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
        "ProcessorFeatures": List[
            ClientStopDbInstanceResponseDBInstancePendingModifiedValuesProcessorFeaturesTypeDef
        ],
    },
    total=False,
)

ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientStopDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "ClientStopDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientStopDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[ClientStopDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef],
        "VpcSecurityGroups": List[ClientStopDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef],
        "DBParameterGroups": List[ClientStopDbInstanceResponseDBInstanceDBParameterGroupsTypeDef],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientStopDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientStopDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
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
            ClientStopDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientStopDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[ClientStopDbInstanceResponseDBInstanceDomainMembershipsTypeDef],
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ClientStopDbInstanceResponseDBInstanceProcessorFeaturesTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[ClientStopDbInstanceResponseDBInstanceAssociatedRolesTypeDef],
        "ListenerEndpoint": ClientStopDbInstanceResponseDBInstanceListenerEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

ClientStopDbInstanceResponseTypeDef = TypedDict(
    "ClientStopDbInstanceResponseTypeDef",
    {"DBInstance": ClientStopDbInstanceResponseDBInstanceTypeDef},
    total=False,
)

VpnDetailsTypeDef = TypedDict(
    "VpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
    },
    total=False,
)

CustomAvailabilityZoneTypeDef = TypedDict(
    "CustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": VpnDetailsTypeDef,
    },
    total=False,
)

CustomAvailabilityZoneMessageTypeDef = TypedDict(
    "CustomAvailabilityZoneMessageTypeDef",
    {"Marker": str, "CustomAvailabilityZones": List[CustomAvailabilityZoneTypeDef]},
    total=False,
)

DBClusterBacktrackTypeDef = TypedDict(
    "DBClusterBacktrackTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)

DBClusterBacktrackMessageTypeDef = TypedDict(
    "DBClusterBacktrackMessageTypeDef",
    {"Marker": str, "DBClusterBacktracks": List[DBClusterBacktrackTypeDef]},
    total=False,
)

DBClusterEndpointTypeDef = TypedDict(
    "DBClusterEndpointTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)

DBClusterEndpointMessageTypeDef = TypedDict(
    "DBClusterEndpointMessageTypeDef",
    {"Marker": str, "DBClusterEndpoints": List[DBClusterEndpointTypeDef]},
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

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef", {"RoleArn": str, "Status": str, "FeatureName": str}, total=False
)

ScalingConfigurationInfoTypeDef = TypedDict(
    "ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": ScalingConfigurationInfoTypeDef,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": Literal["sync", "async"],
        "ActivityStreamStatus": Literal["stopped", "starting", "started", "stopping"],
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
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
        "SupportedEngineModes": List[str],
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
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
    },
    total=False,
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {"Marker": str, "DBEngineVersions": List[DBEngineVersionTypeDef]},
    total=False,
)

RestoreWindowTypeDef = TypedDict(
    "RestoreWindowTypeDef", {"EarliestTime": datetime, "LatestTime": datetime}, total=False
)

DBInstanceAutomatedBackupTypeDef = TypedDict(
    "DBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": RestoreWindowTypeDef,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

DBInstanceAutomatedBackupMessageTypeDef = TypedDict(
    "DBInstanceAutomatedBackupMessageTypeDef",
    {"Marker": str, "DBInstanceAutomatedBackups": List[DBInstanceAutomatedBackupTypeDef]},
    total=False,
)

DBInstanceRoleTypeDef = TypedDict(
    "DBInstanceRoleTypeDef", {"RoleArn": str, "FeatureName": str, "Status": str}, total=False
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

ProcessorFeatureTypeDef = TypedDict(
    "ProcessorFeatureTypeDef", {"Name": str, "Value": str}, total=False
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
        "ProcessorFeatures": List[ProcessorFeatureTypeDef],
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List[ProcessorFeatureTypeDef],
        "DeletionProtection": bool,
        "AssociatedRoles": List[DBInstanceRoleTypeDef],
        "ListenerEndpoint": EndpointTypeDef,
        "MaxAllocatedStorage": int,
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

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

IPRangeTypeDef = TypedDict("IPRangeTypeDef", {"Status": str, "CIDRIP": str}, total=False)

DBSecurityGroupTypeDef = TypedDict(
    "DBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List[EC2SecurityGroupTypeDef],
        "IPRanges": List[IPRangeTypeDef],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

DBSecurityGroupMessageTypeDef = TypedDict(
    "DBSecurityGroupMessageTypeDef",
    {"Marker": str, "DBSecurityGroups": List[DBSecurityGroupTypeDef]},
    total=False,
)

DBSnapshotTypeDef = TypedDict(
    "DBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[ProcessorFeatureTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)

DBSnapshotMessageTypeDef = TypedDict(
    "DBSnapshotMessageTypeDef", {"Marker": str, "DBSnapshots": List[DBSnapshotTypeDef]}, total=False
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {"Marker": str, "DBSubnetGroups": List[DBSubnetGroupTypeDef]},
    total=False,
)

DescribeDBLogFilesDetailsTypeDef = TypedDict(
    "DescribeDBLogFilesDetailsTypeDef",
    {"LogFileName": str, "LastWritten": int, "Size": int},
    total=False,
)

DescribeDBLogFilesResponseTypeDef = TypedDict(
    "DescribeDBLogFilesResponseTypeDef",
    {"DescribeDBLogFiles": List[DescribeDBLogFilesDetailsTypeDef], "Marker": str},
    total=False,
)

UserAuthConfigInfoTypeDef = TypedDict(
    "UserAuthConfigInfoTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": Literal["SECRETS"],
        "SecretArn": str,
        "IAMAuth": Literal["DISABLED", "REQUIRED"],
    },
    total=False,
)

DBProxyTypeDef = TypedDict(
    "DBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": Literal[
            "available",
            "modifying",
            "incompatible-network",
            "insufficient-resource-limits",
            "creating",
            "deleting",
        ],
        "EngineFamily": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List[UserAuthConfigInfoTypeDef],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

DescribeDBProxiesResponseTypeDef = TypedDict(
    "DescribeDBProxiesResponseTypeDef",
    {"DBProxies": List[DBProxyTypeDef], "Marker": str},
    total=False,
)

ConnectionPoolConfigurationInfoTypeDef = TypedDict(
    "ConnectionPoolConfigurationInfoTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

DBProxyTargetGroupTypeDef = TypedDict(
    "DBProxyTargetGroupTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": ConnectionPoolConfigurationInfoTypeDef,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

DescribeDBProxyTargetGroupsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    {"TargetGroups": List[DBProxyTargetGroupTypeDef], "Marker": str},
    total=False,
)

DBProxyTargetTypeDef = TypedDict(
    "DBProxyTargetTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"],
    },
    total=False,
)

DescribeDBProxyTargetsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetsResponseTypeDef",
    {"Targets": List[DBProxyTargetTypeDef], "Marker": str},
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {"DBParameterGroupFamily": str, "Marker": str, "Parameters": List[ParameterTypeDef]},
    total=False,
)

DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {"EngineDefaults": EngineDefaultsTypeDef},
    total=False,
)

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {"EngineDefaults": EngineDefaultsTypeDef},
    total=False,
)

DownloadDBLogFilePortionDetailsTypeDef = TypedDict(
    "DownloadDBLogFilePortionDetailsTypeDef",
    {"LogFileData": str, "Marker": str, "AdditionalDataPending": bool},
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

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
    },
    total=False,
)

ExportTasksMessageTypeDef = TypedDict(
    "ExportTasksMessageTypeDef",
    {"Marker": str, "ExportTasks": List[ExportTaskTypeDef]},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]})

GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {"DBClusterArn": str, "Readers": List[str], "IsWriter": bool},
    total=False,
)

GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List[GlobalClusterMemberTypeDef],
    },
    total=False,
)

GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {"Marker": str, "GlobalClusters": List[GlobalClusterTypeDef]},
    total=False,
)

InstallationMediaFailureCauseTypeDef = TypedDict(
    "InstallationMediaFailureCauseTypeDef", {"Message": str}, total=False
)

InstallationMediaTypeDef = TypedDict(
    "InstallationMediaTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": InstallationMediaFailureCauseTypeDef,
    },
    total=False,
)

InstallationMediaMessageTypeDef = TypedDict(
    "InstallationMediaMessageTypeDef",
    {"Marker": str, "InstallationMedia": List[InstallationMediaTypeDef]},
    total=False,
)

MinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "MinimumEngineVersionPerAllowedValueTypeDef",
    {"AllowedValue": str, "MinimumEngineVersion": str},
    total=False,
)

OptionGroupOptionSettingTypeDef = TypedDict(
    "OptionGroupOptionSettingTypeDef",
    {
        "SettingName": str,
        "SettingDescription": str,
        "DefaultValue": str,
        "ApplyType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsRequired": bool,
        "MinimumEngineVersionPerAllowedValue": List[MinimumEngineVersionPerAllowedValueTypeDef],
    },
    total=False,
)

OptionVersionTypeDef = TypedDict(
    "OptionVersionTypeDef", {"Version": str, "IsDefault": bool}, total=False
)

OptionGroupOptionTypeDef = TypedDict(
    "OptionGroupOptionTypeDef",
    {
        "Name": str,
        "Description": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "MinimumRequiredMinorEngineVersion": str,
        "PortRequired": bool,
        "DefaultPort": int,
        "OptionsDependedOn": List[str],
        "OptionsConflictsWith": List[str],
        "Persistent": bool,
        "Permanent": bool,
        "RequiresAutoMinorEngineVersionUpgrade": bool,
        "VpcOnly": bool,
        "SupportsOptionVersionDowngrade": bool,
        "OptionGroupOptionSettings": List[OptionGroupOptionSettingTypeDef],
        "OptionGroupOptionVersions": List[OptionVersionTypeDef],
    },
    total=False,
)

OptionGroupOptionsMessageTypeDef = TypedDict(
    "OptionGroupOptionsMessageTypeDef",
    {"OptionGroupOptions": List[OptionGroupOptionTypeDef], "Marker": str},
    total=False,
)

OptionSettingTypeDef = TypedDict(
    "OptionSettingTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

OptionTypeDef = TypedDict(
    "OptionTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List[OptionSettingTypeDef],
        "DBSecurityGroupMemberships": List[DBSecurityGroupMembershipTypeDef],
        "VpcSecurityGroupMemberships": List[VpcSecurityGroupMembershipTypeDef],
    },
    total=False,
)

OptionGroupTypeDef = TypedDict(
    "OptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List[OptionTypeDef],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)

OptionGroupsTypeDef = TypedDict(
    "OptionGroupsTypeDef",
    {"OptionGroupsList": List[OptionGroupTypeDef], "Marker": str},
    total=False,
)

AvailableProcessorFeatureTypeDef = TypedDict(
    "AvailableProcessorFeatureTypeDef",
    {"Name": str, "DefaultValue": str, "AllowedValues": str},
    total=False,
)

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
        "AvailableProcessorFeatures": List[AvailableProcessorFeatureTypeDef],
        "SupportedEngineModes": List[str],
        "SupportsStorageAutoscaling": bool,
        "SupportsKerberosAuthentication": bool,
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

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedDBInstanceTypeDef = TypedDict(
    "ReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List[RecurringChargeTypeDef],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)

ReservedDBInstanceMessageTypeDef = TypedDict(
    "ReservedDBInstanceMessageTypeDef",
    {"Marker": str, "ReservedDBInstances": List[ReservedDBInstanceTypeDef]},
    total=False,
)

ReservedDBInstancesOfferingTypeDef = TypedDict(
    "ReservedDBInstancesOfferingTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "RecurringCharges": List[RecurringChargeTypeDef],
    },
    total=False,
)

ReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "ReservedDBInstancesOfferingMessageTypeDef",
    {"Marker": str, "ReservedDBInstancesOfferings": List[ReservedDBInstancesOfferingTypeDef]},
    total=False,
)

SourceRegionTypeDef = TypedDict(
    "SourceRegionTypeDef", {"RegionName": str, "Endpoint": str, "Status": str}, total=False
)

SourceRegionMessageTypeDef = TypedDict(
    "SourceRegionMessageTypeDef",
    {"Marker": str, "SourceRegions": List[SourceRegionTypeDef]},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
