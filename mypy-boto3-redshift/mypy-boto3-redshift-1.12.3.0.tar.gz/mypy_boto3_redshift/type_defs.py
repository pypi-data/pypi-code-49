"""
Main interface for redshift service type definitions.

Usage::

    from mypy_boto3.redshift.type_defs import ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef

    data: ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef = {...}
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
    "ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef",
    "ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef",
    "ClientAcceptReservedNodeExchangeResponseTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    "ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef",
    "ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef",
    "ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef",
    "ClientAuthorizeSnapshotAccessResponseTypeDef",
    "ClientBatchDeleteClusterSnapshotsIdentifiersTypeDef",
    "ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef",
    "ClientBatchDeleteClusterSnapshotsResponseTypeDef",
    "ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef",
    "ClientBatchModifyClusterSnapshotsResponseTypeDef",
    "ClientCancelResizeResponseTypeDef",
    "ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientCopyClusterSnapshotResponseSnapshotTypeDef",
    "ClientCopyClusterSnapshotResponseTypeDef",
    "ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef",
    "ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef",
    "ClientCreateClusterParameterGroupResponseTypeDef",
    "ClientCreateClusterParameterGroupTagsTypeDef",
    "ClientCreateClusterResponseClusterClusterNodesTypeDef",
    "ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientCreateClusterResponseClusterDataTransferProgressTypeDef",
    "ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientCreateClusterResponseClusterElasticIpStatusTypeDef",
    "ClientCreateClusterResponseClusterEndpointTypeDef",
    "ClientCreateClusterResponseClusterHsmStatusTypeDef",
    "ClientCreateClusterResponseClusterIamRolesTypeDef",
    "ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientCreateClusterResponseClusterResizeInfoTypeDef",
    "ClientCreateClusterResponseClusterRestoreStatusTypeDef",
    "ClientCreateClusterResponseClusterTagsTypeDef",
    "ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef",
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef",
    "ClientCreateClusterSecurityGroupResponseTypeDef",
    "ClientCreateClusterSecurityGroupTagsTypeDef",
    "ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientCreateClusterSnapshotResponseSnapshotTypeDef",
    "ClientCreateClusterSnapshotResponseTypeDef",
    "ClientCreateClusterSnapshotTagsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    "ClientCreateClusterSubnetGroupResponseTypeDef",
    "ClientCreateClusterSubnetGroupTagsTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef",
    "ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef",
    "ClientCreateHsmClientCertificateResponseTypeDef",
    "ClientCreateHsmClientCertificateTagsTypeDef",
    "ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef",
    "ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef",
    "ClientCreateHsmConfigurationResponseTypeDef",
    "ClientCreateHsmConfigurationTagsTypeDef",
    "ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef",
    "ClientCreateScheduledActionResponseTargetActionTypeDef",
    "ClientCreateScheduledActionResponseTypeDef",
    "ClientCreateScheduledActionTargetActionResizeClusterTypeDef",
    "ClientCreateScheduledActionTargetActionTypeDef",
    "ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef",
    "ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef",
    "ClientCreateSnapshotCopyGrantResponseTypeDef",
    "ClientCreateSnapshotCopyGrantTagsTypeDef",
    "ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef",
    "ClientCreateSnapshotScheduleResponseTagsTypeDef",
    "ClientCreateSnapshotScheduleResponseTypeDef",
    "ClientCreateSnapshotScheduleTagsTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDeleteClusterResponseClusterClusterNodesTypeDef",
    "ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientDeleteClusterResponseClusterDataTransferProgressTypeDef",
    "ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientDeleteClusterResponseClusterElasticIpStatusTypeDef",
    "ClientDeleteClusterResponseClusterEndpointTypeDef",
    "ClientDeleteClusterResponseClusterHsmStatusTypeDef",
    "ClientDeleteClusterResponseClusterIamRolesTypeDef",
    "ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientDeleteClusterResponseClusterResizeInfoTypeDef",
    "ClientDeleteClusterResponseClusterRestoreStatusTypeDef",
    "ClientDeleteClusterResponseClusterTagsTypeDef",
    "ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientDeleteClusterSnapshotResponseSnapshotTypeDef",
    "ClientDeleteClusterSnapshotResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef",
    "ClientDescribeAccountAttributesResponseAccountAttributesTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef",
    "ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef",
    "ClientDescribeClusterDbRevisionsResponseTypeDef",
    "ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef",
    "ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef",
    "ClientDescribeClusterParameterGroupsResponseTypeDef",
    "ClientDescribeClusterParametersResponseParametersTypeDef",
    "ClientDescribeClusterParametersResponseTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef",
    "ClientDescribeClusterSecurityGroupsResponseTypeDef",
    "ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef",
    "ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef",
    "ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeClusterSnapshotsResponseTypeDef",
    "ClientDescribeClusterSnapshotsSortingEntitiesTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef",
    "ClientDescribeClusterSubnetGroupsResponseTypeDef",
    "ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef",
    "ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef",
    "ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef",
    "ClientDescribeClusterTracksResponseTypeDef",
    "ClientDescribeClusterVersionsResponseClusterVersionsTypeDef",
    "ClientDescribeClusterVersionsResponseTypeDef",
    "ClientDescribeClustersResponseClustersClusterNodesTypeDef",
    "ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef",
    "ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef",
    "ClientDescribeClustersResponseClustersDataTransferProgressTypeDef",
    "ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef",
    "ClientDescribeClustersResponseClustersElasticIpStatusTypeDef",
    "ClientDescribeClustersResponseClustersEndpointTypeDef",
    "ClientDescribeClustersResponseClustersHsmStatusTypeDef",
    "ClientDescribeClustersResponseClustersIamRolesTypeDef",
    "ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef",
    "ClientDescribeClustersResponseClustersResizeInfoTypeDef",
    "ClientDescribeClustersResponseClustersRestoreStatusTypeDef",
    "ClientDescribeClustersResponseClustersTagsTypeDef",
    "ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef",
    "ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef",
    "ClientDescribeDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef",
    "ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef",
    "ClientDescribeHsmClientCertificatesResponseTypeDef",
    "ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef",
    "ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef",
    "ClientDescribeHsmConfigurationsResponseTypeDef",
    "ClientDescribeLoggingStatusResponseTypeDef",
    "ClientDescribeNodeConfigurationOptionsFiltersTypeDef",
    "ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef",
    "ClientDescribeNodeConfigurationOptionsResponseTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef",
    "ClientDescribeOrderableClusterOptionsResponseTypeDef",
    "ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef",
    "ClientDescribeReservedNodeOfferingsResponseTypeDef",
    "ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef",
    "ClientDescribeReservedNodesResponseReservedNodesTypeDef",
    "ClientDescribeReservedNodesResponseTypeDef",
    "ClientDescribeResizeResponseTypeDef",
    "ClientDescribeScheduledActionsFiltersTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef",
    "ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef",
    "ClientDescribeSnapshotCopyGrantsResponseTypeDef",
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef",
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef",
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef",
    "ClientDescribeSnapshotSchedulesResponseTypeDef",
    "ClientDescribeStorageResponseTypeDef",
    "ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef",
    "ClientDescribeTableRestoreStatusResponseTypeDef",
    "ClientDescribeTagsResponseTaggedResourcesTagTypeDef",
    "ClientDescribeTagsResponseTaggedResourcesTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDisableLoggingResponseTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    "ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterEndpointTypeDef",
    "ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef",
    "ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    "ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef",
    "ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    "ClientDisableSnapshotCopyResponseClusterTagsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    "ClientDisableSnapshotCopyResponseClusterTypeDef",
    "ClientDisableSnapshotCopyResponseTypeDef",
    "ClientEnableLoggingResponseTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    "ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterEndpointTypeDef",
    "ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef",
    "ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    "ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef",
    "ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    "ClientEnableSnapshotCopyResponseClusterTagsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    "ClientEnableSnapshotCopyResponseClusterTypeDef",
    "ClientEnableSnapshotCopyResponseTypeDef",
    "ClientGetClusterCredentialsResponseTypeDef",
    "ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    "ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef",
    "ClientGetReservedNodeExchangeOfferingsResponseTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterTagsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterDbRevisionResponseClusterTypeDef",
    "ClientModifyClusterDbRevisionResponseTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterEndpointTypeDef",
    "ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef",
    "ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterIamRolesResponseClusterTagsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterIamRolesResponseClusterTypeDef",
    "ClientModifyClusterIamRolesResponseTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterTagsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterMaintenanceResponseClusterTypeDef",
    "ClientModifyClusterMaintenanceResponseTypeDef",
    "ClientModifyClusterParameterGroupParametersTypeDef",
    "ClientModifyClusterParameterGroupResponseTypeDef",
    "ClientModifyClusterResponseClusterClusterNodesTypeDef",
    "ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifyClusterResponseClusterDataTransferProgressTypeDef",
    "ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifyClusterResponseClusterElasticIpStatusTypeDef",
    "ClientModifyClusterResponseClusterEndpointTypeDef",
    "ClientModifyClusterResponseClusterHsmStatusTypeDef",
    "ClientModifyClusterResponseClusterIamRolesTypeDef",
    "ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifyClusterResponseClusterResizeInfoTypeDef",
    "ClientModifyClusterResponseClusterRestoreStatusTypeDef",
    "ClientModifyClusterResponseClusterTagsTypeDef",
    "ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifyClusterResponseClusterTypeDef",
    "ClientModifyClusterResponseTypeDef",
    "ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef",
    "ClientModifyClusterSnapshotResponseSnapshotTypeDef",
    "ClientModifyClusterSnapshotResponseTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    "ClientModifyClusterSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef",
    "ClientModifyScheduledActionResponseTargetActionTypeDef",
    "ClientModifyScheduledActionResponseTypeDef",
    "ClientModifyScheduledActionTargetActionResizeClusterTypeDef",
    "ClientModifyScheduledActionTargetActionTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef",
    "ClientModifySnapshotCopyRetentionPeriodResponseTypeDef",
    "ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef",
    "ClientModifySnapshotScheduleResponseTagsTypeDef",
    "ClientModifySnapshotScheduleResponseTypeDef",
    "ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef",
    "ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef",
    "ClientPurchaseReservedNodeOfferingResponseTypeDef",
    "ClientRebootClusterResponseClusterClusterNodesTypeDef",
    "ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientRebootClusterResponseClusterDataTransferProgressTypeDef",
    "ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientRebootClusterResponseClusterElasticIpStatusTypeDef",
    "ClientRebootClusterResponseClusterEndpointTypeDef",
    "ClientRebootClusterResponseClusterHsmStatusTypeDef",
    "ClientRebootClusterResponseClusterIamRolesTypeDef",
    "ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientRebootClusterResponseClusterResizeInfoTypeDef",
    "ClientRebootClusterResponseClusterRestoreStatusTypeDef",
    "ClientRebootClusterResponseClusterTagsTypeDef",
    "ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientRebootClusterResponseClusterTypeDef",
    "ClientRebootClusterResponseTypeDef",
    "ClientResetClusterParameterGroupParametersTypeDef",
    "ClientResetClusterParameterGroupResponseTypeDef",
    "ClientResizeClusterResponseClusterClusterNodesTypeDef",
    "ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef",
    "ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef",
    "ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientResizeClusterResponseClusterDataTransferProgressTypeDef",
    "ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientResizeClusterResponseClusterElasticIpStatusTypeDef",
    "ClientResizeClusterResponseClusterEndpointTypeDef",
    "ClientResizeClusterResponseClusterHsmStatusTypeDef",
    "ClientResizeClusterResponseClusterIamRolesTypeDef",
    "ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef",
    "ClientResizeClusterResponseClusterResizeInfoTypeDef",
    "ClientResizeClusterResponseClusterRestoreStatusTypeDef",
    "ClientResizeClusterResponseClusterTagsTypeDef",
    "ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef",
    "ClientResizeClusterResponseClusterTypeDef",
    "ClientResizeClusterResponseTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreFromClusterSnapshotResponseClusterTypeDef",
    "ClientRestoreFromClusterSnapshotResponseTypeDef",
    "ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef",
    "ClientRestoreTableFromClusterSnapshotResponseTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    "ClientRevokeClusterSecurityGroupIngressResponseTypeDef",
    "ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    "ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef",
    "ClientRevokeSnapshotAccessResponseSnapshotTypeDef",
    "ClientRevokeSnapshotAccessResponseTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef",
    "ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterEndpointTypeDef",
    "ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef",
    "ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef",
    "ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef",
    "ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef",
    "ClientRotateEncryptionKeyResponseClusterTagsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef",
    "ClientRotateEncryptionKeyResponseClusterTypeDef",
    "ClientRotateEncryptionKeyResponseTypeDef",
    "RevisionTargetTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ParameterTypeDef",
    "ClusterParameterGroupDetailsTypeDef",
    "TagTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterGroupsMessageTypeDef",
    "EC2SecurityGroupTypeDef",
    "IPRangeTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSecurityGroupMessageTypeDef",
    "SupportedPlatformTypeDef",
    "AvailabilityZoneTypeDef",
    "SubnetTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterSubnetGroupMessageTypeDef",
    "ClusterVersionTypeDef",
    "ClusterVersionsMessageTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "DataTransferProgressTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "ElasticIpStatusTypeDef",
    "EndpointTypeDef",
    "HsmStatusTypeDef",
    "PendingModifiedValuesTypeDef",
    "ResizeInfoTypeDef",
    "RestoreStatusTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "ClusterTypeDef",
    "ClustersMessageTypeDef",
    "DefaultClusterParametersTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "SnapshotScheduleTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "RecurringChargeTypeDef",
    "ReservedNodeOfferingTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmConfigurationTypeDef",
    "HsmConfigurationMessageTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionTypeDef",
    "NodeConfigurationOptionsMessageTypeDef",
    "OrderableClusterOptionTypeDef",
    "OrderableClusterOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageTypeDef",
    "ScheduledActionFilterTypeDef",
    "ResizeClusterMessageTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "SnapshotTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotSortingEntityTypeDef",
    "TableRestoreStatusTypeDef",
    "TableRestoreStatusMessageTypeDef",
    "TaggedResourceTypeDef",
    "TaggedResourceListMessageTypeDef",
    "SupportedOperationTypeDef",
    "UpdateTargetTypeDef",
    "MaintenanceTrackTypeDef",
    "TrackListMessageTypeDef",
    "WaiterConfigTypeDef",
)

ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef = TypedDict(
    "ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef = TypedDict(
    "ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ClientAcceptReservedNodeExchangeResponseTypeDef = TypedDict(
    "ClientAcceptReservedNodeExchangeResponseTypeDef",
    {"ExchangedReservedNode": ClientAcceptReservedNodeExchangeResponseExchangedReservedNodeTypeDef},
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef
        ],
    },
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef
        ],
        "Tags": List[
            ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef
        ],
    },
    total=False,
)

ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientAuthorizeClusterSecurityGroupIngressResponseTypeDef",
    {
        "ClusterSecurityGroup": ClientAuthorizeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef
    },
    total=False,
)

ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef = TypedDict(
    "ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef = TypedDict(
    "ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientAuthorizeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientAuthorizeSnapshotAccessResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientAuthorizeSnapshotAccessResponseTypeDef = TypedDict(
    "ClientAuthorizeSnapshotAccessResponseTypeDef",
    {"Snapshot": ClientAuthorizeSnapshotAccessResponseSnapshotTypeDef},
    total=False,
)

_RequiredClientBatchDeleteClusterSnapshotsIdentifiersTypeDef = TypedDict(
    "_RequiredClientBatchDeleteClusterSnapshotsIdentifiersTypeDef", {"SnapshotIdentifier": str}
)
_OptionalClientBatchDeleteClusterSnapshotsIdentifiersTypeDef = TypedDict(
    "_OptionalClientBatchDeleteClusterSnapshotsIdentifiersTypeDef",
    {"SnapshotClusterIdentifier": str},
    total=False,
)


class ClientBatchDeleteClusterSnapshotsIdentifiersTypeDef(
    _RequiredClientBatchDeleteClusterSnapshotsIdentifiersTypeDef,
    _OptionalClientBatchDeleteClusterSnapshotsIdentifiersTypeDef,
):
    pass


ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef = TypedDict(
    "ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

ClientBatchDeleteClusterSnapshotsResponseTypeDef = TypedDict(
    "ClientBatchDeleteClusterSnapshotsResponseTypeDef",
    {
        "Resources": List[str],
        "Errors": List[ClientBatchDeleteClusterSnapshotsResponseErrorsTypeDef],
    },
    total=False,
)

ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef = TypedDict(
    "ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

ClientBatchModifyClusterSnapshotsResponseTypeDef = TypedDict(
    "ClientBatchModifyClusterSnapshotsResponseTypeDef",
    {
        "Resources": List[str],
        "Errors": List[ClientBatchModifyClusterSnapshotsResponseErrorsTypeDef],
    },
    total=False,
)

ClientCancelResizeResponseTypeDef = TypedDict(
    "ClientCancelResizeResponseTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
    },
    total=False,
)

ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCopyClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientCopyClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientCopyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientCopyClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientCopyClusterSnapshotResponseTypeDef = TypedDict(
    "ClientCopyClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientCopyClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef = TypedDict(
    "ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef = TypedDict(
    "ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List[ClientCreateClusterParameterGroupResponseClusterParameterGroupTagsTypeDef],
    },
    total=False,
)

ClientCreateClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientCreateClusterParameterGroupResponseTypeDef",
    {
        "ClusterParameterGroup": ClientCreateClusterParameterGroupResponseClusterParameterGroupTypeDef
    },
    total=False,
)

ClientCreateClusterParameterGroupTagsTypeDef = TypedDict(
    "ClientCreateClusterParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientCreateClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientCreateClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientCreateClusterResponseClusterEndpointTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)

ClientCreateClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientCreateClusterResponseClusterIamRolesTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientCreateClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientCreateClusterResponseClusterTagsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientCreateClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientCreateClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientCreateClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientCreateClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientCreateClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientCreateClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientCreateClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientCreateClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientCreateClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientCreateClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientCreateClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientCreateClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientCreateClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)

ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)

ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTagsTypeDef
        ],
    },
    total=False,
)

ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientCreateClusterSecurityGroupResponseClusterSecurityGroupIPRangesTypeDef
        ],
        "Tags": List[ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTagsTypeDef],
    },
    total=False,
)

ClientCreateClusterSecurityGroupResponseTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupResponseTypeDef",
    {"ClusterSecurityGroup": ClientCreateClusterSecurityGroupResponseClusterSecurityGroupTypeDef},
    total=False,
)

ClientCreateClusterSecurityGroupTagsTypeDef = TypedDict(
    "ClientCreateClusterSecurityGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientCreateClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientCreateClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientCreateClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientCreateClusterSnapshotResponseTypeDef = TypedDict(
    "ClientCreateClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientCreateClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientCreateClusterSnapshotTagsTypeDef = TypedDict(
    "ClientCreateClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)

ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef],
        "Tags": List[ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef],
    },
    total=False,
)

ClientCreateClusterSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupResponseTypeDef",
    {"ClusterSubnetGroup": ClientCreateClusterSubnetGroupResponseClusterSubnetGroupTypeDef},
    total=False,
)

ClientCreateClusterSubnetGroupTagsTypeDef = TypedDict(
    "ClientCreateClusterSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateClusterTagsTypeDef = TypedDict(
    "ClientCreateClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[ClientCreateEventSubscriptionResponseEventSubscriptionTagsTypeDef],
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

ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef = TypedDict(
    "ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef = TypedDict(
    "ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List[ClientCreateHsmClientCertificateResponseHsmClientCertificateTagsTypeDef],
    },
    total=False,
)

ClientCreateHsmClientCertificateResponseTypeDef = TypedDict(
    "ClientCreateHsmClientCertificateResponseTypeDef",
    {"HsmClientCertificate": ClientCreateHsmClientCertificateResponseHsmClientCertificateTypeDef},
    total=False,
)

ClientCreateHsmClientCertificateTagsTypeDef = TypedDict(
    "ClientCreateHsmClientCertificateTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef = TypedDict(
    "ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef = TypedDict(
    "ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List[ClientCreateHsmConfigurationResponseHsmConfigurationTagsTypeDef],
    },
    total=False,
)

ClientCreateHsmConfigurationResponseTypeDef = TypedDict(
    "ClientCreateHsmConfigurationResponseTypeDef",
    {"HsmConfiguration": ClientCreateHsmConfigurationResponseHsmConfigurationTypeDef},
    total=False,
)

ClientCreateHsmConfigurationTagsTypeDef = TypedDict(
    "ClientCreateHsmConfigurationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef = TypedDict(
    "ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)

ClientCreateScheduledActionResponseTargetActionTypeDef = TypedDict(
    "ClientCreateScheduledActionResponseTargetActionTypeDef",
    {"ResizeCluster": ClientCreateScheduledActionResponseTargetActionResizeClusterTypeDef},
    total=False,
)

ClientCreateScheduledActionResponseTypeDef = TypedDict(
    "ClientCreateScheduledActionResponseTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ClientCreateScheduledActionResponseTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

_RequiredClientCreateScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_RequiredClientCreateScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterIdentifier": str},
)
_OptionalClientCreateScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_OptionalClientCreateScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterType": str, "NodeType": str, "NumberOfNodes": int, "Classic": bool},
    total=False,
)


class ClientCreateScheduledActionTargetActionResizeClusterTypeDef(
    _RequiredClientCreateScheduledActionTargetActionResizeClusterTypeDef,
    _OptionalClientCreateScheduledActionTargetActionResizeClusterTypeDef,
):
    pass


ClientCreateScheduledActionTargetActionTypeDef = TypedDict(
    "ClientCreateScheduledActionTargetActionTypeDef",
    {"ResizeCluster": ClientCreateScheduledActionTargetActionResizeClusterTypeDef},
    total=False,
)

ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef = TypedDict(
    "ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef = TypedDict(
    "ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List[ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTagsTypeDef],
    },
    total=False,
)

ClientCreateSnapshotCopyGrantResponseTypeDef = TypedDict(
    "ClientCreateSnapshotCopyGrantResponseTypeDef",
    {"SnapshotCopyGrant": ClientCreateSnapshotCopyGrantResponseSnapshotCopyGrantTypeDef},
    total=False,
)

ClientCreateSnapshotCopyGrantTagsTypeDef = TypedDict(
    "ClientCreateSnapshotCopyGrantTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef = TypedDict(
    "ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)

ClientCreateSnapshotScheduleResponseTagsTypeDef = TypedDict(
    "ClientCreateSnapshotScheduleResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSnapshotScheduleResponseTypeDef = TypedDict(
    "ClientCreateSnapshotScheduleResponseTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[ClientCreateSnapshotScheduleResponseTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[ClientCreateSnapshotScheduleResponseAssociatedClustersTypeDef],
    },
    total=False,
)

ClientCreateSnapshotScheduleTagsTypeDef = TypedDict(
    "ClientCreateSnapshotScheduleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateTagsTagsTypeDef = TypedDict(
    "ClientCreateTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientDeleteClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientDeleteClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientDeleteClusterResponseClusterEndpointTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)

ClientDeleteClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientDeleteClusterResponseClusterIamRolesTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientDeleteClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientDeleteClusterResponseClusterTagsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDeleteClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientDeleteClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientDeleteClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientDeleteClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientDeleteClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientDeleteClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientDeleteClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientDeleteClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientDeleteClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientDeleteClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientDeleteClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientDeleteClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientDeleteClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientDeleteClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)

ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDeleteClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientDeleteClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientDeleteClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientDeleteClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientDeleteClusterSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientDeleteClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef",
    {"AttributeValue": str},
    total=False,
)

ClientDescribeAccountAttributesResponseAccountAttributesTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseAccountAttributesTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[
            ClientDescribeAccountAttributesResponseAccountAttributesAttributeValuesTypeDef
        ],
    },
    total=False,
)

ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseTypeDef",
    {"AccountAttributes": List[ClientDescribeAccountAttributesResponseAccountAttributesTypeDef]},
    total=False,
)

ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef = TypedDict(
    "ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef",
    {"DatabaseRevision": str, "Description": str, "DatabaseRevisionReleaseDate": datetime},
    total=False,
)

ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef = TypedDict(
    "ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List[
            ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsRevisionTargetsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterDbRevisionsResponseTypeDef = TypedDict(
    "ClientDescribeClusterDbRevisionsResponseTypeDef",
    {
        "Marker": str,
        "ClusterDbRevisions": List[
            ClientDescribeClusterDbRevisionsResponseClusterDbRevisionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef = TypedDict(
    "ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef = TypedDict(
    "ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List[ClientDescribeClusterParameterGroupsResponseParameterGroupsTagsTypeDef],
    },
    total=False,
)

ClientDescribeClusterParameterGroupsResponseTypeDef = TypedDict(
    "ClientDescribeClusterParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "ParameterGroups": List[ClientDescribeClusterParameterGroupsResponseParameterGroupsTypeDef],
    },
    total=False,
)

ClientDescribeClusterParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeClusterParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ClientDescribeClusterParametersResponseTypeDef = TypedDict(
    "ClientDescribeClusterParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeClusterParametersResponseParametersTypeDef], "Marker": str},
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTagsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsIPRangesTypeDef
        ],
        "Tags": List[ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTagsTypeDef],
    },
    total=False,
)

ClientDescribeClusterSecurityGroupsResponseTypeDef = TypedDict(
    "ClientDescribeClusterSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "ClusterSecurityGroups": List[
            ClientDescribeClusterSecurityGroupsResponseClusterSecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef = TypedDict(
    "ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientDescribeClusterSnapshotsResponseSnapshotsAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientDescribeClusterSnapshotsResponseSnapshotsTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientDescribeClusterSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeClusterSnapshotsResponseTypeDef",
    {"Marker": str, "Snapshots": List[ClientDescribeClusterSnapshotsResponseSnapshotsTypeDef]},
    total=False,
)

_RequiredClientDescribeClusterSnapshotsSortingEntitiesTypeDef = TypedDict(
    "_RequiredClientDescribeClusterSnapshotsSortingEntitiesTypeDef",
    {"Attribute": Literal["SOURCE_TYPE", "TOTAL_SIZE", "CREATE_TIME"]},
)
_OptionalClientDescribeClusterSnapshotsSortingEntitiesTypeDef = TypedDict(
    "_OptionalClientDescribeClusterSnapshotsSortingEntitiesTypeDef",
    {"SortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class ClientDescribeClusterSnapshotsSortingEntitiesTypeDef(
    _RequiredClientDescribeClusterSnapshotsSortingEntitiesTypeDef,
    _OptionalClientDescribeClusterSnapshotsSortingEntitiesTypeDef,
):
    pass


ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef = TypedDict(
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsSubnetsTypeDef],
        "Tags": List[ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTagsTypeDef],
    },
    total=False,
)

ClientDescribeClusterSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeClusterSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ClusterSubnetGroups": List[
            ClientDescribeClusterSubnetGroupsResponseClusterSubnetGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef = TypedDict(
    "ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef",
    {"OperationName": str},
    total=False,
)

ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef = TypedDict(
    "ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List[
            ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsSupportedOperationsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef = TypedDict(
    "ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List[
            ClientDescribeClusterTracksResponseMaintenanceTracksUpdateTargetsTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterTracksResponseTypeDef = TypedDict(
    "ClientDescribeClusterTracksResponseTypeDef",
    {
        "MaintenanceTracks": List[ClientDescribeClusterTracksResponseMaintenanceTracksTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeClusterVersionsResponseClusterVersionsTypeDef = TypedDict(
    "ClientDescribeClusterVersionsResponseClusterVersionsTypeDef",
    {"ClusterVersion": str, "ClusterParameterGroupFamily": str, "Description": str},
    total=False,
)

ClientDescribeClusterVersionsResponseTypeDef = TypedDict(
    "ClientDescribeClusterVersionsResponseTypeDef",
    {
        "Marker": str,
        "ClusterVersions": List[ClientDescribeClusterVersionsResponseClusterVersionsTypeDef],
    },
    total=False,
)

ClientDescribeClustersResponseClustersClusterNodesTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientDescribeClustersResponseClustersClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersDataTransferProgressTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientDescribeClustersResponseClustersElasticIpStatusTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientDescribeClustersResponseClustersEndpointTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDescribeClustersResponseClustersHsmStatusTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientDescribeClustersResponseClustersIamRolesTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersResizeInfoTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientDescribeClustersResponseClustersRestoreStatusTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientDescribeClustersResponseClustersTagsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDescribeClustersResponseClustersEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientDescribeClustersResponseClustersClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientDescribeClustersResponseClustersVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientDescribeClustersResponseClustersClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeClustersResponseClustersPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientDescribeClustersResponseClustersRestoreStatusTypeDef,
        "DataTransferProgress": ClientDescribeClustersResponseClustersDataTransferProgressTypeDef,
        "HsmStatus": ClientDescribeClustersResponseClustersHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientDescribeClustersResponseClustersClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientDescribeClustersResponseClustersClusterNodesTypeDef],
        "ElasticIpStatus": ClientDescribeClustersResponseClustersElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientDescribeClustersResponseClustersTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientDescribeClustersResponseClustersIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientDescribeClustersResponseClustersDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientDescribeClustersResponseClustersResizeInfoTypeDef,
    },
    total=False,
)

ClientDescribeClustersResponseTypeDef = TypedDict(
    "ClientDescribeClustersResponseTypeDef",
    {"Marker": str, "Clusters": List[ClientDescribeClustersResponseClustersTypeDef]},
    total=False,
)

ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef = TypedDict(
    "ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef = TypedDict(
    "ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef",
    {
        "ParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeDefaultClusterParametersResponseTypeDef = TypedDict(
    "ClientDescribeDefaultClusterParametersResponseTypeDef",
    {
        "DefaultClusterParameters": ClientDescribeDefaultClusterParametersResponseDefaultClusterParametersTypeDef
    },
    total=False,
)

ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef",
    {"EventId": str, "EventCategories": List[str], "EventDescription": str, "Severity": str},
    total=False,
)

ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    {
        "SourceType": str,
        "Events": List[ClientDescribeEventCategoriesResponseEventCategoriesMapListEventsTypeDef],
    },
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

ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTagsTypeDef],
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

ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Severity": str,
        "Date": datetime,
        "EventId": str,
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef = TypedDict(
    "ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef = TypedDict(
    "ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List[ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTagsTypeDef],
    },
    total=False,
)

ClientDescribeHsmClientCertificatesResponseTypeDef = TypedDict(
    "ClientDescribeHsmClientCertificatesResponseTypeDef",
    {
        "Marker": str,
        "HsmClientCertificates": List[
            ClientDescribeHsmClientCertificatesResponseHsmClientCertificatesTypeDef
        ],
    },
    total=False,
)

ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef = TypedDict(
    "ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef = TypedDict(
    "ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List[ClientDescribeHsmConfigurationsResponseHsmConfigurationsTagsTypeDef],
    },
    total=False,
)

ClientDescribeHsmConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeHsmConfigurationsResponseTypeDef",
    {
        "Marker": str,
        "HsmConfigurations": List[ClientDescribeHsmConfigurationsResponseHsmConfigurationsTypeDef],
    },
    total=False,
)

ClientDescribeLoggingStatusResponseTypeDef = TypedDict(
    "ClientDescribeLoggingStatusResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientDescribeNodeConfigurationOptionsFiltersTypeDef = TypedDict(
    "ClientDescribeNodeConfigurationOptionsFiltersTypeDef",
    {
        "Name": Literal["NodeType", "NumberOfNodes", "EstimatedDiskUtilizationPercent", "Mode"],
        "Operator": Literal["eq", "lt", "gt", "le", "ge", "in", "between"],
        "Values": List[str],
    },
    total=False,
)

ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef = TypedDict(
    "ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": Literal["standard", "high-performance"],
    },
    total=False,
)

ClientDescribeNodeConfigurationOptionsResponseTypeDef = TypedDict(
    "ClientDescribeNodeConfigurationOptionsResponseTypeDef",
    {
        "NodeConfigurationOptionList": List[
            ClientDescribeNodeConfigurationOptionsResponseNodeConfigurationOptionListTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef = TypedDict(
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef = TypedDict(
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesSupportedPlatformsTypeDef
        ],
    },
    total=False,
)

ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef = TypedDict(
    "ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List[
            ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsAvailabilityZonesTypeDef
        ],
    },
    total=False,
)

ClientDescribeOrderableClusterOptionsResponseTypeDef = TypedDict(
    "ClientDescribeOrderableClusterOptionsResponseTypeDef",
    {
        "OrderableClusterOptions": List[
            ClientDescribeOrderableClusterOptionsResponseOrderableClusterOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef = TypedDict(
    "ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ClientDescribeReservedNodeOfferingsResponseTypeDef = TypedDict(
    "ClientDescribeReservedNodeOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List[
            ClientDescribeReservedNodeOfferingsResponseReservedNodeOfferingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedNodesResponseReservedNodesTypeDef = TypedDict(
    "ClientDescribeReservedNodesResponseReservedNodesTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedNodesResponseReservedNodesRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ClientDescribeReservedNodesResponseTypeDef = TypedDict(
    "ClientDescribeReservedNodesResponseTypeDef",
    {"Marker": str, "ReservedNodes": List[ClientDescribeReservedNodesResponseReservedNodesTypeDef]},
    total=False,
)

ClientDescribeResizeResponseTypeDef = TypedDict(
    "ClientDescribeResizeResponseTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
    },
    total=False,
)

_RequiredClientDescribeScheduledActionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeScheduledActionsFiltersTypeDef",
    {"Name": Literal["cluster-identifier", "iam-role"]},
)
_OptionalClientDescribeScheduledActionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeScheduledActionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeScheduledActionsFiltersTypeDef(
    _RequiredClientDescribeScheduledActionsFiltersTypeDef,
    _OptionalClientDescribeScheduledActionsFiltersTypeDef,
):
    pass


ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef",
    {
        "ResizeCluster": ClientDescribeScheduledActionsResponseScheduledActionsTargetActionResizeClusterTypeDef
    },
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledActionsTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ClientDescribeScheduledActionsResponseScheduledActionsTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseTypeDef",
    {
        "Marker": str,
        "ScheduledActions": List[ClientDescribeScheduledActionsResponseScheduledActionsTypeDef],
    },
    total=False,
)

ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef = TypedDict(
    "ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef = TypedDict(
    "ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List[ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTagsTypeDef],
    },
    total=False,
)

ClientDescribeSnapshotCopyGrantsResponseTypeDef = TypedDict(
    "ClientDescribeSnapshotCopyGrantsResponseTypeDef",
    {
        "Marker": str,
        "SnapshotCopyGrants": List[
            ClientDescribeSnapshotCopyGrantsResponseSnapshotCopyGrantsTypeDef
        ],
    },
    total=False,
)

ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef = TypedDict(
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)

ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef = TypedDict(
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef = TypedDict(
    "ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[
            ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesAssociatedClustersTypeDef
        ],
    },
    total=False,
)

ClientDescribeSnapshotSchedulesResponseTypeDef = TypedDict(
    "ClientDescribeSnapshotSchedulesResponseTypeDef",
    {
        "SnapshotSchedules": List[ClientDescribeSnapshotSchedulesResponseSnapshotSchedulesTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeStorageResponseTypeDef = TypedDict(
    "ClientDescribeStorageResponseTypeDef",
    {"TotalBackupSizeInMegaBytes": float, "TotalProvisionedStorageInMegaBytes": float},
    total=False,
)

ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef = TypedDict(
    "ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)

ClientDescribeTableRestoreStatusResponseTypeDef = TypedDict(
    "ClientDescribeTableRestoreStatusResponseTypeDef",
    {
        "TableRestoreStatusDetails": List[
            ClientDescribeTableRestoreStatusResponseTableRestoreStatusDetailsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeTagsResponseTaggedResourcesTagTypeDef = TypedDict(
    "ClientDescribeTagsResponseTaggedResourcesTagTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTaggedResourcesTypeDef = TypedDict(
    "ClientDescribeTagsResponseTaggedResourcesTypeDef",
    {
        "Tag": ClientDescribeTagsResponseTaggedResourcesTagTypeDef,
        "ResourceName": str,
        "ResourceType": str,
    },
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"TaggedResources": List[ClientDescribeTagsResponseTaggedResourcesTypeDef], "Marker": str},
    total=False,
)

ClientDisableLoggingResponseTypeDef = TypedDict(
    "ClientDisableLoggingResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterEndpointTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseClusterTagsTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDisableSnapshotCopyResponseClusterTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDisableSnapshotCopyResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientDisableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientDisableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientDisableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDisableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientDisableSnapshotCopyResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientDisableSnapshotCopyResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientDisableSnapshotCopyResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientDisableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientDisableSnapshotCopyResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientDisableSnapshotCopyResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientDisableSnapshotCopyResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientDisableSnapshotCopyResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientDisableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientDisableSnapshotCopyResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientDisableSnapshotCopyResponseTypeDef = TypedDict(
    "ClientDisableSnapshotCopyResponseTypeDef",
    {"Cluster": ClientDisableSnapshotCopyResponseClusterTypeDef},
    total=False,
)

ClientEnableLoggingResponseTypeDef = TypedDict(
    "ClientEnableLoggingResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterEndpointTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseClusterTagsTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientEnableSnapshotCopyResponseClusterTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientEnableSnapshotCopyResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientEnableSnapshotCopyResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientEnableSnapshotCopyResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientEnableSnapshotCopyResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientEnableSnapshotCopyResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientEnableSnapshotCopyResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientEnableSnapshotCopyResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientEnableSnapshotCopyResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientEnableSnapshotCopyResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientEnableSnapshotCopyResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientEnableSnapshotCopyResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientEnableSnapshotCopyResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientEnableSnapshotCopyResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientEnableSnapshotCopyResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientEnableSnapshotCopyResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientEnableSnapshotCopyResponseTypeDef = TypedDict(
    "ClientEnableSnapshotCopyResponseTypeDef",
    {"Cluster": ClientEnableSnapshotCopyResponseClusterTypeDef},
    total=False,
)

ClientGetClusterCredentialsResponseTypeDef = TypedDict(
    "ClientGetClusterCredentialsResponseTypeDef",
    {"DbUser": str, "DbPassword": str, "Expiration": datetime},
    total=False,
)

ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef = TypedDict(
    "ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef = TypedDict(
    "ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ClientGetReservedNodeExchangeOfferingsResponseTypeDef = TypedDict(
    "ClientGetReservedNodeExchangeOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List[
            ClientGetReservedNodeExchangeOfferingsResponseReservedNodeOfferingsTypeDef
        ],
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterTagsTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyClusterDbRevisionResponseClusterTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterDbRevisionResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterDbRevisionResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyClusterDbRevisionResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifyClusterDbRevisionResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterDbRevisionResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterDbRevisionResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterDbRevisionResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterDbRevisionResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterDbRevisionResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterDbRevisionResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterDbRevisionResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterDbRevisionResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterDbRevisionResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterDbRevisionResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterDbRevisionResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientModifyClusterDbRevisionResponseTypeDef = TypedDict(
    "ClientModifyClusterDbRevisionResponseTypeDef",
    {"Cluster": ClientModifyClusterDbRevisionResponseClusterTypeDef},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterEndpointTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientModifyClusterIamRolesResponseClusterTagsTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyClusterIamRolesResponseClusterTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterIamRolesResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterIamRolesResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyClusterIamRolesResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifyClusterIamRolesResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterIamRolesResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterIamRolesResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterIamRolesResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterIamRolesResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterIamRolesResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterIamRolesResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterIamRolesResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterIamRolesResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterIamRolesResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterIamRolesResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterIamRolesResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientModifyClusterIamRolesResponseTypeDef = TypedDict(
    "ClientModifyClusterIamRolesResponseTypeDef",
    {"Cluster": ClientModifyClusterIamRolesResponseClusterTypeDef},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterTagsTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyClusterMaintenanceResponseClusterTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterMaintenanceResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterMaintenanceResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyClusterMaintenanceResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifyClusterMaintenanceResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterMaintenanceResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterMaintenanceResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterMaintenanceResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterMaintenanceResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterMaintenanceResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterMaintenanceResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterMaintenanceResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterMaintenanceResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterMaintenanceResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterMaintenanceResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterMaintenanceResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientModifyClusterMaintenanceResponseTypeDef = TypedDict(
    "ClientModifyClusterMaintenanceResponseTypeDef",
    {"Cluster": ClientModifyClusterMaintenanceResponseClusterTypeDef},
    total=False,
)

ClientModifyClusterParameterGroupParametersTypeDef = TypedDict(
    "ClientModifyClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ClientModifyClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientModifyClusterParameterGroupResponseTypeDef",
    {"ParameterGroupName": str, "ParameterGroupStatus": str},
    total=False,
)

ClientModifyClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifyClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientModifyClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientModifyClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientModifyClusterResponseClusterEndpointTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)

ClientModifyClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientModifyClusterResponseClusterIamRolesTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientModifyClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientModifyClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientModifyClusterResponseClusterTagsTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyClusterResponseClusterTypeDef = TypedDict(
    "ClientModifyClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifyClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientModifyClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientModifyClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifyClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifyClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifyClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifyClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientModifyClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientModifyClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifyClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifyClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifyClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifyClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientModifyClusterResponseTypeDef = TypedDict(
    "ClientModifyClusterResponseTypeDef",
    {"Cluster": ClientModifyClusterResponseClusterTypeDef},
    total=False,
)

ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef = TypedDict(
    "ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyClusterSnapshotResponseSnapshotTypeDef = TypedDict(
    "ClientModifyClusterSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientModifyClusterSnapshotResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientModifyClusterSnapshotResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientModifyClusterSnapshotResponseTypeDef = TypedDict(
    "ClientModifyClusterSnapshotResponseTypeDef",
    {"Snapshot": ClientModifyClusterSnapshotResponseSnapshotTypeDef},
    total=False,
)

ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef = TypedDict(
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List[
            ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneSupportedPlatformsTypeDef
        ],
    },
    total=False,
)

ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef = TypedDict(
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef = TypedDict(
    "ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyClusterSubnetGroupResponseClusterSubnetGroupSubnetsTypeDef],
        "Tags": List[ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTagsTypeDef],
    },
    total=False,
)

ClientModifyClusterSubnetGroupResponseTypeDef = TypedDict(
    "ClientModifyClusterSubnetGroupResponseTypeDef",
    {"ClusterSubnetGroup": ClientModifyClusterSubnetGroupResponseClusterSubnetGroupTypeDef},
    total=False,
)

ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[ClientModifyEventSubscriptionResponseEventSubscriptionTagsTypeDef],
    },
    total=False,
)

ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef = TypedDict(
    "ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)

ClientModifyScheduledActionResponseTargetActionTypeDef = TypedDict(
    "ClientModifyScheduledActionResponseTargetActionTypeDef",
    {"ResizeCluster": ClientModifyScheduledActionResponseTargetActionResizeClusterTypeDef},
    total=False,
)

ClientModifyScheduledActionResponseTypeDef = TypedDict(
    "ClientModifyScheduledActionResponseTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ClientModifyScheduledActionResponseTargetActionTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

_RequiredClientModifyScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_RequiredClientModifyScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterIdentifier": str},
)
_OptionalClientModifyScheduledActionTargetActionResizeClusterTypeDef = TypedDict(
    "_OptionalClientModifyScheduledActionTargetActionResizeClusterTypeDef",
    {"ClusterType": str, "NodeType": str, "NumberOfNodes": int, "Classic": bool},
    total=False,
)


class ClientModifyScheduledActionTargetActionResizeClusterTypeDef(
    _RequiredClientModifyScheduledActionTargetActionResizeClusterTypeDef,
    _OptionalClientModifyScheduledActionTargetActionResizeClusterTypeDef,
):
    pass


ClientModifyScheduledActionTargetActionTypeDef = TypedDict(
    "ClientModifyScheduledActionTargetActionTypeDef",
    {"ResizeCluster": ClientModifyScheduledActionTargetActionResizeClusterTypeDef},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifySnapshotCopyRetentionPeriodResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifySnapshotCopyRetentionPeriodResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientModifySnapshotCopyRetentionPeriodResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterClusterNodesTypeDef
        ],
        "ElasticIpStatus": ClientModifySnapshotCopyRetentionPeriodResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientModifySnapshotCopyRetentionPeriodResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientModifySnapshotCopyRetentionPeriodResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientModifySnapshotCopyRetentionPeriodResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientModifySnapshotCopyRetentionPeriodResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientModifySnapshotCopyRetentionPeriodResponseTypeDef = TypedDict(
    "ClientModifySnapshotCopyRetentionPeriodResponseTypeDef",
    {"Cluster": ClientModifySnapshotCopyRetentionPeriodResponseClusterTypeDef},
    total=False,
)

ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef = TypedDict(
    "ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)

ClientModifySnapshotScheduleResponseTagsTypeDef = TypedDict(
    "ClientModifySnapshotScheduleResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientModifySnapshotScheduleResponseTypeDef = TypedDict(
    "ClientModifySnapshotScheduleResponseTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[ClientModifySnapshotScheduleResponseTagsTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[ClientModifySnapshotScheduleResponseAssociatedClustersTypeDef],
    },
    total=False,
)

ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef = TypedDict(
    "ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef = TypedDict(
    "ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientPurchaseReservedNodeOfferingResponseReservedNodeRecurringChargesTypeDef
        ],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ClientPurchaseReservedNodeOfferingResponseTypeDef = TypedDict(
    "ClientPurchaseReservedNodeOfferingResponseTypeDef",
    {"ReservedNode": ClientPurchaseReservedNodeOfferingResponseReservedNodeTypeDef},
    total=False,
)

ClientRebootClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientRebootClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientRebootClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientRebootClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientRebootClusterResponseClusterEndpointTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)

ClientRebootClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientRebootClusterResponseClusterIamRolesTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientRebootClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientRebootClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientRebootClusterResponseClusterTagsTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRebootClusterResponseClusterTypeDef = TypedDict(
    "ClientRebootClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRebootClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientRebootClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientRebootClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientRebootClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientRebootClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientRebootClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientRebootClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientRebootClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientRebootClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientRebootClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientRebootClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientRebootClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientRebootClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientRebootClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientRebootClusterResponseTypeDef = TypedDict(
    "ClientRebootClusterResponseTypeDef",
    {"Cluster": ClientRebootClusterResponseClusterTypeDef},
    total=False,
)

ClientResetClusterParameterGroupParametersTypeDef = TypedDict(
    "ClientResetClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ClientResetClusterParameterGroupResponseTypeDef = TypedDict(
    "ClientResetClusterParameterGroupResponseTypeDef",
    {"ParameterGroupName": str, "ParameterGroupStatus": str},
    total=False,
)

ClientResizeClusterResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientResizeClusterResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientResizeClusterResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientResizeClusterResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientResizeClusterResponseClusterEndpointTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)

ClientResizeClusterResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientResizeClusterResponseClusterIamRolesTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientResizeClusterResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientResizeClusterResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientResizeClusterResponseClusterTagsTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientResizeClusterResponseClusterTypeDef = TypedDict(
    "ClientResizeClusterResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientResizeClusterResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientResizeClusterResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientResizeClusterResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientResizeClusterResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientResizeClusterResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientResizeClusterResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientResizeClusterResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientResizeClusterResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientResizeClusterResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientResizeClusterResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientResizeClusterResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientResizeClusterResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientResizeClusterResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientResizeClusterResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientResizeClusterResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientResizeClusterResponseTypeDef = TypedDict(
    "ClientResizeClusterResponseTypeDef",
    {"Cluster": ClientResizeClusterResponseClusterTypeDef},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRestoreFromClusterSnapshotResponseClusterTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRestoreFromClusterSnapshotResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientRestoreFromClusterSnapshotResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreFromClusterSnapshotResponseClusterVpcSecurityGroupsTypeDef
        ],
        "ClusterParameterGroups": List[
            ClientRestoreFromClusterSnapshotResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRestoreFromClusterSnapshotResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientRestoreFromClusterSnapshotResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientRestoreFromClusterSnapshotResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientRestoreFromClusterSnapshotResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientRestoreFromClusterSnapshotResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientRestoreFromClusterSnapshotResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientRestoreFromClusterSnapshotResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientRestoreFromClusterSnapshotResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientRestoreFromClusterSnapshotResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientRestoreFromClusterSnapshotResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientRestoreFromClusterSnapshotResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientRestoreFromClusterSnapshotResponseTypeDef = TypedDict(
    "ClientRestoreFromClusterSnapshotResponseTypeDef",
    {"Cluster": ClientRestoreFromClusterSnapshotResponseClusterTypeDef},
    total=False,
)

ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef = TypedDict(
    "ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)

ClientRestoreTableFromClusterSnapshotResponseTypeDef = TypedDict(
    "ClientRestoreTableFromClusterSnapshotResponseTypeDef",
    {"TableRestoreStatus": ClientRestoreTableFromClusterSnapshotResponseTableRestoreStatusTypeDef},
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTagsTypeDef
        ],
    },
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTagsTypeDef
        ],
    },
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupEC2SecurityGroupsTypeDef
        ],
        "IPRanges": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupIPRangesTypeDef
        ],
        "Tags": List[
            ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTagsTypeDef
        ],
    },
    total=False,
)

ClientRevokeClusterSecurityGroupIngressResponseTypeDef = TypedDict(
    "ClientRevokeClusterSecurityGroupIngressResponseTypeDef",
    {
        "ClusterSecurityGroup": ClientRevokeClusterSecurityGroupIngressResponseClusterSecurityGroupTypeDef
    },
    total=False,
)

ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef = TypedDict(
    "ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef",
    {"AccountId": str, "AccountAlias": str},
    total=False,
)

ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef = TypedDict(
    "ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRevokeSnapshotAccessResponseSnapshotTypeDef = TypedDict(
    "ClientRevokeSnapshotAccessResponseSnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[
            ClientRevokeSnapshotAccessResponseSnapshotAccountsWithRestoreAccessTypeDef
        ],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[ClientRevokeSnapshotAccessResponseSnapshotTagsTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

ClientRevokeSnapshotAccessResponseTypeDef = TypedDict(
    "ClientRevokeSnapshotAccessResponseTypeDef",
    {"Snapshot": ClientRevokeSnapshotAccessResponseSnapshotTypeDef},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[
            ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsClusterParameterStatusListTypeDef
        ],
    },
    total=False,
)

ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef",
    {"ElasticIp": str, "Status": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterEndpointTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef",
    {"IamRoleArn": str, "ApplyStatus": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef",
    {"ResizeType": str, "AllowCancelResize": bool},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ClientRotateEncryptionKeyResponseClusterTagsTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRotateEncryptionKeyResponseClusterTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRotateEncryptionKeyResponseClusterEndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[
            ClientRotateEncryptionKeyResponseClusterClusterSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[ClientRotateEncryptionKeyResponseClusterVpcSecurityGroupsTypeDef],
        "ClusterParameterGroups": List[
            ClientRotateEncryptionKeyResponseClusterClusterParameterGroupsTypeDef
        ],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRotateEncryptionKeyResponseClusterPendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": ClientRotateEncryptionKeyResponseClusterRestoreStatusTypeDef,
        "DataTransferProgress": ClientRotateEncryptionKeyResponseClusterDataTransferProgressTypeDef,
        "HsmStatus": ClientRotateEncryptionKeyResponseClusterHsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClientRotateEncryptionKeyResponseClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClientRotateEncryptionKeyResponseClusterClusterNodesTypeDef],
        "ElasticIpStatus": ClientRotateEncryptionKeyResponseClusterElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[ClientRotateEncryptionKeyResponseClusterTagsTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClientRotateEncryptionKeyResponseClusterIamRolesTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[
            ClientRotateEncryptionKeyResponseClusterDeferredMaintenanceWindowsTypeDef
        ],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ClientRotateEncryptionKeyResponseClusterResizeInfoTypeDef,
    },
    total=False,
)

ClientRotateEncryptionKeyResponseTypeDef = TypedDict(
    "ClientRotateEncryptionKeyResponseTypeDef",
    {"Cluster": ClientRotateEncryptionKeyResponseClusterTypeDef},
    total=False,
)

RevisionTargetTypeDef = TypedDict(
    "RevisionTargetTypeDef",
    {"DatabaseRevision": str, "Description": str, "DatabaseRevisionReleaseDate": datetime},
    total=False,
)

ClusterDbRevisionTypeDef = TypedDict(
    "ClusterDbRevisionTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List[RevisionTargetTypeDef],
    },
    total=False,
)

ClusterDbRevisionsMessageTypeDef = TypedDict(
    "ClusterDbRevisionsMessageTypeDef",
    {"Marker": str, "ClusterDbRevisions": List[ClusterDbRevisionTypeDef]},
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
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ClusterParameterGroupDetailsTypeDef = TypedDict(
    "ClusterParameterGroupDetailsTypeDef",
    {"Parameters": List[ParameterTypeDef], "Marker": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

ClusterParameterGroupTypeDef = TypedDict(
    "ClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

ClusterParameterGroupsMessageTypeDef = TypedDict(
    "ClusterParameterGroupsMessageTypeDef",
    {"Marker": str, "ParameterGroups": List[ClusterParameterGroupTypeDef]},
    total=False,
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef", {"Status": str, "CIDRIP": str, "Tags": List[TagTypeDef]}, total=False
)

ClusterSecurityGroupTypeDef = TypedDict(
    "ClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[EC2SecurityGroupTypeDef],
        "IPRanges": List[IPRangeTypeDef],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

ClusterSecurityGroupMessageTypeDef = TypedDict(
    "ClusterSecurityGroupMessageTypeDef",
    {"Marker": str, "ClusterSecurityGroups": List[ClusterSecurityGroupTypeDef]},
    total=False,
)

SupportedPlatformTypeDef = TypedDict("SupportedPlatformTypeDef", {"Name": str}, total=False)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {"Name": str, "SupportedPlatforms": List[SupportedPlatformTypeDef]},
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": AvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClusterSubnetGroupTypeDef = TypedDict(
    "ClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[SubnetTypeDef],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

ClusterSubnetGroupMessageTypeDef = TypedDict(
    "ClusterSubnetGroupMessageTypeDef",
    {"Marker": str, "ClusterSubnetGroups": List[ClusterSubnetGroupTypeDef]},
    total=False,
)

ClusterVersionTypeDef = TypedDict(
    "ClusterVersionTypeDef",
    {"ClusterVersion": str, "ClusterParameterGroupFamily": str, "Description": str},
    total=False,
)

ClusterVersionsMessageTypeDef = TypedDict(
    "ClusterVersionsMessageTypeDef",
    {"Marker": str, "ClusterVersions": List[ClusterVersionTypeDef]},
    total=False,
)

ClusterIamRoleTypeDef = TypedDict(
    "ClusterIamRoleTypeDef", {"IamRoleArn": str, "ApplyStatus": str}, total=False
)

ClusterNodeTypeDef = TypedDict(
    "ClusterNodeTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClusterParameterStatusTypeDef = TypedDict(
    "ClusterParameterStatusTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClusterParameterGroupStatusTypeDef = TypedDict(
    "ClusterParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List[ClusterParameterStatusTypeDef],
    },
    total=False,
)

ClusterSecurityGroupMembershipTypeDef = TypedDict(
    "ClusterSecurityGroupMembershipTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

DataTransferProgressTypeDef = TypedDict(
    "DataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

DeferredMaintenanceWindowTypeDef = TypedDict(
    "DeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

ElasticIpStatusTypeDef = TypedDict(
    "ElasticIpStatusTypeDef", {"ElasticIp": str, "Status": str}, total=False
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "Port": int}, total=False)

HsmStatusTypeDef = TypedDict(
    "HsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

ResizeInfoTypeDef = TypedDict(
    "ResizeInfoTypeDef", {"ResizeType": str, "AllowCancelResize": bool}, total=False
)

RestoreStatusTypeDef = TypedDict(
    "RestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef", {"VpcSecurityGroupId": str, "Status": str}, total=False
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": EndpointTypeDef,
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List[ClusterSecurityGroupMembershipTypeDef],
        "VpcSecurityGroups": List[VpcSecurityGroupMembershipTypeDef],
        "ClusterParameterGroups": List[ClusterParameterGroupStatusTypeDef],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": PendingModifiedValuesTypeDef,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": RestoreStatusTypeDef,
        "DataTransferProgress": DataTransferProgressTypeDef,
        "HsmStatus": HsmStatusTypeDef,
        "ClusterSnapshotCopyStatus": ClusterSnapshotCopyStatusTypeDef,
        "ClusterPublicKey": str,
        "ClusterNodes": List[ClusterNodeTypeDef],
        "ElasticIpStatus": ElasticIpStatusTypeDef,
        "ClusterRevisionNumber": str,
        "Tags": List[TagTypeDef],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List[ClusterIamRoleTypeDef],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List[DeferredMaintenanceWindowTypeDef],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": ResizeInfoTypeDef,
    },
    total=False,
)

ClustersMessageTypeDef = TypedDict(
    "ClustersMessageTypeDef", {"Marker": str, "Clusters": List[ClusterTypeDef]}, total=False
)

DefaultClusterParametersTypeDef = TypedDict(
    "DefaultClusterParametersTypeDef",
    {"ParameterGroupFamily": str, "Marker": str, "Parameters": List[ParameterTypeDef]},
    total=False,
)

DescribeDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeDefaultClusterParametersResultTypeDef",
    {"DefaultClusterParameters": DefaultClusterParametersTypeDef},
    total=False,
)

ClusterAssociatedToScheduleTypeDef = TypedDict(
    "ClusterAssociatedToScheduleTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)

SnapshotScheduleTypeDef = TypedDict(
    "SnapshotScheduleTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List[TagTypeDef],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List[ClusterAssociatedToScheduleTypeDef],
    },
    total=False,
)

DescribeSnapshotSchedulesOutputMessageTypeDef = TypedDict(
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    {"SnapshotSchedules": List[SnapshotScheduleTypeDef], "Marker": str},
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List[TagTypeDef],
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
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Severity": str,
        "Date": datetime,
        "EventId": str,
    },
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef", {"Marker": str, "Events": List[EventTypeDef]}, total=False
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedNodeOfferingTypeDef = TypedDict(
    "ReservedNodeOfferingTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List[RecurringChargeTypeDef],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

GetReservedNodeExchangeOfferingsOutputMessageTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    {"Marker": str, "ReservedNodeOfferings": List[ReservedNodeOfferingTypeDef]},
    total=False,
)

HsmClientCertificateTypeDef = TypedDict(
    "HsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

HsmClientCertificateMessageTypeDef = TypedDict(
    "HsmClientCertificateMessageTypeDef",
    {"Marker": str, "HsmClientCertificates": List[HsmClientCertificateTypeDef]},
    total=False,
)

HsmConfigurationTypeDef = TypedDict(
    "HsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

HsmConfigurationMessageTypeDef = TypedDict(
    "HsmConfigurationMessageTypeDef",
    {"Marker": str, "HsmConfigurations": List[HsmConfigurationTypeDef]},
    total=False,
)

NodeConfigurationOptionsFilterTypeDef = TypedDict(
    "NodeConfigurationOptionsFilterTypeDef",
    {
        "Name": Literal["NodeType", "NumberOfNodes", "EstimatedDiskUtilizationPercent", "Mode"],
        "Operator": Literal["eq", "lt", "gt", "le", "ge", "in", "between"],
        "Values": List[str],
    },
    total=False,
)

NodeConfigurationOptionTypeDef = TypedDict(
    "NodeConfigurationOptionTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": Literal["standard", "high-performance"],
    },
    total=False,
)

NodeConfigurationOptionsMessageTypeDef = TypedDict(
    "NodeConfigurationOptionsMessageTypeDef",
    {"NodeConfigurationOptionList": List[NodeConfigurationOptionTypeDef], "Marker": str},
    total=False,
)

OrderableClusterOptionTypeDef = TypedDict(
    "OrderableClusterOptionTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
    },
    total=False,
)

OrderableClusterOptionsMessageTypeDef = TypedDict(
    "OrderableClusterOptionsMessageTypeDef",
    {"OrderableClusterOptions": List[OrderableClusterOptionTypeDef], "Marker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReservedNodeOfferingsMessageTypeDef = TypedDict(
    "ReservedNodeOfferingsMessageTypeDef",
    {"Marker": str, "ReservedNodeOfferings": List[ReservedNodeOfferingTypeDef]},
    total=False,
)

ReservedNodeTypeDef = TypedDict(
    "ReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List[RecurringChargeTypeDef],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ReservedNodesMessageTypeDef = TypedDict(
    "ReservedNodesMessageTypeDef",
    {"Marker": str, "ReservedNodes": List[ReservedNodeTypeDef]},
    total=False,
)

ScheduledActionFilterTypeDef = TypedDict(
    "ScheduledActionFilterTypeDef",
    {"Name": Literal["cluster-identifier", "iam-role"], "Values": List[str]},
)

_RequiredResizeClusterMessageTypeDef = TypedDict(
    "_RequiredResizeClusterMessageTypeDef", {"ClusterIdentifier": str, "NumberOfNodes": int}
)
_OptionalResizeClusterMessageTypeDef = TypedDict(
    "_OptionalResizeClusterMessageTypeDef",
    {"ClusterType": str, "NodeType": str, "Classic": bool},
    total=False,
)


class ResizeClusterMessageTypeDef(
    _RequiredResizeClusterMessageTypeDef, _OptionalResizeClusterMessageTypeDef
):
    pass


ScheduledActionTypeTypeDef = TypedDict(
    "ScheduledActionTypeTypeDef", {"ResizeCluster": ResizeClusterMessageTypeDef}, total=False
)

ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": ScheduledActionTypeTypeDef,
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ScheduledActionsMessageTypeDef = TypedDict(
    "ScheduledActionsMessageTypeDef",
    {"Marker": str, "ScheduledActions": List[ScheduledActionTypeDef]},
    total=False,
)

SnapshotCopyGrantTypeDef = TypedDict(
    "SnapshotCopyGrantTypeDef",
    {"SnapshotCopyGrantName": str, "KmsKeyId": str, "Tags": List[TagTypeDef]},
    total=False,
)

SnapshotCopyGrantMessageTypeDef = TypedDict(
    "SnapshotCopyGrantMessageTypeDef",
    {"Marker": str, "SnapshotCopyGrants": List[SnapshotCopyGrantTypeDef]},
    total=False,
)

AccountWithRestoreAccessTypeDef = TypedDict(
    "AccountWithRestoreAccessTypeDef", {"AccountId": str, "AccountAlias": str}, total=False
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List[AccountWithRestoreAccessTypeDef],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List[TagTypeDef],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
)

SnapshotMessageTypeDef = TypedDict(
    "SnapshotMessageTypeDef", {"Marker": str, "Snapshots": List[SnapshotTypeDef]}, total=False
)

_RequiredSnapshotSortingEntityTypeDef = TypedDict(
    "_RequiredSnapshotSortingEntityTypeDef",
    {"Attribute": Literal["SOURCE_TYPE", "TOTAL_SIZE", "CREATE_TIME"]},
)
_OptionalSnapshotSortingEntityTypeDef = TypedDict(
    "_OptionalSnapshotSortingEntityTypeDef", {"SortOrder": Literal["ASC", "DESC"]}, total=False
)


class SnapshotSortingEntityTypeDef(
    _RequiredSnapshotSortingEntityTypeDef, _OptionalSnapshotSortingEntityTypeDef
):
    pass


TableRestoreStatusTypeDef = TypedDict(
    "TableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)

TableRestoreStatusMessageTypeDef = TypedDict(
    "TableRestoreStatusMessageTypeDef",
    {"TableRestoreStatusDetails": List[TableRestoreStatusTypeDef], "Marker": str},
    total=False,
)

TaggedResourceTypeDef = TypedDict(
    "TaggedResourceTypeDef",
    {"Tag": TagTypeDef, "ResourceName": str, "ResourceType": str},
    total=False,
)

TaggedResourceListMessageTypeDef = TypedDict(
    "TaggedResourceListMessageTypeDef",
    {"TaggedResources": List[TaggedResourceTypeDef], "Marker": str},
    total=False,
)

SupportedOperationTypeDef = TypedDict(
    "SupportedOperationTypeDef", {"OperationName": str}, total=False
)

UpdateTargetTypeDef = TypedDict(
    "UpdateTargetTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List[SupportedOperationTypeDef],
    },
    total=False,
)

MaintenanceTrackTypeDef = TypedDict(
    "MaintenanceTrackTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List[UpdateTargetTypeDef],
    },
    total=False,
)

TrackListMessageTypeDef = TypedDict(
    "TrackListMessageTypeDef",
    {"MaintenanceTracks": List[MaintenanceTrackTypeDef], "Marker": str},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
