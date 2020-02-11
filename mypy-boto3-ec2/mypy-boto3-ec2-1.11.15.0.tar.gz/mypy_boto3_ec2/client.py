"""
Main interface for ec2 service client

Usage::

    import boto3
    from mypy_boto3.ec2 import EC2Client

    session = boto3.Session()

    client: EC2Client = boto3.client("ec2")
    session_client: EC2Client = session.client("ec2")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ec2.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ec2.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ec2.type_defs import (
    ClientAcceptReservedInstancesExchangeQuoteResponseTypeDef,
    ClientAcceptReservedInstancesExchangeQuoteTargetConfigurationsTypeDef,
    ClientAcceptTransitGatewayPeeringAttachmentResponseTypeDef,
    ClientAcceptTransitGatewayVpcAttachmentResponseTypeDef,
    ClientAcceptVpcEndpointConnectionsResponseTypeDef,
    ClientAcceptVpcPeeringConnectionResponseTypeDef,
    ClientAdvertiseByoipCidrResponseTypeDef,
    ClientAllocateAddressResponseTypeDef,
    ClientAllocateHostsResponseTypeDef,
    ClientAllocateHostsTagSpecificationsTypeDef,
    ClientApplySecurityGroupsToClientVpnTargetNetworkResponseTypeDef,
    ClientAssignIpv6AddressesResponseTypeDef,
    ClientAssignPrivateIpAddressesResponseTypeDef,
    ClientAssociateAddressResponseTypeDef,
    ClientAssociateClientVpnTargetNetworkResponseTypeDef,
    ClientAssociateIamInstanceProfileIamInstanceProfileTypeDef,
    ClientAssociateIamInstanceProfileResponseTypeDef,
    ClientAssociateRouteTableResponseTypeDef,
    ClientAssociateSubnetCidrBlockResponseTypeDef,
    ClientAssociateTransitGatewayMulticastDomainResponseTypeDef,
    ClientAssociateTransitGatewayRouteTableResponseTypeDef,
    ClientAssociateVpcCidrBlockResponseTypeDef,
    ClientAttachClassicLinkVpcResponseTypeDef,
    ClientAttachNetworkInterfaceResponseTypeDef,
    ClientAttachVolumeResponseTypeDef,
    ClientAttachVpnGatewayResponseTypeDef,
    ClientAuthorizeClientVpnIngressResponseTypeDef,
    ClientAuthorizeSecurityGroupEgressIpPermissionsTypeDef,
    ClientAuthorizeSecurityGroupIngressIpPermissionsTypeDef,
    ClientBundleInstanceResponseTypeDef,
    ClientBundleInstanceStorageTypeDef,
    ClientCancelBundleTaskResponseTypeDef,
    ClientCancelCapacityReservationResponseTypeDef,
    ClientCancelImportTaskResponseTypeDef,
    ClientCancelReservedInstancesListingResponseTypeDef,
    ClientCancelSpotFleetRequestsResponseTypeDef,
    ClientCancelSpotInstanceRequestsResponseTypeDef,
    ClientConfirmProductInstanceResponseTypeDef,
    ClientCopyFpgaImageResponseTypeDef,
    ClientCopyImageResponseTypeDef,
    ClientCopySnapshotResponseTypeDef,
    ClientCopySnapshotTagSpecificationsTypeDef,
    ClientCreateCapacityReservationResponseTypeDef,
    ClientCreateCapacityReservationTagSpecificationsTypeDef,
    ClientCreateClientVpnEndpointAuthenticationOptionsTypeDef,
    ClientCreateClientVpnEndpointConnectionLogOptionsTypeDef,
    ClientCreateClientVpnEndpointResponseTypeDef,
    ClientCreateClientVpnEndpointTagSpecificationsTypeDef,
    ClientCreateClientVpnRouteResponseTypeDef,
    ClientCreateCustomerGatewayResponseTypeDef,
    ClientCreateDefaultSubnetResponseTypeDef,
    ClientCreateDefaultVpcResponseTypeDef,
    ClientCreateDhcpOptionsDhcpConfigurationsTypeDef,
    ClientCreateDhcpOptionsResponseTypeDef,
    ClientCreateEgressOnlyInternetGatewayResponseTypeDef,
    ClientCreateFleetLaunchTemplateConfigsTypeDef,
    ClientCreateFleetOnDemandOptionsTypeDef,
    ClientCreateFleetResponseTypeDef,
    ClientCreateFleetSpotOptionsTypeDef,
    ClientCreateFleetTagSpecificationsTypeDef,
    ClientCreateFleetTargetCapacitySpecificationTypeDef,
    ClientCreateFlowLogsResponseTypeDef,
    ClientCreateFpgaImageInputStorageLocationTypeDef,
    ClientCreateFpgaImageLogsStorageLocationTypeDef,
    ClientCreateFpgaImageResponseTypeDef,
    ClientCreateFpgaImageTagSpecificationsTypeDef,
    ClientCreateImageBlockDeviceMappingsTypeDef,
    ClientCreateImageResponseTypeDef,
    ClientCreateInstanceExportTaskExportToS3TaskTypeDef,
    ClientCreateInstanceExportTaskResponseTypeDef,
    ClientCreateInternetGatewayResponseTypeDef,
    ClientCreateKeyPairResponseTypeDef,
    ClientCreateLaunchTemplateLaunchTemplateDataTypeDef,
    ClientCreateLaunchTemplateResponseTypeDef,
    ClientCreateLaunchTemplateTagSpecificationsTypeDef,
    ClientCreateLaunchTemplateVersionLaunchTemplateDataTypeDef,
    ClientCreateLaunchTemplateVersionResponseTypeDef,
    ClientCreateLocalGatewayRouteResponseTypeDef,
    ClientCreateLocalGatewayRouteTableVpcAssociationResponseTypeDef,
    ClientCreateNatGatewayResponseTypeDef,
    ClientCreateNetworkAclEntryIcmpTypeCodeTypeDef,
    ClientCreateNetworkAclEntryPortRangeTypeDef,
    ClientCreateNetworkAclResponseTypeDef,
    ClientCreateNetworkInterfaceIpv6AddressesTypeDef,
    ClientCreateNetworkInterfacePermissionResponseTypeDef,
    ClientCreateNetworkInterfacePrivateIpAddressesTypeDef,
    ClientCreateNetworkInterfaceResponseTypeDef,
    ClientCreateReservedInstancesListingPriceSchedulesTypeDef,
    ClientCreateReservedInstancesListingResponseTypeDef,
    ClientCreateRouteResponseTypeDef,
    ClientCreateRouteTableResponseTypeDef,
    ClientCreateSecurityGroupResponseTypeDef,
    ClientCreateSnapshotResponseTypeDef,
    ClientCreateSnapshotTagSpecificationsTypeDef,
    ClientCreateSnapshotsInstanceSpecificationTypeDef,
    ClientCreateSnapshotsResponseTypeDef,
    ClientCreateSnapshotsTagSpecificationsTypeDef,
    ClientCreateSpotDatafeedSubscriptionResponseTypeDef,
    ClientCreateSubnetResponseTypeDef,
    ClientCreateTagsTagsTypeDef,
    ClientCreateTrafficMirrorFilterResponseTypeDef,
    ClientCreateTrafficMirrorFilterRuleDestinationPortRangeTypeDef,
    ClientCreateTrafficMirrorFilterRuleResponseTypeDef,
    ClientCreateTrafficMirrorFilterRuleSourcePortRangeTypeDef,
    ClientCreateTrafficMirrorFilterTagSpecificationsTypeDef,
    ClientCreateTrafficMirrorSessionResponseTypeDef,
    ClientCreateTrafficMirrorSessionTagSpecificationsTypeDef,
    ClientCreateTrafficMirrorTargetResponseTypeDef,
    ClientCreateTrafficMirrorTargetTagSpecificationsTypeDef,
    ClientCreateTransitGatewayMulticastDomainResponseTypeDef,
    ClientCreateTransitGatewayMulticastDomainTagSpecificationsTypeDef,
    ClientCreateTransitGatewayOptionsTypeDef,
    ClientCreateTransitGatewayPeeringAttachmentResponseTypeDef,
    ClientCreateTransitGatewayPeeringAttachmentTagSpecificationsTypeDef,
    ClientCreateTransitGatewayResponseTypeDef,
    ClientCreateTransitGatewayRouteResponseTypeDef,
    ClientCreateTransitGatewayRouteTableResponseTypeDef,
    ClientCreateTransitGatewayRouteTableTagSpecificationsTypeDef,
    ClientCreateTransitGatewayTagSpecificationsTypeDef,
    ClientCreateTransitGatewayVpcAttachmentOptionsTypeDef,
    ClientCreateTransitGatewayVpcAttachmentResponseTypeDef,
    ClientCreateTransitGatewayVpcAttachmentTagSpecificationsTypeDef,
    ClientCreateVolumeResponseTypeDef,
    ClientCreateVolumeTagSpecificationsTypeDef,
    ClientCreateVpcEndpointConnectionNotificationResponseTypeDef,
    ClientCreateVpcEndpointResponseTypeDef,
    ClientCreateVpcEndpointServiceConfigurationResponseTypeDef,
    ClientCreateVpcEndpointServiceConfigurationTagSpecificationsTypeDef,
    ClientCreateVpcEndpointTagSpecificationsTypeDef,
    ClientCreateVpcPeeringConnectionResponseTypeDef,
    ClientCreateVpcResponseTypeDef,
    ClientCreateVpnConnectionOptionsTypeDef,
    ClientCreateVpnConnectionResponseTypeDef,
    ClientCreateVpnGatewayResponseTypeDef,
    ClientDeleteClientVpnEndpointResponseTypeDef,
    ClientDeleteClientVpnRouteResponseTypeDef,
    ClientDeleteEgressOnlyInternetGatewayResponseTypeDef,
    ClientDeleteFleetsResponseTypeDef,
    ClientDeleteFlowLogsResponseTypeDef,
    ClientDeleteFpgaImageResponseTypeDef,
    ClientDeleteLaunchTemplateResponseTypeDef,
    ClientDeleteLaunchTemplateVersionsResponseTypeDef,
    ClientDeleteLocalGatewayRouteResponseTypeDef,
    ClientDeleteLocalGatewayRouteTableVpcAssociationResponseTypeDef,
    ClientDeleteNatGatewayResponseTypeDef,
    ClientDeleteNetworkInterfacePermissionResponseTypeDef,
    ClientDeleteQueuedReservedInstancesResponseTypeDef,
    ClientDeleteTagsTagsTypeDef,
    ClientDeleteTrafficMirrorFilterResponseTypeDef,
    ClientDeleteTrafficMirrorFilterRuleResponseTypeDef,
    ClientDeleteTrafficMirrorSessionResponseTypeDef,
    ClientDeleteTrafficMirrorTargetResponseTypeDef,
    ClientDeleteTransitGatewayMulticastDomainResponseTypeDef,
    ClientDeleteTransitGatewayPeeringAttachmentResponseTypeDef,
    ClientDeleteTransitGatewayResponseTypeDef,
    ClientDeleteTransitGatewayRouteResponseTypeDef,
    ClientDeleteTransitGatewayRouteTableResponseTypeDef,
    ClientDeleteTransitGatewayVpcAttachmentResponseTypeDef,
    ClientDeleteVpcEndpointConnectionNotificationsResponseTypeDef,
    ClientDeleteVpcEndpointServiceConfigurationsResponseTypeDef,
    ClientDeleteVpcEndpointsResponseTypeDef,
    ClientDeleteVpcPeeringConnectionResponseTypeDef,
    ClientDeprovisionByoipCidrResponseTypeDef,
    ClientDeregisterTransitGatewayMulticastGroupMembersResponseTypeDef,
    ClientDeregisterTransitGatewayMulticastGroupSourcesResponseTypeDef,
    ClientDescribeAccountAttributesResponseTypeDef,
    ClientDescribeAddressesFiltersTypeDef,
    ClientDescribeAddressesResponseTypeDef,
    ClientDescribeAggregateIdFormatResponseTypeDef,
    ClientDescribeAvailabilityZonesFiltersTypeDef,
    ClientDescribeAvailabilityZonesResponseTypeDef,
    ClientDescribeBundleTasksFiltersTypeDef,
    ClientDescribeBundleTasksResponseTypeDef,
    ClientDescribeByoipCidrsResponseTypeDef,
    ClientDescribeCapacityReservationsFiltersTypeDef,
    ClientDescribeCapacityReservationsResponseTypeDef,
    ClientDescribeClassicLinkInstancesFiltersTypeDef,
    ClientDescribeClassicLinkInstancesResponseTypeDef,
    ClientDescribeClientVpnAuthorizationRulesFiltersTypeDef,
    ClientDescribeClientVpnAuthorizationRulesResponseTypeDef,
    ClientDescribeClientVpnConnectionsFiltersTypeDef,
    ClientDescribeClientVpnConnectionsResponseTypeDef,
    ClientDescribeClientVpnEndpointsFiltersTypeDef,
    ClientDescribeClientVpnEndpointsResponseTypeDef,
    ClientDescribeClientVpnRoutesFiltersTypeDef,
    ClientDescribeClientVpnRoutesResponseTypeDef,
    ClientDescribeClientVpnTargetNetworksFiltersTypeDef,
    ClientDescribeClientVpnTargetNetworksResponseTypeDef,
    ClientDescribeCoipPoolsFiltersTypeDef,
    ClientDescribeCoipPoolsResponseTypeDef,
    ClientDescribeConversionTasksResponseTypeDef,
    ClientDescribeCustomerGatewaysFiltersTypeDef,
    ClientDescribeCustomerGatewaysResponseTypeDef,
    ClientDescribeDhcpOptionsFiltersTypeDef,
    ClientDescribeDhcpOptionsResponseTypeDef,
    ClientDescribeEgressOnlyInternetGatewaysFiltersTypeDef,
    ClientDescribeEgressOnlyInternetGatewaysResponseTypeDef,
    ClientDescribeElasticGpusFiltersTypeDef,
    ClientDescribeElasticGpusResponseTypeDef,
    ClientDescribeExportImageTasksFiltersTypeDef,
    ClientDescribeExportImageTasksResponseTypeDef,
    ClientDescribeExportTasksFiltersTypeDef,
    ClientDescribeExportTasksResponseTypeDef,
    ClientDescribeFastSnapshotRestoresFiltersTypeDef,
    ClientDescribeFastSnapshotRestoresResponseTypeDef,
    ClientDescribeFleetHistoryResponseTypeDef,
    ClientDescribeFleetInstancesFiltersTypeDef,
    ClientDescribeFleetInstancesResponseTypeDef,
    ClientDescribeFleetsFiltersTypeDef,
    ClientDescribeFleetsResponseTypeDef,
    ClientDescribeFlowLogsFiltersTypeDef,
    ClientDescribeFlowLogsResponseTypeDef,
    ClientDescribeFpgaImageAttributeResponseTypeDef,
    ClientDescribeFpgaImagesFiltersTypeDef,
    ClientDescribeFpgaImagesResponseTypeDef,
    ClientDescribeHostReservationOfferingsFiltersTypeDef,
    ClientDescribeHostReservationOfferingsResponseTypeDef,
    ClientDescribeHostReservationsFiltersTypeDef,
    ClientDescribeHostReservationsResponseTypeDef,
    ClientDescribeHostsFiltersTypeDef,
    ClientDescribeHostsResponseTypeDef,
    ClientDescribeIamInstanceProfileAssociationsFiltersTypeDef,
    ClientDescribeIamInstanceProfileAssociationsResponseTypeDef,
    ClientDescribeIdFormatResponseTypeDef,
    ClientDescribeIdentityIdFormatResponseTypeDef,
    ClientDescribeImageAttributeResponseTypeDef,
    ClientDescribeImagesFiltersTypeDef,
    ClientDescribeImagesResponseTypeDef,
    ClientDescribeImportImageTasksFiltersTypeDef,
    ClientDescribeImportImageTasksResponseTypeDef,
    ClientDescribeImportSnapshotTasksFiltersTypeDef,
    ClientDescribeImportSnapshotTasksResponseTypeDef,
    ClientDescribeInstanceAttributeResponseTypeDef,
    ClientDescribeInstanceCreditSpecificationsFiltersTypeDef,
    ClientDescribeInstanceCreditSpecificationsResponseTypeDef,
    ClientDescribeInstanceStatusFiltersTypeDef,
    ClientDescribeInstanceStatusResponseTypeDef,
    ClientDescribeInstanceTypeOfferingsFiltersTypeDef,
    ClientDescribeInstanceTypeOfferingsResponseTypeDef,
    ClientDescribeInstanceTypesFiltersTypeDef,
    ClientDescribeInstanceTypesResponseTypeDef,
    ClientDescribeInstancesFiltersTypeDef,
    ClientDescribeInstancesResponseTypeDef,
    ClientDescribeInternetGatewaysFiltersTypeDef,
    ClientDescribeInternetGatewaysResponseTypeDef,
    ClientDescribeIpv6PoolsFiltersTypeDef,
    ClientDescribeIpv6PoolsResponseTypeDef,
    ClientDescribeKeyPairsFiltersTypeDef,
    ClientDescribeKeyPairsResponseTypeDef,
    ClientDescribeLaunchTemplateVersionsFiltersTypeDef,
    ClientDescribeLaunchTemplateVersionsResponseTypeDef,
    ClientDescribeLaunchTemplatesFiltersTypeDef,
    ClientDescribeLaunchTemplatesResponseTypeDef,
    ClientDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsFiltersTypeDef,
    ClientDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponseTypeDef,
    ClientDescribeLocalGatewayRouteTableVpcAssociationsFiltersTypeDef,
    ClientDescribeLocalGatewayRouteTableVpcAssociationsResponseTypeDef,
    ClientDescribeLocalGatewayRouteTablesFiltersTypeDef,
    ClientDescribeLocalGatewayRouteTablesResponseTypeDef,
    ClientDescribeLocalGatewayVirtualInterfaceGroupsFiltersTypeDef,
    ClientDescribeLocalGatewayVirtualInterfaceGroupsResponseTypeDef,
    ClientDescribeLocalGatewayVirtualInterfacesFiltersTypeDef,
    ClientDescribeLocalGatewayVirtualInterfacesResponseTypeDef,
    ClientDescribeLocalGatewaysFiltersTypeDef,
    ClientDescribeLocalGatewaysResponseTypeDef,
    ClientDescribeMovingAddressesFiltersTypeDef,
    ClientDescribeMovingAddressesResponseTypeDef,
    ClientDescribeNatGatewaysFiltersTypeDef,
    ClientDescribeNatGatewaysResponseTypeDef,
    ClientDescribeNetworkAclsFiltersTypeDef,
    ClientDescribeNetworkAclsResponseTypeDef,
    ClientDescribeNetworkInterfaceAttributeResponseTypeDef,
    ClientDescribeNetworkInterfacePermissionsFiltersTypeDef,
    ClientDescribeNetworkInterfacePermissionsResponseTypeDef,
    ClientDescribeNetworkInterfacesFiltersTypeDef,
    ClientDescribeNetworkInterfacesResponseTypeDef,
    ClientDescribePlacementGroupsFiltersTypeDef,
    ClientDescribePlacementGroupsResponseTypeDef,
    ClientDescribePrefixListsFiltersTypeDef,
    ClientDescribePrefixListsResponseTypeDef,
    ClientDescribePrincipalIdFormatResponseTypeDef,
    ClientDescribePublicIpv4PoolsResponseTypeDef,
    ClientDescribeRegionsFiltersTypeDef,
    ClientDescribeRegionsResponseTypeDef,
    ClientDescribeReservedInstancesFiltersTypeDef,
    ClientDescribeReservedInstancesListingsFiltersTypeDef,
    ClientDescribeReservedInstancesListingsResponseTypeDef,
    ClientDescribeReservedInstancesModificationsFiltersTypeDef,
    ClientDescribeReservedInstancesModificationsResponseTypeDef,
    ClientDescribeReservedInstancesOfferingsFiltersTypeDef,
    ClientDescribeReservedInstancesOfferingsResponseTypeDef,
    ClientDescribeReservedInstancesResponseTypeDef,
    ClientDescribeRouteTablesFiltersTypeDef,
    ClientDescribeRouteTablesResponseTypeDef,
    ClientDescribeScheduledInstanceAvailabilityFiltersTypeDef,
    ClientDescribeScheduledInstanceAvailabilityFirstSlotStartTimeRangeTypeDef,
    ClientDescribeScheduledInstanceAvailabilityRecurrenceTypeDef,
    ClientDescribeScheduledInstanceAvailabilityResponseTypeDef,
    ClientDescribeScheduledInstancesFiltersTypeDef,
    ClientDescribeScheduledInstancesResponseTypeDef,
    ClientDescribeScheduledInstancesSlotStartTimeRangeTypeDef,
    ClientDescribeSecurityGroupReferencesResponseTypeDef,
    ClientDescribeSecurityGroupsFiltersTypeDef,
    ClientDescribeSecurityGroupsResponseTypeDef,
    ClientDescribeSnapshotAttributeResponseTypeDef,
    ClientDescribeSnapshotsFiltersTypeDef,
    ClientDescribeSnapshotsResponseTypeDef,
    ClientDescribeSpotDatafeedSubscriptionResponseTypeDef,
    ClientDescribeSpotFleetInstancesResponseTypeDef,
    ClientDescribeSpotFleetRequestHistoryResponseTypeDef,
    ClientDescribeSpotFleetRequestsResponseTypeDef,
    ClientDescribeSpotInstanceRequestsFiltersTypeDef,
    ClientDescribeSpotInstanceRequestsResponseTypeDef,
    ClientDescribeSpotPriceHistoryFiltersTypeDef,
    ClientDescribeSpotPriceHistoryResponseTypeDef,
    ClientDescribeStaleSecurityGroupsResponseTypeDef,
    ClientDescribeSubnetsFiltersTypeDef,
    ClientDescribeSubnetsResponseTypeDef,
    ClientDescribeTagsFiltersTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDescribeTrafficMirrorFiltersFiltersTypeDef,
    ClientDescribeTrafficMirrorFiltersResponseTypeDef,
    ClientDescribeTrafficMirrorSessionsFiltersTypeDef,
    ClientDescribeTrafficMirrorSessionsResponseTypeDef,
    ClientDescribeTrafficMirrorTargetsFiltersTypeDef,
    ClientDescribeTrafficMirrorTargetsResponseTypeDef,
    ClientDescribeTransitGatewayAttachmentsFiltersTypeDef,
    ClientDescribeTransitGatewayAttachmentsResponseTypeDef,
    ClientDescribeTransitGatewayMulticastDomainsFiltersTypeDef,
    ClientDescribeTransitGatewayMulticastDomainsResponseTypeDef,
    ClientDescribeTransitGatewayPeeringAttachmentsFiltersTypeDef,
    ClientDescribeTransitGatewayPeeringAttachmentsResponseTypeDef,
    ClientDescribeTransitGatewayRouteTablesFiltersTypeDef,
    ClientDescribeTransitGatewayRouteTablesResponseTypeDef,
    ClientDescribeTransitGatewayVpcAttachmentsFiltersTypeDef,
    ClientDescribeTransitGatewayVpcAttachmentsResponseTypeDef,
    ClientDescribeTransitGatewaysFiltersTypeDef,
    ClientDescribeTransitGatewaysResponseTypeDef,
    ClientDescribeVolumeAttributeResponseTypeDef,
    ClientDescribeVolumeStatusFiltersTypeDef,
    ClientDescribeVolumeStatusResponseTypeDef,
    ClientDescribeVolumesFiltersTypeDef,
    ClientDescribeVolumesModificationsFiltersTypeDef,
    ClientDescribeVolumesModificationsResponseTypeDef,
    ClientDescribeVolumesResponseTypeDef,
    ClientDescribeVpcAttributeResponseTypeDef,
    ClientDescribeVpcClassicLinkDnsSupportResponseTypeDef,
    ClientDescribeVpcClassicLinkFiltersTypeDef,
    ClientDescribeVpcClassicLinkResponseTypeDef,
    ClientDescribeVpcEndpointConnectionNotificationsFiltersTypeDef,
    ClientDescribeVpcEndpointConnectionNotificationsResponseTypeDef,
    ClientDescribeVpcEndpointConnectionsFiltersTypeDef,
    ClientDescribeVpcEndpointConnectionsResponseTypeDef,
    ClientDescribeVpcEndpointServiceConfigurationsFiltersTypeDef,
    ClientDescribeVpcEndpointServiceConfigurationsResponseTypeDef,
    ClientDescribeVpcEndpointServicePermissionsFiltersTypeDef,
    ClientDescribeVpcEndpointServicePermissionsResponseTypeDef,
    ClientDescribeVpcEndpointServicesFiltersTypeDef,
    ClientDescribeVpcEndpointServicesResponseTypeDef,
    ClientDescribeVpcEndpointsFiltersTypeDef,
    ClientDescribeVpcEndpointsResponseTypeDef,
    ClientDescribeVpcPeeringConnectionsFiltersTypeDef,
    ClientDescribeVpcPeeringConnectionsResponseTypeDef,
    ClientDescribeVpcsFiltersTypeDef,
    ClientDescribeVpcsResponseTypeDef,
    ClientDescribeVpnConnectionsFiltersTypeDef,
    ClientDescribeVpnConnectionsResponseTypeDef,
    ClientDescribeVpnGatewaysFiltersTypeDef,
    ClientDescribeVpnGatewaysResponseTypeDef,
    ClientDetachClassicLinkVpcResponseTypeDef,
    ClientDetachVolumeResponseTypeDef,
    ClientDisableEbsEncryptionByDefaultResponseTypeDef,
    ClientDisableFastSnapshotRestoresResponseTypeDef,
    ClientDisableTransitGatewayRouteTablePropagationResponseTypeDef,
    ClientDisableVpcClassicLinkDnsSupportResponseTypeDef,
    ClientDisableVpcClassicLinkResponseTypeDef,
    ClientDisassociateClientVpnTargetNetworkResponseTypeDef,
    ClientDisassociateIamInstanceProfileResponseTypeDef,
    ClientDisassociateSubnetCidrBlockResponseTypeDef,
    ClientDisassociateTransitGatewayMulticastDomainResponseTypeDef,
    ClientDisassociateTransitGatewayRouteTableResponseTypeDef,
    ClientDisassociateVpcCidrBlockResponseTypeDef,
    ClientEnableEbsEncryptionByDefaultResponseTypeDef,
    ClientEnableFastSnapshotRestoresResponseTypeDef,
    ClientEnableTransitGatewayRouteTablePropagationResponseTypeDef,
    ClientEnableVpcClassicLinkDnsSupportResponseTypeDef,
    ClientEnableVpcClassicLinkResponseTypeDef,
    ClientExportClientVpnClientCertificateRevocationListResponseTypeDef,
    ClientExportClientVpnClientConfigurationResponseTypeDef,
    ClientExportImageResponseTypeDef,
    ClientExportImageS3ExportLocationTypeDef,
    ClientExportTransitGatewayRoutesFiltersTypeDef,
    ClientExportTransitGatewayRoutesResponseTypeDef,
    ClientGetAssociatedIpv6PoolCidrsResponseTypeDef,
    ClientGetCapacityReservationUsageResponseTypeDef,
    ClientGetCoipPoolUsageFiltersTypeDef,
    ClientGetCoipPoolUsageResponseTypeDef,
    ClientGetConsoleOutputResponseTypeDef,
    ClientGetConsoleScreenshotResponseTypeDef,
    ClientGetDefaultCreditSpecificationResponseTypeDef,
    ClientGetEbsDefaultKmsKeyIdResponseTypeDef,
    ClientGetEbsEncryptionByDefaultResponseTypeDef,
    ClientGetHostReservationPurchasePreviewResponseTypeDef,
    ClientGetLaunchTemplateDataResponseTypeDef,
    ClientGetPasswordDataResponseTypeDef,
    ClientGetReservedInstancesExchangeQuoteResponseTypeDef,
    ClientGetReservedInstancesExchangeQuoteTargetConfigurationsTypeDef,
    ClientGetTransitGatewayAttachmentPropagationsFiltersTypeDef,
    ClientGetTransitGatewayAttachmentPropagationsResponseTypeDef,
    ClientGetTransitGatewayMulticastDomainAssociationsFiltersTypeDef,
    ClientGetTransitGatewayMulticastDomainAssociationsResponseTypeDef,
    ClientGetTransitGatewayRouteTableAssociationsFiltersTypeDef,
    ClientGetTransitGatewayRouteTableAssociationsResponseTypeDef,
    ClientGetTransitGatewayRouteTablePropagationsFiltersTypeDef,
    ClientGetTransitGatewayRouteTablePropagationsResponseTypeDef,
    ClientImportClientVpnClientCertificateRevocationListResponseTypeDef,
    ClientImportImageClientDataTypeDef,
    ClientImportImageDiskContainersTypeDef,
    ClientImportImageLicenseSpecificationsTypeDef,
    ClientImportImageResponseTypeDef,
    ClientImportInstanceDiskImagesTypeDef,
    ClientImportInstanceLaunchSpecificationTypeDef,
    ClientImportInstanceResponseTypeDef,
    ClientImportKeyPairResponseTypeDef,
    ClientImportSnapshotClientDataTypeDef,
    ClientImportSnapshotDiskContainerTypeDef,
    ClientImportSnapshotResponseTypeDef,
    ClientImportVolumeImageTypeDef,
    ClientImportVolumeResponseTypeDef,
    ClientImportVolumeVolumeTypeDef,
    ClientModifyCapacityReservationResponseTypeDef,
    ClientModifyClientVpnEndpointConnectionLogOptionsTypeDef,
    ClientModifyClientVpnEndpointDnsServersTypeDef,
    ClientModifyClientVpnEndpointResponseTypeDef,
    ClientModifyDefaultCreditSpecificationResponseTypeDef,
    ClientModifyEbsDefaultKmsKeyIdResponseTypeDef,
    ClientModifyFleetResponseTypeDef,
    ClientModifyFleetTargetCapacitySpecificationTypeDef,
    ClientModifyFpgaImageAttributeLoadPermissionTypeDef,
    ClientModifyFpgaImageAttributeResponseTypeDef,
    ClientModifyHostsResponseTypeDef,
    ClientModifyImageAttributeDescriptionTypeDef,
    ClientModifyImageAttributeLaunchPermissionTypeDef,
    ClientModifyInstanceAttributeBlockDeviceMappingsTypeDef,
    ClientModifyInstanceAttributeDisableApiTerminationTypeDef,
    ClientModifyInstanceAttributeEbsOptimizedTypeDef,
    ClientModifyInstanceAttributeEnaSupportTypeDef,
    ClientModifyInstanceAttributeInstanceInitiatedShutdownBehaviorTypeDef,
    ClientModifyInstanceAttributeInstanceTypeTypeDef,
    ClientModifyInstanceAttributeKernelTypeDef,
    ClientModifyInstanceAttributeRamdiskTypeDef,
    ClientModifyInstanceAttributeSourceDestCheckTypeDef,
    ClientModifyInstanceAttributeSriovNetSupportTypeDef,
    ClientModifyInstanceAttributeUserDataTypeDef,
    ClientModifyInstanceCapacityReservationAttributesCapacityReservationSpecificationTypeDef,
    ClientModifyInstanceCapacityReservationAttributesResponseTypeDef,
    ClientModifyInstanceCreditSpecificationInstanceCreditSpecificationsTypeDef,
    ClientModifyInstanceCreditSpecificationResponseTypeDef,
    ClientModifyInstanceEventStartTimeResponseTypeDef,
    ClientModifyInstanceMetadataOptionsResponseTypeDef,
    ClientModifyInstancePlacementResponseTypeDef,
    ClientModifyLaunchTemplateResponseTypeDef,
    ClientModifyNetworkInterfaceAttributeAttachmentTypeDef,
    ClientModifyNetworkInterfaceAttributeDescriptionTypeDef,
    ClientModifyNetworkInterfaceAttributeSourceDestCheckTypeDef,
    ClientModifyReservedInstancesResponseTypeDef,
    ClientModifyReservedInstancesTargetConfigurationsTypeDef,
    ClientModifySnapshotAttributeCreateVolumePermissionTypeDef,
    ClientModifySpotFleetRequestResponseTypeDef,
    ClientModifySubnetAttributeAssignIpv6AddressOnCreationTypeDef,
    ClientModifySubnetAttributeMapPublicIpOnLaunchTypeDef,
    ClientModifyTrafficMirrorFilterNetworkServicesResponseTypeDef,
    ClientModifyTrafficMirrorFilterRuleDestinationPortRangeTypeDef,
    ClientModifyTrafficMirrorFilterRuleResponseTypeDef,
    ClientModifyTrafficMirrorFilterRuleSourcePortRangeTypeDef,
    ClientModifyTrafficMirrorSessionResponseTypeDef,
    ClientModifyTransitGatewayVpcAttachmentOptionsTypeDef,
    ClientModifyTransitGatewayVpcAttachmentResponseTypeDef,
    ClientModifyVolumeAttributeAutoEnableIOTypeDef,
    ClientModifyVolumeResponseTypeDef,
    ClientModifyVpcAttributeEnableDnsHostnamesTypeDef,
    ClientModifyVpcAttributeEnableDnsSupportTypeDef,
    ClientModifyVpcEndpointConnectionNotificationResponseTypeDef,
    ClientModifyVpcEndpointResponseTypeDef,
    ClientModifyVpcEndpointServiceConfigurationResponseTypeDef,
    ClientModifyVpcEndpointServicePermissionsResponseTypeDef,
    ClientModifyVpcPeeringConnectionOptionsAccepterPeeringConnectionOptionsTypeDef,
    ClientModifyVpcPeeringConnectionOptionsRequesterPeeringConnectionOptionsTypeDef,
    ClientModifyVpcPeeringConnectionOptionsResponseTypeDef,
    ClientModifyVpcTenancyResponseTypeDef,
    ClientModifyVpnConnectionResponseTypeDef,
    ClientModifyVpnTunnelCertificateResponseTypeDef,
    ClientModifyVpnTunnelOptionsResponseTypeDef,
    ClientModifyVpnTunnelOptionsTunnelOptionsTypeDef,
    ClientMonitorInstancesResponseTypeDef,
    ClientMoveAddressToVpcResponseTypeDef,
    ClientProvisionByoipCidrCidrAuthorizationContextTypeDef,
    ClientProvisionByoipCidrResponseTypeDef,
    ClientPurchaseHostReservationResponseTypeDef,
    ClientPurchaseReservedInstancesOfferingLimitPriceTypeDef,
    ClientPurchaseReservedInstancesOfferingResponseTypeDef,
    ClientPurchaseScheduledInstancesPurchaseRequestsTypeDef,
    ClientPurchaseScheduledInstancesResponseTypeDef,
    ClientRegisterImageBlockDeviceMappingsTypeDef,
    ClientRegisterImageResponseTypeDef,
    ClientRegisterTransitGatewayMulticastGroupMembersResponseTypeDef,
    ClientRegisterTransitGatewayMulticastGroupSourcesResponseTypeDef,
    ClientRejectTransitGatewayPeeringAttachmentResponseTypeDef,
    ClientRejectTransitGatewayVpcAttachmentResponseTypeDef,
    ClientRejectVpcEndpointConnectionsResponseTypeDef,
    ClientRejectVpcPeeringConnectionResponseTypeDef,
    ClientReleaseHostsResponseTypeDef,
    ClientReplaceIamInstanceProfileAssociationIamInstanceProfileTypeDef,
    ClientReplaceIamInstanceProfileAssociationResponseTypeDef,
    ClientReplaceNetworkAclAssociationResponseTypeDef,
    ClientReplaceNetworkAclEntryIcmpTypeCodeTypeDef,
    ClientReplaceNetworkAclEntryPortRangeTypeDef,
    ClientReplaceRouteTableAssociationResponseTypeDef,
    ClientReplaceTransitGatewayRouteResponseTypeDef,
    ClientRequestSpotFleetResponseTypeDef,
    ClientRequestSpotFleetSpotFleetRequestConfigTypeDef,
    ClientRequestSpotInstancesLaunchSpecificationTypeDef,
    ClientRequestSpotInstancesResponseTypeDef,
    ClientResetEbsDefaultKmsKeyIdResponseTypeDef,
    ClientResetFpgaImageAttributeResponseTypeDef,
    ClientRestoreAddressToClassicResponseTypeDef,
    ClientRevokeClientVpnIngressResponseTypeDef,
    ClientRevokeSecurityGroupEgressIpPermissionsTypeDef,
    ClientRevokeSecurityGroupIngressIpPermissionsTypeDef,
    ClientRunInstancesBlockDeviceMappingsTypeDef,
    ClientRunInstancesCapacityReservationSpecificationTypeDef,
    ClientRunInstancesCpuOptionsTypeDef,
    ClientRunInstancesCreditSpecificationTypeDef,
    ClientRunInstancesElasticGpuSpecificationTypeDef,
    ClientRunInstancesElasticInferenceAcceleratorsTypeDef,
    ClientRunInstancesHibernationOptionsTypeDef,
    ClientRunInstancesIamInstanceProfileTypeDef,
    ClientRunInstancesInstanceMarketOptionsTypeDef,
    ClientRunInstancesIpv6AddressesTypeDef,
    ClientRunInstancesLaunchTemplateTypeDef,
    ClientRunInstancesLicenseSpecificationsTypeDef,
    ClientRunInstancesMetadataOptionsTypeDef,
    ClientRunInstancesMonitoringTypeDef,
    ClientRunInstancesNetworkInterfacesTypeDef,
    ClientRunInstancesPlacementTypeDef,
    ClientRunInstancesResponseTypeDef,
    ClientRunInstancesTagSpecificationsTypeDef,
    ClientRunScheduledInstancesLaunchSpecificationTypeDef,
    ClientRunScheduledInstancesResponseTypeDef,
    ClientSearchLocalGatewayRoutesFiltersTypeDef,
    ClientSearchLocalGatewayRoutesResponseTypeDef,
    ClientSearchTransitGatewayMulticastGroupsFiltersTypeDef,
    ClientSearchTransitGatewayMulticastGroupsResponseTypeDef,
    ClientSearchTransitGatewayRoutesFiltersTypeDef,
    ClientSearchTransitGatewayRoutesResponseTypeDef,
    ClientStartInstancesResponseTypeDef,
    ClientStartVpcEndpointServicePrivateDnsVerificationResponseTypeDef,
    ClientStopInstancesResponseTypeDef,
    ClientTerminateClientVpnConnectionsResponseTypeDef,
    ClientTerminateInstancesResponseTypeDef,
    ClientUnassignIpv6AddressesResponseTypeDef,
    ClientUnmonitorInstancesResponseTypeDef,
    ClientUpdateSecurityGroupRuleDescriptionsEgressIpPermissionsTypeDef,
    ClientUpdateSecurityGroupRuleDescriptionsEgressResponseTypeDef,
    ClientUpdateSecurityGroupRuleDescriptionsIngressIpPermissionsTypeDef,
    ClientUpdateSecurityGroupRuleDescriptionsIngressResponseTypeDef,
    ClientWithdrawByoipCidrResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ec2.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EC2Client",)


class EC2Client:
    """
    [EC2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List[
            ClientAcceptReservedInstancesExchangeQuoteTargetConfigurationsTypeDef
        ] = None,
    ) -> ClientAcceptReservedInstancesExchangeQuoteResponseTypeDef:
        """
        [Client.accept_reserved_instances_exchange_quote documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.accept_reserved_instances_exchange_quote)
        """

    def accept_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientAcceptTransitGatewayPeeringAttachmentResponseTypeDef:
        """
        [Client.accept_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.accept_transit_gateway_peering_attachment)
        """

    def accept_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientAcceptTransitGatewayVpcAttachmentResponseTypeDef:
        """
        [Client.accept_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.accept_transit_gateway_vpc_attachment)
        """

    def accept_vpc_endpoint_connections(
        self, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> ClientAcceptVpcEndpointConnectionsResponseTypeDef:
        """
        [Client.accept_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.accept_vpc_endpoint_connections)
        """

    def accept_vpc_peering_connection(
        self, DryRun: bool = None, VpcPeeringConnectionId: str = None
    ) -> ClientAcceptVpcPeeringConnectionResponseTypeDef:
        """
        [Client.accept_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.accept_vpc_peering_connection)
        """

    def advertise_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> ClientAdvertiseByoipCidrResponseTypeDef:
        """
        [Client.advertise_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.advertise_byoip_cidr)
        """

    def allocate_address(
        self,
        Domain: Literal["vpc", "standard"] = None,
        Address: str = None,
        PublicIpv4Pool: str = None,
        NetworkBorderGroup: str = None,
        CustomerOwnedIpv4Pool: str = None,
        DryRun: bool = None,
    ) -> ClientAllocateAddressResponseTypeDef:
        """
        [Client.allocate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.allocate_address)
        """

    def allocate_hosts(
        self,
        AvailabilityZone: str,
        Quantity: int,
        AutoPlacement: Literal["on", "off"] = None,
        ClientToken: str = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
        TagSpecifications: List[ClientAllocateHostsTagSpecificationsTypeDef] = None,
        HostRecovery: Literal["on", "off"] = None,
    ) -> ClientAllocateHostsResponseTypeDef:
        """
        [Client.allocate_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.allocate_hosts)
        """

    def apply_security_groups_to_client_vpn_target_network(
        self, ClientVpnEndpointId: str, VpcId: str, SecurityGroupIds: List[str], DryRun: bool = None
    ) -> ClientApplySecurityGroupsToClientVpnTargetNetworkResponseTypeDef:
        """
        [Client.apply_security_groups_to_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.apply_security_groups_to_client_vpn_target_network)
        """

    def assign_ipv6_addresses(
        self, NetworkInterfaceId: str, Ipv6AddressCount: int = None, Ipv6Addresses: List[str] = None
    ) -> ClientAssignIpv6AddressesResponseTypeDef:
        """
        [Client.assign_ipv6_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.assign_ipv6_addresses)
        """

    def assign_private_ip_addresses(
        self,
        NetworkInterfaceId: str,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> ClientAssignPrivateIpAddressesResponseTypeDef:
        """
        [Client.assign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.assign_private_ip_addresses)
        """

    def associate_address(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> ClientAssociateAddressResponseTypeDef:
        """
        [Client.associate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_address)
        """

    def associate_client_vpn_target_network(
        self, ClientVpnEndpointId: str, SubnetId: str, ClientToken: str = None, DryRun: bool = None
    ) -> ClientAssociateClientVpnTargetNetworkResponseTypeDef:
        """
        [Client.associate_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_client_vpn_target_network)
        """

    def associate_dhcp_options(self, DhcpOptionsId: str, VpcId: str, DryRun: bool = None) -> None:
        """
        [Client.associate_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_dhcp_options)
        """

    def associate_iam_instance_profile(
        self,
        IamInstanceProfile: ClientAssociateIamInstanceProfileIamInstanceProfileTypeDef,
        InstanceId: str,
    ) -> ClientAssociateIamInstanceProfileResponseTypeDef:
        """
        [Client.associate_iam_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_iam_instance_profile)
        """

    def associate_route_table(
        self, RouteTableId: str, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> ClientAssociateRouteTableResponseTypeDef:
        """
        [Client.associate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_route_table)
        """

    def associate_subnet_cidr_block(
        self, Ipv6CidrBlock: str, SubnetId: str
    ) -> ClientAssociateSubnetCidrBlockResponseTypeDef:
        """
        [Client.associate_subnet_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_subnet_cidr_block)
        """

    def associate_transit_gateway_multicast_domain(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientAssociateTransitGatewayMulticastDomainResponseTypeDef:
        """
        [Client.associate_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_transit_gateway_multicast_domain)
        """

    def associate_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientAssociateTransitGatewayRouteTableResponseTypeDef:
        """
        [Client.associate_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_transit_gateway_route_table)
        """

    def associate_vpc_cidr_block(
        self,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        CidrBlock: str = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
    ) -> ClientAssociateVpcCidrBlockResponseTypeDef:
        """
        [Client.associate_vpc_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.associate_vpc_cidr_block)
        """

    def attach_classic_link_vpc(
        self, Groups: List[str], InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> ClientAttachClassicLinkVpcResponseTypeDef:
        """
        [Client.attach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.attach_classic_link_vpc)
        """

    def attach_internet_gateway(
        self, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        [Client.attach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.attach_internet_gateway)
        """

    def attach_network_interface(
        self, DeviceIndex: int, InstanceId: str, NetworkInterfaceId: str, DryRun: bool = None
    ) -> ClientAttachNetworkInterfaceResponseTypeDef:
        """
        [Client.attach_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.attach_network_interface)
        """

    def attach_volume(
        self, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = None
    ) -> ClientAttachVolumeResponseTypeDef:
        """
        [Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.attach_volume)
        """

    def attach_vpn_gateway(
        self, VpcId: str, VpnGatewayId: str, DryRun: bool = None
    ) -> ClientAttachVpnGatewayResponseTypeDef:
        """
        [Client.attach_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.attach_vpn_gateway)
        """

    def authorize_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        AuthorizeAllGroups: bool = None,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> ClientAuthorizeClientVpnIngressResponseTypeDef:
        """
        [Client.authorize_client_vpn_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.authorize_client_vpn_ingress)
        """

    def authorize_security_group_egress(
        self,
        GroupId: str,
        DryRun: bool = None,
        IpPermissions: List[ClientAuthorizeSecurityGroupEgressIpPermissionsTypeDef] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        """
        [Client.authorize_security_group_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.authorize_security_group_egress)
        """

    def authorize_security_group_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List[ClientAuthorizeSecurityGroupIngressIpPermissionsTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.authorize_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress)
        """

    def bundle_instance(
        self, InstanceId: str, Storage: ClientBundleInstanceStorageTypeDef, DryRun: bool = None
    ) -> ClientBundleInstanceResponseTypeDef:
        """
        [Client.bundle_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.bundle_instance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.can_paginate)
        """

    def cancel_bundle_task(
        self, BundleId: str, DryRun: bool = None
    ) -> ClientCancelBundleTaskResponseTypeDef:
        """
        [Client.cancel_bundle_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_bundle_task)
        """

    def cancel_capacity_reservation(
        self, CapacityReservationId: str, DryRun: bool = None
    ) -> ClientCancelCapacityReservationResponseTypeDef:
        """
        [Client.cancel_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation)
        """

    def cancel_conversion_task(
        self, ConversionTaskId: str, DryRun: bool = None, ReasonMessage: str = None
    ) -> None:
        """
        [Client.cancel_conversion_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_conversion_task)
        """

    def cancel_export_task(self, ExportTaskId: str) -> None:
        """
        [Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_export_task)
        """

    def cancel_import_task(
        self, CancelReason: str = None, DryRun: bool = None, ImportTaskId: str = None
    ) -> ClientCancelImportTaskResponseTypeDef:
        """
        [Client.cancel_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_import_task)
        """

    def cancel_reserved_instances_listing(
        self, ReservedInstancesListingId: str
    ) -> ClientCancelReservedInstancesListingResponseTypeDef:
        """
        [Client.cancel_reserved_instances_listing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_reserved_instances_listing)
        """

    def cancel_spot_fleet_requests(
        self, SpotFleetRequestIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> ClientCancelSpotFleetRequestsResponseTypeDef:
        """
        [Client.cancel_spot_fleet_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_spot_fleet_requests)
        """

    def cancel_spot_instance_requests(
        self, SpotInstanceRequestIds: List[str], DryRun: bool = None
    ) -> ClientCancelSpotInstanceRequestsResponseTypeDef:
        """
        [Client.cancel_spot_instance_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.cancel_spot_instance_requests)
        """

    def confirm_product_instance(
        self, InstanceId: str, ProductCode: str, DryRun: bool = None
    ) -> ClientConfirmProductInstanceResponseTypeDef:
        """
        [Client.confirm_product_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.confirm_product_instance)
        """

    def copy_fpga_image(
        self,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: bool = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
    ) -> ClientCopyFpgaImageResponseTypeDef:
        """
        [Client.copy_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.copy_fpga_image)
        """

    def copy_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: str = None,
        Description: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        DryRun: bool = None,
    ) -> ClientCopyImageResponseTypeDef:
        """
        [Client.copy_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.copy_image)
        """

    def copy_snapshot(
        self,
        SourceRegion: str,
        SourceSnapshotId: str,
        Description: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List[ClientCopySnapshotTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientCopySnapshotResponseTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.copy_snapshot)
        """

    def create_capacity_reservation(
        self,
        InstanceType: str,
        InstancePlatform: Literal[
            "Linux/UNIX",
            "Red Hat Enterprise Linux",
            "SUSE Linux",
            "Windows",
            "Windows with SQL Server",
            "Windows with SQL Server Enterprise",
            "Windows with SQL Server Standard",
            "Windows with SQL Server Web",
            "Linux with SQL Server Standard",
            "Linux with SQL Server Web",
            "Linux with SQL Server Enterprise",
        ],
        InstanceCount: int,
        ClientToken: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tenancy: Literal["default", "dedicated"] = None,
        EbsOptimized: bool = None,
        EphemeralStorage: bool = None,
        EndDate: datetime = None,
        EndDateType: Literal["unlimited", "limited"] = None,
        InstanceMatchCriteria: Literal["open", "targeted"] = None,
        TagSpecifications: List[ClientCreateCapacityReservationTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientCreateCapacityReservationResponseTypeDef:
        """
        [Client.create_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_capacity_reservation)
        """

    def create_client_vpn_endpoint(
        self,
        ClientCidrBlock: str,
        ServerCertificateArn: str,
        AuthenticationOptions: List[ClientCreateClientVpnEndpointAuthenticationOptionsTypeDef],
        ConnectionLogOptions: ClientCreateClientVpnEndpointConnectionLogOptionsTypeDef,
        DnsServers: List[str] = None,
        TransportProtocol: Literal["tcp", "udp"] = None,
        VpnPort: int = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
        ClientToken: str = None,
        TagSpecifications: List[ClientCreateClientVpnEndpointTagSpecificationsTypeDef] = None,
    ) -> ClientCreateClientVpnEndpointResponseTypeDef:
        """
        [Client.create_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_client_vpn_endpoint)
        """

    def create_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> ClientCreateClientVpnRouteResponseTypeDef:
        """
        [Client.create_client_vpn_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_client_vpn_route)
        """

    def create_customer_gateway(
        self,
        BgpAsn: int,
        Type: str,
        PublicIp: str = None,
        CertificateArn: str = None,
        DeviceName: str = None,
        DryRun: bool = None,
    ) -> ClientCreateCustomerGatewayResponseTypeDef:
        """
        [Client.create_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_customer_gateway)
        """

    def create_default_subnet(
        self, AvailabilityZone: str, DryRun: bool = None
    ) -> ClientCreateDefaultSubnetResponseTypeDef:
        """
        [Client.create_default_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_default_subnet)
        """

    def create_default_vpc(self, DryRun: bool = None) -> ClientCreateDefaultVpcResponseTypeDef:
        """
        [Client.create_default_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_default_vpc)
        """

    def create_dhcp_options(
        self,
        DhcpConfigurations: List[ClientCreateDhcpOptionsDhcpConfigurationsTypeDef],
        DryRun: bool = None,
    ) -> ClientCreateDhcpOptionsResponseTypeDef:
        """
        [Client.create_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_dhcp_options)
        """

    def create_egress_only_internet_gateway(
        self, VpcId: str, ClientToken: str = None, DryRun: bool = None
    ) -> ClientCreateEgressOnlyInternetGatewayResponseTypeDef:
        """
        [Client.create_egress_only_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_egress_only_internet_gateway)
        """

    def create_fleet(
        self,
        LaunchTemplateConfigs: List[ClientCreateFleetLaunchTemplateConfigsTypeDef],
        TargetCapacitySpecification: ClientCreateFleetTargetCapacitySpecificationTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        SpotOptions: ClientCreateFleetSpotOptionsTypeDef = None,
        OnDemandOptions: ClientCreateFleetOnDemandOptionsTypeDef = None,
        ExcessCapacityTerminationPolicy: Literal["no-termination", "termination"] = None,
        TerminateInstancesWithExpiration: bool = None,
        Type: Literal["request", "maintain", "instant"] = None,
        ValidFrom: datetime = None,
        ValidUntil: datetime = None,
        ReplaceUnhealthyInstances: bool = None,
        TagSpecifications: List[ClientCreateFleetTagSpecificationsTypeDef] = None,
    ) -> ClientCreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_fleet)
        """

    def create_flow_logs(
        self,
        ResourceIds: List[str],
        ResourceType: Literal["VPC", "Subnet", "NetworkInterface"],
        TrafficType: Literal["ACCEPT", "REJECT", "ALL"],
        DryRun: bool = None,
        ClientToken: str = None,
        DeliverLogsPermissionArn: str = None,
        LogGroupName: str = None,
        LogDestinationType: Literal["cloud-watch-logs", "s3"] = None,
        LogDestination: str = None,
        LogFormat: str = None,
        MaxAggregationInterval: int = None,
    ) -> ClientCreateFlowLogsResponseTypeDef:
        """
        [Client.create_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_flow_logs)
        """

    def create_fpga_image(
        self,
        InputStorageLocation: ClientCreateFpgaImageInputStorageLocationTypeDef,
        DryRun: bool = None,
        LogsStorageLocation: ClientCreateFpgaImageLogsStorageLocationTypeDef = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
        TagSpecifications: List[ClientCreateFpgaImageTagSpecificationsTypeDef] = None,
    ) -> ClientCreateFpgaImageResponseTypeDef:
        """
        [Client.create_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_fpga_image)
        """

    def create_image(
        self,
        InstanceId: str,
        Name: str,
        BlockDeviceMappings: List[ClientCreateImageBlockDeviceMappingsTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
    ) -> ClientCreateImageResponseTypeDef:
        """
        [Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_image)
        """

    def create_instance_export_task(
        self,
        InstanceId: str,
        Description: str = None,
        ExportToS3Task: ClientCreateInstanceExportTaskExportToS3TaskTypeDef = None,
        TargetEnvironment: Literal["citrix", "vmware", "microsoft"] = None,
    ) -> ClientCreateInstanceExportTaskResponseTypeDef:
        """
        [Client.create_instance_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_instance_export_task)
        """

    def create_internet_gateway(
        self, DryRun: bool = None
    ) -> ClientCreateInternetGatewayResponseTypeDef:
        """
        [Client.create_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_internet_gateway)
        """

    def create_key_pair(
        self, KeyName: str, DryRun: bool = None
    ) -> ClientCreateKeyPairResponseTypeDef:
        """
        [Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_key_pair)
        """

    def create_launch_template(
        self,
        LaunchTemplateName: str,
        LaunchTemplateData: ClientCreateLaunchTemplateLaunchTemplateDataTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        VersionDescription: str = None,
        TagSpecifications: List[ClientCreateLaunchTemplateTagSpecificationsTypeDef] = None,
    ) -> ClientCreateLaunchTemplateResponseTypeDef:
        """
        [Client.create_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_launch_template)
        """

    def create_launch_template_version(
        self,
        LaunchTemplateData: ClientCreateLaunchTemplateVersionLaunchTemplateDataTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        SourceVersion: str = None,
        VersionDescription: str = None,
    ) -> ClientCreateLaunchTemplateVersionResponseTypeDef:
        """
        [Client.create_launch_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_launch_template_version)
        """

    def create_local_gateway_route(
        self,
        DestinationCidrBlock: str,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        DryRun: bool = None,
    ) -> ClientCreateLocalGatewayRouteResponseTypeDef:
        """
        [Client.create_local_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_local_gateway_route)
        """

    def create_local_gateway_route_table_vpc_association(
        self, LocalGatewayRouteTableId: str, VpcId: str, DryRun: bool = None
    ) -> ClientCreateLocalGatewayRouteTableVpcAssociationResponseTypeDef:
        """
        [Client.create_local_gateway_route_table_vpc_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_vpc_association)
        """

    def create_nat_gateway(
        self, AllocationId: str, SubnetId: str, ClientToken: str = None
    ) -> ClientCreateNatGatewayResponseTypeDef:
        """
        [Client.create_nat_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_nat_gateway)
        """

    def create_network_acl(
        self, VpcId: str, DryRun: bool = None
    ) -> ClientCreateNetworkAclResponseTypeDef:
        """
        [Client.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_network_acl)
        """

    def create_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: Literal["allow", "deny"],
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: ClientCreateNetworkAclEntryIcmpTypeCodeTypeDef = None,
        Ipv6CidrBlock: str = None,
        PortRange: ClientCreateNetworkAclEntryPortRangeTypeDef = None,
    ) -> None:
        """
        [Client.create_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_network_acl_entry)
        """

    def create_network_interface(
        self,
        SubnetId: str,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[ClientCreateNetworkInterfaceIpv6AddressesTypeDef] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List[ClientCreateNetworkInterfacePrivateIpAddressesTypeDef] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: str = None,
    ) -> ClientCreateNetworkInterfaceResponseTypeDef:
        """
        [Client.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_network_interface)
        """

    def create_network_interface_permission(
        self,
        NetworkInterfaceId: str,
        Permission: Literal["INSTANCE-ATTACH", "EIP-ASSOCIATE"],
        AwsAccountId: str = None,
        AwsService: str = None,
        DryRun: bool = None,
    ) -> ClientCreateNetworkInterfacePermissionResponseTypeDef:
        """
        [Client.create_network_interface_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_network_interface_permission)
        """

    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: Literal["cluster", "spread", "partition"] = None,
        PartitionCount: int = None,
    ) -> None:
        """
        [Client.create_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_placement_group)
        """

    def create_reserved_instances_listing(
        self,
        ClientToken: str,
        InstanceCount: int,
        PriceSchedules: List[ClientCreateReservedInstancesListingPriceSchedulesTypeDef],
        ReservedInstancesId: str,
    ) -> ClientCreateReservedInstancesListingResponseTypeDef:
        """
        [Client.create_reserved_instances_listing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_reserved_instances_listing)
        """

    def create_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> ClientCreateRouteResponseTypeDef:
        """
        [Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_route)
        """

    def create_route_table(
        self, VpcId: str, DryRun: bool = None
    ) -> ClientCreateRouteTableResponseTypeDef:
        """
        [Client.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_route_table)
        """

    def create_security_group(
        self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None
    ) -> ClientCreateSecurityGroupResponseTypeDef:
        """
        [Client.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_security_group)
        """

    def create_snapshot(
        self,
        VolumeId: str,
        Description: str = None,
        TagSpecifications: List[ClientCreateSnapshotTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientCreateSnapshotResponseTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_snapshot)
        """

    def create_snapshots(
        self,
        InstanceSpecification: ClientCreateSnapshotsInstanceSpecificationTypeDef,
        Description: str = None,
        TagSpecifications: List[ClientCreateSnapshotsTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
        CopyTagsFromSource: str = None,
    ) -> ClientCreateSnapshotsResponseTypeDef:
        """
        [Client.create_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_snapshots)
        """

    def create_spot_datafeed_subscription(
        self, Bucket: str, DryRun: bool = None, Prefix: str = None
    ) -> ClientCreateSpotDatafeedSubscriptionResponseTypeDef:
        """
        [Client.create_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_spot_datafeed_subscription)
        """

    def create_subnet(
        self,
        CidrBlock: str,
        VpcId: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> ClientCreateSubnetResponseTypeDef:
        """
        [Client.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_subnet)
        """

    def create_tags(
        self, Resources: List[str], Tags: List[ClientCreateTagsTagsTypeDef], DryRun: bool = None
    ) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_tags)
        """

    def create_traffic_mirror_filter(
        self,
        Description: str = None,
        TagSpecifications: List[ClientCreateTrafficMirrorFilterTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ClientCreateTrafficMirrorFilterResponseTypeDef:
        """
        [Client.create_traffic_mirror_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter)
        """

    def create_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterId: str,
        TrafficDirection: Literal["ingress", "egress"],
        RuleNumber: int,
        RuleAction: Literal["accept", "reject"],
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: ClientCreateTrafficMirrorFilterRuleDestinationPortRangeTypeDef = None,
        SourcePortRange: ClientCreateTrafficMirrorFilterRuleSourcePortRangeTypeDef = None,
        Protocol: int = None,
        Description: str = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ClientCreateTrafficMirrorFilterRuleResponseTypeDef:
        """
        [Client.create_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter_rule)
        """

    def create_traffic_mirror_session(
        self,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        TagSpecifications: List[ClientCreateTrafficMirrorSessionTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ClientCreateTrafficMirrorSessionResponseTypeDef:
        """
        [Client.create_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_traffic_mirror_session)
        """

    def create_traffic_mirror_target(
        self,
        NetworkInterfaceId: str = None,
        NetworkLoadBalancerArn: str = None,
        Description: str = None,
        TagSpecifications: List[ClientCreateTrafficMirrorTargetTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ClientCreateTrafficMirrorTargetResponseTypeDef:
        """
        [Client.create_traffic_mirror_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_traffic_mirror_target)
        """

    def create_transit_gateway(
        self,
        Description: str = None,
        Options: ClientCreateTransitGatewayOptionsTypeDef = None,
        TagSpecifications: List[ClientCreateTransitGatewayTagSpecificationsTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientCreateTransitGatewayResponseTypeDef:
        """
        [Client.create_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_transit_gateway)
        """

    def create_transit_gateway_multicast_domain(
        self,
        TransitGatewayId: str,
        TagSpecifications: List[
            ClientCreateTransitGatewayMulticastDomainTagSpecificationsTypeDef
        ] = None,
        DryRun: bool = None,
    ) -> ClientCreateTransitGatewayMulticastDomainResponseTypeDef:
        """
        [Client.create_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_transit_gateway_multicast_domain)
        """

    def create_transit_gateway_peering_attachment(
        self,
        TransitGatewayId: str,
        PeerTransitGatewayId: str,
        PeerAccountId: str,
        PeerRegion: str,
        TagSpecifications: List[
            ClientCreateTransitGatewayPeeringAttachmentTagSpecificationsTypeDef
        ] = None,
        DryRun: bool = None,
    ) -> ClientCreateTransitGatewayPeeringAttachmentResponseTypeDef:
        """
        [Client.create_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_transit_gateway_peering_attachment)
        """

    def create_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> ClientCreateTransitGatewayRouteResponseTypeDef:
        """
        [Client.create_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_transit_gateway_route)
        """

    def create_transit_gateway_route_table(
        self,
        TransitGatewayId: str,
        TagSpecifications: List[
            ClientCreateTransitGatewayRouteTableTagSpecificationsTypeDef
        ] = None,
        DryRun: bool = None,
    ) -> ClientCreateTransitGatewayRouteTableResponseTypeDef:
        """
        [Client.create_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table)
        """

    def create_transit_gateway_vpc_attachment(
        self,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: List[str],
        Options: ClientCreateTransitGatewayVpcAttachmentOptionsTypeDef = None,
        TagSpecifications: List[
            ClientCreateTransitGatewayVpcAttachmentTagSpecificationsTypeDef
        ] = None,
        DryRun: bool = None,
    ) -> ClientCreateTransitGatewayVpcAttachmentResponseTypeDef:
        """
        [Client.create_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_transit_gateway_vpc_attachment)
        """

    def create_volume(
        self,
        AvailabilityZone: str,
        Encrypted: bool = None,
        Iops: int = None,
        KmsKeyId: str = None,
        OutpostArn: str = None,
        Size: int = None,
        SnapshotId: str = None,
        VolumeType: Literal["standard", "io1", "gp2", "sc1", "st1"] = None,
        DryRun: bool = None,
        TagSpecifications: List[ClientCreateVolumeTagSpecificationsTypeDef] = None,
    ) -> ClientCreateVolumeResponseTypeDef:
        """
        [Client.create_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_volume)
        """

    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
    ) -> ClientCreateVpcResponseTypeDef:
        """
        [Client.create_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpc)
        """

    def create_vpc_endpoint(
        self,
        VpcId: str,
        ServiceName: str,
        DryRun: bool = None,
        VpcEndpointType: Literal["Interface", "Gateway"] = None,
        PolicyDocument: str = None,
        RouteTableIds: List[str] = None,
        SubnetIds: List[str] = None,
        SecurityGroupIds: List[str] = None,
        ClientToken: str = None,
        PrivateDnsEnabled: bool = None,
        TagSpecifications: List[ClientCreateVpcEndpointTagSpecificationsTypeDef] = None,
    ) -> ClientCreateVpcEndpointResponseTypeDef:
        """
        [Client.create_vpc_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpc_endpoint)
        """

    def create_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationArn: str,
        ConnectionEvents: List[str],
        DryRun: bool = None,
        ServiceId: str = None,
        VpcEndpointId: str = None,
        ClientToken: str = None,
    ) -> ClientCreateVpcEndpointConnectionNotificationResponseTypeDef:
        """
        [Client.create_vpc_endpoint_connection_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_connection_notification)
        """

    def create_vpc_endpoint_service_configuration(
        self,
        NetworkLoadBalancerArns: List[str],
        DryRun: bool = None,
        AcceptanceRequired: bool = None,
        PrivateDnsName: str = None,
        ClientToken: str = None,
        TagSpecifications: List[
            ClientCreateVpcEndpointServiceConfigurationTagSpecificationsTypeDef
        ] = None,
    ) -> ClientCreateVpcEndpointServiceConfigurationResponseTypeDef:
        """
        [Client.create_vpc_endpoint_service_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_service_configuration)
        """

    def create_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
    ) -> ClientCreateVpcPeeringConnectionResponseTypeDef:
        """
        [Client.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpc_peering_connection)
        """

    def create_vpn_connection(
        self,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: str = None,
        TransitGatewayId: str = None,
        DryRun: bool = None,
        Options: ClientCreateVpnConnectionOptionsTypeDef = None,
    ) -> ClientCreateVpnConnectionResponseTypeDef:
        """
        [Client.create_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpn_connection)
        """

    def create_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> None:
        """
        [Client.create_vpn_connection_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpn_connection_route)
        """

    def create_vpn_gateway(
        self,
        Type: str,
        AvailabilityZone: str = None,
        AmazonSideAsn: int = None,
        DryRun: bool = None,
    ) -> ClientCreateVpnGatewayResponseTypeDef:
        """
        [Client.create_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.create_vpn_gateway)
        """

    def delete_client_vpn_endpoint(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ClientDeleteClientVpnEndpointResponseTypeDef:
        """
        [Client.delete_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_client_vpn_endpoint)
        """

    def delete_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str = None,
        DryRun: bool = None,
    ) -> ClientDeleteClientVpnRouteResponseTypeDef:
        """
        [Client.delete_client_vpn_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_client_vpn_route)
        """

    def delete_customer_gateway(self, CustomerGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_customer_gateway)
        """

    def delete_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_dhcp_options)
        """

    def delete_egress_only_internet_gateway(
        self, EgressOnlyInternetGatewayId: str, DryRun: bool = None
    ) -> ClientDeleteEgressOnlyInternetGatewayResponseTypeDef:
        """
        [Client.delete_egress_only_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_egress_only_internet_gateway)
        """

    def delete_fleets(
        self, FleetIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> ClientDeleteFleetsResponseTypeDef:
        """
        [Client.delete_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_fleets)
        """

    def delete_flow_logs(
        self, FlowLogIds: List[str], DryRun: bool = None
    ) -> ClientDeleteFlowLogsResponseTypeDef:
        """
        [Client.delete_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_flow_logs)
        """

    def delete_fpga_image(
        self, FpgaImageId: str, DryRun: bool = None
    ) -> ClientDeleteFpgaImageResponseTypeDef:
        """
        [Client.delete_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_fpga_image)
        """

    def delete_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_internet_gateway)
        """

    def delete_key_pair(self, KeyName: str, DryRun: bool = None) -> None:
        """
        [Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_key_pair)
        """

    def delete_launch_template(
        self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None
    ) -> ClientDeleteLaunchTemplateResponseTypeDef:
        """
        [Client.delete_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_launch_template)
        """

    def delete_launch_template_versions(
        self,
        Versions: List[str],
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
    ) -> ClientDeleteLaunchTemplateVersionsResponseTypeDef:
        """
        [Client.delete_launch_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_launch_template_versions)
        """

    def delete_local_gateway_route(
        self, DestinationCidrBlock: str, LocalGatewayRouteTableId: str, DryRun: bool = None
    ) -> ClientDeleteLocalGatewayRouteResponseTypeDef:
        """
        [Client.delete_local_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_local_gateway_route)
        """

    def delete_local_gateway_route_table_vpc_association(
        self, LocalGatewayRouteTableVpcAssociationId: str, DryRun: bool = None
    ) -> ClientDeleteLocalGatewayRouteTableVpcAssociationResponseTypeDef:
        """
        [Client.delete_local_gateway_route_table_vpc_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_vpc_association)
        """

    def delete_nat_gateway(self, NatGatewayId: str) -> ClientDeleteNatGatewayResponseTypeDef:
        """
        [Client.delete_nat_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_nat_gateway)
        """

    def delete_network_acl(self, NetworkAclId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_network_acl)
        """

    def delete_network_acl_entry(
        self, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = None
    ) -> None:
        """
        [Client.delete_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_network_acl_entry)
        """

    def delete_network_interface(self, NetworkInterfaceId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_network_interface)
        """

    def delete_network_interface_permission(
        self, NetworkInterfacePermissionId: str, Force: bool = None, DryRun: bool = None
    ) -> ClientDeleteNetworkInterfacePermissionResponseTypeDef:
        """
        [Client.delete_network_interface_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_network_interface_permission)
        """

    def delete_placement_group(self, GroupName: str, DryRun: bool = None) -> None:
        """
        [Client.delete_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_placement_group)
        """

    def delete_queued_reserved_instances(
        self, ReservedInstancesIds: List[str], DryRun: bool = None
    ) -> ClientDeleteQueuedReservedInstancesResponseTypeDef:
        """
        [Client.delete_queued_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_queued_reserved_instances)
        """

    def delete_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_route)
        """

    def delete_route_table(self, RouteTableId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_route_table)
        """

    def delete_security_group(
        self, GroupId: str = None, GroupName: str = None, DryRun: bool = None
    ) -> None:
        """
        [Client.delete_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_security_group)
        """

    def delete_snapshot(self, SnapshotId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_snapshot)
        """

    def delete_spot_datafeed_subscription(self, DryRun: bool = None) -> None:
        """
        [Client.delete_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_spot_datafeed_subscription)
        """

    def delete_subnet(self, SubnetId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_subnet)
        """

    def delete_tags(
        self,
        Resources: List[str],
        DryRun: bool = None,
        Tags: List[ClientDeleteTagsTagsTypeDef] = None,
    ) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_tags)
        """

    def delete_traffic_mirror_filter(
        self, TrafficMirrorFilterId: str, DryRun: bool = None
    ) -> ClientDeleteTrafficMirrorFilterResponseTypeDef:
        """
        [Client.delete_traffic_mirror_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter)
        """

    def delete_traffic_mirror_filter_rule(
        self, TrafficMirrorFilterRuleId: str, DryRun: bool = None
    ) -> ClientDeleteTrafficMirrorFilterRuleResponseTypeDef:
        """
        [Client.delete_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter_rule)
        """

    def delete_traffic_mirror_session(
        self, TrafficMirrorSessionId: str, DryRun: bool = None
    ) -> ClientDeleteTrafficMirrorSessionResponseTypeDef:
        """
        [Client.delete_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_session)
        """

    def delete_traffic_mirror_target(
        self, TrafficMirrorTargetId: str, DryRun: bool = None
    ) -> ClientDeleteTrafficMirrorTargetResponseTypeDef:
        """
        [Client.delete_traffic_mirror_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_target)
        """

    def delete_transit_gateway(
        self, TransitGatewayId: str, DryRun: bool = None
    ) -> ClientDeleteTransitGatewayResponseTypeDef:
        """
        [Client.delete_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_transit_gateway)
        """

    def delete_transit_gateway_multicast_domain(
        self, TransitGatewayMulticastDomainId: str, DryRun: bool = None
    ) -> ClientDeleteTransitGatewayMulticastDomainResponseTypeDef:
        """
        [Client.delete_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_transit_gateway_multicast_domain)
        """

    def delete_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientDeleteTransitGatewayPeeringAttachmentResponseTypeDef:
        """
        [Client.delete_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_transit_gateway_peering_attachment)
        """

    def delete_transit_gateway_route(
        self, TransitGatewayRouteTableId: str, DestinationCidrBlock: str, DryRun: bool = None
    ) -> ClientDeleteTransitGatewayRouteResponseTypeDef:
        """
        [Client.delete_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route)
        """

    def delete_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, DryRun: bool = None
    ) -> ClientDeleteTransitGatewayRouteTableResponseTypeDef:
        """
        [Client.delete_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table)
        """

    def delete_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientDeleteTransitGatewayVpcAttachmentResponseTypeDef:
        """
        [Client.delete_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_transit_gateway_vpc_attachment)
        """

    def delete_volume(self, VolumeId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_volume)
        """

    def delete_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpc)
        """

    def delete_vpc_endpoint_connection_notifications(
        self, ConnectionNotificationIds: List[str], DryRun: bool = None
    ) -> ClientDeleteVpcEndpointConnectionNotificationsResponseTypeDef:
        """
        [Client.delete_vpc_endpoint_connection_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_connection_notifications)
        """

    def delete_vpc_endpoint_service_configurations(
        self, ServiceIds: List[str], DryRun: bool = None
    ) -> ClientDeleteVpcEndpointServiceConfigurationsResponseTypeDef:
        """
        [Client.delete_vpc_endpoint_service_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_service_configurations)
        """

    def delete_vpc_endpoints(
        self, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> ClientDeleteVpcEndpointsResponseTypeDef:
        """
        [Client.delete_vpc_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpc_endpoints)
        """

    def delete_vpc_peering_connection(
        self, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> ClientDeleteVpcPeeringConnectionResponseTypeDef:
        """
        [Client.delete_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpc_peering_connection)
        """

    def delete_vpn_connection(self, VpnConnectionId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpn_connection)
        """

    def delete_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> None:
        """
        [Client.delete_vpn_connection_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpn_connection_route)
        """

    def delete_vpn_gateway(self, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.delete_vpn_gateway)
        """

    def deprovision_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> ClientDeprovisionByoipCidrResponseTypeDef:
        """
        [Client.deprovision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.deprovision_byoip_cidr)
        """

    def deregister_image(self, ImageId: str, DryRun: bool = None) -> None:
        """
        [Client.deregister_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.deregister_image)
        """

    def deregister_transit_gateway_multicast_group_members(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDeregisterTransitGatewayMulticastGroupMembersResponseTypeDef:
        """
        [Client.deregister_transit_gateway_multicast_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_members)
        """

    def deregister_transit_gateway_multicast_group_sources(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDeregisterTransitGatewayMulticastGroupSourcesResponseTypeDef:
        """
        [Client.deregister_transit_gateway_multicast_group_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_sources)
        """

    def describe_account_attributes(
        self,
        AttributeNames: List[Literal["supported-platforms", "default-vpc"]] = None,
        DryRun: bool = None,
    ) -> ClientDescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_account_attributes)
        """

    def describe_addresses(
        self,
        Filters: List[ClientDescribeAddressesFiltersTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeAddressesResponseTypeDef:
        """
        [Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_addresses)
        """

    def describe_aggregate_id_format(
        self, DryRun: bool = None
    ) -> ClientDescribeAggregateIdFormatResponseTypeDef:
        """
        [Client.describe_aggregate_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_aggregate_id_format)
        """

    def describe_availability_zones(
        self,
        Filters: List[ClientDescribeAvailabilityZonesFiltersTypeDef] = None,
        ZoneNames: List[str] = None,
        ZoneIds: List[str] = None,
        AllAvailabilityZones: bool = None,
        DryRun: bool = None,
    ) -> ClientDescribeAvailabilityZonesResponseTypeDef:
        """
        [Client.describe_availability_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_availability_zones)
        """

    def describe_bundle_tasks(
        self,
        BundleIds: List[str] = None,
        Filters: List[ClientDescribeBundleTasksFiltersTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientDescribeBundleTasksResponseTypeDef:
        """
        [Client.describe_bundle_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_bundle_tasks)
        """

    def describe_byoip_cidrs(
        self, MaxResults: int, DryRun: bool = None, NextToken: str = None
    ) -> ClientDescribeByoipCidrsResponseTypeDef:
        """
        [Client.describe_byoip_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_byoip_cidrs)
        """

    def describe_capacity_reservations(
        self,
        CapacityReservationIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientDescribeCapacityReservationsFiltersTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientDescribeCapacityReservationsResponseTypeDef:
        """
        [Client.describe_capacity_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_capacity_reservations)
        """

    def describe_classic_link_instances(
        self,
        Filters: List[ClientDescribeClassicLinkInstancesFiltersTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeClassicLinkInstancesResponseTypeDef:
        """
        [Client.describe_classic_link_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_classic_link_instances)
        """

    def describe_client_vpn_authorization_rules(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        NextToken: str = None,
        Filters: List[ClientDescribeClientVpnAuthorizationRulesFiltersTypeDef] = None,
        MaxResults: int = None,
    ) -> ClientDescribeClientVpnAuthorizationRulesResponseTypeDef:
        """
        [Client.describe_client_vpn_authorization_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_client_vpn_authorization_rules)
        """

    def describe_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        Filters: List[ClientDescribeClientVpnConnectionsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> ClientDescribeClientVpnConnectionsResponseTypeDef:
        """
        [Client.describe_client_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_client_vpn_connections)
        """

    def describe_client_vpn_endpoints(
        self,
        ClientVpnEndpointIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientDescribeClientVpnEndpointsFiltersTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientDescribeClientVpnEndpointsResponseTypeDef:
        """
        [Client.describe_client_vpn_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_client_vpn_endpoints)
        """

    def describe_client_vpn_routes(
        self,
        ClientVpnEndpointId: str,
        Filters: List[ClientDescribeClientVpnRoutesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeClientVpnRoutesResponseTypeDef:
        """
        [Client.describe_client_vpn_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_client_vpn_routes)
        """

    def describe_client_vpn_target_networks(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientDescribeClientVpnTargetNetworksFiltersTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientDescribeClientVpnTargetNetworksResponseTypeDef:
        """
        [Client.describe_client_vpn_target_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_client_vpn_target_networks)
        """

    def describe_coip_pools(
        self,
        PoolIds: List[str] = None,
        Filters: List[ClientDescribeCoipPoolsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeCoipPoolsResponseTypeDef:
        """
        [Client.describe_coip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_coip_pools)
        """

    def describe_conversion_tasks(
        self, ConversionTaskIds: List[str] = None, DryRun: bool = None
    ) -> ClientDescribeConversionTasksResponseTypeDef:
        """
        [Client.describe_conversion_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_conversion_tasks)
        """

    def describe_customer_gateways(
        self,
        CustomerGatewayIds: List[str] = None,
        Filters: List[ClientDescribeCustomerGatewaysFiltersTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientDescribeCustomerGatewaysResponseTypeDef:
        """
        [Client.describe_customer_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_customer_gateways)
        """

    def describe_dhcp_options(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[ClientDescribeDhcpOptionsFiltersTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeDhcpOptionsResponseTypeDef:
        """
        [Client.describe_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_dhcp_options)
        """

    def describe_egress_only_internet_gateways(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientDescribeEgressOnlyInternetGatewaysFiltersTypeDef] = None,
    ) -> ClientDescribeEgressOnlyInternetGatewaysResponseTypeDef:
        """
        [Client.describe_egress_only_internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_egress_only_internet_gateways)
        """

    def describe_elastic_gpus(
        self,
        ElasticGpuIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[ClientDescribeElasticGpusFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeElasticGpusResponseTypeDef:
        """
        [Client.describe_elastic_gpus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_elastic_gpus)
        """

    def describe_export_image_tasks(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeExportImageTasksFiltersTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeExportImageTasksResponseTypeDef:
        """
        [Client.describe_export_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_export_image_tasks)
        """

    def describe_export_tasks(
        self,
        ExportTaskIds: List[str] = None,
        Filters: List[ClientDescribeExportTasksFiltersTypeDef] = None,
    ) -> ClientDescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_export_tasks)
        """

    def describe_fast_snapshot_restores(
        self,
        Filters: List[ClientDescribeFastSnapshotRestoresFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeFastSnapshotRestoresResponseTypeDef:
        """
        [Client.describe_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_fast_snapshot_restores)
        """

    def describe_fleet_history(
        self,
        FleetId: str,
        StartTime: datetime,
        DryRun: bool = None,
        EventType: Literal["instance-change", "fleet-change", "service-error"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeFleetHistoryResponseTypeDef:
        """
        [Client.describe_fleet_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_fleet_history)
        """

    def describe_fleet_instances(
        self,
        FleetId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientDescribeFleetInstancesFiltersTypeDef] = None,
    ) -> ClientDescribeFleetInstancesResponseTypeDef:
        """
        [Client.describe_fleet_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_fleet_instances)
        """

    def describe_fleets(
        self,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        FleetIds: List[str] = None,
        Filters: List[ClientDescribeFleetsFiltersTypeDef] = None,
    ) -> ClientDescribeFleetsResponseTypeDef:
        """
        [Client.describe_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_fleets)
        """

    def describe_flow_logs(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeFlowLogsFiltersTypeDef] = None,
        FlowLogIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeFlowLogsResponseTypeDef:
        """
        [Client.describe_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_flow_logs)
        """

    def describe_fpga_image_attribute(
        self,
        FpgaImageId: str,
        Attribute: Literal["description", "name", "loadPermission", "productCodes"],
        DryRun: bool = None,
    ) -> ClientDescribeFpgaImageAttributeResponseTypeDef:
        """
        [Client.describe_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_fpga_image_attribute)
        """

    def describe_fpga_images(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[ClientDescribeFpgaImagesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeFpgaImagesResponseTypeDef:
        """
        [Client.describe_fpga_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_fpga_images)
        """

    def describe_host_reservation_offerings(
        self,
        Filters: List[ClientDescribeHostReservationOfferingsFiltersTypeDef] = None,
        MaxDuration: int = None,
        MaxResults: int = None,
        MinDuration: int = None,
        NextToken: str = None,
        OfferingId: str = None,
    ) -> ClientDescribeHostReservationOfferingsResponseTypeDef:
        """
        [Client.describe_host_reservation_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_host_reservation_offerings)
        """

    def describe_host_reservations(
        self,
        Filters: List[ClientDescribeHostReservationsFiltersTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeHostReservationsResponseTypeDef:
        """
        [Client.describe_host_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_host_reservations)
        """

    def describe_hosts(
        self,
        Filters: List[ClientDescribeHostsFiltersTypeDef] = None,
        HostIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeHostsResponseTypeDef:
        """
        [Client.describe_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_hosts)
        """

    def describe_iam_instance_profile_associations(
        self,
        AssociationIds: List[str] = None,
        Filters: List[ClientDescribeIamInstanceProfileAssociationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeIamInstanceProfileAssociationsResponseTypeDef:
        """
        [Client.describe_iam_instance_profile_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_iam_instance_profile_associations)
        """

    def describe_id_format(self, Resource: str = None) -> ClientDescribeIdFormatResponseTypeDef:
        """
        [Client.describe_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_id_format)
        """

    def describe_identity_id_format(
        self, PrincipalArn: str, Resource: str = None
    ) -> ClientDescribeIdentityIdFormatResponseTypeDef:
        """
        [Client.describe_identity_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_identity_id_format)
        """

    def describe_image_attribute(
        self,
        Attribute: Literal[
            "description",
            "kernel",
            "ramdisk",
            "launchPermission",
            "productCodes",
            "blockDeviceMapping",
            "sriovNetSupport",
        ],
        ImageId: str,
        DryRun: bool = None,
    ) -> ClientDescribeImageAttributeResponseTypeDef:
        """
        [Client.describe_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_image_attribute)
        """

    def describe_images(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[ClientDescribeImagesFiltersTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeImagesResponseTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_images)
        """

    def describe_import_image_tasks(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeImportImageTasksFiltersTypeDef] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeImportImageTasksResponseTypeDef:
        """
        [Client.describe_import_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_import_image_tasks)
        """

    def describe_import_snapshot_tasks(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeImportSnapshotTasksFiltersTypeDef] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeImportSnapshotTasksResponseTypeDef:
        """
        [Client.describe_import_snapshot_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_import_snapshot_tasks)
        """

    def describe_instance_attribute(
        self,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ],
        InstanceId: str,
        DryRun: bool = None,
    ) -> ClientDescribeInstanceAttributeResponseTypeDef:
        """
        [Client.describe_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_instance_attribute)
        """

    def describe_instance_credit_specifications(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeInstanceCreditSpecificationsFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeInstanceCreditSpecificationsResponseTypeDef:
        """
        [Client.describe_instance_credit_specifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_instance_credit_specifications)
        """

    def describe_instance_status(
        self,
        Filters: List[ClientDescribeInstanceStatusFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
    ) -> ClientDescribeInstanceStatusResponseTypeDef:
        """
        [Client.describe_instance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_instance_status)
        """

    def describe_instance_type_offerings(
        self,
        DryRun: bool = None,
        LocationType: Literal["region", "availability-zone", "availability-zone-id"] = None,
        Filters: List[ClientDescribeInstanceTypeOfferingsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeInstanceTypeOfferingsResponseTypeDef:
        """
        [Client.describe_instance_type_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_instance_type_offerings)
        """

    def describe_instance_types(
        self,
        DryRun: bool = None,
        InstanceTypes: List[
            Literal[
                "t1.micro",
                "t2.nano",
                "t2.micro",
                "t2.small",
                "t2.medium",
                "t2.large",
                "t2.xlarge",
                "t2.2xlarge",
                "t3.nano",
                "t3.micro",
                "t3.small",
                "t3.medium",
                "t3.large",
                "t3.xlarge",
                "t3.2xlarge",
                "t3a.nano",
                "t3a.micro",
                "t3a.small",
                "t3a.medium",
                "t3a.large",
                "t3a.xlarge",
                "t3a.2xlarge",
                "m1.small",
                "m1.medium",
                "m1.large",
                "m1.xlarge",
                "m3.medium",
                "m3.large",
                "m3.xlarge",
                "m3.2xlarge",
                "m4.large",
                "m4.xlarge",
                "m4.2xlarge",
                "m4.4xlarge",
                "m4.10xlarge",
                "m4.16xlarge",
                "m2.xlarge",
                "m2.2xlarge",
                "m2.4xlarge",
                "cr1.8xlarge",
                "r3.large",
                "r3.xlarge",
                "r3.2xlarge",
                "r3.4xlarge",
                "r3.8xlarge",
                "r4.large",
                "r4.xlarge",
                "r4.2xlarge",
                "r4.4xlarge",
                "r4.8xlarge",
                "r4.16xlarge",
                "r5.large",
                "r5.xlarge",
                "r5.2xlarge",
                "r5.4xlarge",
                "r5.8xlarge",
                "r5.12xlarge",
                "r5.16xlarge",
                "r5.24xlarge",
                "r5.metal",
                "r5a.large",
                "r5a.xlarge",
                "r5a.2xlarge",
                "r5a.4xlarge",
                "r5a.8xlarge",
                "r5a.12xlarge",
                "r5a.16xlarge",
                "r5a.24xlarge",
                "r5d.large",
                "r5d.xlarge",
                "r5d.2xlarge",
                "r5d.4xlarge",
                "r5d.8xlarge",
                "r5d.12xlarge",
                "r5d.16xlarge",
                "r5d.24xlarge",
                "r5d.metal",
                "r5ad.large",
                "r5ad.xlarge",
                "r5ad.2xlarge",
                "r5ad.4xlarge",
                "r5ad.8xlarge",
                "r5ad.12xlarge",
                "r5ad.16xlarge",
                "r5ad.24xlarge",
                "x1.16xlarge",
                "x1.32xlarge",
                "x1e.xlarge",
                "x1e.2xlarge",
                "x1e.4xlarge",
                "x1e.8xlarge",
                "x1e.16xlarge",
                "x1e.32xlarge",
                "i2.xlarge",
                "i2.2xlarge",
                "i2.4xlarge",
                "i2.8xlarge",
                "i3.large",
                "i3.xlarge",
                "i3.2xlarge",
                "i3.4xlarge",
                "i3.8xlarge",
                "i3.16xlarge",
                "i3.metal",
                "i3en.large",
                "i3en.xlarge",
                "i3en.2xlarge",
                "i3en.3xlarge",
                "i3en.6xlarge",
                "i3en.12xlarge",
                "i3en.24xlarge",
                "i3en.metal",
                "hi1.4xlarge",
                "hs1.8xlarge",
                "c1.medium",
                "c1.xlarge",
                "c3.large",
                "c3.xlarge",
                "c3.2xlarge",
                "c3.4xlarge",
                "c3.8xlarge",
                "c4.large",
                "c4.xlarge",
                "c4.2xlarge",
                "c4.4xlarge",
                "c4.8xlarge",
                "c5.large",
                "c5.xlarge",
                "c5.2xlarge",
                "c5.4xlarge",
                "c5.9xlarge",
                "c5.12xlarge",
                "c5.18xlarge",
                "c5.24xlarge",
                "c5.metal",
                "c5d.large",
                "c5d.xlarge",
                "c5d.2xlarge",
                "c5d.4xlarge",
                "c5d.9xlarge",
                "c5d.12xlarge",
                "c5d.18xlarge",
                "c5d.24xlarge",
                "c5d.metal",
                "c5n.large",
                "c5n.xlarge",
                "c5n.2xlarge",
                "c5n.4xlarge",
                "c5n.9xlarge",
                "c5n.18xlarge",
                "cc1.4xlarge",
                "cc2.8xlarge",
                "g2.2xlarge",
                "g2.8xlarge",
                "g3.4xlarge",
                "g3.8xlarge",
                "g3.16xlarge",
                "g3s.xlarge",
                "g4dn.xlarge",
                "g4dn.2xlarge",
                "g4dn.4xlarge",
                "g4dn.8xlarge",
                "g4dn.12xlarge",
                "g4dn.16xlarge",
                "cg1.4xlarge",
                "p2.xlarge",
                "p2.8xlarge",
                "p2.16xlarge",
                "p3.2xlarge",
                "p3.8xlarge",
                "p3.16xlarge",
                "p3dn.24xlarge",
                "d2.xlarge",
                "d2.2xlarge",
                "d2.4xlarge",
                "d2.8xlarge",
                "f1.2xlarge",
                "f1.4xlarge",
                "f1.16xlarge",
                "m5.large",
                "m5.xlarge",
                "m5.2xlarge",
                "m5.4xlarge",
                "m5.8xlarge",
                "m5.12xlarge",
                "m5.16xlarge",
                "m5.24xlarge",
                "m5.metal",
                "m5a.large",
                "m5a.xlarge",
                "m5a.2xlarge",
                "m5a.4xlarge",
                "m5a.8xlarge",
                "m5a.12xlarge",
                "m5a.16xlarge",
                "m5a.24xlarge",
                "m5d.large",
                "m5d.xlarge",
                "m5d.2xlarge",
                "m5d.4xlarge",
                "m5d.8xlarge",
                "m5d.12xlarge",
                "m5d.16xlarge",
                "m5d.24xlarge",
                "m5d.metal",
                "m5ad.large",
                "m5ad.xlarge",
                "m5ad.2xlarge",
                "m5ad.4xlarge",
                "m5ad.8xlarge",
                "m5ad.12xlarge",
                "m5ad.16xlarge",
                "m5ad.24xlarge",
                "h1.2xlarge",
                "h1.4xlarge",
                "h1.8xlarge",
                "h1.16xlarge",
                "z1d.large",
                "z1d.xlarge",
                "z1d.2xlarge",
                "z1d.3xlarge",
                "z1d.6xlarge",
                "z1d.12xlarge",
                "z1d.metal",
                "u-6tb1.metal",
                "u-9tb1.metal",
                "u-12tb1.metal",
                "u-18tb1.metal",
                "u-24tb1.metal",
                "a1.medium",
                "a1.large",
                "a1.xlarge",
                "a1.2xlarge",
                "a1.4xlarge",
                "a1.metal",
                "m5dn.large",
                "m5dn.xlarge",
                "m5dn.2xlarge",
                "m5dn.4xlarge",
                "m5dn.8xlarge",
                "m5dn.12xlarge",
                "m5dn.16xlarge",
                "m5dn.24xlarge",
                "m5n.large",
                "m5n.xlarge",
                "m5n.2xlarge",
                "m5n.4xlarge",
                "m5n.8xlarge",
                "m5n.12xlarge",
                "m5n.16xlarge",
                "m5n.24xlarge",
                "r5dn.large",
                "r5dn.xlarge",
                "r5dn.2xlarge",
                "r5dn.4xlarge",
                "r5dn.8xlarge",
                "r5dn.12xlarge",
                "r5dn.16xlarge",
                "r5dn.24xlarge",
                "r5n.large",
                "r5n.xlarge",
                "r5n.2xlarge",
                "r5n.4xlarge",
                "r5n.8xlarge",
                "r5n.12xlarge",
                "r5n.16xlarge",
                "r5n.24xlarge",
                "inf1.xlarge",
                "inf1.2xlarge",
                "inf1.6xlarge",
                "inf1.24xlarge",
            ]
        ] = None,
        Filters: List[ClientDescribeInstanceTypesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeInstanceTypesResponseTypeDef:
        """
        [Client.describe_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_instance_types)
        """

    def describe_instances(
        self,
        Filters: List[ClientDescribeInstancesFiltersTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeInstancesResponseTypeDef:
        """
        [Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_instances)
        """

    def describe_internet_gateways(
        self,
        Filters: List[ClientDescribeInternetGatewaysFiltersTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeInternetGatewaysResponseTypeDef:
        """
        [Client.describe_internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_internet_gateways)
        """

    def describe_ipv6_pools(
        self,
        PoolIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
        Filters: List[ClientDescribeIpv6PoolsFiltersTypeDef] = None,
    ) -> ClientDescribeIpv6PoolsResponseTypeDef:
        """
        [Client.describe_ipv6_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_ipv6_pools)
        """

    def describe_key_pairs(
        self,
        Filters: List[ClientDescribeKeyPairsFiltersTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeKeyPairsResponseTypeDef:
        """
        [Client.describe_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_key_pairs)
        """

    def describe_launch_template_versions(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientDescribeLaunchTemplateVersionsFiltersTypeDef] = None,
    ) -> ClientDescribeLaunchTemplateVersionsResponseTypeDef:
        """
        [Client.describe_launch_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_launch_template_versions)
        """

    def describe_launch_templates(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[ClientDescribeLaunchTemplatesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeLaunchTemplatesResponseTypeDef:
        """
        [Client.describe_launch_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_launch_templates)
        """

    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List[
            ClientDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsFiltersTypeDef
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResponseTypeDef:
        """
        [Client.describe_local_gateway_route_table_virtual_interface_group_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_virtual_interface_group_associations)
        """

    def describe_local_gateway_route_table_vpc_associations(
        self,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List[ClientDescribeLocalGatewayRouteTableVpcAssociationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeLocalGatewayRouteTableVpcAssociationsResponseTypeDef:
        """
        [Client.describe_local_gateway_route_table_vpc_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_vpc_associations)
        """

    def describe_local_gateway_route_tables(
        self,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List[ClientDescribeLocalGatewayRouteTablesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeLocalGatewayRouteTablesResponseTypeDef:
        """
        [Client.describe_local_gateway_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_tables)
        """

    def describe_local_gateway_virtual_interface_groups(
        self,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List[ClientDescribeLocalGatewayVirtualInterfaceGroupsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeLocalGatewayVirtualInterfaceGroupsResponseTypeDef:
        """
        [Client.describe_local_gateway_virtual_interface_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interface_groups)
        """

    def describe_local_gateway_virtual_interfaces(
        self,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List[ClientDescribeLocalGatewayVirtualInterfacesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeLocalGatewayVirtualInterfacesResponseTypeDef:
        """
        [Client.describe_local_gateway_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interfaces)
        """

    def describe_local_gateways(
        self,
        LocalGatewayIds: List[str] = None,
        Filters: List[ClientDescribeLocalGatewaysFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeLocalGatewaysResponseTypeDef:
        """
        [Client.describe_local_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_local_gateways)
        """

    def describe_moving_addresses(
        self,
        Filters: List[ClientDescribeMovingAddressesFiltersTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        PublicIps: List[str] = None,
    ) -> ClientDescribeMovingAddressesResponseTypeDef:
        """
        [Client.describe_moving_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_moving_addresses)
        """

    def describe_nat_gateways(
        self,
        Filters: List[ClientDescribeNatGatewaysFiltersTypeDef] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None,
    ) -> ClientDescribeNatGatewaysResponseTypeDef:
        """
        [Client.describe_nat_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_nat_gateways)
        """

    def describe_network_acls(
        self,
        Filters: List[ClientDescribeNetworkAclsFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeNetworkAclsResponseTypeDef:
        """
        [Client.describe_network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_network_acls)
        """

    def describe_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attribute: Literal["description", "groupSet", "sourceDestCheck", "attachment"] = None,
        DryRun: bool = None,
    ) -> ClientDescribeNetworkInterfaceAttributeResponseTypeDef:
        """
        [Client.describe_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_network_interface_attribute)
        """

    def describe_network_interface_permissions(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[ClientDescribeNetworkInterfacePermissionsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeNetworkInterfacePermissionsResponseTypeDef:
        """
        [Client.describe_network_interface_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_network_interface_permissions)
        """

    def describe_network_interfaces(
        self,
        Filters: List[ClientDescribeNetworkInterfacesFiltersTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeNetworkInterfacesResponseTypeDef:
        """
        [Client.describe_network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_network_interfaces)
        """

    def describe_placement_groups(
        self,
        Filters: List[ClientDescribePlacementGroupsFiltersTypeDef] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
        GroupIds: List[str] = None,
    ) -> ClientDescribePlacementGroupsResponseTypeDef:
        """
        [Client.describe_placement_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_placement_groups)
        """

    def describe_prefix_lists(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribePrefixListsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        PrefixListIds: List[str] = None,
    ) -> ClientDescribePrefixListsResponseTypeDef:
        """
        [Client.describe_prefix_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_prefix_lists)
        """

    def describe_principal_id_format(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribePrincipalIdFormatResponseTypeDef:
        """
        [Client.describe_principal_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_principal_id_format)
        """

    def describe_public_ipv4_pools(
        self, PoolIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribePublicIpv4PoolsResponseTypeDef:
        """
        [Client.describe_public_ipv4_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_public_ipv4_pools)
        """

    def describe_regions(
        self,
        Filters: List[ClientDescribeRegionsFiltersTypeDef] = None,
        RegionNames: List[str] = None,
        DryRun: bool = None,
        AllRegions: bool = None,
    ) -> ClientDescribeRegionsResponseTypeDef:
        """
        [Client.describe_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_regions)
        """

    def describe_reserved_instances(
        self,
        Filters: List[ClientDescribeReservedInstancesFiltersTypeDef] = None,
        OfferingClass: Literal["standard", "convertible"] = None,
        ReservedInstancesIds: List[str] = None,
        DryRun: bool = None,
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
    ) -> ClientDescribeReservedInstancesResponseTypeDef:
        """
        [Client.describe_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_reserved_instances)
        """

    def describe_reserved_instances_listings(
        self,
        Filters: List[ClientDescribeReservedInstancesListingsFiltersTypeDef] = None,
        ReservedInstancesId: str = None,
        ReservedInstancesListingId: str = None,
    ) -> ClientDescribeReservedInstancesListingsResponseTypeDef:
        """
        [Client.describe_reserved_instances_listings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_reserved_instances_listings)
        """

    def describe_reserved_instances_modifications(
        self,
        Filters: List[ClientDescribeReservedInstancesModificationsFiltersTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        NextToken: str = None,
    ) -> ClientDescribeReservedInstancesModificationsResponseTypeDef:
        """
        [Client.describe_reserved_instances_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_reserved_instances_modifications)
        """

    def describe_reserved_instances_offerings(
        self,
        AvailabilityZone: str = None,
        Filters: List[ClientDescribeReservedInstancesOfferingsFiltersTypeDef] = None,
        IncludeMarketplace: bool = None,
        InstanceType: Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
        ] = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: Literal["standard", "convertible"] = None,
        ProductDescription: Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ] = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
    ) -> ClientDescribeReservedInstancesOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_instances_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_reserved_instances_offerings)
        """

    def describe_route_tables(
        self,
        Filters: List[ClientDescribeRouteTablesFiltersTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeRouteTablesResponseTypeDef:
        """
        [Client.describe_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_route_tables)
        """

    def describe_scheduled_instance_availability(
        self,
        FirstSlotStartTimeRange: ClientDescribeScheduledInstanceAvailabilityFirstSlotStartTimeRangeTypeDef,
        Recurrence: ClientDescribeScheduledInstanceAvailabilityRecurrenceTypeDef,
        DryRun: bool = None,
        Filters: List[ClientDescribeScheduledInstanceAvailabilityFiltersTypeDef] = None,
        MaxResults: int = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScheduledInstanceAvailabilityResponseTypeDef:
        """
        [Client.describe_scheduled_instance_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_scheduled_instance_availability)
        """

    def describe_scheduled_instances(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeScheduledInstancesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: ClientDescribeScheduledInstancesSlotStartTimeRangeTypeDef = None,
    ) -> ClientDescribeScheduledInstancesResponseTypeDef:
        """
        [Client.describe_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_scheduled_instances)
        """

    def describe_security_group_references(
        self, GroupId: List[str], DryRun: bool = None
    ) -> ClientDescribeSecurityGroupReferencesResponseTypeDef:
        """
        [Client.describe_security_group_references documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_security_group_references)
        """

    def describe_security_groups(
        self,
        Filters: List[ClientDescribeSecurityGroupsFiltersTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeSecurityGroupsResponseTypeDef:
        """
        [Client.describe_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_security_groups)
        """

    def describe_snapshot_attribute(
        self,
        Attribute: Literal["productCodes", "createVolumePermission"],
        SnapshotId: str,
        DryRun: bool = None,
    ) -> ClientDescribeSnapshotAttributeResponseTypeDef:
        """
        [Client.describe_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_snapshot_attribute)
        """

    def describe_snapshots(
        self,
        Filters: List[ClientDescribeSnapshotsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeSnapshotsResponseTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_snapshots)
        """

    def describe_spot_datafeed_subscription(
        self, DryRun: bool = None
    ) -> ClientDescribeSpotDatafeedSubscriptionResponseTypeDef:
        """
        [Client.describe_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_spot_datafeed_subscription)
        """

    def describe_spot_fleet_instances(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeSpotFleetInstancesResponseTypeDef:
        """
        [Client.describe_spot_fleet_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_spot_fleet_instances)
        """

    def describe_spot_fleet_request_history(
        self,
        SpotFleetRequestId: str,
        StartTime: datetime,
        DryRun: bool = None,
        EventType: Literal["instanceChange", "fleetRequestChange", "error", "information"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeSpotFleetRequestHistoryResponseTypeDef:
        """
        [Client.describe_spot_fleet_request_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_spot_fleet_request_history)
        """

    def describe_spot_fleet_requests(
        self,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        SpotFleetRequestIds: List[str] = None,
    ) -> ClientDescribeSpotFleetRequestsResponseTypeDef:
        """
        [Client.describe_spot_fleet_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_spot_fleet_requests)
        """

    def describe_spot_instance_requests(
        self,
        Filters: List[ClientDescribeSpotInstanceRequestsFiltersTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeSpotInstanceRequestsResponseTypeDef:
        """
        [Client.describe_spot_instance_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests)
        """

    def describe_spot_price_history(
        self,
        Filters: List[ClientDescribeSpotPriceHistoryFiltersTypeDef] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[
            Literal[
                "t1.micro",
                "t2.nano",
                "t2.micro",
                "t2.small",
                "t2.medium",
                "t2.large",
                "t2.xlarge",
                "t2.2xlarge",
                "t3.nano",
                "t3.micro",
                "t3.small",
                "t3.medium",
                "t3.large",
                "t3.xlarge",
                "t3.2xlarge",
                "t3a.nano",
                "t3a.micro",
                "t3a.small",
                "t3a.medium",
                "t3a.large",
                "t3a.xlarge",
                "t3a.2xlarge",
                "m1.small",
                "m1.medium",
                "m1.large",
                "m1.xlarge",
                "m3.medium",
                "m3.large",
                "m3.xlarge",
                "m3.2xlarge",
                "m4.large",
                "m4.xlarge",
                "m4.2xlarge",
                "m4.4xlarge",
                "m4.10xlarge",
                "m4.16xlarge",
                "m2.xlarge",
                "m2.2xlarge",
                "m2.4xlarge",
                "cr1.8xlarge",
                "r3.large",
                "r3.xlarge",
                "r3.2xlarge",
                "r3.4xlarge",
                "r3.8xlarge",
                "r4.large",
                "r4.xlarge",
                "r4.2xlarge",
                "r4.4xlarge",
                "r4.8xlarge",
                "r4.16xlarge",
                "r5.large",
                "r5.xlarge",
                "r5.2xlarge",
                "r5.4xlarge",
                "r5.8xlarge",
                "r5.12xlarge",
                "r5.16xlarge",
                "r5.24xlarge",
                "r5.metal",
                "r5a.large",
                "r5a.xlarge",
                "r5a.2xlarge",
                "r5a.4xlarge",
                "r5a.8xlarge",
                "r5a.12xlarge",
                "r5a.16xlarge",
                "r5a.24xlarge",
                "r5d.large",
                "r5d.xlarge",
                "r5d.2xlarge",
                "r5d.4xlarge",
                "r5d.8xlarge",
                "r5d.12xlarge",
                "r5d.16xlarge",
                "r5d.24xlarge",
                "r5d.metal",
                "r5ad.large",
                "r5ad.xlarge",
                "r5ad.2xlarge",
                "r5ad.4xlarge",
                "r5ad.8xlarge",
                "r5ad.12xlarge",
                "r5ad.16xlarge",
                "r5ad.24xlarge",
                "x1.16xlarge",
                "x1.32xlarge",
                "x1e.xlarge",
                "x1e.2xlarge",
                "x1e.4xlarge",
                "x1e.8xlarge",
                "x1e.16xlarge",
                "x1e.32xlarge",
                "i2.xlarge",
                "i2.2xlarge",
                "i2.4xlarge",
                "i2.8xlarge",
                "i3.large",
                "i3.xlarge",
                "i3.2xlarge",
                "i3.4xlarge",
                "i3.8xlarge",
                "i3.16xlarge",
                "i3.metal",
                "i3en.large",
                "i3en.xlarge",
                "i3en.2xlarge",
                "i3en.3xlarge",
                "i3en.6xlarge",
                "i3en.12xlarge",
                "i3en.24xlarge",
                "i3en.metal",
                "hi1.4xlarge",
                "hs1.8xlarge",
                "c1.medium",
                "c1.xlarge",
                "c3.large",
                "c3.xlarge",
                "c3.2xlarge",
                "c3.4xlarge",
                "c3.8xlarge",
                "c4.large",
                "c4.xlarge",
                "c4.2xlarge",
                "c4.4xlarge",
                "c4.8xlarge",
                "c5.large",
                "c5.xlarge",
                "c5.2xlarge",
                "c5.4xlarge",
                "c5.9xlarge",
                "c5.12xlarge",
                "c5.18xlarge",
                "c5.24xlarge",
                "c5.metal",
                "c5d.large",
                "c5d.xlarge",
                "c5d.2xlarge",
                "c5d.4xlarge",
                "c5d.9xlarge",
                "c5d.12xlarge",
                "c5d.18xlarge",
                "c5d.24xlarge",
                "c5d.metal",
                "c5n.large",
                "c5n.xlarge",
                "c5n.2xlarge",
                "c5n.4xlarge",
                "c5n.9xlarge",
                "c5n.18xlarge",
                "cc1.4xlarge",
                "cc2.8xlarge",
                "g2.2xlarge",
                "g2.8xlarge",
                "g3.4xlarge",
                "g3.8xlarge",
                "g3.16xlarge",
                "g3s.xlarge",
                "g4dn.xlarge",
                "g4dn.2xlarge",
                "g4dn.4xlarge",
                "g4dn.8xlarge",
                "g4dn.12xlarge",
                "g4dn.16xlarge",
                "cg1.4xlarge",
                "p2.xlarge",
                "p2.8xlarge",
                "p2.16xlarge",
                "p3.2xlarge",
                "p3.8xlarge",
                "p3.16xlarge",
                "p3dn.24xlarge",
                "d2.xlarge",
                "d2.2xlarge",
                "d2.4xlarge",
                "d2.8xlarge",
                "f1.2xlarge",
                "f1.4xlarge",
                "f1.16xlarge",
                "m5.large",
                "m5.xlarge",
                "m5.2xlarge",
                "m5.4xlarge",
                "m5.8xlarge",
                "m5.12xlarge",
                "m5.16xlarge",
                "m5.24xlarge",
                "m5.metal",
                "m5a.large",
                "m5a.xlarge",
                "m5a.2xlarge",
                "m5a.4xlarge",
                "m5a.8xlarge",
                "m5a.12xlarge",
                "m5a.16xlarge",
                "m5a.24xlarge",
                "m5d.large",
                "m5d.xlarge",
                "m5d.2xlarge",
                "m5d.4xlarge",
                "m5d.8xlarge",
                "m5d.12xlarge",
                "m5d.16xlarge",
                "m5d.24xlarge",
                "m5d.metal",
                "m5ad.large",
                "m5ad.xlarge",
                "m5ad.2xlarge",
                "m5ad.4xlarge",
                "m5ad.8xlarge",
                "m5ad.12xlarge",
                "m5ad.16xlarge",
                "m5ad.24xlarge",
                "h1.2xlarge",
                "h1.4xlarge",
                "h1.8xlarge",
                "h1.16xlarge",
                "z1d.large",
                "z1d.xlarge",
                "z1d.2xlarge",
                "z1d.3xlarge",
                "z1d.6xlarge",
                "z1d.12xlarge",
                "z1d.metal",
                "u-6tb1.metal",
                "u-9tb1.metal",
                "u-12tb1.metal",
                "u-18tb1.metal",
                "u-24tb1.metal",
                "a1.medium",
                "a1.large",
                "a1.xlarge",
                "a1.2xlarge",
                "a1.4xlarge",
                "a1.metal",
                "m5dn.large",
                "m5dn.xlarge",
                "m5dn.2xlarge",
                "m5dn.4xlarge",
                "m5dn.8xlarge",
                "m5dn.12xlarge",
                "m5dn.16xlarge",
                "m5dn.24xlarge",
                "m5n.large",
                "m5n.xlarge",
                "m5n.2xlarge",
                "m5n.4xlarge",
                "m5n.8xlarge",
                "m5n.12xlarge",
                "m5n.16xlarge",
                "m5n.24xlarge",
                "r5dn.large",
                "r5dn.xlarge",
                "r5dn.2xlarge",
                "r5dn.4xlarge",
                "r5dn.8xlarge",
                "r5dn.12xlarge",
                "r5dn.16xlarge",
                "r5dn.24xlarge",
                "r5n.large",
                "r5n.xlarge",
                "r5n.2xlarge",
                "r5n.4xlarge",
                "r5n.8xlarge",
                "r5n.12xlarge",
                "r5n.16xlarge",
                "r5n.24xlarge",
                "inf1.xlarge",
                "inf1.2xlarge",
                "inf1.6xlarge",
                "inf1.24xlarge",
            ]
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
    ) -> ClientDescribeSpotPriceHistoryResponseTypeDef:
        """
        [Client.describe_spot_price_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_spot_price_history)
        """

    def describe_stale_security_groups(
        self, VpcId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeStaleSecurityGroupsResponseTypeDef:
        """
        [Client.describe_stale_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_stale_security_groups)
        """

    def describe_subnets(
        self,
        Filters: List[ClientDescribeSubnetsFiltersTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeSubnetsResponseTypeDef:
        """
        [Client.describe_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_subnets)
        """

    def describe_tags(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeTagsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_tags)
        """

    def describe_traffic_mirror_filters(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[ClientDescribeTrafficMirrorFiltersFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeTrafficMirrorFiltersResponseTypeDef:
        """
        [Client.describe_traffic_mirror_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filters)
        """

    def describe_traffic_mirror_sessions(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[ClientDescribeTrafficMirrorSessionsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeTrafficMirrorSessionsResponseTypeDef:
        """
        [Client.describe_traffic_mirror_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_sessions)
        """

    def describe_traffic_mirror_targets(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[ClientDescribeTrafficMirrorTargetsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeTrafficMirrorTargetsResponseTypeDef:
        """
        [Client.describe_traffic_mirror_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_targets)
        """

    def describe_transit_gateway_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[ClientDescribeTransitGatewayAttachmentsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeTransitGatewayAttachmentsResponseTypeDef:
        """
        [Client.describe_transit_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_transit_gateway_attachments)
        """

    def describe_transit_gateway_multicast_domains(
        self,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List[ClientDescribeTransitGatewayMulticastDomainsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeTransitGatewayMulticastDomainsResponseTypeDef:
        """
        [Client.describe_transit_gateway_multicast_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_transit_gateway_multicast_domains)
        """

    def describe_transit_gateway_peering_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[ClientDescribeTransitGatewayPeeringAttachmentsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeTransitGatewayPeeringAttachmentsResponseTypeDef:
        """
        [Client.describe_transit_gateway_peering_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_transit_gateway_peering_attachments)
        """

    def describe_transit_gateway_route_tables(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[ClientDescribeTransitGatewayRouteTablesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeTransitGatewayRouteTablesResponseTypeDef:
        """
        [Client.describe_transit_gateway_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_tables)
        """

    def describe_transit_gateway_vpc_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[ClientDescribeTransitGatewayVpcAttachmentsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeTransitGatewayVpcAttachmentsResponseTypeDef:
        """
        [Client.describe_transit_gateway_vpc_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_transit_gateway_vpc_attachments)
        """

    def describe_transit_gateways(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[ClientDescribeTransitGatewaysFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientDescribeTransitGatewaysResponseTypeDef:
        """
        [Client.describe_transit_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_transit_gateways)
        """

    def describe_volume_attribute(
        self, Attribute: Literal["autoEnableIO", "productCodes"], VolumeId: str, DryRun: bool = None
    ) -> ClientDescribeVolumeAttributeResponseTypeDef:
        """
        [Client.describe_volume_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_volume_attribute)
        """

    def describe_volume_status(
        self,
        Filters: List[ClientDescribeVolumeStatusFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeVolumeStatusResponseTypeDef:
        """
        [Client.describe_volume_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_volume_status)
        """

    def describe_volumes(
        self,
        Filters: List[ClientDescribeVolumesFiltersTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVolumesResponseTypeDef:
        """
        [Client.describe_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_volumes)
        """

    def describe_volumes_modifications(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[ClientDescribeVolumesModificationsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeVolumesModificationsResponseTypeDef:
        """
        [Client.describe_volumes_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_volumes_modifications)
        """

    def describe_vpc_attribute(
        self,
        Attribute: Literal["enableDnsSupport", "enableDnsHostnames"],
        VpcId: str,
        DryRun: bool = None,
    ) -> ClientDescribeVpcAttributeResponseTypeDef:
        """
        [Client.describe_vpc_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_attribute)
        """

    def describe_vpc_classic_link(
        self,
        Filters: List[ClientDescribeVpcClassicLinkFiltersTypeDef] = None,
        DryRun: bool = None,
        VpcIds: List[str] = None,
    ) -> ClientDescribeVpcClassicLinkResponseTypeDef:
        """
        [Client.describe_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link)
        """

    def describe_vpc_classic_link_dns_support(
        self, MaxResults: int = None, NextToken: str = None, VpcIds: List[str] = None
    ) -> ClientDescribeVpcClassicLinkDnsSupportResponseTypeDef:
        """
        [Client.describe_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link_dns_support)
        """

    def describe_vpc_endpoint_connection_notifications(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[ClientDescribeVpcEndpointConnectionNotificationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVpcEndpointConnectionNotificationsResponseTypeDef:
        """
        [Client.describe_vpc_endpoint_connection_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connection_notifications)
        """

    def describe_vpc_endpoint_connections(
        self,
        DryRun: bool = None,
        Filters: List[ClientDescribeVpcEndpointConnectionsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVpcEndpointConnectionsResponseTypeDef:
        """
        [Client.describe_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connections)
        """

    def describe_vpc_endpoint_service_configurations(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[ClientDescribeVpcEndpointServiceConfigurationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVpcEndpointServiceConfigurationsResponseTypeDef:
        """
        [Client.describe_vpc_endpoint_service_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_configurations)
        """

    def describe_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[ClientDescribeVpcEndpointServicePermissionsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVpcEndpointServicePermissionsResponseTypeDef:
        """
        [Client.describe_vpc_endpoint_service_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_permissions)
        """

    def describe_vpc_endpoint_services(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[ClientDescribeVpcEndpointServicesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVpcEndpointServicesResponseTypeDef:
        """
        [Client.describe_vpc_endpoint_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_services)
        """

    def describe_vpc_endpoints(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[ClientDescribeVpcEndpointsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeVpcEndpointsResponseTypeDef:
        """
        [Client.describe_vpc_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_endpoints)
        """

    def describe_vpc_peering_connections(
        self,
        Filters: List[ClientDescribeVpcPeeringConnectionsFiltersTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeVpcPeeringConnectionsResponseTypeDef:
        """
        [Client.describe_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpc_peering_connections)
        """

    def describe_vpcs(
        self,
        Filters: List[ClientDescribeVpcsFiltersTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeVpcsResponseTypeDef:
        """
        [Client.describe_vpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpcs)
        """

    def describe_vpn_connections(
        self,
        Filters: List[ClientDescribeVpnConnectionsFiltersTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeVpnConnectionsResponseTypeDef:
        """
        [Client.describe_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpn_connections)
        """

    def describe_vpn_gateways(
        self,
        Filters: List[ClientDescribeVpnGatewaysFiltersTypeDef] = None,
        VpnGatewayIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDescribeVpnGatewaysResponseTypeDef:
        """
        [Client.describe_vpn_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.describe_vpn_gateways)
        """

    def detach_classic_link_vpc(
        self, InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> ClientDetachClassicLinkVpcResponseTypeDef:
        """
        [Client.detach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.detach_classic_link_vpc)
        """

    def detach_internet_gateway(
        self, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        [Client.detach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.detach_internet_gateway)
        """

    def detach_network_interface(
        self, AttachmentId: str, DryRun: bool = None, Force: bool = None
    ) -> None:
        """
        [Client.detach_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.detach_network_interface)
        """

    def detach_volume(
        self,
        VolumeId: str,
        Device: str = None,
        Force: bool = None,
        InstanceId: str = None,
        DryRun: bool = None,
    ) -> ClientDetachVolumeResponseTypeDef:
        """
        [Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.detach_volume)
        """

    def detach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.detach_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.detach_vpn_gateway)
        """

    def disable_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> ClientDisableEbsEncryptionByDefaultResponseTypeDef:
        """
        [Client.disable_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disable_ebs_encryption_by_default)
        """

    def disable_fast_snapshot_restores(
        self, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> ClientDisableFastSnapshotRestoresResponseTypeDef:
        """
        [Client.disable_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disable_fast_snapshot_restores)
        """

    def disable_transit_gateway_route_table_propagation(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientDisableTransitGatewayRouteTablePropagationResponseTypeDef:
        """
        [Client.disable_transit_gateway_route_table_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disable_transit_gateway_route_table_propagation)
        """

    def disable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str) -> None:
        """
        [Client.disable_vgw_route_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disable_vgw_route_propagation)
        """

    def disable_vpc_classic_link(
        self, VpcId: str, DryRun: bool = None
    ) -> ClientDisableVpcClassicLinkResponseTypeDef:
        """
        [Client.disable_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link)
        """

    def disable_vpc_classic_link_dns_support(
        self, VpcId: str = None
    ) -> ClientDisableVpcClassicLinkDnsSupportResponseTypeDef:
        """
        [Client.disable_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link_dns_support)
        """

    def disassociate_address(
        self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        [Client.disassociate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_address)
        """

    def disassociate_client_vpn_target_network(
        self, ClientVpnEndpointId: str, AssociationId: str, DryRun: bool = None
    ) -> ClientDisassociateClientVpnTargetNetworkResponseTypeDef:
        """
        [Client.disassociate_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_client_vpn_target_network)
        """

    def disassociate_iam_instance_profile(
        self, AssociationId: str
    ) -> ClientDisassociateIamInstanceProfileResponseTypeDef:
        """
        [Client.disassociate_iam_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_iam_instance_profile)
        """

    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        """
        [Client.disassociate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_route_table)
        """

    def disassociate_subnet_cidr_block(
        self, AssociationId: str
    ) -> ClientDisassociateSubnetCidrBlockResponseTypeDef:
        """
        [Client.disassociate_subnet_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_subnet_cidr_block)
        """

    def disassociate_transit_gateway_multicast_domain(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientDisassociateTransitGatewayMulticastDomainResponseTypeDef:
        """
        [Client.disassociate_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_multicast_domain)
        """

    def disassociate_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientDisassociateTransitGatewayRouteTableResponseTypeDef:
        """
        [Client.disassociate_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_route_table)
        """

    def disassociate_vpc_cidr_block(
        self, AssociationId: str
    ) -> ClientDisassociateVpcCidrBlockResponseTypeDef:
        """
        [Client.disassociate_vpc_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.disassociate_vpc_cidr_block)
        """

    def enable_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> ClientEnableEbsEncryptionByDefaultResponseTypeDef:
        """
        [Client.enable_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_ebs_encryption_by_default)
        """

    def enable_fast_snapshot_restores(
        self, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> ClientEnableFastSnapshotRestoresResponseTypeDef:
        """
        [Client.enable_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_fast_snapshot_restores)
        """

    def enable_transit_gateway_route_table_propagation(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientEnableTransitGatewayRouteTablePropagationResponseTypeDef:
        """
        [Client.enable_transit_gateway_route_table_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_transit_gateway_route_table_propagation)
        """

    def enable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str) -> None:
        """
        [Client.enable_vgw_route_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_vgw_route_propagation)
        """

    def enable_volume_io(self, VolumeId: str, DryRun: bool = None) -> None:
        """
        [Client.enable_volume_io documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_volume_io)
        """

    def enable_vpc_classic_link(
        self, VpcId: str, DryRun: bool = None
    ) -> ClientEnableVpcClassicLinkResponseTypeDef:
        """
        [Client.enable_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link)
        """

    def enable_vpc_classic_link_dns_support(
        self, VpcId: str = None
    ) -> ClientEnableVpcClassicLinkDnsSupportResponseTypeDef:
        """
        [Client.enable_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link_dns_support)
        """

    def export_client_vpn_client_certificate_revocation_list(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ClientExportClientVpnClientCertificateRevocationListResponseTypeDef:
        """
        [Client.export_client_vpn_client_certificate_revocation_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.export_client_vpn_client_certificate_revocation_list)
        """

    def export_client_vpn_client_configuration(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ClientExportClientVpnClientConfigurationResponseTypeDef:
        """
        [Client.export_client_vpn_client_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.export_client_vpn_client_configuration)
        """

    def export_image(
        self,
        DiskImageFormat: Literal["VMDK", "RAW", "VHD"],
        ImageId: str,
        S3ExportLocation: ClientExportImageS3ExportLocationTypeDef,
        ClientToken: str = None,
        Description: str = None,
        DryRun: bool = None,
        RoleName: str = None,
    ) -> ClientExportImageResponseTypeDef:
        """
        [Client.export_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.export_image)
        """

    def export_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: List[ClientExportTransitGatewayRoutesFiltersTypeDef] = None,
        DryRun: bool = None,
    ) -> ClientExportTransitGatewayRoutesResponseTypeDef:
        """
        [Client.export_transit_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.export_transit_gateway_routes)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.generate_presigned_url)
        """

    def get_associated_ipv6_pool_cidrs(
        self, PoolId: str, NextToken: str = None, MaxResults: int = None, DryRun: bool = None
    ) -> ClientGetAssociatedIpv6PoolCidrsResponseTypeDef:
        """
        [Client.get_associated_ipv6_pool_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_associated_ipv6_pool_cidrs)
        """

    def get_capacity_reservation_usage(
        self,
        CapacityReservationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> ClientGetCapacityReservationUsageResponseTypeDef:
        """
        [Client.get_capacity_reservation_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_capacity_reservation_usage)
        """

    def get_coip_pool_usage(
        self,
        PoolId: str,
        Filters: List[ClientGetCoipPoolUsageFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientGetCoipPoolUsageResponseTypeDef:
        """
        [Client.get_coip_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_coip_pool_usage)
        """

    def get_console_output(
        self, InstanceId: str, DryRun: bool = None, Latest: bool = None
    ) -> ClientGetConsoleOutputResponseTypeDef:
        """
        [Client.get_console_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_console_output)
        """

    def get_console_screenshot(
        self, InstanceId: str, DryRun: bool = None, WakeUp: bool = None
    ) -> ClientGetConsoleScreenshotResponseTypeDef:
        """
        [Client.get_console_screenshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_console_screenshot)
        """

    def get_default_credit_specification(
        self, InstanceFamily: Literal["t2", "t3", "t3a"], DryRun: bool = None
    ) -> ClientGetDefaultCreditSpecificationResponseTypeDef:
        """
        [Client.get_default_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_default_credit_specification)
        """

    def get_ebs_default_kms_key_id(
        self, DryRun: bool = None
    ) -> ClientGetEbsDefaultKmsKeyIdResponseTypeDef:
        """
        [Client.get_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_ebs_default_kms_key_id)
        """

    def get_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> ClientGetEbsEncryptionByDefaultResponseTypeDef:
        """
        [Client.get_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_ebs_encryption_by_default)
        """

    def get_host_reservation_purchase_preview(
        self, HostIdSet: List[str], OfferingId: str
    ) -> ClientGetHostReservationPurchasePreviewResponseTypeDef:
        """
        [Client.get_host_reservation_purchase_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_host_reservation_purchase_preview)
        """

    def get_launch_template_data(
        self, InstanceId: str, DryRun: bool = None
    ) -> ClientGetLaunchTemplateDataResponseTypeDef:
        """
        [Client.get_launch_template_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_launch_template_data)
        """

    def get_password_data(
        self, InstanceId: str, DryRun: bool = None
    ) -> ClientGetPasswordDataResponseTypeDef:
        """
        [Client.get_password_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_password_data)
        """

    def get_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List[
            ClientGetReservedInstancesExchangeQuoteTargetConfigurationsTypeDef
        ] = None,
    ) -> ClientGetReservedInstancesExchangeQuoteResponseTypeDef:
        """
        [Client.get_reserved_instances_exchange_quote documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_reserved_instances_exchange_quote)
        """

    def get_transit_gateway_attachment_propagations(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[ClientGetTransitGatewayAttachmentPropagationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientGetTransitGatewayAttachmentPropagationsResponseTypeDef:
        """
        [Client.get_transit_gateway_attachment_propagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_transit_gateway_attachment_propagations)
        """

    def get_transit_gateway_multicast_domain_associations(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[ClientGetTransitGatewayMulticastDomainAssociationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientGetTransitGatewayMulticastDomainAssociationsResponseTypeDef:
        """
        [Client.get_transit_gateway_multicast_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_transit_gateway_multicast_domain_associations)
        """

    def get_transit_gateway_route_table_associations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[ClientGetTransitGatewayRouteTableAssociationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientGetTransitGatewayRouteTableAssociationsResponseTypeDef:
        """
        [Client.get_transit_gateway_route_table_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_associations)
        """

    def get_transit_gateway_route_table_propagations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[ClientGetTransitGatewayRouteTablePropagationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientGetTransitGatewayRouteTablePropagationsResponseTypeDef:
        """
        [Client.get_transit_gateway_route_table_propagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_propagations)
        """

    def import_client_vpn_client_certificate_revocation_list(
        self, ClientVpnEndpointId: str, CertificateRevocationList: str, DryRun: bool = None
    ) -> ClientImportClientVpnClientCertificateRevocationListResponseTypeDef:
        """
        [Client.import_client_vpn_client_certificate_revocation_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.import_client_vpn_client_certificate_revocation_list)
        """

    def import_image(
        self,
        Architecture: str = None,
        ClientData: ClientImportImageClientDataTypeDef = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainers: List[ClientImportImageDiskContainersTypeDef] = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        Hypervisor: str = None,
        KmsKeyId: str = None,
        LicenseType: str = None,
        Platform: str = None,
        RoleName: str = None,
        LicenseSpecifications: List[ClientImportImageLicenseSpecificationsTypeDef] = None,
    ) -> ClientImportImageResponseTypeDef:
        """
        [Client.import_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.import_image)
        """

    def import_instance(
        self,
        Platform: str,
        Description: str = None,
        DiskImages: List[ClientImportInstanceDiskImagesTypeDef] = None,
        DryRun: bool = None,
        LaunchSpecification: ClientImportInstanceLaunchSpecificationTypeDef = None,
    ) -> ClientImportInstanceResponseTypeDef:
        """
        [Client.import_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.import_instance)
        """

    def import_key_pair(
        self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None
    ) -> ClientImportKeyPairResponseTypeDef:
        """
        [Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.import_key_pair)
        """

    def import_snapshot(
        self,
        ClientData: ClientImportSnapshotClientDataTypeDef = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainer: ClientImportSnapshotDiskContainerTypeDef = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        RoleName: str = None,
    ) -> ClientImportSnapshotResponseTypeDef:
        """
        [Client.import_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.import_snapshot)
        """

    def import_volume(
        self,
        AvailabilityZone: str,
        Image: ClientImportVolumeImageTypeDef,
        Volume: ClientImportVolumeVolumeTypeDef,
        Description: str = None,
        DryRun: bool = None,
    ) -> ClientImportVolumeResponseTypeDef:
        """
        [Client.import_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.import_volume)
        """

    def modify_capacity_reservation(
        self,
        CapacityReservationId: str,
        InstanceCount: int = None,
        EndDate: datetime = None,
        EndDateType: Literal["unlimited", "limited"] = None,
        DryRun: bool = None,
    ) -> ClientModifyCapacityReservationResponseTypeDef:
        """
        [Client.modify_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_capacity_reservation)
        """

    def modify_client_vpn_endpoint(
        self,
        ClientVpnEndpointId: str,
        ServerCertificateArn: str = None,
        ConnectionLogOptions: ClientModifyClientVpnEndpointConnectionLogOptionsTypeDef = None,
        DnsServers: ClientModifyClientVpnEndpointDnsServersTypeDef = None,
        VpnPort: int = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
    ) -> ClientModifyClientVpnEndpointResponseTypeDef:
        """
        [Client.modify_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_client_vpn_endpoint)
        """

    def modify_default_credit_specification(
        self, InstanceFamily: Literal["t2", "t3", "t3a"], CpuCredits: str, DryRun: bool = None
    ) -> ClientModifyDefaultCreditSpecificationResponseTypeDef:
        """
        [Client.modify_default_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_default_credit_specification)
        """

    def modify_ebs_default_kms_key_id(
        self, KmsKeyId: str, DryRun: bool = None
    ) -> ClientModifyEbsDefaultKmsKeyIdResponseTypeDef:
        """
        [Client.modify_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_ebs_default_kms_key_id)
        """

    def modify_fleet(
        self,
        FleetId: str,
        TargetCapacitySpecification: ClientModifyFleetTargetCapacitySpecificationTypeDef,
        DryRun: bool = None,
        ExcessCapacityTerminationPolicy: Literal["no-termination", "termination"] = None,
    ) -> ClientModifyFleetResponseTypeDef:
        """
        [Client.modify_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_fleet)
        """

    def modify_fpga_image_attribute(
        self,
        FpgaImageId: str,
        DryRun: bool = None,
        Attribute: Literal["description", "name", "loadPermission", "productCodes"] = None,
        OperationType: Literal["add", "remove"] = None,
        UserIds: List[str] = None,
        UserGroups: List[str] = None,
        ProductCodes: List[str] = None,
        LoadPermission: ClientModifyFpgaImageAttributeLoadPermissionTypeDef = None,
        Description: str = None,
        Name: str = None,
    ) -> ClientModifyFpgaImageAttributeResponseTypeDef:
        """
        [Client.modify_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_fpga_image_attribute)
        """

    def modify_hosts(
        self,
        HostIds: List[str],
        AutoPlacement: Literal["on", "off"] = None,
        HostRecovery: Literal["on", "off"] = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
    ) -> ClientModifyHostsResponseTypeDef:
        """
        [Client.modify_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_hosts)
        """

    def modify_id_format(self, Resource: str, UseLongIds: bool) -> None:
        """
        [Client.modify_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_id_format)
        """

    def modify_identity_id_format(self, PrincipalArn: str, Resource: str, UseLongIds: bool) -> None:
        """
        [Client.modify_identity_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_identity_id_format)
        """

    def modify_image_attribute(
        self,
        ImageId: str,
        Attribute: str = None,
        Description: ClientModifyImageAttributeDescriptionTypeDef = None,
        LaunchPermission: ClientModifyImageAttributeLaunchPermissionTypeDef = None,
        OperationType: Literal["add", "remove"] = None,
        ProductCodes: List[str] = None,
        UserGroups: List[str] = None,
        UserIds: List[str] = None,
        Value: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.modify_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_image_attribute)
        """

    def modify_instance_attribute(
        self,
        InstanceId: str,
        SourceDestCheck: ClientModifyInstanceAttributeSourceDestCheckTypeDef = None,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ] = None,
        BlockDeviceMappings: List[ClientModifyInstanceAttributeBlockDeviceMappingsTypeDef] = None,
        DisableApiTermination: ClientModifyInstanceAttributeDisableApiTerminationTypeDef = None,
        DryRun: bool = None,
        EbsOptimized: ClientModifyInstanceAttributeEbsOptimizedTypeDef = None,
        EnaSupport: ClientModifyInstanceAttributeEnaSupportTypeDef = None,
        Groups: List[str] = None,
        InstanceInitiatedShutdownBehavior: ClientModifyInstanceAttributeInstanceInitiatedShutdownBehaviorTypeDef = None,
        InstanceType: ClientModifyInstanceAttributeInstanceTypeTypeDef = None,
        Kernel: ClientModifyInstanceAttributeKernelTypeDef = None,
        Ramdisk: ClientModifyInstanceAttributeRamdiskTypeDef = None,
        SriovNetSupport: ClientModifyInstanceAttributeSriovNetSupportTypeDef = None,
        UserData: ClientModifyInstanceAttributeUserDataTypeDef = None,
        Value: str = None,
    ) -> None:
        """
        [Client.modify_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_instance_attribute)
        """

    def modify_instance_capacity_reservation_attributes(
        self,
        InstanceId: str,
        CapacityReservationSpecification: ClientModifyInstanceCapacityReservationAttributesCapacityReservationSpecificationTypeDef,
        DryRun: bool = None,
    ) -> ClientModifyInstanceCapacityReservationAttributesResponseTypeDef:
        """
        [Client.modify_instance_capacity_reservation_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_instance_capacity_reservation_attributes)
        """

    def modify_instance_credit_specification(
        self,
        InstanceCreditSpecifications: List[
            ClientModifyInstanceCreditSpecificationInstanceCreditSpecificationsTypeDef
        ],
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ClientModifyInstanceCreditSpecificationResponseTypeDef:
        """
        [Client.modify_instance_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_instance_credit_specification)
        """

    def modify_instance_event_start_time(
        self, InstanceId: str, InstanceEventId: str, NotBefore: datetime, DryRun: bool = None
    ) -> ClientModifyInstanceEventStartTimeResponseTypeDef:
        """
        [Client.modify_instance_event_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_instance_event_start_time)
        """

    def modify_instance_metadata_options(
        self,
        InstanceId: str,
        HttpTokens: Literal["optional", "required"] = None,
        HttpPutResponseHopLimit: int = None,
        HttpEndpoint: Literal["disabled", "enabled"] = None,
        DryRun: bool = None,
    ) -> ClientModifyInstanceMetadataOptionsResponseTypeDef:
        """
        [Client.modify_instance_metadata_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_instance_metadata_options)
        """

    def modify_instance_placement(
        self,
        InstanceId: str,
        Affinity: Literal["default", "host"] = None,
        GroupName: str = None,
        HostId: str = None,
        Tenancy: Literal["dedicated", "host"] = None,
        PartitionNumber: int = None,
        HostResourceGroupArn: str = None,
    ) -> ClientModifyInstancePlacementResponseTypeDef:
        """
        [Client.modify_instance_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_instance_placement)
        """

    def modify_launch_template(
        self,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        DefaultVersion: str = None,
    ) -> ClientModifyLaunchTemplateResponseTypeDef:
        """
        [Client.modify_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_launch_template)
        """

    def modify_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attachment: ClientModifyNetworkInterfaceAttributeAttachmentTypeDef = None,
        Description: ClientModifyNetworkInterfaceAttributeDescriptionTypeDef = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: ClientModifyNetworkInterfaceAttributeSourceDestCheckTypeDef = None,
    ) -> None:
        """
        [Client.modify_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_network_interface_attribute)
        """

    def modify_reserved_instances(
        self,
        ReservedInstancesIds: List[str],
        TargetConfigurations: List[ClientModifyReservedInstancesTargetConfigurationsTypeDef],
        ClientToken: str = None,
    ) -> ClientModifyReservedInstancesResponseTypeDef:
        """
        [Client.modify_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_reserved_instances)
        """

    def modify_snapshot_attribute(
        self,
        SnapshotId: str,
        Attribute: Literal["productCodes", "createVolumePermission"] = None,
        CreateVolumePermission: ClientModifySnapshotAttributeCreateVolumePermissionTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: Literal["add", "remove"] = None,
        UserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.modify_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_snapshot_attribute)
        """

    def modify_spot_fleet_request(
        self,
        SpotFleetRequestId: str,
        ExcessCapacityTerminationPolicy: Literal["noTermination", "default"] = None,
        TargetCapacity: int = None,
        OnDemandTargetCapacity: int = None,
    ) -> ClientModifySpotFleetRequestResponseTypeDef:
        """
        [Client.modify_spot_fleet_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_spot_fleet_request)
        """

    def modify_subnet_attribute(
        self,
        SubnetId: str,
        AssignIpv6AddressOnCreation: ClientModifySubnetAttributeAssignIpv6AddressOnCreationTypeDef = None,
        MapPublicIpOnLaunch: ClientModifySubnetAttributeMapPublicIpOnLaunchTypeDef = None,
    ) -> None:
        """
        [Client.modify_subnet_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_subnet_attribute)
        """

    def modify_traffic_mirror_filter_network_services(
        self,
        TrafficMirrorFilterId: str,
        AddNetworkServices: List[str] = None,
        RemoveNetworkServices: List[str] = None,
        DryRun: bool = None,
    ) -> ClientModifyTrafficMirrorFilterNetworkServicesResponseTypeDef:
        """
        [Client.modify_traffic_mirror_filter_network_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_network_services)
        """

    def modify_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: Literal["ingress", "egress"] = None,
        RuleNumber: int = None,
        RuleAction: Literal["accept", "reject"] = None,
        DestinationPortRange: ClientModifyTrafficMirrorFilterRuleDestinationPortRangeTypeDef = None,
        SourcePortRange: ClientModifyTrafficMirrorFilterRuleSourcePortRangeTypeDef = None,
        Protocol: int = None,
        DestinationCidrBlock: str = None,
        SourceCidrBlock: str = None,
        Description: str = None,
        RemoveFields: List[
            Literal["destination-port-range", "source-port-range", "protocol", "description"]
        ] = None,
        DryRun: bool = None,
    ) -> ClientModifyTrafficMirrorFilterRuleResponseTypeDef:
        """
        [Client.modify_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_rule)
        """

    def modify_traffic_mirror_session(
        self,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: str = None,
        TrafficMirrorFilterId: str = None,
        PacketLength: int = None,
        SessionNumber: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        RemoveFields: List[Literal["packet-length", "description", "virtual-network-id"]] = None,
        DryRun: bool = None,
    ) -> ClientModifyTrafficMirrorSessionResponseTypeDef:
        """
        [Client.modify_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_session)
        """

    def modify_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        Options: ClientModifyTransitGatewayVpcAttachmentOptionsTypeDef = None,
        DryRun: bool = None,
    ) -> ClientModifyTransitGatewayVpcAttachmentResponseTypeDef:
        """
        [Client.modify_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_transit_gateway_vpc_attachment)
        """

    def modify_volume(
        self,
        VolumeId: str,
        DryRun: bool = None,
        Size: int = None,
        VolumeType: Literal["standard", "io1", "gp2", "sc1", "st1"] = None,
        Iops: int = None,
    ) -> ClientModifyVolumeResponseTypeDef:
        """
        [Client.modify_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_volume)
        """

    def modify_volume_attribute(
        self,
        VolumeId: str,
        AutoEnableIO: ClientModifyVolumeAttributeAutoEnableIOTypeDef = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.modify_volume_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_volume_attribute)
        """

    def modify_vpc_attribute(
        self,
        VpcId: str,
        EnableDnsHostnames: ClientModifyVpcAttributeEnableDnsHostnamesTypeDef = None,
        EnableDnsSupport: ClientModifyVpcAttributeEnableDnsSupportTypeDef = None,
    ) -> None:
        """
        [Client.modify_vpc_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_attribute)
        """

    def modify_vpc_endpoint(
        self,
        VpcEndpointId: str,
        DryRun: bool = None,
        ResetPolicy: bool = None,
        PolicyDocument: str = None,
        AddRouteTableIds: List[str] = None,
        RemoveRouteTableIds: List[str] = None,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        AddSecurityGroupIds: List[str] = None,
        RemoveSecurityGroupIds: List[str] = None,
        PrivateDnsEnabled: bool = None,
    ) -> ClientModifyVpcEndpointResponseTypeDef:
        """
        [Client.modify_vpc_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint)
        """

    def modify_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationId: str,
        DryRun: bool = None,
        ConnectionNotificationArn: str = None,
        ConnectionEvents: List[str] = None,
    ) -> ClientModifyVpcEndpointConnectionNotificationResponseTypeDef:
        """
        [Client.modify_vpc_endpoint_connection_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_connection_notification)
        """

    def modify_vpc_endpoint_service_configuration(
        self,
        ServiceId: str,
        DryRun: bool = None,
        PrivateDnsName: str = None,
        RemovePrivateDnsName: bool = None,
        AcceptanceRequired: bool = None,
        AddNetworkLoadBalancerArns: List[str] = None,
        RemoveNetworkLoadBalancerArns: List[str] = None,
    ) -> ClientModifyVpcEndpointServiceConfigurationResponseTypeDef:
        """
        [Client.modify_vpc_endpoint_service_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_configuration)
        """

    def modify_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: bool = None,
        AddAllowedPrincipals: List[str] = None,
        RemoveAllowedPrincipals: List[str] = None,
    ) -> ClientModifyVpcEndpointServicePermissionsResponseTypeDef:
        """
        [Client.modify_vpc_endpoint_service_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_permissions)
        """

    def modify_vpc_peering_connection_options(
        self,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: ClientModifyVpcPeeringConnectionOptionsAccepterPeeringConnectionOptionsTypeDef = None,
        DryRun: bool = None,
        RequesterPeeringConnectionOptions: ClientModifyVpcPeeringConnectionOptionsRequesterPeeringConnectionOptionsTypeDef = None,
    ) -> ClientModifyVpcPeeringConnectionOptionsResponseTypeDef:
        """
        [Client.modify_vpc_peering_connection_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_peering_connection_options)
        """

    def modify_vpc_tenancy(
        self, VpcId: str, InstanceTenancy: str, DryRun: bool = None
    ) -> ClientModifyVpcTenancyResponseTypeDef:
        """
        [Client.modify_vpc_tenancy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpc_tenancy)
        """

    def modify_vpn_connection(
        self,
        VpnConnectionId: str,
        TransitGatewayId: str = None,
        CustomerGatewayId: str = None,
        VpnGatewayId: str = None,
        DryRun: bool = None,
    ) -> ClientModifyVpnConnectionResponseTypeDef:
        """
        [Client.modify_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpn_connection)
        """

    def modify_vpn_tunnel_certificate(
        self, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = None
    ) -> ClientModifyVpnTunnelCertificateResponseTypeDef:
        """
        [Client.modify_vpn_tunnel_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_certificate)
        """

    def modify_vpn_tunnel_options(
        self,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: ClientModifyVpnTunnelOptionsTunnelOptionsTypeDef,
        DryRun: bool = None,
    ) -> ClientModifyVpnTunnelOptionsResponseTypeDef:
        """
        [Client.modify_vpn_tunnel_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_options)
        """

    def monitor_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> ClientMonitorInstancesResponseTypeDef:
        """
        [Client.monitor_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.monitor_instances)
        """

    def move_address_to_vpc(
        self, PublicIp: str, DryRun: bool = None
    ) -> ClientMoveAddressToVpcResponseTypeDef:
        """
        [Client.move_address_to_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.move_address_to_vpc)
        """

    def provision_byoip_cidr(
        self,
        Cidr: str,
        CidrAuthorizationContext: ClientProvisionByoipCidrCidrAuthorizationContextTypeDef = None,
        PubliclyAdvertisable: bool = None,
        Description: str = None,
        DryRun: bool = None,
    ) -> ClientProvisionByoipCidrResponseTypeDef:
        """
        [Client.provision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.provision_byoip_cidr)
        """

    def purchase_host_reservation(
        self,
        HostIdSet: List[str],
        OfferingId: str,
        ClientToken: str = None,
        CurrencyCode: str = None,
        LimitPrice: str = None,
    ) -> ClientPurchaseHostReservationResponseTypeDef:
        """
        [Client.purchase_host_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.purchase_host_reservation)
        """

    def purchase_reserved_instances_offering(
        self,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        DryRun: bool = None,
        LimitPrice: ClientPurchaseReservedInstancesOfferingLimitPriceTypeDef = None,
        PurchaseTime: datetime = None,
    ) -> ClientPurchaseReservedInstancesOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_instances_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.purchase_reserved_instances_offering)
        """

    def purchase_scheduled_instances(
        self,
        PurchaseRequests: List[ClientPurchaseScheduledInstancesPurchaseRequestsTypeDef],
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> ClientPurchaseScheduledInstancesResponseTypeDef:
        """
        [Client.purchase_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.purchase_scheduled_instances)
        """

    def reboot_instances(self, InstanceIds: List[str], DryRun: bool = None) -> None:
        """
        [Client.reboot_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reboot_instances)
        """

    def register_image(
        self,
        Name: str,
        ImageLocation: str = None,
        Architecture: Literal["i386", "x86_64", "arm64"] = None,
        BlockDeviceMappings: List[ClientRegisterImageBlockDeviceMappingsTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        EnaSupport: bool = None,
        KernelId: str = None,
        BillingProducts: List[str] = None,
        RamdiskId: str = None,
        RootDeviceName: str = None,
        SriovNetSupport: str = None,
        VirtualizationType: str = None,
    ) -> ClientRegisterImageResponseTypeDef:
        """
        [Client.register_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.register_image)
        """

    def register_transit_gateway_multicast_group_members(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientRegisterTransitGatewayMulticastGroupMembersResponseTypeDef:
        """
        [Client.register_transit_gateway_multicast_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_members)
        """

    def register_transit_gateway_multicast_group_sources(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> ClientRegisterTransitGatewayMulticastGroupSourcesResponseTypeDef:
        """
        [Client.register_transit_gateway_multicast_group_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_sources)
        """

    def reject_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientRejectTransitGatewayPeeringAttachmentResponseTypeDef:
        """
        [Client.reject_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reject_transit_gateway_peering_attachment)
        """

    def reject_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> ClientRejectTransitGatewayVpcAttachmentResponseTypeDef:
        """
        [Client.reject_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reject_transit_gateway_vpc_attachment)
        """

    def reject_vpc_endpoint_connections(
        self, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> ClientRejectVpcEndpointConnectionsResponseTypeDef:
        """
        [Client.reject_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reject_vpc_endpoint_connections)
        """

    def reject_vpc_peering_connection(
        self, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> ClientRejectVpcPeeringConnectionResponseTypeDef:
        """
        [Client.reject_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reject_vpc_peering_connection)
        """

    def release_address(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.release_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.release_address)
        """

    def release_hosts(self, HostIds: List[str]) -> ClientReleaseHostsResponseTypeDef:
        """
        [Client.release_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.release_hosts)
        """

    def replace_iam_instance_profile_association(
        self,
        IamInstanceProfile: ClientReplaceIamInstanceProfileAssociationIamInstanceProfileTypeDef,
        AssociationId: str,
    ) -> ClientReplaceIamInstanceProfileAssociationResponseTypeDef:
        """
        [Client.replace_iam_instance_profile_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.replace_iam_instance_profile_association)
        """

    def replace_network_acl_association(
        self, AssociationId: str, NetworkAclId: str, DryRun: bool = None
    ) -> ClientReplaceNetworkAclAssociationResponseTypeDef:
        """
        [Client.replace_network_acl_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.replace_network_acl_association)
        """

    def replace_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: Literal["allow", "deny"],
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: ClientReplaceNetworkAclEntryIcmpTypeCodeTypeDef = None,
        Ipv6CidrBlock: str = None,
        PortRange: ClientReplaceNetworkAclEntryPortRangeTypeDef = None,
    ) -> None:
        """
        [Client.replace_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.replace_network_acl_entry)
        """

    def replace_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        LocalTarget: bool = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> None:
        """
        [Client.replace_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.replace_route)
        """

    def replace_route_table_association(
        self, AssociationId: str, RouteTableId: str, DryRun: bool = None
    ) -> ClientReplaceRouteTableAssociationResponseTypeDef:
        """
        [Client.replace_route_table_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.replace_route_table_association)
        """

    def replace_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> ClientReplaceTransitGatewayRouteResponseTypeDef:
        """
        [Client.replace_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.replace_transit_gateway_route)
        """

    def report_instance_status(
        self,
        Instances: List[str],
        ReasonCodes: List[
            Literal[
                "instance-stuck-in-state",
                "unresponsive",
                "not-accepting-credentials",
                "password-not-available",
                "performance-network",
                "performance-instance-store",
                "performance-ebs-volume",
                "performance-other",
                "other",
            ]
        ],
        Status: Literal["ok", "impaired"],
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None,
    ) -> None:
        """
        [Client.report_instance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.report_instance_status)
        """

    def request_spot_fleet(
        self,
        SpotFleetRequestConfig: ClientRequestSpotFleetSpotFleetRequestConfigTypeDef,
        DryRun: bool = None,
    ) -> ClientRequestSpotFleetResponseTypeDef:
        """
        [Client.request_spot_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.request_spot_fleet)
        """

    def request_spot_instances(
        self,
        AvailabilityZoneGroup: str = None,
        BlockDurationMinutes: int = None,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
        LaunchGroup: str = None,
        LaunchSpecification: ClientRequestSpotInstancesLaunchSpecificationTypeDef = None,
        SpotPrice: str = None,
        Type: Literal["one-time", "persistent"] = None,
        ValidFrom: datetime = None,
        ValidUntil: datetime = None,
        InstanceInterruptionBehavior: Literal["hibernate", "stop", "terminate"] = None,
    ) -> ClientRequestSpotInstancesResponseTypeDef:
        """
        [Client.request_spot_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.request_spot_instances)
        """

    def reset_ebs_default_kms_key_id(
        self, DryRun: bool = None
    ) -> ClientResetEbsDefaultKmsKeyIdResponseTypeDef:
        """
        [Client.reset_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reset_ebs_default_kms_key_id)
        """

    def reset_fpga_image_attribute(
        self, FpgaImageId: str, DryRun: bool = None, Attribute: str = None
    ) -> ClientResetFpgaImageAttributeResponseTypeDef:
        """
        [Client.reset_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reset_fpga_image_attribute)
        """

    def reset_image_attribute(self, Attribute: str, ImageId: str, DryRun: bool = None) -> None:
        """
        [Client.reset_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reset_image_attribute)
        """

    def reset_instance_attribute(
        self,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ],
        InstanceId: str,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.reset_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reset_instance_attribute)
        """

    def reset_network_interface_attribute(
        self, NetworkInterfaceId: str, DryRun: bool = None, SourceDestCheck: str = None
    ) -> None:
        """
        [Client.reset_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reset_network_interface_attribute)
        """

    def reset_snapshot_attribute(
        self,
        Attribute: Literal["productCodes", "createVolumePermission"],
        SnapshotId: str,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.reset_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.reset_snapshot_attribute)
        """

    def restore_address_to_classic(
        self, PublicIp: str, DryRun: bool = None
    ) -> ClientRestoreAddressToClassicResponseTypeDef:
        """
        [Client.restore_address_to_classic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.restore_address_to_classic)
        """

    def revoke_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        RevokeAllGroups: bool = None,
        DryRun: bool = None,
    ) -> ClientRevokeClientVpnIngressResponseTypeDef:
        """
        [Client.revoke_client_vpn_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.revoke_client_vpn_ingress)
        """

    def revoke_security_group_egress(
        self,
        GroupId: str,
        DryRun: bool = None,
        IpPermissions: List[ClientRevokeSecurityGroupEgressIpPermissionsTypeDef] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        """
        [Client.revoke_security_group_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.revoke_security_group_egress)
        """

    def revoke_security_group_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List[ClientRevokeSecurityGroupIngressIpPermissionsTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.revoke_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.revoke_security_group_ingress)
        """

    def run_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List[ClientRunInstancesBlockDeviceMappingsTypeDef] = None,
        ImageId: str = None,
        InstanceType: Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
        ] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[ClientRunInstancesIpv6AddressesTypeDef] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: ClientRunInstancesMonitoringTypeDef = None,
        Placement: ClientRunInstancesPlacementTypeDef = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        SubnetId: str = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: ClientRunInstancesIamInstanceProfileTypeDef = None,
        InstanceInitiatedShutdownBehavior: Literal["stop", "terminate"] = None,
        NetworkInterfaces: List[ClientRunInstancesNetworkInterfacesTypeDef] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List[ClientRunInstancesElasticGpuSpecificationTypeDef] = None,
        ElasticInferenceAccelerators: List[
            ClientRunInstancesElasticInferenceAcceleratorsTypeDef
        ] = None,
        TagSpecifications: List[ClientRunInstancesTagSpecificationsTypeDef] = None,
        LaunchTemplate: ClientRunInstancesLaunchTemplateTypeDef = None,
        InstanceMarketOptions: ClientRunInstancesInstanceMarketOptionsTypeDef = None,
        CreditSpecification: ClientRunInstancesCreditSpecificationTypeDef = None,
        CpuOptions: ClientRunInstancesCpuOptionsTypeDef = None,
        CapacityReservationSpecification: ClientRunInstancesCapacityReservationSpecificationTypeDef = None,
        HibernationOptions: ClientRunInstancesHibernationOptionsTypeDef = None,
        LicenseSpecifications: List[ClientRunInstancesLicenseSpecificationsTypeDef] = None,
        MetadataOptions: ClientRunInstancesMetadataOptionsTypeDef = None,
    ) -> ClientRunInstancesResponseTypeDef:
        """
        [Client.run_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.run_instances)
        """

    def run_scheduled_instances(
        self,
        LaunchSpecification: ClientRunScheduledInstancesLaunchSpecificationTypeDef,
        ScheduledInstanceId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
    ) -> ClientRunScheduledInstancesResponseTypeDef:
        """
        [Client.run_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.run_scheduled_instances)
        """

    def search_local_gateway_routes(
        self,
        LocalGatewayRouteTableId: str,
        Filters: List[ClientSearchLocalGatewayRoutesFiltersTypeDef],
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientSearchLocalGatewayRoutesResponseTypeDef:
        """
        [Client.search_local_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.search_local_gateway_routes)
        """

    def search_transit_gateway_multicast_groups(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[ClientSearchTransitGatewayMulticastGroupsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> ClientSearchTransitGatewayMulticastGroupsResponseTypeDef:
        """
        [Client.search_transit_gateway_multicast_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.search_transit_gateway_multicast_groups)
        """

    def search_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[ClientSearchTransitGatewayRoutesFiltersTypeDef],
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> ClientSearchTransitGatewayRoutesResponseTypeDef:
        """
        [Client.search_transit_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.search_transit_gateway_routes)
        """

    def send_diagnostic_interrupt(self, InstanceId: str, DryRun: bool = None) -> None:
        """
        [Client.send_diagnostic_interrupt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.send_diagnostic_interrupt)
        """

    def start_instances(
        self, InstanceIds: List[str], AdditionalInfo: str = None, DryRun: bool = None
    ) -> ClientStartInstancesResponseTypeDef:
        """
        [Client.start_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.start_instances)
        """

    def start_vpc_endpoint_service_private_dns_verification(
        self, ServiceId: str, DryRun: bool = None
    ) -> ClientStartVpcEndpointServicePrivateDnsVerificationResponseTypeDef:
        """
        [Client.start_vpc_endpoint_service_private_dns_verification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.start_vpc_endpoint_service_private_dns_verification)
        """

    def stop_instances(
        self,
        InstanceIds: List[str],
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None,
    ) -> ClientStopInstancesResponseTypeDef:
        """
        [Client.stop_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.stop_instances)
        """

    def terminate_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        ConnectionId: str = None,
        Username: str = None,
        DryRun: bool = None,
    ) -> ClientTerminateClientVpnConnectionsResponseTypeDef:
        """
        [Client.terminate_client_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.terminate_client_vpn_connections)
        """

    def terminate_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> ClientTerminateInstancesResponseTypeDef:
        """
        [Client.terminate_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.terminate_instances)
        """

    def unassign_ipv6_addresses(
        self, Ipv6Addresses: List[str], NetworkInterfaceId: str
    ) -> ClientUnassignIpv6AddressesResponseTypeDef:
        """
        [Client.unassign_ipv6_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.unassign_ipv6_addresses)
        """

    def unassign_private_ip_addresses(
        self, NetworkInterfaceId: str, PrivateIpAddresses: List[str]
    ) -> None:
        """
        [Client.unassign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.unassign_private_ip_addresses)
        """

    def unmonitor_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> ClientUnmonitorInstancesResponseTypeDef:
        """
        [Client.unmonitor_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.unmonitor_instances)
        """

    def update_security_group_rule_descriptions_egress(
        self,
        IpPermissions: List[ClientUpdateSecurityGroupRuleDescriptionsEgressIpPermissionsTypeDef],
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
    ) -> ClientUpdateSecurityGroupRuleDescriptionsEgressResponseTypeDef:
        """
        [Client.update_security_group_rule_descriptions_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_egress)
        """

    def update_security_group_rule_descriptions_ingress(
        self,
        IpPermissions: List[ClientUpdateSecurityGroupRuleDescriptionsIngressIpPermissionsTypeDef],
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
    ) -> ClientUpdateSecurityGroupRuleDescriptionsIngressResponseTypeDef:
        """
        [Client.update_security_group_rule_descriptions_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_ingress)
        """

    def withdraw_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> ClientWithdrawByoipCidrResponseTypeDef:
        """
        [Client.withdraw_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Client.withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_byoip_cidrs"]
    ) -> "paginator_scope.DescribeByoipCidrsPaginator":
        """
        [Paginator.DescribeByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservations"]
    ) -> "paginator_scope.DescribeCapacityReservationsPaginator":
        """
        [Paginator.DescribeCapacityReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_classic_link_instances"]
    ) -> "paginator_scope.DescribeClassicLinkInstancesPaginator":
        """
        [Paginator.DescribeClassicLinkInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_authorization_rules"]
    ) -> "paginator_scope.DescribeClientVpnAuthorizationRulesPaginator":
        """
        [Paginator.DescribeClientVpnAuthorizationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_connections"]
    ) -> "paginator_scope.DescribeClientVpnConnectionsPaginator":
        """
        [Paginator.DescribeClientVpnConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_endpoints"]
    ) -> "paginator_scope.DescribeClientVpnEndpointsPaginator":
        """
        [Paginator.DescribeClientVpnEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_routes"]
    ) -> "paginator_scope.DescribeClientVpnRoutesPaginator":
        """
        [Paginator.DescribeClientVpnRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_target_networks"]
    ) -> "paginator_scope.DescribeClientVpnTargetNetworksPaginator":
        """
        [Paginator.DescribeClientVpnTargetNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_dhcp_options"]
    ) -> "paginator_scope.DescribeDhcpOptionsPaginator":
        """
        [Paginator.DescribeDhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_egress_only_internet_gateways"]
    ) -> "paginator_scope.DescribeEgressOnlyInternetGatewaysPaginator":
        """
        [Paginator.DescribeEgressOnlyInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_image_tasks"]
    ) -> "paginator_scope.DescribeExportImageTasksPaginator":
        """
        [Paginator.DescribeExportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fast_snapshot_restores"]
    ) -> "paginator_scope.DescribeFastSnapshotRestoresPaginator":
        """
        [Paginator.DescribeFastSnapshotRestores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleets"]
    ) -> "paginator_scope.DescribeFleetsPaginator":
        """
        [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeFleets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_flow_logs"]
    ) -> "paginator_scope.DescribeFlowLogsPaginator":
        """
        [Paginator.DescribeFlowLogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fpga_images"]
    ) -> "paginator_scope.DescribeFpgaImagesPaginator":
        """
        [Paginator.DescribeFpgaImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservation_offerings"]
    ) -> "paginator_scope.DescribeHostReservationOfferingsPaginator":
        """
        [Paginator.DescribeHostReservationOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservations"]
    ) -> "paginator_scope.DescribeHostReservationsPaginator":
        """
        [Paginator.DescribeHostReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hosts"]
    ) -> "paginator_scope.DescribeHostsPaginator":
        """
        [Paginator.DescribeHosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeHosts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_iam_instance_profile_associations"]
    ) -> "paginator_scope.DescribeIamInstanceProfileAssociationsPaginator":
        """
        [Paginator.DescribeIamInstanceProfileAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_image_tasks"]
    ) -> "paginator_scope.DescribeImportImageTasksPaginator":
        """
        [Paginator.DescribeImportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_snapshot_tasks"]
    ) -> "paginator_scope.DescribeImportSnapshotTasksPaginator":
        """
        [Paginator.DescribeImportSnapshotTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_credit_specifications"]
    ) -> "paginator_scope.DescribeInstanceCreditSpecificationsPaginator":
        """
        [Paginator.DescribeInstanceCreditSpecifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_status"]
    ) -> "paginator_scope.DescribeInstanceStatusPaginator":
        """
        [Paginator.DescribeInstanceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> "paginator_scope.DescribeInstancesPaginator":
        """
        [Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_internet_gateways"]
    ) -> "paginator_scope.DescribeInternetGatewaysPaginator":
        """
        [Paginator.DescribeInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipv6_pools"]
    ) -> "paginator_scope.DescribeIpv6PoolsPaginator":
        """
        [Paginator.DescribeIpv6Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_template_versions"]
    ) -> "paginator_scope.DescribeLaunchTemplateVersionsPaginator":
        """
        [Paginator.DescribeLaunchTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_templates"]
    ) -> "paginator_scope.DescribeLaunchTemplatesPaginator":
        """
        [Paginator.DescribeLaunchTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_moving_addresses"]
    ) -> "paginator_scope.DescribeMovingAddressesPaginator":
        """
        [Paginator.DescribeMovingAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_nat_gateways"]
    ) -> "paginator_scope.DescribeNatGatewaysPaginator":
        """
        [Paginator.DescribeNatGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_acls"]
    ) -> "paginator_scope.DescribeNetworkAclsPaginator":
        """
        [Paginator.DescribeNetworkAcls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interface_permissions"]
    ) -> "paginator_scope.DescribeNetworkInterfacePermissionsPaginator":
        """
        [Paginator.DescribeNetworkInterfacePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interfaces"]
    ) -> "paginator_scope.DescribeNetworkInterfacesPaginator":
        """
        [Paginator.DescribeNetworkInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_prefix_lists"]
    ) -> "paginator_scope.DescribePrefixListsPaginator":
        """
        [Paginator.DescribePrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_principal_id_format"]
    ) -> "paginator_scope.DescribePrincipalIdFormatPaginator":
        """
        [Paginator.DescribePrincipalIdFormat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_public_ipv4_pools"]
    ) -> "paginator_scope.DescribePublicIpv4PoolsPaginator":
        """
        [Paginator.DescribePublicIpv4Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_modifications"]
    ) -> "paginator_scope.DescribeReservedInstancesModificationsPaginator":
        """
        [Paginator.DescribeReservedInstancesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_offerings"]
    ) -> "paginator_scope.DescribeReservedInstancesOfferingsPaginator":
        """
        [Paginator.DescribeReservedInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_route_tables"]
    ) -> "paginator_scope.DescribeRouteTablesPaginator":
        """
        [Paginator.DescribeRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instance_availability"]
    ) -> "paginator_scope.DescribeScheduledInstanceAvailabilityPaginator":
        """
        [Paginator.DescribeScheduledInstanceAvailability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instances"]
    ) -> "paginator_scope.DescribeScheduledInstancesPaginator":
        """
        [Paginator.DescribeScheduledInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_security_groups"]
    ) -> "paginator_scope.DescribeSecurityGroupsPaginator":
        """
        [Paginator.DescribeSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> "paginator_scope.DescribeSnapshotsPaginator":
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_instances"]
    ) -> "paginator_scope.DescribeSpotFleetInstancesPaginator":
        """
        [Paginator.DescribeSpotFleetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_requests"]
    ) -> "paginator_scope.DescribeSpotFleetRequestsPaginator":
        """
        [Paginator.DescribeSpotFleetRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_instance_requests"]
    ) -> "paginator_scope.DescribeSpotInstanceRequestsPaginator":
        """
        [Paginator.DescribeSpotInstanceRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_price_history"]
    ) -> "paginator_scope.DescribeSpotPriceHistoryPaginator":
        """
        [Paginator.DescribeSpotPriceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_stale_security_groups"]
    ) -> "paginator_scope.DescribeStaleSecurityGroupsPaginator":
        """
        [Paginator.DescribeStaleSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnets"]
    ) -> "paginator_scope.DescribeSubnetsPaginator":
        """
        [Paginator.DescribeSubnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> "paginator_scope.DescribeTagsPaginator":
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_filters"]
    ) -> "paginator_scope.DescribeTrafficMirrorFiltersPaginator":
        """
        [Paginator.DescribeTrafficMirrorFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_sessions"]
    ) -> "paginator_scope.DescribeTrafficMirrorSessionsPaginator":
        """
        [Paginator.DescribeTrafficMirrorSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_targets"]
    ) -> "paginator_scope.DescribeTrafficMirrorTargetsPaginator":
        """
        [Paginator.DescribeTrafficMirrorTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_attachments"]
    ) -> "paginator_scope.DescribeTransitGatewayAttachmentsPaginator":
        """
        [Paginator.DescribeTransitGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_tables"]
    ) -> "paginator_scope.DescribeTransitGatewayRouteTablesPaginator":
        """
        [Paginator.DescribeTransitGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_vpc_attachments"]
    ) -> "paginator_scope.DescribeTransitGatewayVpcAttachmentsPaginator":
        """
        [Paginator.DescribeTransitGatewayVpcAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateways"]
    ) -> "paginator_scope.DescribeTransitGatewaysPaginator":
        """
        [Paginator.DescribeTransitGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volume_status"]
    ) -> "paginator_scope.DescribeVolumeStatusPaginator":
        """
        [Paginator.DescribeVolumeStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes"]
    ) -> "paginator_scope.DescribeVolumesPaginator":
        """
        [Paginator.DescribeVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes_modifications"]
    ) -> "paginator_scope.DescribeVolumesModificationsPaginator":
        """
        [Paginator.DescribeVolumesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_classic_link_dns_support"]
    ) -> "paginator_scope.DescribeVpcClassicLinkDnsSupportPaginator":
        """
        [Paginator.DescribeVpcClassicLinkDnsSupport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connection_notifications"]
    ) -> "paginator_scope.DescribeVpcEndpointConnectionNotificationsPaginator":
        """
        [Paginator.DescribeVpcEndpointConnectionNotifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connections"]
    ) -> "paginator_scope.DescribeVpcEndpointConnectionsPaginator":
        """
        [Paginator.DescribeVpcEndpointConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_configurations"]
    ) -> "paginator_scope.DescribeVpcEndpointServiceConfigurationsPaginator":
        """
        [Paginator.DescribeVpcEndpointServiceConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_permissions"]
    ) -> "paginator_scope.DescribeVpcEndpointServicePermissionsPaginator":
        """
        [Paginator.DescribeVpcEndpointServicePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_services"]
    ) -> "paginator_scope.DescribeVpcEndpointServicesPaginator":
        """
        [Paginator.DescribeVpcEndpointServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoints"]
    ) -> "paginator_scope.DescribeVpcEndpointsPaginator":
        """
        [Paginator.DescribeVpcEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_peering_connections"]
    ) -> "paginator_scope.DescribeVpcPeeringConnectionsPaginator":
        """
        [Paginator.DescribeVpcPeeringConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpcs"]
    ) -> "paginator_scope.DescribeVpcsPaginator":
        """
        [Paginator.DescribeVpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_associated_ipv6_pool_cidrs"]
    ) -> "paginator_scope.GetAssociatedIpv6PoolCidrsPaginator":
        """
        [Paginator.GetAssociatedIpv6PoolCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_attachment_propagations"]
    ) -> "paginator_scope.GetTransitGatewayAttachmentPropagationsPaginator":
        """
        [Paginator.GetTransitGatewayAttachmentPropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_associations"]
    ) -> "paginator_scope.GetTransitGatewayRouteTableAssociationsPaginator":
        """
        [Paginator.GetTransitGatewayRouteTableAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_propagations"]
    ) -> "paginator_scope.GetTransitGatewayRouteTablePropagationsPaginator":
        """
        [Paginator.GetTransitGatewayRouteTablePropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["bundle_task_complete"]
    ) -> "waiter_scope.BundleTaskCompleteWaiter":
        """
        [Waiter.BundleTaskComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.BundleTaskComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_cancelled"]
    ) -> "waiter_scope.ConversionTaskCancelledWaiter":
        """
        [Waiter.ConversionTaskCancelled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ConversionTaskCancelled)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_completed"]
    ) -> "waiter_scope.ConversionTaskCompletedWaiter":
        """
        [Waiter.ConversionTaskCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ConversionTaskCompleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_deleted"]
    ) -> "waiter_scope.ConversionTaskDeletedWaiter":
        """
        [Waiter.ConversionTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ConversionTaskDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["customer_gateway_available"]
    ) -> "waiter_scope.CustomerGatewayAvailableWaiter":
        """
        [Waiter.CustomerGatewayAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.CustomerGatewayAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> "waiter_scope.ExportTaskCancelledWaiter":
        """
        [Waiter.ExportTaskCancelled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ExportTaskCancelled)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_completed"]
    ) -> "waiter_scope.ExportTaskCompletedWaiter":
        """
        [Waiter.ExportTaskCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ExportTaskCompleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["image_available"]
    ) -> "waiter_scope.ImageAvailableWaiter":
        """
        [Waiter.ImageAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ImageAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_exists"]) -> "waiter_scope.ImageExistsWaiter":
        """
        [Waiter.ImageExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.ImageExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_exists"]
    ) -> "waiter_scope.InstanceExistsWaiter":
        """
        [Waiter.InstanceExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.InstanceExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_running"]
    ) -> "waiter_scope.InstanceRunningWaiter":
        """
        [Waiter.InstanceRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.InstanceRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_status_ok"]
    ) -> "waiter_scope.InstanceStatusOkWaiter":
        """
        [Waiter.InstanceStatusOk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.InstanceStatusOk)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_stopped"]
    ) -> "waiter_scope.InstanceStoppedWaiter":
        """
        [Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.InstanceStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_terminated"]
    ) -> "waiter_scope.InstanceTerminatedWaiter":
        """
        [Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.InstanceTerminated)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["key_pair_exists"]
    ) -> "waiter_scope.KeyPairExistsWaiter":
        """
        [Waiter.KeyPairExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.KeyPairExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["nat_gateway_available"]
    ) -> "waiter_scope.NatGatewayAvailableWaiter":
        """
        [Waiter.NatGatewayAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.NatGatewayAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["network_interface_available"]
    ) -> "waiter_scope.NetworkInterfaceAvailableWaiter":
        """
        [Waiter.NetworkInterfaceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.NetworkInterfaceAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["password_data_available"]
    ) -> "waiter_scope.PasswordDataAvailableWaiter":
        """
        [Waiter.PasswordDataAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.PasswordDataAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["security_group_exists"]
    ) -> "waiter_scope.SecurityGroupExistsWaiter":
        """
        [Waiter.SecurityGroupExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.SecurityGroupExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["snapshot_completed"]
    ) -> "waiter_scope.SnapshotCompletedWaiter":
        """
        [Waiter.SnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.SnapshotCompleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["spot_instance_request_fulfilled"]
    ) -> "waiter_scope.SpotInstanceRequestFulfilledWaiter":
        """
        [Waiter.SpotInstanceRequestFulfilled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.SpotInstanceRequestFulfilled)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["subnet_available"]
    ) -> "waiter_scope.SubnetAvailableWaiter":
        """
        [Waiter.SubnetAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.SubnetAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["system_status_ok"]
    ) -> "waiter_scope.SystemStatusOkWaiter":
        """
        [Waiter.SystemStatusOk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.SystemStatusOk)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["volume_available"]
    ) -> "waiter_scope.VolumeAvailableWaiter":
        """
        [Waiter.VolumeAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VolumeAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["volume_deleted"]
    ) -> "waiter_scope.VolumeDeletedWaiter":
        """
        [Waiter.VolumeDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VolumeDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_in_use"]) -> "waiter_scope.VolumeInUseWaiter":
        """
        [Waiter.VolumeInUse documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VolumeInUse)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_available"]
    ) -> "waiter_scope.VpcAvailableWaiter":
        """
        [Waiter.VpcAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VpcAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_exists"]) -> "waiter_scope.VpcExistsWaiter":
        """
        [Waiter.VpcExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VpcExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_deleted"]
    ) -> "waiter_scope.VpcPeeringConnectionDeletedWaiter":
        """
        [Waiter.VpcPeeringConnectionDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_exists"]
    ) -> "waiter_scope.VpcPeeringConnectionExistsWaiter":
        """
        [Waiter.VpcPeeringConnectionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_available"]
    ) -> "waiter_scope.VpnConnectionAvailableWaiter":
        """
        [Waiter.VpnConnectionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VpnConnectionAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_deleted"]
    ) -> "waiter_scope.VpnConnectionDeletedWaiter":
        """
        [Waiter.VpnConnectionDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ec2.html#EC2.Waiter.VpnConnectionDeleted)
        """


class Exceptions:
    ClientError: Boto3ClientError
