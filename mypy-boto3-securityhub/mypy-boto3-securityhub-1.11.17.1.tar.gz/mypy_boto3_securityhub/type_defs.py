"""
Main interface for securityhub service type definitions.

Usage::

    from mypy_boto3.securityhub.type_defs import DateRangeTypeDef

    data: DateRangeTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DateRangeTypeDef",
    "DateFilterTypeDef",
    "IpFilterTypeDef",
    "KeywordFilterTypeDef",
    "MapFilterTypeDef",
    "NumberFilterTypeDef",
    "StringFilterTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef",
    "ClientBatchDisableStandardsResponseTypeDef",
    "ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef",
    "ClientBatchEnableStandardsResponseTypeDef",
    "ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef",
    "ClientBatchImportFindingsFindingsComplianceTypeDef",
    "ClientBatchImportFindingsFindingsMalwareTypeDef",
    "ClientBatchImportFindingsFindingsNetworkTypeDef",
    "ClientBatchImportFindingsFindingsNoteTypeDef",
    "ClientBatchImportFindingsFindingsProcessTypeDef",
    "ClientBatchImportFindingsFindingsRelatedFindingsTypeDef",
    "ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef",
    "ClientBatchImportFindingsFindingsRemediationTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsIamRoleTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsKmsKeyTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsSqsQueueTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesTypeDef",
    "ClientBatchImportFindingsFindingsSeverityTypeDef",
    "ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef",
    "ClientBatchImportFindingsFindingsTypeDef",
    "ClientBatchImportFindingsResponseFailedFindingsTypeDef",
    "ClientBatchImportFindingsResponseTypeDef",
    "ClientCreateActionTargetResponseTypeDef",
    "ClientCreateInsightFiltersAwsAccountIdTypeDef",
    "ClientCreateInsightFiltersCompanyNameTypeDef",
    "ClientCreateInsightFiltersComplianceStatusTypeDef",
    "ClientCreateInsightFiltersConfidenceTypeDef",
    "ClientCreateInsightFiltersCreatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersCreatedAtTypeDef",
    "ClientCreateInsightFiltersCriticalityTypeDef",
    "ClientCreateInsightFiltersDescriptionTypeDef",
    "ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersFirstObservedAtTypeDef",
    "ClientCreateInsightFiltersGeneratorIdTypeDef",
    "ClientCreateInsightFiltersIdTypeDef",
    "ClientCreateInsightFiltersKeywordTypeDef",
    "ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersLastObservedAtTypeDef",
    "ClientCreateInsightFiltersMalwareNameTypeDef",
    "ClientCreateInsightFiltersMalwarePathTypeDef",
    "ClientCreateInsightFiltersMalwareStateTypeDef",
    "ClientCreateInsightFiltersMalwareTypeTypeDef",
    "ClientCreateInsightFiltersNetworkDestinationDomainTypeDef",
    "ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef",
    "ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef",
    "ClientCreateInsightFiltersNetworkDestinationPortTypeDef",
    "ClientCreateInsightFiltersNetworkDirectionTypeDef",
    "ClientCreateInsightFiltersNetworkProtocolTypeDef",
    "ClientCreateInsightFiltersNetworkSourceDomainTypeDef",
    "ClientCreateInsightFiltersNetworkSourceIpV4TypeDef",
    "ClientCreateInsightFiltersNetworkSourceIpV6TypeDef",
    "ClientCreateInsightFiltersNetworkSourceMacTypeDef",
    "ClientCreateInsightFiltersNetworkSourcePortTypeDef",
    "ClientCreateInsightFiltersNoteTextTypeDef",
    "ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersNoteUpdatedAtTypeDef",
    "ClientCreateInsightFiltersNoteUpdatedByTypeDef",
    "ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersProcessLaunchedAtTypeDef",
    "ClientCreateInsightFiltersProcessNameTypeDef",
    "ClientCreateInsightFiltersProcessParentPidTypeDef",
    "ClientCreateInsightFiltersProcessPathTypeDef",
    "ClientCreateInsightFiltersProcessPidTypeDef",
    "ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersProcessTerminatedAtTypeDef",
    "ClientCreateInsightFiltersProductArnTypeDef",
    "ClientCreateInsightFiltersProductFieldsTypeDef",
    "ClientCreateInsightFiltersProductNameTypeDef",
    "ClientCreateInsightFiltersRecommendationTextTypeDef",
    "ClientCreateInsightFiltersRecordStateTypeDef",
    "ClientCreateInsightFiltersRelatedFindingsIdTypeDef",
    "ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientCreateInsightFiltersResourceContainerImageIdTypeDef",
    "ClientCreateInsightFiltersResourceContainerImageNameTypeDef",
    "ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef",
    "ClientCreateInsightFiltersResourceContainerNameTypeDef",
    "ClientCreateInsightFiltersResourceDetailsOtherTypeDef",
    "ClientCreateInsightFiltersResourceIdTypeDef",
    "ClientCreateInsightFiltersResourcePartitionTypeDef",
    "ClientCreateInsightFiltersResourceRegionTypeDef",
    "ClientCreateInsightFiltersResourceTagsTypeDef",
    "ClientCreateInsightFiltersResourceTypeTypeDef",
    "ClientCreateInsightFiltersSeverityLabelTypeDef",
    "ClientCreateInsightFiltersSeverityNormalizedTypeDef",
    "ClientCreateInsightFiltersSeverityProductTypeDef",
    "ClientCreateInsightFiltersSourceUrlTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef",
    "ClientCreateInsightFiltersTitleTypeDef",
    "ClientCreateInsightFiltersTypeTypeDef",
    "ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersUpdatedAtTypeDef",
    "ClientCreateInsightFiltersUserDefinedFieldsTypeDef",
    "ClientCreateInsightFiltersVerificationStateTypeDef",
    "ClientCreateInsightFiltersWorkflowStateTypeDef",
    "ClientCreateInsightFiltersTypeDef",
    "ClientCreateInsightResponseTypeDef",
    "ClientCreateMembersAccountDetailsTypeDef",
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    "ClientCreateMembersResponseTypeDef",
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeclineInvitationsResponseTypeDef",
    "ClientDeleteActionTargetResponseTypeDef",
    "ClientDeleteInsightResponseTypeDef",
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeleteInvitationsResponseTypeDef",
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    "ClientDeleteMembersResponseTypeDef",
    "ClientDescribeActionTargetsResponseActionTargetsTypeDef",
    "ClientDescribeActionTargetsResponseTypeDef",
    "ClientDescribeHubResponseTypeDef",
    "ClientDescribeProductsResponseProductsTypeDef",
    "ClientDescribeProductsResponseTypeDef",
    "ClientDescribeStandardsControlsResponseControlsTypeDef",
    "ClientDescribeStandardsControlsResponseTypeDef",
    "ClientEnableImportFindingsForProductResponseTypeDef",
    "ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef",
    "ClientGetEnabledStandardsResponseTypeDef",
    "ClientGetFindingsFiltersAwsAccountIdTypeDef",
    "ClientGetFindingsFiltersCompanyNameTypeDef",
    "ClientGetFindingsFiltersComplianceStatusTypeDef",
    "ClientGetFindingsFiltersConfidenceTypeDef",
    "ClientGetFindingsFiltersCreatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersCreatedAtTypeDef",
    "ClientGetFindingsFiltersCriticalityTypeDef",
    "ClientGetFindingsFiltersDescriptionTypeDef",
    "ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersFirstObservedAtTypeDef",
    "ClientGetFindingsFiltersGeneratorIdTypeDef",
    "ClientGetFindingsFiltersIdTypeDef",
    "ClientGetFindingsFiltersKeywordTypeDef",
    "ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersLastObservedAtTypeDef",
    "ClientGetFindingsFiltersMalwareNameTypeDef",
    "ClientGetFindingsFiltersMalwarePathTypeDef",
    "ClientGetFindingsFiltersMalwareStateTypeDef",
    "ClientGetFindingsFiltersMalwareTypeTypeDef",
    "ClientGetFindingsFiltersNetworkDestinationDomainTypeDef",
    "ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef",
    "ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef",
    "ClientGetFindingsFiltersNetworkDestinationPortTypeDef",
    "ClientGetFindingsFiltersNetworkDirectionTypeDef",
    "ClientGetFindingsFiltersNetworkProtocolTypeDef",
    "ClientGetFindingsFiltersNetworkSourceDomainTypeDef",
    "ClientGetFindingsFiltersNetworkSourceIpV4TypeDef",
    "ClientGetFindingsFiltersNetworkSourceIpV6TypeDef",
    "ClientGetFindingsFiltersNetworkSourceMacTypeDef",
    "ClientGetFindingsFiltersNetworkSourcePortTypeDef",
    "ClientGetFindingsFiltersNoteTextTypeDef",
    "ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersNoteUpdatedAtTypeDef",
    "ClientGetFindingsFiltersNoteUpdatedByTypeDef",
    "ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersProcessLaunchedAtTypeDef",
    "ClientGetFindingsFiltersProcessNameTypeDef",
    "ClientGetFindingsFiltersProcessParentPidTypeDef",
    "ClientGetFindingsFiltersProcessPathTypeDef",
    "ClientGetFindingsFiltersProcessPidTypeDef",
    "ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersProcessTerminatedAtTypeDef",
    "ClientGetFindingsFiltersProductArnTypeDef",
    "ClientGetFindingsFiltersProductFieldsTypeDef",
    "ClientGetFindingsFiltersProductNameTypeDef",
    "ClientGetFindingsFiltersRecommendationTextTypeDef",
    "ClientGetFindingsFiltersRecordStateTypeDef",
    "ClientGetFindingsFiltersRelatedFindingsIdTypeDef",
    "ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientGetFindingsFiltersResourceContainerImageIdTypeDef",
    "ClientGetFindingsFiltersResourceContainerImageNameTypeDef",
    "ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef",
    "ClientGetFindingsFiltersResourceContainerNameTypeDef",
    "ClientGetFindingsFiltersResourceDetailsOtherTypeDef",
    "ClientGetFindingsFiltersResourceIdTypeDef",
    "ClientGetFindingsFiltersResourcePartitionTypeDef",
    "ClientGetFindingsFiltersResourceRegionTypeDef",
    "ClientGetFindingsFiltersResourceTagsTypeDef",
    "ClientGetFindingsFiltersResourceTypeTypeDef",
    "ClientGetFindingsFiltersSeverityLabelTypeDef",
    "ClientGetFindingsFiltersSeverityNormalizedTypeDef",
    "ClientGetFindingsFiltersSeverityProductTypeDef",
    "ClientGetFindingsFiltersSourceUrlTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef",
    "ClientGetFindingsFiltersTitleTypeDef",
    "ClientGetFindingsFiltersTypeTypeDef",
    "ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersUpdatedAtTypeDef",
    "ClientGetFindingsFiltersUserDefinedFieldsTypeDef",
    "ClientGetFindingsFiltersVerificationStateTypeDef",
    "ClientGetFindingsFiltersWorkflowStateTypeDef",
    "ClientGetFindingsFiltersTypeDef",
    "ClientGetFindingsResponseFindingsComplianceTypeDef",
    "ClientGetFindingsResponseFindingsMalwareTypeDef",
    "ClientGetFindingsResponseFindingsNetworkTypeDef",
    "ClientGetFindingsResponseFindingsNoteTypeDef",
    "ClientGetFindingsResponseFindingsProcessTypeDef",
    "ClientGetFindingsResponseFindingsRelatedFindingsTypeDef",
    "ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef",
    "ClientGetFindingsResponseFindingsRemediationTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsIamRoleTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsKmsKeyTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsSqsQueueTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesTypeDef",
    "ClientGetFindingsResponseFindingsSeverityTypeDef",
    "ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef",
    "ClientGetFindingsResponseFindingsTypeDef",
    "ClientGetFindingsResponseTypeDef",
    "ClientGetFindingsSortCriteriaTypeDef",
    "ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef",
    "ClientGetInsightResultsResponseInsightResultsTypeDef",
    "ClientGetInsightResultsResponseTypeDef",
    "ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef",
    "ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef",
    "ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersKeywordTypeDef",
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProductArnTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProductNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    "ClientGetInsightsResponseInsightsFiltersTitleTypeDef",
    "ClientGetInsightsResponseInsightsFiltersTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef",
    "ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersTypeDef",
    "ClientGetInsightsResponseInsightsTypeDef",
    "ClientGetInsightsResponseTypeDef",
    "ClientGetInvitationsCountResponseTypeDef",
    "ClientGetMasterAccountResponseMasterTypeDef",
    "ClientGetMasterAccountResponseTypeDef",
    "ClientGetMembersResponseMembersTypeDef",
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    "ClientGetMembersResponseTypeDef",
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    "ClientInviteMembersResponseTypeDef",
    "ClientListEnabledProductsForImportResponseTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateFindingsFiltersAwsAccountIdTypeDef",
    "ClientUpdateFindingsFiltersCompanyNameTypeDef",
    "ClientUpdateFindingsFiltersComplianceStatusTypeDef",
    "ClientUpdateFindingsFiltersConfidenceTypeDef",
    "ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersCreatedAtTypeDef",
    "ClientUpdateFindingsFiltersCriticalityTypeDef",
    "ClientUpdateFindingsFiltersDescriptionTypeDef",
    "ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersFirstObservedAtTypeDef",
    "ClientUpdateFindingsFiltersGeneratorIdTypeDef",
    "ClientUpdateFindingsFiltersIdTypeDef",
    "ClientUpdateFindingsFiltersKeywordTypeDef",
    "ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersLastObservedAtTypeDef",
    "ClientUpdateFindingsFiltersMalwareNameTypeDef",
    "ClientUpdateFindingsFiltersMalwarePathTypeDef",
    "ClientUpdateFindingsFiltersMalwareStateTypeDef",
    "ClientUpdateFindingsFiltersMalwareTypeTypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef",
    "ClientUpdateFindingsFiltersNetworkDirectionTypeDef",
    "ClientUpdateFindingsFiltersNetworkProtocolTypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceMacTypeDef",
    "ClientUpdateFindingsFiltersNetworkSourcePortTypeDef",
    "ClientUpdateFindingsFiltersNoteTextTypeDef",
    "ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef",
    "ClientUpdateFindingsFiltersNoteUpdatedByTypeDef",
    "ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef",
    "ClientUpdateFindingsFiltersProcessNameTypeDef",
    "ClientUpdateFindingsFiltersProcessParentPidTypeDef",
    "ClientUpdateFindingsFiltersProcessPathTypeDef",
    "ClientUpdateFindingsFiltersProcessPidTypeDef",
    "ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef",
    "ClientUpdateFindingsFiltersProductArnTypeDef",
    "ClientUpdateFindingsFiltersProductFieldsTypeDef",
    "ClientUpdateFindingsFiltersProductNameTypeDef",
    "ClientUpdateFindingsFiltersRecommendationTextTypeDef",
    "ClientUpdateFindingsFiltersRecordStateTypeDef",
    "ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef",
    "ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerNameTypeDef",
    "ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef",
    "ClientUpdateFindingsFiltersResourceIdTypeDef",
    "ClientUpdateFindingsFiltersResourcePartitionTypeDef",
    "ClientUpdateFindingsFiltersResourceRegionTypeDef",
    "ClientUpdateFindingsFiltersResourceTagsTypeDef",
    "ClientUpdateFindingsFiltersResourceTypeTypeDef",
    "ClientUpdateFindingsFiltersSeverityLabelTypeDef",
    "ClientUpdateFindingsFiltersSeverityNormalizedTypeDef",
    "ClientUpdateFindingsFiltersSeverityProductTypeDef",
    "ClientUpdateFindingsFiltersSourceUrlTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef",
    "ClientUpdateFindingsFiltersTitleTypeDef",
    "ClientUpdateFindingsFiltersTypeTypeDef",
    "ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersUpdatedAtTypeDef",
    "ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef",
    "ClientUpdateFindingsFiltersVerificationStateTypeDef",
    "ClientUpdateFindingsFiltersWorkflowStateTypeDef",
    "ClientUpdateFindingsFiltersTypeDef",
    "ClientUpdateFindingsNoteTypeDef",
    "ClientUpdateInsightFiltersAwsAccountIdTypeDef",
    "ClientUpdateInsightFiltersCompanyNameTypeDef",
    "ClientUpdateInsightFiltersComplianceStatusTypeDef",
    "ClientUpdateInsightFiltersConfidenceTypeDef",
    "ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersCreatedAtTypeDef",
    "ClientUpdateInsightFiltersCriticalityTypeDef",
    "ClientUpdateInsightFiltersDescriptionTypeDef",
    "ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersFirstObservedAtTypeDef",
    "ClientUpdateInsightFiltersGeneratorIdTypeDef",
    "ClientUpdateInsightFiltersIdTypeDef",
    "ClientUpdateInsightFiltersKeywordTypeDef",
    "ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersLastObservedAtTypeDef",
    "ClientUpdateInsightFiltersMalwareNameTypeDef",
    "ClientUpdateInsightFiltersMalwarePathTypeDef",
    "ClientUpdateInsightFiltersMalwareStateTypeDef",
    "ClientUpdateInsightFiltersMalwareTypeTypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationPortTypeDef",
    "ClientUpdateInsightFiltersNetworkDirectionTypeDef",
    "ClientUpdateInsightFiltersNetworkProtocolTypeDef",
    "ClientUpdateInsightFiltersNetworkSourceDomainTypeDef",
    "ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef",
    "ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef",
    "ClientUpdateInsightFiltersNetworkSourceMacTypeDef",
    "ClientUpdateInsightFiltersNetworkSourcePortTypeDef",
    "ClientUpdateInsightFiltersNoteTextTypeDef",
    "ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersNoteUpdatedAtTypeDef",
    "ClientUpdateInsightFiltersNoteUpdatedByTypeDef",
    "ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersProcessLaunchedAtTypeDef",
    "ClientUpdateInsightFiltersProcessNameTypeDef",
    "ClientUpdateInsightFiltersProcessParentPidTypeDef",
    "ClientUpdateInsightFiltersProcessPathTypeDef",
    "ClientUpdateInsightFiltersProcessPidTypeDef",
    "ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersProcessTerminatedAtTypeDef",
    "ClientUpdateInsightFiltersProductArnTypeDef",
    "ClientUpdateInsightFiltersProductFieldsTypeDef",
    "ClientUpdateInsightFiltersProductNameTypeDef",
    "ClientUpdateInsightFiltersRecommendationTextTypeDef",
    "ClientUpdateInsightFiltersRecordStateTypeDef",
    "ClientUpdateInsightFiltersRelatedFindingsIdTypeDef",
    "ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientUpdateInsightFiltersResourceContainerImageIdTypeDef",
    "ClientUpdateInsightFiltersResourceContainerImageNameTypeDef",
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef",
    "ClientUpdateInsightFiltersResourceContainerNameTypeDef",
    "ClientUpdateInsightFiltersResourceDetailsOtherTypeDef",
    "ClientUpdateInsightFiltersResourceIdTypeDef",
    "ClientUpdateInsightFiltersResourcePartitionTypeDef",
    "ClientUpdateInsightFiltersResourceRegionTypeDef",
    "ClientUpdateInsightFiltersResourceTagsTypeDef",
    "ClientUpdateInsightFiltersResourceTypeTypeDef",
    "ClientUpdateInsightFiltersSeverityLabelTypeDef",
    "ClientUpdateInsightFiltersSeverityNormalizedTypeDef",
    "ClientUpdateInsightFiltersSeverityProductTypeDef",
    "ClientUpdateInsightFiltersSourceUrlTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef",
    "ClientUpdateInsightFiltersTitleTypeDef",
    "ClientUpdateInsightFiltersTypeTypeDef",
    "ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersUpdatedAtTypeDef",
    "ClientUpdateInsightFiltersUserDefinedFieldsTypeDef",
    "ClientUpdateInsightFiltersVerificationStateTypeDef",
    "ClientUpdateInsightFiltersWorkflowStateTypeDef",
    "ClientUpdateInsightFiltersTypeDef",
    "StandardsSubscriptionTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "ComplianceTypeDef",
    "MalwareTypeDef",
    "NetworkTypeDef",
    "NoteTypeDef",
    "ProcessDetailsTypeDef",
    "RelatedFindingTypeDef",
    "RecommendationTypeDef",
    "RemediationTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AvailabilityZoneTypeDef",
    "LoadBalancerStateTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "ContainerDetailsTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "SeverityTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "AwsSecurityFindingTypeDef",
    "GetFindingsResponseTypeDef",
    "InsightTypeDef",
    "GetInsightsResponseTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "InvitationTypeDef",
    "ListInvitationsResponseTypeDef",
    "MemberTypeDef",
    "ListMembersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SortCriterionTypeDef",
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef", {"Value": int, "Unit": Literal["DAYS"]}, total=False
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef", {"Start": str, "End": str, "DateRange": DateRangeTypeDef}, total=False
)

IpFilterTypeDef = TypedDict("IpFilterTypeDef", {"Cidr": str}, total=False)

KeywordFilterTypeDef = TypedDict("KeywordFilterTypeDef", {"Value": str}, total=False)

MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef", {"Key": str, "Value": str, "Comparison": Literal["EQUALS"]}, total=False
)

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef", {"Gte": float, "Lte": float, "Eq": float}, total=False
)

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef", {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]}, total=False
)

AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": List[StringFilterTypeDef],
        "AwsAccountId": List[StringFilterTypeDef],
        "Id": List[StringFilterTypeDef],
        "GeneratorId": List[StringFilterTypeDef],
        "Type": List[StringFilterTypeDef],
        "FirstObservedAt": List[DateFilterTypeDef],
        "LastObservedAt": List[DateFilterTypeDef],
        "CreatedAt": List[DateFilterTypeDef],
        "UpdatedAt": List[DateFilterTypeDef],
        "SeverityProduct": List[NumberFilterTypeDef],
        "SeverityNormalized": List[NumberFilterTypeDef],
        "SeverityLabel": List[StringFilterTypeDef],
        "Confidence": List[NumberFilterTypeDef],
        "Criticality": List[NumberFilterTypeDef],
        "Title": List[StringFilterTypeDef],
        "Description": List[StringFilterTypeDef],
        "RecommendationText": List[StringFilterTypeDef],
        "SourceUrl": List[StringFilterTypeDef],
        "ProductFields": List[MapFilterTypeDef],
        "ProductName": List[StringFilterTypeDef],
        "CompanyName": List[StringFilterTypeDef],
        "UserDefinedFields": List[MapFilterTypeDef],
        "MalwareName": List[StringFilterTypeDef],
        "MalwareType": List[StringFilterTypeDef],
        "MalwarePath": List[StringFilterTypeDef],
        "MalwareState": List[StringFilterTypeDef],
        "NetworkDirection": List[StringFilterTypeDef],
        "NetworkProtocol": List[StringFilterTypeDef],
        "NetworkSourceIpV4": List[IpFilterTypeDef],
        "NetworkSourceIpV6": List[IpFilterTypeDef],
        "NetworkSourcePort": List[NumberFilterTypeDef],
        "NetworkSourceDomain": List[StringFilterTypeDef],
        "NetworkSourceMac": List[StringFilterTypeDef],
        "NetworkDestinationIpV4": List[IpFilterTypeDef],
        "NetworkDestinationIpV6": List[IpFilterTypeDef],
        "NetworkDestinationPort": List[NumberFilterTypeDef],
        "NetworkDestinationDomain": List[StringFilterTypeDef],
        "ProcessName": List[StringFilterTypeDef],
        "ProcessPath": List[StringFilterTypeDef],
        "ProcessPid": List[NumberFilterTypeDef],
        "ProcessParentPid": List[NumberFilterTypeDef],
        "ProcessLaunchedAt": List[DateFilterTypeDef],
        "ProcessTerminatedAt": List[DateFilterTypeDef],
        "ThreatIntelIndicatorType": List[StringFilterTypeDef],
        "ThreatIntelIndicatorValue": List[StringFilterTypeDef],
        "ThreatIntelIndicatorCategory": List[StringFilterTypeDef],
        "ThreatIntelIndicatorLastObservedAt": List[DateFilterTypeDef],
        "ThreatIntelIndicatorSource": List[StringFilterTypeDef],
        "ThreatIntelIndicatorSourceUrl": List[StringFilterTypeDef],
        "ResourceType": List[StringFilterTypeDef],
        "ResourceId": List[StringFilterTypeDef],
        "ResourcePartition": List[StringFilterTypeDef],
        "ResourceRegion": List[StringFilterTypeDef],
        "ResourceTags": List[MapFilterTypeDef],
        "ResourceAwsEc2InstanceType": List[StringFilterTypeDef],
        "ResourceAwsEc2InstanceImageId": List[StringFilterTypeDef],
        "ResourceAwsEc2InstanceIpV4Addresses": List[IpFilterTypeDef],
        "ResourceAwsEc2InstanceIpV6Addresses": List[IpFilterTypeDef],
        "ResourceAwsEc2InstanceKeyName": List[StringFilterTypeDef],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[StringFilterTypeDef],
        "ResourceAwsEc2InstanceVpcId": List[StringFilterTypeDef],
        "ResourceAwsEc2InstanceSubnetId": List[StringFilterTypeDef],
        "ResourceAwsEc2InstanceLaunchedAt": List[DateFilterTypeDef],
        "ResourceAwsS3BucketOwnerId": List[StringFilterTypeDef],
        "ResourceAwsS3BucketOwnerName": List[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyUserName": List[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyStatus": List[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyCreatedAt": List[DateFilterTypeDef],
        "ResourceContainerName": List[StringFilterTypeDef],
        "ResourceContainerImageId": List[StringFilterTypeDef],
        "ResourceContainerImageName": List[StringFilterTypeDef],
        "ResourceContainerLaunchedAt": List[DateFilterTypeDef],
        "ResourceDetailsOther": List[MapFilterTypeDef],
        "ComplianceStatus": List[StringFilterTypeDef],
        "VerificationState": List[StringFilterTypeDef],
        "WorkflowState": List[StringFilterTypeDef],
        "RecordState": List[StringFilterTypeDef],
        "RelatedFindingsProductArn": List[StringFilterTypeDef],
        "RelatedFindingsId": List[StringFilterTypeDef],
        "NoteText": List[StringFilterTypeDef],
        "NoteUpdatedAt": List[DateFilterTypeDef],
        "NoteUpdatedBy": List[StringFilterTypeDef],
        "Keyword": List[KeywordFilterTypeDef],
    },
    total=False,
)

ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

ClientBatchDisableStandardsResponseTypeDef = TypedDict(
    "ClientBatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)

ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

ClientBatchEnableStandardsResponseTypeDef = TypedDict(
    "ClientBatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)

ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef = TypedDict(
    "ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef",
    {"StandardsArn": str, "StandardsInput": Dict[str, str]},
    total=False,
)

ClientBatchImportFindingsFindingsComplianceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsComplianceTypeDef",
    {
        "Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"],
        "RelatedRequirements": List[str],
    },
    total=False,
)

ClientBatchImportFindingsFindingsMalwareTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)

ClientBatchImportFindingsFindingsNetworkTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsNoteTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)

ClientBatchImportFindingsFindingsProcessTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsRelatedFindingsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)

ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)

ClientBatchImportFindingsFindingsRemediationTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsRemediationTypeDef",
    {"Recommendation": ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef",
    {"Bucket": str, "Enabled": bool, "IncludeCookies": bool, "Prefix": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef",
    {"DomainName": str, "Id": str, "OriginPath": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef
        ]
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef",
    {
        "DomainName": str,
        "ETag": str,
        "LastModifiedTime": str,
        "Logging": ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef,
        "Origins": ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef,
        "Status": str,
        "WebAclId": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {"Credential": str, "CredentialProvider": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": str,
        "ImagePullCredentialsType": str,
        "RegistryCredential": ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef,
        "Type": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef",
    {"Type": str, "Location": str, "GitCloneDepth": int, "InsecureSsl": bool},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef",
    {"VpcId": str, "Subnets": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectTypeDef",
    {
        "EncryptionKey": str,
        "Environment": ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef,
        "Name": str,
        "Source": ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef,
        "ServiceRole": str,
        "VpcConfig": ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": str,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef",
    {
        "Attachment": ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef,
        "NetworkInterfaceId": str,
        "SecurityGroups": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef
        ],
        "SourceDestCheck": bool,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef",
    {"CidrIp": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef",
    {"CidrIpv6": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef",
    {"PrefixListId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef
        ],
        "IpRanges": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef
        ],
        "Ipv6Ranges": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef
        ],
        "PrefixListIds": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef
        ],
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef",
    {"CidrIp": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef",
    {"CidrIpv6": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef",
    {"PrefixListId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef
        ],
        "IpRanges": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef
        ],
        "Ipv6Ranges": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef
        ],
        "PrefixListIds": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef
        ],
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
        "OwnerId": str,
        "VpcId": str,
        "IpPermissions": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef
        ],
        "IpPermissionsEgress": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef
        ],
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VPCId": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainTypeDef",
    {
        "AccessPolicies": str,
        "DomainEndpointOptions": ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef,
        "DomainId": str,
        "DomainName": str,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "ElasticsearchVersion": str,
        "EncryptionAtRestOptions": ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef,
        "VPCOptions": ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef",
    {"ZoneName": str, "SubnetId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef",
    {"Code": str, "Reason": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef",
    {
        "AvailabilityZones": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef
        ],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": List[str],
        "State": ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef,
        "Type": str,
        "VpcId": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
        "CreatedAt": str,
        "PrincipalId": str,
        "PrincipalType": str,
        "PrincipalName": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsIamRoleTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsIamRoleTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "CreateDate": str,
        "RoleId": str,
        "RoleName": str,
        "MaxSessionDuration": int,
        "Path": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsKmsKeyTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsKmsKeyTypeDef",
    {
        "AWSAccountId": str,
        "CreationDate": float,
        "KeyId": str,
        "KeyManager": str,
        "KeyState": str,
        "Origin": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "SubnetIds": List[str], "VpcId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTypeDef",
    {
        "Code": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef,
        "CodeSha256": str,
        "DeadLetterConfig": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef,
        "Environment": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef,
        "FunctionName": str,
        "Handler": str,
        "KmsKeyArn": str,
        "LastModified": str,
        "Layers": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef
        ],
        "MasterArn": str,
        "MemorySize": int,
        "RevisionId": str,
        "Role": str,
        "Runtime": str,
        "Timeout": int,
        "TracingConfig": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef,
        "VpcConfig": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef,
        "Version": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef",
    {"Version": int, "CompatibleRuntimes": List[str], "CreatedDate": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceTypeDef",
    {
        "AssociatedRoles": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef
        ],
        "CACertificateIdentifier": str,
        "DBClusterIdentifier": str,
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "DbInstancePort": int,
        "DbiResourceId": str,
        "DBName": str,
        "DeletionProtection": bool,
        "Endpoint": ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef,
        "Engine": str,
        "EngineVersion": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "InstanceCreateTime": str,
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "StorageEncrypted": bool,
        "TdeCredentialArn": str,
        "VpcSecurityGroups": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef",
    {"Endpoint": str, "Protocol": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicTypeDef",
    {
        "KmsMasterKeyId": str,
        "Subscription": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef
        ],
        "TopicName": str,
        "Owner": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsSqsQueueTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsSqsQueueTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": int,
        "KmsMasterKeyId": str,
        "QueueName": str,
        "DeadLetterTargetArn": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef",
    {"Type": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef",
    {"Type": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesTypeDef",
    {
        "Action": ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef,
        "ExcludedRules": List[
            ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef
        ],
        "OverrideAction": ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclTypeDef",
    {
        "Name": str,
        "DefaultAction": str,
        "Rules": List[ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclRulesTypeDef],
        "WebAclId": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsTypeDef",
    {
        "AwsCodeBuildProject": ClientBatchImportFindingsFindingsResourcesDetailsAwsCodeBuildProjectTypeDef,
        "AwsCloudFrontDistribution": ClientBatchImportFindingsFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef,
        "AwsEc2Instance": ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsEc2NetworkInterface": ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef,
        "AwsEc2SecurityGroup": ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef,
        "AwsElbv2LoadBalancer": ClientBatchImportFindingsFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef,
        "AwsElasticsearchDomain": ClientBatchImportFindingsFindingsResourcesDetailsAwsElasticsearchDomainTypeDef,
        "AwsS3Bucket": ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "AwsIamRole": ClientBatchImportFindingsFindingsResourcesDetailsAwsIamRoleTypeDef,
        "AwsKmsKey": ClientBatchImportFindingsFindingsResourcesDetailsAwsKmsKeyTypeDef,
        "AwsLambdaFunction": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaFunctionTypeDef,
        "AwsLambdaLayerVersion": ClientBatchImportFindingsFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef,
        "AwsRdsDbInstance": ClientBatchImportFindingsFindingsResourcesDetailsAwsRdsDbInstanceTypeDef,
        "AwsSnsTopic": ClientBatchImportFindingsFindingsResourcesDetailsAwsSnsTopicTypeDef,
        "AwsSqsQueue": ClientBatchImportFindingsFindingsResourcesDetailsAwsSqsQueueTypeDef,
        "AwsWafWebAcl": ClientBatchImportFindingsFindingsResourcesDetailsAwsWafWebAclTypeDef,
        "Container": ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ClientBatchImportFindingsFindingsResourcesDetailsTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsFindingsSeverityTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)

ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": ClientBatchImportFindingsFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": ClientBatchImportFindingsFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[ClientBatchImportFindingsFindingsMalwareTypeDef],
        "Network": ClientBatchImportFindingsFindingsNetworkTypeDef,
        "Process": ClientBatchImportFindingsFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[ClientBatchImportFindingsFindingsResourcesTypeDef],
        "Compliance": ClientBatchImportFindingsFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[ClientBatchImportFindingsFindingsRelatedFindingsTypeDef],
        "Note": ClientBatchImportFindingsFindingsNoteTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsResponseFailedFindingsTypeDef = TypedDict(
    "ClientBatchImportFindingsResponseFailedFindingsTypeDef",
    {"Id": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchImportFindingsResponseTypeDef = TypedDict(
    "ClientBatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List[ClientBatchImportFindingsResponseFailedFindingsTypeDef],
    },
    total=False,
)

ClientCreateActionTargetResponseTypeDef = TypedDict(
    "ClientCreateActionTargetResponseTypeDef", {"ActionTargetArn": str}, total=False
)

ClientCreateInsightFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersCompanyNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersComplianceStatusTypeDef = TypedDict(
    "ClientCreateInsightFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersConfidenceTypeDef = TypedDict(
    "ClientCreateInsightFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientCreateInsightFiltersCreatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientCreateInsightFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientCreateInsightFiltersCriticalityTypeDef = TypedDict(
    "ClientCreateInsightFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersDescriptionTypeDef = TypedDict(
    "ClientCreateInsightFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersGeneratorIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersKeywordTypeDef = TypedDict(
    "ClientCreateInsightFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersLastObservedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersMalwareNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersMalwarePathTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersMalwareStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersMalwareTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersNoteTextTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersProcessNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProcessParentPidTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersProcessPathTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProcessPidTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersProductArnTypeDef = TypedDict(
    "ClientCreateInsightFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProductFieldsTypeDef = TypedDict(
    "ClientCreateInsightFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersProductNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRecommendationTextTypeDef = TypedDict(
    "ClientCreateInsightFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRecordStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersResourceIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourcePartitionTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceRegionTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceTagsTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersResourceTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersSeverityLabelTypeDef = TypedDict(
    "ClientCreateInsightFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientCreateInsightFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersSeverityProductTypeDef = TypedDict(
    "ClientCreateInsightFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersSourceUrlTypeDef = TypedDict(
    "ClientCreateInsightFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersTitleTypeDef = TypedDict(
    "ClientCreateInsightFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientCreateInsightFiltersUpdatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientCreateInsightFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientCreateInsightFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersVerificationStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersWorkflowStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersTypeDef = TypedDict(
    "ClientCreateInsightFiltersTypeDef",
    {
        "ProductArn": List[ClientCreateInsightFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientCreateInsightFiltersAwsAccountIdTypeDef],
        "Id": List[ClientCreateInsightFiltersIdTypeDef],
        "GeneratorId": List[ClientCreateInsightFiltersGeneratorIdTypeDef],
        "Type": List[ClientCreateInsightFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientCreateInsightFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientCreateInsightFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientCreateInsightFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientCreateInsightFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientCreateInsightFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientCreateInsightFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientCreateInsightFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientCreateInsightFiltersConfidenceTypeDef],
        "Criticality": List[ClientCreateInsightFiltersCriticalityTypeDef],
        "Title": List[ClientCreateInsightFiltersTitleTypeDef],
        "Description": List[ClientCreateInsightFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientCreateInsightFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientCreateInsightFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientCreateInsightFiltersProductFieldsTypeDef],
        "ProductName": List[ClientCreateInsightFiltersProductNameTypeDef],
        "CompanyName": List[ClientCreateInsightFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientCreateInsightFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientCreateInsightFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientCreateInsightFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientCreateInsightFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientCreateInsightFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientCreateInsightFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientCreateInsightFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientCreateInsightFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientCreateInsightFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientCreateInsightFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientCreateInsightFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientCreateInsightFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientCreateInsightFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientCreateInsightFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientCreateInsightFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientCreateInsightFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientCreateInsightFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientCreateInsightFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientCreateInsightFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientCreateInsightFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientCreateInsightFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientCreateInsightFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientCreateInsightFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientCreateInsightFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientCreateInsightFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientCreateInsightFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientCreateInsightFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientCreateInsightFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientCreateInsightFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientCreateInsightFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientCreateInsightFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientCreateInsightFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientCreateInsightFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientCreateInsightFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientCreateInsightFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientCreateInsightFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientCreateInsightFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientCreateInsightFiltersKeywordTypeDef],
    },
    total=False,
)

ClientCreateInsightResponseTypeDef = TypedDict(
    "ClientCreateInsightResponseTypeDef", {"InsightArn": str}, total=False
)

ClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "ClientCreateMembersAccountDetailsTypeDef", {"AccountId": str, "Email": str}, total=False
)

ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientCreateMembersResponseTypeDef = TypedDict(
    "ClientCreateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientCreateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientDeclineInvitationsResponseTypeDef = TypedDict(
    "ClientDeclineInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeleteActionTargetResponseTypeDef = TypedDict(
    "ClientDeleteActionTargetResponseTypeDef", {"ActionTargetArn": str}, total=False
)

ClientDeleteInsightResponseTypeDef = TypedDict(
    "ClientDeleteInsightResponseTypeDef", {"InsightArn": str}, total=False
)

ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientDeleteInvitationsResponseTypeDef = TypedDict(
    "ClientDeleteInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientDeleteMembersResponseTypeDef = TypedDict(
    "ClientDeleteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDescribeActionTargetsResponseActionTargetsTypeDef = TypedDict(
    "ClientDescribeActionTargetsResponseActionTargetsTypeDef",
    {"ActionTargetArn": str, "Name": str, "Description": str},
    total=False,
)

ClientDescribeActionTargetsResponseTypeDef = TypedDict(
    "ClientDescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List[ClientDescribeActionTargetsResponseActionTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeHubResponseTypeDef = TypedDict(
    "ClientDescribeHubResponseTypeDef", {"HubArn": str, "SubscribedAt": str}, total=False
)

ClientDescribeProductsResponseProductsTypeDef = TypedDict(
    "ClientDescribeProductsResponseProductsTypeDef",
    {
        "ProductArn": str,
        "ProductName": str,
        "CompanyName": str,
        "Description": str,
        "Categories": List[str],
        "MarketplaceUrl": str,
        "ActivationUrl": str,
        "ProductSubscriptionResourcePolicy": str,
    },
    total=False,
)

ClientDescribeProductsResponseTypeDef = TypedDict(
    "ClientDescribeProductsResponseTypeDef",
    {"Products": List[ClientDescribeProductsResponseProductsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeStandardsControlsResponseControlsTypeDef = TypedDict(
    "ClientDescribeStandardsControlsResponseControlsTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": Literal["ENABLED", "DISABLED"],
        "DisabledReason": str,
        "ControlStatusUpdatedAt": datetime,
        "ControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"],
    },
    total=False,
)

ClientDescribeStandardsControlsResponseTypeDef = TypedDict(
    "ClientDescribeStandardsControlsResponseTypeDef",
    {"Controls": List[ClientDescribeStandardsControlsResponseControlsTypeDef], "NextToken": str},
    total=False,
)

ClientEnableImportFindingsForProductResponseTypeDef = TypedDict(
    "ClientEnableImportFindingsForProductResponseTypeDef",
    {"ProductSubscriptionArn": str},
    total=False,
)

ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

ClientGetEnabledStandardsResponseTypeDef = TypedDict(
    "ClientGetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetFindingsFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersCompanyNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersComplianceStatusTypeDef = TypedDict(
    "ClientGetFindingsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersConfidenceTypeDef = TypedDict(
    "ClientGetFindingsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientGetFindingsFiltersCreatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersCriticalityTypeDef = TypedDict(
    "ClientGetFindingsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersDescriptionTypeDef = TypedDict(
    "ClientGetFindingsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersGeneratorIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersKeywordTypeDef = TypedDict(
    "ClientGetFindingsFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersLastObservedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersLastObservedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersMalwareNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersMalwarePathTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersMalwareStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersMalwareTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersNoteTextTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersProcessNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProcessParentPidTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersProcessPathTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProcessPidTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersProductArnTypeDef = TypedDict(
    "ClientGetFindingsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProductFieldsTypeDef = TypedDict(
    "ClientGetFindingsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersProductNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRecommendationTextTypeDef = TypedDict(
    "ClientGetFindingsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRecordStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersResourceIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourcePartitionTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceRegionTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceTagsTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersResourceTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersSeverityLabelTypeDef = TypedDict(
    "ClientGetFindingsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientGetFindingsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersSeverityProductTypeDef = TypedDict(
    "ClientGetFindingsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersSourceUrlTypeDef = TypedDict(
    "ClientGetFindingsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersTitleTypeDef = TypedDict(
    "ClientGetFindingsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientGetFindingsFiltersUpdatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientGetFindingsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersVerificationStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersWorkflowStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersTypeDef = TypedDict(
    "ClientGetFindingsFiltersTypeDef",
    {
        "ProductArn": List[ClientGetFindingsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientGetFindingsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientGetFindingsFiltersIdTypeDef],
        "GeneratorId": List[ClientGetFindingsFiltersGeneratorIdTypeDef],
        "Type": List[ClientGetFindingsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientGetFindingsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientGetFindingsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientGetFindingsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientGetFindingsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientGetFindingsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientGetFindingsFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientGetFindingsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientGetFindingsFiltersConfidenceTypeDef],
        "Criticality": List[ClientGetFindingsFiltersCriticalityTypeDef],
        "Title": List[ClientGetFindingsFiltersTitleTypeDef],
        "Description": List[ClientGetFindingsFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientGetFindingsFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientGetFindingsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientGetFindingsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientGetFindingsFiltersProductNameTypeDef],
        "CompanyName": List[ClientGetFindingsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientGetFindingsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientGetFindingsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientGetFindingsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientGetFindingsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientGetFindingsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientGetFindingsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientGetFindingsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientGetFindingsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientGetFindingsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientGetFindingsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientGetFindingsFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientGetFindingsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientGetFindingsFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientGetFindingsFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientGetFindingsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientGetFindingsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientGetFindingsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientGetFindingsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientGetFindingsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientGetFindingsFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef],
        "ThreatIntelIndicatorCategory": List[
            ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientGetFindingsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientGetFindingsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientGetFindingsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientGetFindingsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientGetFindingsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientGetFindingsFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientGetFindingsFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientGetFindingsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientGetFindingsFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientGetFindingsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientGetFindingsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientGetFindingsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientGetFindingsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef],
        "RelatedFindingsId": List[ClientGetFindingsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientGetFindingsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientGetFindingsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientGetFindingsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientGetFindingsFiltersKeywordTypeDef],
    },
    total=False,
)

ClientGetFindingsResponseFindingsComplianceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsComplianceTypeDef",
    {
        "Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"],
        "RelatedRequirements": List[str],
    },
    total=False,
)

ClientGetFindingsResponseFindingsMalwareTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)

ClientGetFindingsResponseFindingsNetworkTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsNoteTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)

ClientGetFindingsResponseFindingsProcessTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsRelatedFindingsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)

ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)

ClientGetFindingsResponseFindingsRemediationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsRemediationTypeDef",
    {"Recommendation": ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef",
    {"Bucket": str, "Enabled": bool, "IncludeCookies": bool, "Prefix": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef",
    {"DomainName": str, "Id": str, "OriginPath": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsItemsTypeDef
        ]
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef",
    {
        "DomainName": str,
        "ETag": str,
        "LastModifiedTime": str,
        "Logging": ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionLoggingTypeDef,
        "Origins": ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionOriginsTypeDef,
        "Status": str,
        "WebAclId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {"Credential": str, "CredentialProvider": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": str,
        "ImagePullCredentialsType": str,
        "RegistryCredential": ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef,
        "Type": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef",
    {"Type": str, "Location": str, "GitCloneDepth": int, "InsecureSsl": bool},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef",
    {"VpcId": str, "Subnets": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectTypeDef",
    {
        "EncryptionKey": str,
        "Environment": ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectEnvironmentTypeDef,
        "Name": str,
        "Source": ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectSourceTypeDef,
        "ServiceRole": str,
        "VpcConfig": ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectVpcConfigTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": str,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef",
    {
        "Attachment": ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceAttachmentTypeDef,
        "NetworkInterfaceId": str,
        "SecurityGroups": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceSecurityGroupsTypeDef
        ],
        "SourceDestCheck": bool,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef",
    {"CidrIp": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef",
    {"CidrIpv6": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef",
    {"PrefixListId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressUserIdGroupPairsTypeDef
        ],
        "IpRanges": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpRangesTypeDef
        ],
        "Ipv6Ranges": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressIpv6RangesTypeDef
        ],
        "PrefixListIds": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressPrefixListIdsTypeDef
        ],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef",
    {"CidrIp": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef",
    {"CidrIpv6": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef",
    {"PrefixListId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsUserIdGroupPairsTypeDef
        ],
        "IpRanges": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpRangesTypeDef
        ],
        "Ipv6Ranges": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsIpv6RangesTypeDef
        ],
        "PrefixListIds": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsPrefixListIdsTypeDef
        ],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
        "OwnerId": str,
        "VpcId": str,
        "IpPermissions": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsTypeDef
        ],
        "IpPermissionsEgress": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupIpPermissionsEgressTypeDef
        ],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VPCId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainTypeDef",
    {
        "AccessPolicies": str,
        "DomainEndpointOptions": ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainDomainEndpointOptionsTypeDef,
        "DomainId": str,
        "DomainName": str,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "ElasticsearchVersion": str,
        "EncryptionAtRestOptions": ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef,
        "VPCOptions": ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainVPCOptionsTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef",
    {"ZoneName": str, "SubnetId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef",
    {"Code": str, "Reason": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef",
    {
        "AvailabilityZones": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerAvailabilityZonesTypeDef
        ],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": List[str],
        "State": ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerStateTypeDef,
        "Type": str,
        "VpcId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
        "CreatedAt": str,
        "PrincipalId": str,
        "PrincipalType": str,
        "PrincipalName": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsIamRoleTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsIamRoleTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "CreateDate": str,
        "RoleId": str,
        "RoleName": str,
        "MaxSessionDuration": int,
        "Path": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsKmsKeyTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsKmsKeyTypeDef",
    {
        "AWSAccountId": str,
        "CreationDate": float,
        "KeyId": str,
        "KeyManager": str,
        "KeyState": str,
        "Origin": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "SubnetIds": List[str], "VpcId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTypeDef",
    {
        "Code": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionCodeTypeDef,
        "CodeSha256": str,
        "DeadLetterConfig": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionDeadLetterConfigTypeDef,
        "Environment": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionEnvironmentTypeDef,
        "FunctionName": str,
        "Handler": str,
        "KmsKeyArn": str,
        "LastModified": str,
        "Layers": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionLayersTypeDef
        ],
        "MasterArn": str,
        "MemorySize": int,
        "RevisionId": str,
        "Role": str,
        "Runtime": str,
        "Timeout": int,
        "TracingConfig": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTracingConfigTypeDef,
        "VpcConfig": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionVpcConfigTypeDef,
        "Version": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef",
    {"Version": int, "CompatibleRuntimes": List[str], "CreatedDate": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceTypeDef",
    {
        "AssociatedRoles": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceAssociatedRolesTypeDef
        ],
        "CACertificateIdentifier": str,
        "DBClusterIdentifier": str,
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "DbInstancePort": int,
        "DbiResourceId": str,
        "DBName": str,
        "DeletionProtection": bool,
        "Endpoint": ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceEndpointTypeDef,
        "Engine": str,
        "EngineVersion": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "InstanceCreateTime": str,
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "StorageEncrypted": bool,
        "TdeCredentialArn": str,
        "VpcSecurityGroups": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceVpcSecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef",
    {"Endpoint": str, "Protocol": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicTypeDef",
    {
        "KmsMasterKeyId": str,
        "Subscription": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicSubscriptionTypeDef
        ],
        "TopicName": str,
        "Owner": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsSqsQueueTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsSqsQueueTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": int,
        "KmsMasterKeyId": str,
        "QueueName": str,
        "DeadLetterTargetArn": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef",
    {"Type": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef",
    {"Type": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesTypeDef",
    {
        "Action": ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesActionTypeDef,
        "ExcludedRules": List[
            ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesExcludedRulesTypeDef
        ],
        "OverrideAction": ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesOverrideActionTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclTypeDef",
    {
        "Name": str,
        "DefaultAction": str,
        "Rules": List[ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclRulesTypeDef],
        "WebAclId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsTypeDef",
    {
        "AwsCodeBuildProject": ClientGetFindingsResponseFindingsResourcesDetailsAwsCodeBuildProjectTypeDef,
        "AwsCloudFrontDistribution": ClientGetFindingsResponseFindingsResourcesDetailsAwsCloudFrontDistributionTypeDef,
        "AwsEc2Instance": ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsEc2NetworkInterface": ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2NetworkInterfaceTypeDef,
        "AwsEc2SecurityGroup": ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2SecurityGroupTypeDef,
        "AwsElbv2LoadBalancer": ClientGetFindingsResponseFindingsResourcesDetailsAwsElbv2LoadBalancerTypeDef,
        "AwsElasticsearchDomain": ClientGetFindingsResponseFindingsResourcesDetailsAwsElasticsearchDomainTypeDef,
        "AwsS3Bucket": ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "AwsIamRole": ClientGetFindingsResponseFindingsResourcesDetailsAwsIamRoleTypeDef,
        "AwsKmsKey": ClientGetFindingsResponseFindingsResourcesDetailsAwsKmsKeyTypeDef,
        "AwsLambdaFunction": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaFunctionTypeDef,
        "AwsLambdaLayerVersion": ClientGetFindingsResponseFindingsResourcesDetailsAwsLambdaLayerVersionTypeDef,
        "AwsRdsDbInstance": ClientGetFindingsResponseFindingsResourcesDetailsAwsRdsDbInstanceTypeDef,
        "AwsSnsTopic": ClientGetFindingsResponseFindingsResourcesDetailsAwsSnsTopicTypeDef,
        "AwsSqsQueue": ClientGetFindingsResponseFindingsResourcesDetailsAwsSqsQueueTypeDef,
        "AwsWafWebAcl": ClientGetFindingsResponseFindingsResourcesDetailsAwsWafWebAclTypeDef,
        "Container": ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ClientGetFindingsResponseFindingsResourcesDetailsTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsSeverityTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)

ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": ClientGetFindingsResponseFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": ClientGetFindingsResponseFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[ClientGetFindingsResponseFindingsMalwareTypeDef],
        "Network": ClientGetFindingsResponseFindingsNetworkTypeDef,
        "Process": ClientGetFindingsResponseFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[ClientGetFindingsResponseFindingsResourcesTypeDef],
        "Compliance": ClientGetFindingsResponseFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[ClientGetFindingsResponseFindingsRelatedFindingsTypeDef],
        "Note": ClientGetFindingsResponseFindingsNoteTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseTypeDef = TypedDict(
    "ClientGetFindingsResponseTypeDef",
    {"Findings": List[ClientGetFindingsResponseFindingsTypeDef], "NextToken": str},
    total=False,
)

ClientGetFindingsSortCriteriaTypeDef = TypedDict(
    "ClientGetFindingsSortCriteriaTypeDef",
    {"Field": str, "SortOrder": Literal["asc", "desc"]},
    total=False,
)

ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef = TypedDict(
    "ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef",
    {"GroupByAttributeValue": str, "Count": int},
    total=False,
)

ClientGetInsightResultsResponseInsightResultsTypeDef = TypedDict(
    "ClientGetInsightResultsResponseInsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List[ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef],
    },
    total=False,
)

ClientGetInsightResultsResponseTypeDef = TypedDict(
    "ClientGetInsightResultsResponseTypeDef",
    {"InsightResults": ClientGetInsightResultsResponseInsightResultsTypeDef},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersKeywordTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProductArnTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProductNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersTitleTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersTypeDef",
    {
        "ProductArn": List[ClientGetInsightsResponseInsightsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientGetInsightsResponseInsightsFiltersIdTypeDef],
        "GeneratorId": List[ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef],
        "Type": List[ClientGetInsightsResponseInsightsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[
            ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef
        ],
        "SeverityLabel": List[ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef],
        "Criticality": List[ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef],
        "Title": List[ClientGetInsightsResponseInsightsFiltersTitleTypeDef],
        "Description": List[ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef],
        "RecommendationText": List[
            ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef
        ],
        "SourceUrl": List[ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientGetInsightsResponseInsightsFiltersProductNameTypeDef],
        "CompanyName": List[ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[
            ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef
        ],
        "NetworkSourceMac": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef
        ],
        "NetworkDestinationIpV6": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef
        ],
        "NetworkDestinationPort": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef
        ],
        "NetworkDestinationDomain": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[
            ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef
        ],
        "ThreatIntelIndicatorType": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef
        ],
        "ResourceContainerImageId": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[
            ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef
        ],
        "ComplianceStatus": List[ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientGetInsightsResponseInsightsFiltersKeywordTypeDef],
    },
    total=False,
)

ClientGetInsightsResponseInsightsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": ClientGetInsightsResponseInsightsFiltersTypeDef,
        "GroupByAttribute": str,
    },
    total=False,
)

ClientGetInsightsResponseTypeDef = TypedDict(
    "ClientGetInsightsResponseTypeDef",
    {"Insights": List[ClientGetInsightsResponseInsightsTypeDef], "NextToken": str},
    total=False,
)

ClientGetInvitationsCountResponseTypeDef = TypedDict(
    "ClientGetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)

ClientGetMasterAccountResponseMasterTypeDef = TypedDict(
    "ClientGetMasterAccountResponseMasterTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

ClientGetMasterAccountResponseTypeDef = TypedDict(
    "ClientGetMasterAccountResponseTypeDef",
    {"Master": ClientGetMasterAccountResponseMasterTypeDef},
    total=False,
)

ClientGetMembersResponseMembersTypeDef = TypedDict(
    "ClientGetMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientGetMembersResponseTypeDef = TypedDict(
    "ClientGetMembersResponseTypeDef",
    {
        "Members": List[ClientGetMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)

ClientInviteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientInviteMembersResponseTypeDef = TypedDict(
    "ClientInviteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientInviteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ClientListEnabledProductsForImportResponseTypeDef",
    {"ProductSubscriptions": List[str], "NextToken": str},
    total=False,
)

ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "ClientListInvitationsResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

ClientListInvitationsResponseTypeDef = TypedDict(
    "ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)

ClientListMembersResponseMembersTypeDef = TypedDict(
    "ClientListMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListMembersResponseTypeDef = TypedDict(
    "ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateFindingsFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersCompanyNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersComplianceStatusTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersConfidenceTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateFindingsFiltersCreatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateFindingsFiltersCriticalityTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersDescriptionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersGeneratorIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersKeywordTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersLastObservedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersMalwareNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersMalwarePathTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersMalwareStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersMalwareTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersNoteTextTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersProcessNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProcessParentPidTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersProcessPathTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProcessPidTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersProductArnTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProductFieldsTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersProductNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRecommendationTextTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRecordStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourcePartitionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceRegionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceTagsTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersSeverityLabelTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersSeverityProductTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersSourceUrlTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersTitleTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateFindingsFiltersUpdatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersVerificationStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersWorkflowStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersTypeDef",
    {
        "ProductArn": List[ClientUpdateFindingsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientUpdateFindingsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientUpdateFindingsFiltersIdTypeDef],
        "GeneratorId": List[ClientUpdateFindingsFiltersGeneratorIdTypeDef],
        "Type": List[ClientUpdateFindingsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientUpdateFindingsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientUpdateFindingsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientUpdateFindingsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientUpdateFindingsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientUpdateFindingsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientUpdateFindingsFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientUpdateFindingsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientUpdateFindingsFiltersConfidenceTypeDef],
        "Criticality": List[ClientUpdateFindingsFiltersCriticalityTypeDef],
        "Title": List[ClientUpdateFindingsFiltersTitleTypeDef],
        "Description": List[ClientUpdateFindingsFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientUpdateFindingsFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientUpdateFindingsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientUpdateFindingsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientUpdateFindingsFiltersProductNameTypeDef],
        "CompanyName": List[ClientUpdateFindingsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientUpdateFindingsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientUpdateFindingsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientUpdateFindingsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientUpdateFindingsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientUpdateFindingsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientUpdateFindingsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientUpdateFindingsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientUpdateFindingsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[
            ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[ClientUpdateFindingsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientUpdateFindingsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientUpdateFindingsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientUpdateFindingsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientUpdateFindingsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientUpdateFindingsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientUpdateFindingsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientUpdateFindingsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientUpdateFindingsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientUpdateFindingsFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[
            ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientUpdateFindingsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientUpdateFindingsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientUpdateFindingsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientUpdateFindingsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientUpdateFindingsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientUpdateFindingsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientUpdateFindingsFiltersKeywordTypeDef],
    },
    total=False,
)

_RequiredClientUpdateFindingsNoteTypeDef = TypedDict(
    "_RequiredClientUpdateFindingsNoteTypeDef", {"Text": str}
)
_OptionalClientUpdateFindingsNoteTypeDef = TypedDict(
    "_OptionalClientUpdateFindingsNoteTypeDef", {"UpdatedBy": str}, total=False
)


class ClientUpdateFindingsNoteTypeDef(
    _RequiredClientUpdateFindingsNoteTypeDef, _OptionalClientUpdateFindingsNoteTypeDef
):
    pass


ClientUpdateInsightFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersCompanyNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersComplianceStatusTypeDef = TypedDict(
    "ClientUpdateInsightFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersConfidenceTypeDef = TypedDict(
    "ClientUpdateInsightFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateInsightFiltersCreatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateInsightFiltersCriticalityTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersDescriptionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersGeneratorIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersKeywordTypeDef = TypedDict(
    "ClientUpdateInsightFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersLastObservedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersMalwareNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersMalwarePathTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersMalwareStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersMalwareTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersNoteTextTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersProcessNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProcessParentPidTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersProcessPathTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProcessPidTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersProductArnTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProductFieldsTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersProductNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRecommendationTextTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRecordStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersResourceIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourcePartitionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceRegionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceTagsTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersResourceTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersSeverityLabelTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersSeverityProductTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersSourceUrlTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersTitleTypeDef = TypedDict(
    "ClientUpdateInsightFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateInsightFiltersUpdatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateInsightFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientUpdateInsightFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersVerificationStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersWorkflowStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersTypeDef = TypedDict(
    "ClientUpdateInsightFiltersTypeDef",
    {
        "ProductArn": List[ClientUpdateInsightFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientUpdateInsightFiltersAwsAccountIdTypeDef],
        "Id": List[ClientUpdateInsightFiltersIdTypeDef],
        "GeneratorId": List[ClientUpdateInsightFiltersGeneratorIdTypeDef],
        "Type": List[ClientUpdateInsightFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientUpdateInsightFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientUpdateInsightFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientUpdateInsightFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientUpdateInsightFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientUpdateInsightFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientUpdateInsightFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientUpdateInsightFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientUpdateInsightFiltersConfidenceTypeDef],
        "Criticality": List[ClientUpdateInsightFiltersCriticalityTypeDef],
        "Title": List[ClientUpdateInsightFiltersTitleTypeDef],
        "Description": List[ClientUpdateInsightFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientUpdateInsightFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientUpdateInsightFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientUpdateInsightFiltersProductFieldsTypeDef],
        "ProductName": List[ClientUpdateInsightFiltersProductNameTypeDef],
        "CompanyName": List[ClientUpdateInsightFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientUpdateInsightFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientUpdateInsightFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientUpdateInsightFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientUpdateInsightFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientUpdateInsightFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientUpdateInsightFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientUpdateInsightFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientUpdateInsightFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientUpdateInsightFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientUpdateInsightFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientUpdateInsightFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientUpdateInsightFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientUpdateInsightFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientUpdateInsightFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientUpdateInsightFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientUpdateInsightFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientUpdateInsightFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientUpdateInsightFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientUpdateInsightFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientUpdateInsightFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientUpdateInsightFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientUpdateInsightFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientUpdateInsightFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientUpdateInsightFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientUpdateInsightFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientUpdateInsightFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientUpdateInsightFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientUpdateInsightFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientUpdateInsightFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientUpdateInsightFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientUpdateInsightFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientUpdateInsightFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientUpdateInsightFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientUpdateInsightFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientUpdateInsightFiltersKeywordTypeDef],
    },
    total=False,
)

StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
)

GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {"StandardsSubscriptions": List[StandardsSubscriptionTypeDef], "NextToken": str},
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"],
        "RelatedRequirements": List[str],
    },
    total=False,
)

_RequiredMalwareTypeDef = TypedDict("_RequiredMalwareTypeDef", {"Name": str})
_OptionalMalwareTypeDef = TypedDict(
    "_OptionalMalwareTypeDef",
    {
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)


class MalwareTypeDef(_RequiredMalwareTypeDef, _OptionalMalwareTypeDef):
    pass


NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

NoteTypeDef = TypedDict("NoteTypeDef", {"Text": str, "UpdatedBy": str, "UpdatedAt": str})

ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

RelatedFindingTypeDef = TypedDict("RelatedFindingTypeDef", {"ProductArn": str, "Id": str})

RecommendationTypeDef = TypedDict("RecommendationTypeDef", {"Text": str, "Url": str}, total=False)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef", {"Recommendation": RecommendationTypeDef}, total=False
)

AwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingTypeDef",
    {"Bucket": str, "Enabled": bool, "IncludeCookies": bool, "Prefix": str},
    total=False,
)

AwsCloudFrontDistributionOriginItemTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemTypeDef",
    {"DomainName": str, "Id": str, "OriginPath": str},
    total=False,
)

AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {"Items": List[AwsCloudFrontDistributionOriginItemTypeDef]},
    total=False,
)

AwsCloudFrontDistributionDetailsTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsTypeDef",
    {
        "DomainName": str,
        "ETag": str,
        "LastModifiedTime": str,
        "Logging": AwsCloudFrontDistributionLoggingTypeDef,
        "Origins": AwsCloudFrontDistributionOriginsTypeDef,
        "Status": str,
        "WebAclId": str,
    },
    total=False,
)

AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {"Credential": str, "CredentialProvider": str},
    total=False,
)

AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": str,
        "ImagePullCredentialsType": str,
        "RegistryCredential": AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef,
        "Type": str,
    },
    total=False,
)

AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {"Type": str, "Location": str, "GitCloneDepth": int, "InsecureSsl": bool},
    total=False,
)

AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {"VpcId": str, "Subnets": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

AwsCodeBuildProjectDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsTypeDef",
    {
        "EncryptionKey": str,
        "Environment": AwsCodeBuildProjectEnvironmentTypeDef,
        "Name": str,
        "Source": AwsCodeBuildProjectSourceTypeDef,
        "ServiceRole": str,
        "VpcConfig": AwsCodeBuildProjectVpcConfigTypeDef,
    },
    total=False,
)

AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": str,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef", {"GroupName": str, "GroupId": str}, total=False
)

AwsEc2NetworkInterfaceDetailsTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    {
        "Attachment": AwsEc2NetworkInterfaceAttachmentTypeDef,
        "NetworkInterfaceId": str,
        "SecurityGroups": List[AwsEc2NetworkInterfaceSecurityGroupTypeDef],
        "SourceDestCheck": bool,
    },
    total=False,
)

AwsEc2SecurityGroupIpRangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeTypeDef", {"CidrIp": str}, total=False
)

AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef", {"CidrIpv6": str}, total=False
)

AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef", {"PrefixListId": str}, total=False
)

AwsEc2SecurityGroupUserIdGroupPairTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

AwsEc2SecurityGroupIpPermissionTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List[AwsEc2SecurityGroupUserIdGroupPairTypeDef],
        "IpRanges": List[AwsEc2SecurityGroupIpRangeTypeDef],
        "Ipv6Ranges": List[AwsEc2SecurityGroupIpv6RangeTypeDef],
        "PrefixListIds": List[AwsEc2SecurityGroupPrefixListIdTypeDef],
    },
    total=False,
)

AwsEc2SecurityGroupDetailsTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
        "OwnerId": str,
        "VpcId": str,
        "IpPermissions": List[AwsEc2SecurityGroupIpPermissionTypeDef],
        "IpPermissionsEgress": List[AwsEc2SecurityGroupIpPermissionTypeDef],
    },
    total=False,
)

AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)

AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef", {"Enabled": bool}, total=False
)

AwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VPCId": str,
    },
    total=False,
)

AwsElasticsearchDomainDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsTypeDef",
    {
        "AccessPolicies": str,
        "DomainEndpointOptions": AwsElasticsearchDomainDomainEndpointOptionsTypeDef,
        "DomainId": str,
        "DomainName": str,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "ElasticsearchVersion": str,
        "EncryptionAtRestOptions": AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef,
        "VPCOptions": AwsElasticsearchDomainVPCOptionsTypeDef,
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef", {"ZoneName": str, "SubnetId": str}, total=False
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef", {"Code": str, "Reason": str}, total=False
)

AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": List[str],
        "State": LoadBalancerStateTypeDef,
        "Type": str,
        "VpcId": str,
    },
    total=False,
)

AwsIamAccessKeyDetailsTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsTypeDef",
    {
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
        "CreatedAt": str,
        "PrincipalId": str,
        "PrincipalType": str,
        "PrincipalName": str,
    },
    total=False,
)

AwsIamRoleDetailsTypeDef = TypedDict(
    "AwsIamRoleDetailsTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "CreateDate": str,
        "RoleId": str,
        "RoleName": str,
        "MaxSessionDuration": int,
        "Path": str,
    },
    total=False,
)

AwsKmsKeyDetailsTypeDef = TypedDict(
    "AwsKmsKeyDetailsTypeDef",
    {
        "AWSAccountId": str,
        "CreationDate": float,
        "KeyId": str,
        "KeyManager": str,
        "KeyState": str,
        "Origin": str,
    },
    total=False,
)

AwsLambdaFunctionCodeTypeDef = TypedDict(
    "AwsLambdaFunctionCodeTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": str},
    total=False,
)

AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

AwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorTypeDef", {"ErrorCode": str, "Message": str}, total=False
)

AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": AwsLambdaFunctionEnvironmentErrorTypeDef},
    total=False,
)

AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef", {"Arn": str, "CodeSize": int}, total=False
)

AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef", {"Mode": str}, total=False
)

AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "SubnetIds": List[str], "VpcId": str},
    total=False,
)

AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "Code": AwsLambdaFunctionCodeTypeDef,
        "CodeSha256": str,
        "DeadLetterConfig": AwsLambdaFunctionDeadLetterConfigTypeDef,
        "Environment": AwsLambdaFunctionEnvironmentTypeDef,
        "FunctionName": str,
        "Handler": str,
        "KmsKeyArn": str,
        "LastModified": str,
        "Layers": List[AwsLambdaFunctionLayerTypeDef],
        "MasterArn": str,
        "MemorySize": int,
        "RevisionId": str,
        "Role": str,
        "Runtime": str,
        "Timeout": int,
        "TracingConfig": AwsLambdaFunctionTracingConfigTypeDef,
        "VpcConfig": AwsLambdaFunctionVpcConfigTypeDef,
        "Version": str,
    },
    total=False,
)

AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {"Version": int, "CompatibleRuntimes": List[str], "CreatedDate": str},
    total=False,
)

AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

AwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

AwsRdsDbInstanceDetailsTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsTypeDef",
    {
        "AssociatedRoles": List[AwsRdsDbInstanceAssociatedRoleTypeDef],
        "CACertificateIdentifier": str,
        "DBClusterIdentifier": str,
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "DbInstancePort": int,
        "DbiResourceId": str,
        "DBName": str,
        "DeletionProtection": bool,
        "Endpoint": AwsRdsDbInstanceEndpointTypeDef,
        "Engine": str,
        "EngineVersion": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "InstanceCreateTime": str,
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "StorageEncrypted": bool,
        "TdeCredentialArn": str,
        "VpcSecurityGroups": List[AwsRdsDbInstanceVpcSecurityGroupTypeDef],
    },
    total=False,
)

AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef", {"OwnerId": str, "OwnerName": str}, total=False
)

AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef", {"Endpoint": str, "Protocol": str}, total=False
)

AwsSnsTopicDetailsTypeDef = TypedDict(
    "AwsSnsTopicDetailsTypeDef",
    {
        "KmsMasterKeyId": str,
        "Subscription": List[AwsSnsTopicSubscriptionTypeDef],
        "TopicName": str,
        "Owner": str,
    },
    total=False,
)

AwsSqsQueueDetailsTypeDef = TypedDict(
    "AwsSqsQueueDetailsTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": int,
        "KmsMasterKeyId": str,
        "QueueName": str,
        "DeadLetterTargetArn": str,
    },
    total=False,
)

WafActionTypeDef = TypedDict("WafActionTypeDef", {"Type": str}, total=False)

WafExcludedRuleTypeDef = TypedDict("WafExcludedRuleTypeDef", {"RuleId": str}, total=False)

WafOverrideActionTypeDef = TypedDict("WafOverrideActionTypeDef", {"Type": str}, total=False)

AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": WafActionTypeDef,
        "ExcludedRules": List[WafExcludedRuleTypeDef],
        "OverrideAction": WafOverrideActionTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {"Name": str, "DefaultAction": str, "Rules": List[AwsWafWebAclRuleTypeDef], "WebAclId": str},
    total=False,
)

ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsCodeBuildProject": AwsCodeBuildProjectDetailsTypeDef,
        "AwsCloudFrontDistribution": AwsCloudFrontDistributionDetailsTypeDef,
        "AwsEc2Instance": AwsEc2InstanceDetailsTypeDef,
        "AwsEc2NetworkInterface": AwsEc2NetworkInterfaceDetailsTypeDef,
        "AwsEc2SecurityGroup": AwsEc2SecurityGroupDetailsTypeDef,
        "AwsElbv2LoadBalancer": AwsElbv2LoadBalancerDetailsTypeDef,
        "AwsElasticsearchDomain": AwsElasticsearchDomainDetailsTypeDef,
        "AwsS3Bucket": AwsS3BucketDetailsTypeDef,
        "AwsIamAccessKey": AwsIamAccessKeyDetailsTypeDef,
        "AwsIamRole": AwsIamRoleDetailsTypeDef,
        "AwsKmsKey": AwsKmsKeyDetailsTypeDef,
        "AwsLambdaFunction": AwsLambdaFunctionDetailsTypeDef,
        "AwsLambdaLayerVersion": AwsLambdaLayerVersionDetailsTypeDef,
        "AwsRdsDbInstance": AwsRdsDbInstanceDetailsTypeDef,
        "AwsSnsTopic": AwsSnsTopicDetailsTypeDef,
        "AwsSqsQueue": AwsSqsQueueDetailsTypeDef,
        "AwsWafWebAcl": AwsWafWebAclDetailsTypeDef,
        "Container": ContainerDetailsTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)

_RequiredResourceTypeDef = TypedDict("_RequiredResourceTypeDef", {"Type": str, "Id": str})
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ResourceDetailsTypeDef,
    },
    total=False,
)


class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass


_RequiredSeverityTypeDef = TypedDict("_RequiredSeverityTypeDef", {"Normalized": int})
_OptionalSeverityTypeDef = TypedDict("_OptionalSeverityTypeDef", {"Product": float}, total=False)


class SeverityTypeDef(_RequiredSeverityTypeDef, _OptionalSeverityTypeDef):
    pass


ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

_RequiredAwsSecurityFindingTypeDef = TypedDict(
    "_RequiredAwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": SeverityTypeDef,
        "Title": str,
        "Description": str,
        "Resources": List[ResourceTypeDef],
    },
)
_OptionalAwsSecurityFindingTypeDef = TypedDict(
    "_OptionalAwsSecurityFindingTypeDef",
    {
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "Confidence": int,
        "Criticality": int,
        "Remediation": RemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[MalwareTypeDef],
        "Network": NetworkTypeDef,
        "Process": ProcessDetailsTypeDef,
        "ThreatIntelIndicators": List[ThreatIntelIndicatorTypeDef],
        "Compliance": ComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[RelatedFindingTypeDef],
        "Note": NoteTypeDef,
    },
    total=False,
)


class AwsSecurityFindingTypeDef(
    _RequiredAwsSecurityFindingTypeDef, _OptionalAwsSecurityFindingTypeDef
):
    pass


_RequiredGetFindingsResponseTypeDef = TypedDict(
    "_RequiredGetFindingsResponseTypeDef", {"Findings": List[AwsSecurityFindingTypeDef]}
)
_OptionalGetFindingsResponseTypeDef = TypedDict(
    "_OptionalGetFindingsResponseTypeDef", {"NextToken": str}, total=False
)


class GetFindingsResponseTypeDef(
    _RequiredGetFindingsResponseTypeDef, _OptionalGetFindingsResponseTypeDef
):
    pass


InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "GroupByAttribute": str,
    },
)

_RequiredGetInsightsResponseTypeDef = TypedDict(
    "_RequiredGetInsightsResponseTypeDef", {"Insights": List[InsightTypeDef]}
)
_OptionalGetInsightsResponseTypeDef = TypedDict(
    "_OptionalGetInsightsResponseTypeDef", {"NextToken": str}, total=False
)


class GetInsightsResponseTypeDef(
    _RequiredGetInsightsResponseTypeDef, _OptionalGetInsightsResponseTypeDef
):
    pass


ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {"ProductSubscriptions": List[str], "NextToken": str},
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {"Invitations": List[InvitationTypeDef], "NextToken": str},
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef", {"Members": List[MemberTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef", {"Field": str, "SortOrder": Literal["asc", "desc"]}, total=False
)
