"""
Main interface for ssm service type definitions.

Usage::

    from mypy_boto3.ssm.type_defs import AssociationExecutionFilterTypeDef

    data: AssociationExecutionFilterTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationFilterTypeDef",
    "AutomationExecutionFilterTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientCancelMaintenanceWindowExecutionResponseTypeDef",
    "ClientCreateActivationResponseTypeDef",
    "ClientCreateActivationTagsTypeDef",
    "ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationBatchEntriesOutputLocationTypeDef",
    "ClientCreateAssociationBatchEntriesTargetsTypeDef",
    "ClientCreateAssociationBatchEntriesTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef",
    "ClientCreateAssociationBatchResponseFailedEntryTypeDef",
    "ClientCreateAssociationBatchResponseFailedTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef",
    "ClientCreateAssociationBatchResponseSuccessfulTypeDef",
    "ClientCreateAssociationBatchResponseTypeDef",
    "ClientCreateAssociationOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationOutputLocationTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef",
    "ClientCreateAssociationResponseAssociationDescriptionTypeDef",
    "ClientCreateAssociationResponseTypeDef",
    "ClientCreateAssociationTargetsTypeDef",
    "ClientCreateDocumentAttachmentsTypeDef",
    "ClientCreateDocumentRequiresTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef",
    "ClientCreateDocumentResponseDocumentDescriptionTypeDef",
    "ClientCreateDocumentResponseTypeDef",
    "ClientCreateDocumentTagsTypeDef",
    "ClientCreateMaintenanceWindowResponseTypeDef",
    "ClientCreateMaintenanceWindowTagsTypeDef",
    "ClientCreateOpsItemNotificationsTypeDef",
    "ClientCreateOpsItemOperationalDataTypeDef",
    "ClientCreateOpsItemRelatedOpsItemsTypeDef",
    "ClientCreateOpsItemResponseTypeDef",
    "ClientCreateOpsItemTagsTypeDef",
    "ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    "ClientCreatePatchBaselineApprovalRulesTypeDef",
    "ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    "ClientCreatePatchBaselineGlobalFiltersTypeDef",
    "ClientCreatePatchBaselineResponseTypeDef",
    "ClientCreatePatchBaselineSourcesTypeDef",
    "ClientCreatePatchBaselineTagsTypeDef",
    "ClientCreateResourceDataSyncS3DestinationTypeDef",
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    "ClientCreateResourceDataSyncSyncSourceTypeDef",
    "ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef",
    "ClientDeleteInventoryResponseDeletionSummaryTypeDef",
    "ClientDeleteInventoryResponseTypeDef",
    "ClientDeleteMaintenanceWindowResponseTypeDef",
    "ClientDeleteParametersResponseTypeDef",
    "ClientDeletePatchBaselineResponseTypeDef",
    "ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef",
    "ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef",
    "ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef",
    "ClientDescribeActivationsFiltersTypeDef",
    "ClientDescribeActivationsResponseActivationListTagsTypeDef",
    "ClientDescribeActivationsResponseActivationListTypeDef",
    "ClientDescribeActivationsResponseTypeDef",
    "ClientDescribeAssociationExecutionTargetsFiltersTypeDef",
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef",
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef",
    "ClientDescribeAssociationExecutionTargetsResponseTypeDef",
    "ClientDescribeAssociationExecutionsFiltersTypeDef",
    "ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef",
    "ClientDescribeAssociationExecutionsResponseTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef",
    "ClientDescribeAssociationResponseAssociationDescriptionTypeDef",
    "ClientDescribeAssociationResponseTypeDef",
    "ClientDescribeAutomationExecutionsFiltersTypeDef",
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef",
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef",
    "ClientDescribeAutomationExecutionsResponseTypeDef",
    "ClientDescribeAutomationStepExecutionsFiltersTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef",
    "ClientDescribeAutomationStepExecutionsResponseTypeDef",
    "ClientDescribeAvailablePatchesFiltersTypeDef",
    "ClientDescribeAvailablePatchesResponsePatchesTypeDef",
    "ClientDescribeAvailablePatchesResponseTypeDef",
    "ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef",
    "ClientDescribeDocumentPermissionResponseTypeDef",
    "ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef",
    "ClientDescribeDocumentResponseDocumentParametersTypeDef",
    "ClientDescribeDocumentResponseDocumentRequiresTypeDef",
    "ClientDescribeDocumentResponseDocumentTagsTypeDef",
    "ClientDescribeDocumentResponseDocumentTypeDef",
    "ClientDescribeDocumentResponseTypeDef",
    "ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef",
    "ClientDescribeEffectiveInstanceAssociationsResponseTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef",
    "ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef",
    "ClientDescribeInstanceAssociationsStatusResponseTypeDef",
    "ClientDescribeInstanceInformationFiltersTypeDef",
    "ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    "ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef",
    "ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef",
    "ClientDescribeInstanceInformationResponseTypeDef",
    "ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef",
    "ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef",
    "ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef",
    "ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef",
    "ClientDescribeInstancePatchStatesResponseTypeDef",
    "ClientDescribeInstancePatchesFiltersTypeDef",
    "ClientDescribeInstancePatchesResponsePatchesTypeDef",
    "ClientDescribeInstancePatchesResponseTypeDef",
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef",
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef",
    "ClientDescribeInventoryDeletionsResponseTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef",
    "ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef",
    "ClientDescribeMaintenanceWindowExecutionsResponseTypeDef",
    "ClientDescribeMaintenanceWindowScheduleFiltersTypeDef",
    "ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef",
    "ClientDescribeMaintenanceWindowScheduleResponseTypeDef",
    "ClientDescribeMaintenanceWindowScheduleTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTargetsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTargetsResponseTypeDef",
    "ClientDescribeMaintenanceWindowTasksFiltersTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef",
    "ClientDescribeMaintenanceWindowTasksResponseTypeDef",
    "ClientDescribeMaintenanceWindowsFiltersTypeDef",
    "ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowsForTargetResponseTypeDef",
    "ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef",
    "ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef",
    "ClientDescribeMaintenanceWindowsResponseTypeDef",
    "ClientDescribeOpsItemsOpsItemFiltersTypeDef",
    "ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef",
    "ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef",
    "ClientDescribeOpsItemsResponseTypeDef",
    "ClientDescribeParametersFiltersTypeDef",
    "ClientDescribeParametersParameterFiltersTypeDef",
    "ClientDescribeParametersResponseParametersPoliciesTypeDef",
    "ClientDescribeParametersResponseParametersTypeDef",
    "ClientDescribeParametersResponseTypeDef",
    "ClientDescribePatchBaselinesFiltersTypeDef",
    "ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef",
    "ClientDescribePatchBaselinesResponseTypeDef",
    "ClientDescribePatchGroupStateResponseTypeDef",
    "ClientDescribePatchGroupsFiltersTypeDef",
    "ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef",
    "ClientDescribePatchGroupsResponseMappingsTypeDef",
    "ClientDescribePatchGroupsResponseTypeDef",
    "ClientDescribePatchPropertiesResponseTypeDef",
    "ClientDescribeSessionsFiltersTypeDef",
    "ClientDescribeSessionsResponseSessionsOutputUrlTypeDef",
    "ClientDescribeSessionsResponseSessionsTypeDef",
    "ClientDescribeSessionsResponseTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef",
    "ClientGetAutomationExecutionResponseAutomationExecutionTypeDef",
    "ClientGetAutomationExecutionResponseTypeDef",
    "ClientGetCalendarStateResponseTypeDef",
    "ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef",
    "ClientGetCommandInvocationResponseTypeDef",
    "ClientGetConnectionStatusResponseTypeDef",
    "ClientGetDefaultPatchBaselineResponseTypeDef",
    "ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef",
    "ClientGetDocumentResponseAttachmentsContentTypeDef",
    "ClientGetDocumentResponseRequiresTypeDef",
    "ClientGetDocumentResponseTypeDef",
    "ClientGetInventoryAggregatorsGroupsFiltersTypeDef",
    "ClientGetInventoryAggregatorsGroupsTypeDef",
    "ClientGetInventoryAggregatorsTypeDef",
    "ClientGetInventoryFiltersTypeDef",
    "ClientGetInventoryResponseEntitiesDataTypeDef",
    "ClientGetInventoryResponseEntitiesTypeDef",
    "ClientGetInventoryResponseTypeDef",
    "ClientGetInventoryResultAttributesTypeDef",
    "ClientGetInventorySchemaResponseSchemasAttributesTypeDef",
    "ClientGetInventorySchemaResponseSchemasTypeDef",
    "ClientGetInventorySchemaResponseTypeDef",
    "ClientGetMaintenanceWindowExecutionResponseTypeDef",
    "ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef",
    "ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef",
    "ClientGetMaintenanceWindowExecutionTaskResponseTypeDef",
    "ClientGetMaintenanceWindowResponseTypeDef",
    "ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTargetsTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef",
    "ClientGetMaintenanceWindowTaskResponseTypeDef",
    "ClientGetOpsItemResponseOpsItemNotificationsTypeDef",
    "ClientGetOpsItemResponseOpsItemOperationalDataTypeDef",
    "ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef",
    "ClientGetOpsItemResponseOpsItemTypeDef",
    "ClientGetOpsItemResponseTypeDef",
    "ClientGetOpsSummaryAggregatorsFiltersTypeDef",
    "ClientGetOpsSummaryAggregatorsTypeDef",
    "ClientGetOpsSummaryFiltersTypeDef",
    "ClientGetOpsSummaryResponseEntitiesDataTypeDef",
    "ClientGetOpsSummaryResponseEntitiesTypeDef",
    "ClientGetOpsSummaryResponseTypeDef",
    "ClientGetOpsSummaryResultAttributesTypeDef",
    "ClientGetParameterHistoryResponseParametersPoliciesTypeDef",
    "ClientGetParameterHistoryResponseParametersTypeDef",
    "ClientGetParameterHistoryResponseTypeDef",
    "ClientGetParameterResponseParameterTypeDef",
    "ClientGetParameterResponseTypeDef",
    "ClientGetParametersByPathParameterFiltersTypeDef",
    "ClientGetParametersByPathResponseParametersTypeDef",
    "ClientGetParametersByPathResponseTypeDef",
    "ClientGetParametersResponseParametersTypeDef",
    "ClientGetParametersResponseTypeDef",
    "ClientGetPatchBaselineForPatchGroupResponseTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    "ClientGetPatchBaselineResponseApprovalRulesTypeDef",
    "ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    "ClientGetPatchBaselineResponseGlobalFiltersTypeDef",
    "ClientGetPatchBaselineResponseSourcesTypeDef",
    "ClientGetPatchBaselineResponseTypeDef",
    "ClientGetServiceSettingResponseServiceSettingTypeDef",
    "ClientGetServiceSettingResponseTypeDef",
    "ClientLabelParameterVersionResponseTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef",
    "ClientListAssociationVersionsResponseAssociationVersionsTypeDef",
    "ClientListAssociationVersionsResponseTypeDef",
    "ClientListAssociationsAssociationFilterListTypeDef",
    "ClientListAssociationsResponseAssociationsOverviewTypeDef",
    "ClientListAssociationsResponseAssociationsTargetsTypeDef",
    "ClientListAssociationsResponseAssociationsTypeDef",
    "ClientListAssociationsResponseTypeDef",
    "ClientListCommandInvocationsFiltersTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef",
    "ClientListCommandInvocationsResponseCommandInvocationsTypeDef",
    "ClientListCommandInvocationsResponseTypeDef",
    "ClientListCommandsFiltersTypeDef",
    "ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef",
    "ClientListCommandsResponseCommandsNotificationConfigTypeDef",
    "ClientListCommandsResponseCommandsTargetsTypeDef",
    "ClientListCommandsResponseCommandsTypeDef",
    "ClientListCommandsResponseTypeDef",
    "ClientListComplianceItemsFiltersTypeDef",
    "ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef",
    "ClientListComplianceItemsResponseComplianceItemsTypeDef",
    "ClientListComplianceItemsResponseTypeDef",
    "ClientListComplianceSummariesFiltersTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    "ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef",
    "ClientListComplianceSummariesResponseTypeDef",
    "ClientListDocumentVersionsResponseDocumentVersionsTypeDef",
    "ClientListDocumentVersionsResponseTypeDef",
    "ClientListDocumentsDocumentFilterListTypeDef",
    "ClientListDocumentsFiltersTypeDef",
    "ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef",
    "ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef",
    "ClientListDocumentsResponseDocumentIdentifiersTypeDef",
    "ClientListDocumentsResponseTypeDef",
    "ClientListInventoryEntriesFiltersTypeDef",
    "ClientListInventoryEntriesResponseTypeDef",
    "ClientListResourceComplianceSummariesFiltersTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef",
    "ClientListResourceComplianceSummariesResponseTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef",
    "ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef",
    "ClientListResourceDataSyncResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutComplianceItemsExecutionSummaryTypeDef",
    "ClientPutComplianceItemsItemsTypeDef",
    "ClientPutInventoryItemsTypeDef",
    "ClientPutInventoryResponseTypeDef",
    "ClientPutParameterResponseTypeDef",
    "ClientPutParameterTagsTypeDef",
    "ClientRegisterDefaultPatchBaselineResponseTypeDef",
    "ClientRegisterPatchBaselineForPatchGroupResponseTypeDef",
    "ClientRegisterTargetWithMaintenanceWindowResponseTypeDef",
    "ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowResponseTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef",
    "ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef",
    "ClientResetServiceSettingResponseServiceSettingTypeDef",
    "ClientResetServiceSettingResponseTypeDef",
    "ClientResumeSessionResponseTypeDef",
    "ClientSendCommandCloudWatchOutputConfigTypeDef",
    "ClientSendCommandNotificationConfigTypeDef",
    "ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef",
    "ClientSendCommandResponseCommandNotificationConfigTypeDef",
    "ClientSendCommandResponseCommandTargetsTypeDef",
    "ClientSendCommandResponseCommandTypeDef",
    "ClientSendCommandResponseTypeDef",
    "ClientSendCommandTargetsTypeDef",
    "ClientStartAutomationExecutionResponseTypeDef",
    "ClientStartAutomationExecutionTagsTypeDef",
    "ClientStartAutomationExecutionTargetLocationsTypeDef",
    "ClientStartAutomationExecutionTargetsTypeDef",
    "ClientStartSessionResponseTypeDef",
    "ClientTerminateSessionResponseTypeDef",
    "ClientUpdateAssociationOutputLocationS3LocationTypeDef",
    "ClientUpdateAssociationOutputLocationTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef",
    "ClientUpdateAssociationResponseAssociationDescriptionTypeDef",
    "ClientUpdateAssociationResponseTypeDef",
    "ClientUpdateAssociationStatusAssociationStatusTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef",
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef",
    "ClientUpdateAssociationStatusResponseTypeDef",
    "ClientUpdateAssociationTargetsTypeDef",
    "ClientUpdateDocumentAttachmentsTypeDef",
    "ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef",
    "ClientUpdateDocumentDefaultVersionResponseTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef",
    "ClientUpdateDocumentResponseDocumentDescriptionTypeDef",
    "ClientUpdateDocumentResponseTypeDef",
    "ClientUpdateMaintenanceWindowResponseTypeDef",
    "ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTargetResponseTypeDef",
    "ClientUpdateMaintenanceWindowTargetTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef",
    "ClientUpdateMaintenanceWindowTaskResponseTypeDef",
    "ClientUpdateMaintenanceWindowTaskTargetsTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef",
    "ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef",
    "ClientUpdateOpsItemNotificationsTypeDef",
    "ClientUpdateOpsItemOperationalDataTypeDef",
    "ClientUpdateOpsItemRelatedOpsItemsTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    "ClientUpdatePatchBaselineApprovalRulesTypeDef",
    "ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineGlobalFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    "ClientUpdatePatchBaselineResponseApprovalRulesTypeDef",
    "ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef",
    "ClientUpdatePatchBaselineResponseSourcesTypeDef",
    "ClientUpdatePatchBaselineResponseTypeDef",
    "ClientUpdatePatchBaselineSourcesTypeDef",
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    "ClientUpdateResourceDataSyncSyncSourceTypeDef",
    "CommandFilterTypeDef",
    "ComplianceStringFilterTypeDef",
    "DescribeActivationsFilterTypeDef",
    "TagTypeDef",
    "ActivationTypeDef",
    "DescribeActivationsResultTypeDef",
    "OutputSourceTypeDef",
    "AssociationExecutionTargetTypeDef",
    "DescribeAssociationExecutionTargetsResultTypeDef",
    "AssociationExecutionTypeDef",
    "DescribeAssociationExecutionsResultTypeDef",
    "ResolvedTargetsTypeDef",
    "TargetTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "DescribeAutomationExecutionsResultTypeDef",
    "FailureDetailsTypeDef",
    "TargetLocationTypeDef",
    "StepExecutionTypeDef",
    "DescribeAutomationStepExecutionsResultTypeDef",
    "PatchTypeDef",
    "DescribeAvailablePatchesResultTypeDef",
    "InstanceAssociationTypeDef",
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    "PatchStatusTypeDef",
    "EffectivePatchTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    "S3OutputUrlTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "DescribeInstanceAssociationsStatusResultTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceInformationTypeDef",
    "DescribeInstanceInformationResultTypeDef",
    "InstancePatchStateTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    "DescribeInstancePatchStatesResultTypeDef",
    "PatchComplianceDataTypeDef",
    "DescribeInstancePatchesResultTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "DescribeInventoryDeletionsResultTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "DescribeMaintenanceWindowTasksResultTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "DescribeMaintenanceWindowsResultTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "DescribeParametersResultTypeDef",
    "PatchBaselineIdentityTypeDef",
    "DescribePatchBaselinesResultTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "DescribePatchGroupsResultTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "DescribeSessionsResponseTypeDef",
    "DocumentFilterTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "InventoryResultItemTypeDef",
    "InventoryResultEntityTypeDef",
    "GetInventoryResultTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "GetInventorySchemaResultTypeDef",
    "ParameterHistoryTypeDef",
    "GetParameterHistoryResultTypeDef",
    "ParameterTypeDef",
    "GetParametersByPathResultTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryAggregatorTypeDef",
    "S3OutputLocationTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "AssociationVersionInfoTypeDef",
    "ListAssociationVersionsResultTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationTypeDef",
    "ListAssociationsResultTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandPluginTypeDef",
    "NotificationConfigTypeDef",
    "CommandInvocationTypeDef",
    "ListCommandInvocationsResultTypeDef",
    "CommandTypeDef",
    "ListCommandsResultTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemTypeDef",
    "ListComplianceItemsResultTypeDef",
    "SeveritySummaryTypeDef",
    "CompliantSummaryTypeDef",
    "NonCompliantSummaryTypeDef",
    "ComplianceSummaryItemTypeDef",
    "ListComplianceSummariesResultTypeDef",
    "DocumentVersionInfoTypeDef",
    "ListDocumentVersionsResultTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentIdentifierTypeDef",
    "ListDocumentsResultTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ListResourceComplianceSummariesResultTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ListResourceDataSyncResultTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterStringFilterTypeDef",
    "ParametersFilterTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "ResultAttributeTypeDef",
    "SessionFilterTypeDef",
    "StepExecutionFilterTypeDef",
)

AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {
        "Key": Literal["ExecutionId", "Status", "CreatedTime"],
        "Value": str,
        "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"],
    },
)

AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"], "Value": str},
)

AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
        ],
        "value": str,
    },
)

AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
            "TagKey",
        ],
        "Values": List[str],
    },
)

ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCancelMaintenanceWindowExecutionResponseTypeDef = TypedDict(
    "ClientCancelMaintenanceWindowExecutionResponseTypeDef", {"WindowExecutionId": str}, total=False
)

ClientCreateActivationResponseTypeDef = TypedDict(
    "ClientCreateActivationResponseTypeDef",
    {"ActivationId": str, "ActivationCode": str},
    total=False,
)

ClientCreateActivationTagsTypeDef = TypedDict(
    "ClientCreateActivationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationBatchEntriesOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchEntriesOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationBatchEntriesTargetsTypeDef = TypedDict(
    "ClientCreateAssociationBatchEntriesTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

_RequiredClientCreateAssociationBatchEntriesTypeDef = TypedDict(
    "_RequiredClientCreateAssociationBatchEntriesTypeDef", {"Name": str}
)
_OptionalClientCreateAssociationBatchEntriesTypeDef = TypedDict(
    "_OptionalClientCreateAssociationBatchEntriesTypeDef",
    {
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List[ClientCreateAssociationBatchEntriesTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchEntriesOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientCreateAssociationBatchEntriesTypeDef(
    _RequiredClientCreateAssociationBatchEntriesTypeDef,
    _OptionalClientCreateAssociationBatchEntriesTypeDef,
):
    pass


ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateAssociationBatchResponseFailedEntryTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List[ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientCreateAssociationBatchResponseFailedTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedTypeDef",
    {
        "Entry": ClientCreateAssociationBatchResponseFailedEntryTypeDef,
        "Message": str,
        "Fault": Literal["Client", "Server", "Unknown"],
    },
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef,
        "Overview": ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientCreateAssociationBatchResponseTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseTypeDef",
    {
        "Successful": List[ClientCreateAssociationBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientCreateAssociationBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientCreateAssociationOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientCreateAssociationResponseTypeDef = TypedDict(
    "ClientCreateAssociationResponseTypeDef",
    {"AssociationDescription": ClientCreateAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)

ClientCreateAssociationTargetsTypeDef = TypedDict(
    "ClientCreateAssociationTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientCreateDocumentAttachmentsTypeDef = TypedDict(
    "ClientCreateDocumentAttachmentsTypeDef",
    {
        "Key": Literal["SourceUrl", "S3FileUrl", "AttachmentReference"],
        "Values": List[str],
        "Name": str,
    },
    total=False,
)

_RequiredClientCreateDocumentRequiresTypeDef = TypedDict(
    "_RequiredClientCreateDocumentRequiresTypeDef", {"Name": str}
)
_OptionalClientCreateDocumentRequiresTypeDef = TypedDict(
    "_OptionalClientCreateDocumentRequiresTypeDef", {"Version": str}, total=False
)


class ClientCreateDocumentRequiresTypeDef(
    _RequiredClientCreateDocumentRequiresTypeDef, _OptionalClientCreateDocumentRequiresTypeDef
):
    pass


ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List[ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef],
        "AttachmentsInformation": List[
            ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef],
    },
    total=False,
)

ClientCreateDocumentResponseTypeDef = TypedDict(
    "ClientCreateDocumentResponseTypeDef",
    {"DocumentDescription": ClientCreateDocumentResponseDocumentDescriptionTypeDef},
    total=False,
)

ClientCreateDocumentTagsTypeDef = TypedDict(
    "ClientCreateDocumentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientCreateMaintenanceWindowResponseTypeDef", {"WindowId": str}, total=False
)

ClientCreateMaintenanceWindowTagsTypeDef = TypedDict(
    "ClientCreateMaintenanceWindowTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateOpsItemNotificationsTypeDef = TypedDict(
    "ClientCreateOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)

ClientCreateOpsItemOperationalDataTypeDef = TypedDict(
    "ClientCreateOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientCreateOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "ClientCreateOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}
)

ClientCreateOpsItemResponseTypeDef = TypedDict(
    "ClientCreateOpsItemResponseTypeDef", {"OpsItemId": str}, total=False
)

ClientCreateOpsItemTagsTypeDef = TypedDict(
    "ClientCreateOpsItemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
    _OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
):
    pass


ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
)

_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {"PatchFilterGroup": ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef},
)
_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef(
    _RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef,
    _OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef,
):
    pass


ClientCreatePatchBaselineApprovalRulesTypeDef = TypedDict(
    "ClientCreatePatchBaselineApprovalRulesTypeDef",
    {"PatchRules": List[ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef]},
)

_RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef(
    _RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
    _OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
):
    pass


ClientCreatePatchBaselineGlobalFiltersTypeDef = TypedDict(
    "ClientCreatePatchBaselineGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef]},
)

ClientCreatePatchBaselineResponseTypeDef = TypedDict(
    "ClientCreatePatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)

_RequiredClientCreatePatchBaselineSourcesTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineSourcesTypeDef", {"Name": str}
)
_OptionalClientCreatePatchBaselineSourcesTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineSourcesTypeDef",
    {"Products": List[str], "Configuration": str},
    total=False,
)


class ClientCreatePatchBaselineSourcesTypeDef(
    _RequiredClientCreatePatchBaselineSourcesTypeDef,
    _OptionalClientCreatePatchBaselineSourcesTypeDef,
):
    pass


ClientCreatePatchBaselineTagsTypeDef = TypedDict(
    "ClientCreatePatchBaselineTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredClientCreateResourceDataSyncS3DestinationTypeDef", {"BucketName": str}
)
_OptionalClientCreateResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalClientCreateResourceDataSyncS3DestinationTypeDef",
    {"Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)


class ClientCreateResourceDataSyncS3DestinationTypeDef(
    _RequiredClientCreateResourceDataSyncS3DestinationTypeDef,
    _OptionalClientCreateResourceDataSyncS3DestinationTypeDef,
):
    pass


ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

_RequiredClientCreateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_RequiredClientCreateResourceDataSyncSyncSourceTypeDef", {"SourceType": str}
)
_OptionalClientCreateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_OptionalClientCreateResourceDataSyncSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ClientCreateResourceDataSyncSyncSourceTypeDef(
    _RequiredClientCreateResourceDataSyncSyncSourceTypeDef,
    _OptionalClientCreateResourceDataSyncSyncSourceTypeDef,
):
    pass


ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef = TypedDict(
    "ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

ClientDeleteInventoryResponseDeletionSummaryTypeDef = TypedDict(
    "ClientDeleteInventoryResponseDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef],
    },
    total=False,
)

ClientDeleteInventoryResponseTypeDef = TypedDict(
    "ClientDeleteInventoryResponseTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": ClientDeleteInventoryResponseDeletionSummaryTypeDef,
    },
    total=False,
)

ClientDeleteMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientDeleteMaintenanceWindowResponseTypeDef", {"WindowId": str}, total=False
)

ClientDeleteParametersResponseTypeDef = TypedDict(
    "ClientDeleteParametersResponseTypeDef",
    {"DeletedParameters": List[str], "InvalidParameters": List[str]},
    total=False,
)

ClientDeletePatchBaselineResponseTypeDef = TypedDict(
    "ClientDeletePatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)

ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef",
    {"WindowId": str, "WindowTargetId": str},
    total=False,
)

ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef",
    {"WindowId": str, "WindowTaskId": str},
    total=False,
)

ClientDescribeActivationsFiltersTypeDef = TypedDict(
    "ClientDescribeActivationsFiltersTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)

ClientDescribeActivationsResponseActivationListTagsTypeDef = TypedDict(
    "ClientDescribeActivationsResponseActivationListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeActivationsResponseActivationListTypeDef = TypedDict(
    "ClientDescribeActivationsResponseActivationListTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List[ClientDescribeActivationsResponseActivationListTagsTypeDef],
    },
    total=False,
)

ClientDescribeActivationsResponseTypeDef = TypedDict(
    "ClientDescribeActivationsResponseTypeDef",
    {
        "ActivationList": List[ClientDescribeActivationsResponseActivationListTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"]},
)
_OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef", {"Value": str}, total=False
)


class ClientDescribeAssociationExecutionTargetsFiltersTypeDef(
    _RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef,
    _OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef,
):
    pass


ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef",
    {"OutputSourceId": str, "OutputSourceType": str},
    total=False,
)

ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef,
    },
    total=False,
)

ClientDescribeAssociationExecutionTargetsResponseTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionTargetsResponseTypeDef",
    {
        "AssociationExecutionTargets": List[
            ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAssociationExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAssociationExecutionsFiltersTypeDef",
    {"Key": Literal["ExecutionId", "Status", "CreatedTime"]},
)
_OptionalClientDescribeAssociationExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAssociationExecutionsFiltersTypeDef",
    {"Value": str, "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"]},
    total=False,
)


class ClientDescribeAssociationExecutionsFiltersTypeDef(
    _RequiredClientDescribeAssociationExecutionsFiltersTypeDef,
    _OptionalClientDescribeAssociationExecutionsFiltersTypeDef,
):
    pass


ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

ClientDescribeAssociationExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionsResponseTypeDef",
    {
        "AssociationExecutions": List[
            ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientDescribeAssociationResponseTypeDef = TypedDict(
    "ClientDescribeAssociationResponseTypeDef",
    {"AssociationDescription": ClientDescribeAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)

_RequiredClientDescribeAutomationExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAutomationExecutionsFiltersTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
            "TagKey",
        ]
    },
)
_OptionalClientDescribeAutomationExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAutomationExecutionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeAutomationExecutionsFiltersTypeDef(
    _RequiredClientDescribeAutomationExecutionsFiltersTypeDef,
    _OptionalClientDescribeAutomationExecutionsFiltersTypeDef,
):
    pass


ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)

ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List[
            ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef
        ],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)

ClientDescribeAutomationExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseTypeDef",
    {
        "AutomationExecutionMetadataList": List[
            ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ]
    },
)
_OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeAutomationStepExecutionsFiltersTypeDef(
    _RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef,
    _OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef,
):
    pass


ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef],
        "TargetLocation": ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseTypeDef",
    {
        "StepExecutions": List[ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAvailablePatchesFiltersTypeDef = TypedDict(
    "ClientDescribeAvailablePatchesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribeAvailablePatchesResponsePatchesTypeDef = TypedDict(
    "ClientDescribeAvailablePatchesResponsePatchesTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

ClientDescribeAvailablePatchesResponseTypeDef = TypedDict(
    "ClientDescribeAvailablePatchesResponseTypeDef",
    {"Patches": List[ClientDescribeAvailablePatchesResponsePatchesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef = TypedDict(
    "ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef",
    {"AccountId": str, "SharedDocumentVersion": str},
    total=False,
)

ClientDescribeDocumentPermissionResponseTypeDef = TypedDict(
    "ClientDescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List[
            ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef
        ],
    },
    total=False,
)

ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeDocumentResponseDocumentParametersTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

ClientDescribeDocumentResponseDocumentRequiresTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribeDocumentResponseDocumentTagsTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeDocumentResponseDocumentTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientDescribeDocumentResponseDocumentParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List[ClientDescribeDocumentResponseDocumentTagsTypeDef],
        "AttachmentsInformation": List[
            ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientDescribeDocumentResponseDocumentRequiresTypeDef],
    },
    total=False,
)

ClientDescribeDocumentResponseTypeDef = TypedDict(
    "ClientDescribeDocumentResponseTypeDef",
    {"Document": ClientDescribeDocumentResponseDocumentTypeDef},
    total=False,
)

ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef = TypedDict(
    "ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)

ClientDescribeEffectiveInstanceAssociationsResponseTypeDef = TypedDict(
    "ClientDescribeEffectiveInstanceAssociationsResponseTypeDef",
    {
        "Associations": List[
            ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef",
    {
        "Patch": ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef,
        "PatchStatus": ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef",
    {
        "EffectivePatches": List[
            ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    {"OutputUrl": str},
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    {
        "S3OutputUrl": ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
    },
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef,
        "AssociationName": str,
    },
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseTypeDef",
    {
        "InstanceAssociationStatusInfos": List[
            ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeInstanceInformationFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeInstanceInformationFiltersTypeDef", {"Key": str}
)
_OptionalClientDescribeInstanceInformationFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeInstanceInformationFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeInstanceInformationFiltersTypeDef(
    _RequiredClientDescribeInstanceInformationFiltersTypeDef,
    _OptionalClientDescribeInstanceInformationFiltersTypeDef,
):
    pass


_RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef = TypedDict(
    "_RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ]
    },
)
_OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef = TypedDict(
    "_OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    {"valueSet": List[str]},
    total=False,
)


class ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef(
    _RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
    _OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
):
    pass


ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef = TypedDict(
    "ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef = TypedDict(
    "ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef,
    },
    total=False,
)

ClientDescribeInstanceInformationResponseTypeDef = TypedDict(
    "ClientDescribeInstanceInformationResponseTypeDef",
    {
        "InstanceInformationList": List[
            ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef", {"Key": str}
)
_OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef",
    {"Values": List[str], "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"]},
    total=False,
)


class ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef(
    _RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
    _OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
):
    pass


ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)

ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef",
    {
        "InstancePatchStates": List[
            ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)

ClientDescribeInstancePatchStatesResponseTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesResponseTypeDef",
    {
        "InstancePatchStates": List[
            ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInstancePatchesFiltersTypeDef = TypedDict(
    "ClientDescribeInstancePatchesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribeInstancePatchesResponsePatchesTypeDef = TypedDict(
    "ClientDescribeInstancePatchesResponsePatchesTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
    total=False,
)

ClientDescribeInstancePatchesResponseTypeDef = TypedDict(
    "ClientDescribeInstancePatchesResponseTypeDef",
    {"Patches": List[ClientDescribeInstancePatchesResponsePatchesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[
            ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
        ],
    },
    total=False,
)

ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef,
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

ClientDescribeInventoryDeletionsResponseTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseTypeDef",
    {
        "InventoryDeletions": List[
            ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef",
    {
        "WindowExecutionTaskIdentities": List[
            ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionsResponseTypeDef",
    {
        "WindowExecutions": List[
            ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowScheduleFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)

ClientDescribeMaintenanceWindowScheduleResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleResponseTypeDef",
    {
        "ScheduledWindowExecutions": List[
            ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowScheduleTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTargetsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List[ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowTargetsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsResponseTypeDef",
    {
        "Targets": List[ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowTasksFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List[ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef],
        "TaskParameters": Dict[
            str, ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef
        ],
        "Priority": int,
        "LoggingInfo": ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef,
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTypeDef",
    {"Tasks": List[ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeMaintenanceWindowsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef",
    {"WindowId": str, "Name": str},
    total=False,
)

ClientDescribeMaintenanceWindowsForTargetResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsForTargetResponseTypeDef",
    {
        "WindowIdentities": List[
            ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsResponseTypeDef",
    {
        "WindowIdentities": List[ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef",
    {
        "Key": Literal[
            "Status",
            "CreatedBy",
            "Source",
            "Priority",
            "Title",
            "OpsItemId",
            "CreatedTime",
            "LastModifiedTime",
            "OperationalData",
            "OperationalDataKey",
            "OperationalDataValue",
            "ResourceId",
            "AutomationId",
            "Category",
            "Severity",
        ]
    },
)
_OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef",
    {"Values": List[str], "Operator": Literal["Equal", "Contains", "GreaterThan", "LessThan"]},
    total=False,
)


class ClientDescribeOpsItemsOpsItemFiltersTypeDef(
    _RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef,
    _OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef,
):
    pass


ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef = TypedDict(
    "ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef = TypedDict(
    "ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[
            str, ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef
        ],
        "Category": str,
        "Severity": str,
    },
    total=False,
)

ClientDescribeOpsItemsResponseTypeDef = TypedDict(
    "ClientDescribeOpsItemsResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List[ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef],
    },
    total=False,
)

_RequiredClientDescribeParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeParametersFiltersTypeDef", {"Key": Literal["Name", "Type", "KeyId"]}
)
_OptionalClientDescribeParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeParametersFiltersTypeDef(
    _RequiredClientDescribeParametersFiltersTypeDef, _OptionalClientDescribeParametersFiltersTypeDef
):
    pass


ClientDescribeParametersParameterFiltersTypeDef = TypedDict(
    "ClientDescribeParametersParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)

ClientDescribeParametersResponseParametersPoliciesTypeDef = TypedDict(
    "ClientDescribeParametersResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

ClientDescribeParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeParametersResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ClientDescribeParametersResponseParametersPoliciesTypeDef],
    },
    total=False,
)

ClientDescribeParametersResponseTypeDef = TypedDict(
    "ClientDescribeParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeParametersResponseParametersTypeDef], "NextToken": str},
    total=False,
)

ClientDescribePatchBaselinesFiltersTypeDef = TypedDict(
    "ClientDescribePatchBaselinesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef = TypedDict(
    "ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

ClientDescribePatchBaselinesResponseTypeDef = TypedDict(
    "ClientDescribePatchBaselinesResponseTypeDef",
    {
        "BaselineIdentities": List[ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribePatchGroupStateResponseTypeDef = TypedDict(
    "ClientDescribePatchGroupStateResponseTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
    },
    total=False,
)

ClientDescribePatchGroupsFiltersTypeDef = TypedDict(
    "ClientDescribePatchGroupsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef = TypedDict(
    "ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

ClientDescribePatchGroupsResponseMappingsTypeDef = TypedDict(
    "ClientDescribePatchGroupsResponseMappingsTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef,
    },
    total=False,
)

ClientDescribePatchGroupsResponseTypeDef = TypedDict(
    "ClientDescribePatchGroupsResponseTypeDef",
    {"Mappings": List[ClientDescribePatchGroupsResponseMappingsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribePatchPropertiesResponseTypeDef = TypedDict(
    "ClientDescribePatchPropertiesResponseTypeDef",
    {"Properties": List[Dict[str, str]], "NextToken": str},
    total=False,
)

_RequiredClientDescribeSessionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeSessionsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"]},
)
_OptionalClientDescribeSessionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeSessionsFiltersTypeDef", {"value": str}, total=False
)


class ClientDescribeSessionsFiltersTypeDef(
    _RequiredClientDescribeSessionsFiltersTypeDef, _OptionalClientDescribeSessionsFiltersTypeDef
):
    pass


ClientDescribeSessionsResponseSessionsOutputUrlTypeDef = TypedDict(
    "ClientDescribeSessionsResponseSessionsOutputUrlTypeDef",
    {"S3OutputUrl": str, "CloudWatchOutputUrl": str},
    total=False,
)

ClientDescribeSessionsResponseSessionsTypeDef = TypedDict(
    "ClientDescribeSessionsResponseSessionsTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": ClientDescribeSessionsResponseSessionsOutputUrlTypeDef,
    },
    total=False,
)

ClientDescribeSessionsResponseTypeDef = TypedDict(
    "ClientDescribeSessionsResponseTypeDef",
    {"Sessions": List[ClientDescribeSessionsResponseSessionsTypeDef], "NextToken": str},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef",
    {
        "TotalSteps": int,
        "SuccessSteps": int,
        "FailedSteps": int,
        "CancelledSteps": int,
        "TimedOutSteps": int,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[
            ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef
        ],
        "TargetLocation": ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "StepExecutions": List[
            ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef
        ],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "ExecutedBy": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "TargetParameterName": str,
        "Targets": List[ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "TargetLocations": List[
            ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef
        ],
        "ProgressCounters": ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef,
    },
    total=False,
)

ClientGetAutomationExecutionResponseTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseTypeDef",
    {"AutomationExecution": ClientGetAutomationExecutionResponseAutomationExecutionTypeDef},
    total=False,
)

ClientGetCalendarStateResponseTypeDef = TypedDict(
    "ClientGetCalendarStateResponseTypeDef",
    {"State": Literal["OPEN", "CLOSED"], "AtTime": str, "NextTransitionTime": str},
    total=False,
)

ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientGetCommandInvocationResponseTypeDef = TypedDict(
    "ClientGetCommandInvocationResponseTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientGetConnectionStatusResponseTypeDef = TypedDict(
    "ClientGetConnectionStatusResponseTypeDef",
    {"Target": str, "Status": Literal["Connected", "NotConnected"]},
    total=False,
)

ClientGetDefaultPatchBaselineResponseTypeDef = TypedDict(
    "ClientGetDefaultPatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
    },
    total=False,
)

ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef = TypedDict(
    "ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef",
    {"InstanceId": str, "SnapshotId": str, "SnapshotDownloadUrl": str, "Product": str},
    total=False,
)

ClientGetDocumentResponseAttachmentsContentTypeDef = TypedDict(
    "ClientGetDocumentResponseAttachmentsContentTypeDef",
    {"Name": str, "Size": int, "Hash": str, "HashType": str, "Url": str},
    total=False,
)

ClientGetDocumentResponseRequiresTypeDef = TypedDict(
    "ClientGetDocumentResponseRequiresTypeDef", {"Name": str, "Version": str}, total=False
)

ClientGetDocumentResponseTypeDef = TypedDict(
    "ClientGetDocumentResponseTypeDef",
    {
        "Name": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "Content": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "Requires": List[ClientGetDocumentResponseRequiresTypeDef],
        "AttachmentsContent": List[ClientGetDocumentResponseAttachmentsContentTypeDef],
    },
    total=False,
)

ClientGetInventoryAggregatorsGroupsFiltersTypeDef = TypedDict(
    "ClientGetInventoryAggregatorsGroupsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)

ClientGetInventoryAggregatorsGroupsTypeDef = TypedDict(
    "ClientGetInventoryAggregatorsGroupsTypeDef",
    {"Name": str, "Filters": List[ClientGetInventoryAggregatorsGroupsFiltersTypeDef]},
    total=False,
)

ClientGetInventoryAggregatorsTypeDef = TypedDict(
    "ClientGetInventoryAggregatorsTypeDef",
    {
        "Expression": str,
        "Aggregators": Any,
        "Groups": List[ClientGetInventoryAggregatorsGroupsTypeDef],
    },
    total=False,
)

_RequiredClientGetInventoryFiltersTypeDef = TypedDict(
    "_RequiredClientGetInventoryFiltersTypeDef", {"Key": str}
)
_OptionalClientGetInventoryFiltersTypeDef = TypedDict(
    "_OptionalClientGetInventoryFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetInventoryFiltersTypeDef(
    _RequiredClientGetInventoryFiltersTypeDef, _OptionalClientGetInventoryFiltersTypeDef
):
    pass


ClientGetInventoryResponseEntitiesDataTypeDef = TypedDict(
    "ClientGetInventoryResponseEntitiesDataTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)

ClientGetInventoryResponseEntitiesTypeDef = TypedDict(
    "ClientGetInventoryResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, ClientGetInventoryResponseEntitiesDataTypeDef]},
    total=False,
)

ClientGetInventoryResponseTypeDef = TypedDict(
    "ClientGetInventoryResponseTypeDef",
    {"Entities": List[ClientGetInventoryResponseEntitiesTypeDef], "NextToken": str},
    total=False,
)

ClientGetInventoryResultAttributesTypeDef = TypedDict(
    "ClientGetInventoryResultAttributesTypeDef", {"TypeName": str}
)

ClientGetInventorySchemaResponseSchemasAttributesTypeDef = TypedDict(
    "ClientGetInventorySchemaResponseSchemasAttributesTypeDef",
    {"Name": str, "DataType": Literal["string", "number"]},
    total=False,
)

ClientGetInventorySchemaResponseSchemasTypeDef = TypedDict(
    "ClientGetInventorySchemaResponseSchemasTypeDef",
    {
        "TypeName": str,
        "Version": str,
        "Attributes": List[ClientGetInventorySchemaResponseSchemasAttributesTypeDef],
        "DisplayName": str,
    },
    total=False,
)

ClientGetInventorySchemaResponseTypeDef = TypedDict(
    "ClientGetInventorySchemaResponseTypeDef",
    {"Schemas": List[ClientGetInventorySchemaResponseSchemasTypeDef], "NextToken": str},
    total=False,
)

ClientGetMaintenanceWindowExecutionResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientGetMaintenanceWindowExecutionTaskResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionTaskResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": List[
            Dict[str, ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef]
        ],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientGetMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTargetsTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "DocumentVersion": str,
        "NotificationConfig": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[ClientGetMaintenanceWindowTaskResponseTargetsTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": Dict[str, ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef],
        "TaskInvocationParameters": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientGetOpsItemResponseOpsItemNotificationsTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)

ClientGetOpsItemResponseOpsItemOperationalDataTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}, total=False
)

ClientGetOpsItemResponseOpsItemTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List[ClientGetOpsItemResponseOpsItemNotificationsTypeDef],
        "Priority": int,
        "RelatedOpsItems": List[ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef],
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, ClientGetOpsItemResponseOpsItemOperationalDataTypeDef],
        "Category": str,
        "Severity": str,
    },
    total=False,
)

ClientGetOpsItemResponseTypeDef = TypedDict(
    "ClientGetOpsItemResponseTypeDef",
    {"OpsItem": ClientGetOpsItemResponseOpsItemTypeDef},
    total=False,
)

ClientGetOpsSummaryAggregatorsFiltersTypeDef = TypedDict(
    "ClientGetOpsSummaryAggregatorsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)

ClientGetOpsSummaryAggregatorsTypeDef = TypedDict(
    "ClientGetOpsSummaryAggregatorsTypeDef",
    {
        "AggregatorType": str,
        "TypeName": str,
        "AttributeName": str,
        "Values": Dict[str, str],
        "Filters": List[ClientGetOpsSummaryAggregatorsFiltersTypeDef],
        "Aggregators": Any,
    },
    total=False,
)

_RequiredClientGetOpsSummaryFiltersTypeDef = TypedDict(
    "_RequiredClientGetOpsSummaryFiltersTypeDef", {"Key": str}
)
_OptionalClientGetOpsSummaryFiltersTypeDef = TypedDict(
    "_OptionalClientGetOpsSummaryFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetOpsSummaryFiltersTypeDef(
    _RequiredClientGetOpsSummaryFiltersTypeDef, _OptionalClientGetOpsSummaryFiltersTypeDef
):
    pass


ClientGetOpsSummaryResponseEntitiesDataTypeDef = TypedDict(
    "ClientGetOpsSummaryResponseEntitiesDataTypeDef",
    {"CaptureTime": str, "Content": List[Dict[str, str]]},
    total=False,
)

ClientGetOpsSummaryResponseEntitiesTypeDef = TypedDict(
    "ClientGetOpsSummaryResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, ClientGetOpsSummaryResponseEntitiesDataTypeDef]},
    total=False,
)

ClientGetOpsSummaryResponseTypeDef = TypedDict(
    "ClientGetOpsSummaryResponseTypeDef",
    {"Entities": List[ClientGetOpsSummaryResponseEntitiesTypeDef], "NextToken": str},
    total=False,
)

ClientGetOpsSummaryResultAttributesTypeDef = TypedDict(
    "ClientGetOpsSummaryResultAttributesTypeDef", {"TypeName": str}
)

ClientGetParameterHistoryResponseParametersPoliciesTypeDef = TypedDict(
    "ClientGetParameterHistoryResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

ClientGetParameterHistoryResponseParametersTypeDef = TypedDict(
    "ClientGetParameterHistoryResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ClientGetParameterHistoryResponseParametersPoliciesTypeDef],
    },
    total=False,
)

ClientGetParameterHistoryResponseTypeDef = TypedDict(
    "ClientGetParameterHistoryResponseTypeDef",
    {"Parameters": List[ClientGetParameterHistoryResponseParametersTypeDef], "NextToken": str},
    total=False,
)

ClientGetParameterResponseParameterTypeDef = TypedDict(
    "ClientGetParameterResponseParameterTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

ClientGetParameterResponseTypeDef = TypedDict(
    "ClientGetParameterResponseTypeDef",
    {"Parameter": ClientGetParameterResponseParameterTypeDef},
    total=False,
)

ClientGetParametersByPathParameterFiltersTypeDef = TypedDict(
    "ClientGetParametersByPathParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)

ClientGetParametersByPathResponseParametersTypeDef = TypedDict(
    "ClientGetParametersByPathResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

ClientGetParametersByPathResponseTypeDef = TypedDict(
    "ClientGetParametersByPathResponseTypeDef",
    {"Parameters": List[ClientGetParametersByPathResponseParametersTypeDef], "NextToken": str},
    total=False,
)

ClientGetParametersResponseParametersTypeDef = TypedDict(
    "ClientGetParametersResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

ClientGetParametersResponseTypeDef = TypedDict(
    "ClientGetParametersResponseTypeDef",
    {
        "Parameters": List[ClientGetParametersResponseParametersTypeDef],
        "InvalidParameters": List[str],
    },
    total=False,
)

ClientGetPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "ClientGetPatchBaselineForPatchGroupResponseTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    {
        "PatchFilterGroup": ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef,
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesTypeDef",
    {"PatchRules": List[ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef]},
    total=False,
)

ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientGetPatchBaselineResponseGlobalFiltersTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef]},
    total=False,
)

ClientGetPatchBaselineResponseSourcesTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseSourcesTypeDef",
    {"Name": str, "Products": List[str], "Configuration": str},
    total=False,
)

ClientGetPatchBaselineResponseTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "GlobalFilters": ClientGetPatchBaselineResponseGlobalFiltersTypeDef,
        "ApprovalRules": ClientGetPatchBaselineResponseApprovalRulesTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[ClientGetPatchBaselineResponseSourcesTypeDef],
    },
    total=False,
)

ClientGetServiceSettingResponseServiceSettingTypeDef = TypedDict(
    "ClientGetServiceSettingResponseServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

ClientGetServiceSettingResponseTypeDef = TypedDict(
    "ClientGetServiceSettingResponseTypeDef",
    {"ServiceSetting": ClientGetServiceSettingResponseServiceSettingTypeDef},
    total=False,
)

ClientLabelParameterVersionResponseTypeDef = TypedDict(
    "ClientLabelParameterVersionResponseTypeDef",
    {"InvalidLabels": List[str], "ParameterVersion": int},
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef",
    {
        "S3Location": ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List[ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientListAssociationVersionsResponseTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseTypeDef",
    {
        "AssociationVersions": List[
            ClientListAssociationVersionsResponseAssociationVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListAssociationsAssociationFilterListTypeDef = TypedDict(
    "_RequiredClientListAssociationsAssociationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
        ]
    },
)
_OptionalClientListAssociationsAssociationFilterListTypeDef = TypedDict(
    "_OptionalClientListAssociationsAssociationFilterListTypeDef", {"value": str}, total=False
)


class ClientListAssociationsAssociationFilterListTypeDef(
    _RequiredClientListAssociationsAssociationFilterListTypeDef,
    _OptionalClientListAssociationsAssociationFilterListTypeDef,
):
    pass


ClientListAssociationsResponseAssociationsOverviewTypeDef = TypedDict(
    "ClientListAssociationsResponseAssociationsOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientListAssociationsResponseAssociationsTargetsTypeDef = TypedDict(
    "ClientListAssociationsResponseAssociationsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListAssociationsResponseAssociationsTypeDef = TypedDict(
    "ClientListAssociationsResponseAssociationsTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List[ClientListAssociationsResponseAssociationsTargetsTypeDef],
        "LastExecutionDate": datetime,
        "Overview": ClientListAssociationsResponseAssociationsOverviewTypeDef,
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

ClientListAssociationsResponseTypeDef = TypedDict(
    "ClientListAssociationsResponseTypeDef",
    {"Associations": List[ClientListAssociationsResponseAssociationsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientListCommandInvocationsFiltersTypeDef = TypedDict(
    "_RequiredClientListCommandInvocationsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalClientListCommandInvocationsFiltersTypeDef = TypedDict(
    "_OptionalClientListCommandInvocationsFiltersTypeDef", {"value": str}, total=False
)


class ClientListCommandInvocationsFiltersTypeDef(
    _RequiredClientListCommandInvocationsFiltersTypeDef,
    _OptionalClientListCommandInvocationsFiltersTypeDef,
):
    pass


ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientListCommandInvocationsResponseCommandInvocationsTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List[
            ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef
        ],
        "ServiceRole": str,
        "NotificationConfig": ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientListCommandInvocationsResponseTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseTypeDef",
    {
        "CommandInvocations": List[ClientListCommandInvocationsResponseCommandInvocationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListCommandsFiltersTypeDef = TypedDict(
    "_RequiredClientListCommandsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalClientListCommandsFiltersTypeDef = TypedDict(
    "_OptionalClientListCommandsFiltersTypeDef", {"value": str}, total=False
)


class ClientListCommandsFiltersTypeDef(
    _RequiredClientListCommandsFiltersTypeDef, _OptionalClientListCommandsFiltersTypeDef
):
    pass


ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientListCommandsResponseCommandsNotificationConfigTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientListCommandsResponseCommandsTargetsTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListCommandsResponseCommandsTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ClientListCommandsResponseCommandsTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ClientListCommandsResponseCommandsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientListCommandsResponseTypeDef = TypedDict(
    "ClientListCommandsResponseTypeDef",
    {"Commands": List[ClientListCommandsResponseCommandsTypeDef], "NextToken": str},
    total=False,
)

ClientListComplianceItemsFiltersTypeDef = TypedDict(
    "ClientListComplianceItemsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)

ClientListComplianceItemsResponseComplianceItemsTypeDef = TypedDict(
    "ClientListComplianceItemsResponseComplianceItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef,
        "Details": Dict[str, str],
    },
    total=False,
)

ClientListComplianceItemsResponseTypeDef = TypedDict(
    "ClientListComplianceItemsResponseTypeDef",
    {
        "ComplianceItems": List[ClientListComplianceItemsResponseComplianceItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListComplianceSummariesFiltersTypeDef = TypedDict(
    "ClientListComplianceSummariesFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)

ClientListComplianceSummariesResponseTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseTypeDef",
    {
        "ComplianceSummaryItems": List[
            ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "ClientListDocumentVersionsResponseDocumentVersionsTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)

ClientListDocumentVersionsResponseTypeDef = TypedDict(
    "ClientListDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[ClientListDocumentVersionsResponseDocumentVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListDocumentsDocumentFilterListTypeDef = TypedDict(
    "_RequiredClientListDocumentsDocumentFilterListTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"]},
)
_OptionalClientListDocumentsDocumentFilterListTypeDef = TypedDict(
    "_OptionalClientListDocumentsDocumentFilterListTypeDef", {"value": str}, total=False
)


class ClientListDocumentsDocumentFilterListTypeDef(
    _RequiredClientListDocumentsDocumentFilterListTypeDef,
    _OptionalClientListDocumentsDocumentFilterListTypeDef,
):
    pass


ClientListDocumentsFiltersTypeDef = TypedDict(
    "ClientListDocumentsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef = TypedDict(
    "ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef = TypedDict(
    "ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListDocumentsResponseDocumentIdentifiersTypeDef = TypedDict(
    "ClientListDocumentsResponseDocumentIdentifiersTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List[ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef],
        "Requires": List[ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef],
    },
    total=False,
)

ClientListDocumentsResponseTypeDef = TypedDict(
    "ClientListDocumentsResponseTypeDef",
    {
        "DocumentIdentifiers": List[ClientListDocumentsResponseDocumentIdentifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListInventoryEntriesFiltersTypeDef = TypedDict(
    "_RequiredClientListInventoryEntriesFiltersTypeDef", {"Key": str}
)
_OptionalClientListInventoryEntriesFiltersTypeDef = TypedDict(
    "_OptionalClientListInventoryEntriesFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientListInventoryEntriesFiltersTypeDef(
    _RequiredClientListInventoryEntriesFiltersTypeDef,
    _OptionalClientListInventoryEntriesFiltersTypeDef,
):
    pass


ClientListInventoryEntriesResponseTypeDef = TypedDict(
    "ClientListInventoryEntriesResponseTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceComplianceSummariesFiltersTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef,
        "CompliantSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseTypeDef",
    {
        "ResourceComplianceSummaryItems": List[
            ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef",
    {"BucketName": str, "Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef,
        "S3Destination": ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef,
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ClientListResourceDataSyncResponseTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseTypeDef",
    {
        "ResourceDataSyncItems": List[
            ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef
        ],
        "NextToken": str,
    },
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

_RequiredClientPutComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_RequiredClientPutComplianceItemsExecutionSummaryTypeDef", {"ExecutionTime": datetime}
)
_OptionalClientPutComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_OptionalClientPutComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ClientPutComplianceItemsExecutionSummaryTypeDef(
    _RequiredClientPutComplianceItemsExecutionSummaryTypeDef,
    _OptionalClientPutComplianceItemsExecutionSummaryTypeDef,
):
    pass


ClientPutComplianceItemsItemsTypeDef = TypedDict(
    "ClientPutComplianceItemsItemsTypeDef",
    {
        "Id": str,
        "Title": str,
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Details": Dict[str, str],
    },
    total=False,
)

_RequiredClientPutInventoryItemsTypeDef = TypedDict(
    "_RequiredClientPutInventoryItemsTypeDef", {"TypeName": str}
)
_OptionalClientPutInventoryItemsTypeDef = TypedDict(
    "_OptionalClientPutInventoryItemsTypeDef",
    {
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
        "Context": Dict[str, str],
    },
    total=False,
)


class ClientPutInventoryItemsTypeDef(
    _RequiredClientPutInventoryItemsTypeDef, _OptionalClientPutInventoryItemsTypeDef
):
    pass


ClientPutInventoryResponseTypeDef = TypedDict(
    "ClientPutInventoryResponseTypeDef", {"Message": str}, total=False
)

ClientPutParameterResponseTypeDef = TypedDict(
    "ClientPutParameterResponseTypeDef",
    {"Version": int, "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"]},
    total=False,
)

ClientPutParameterTagsTypeDef = TypedDict(
    "ClientPutParameterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRegisterDefaultPatchBaselineResponseTypeDef = TypedDict(
    "ClientRegisterDefaultPatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)

ClientRegisterPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "ClientRegisterPatchBaselineForPatchGroupResponseTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

ClientRegisterTargetWithMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientRegisterTargetWithMaintenanceWindowResponseTypeDef", {"WindowTargetId": str}, total=False
)

ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef = TypedDict(
    "ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowResponseTypeDef", {"WindowTaskId": str}, total=False
)

ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "DocumentVersion": str,
        "NotificationConfig": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientResetServiceSettingResponseServiceSettingTypeDef = TypedDict(
    "ClientResetServiceSettingResponseServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

ClientResetServiceSettingResponseTypeDef = TypedDict(
    "ClientResetServiceSettingResponseTypeDef",
    {"ServiceSetting": ClientResetServiceSettingResponseServiceSettingTypeDef},
    total=False,
)

ClientResumeSessionResponseTypeDef = TypedDict(
    "ClientResumeSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

ClientSendCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientSendCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientSendCommandNotificationConfigTypeDef = TypedDict(
    "ClientSendCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientSendCommandResponseCommandNotificationConfigTypeDef = TypedDict(
    "ClientSendCommandResponseCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientSendCommandResponseCommandTargetsTypeDef = TypedDict(
    "ClientSendCommandResponseCommandTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientSendCommandResponseCommandTypeDef = TypedDict(
    "ClientSendCommandResponseCommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ClientSendCommandResponseCommandTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ClientSendCommandResponseCommandNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientSendCommandResponseTypeDef = TypedDict(
    "ClientSendCommandResponseTypeDef",
    {"Command": ClientSendCommandResponseCommandTypeDef},
    total=False,
)

ClientSendCommandTargetsTypeDef = TypedDict(
    "ClientSendCommandTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientStartAutomationExecutionResponseTypeDef = TypedDict(
    "ClientStartAutomationExecutionResponseTypeDef", {"AutomationExecutionId": str}, total=False
)

ClientStartAutomationExecutionTagsTypeDef = TypedDict(
    "ClientStartAutomationExecutionTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientStartAutomationExecutionTargetLocationsTypeDef = TypedDict(
    "ClientStartAutomationExecutionTargetLocationsTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientStartAutomationExecutionTargetsTypeDef = TypedDict(
    "ClientStartAutomationExecutionTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientStartSessionResponseTypeDef = TypedDict(
    "ClientStartSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

ClientTerminateSessionResponseTypeDef = TypedDict(
    "ClientTerminateSessionResponseTypeDef", {"SessionId": str}, total=False
)

ClientUpdateAssociationOutputLocationS3LocationTypeDef = TypedDict(
    "ClientUpdateAssociationOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientUpdateAssociationOutputLocationTypeDef = TypedDict(
    "ClientUpdateAssociationOutputLocationTypeDef",
    {"S3Location": ClientUpdateAssociationOutputLocationS3LocationTypeDef},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientUpdateAssociationResponseTypeDef = TypedDict(
    "ClientUpdateAssociationResponseTypeDef",
    {"AssociationDescription": ClientUpdateAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)

_RequiredClientUpdateAssociationStatusAssociationStatusTypeDef = TypedDict(
    "_RequiredClientUpdateAssociationStatusAssociationStatusTypeDef", {"Date": datetime}
)
_OptionalClientUpdateAssociationStatusAssociationStatusTypeDef = TypedDict(
    "_OptionalClientUpdateAssociationStatusAssociationStatusTypeDef",
    {"Name": Literal["Pending", "Success", "Failed"], "Message": str, "AdditionalInfo": str},
    total=False,
)


class ClientUpdateAssociationStatusAssociationStatusTypeDef(
    _RequiredClientUpdateAssociationStatusAssociationStatusTypeDef,
    _OptionalClientUpdateAssociationStatusAssociationStatusTypeDef,
):
    pass


ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientUpdateAssociationStatusResponseTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseTypeDef",
    {"AssociationDescription": ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef},
    total=False,
)

ClientUpdateAssociationTargetsTypeDef = TypedDict(
    "ClientUpdateAssociationTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientUpdateDocumentAttachmentsTypeDef = TypedDict(
    "ClientUpdateDocumentAttachmentsTypeDef",
    {
        "Key": Literal["SourceUrl", "S3FileUrl", "AttachmentReference"],
        "Values": List[str],
        "Name": str,
    },
    total=False,
)

ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef = TypedDict(
    "ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef",
    {"Name": str, "DefaultVersion": str, "DefaultVersionName": str},
    total=False,
)

ClientUpdateDocumentDefaultVersionResponseTypeDef = TypedDict(
    "ClientUpdateDocumentDefaultVersionResponseTypeDef",
    {"Description": ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List[ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef],
        "AttachmentsInformation": List[
            ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef],
    },
    total=False,
)

ClientUpdateDocumentResponseTypeDef = TypedDict(
    "ClientUpdateDocumentResponseTypeDef",
    {"DocumentDescription": ClientUpdateDocumentResponseDocumentDescriptionTypeDef},
    total=False,
)

ClientUpdateMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTargetResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTargetResponseTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List[ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTargetTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTargetTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "DocumentVersion": str,
        "NotificationConfig": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef],
        "TaskInvocationParameters": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandCloudWatchOutputConfigTypeDef,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "DocumentVersion": str,
        "NotificationConfig": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef", {"Values": List[str]}, total=False
)

ClientUpdateOpsItemNotificationsTypeDef = TypedDict(
    "ClientUpdateOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)

ClientUpdateOpsItemOperationalDataTypeDef = TypedDict(
    "ClientUpdateOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientUpdateOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "ClientUpdateOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}
)

_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
    _OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
):
    pass


ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
)

_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {"PatchFilterGroup": ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef},
)
_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef(
    _RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef,
    _OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef,
):
    pass


ClientUpdatePatchBaselineApprovalRulesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineApprovalRulesTypeDef",
    {"PatchRules": List[ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef]},
)

_RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef(
    _RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
    _OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
):
    pass


ClientUpdatePatchBaselineGlobalFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef]},
)

ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
    total=False,
)

ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    {
        "PatchFilterGroup": ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef,
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)

ClientUpdatePatchBaselineResponseApprovalRulesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesTypeDef",
    {"PatchRules": List[ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef]},
    total=False,
)

ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef]},
    total=False,
)

ClientUpdatePatchBaselineResponseSourcesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseSourcesTypeDef",
    {"Name": str, "Products": List[str], "Configuration": str},
    total=False,
)

ClientUpdatePatchBaselineResponseTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "GlobalFilters": ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef,
        "ApprovalRules": ClientUpdatePatchBaselineResponseApprovalRulesTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[ClientUpdatePatchBaselineResponseSourcesTypeDef],
    },
    total=False,
)

_RequiredClientUpdatePatchBaselineSourcesTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineSourcesTypeDef", {"Name": str}
)
_OptionalClientUpdatePatchBaselineSourcesTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineSourcesTypeDef",
    {"Products": List[str], "Configuration": str},
    total=False,
)


class ClientUpdatePatchBaselineSourcesTypeDef(
    _RequiredClientUpdatePatchBaselineSourcesTypeDef,
    _OptionalClientUpdatePatchBaselineSourcesTypeDef,
):
    pass


ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

_RequiredClientUpdateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_RequiredClientUpdateResourceDataSyncSyncSourceTypeDef", {"SourceType": str}
)
_OptionalClientUpdateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_OptionalClientUpdateResourceDataSyncSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ClientUpdateResourceDataSyncSyncSourceTypeDef(
    _RequiredClientUpdateResourceDataSyncSyncSourceTypeDef,
    _OptionalClientUpdateResourceDataSyncSyncSourceTypeDef,
):
    pass


CommandFilterTypeDef = TypedDict(
    "CommandFilterTypeDef",
    {
        "key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"],
        "value": str,
    },
)

ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ActivationTypeDef = TypedDict(
    "ActivationTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

DescribeActivationsResultTypeDef = TypedDict(
    "DescribeActivationsResultTypeDef",
    {"ActivationList": List[ActivationTypeDef], "NextToken": str},
    total=False,
)

OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef", {"OutputSourceId": str, "OutputSourceType": str}, total=False
)

AssociationExecutionTargetTypeDef = TypedDict(
    "AssociationExecutionTargetTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": OutputSourceTypeDef,
    },
    total=False,
)

DescribeAssociationExecutionTargetsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultTypeDef",
    {"AssociationExecutionTargets": List[AssociationExecutionTargetTypeDef], "NextToken": str},
    total=False,
)

AssociationExecutionTypeDef = TypedDict(
    "AssociationExecutionTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

DescribeAssociationExecutionsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultTypeDef",
    {"AssociationExecutions": List[AssociationExecutionTypeDef], "NextToken": str},
    total=False,
)

ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef", {"ParameterValues": List[str], "Truncated": bool}, total=False
)

TargetTypeDef = TypedDict("TargetTypeDef", {"Key": str, "Values": List[str]}, total=False)

AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List[TargetTypeDef],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)

DescribeAutomationExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultTypeDef",
    {"AutomationExecutionMetadataList": List[AutomationExecutionMetadataTypeDef], "NextToken": str},
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

TargetLocationTypeDef = TypedDict(
    "TargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

StepExecutionTypeDef = TypedDict(
    "StepExecutionTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": FailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[TargetTypeDef],
        "TargetLocation": TargetLocationTypeDef,
    },
    total=False,
)

DescribeAutomationStepExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultTypeDef",
    {"StepExecutions": List[StepExecutionTypeDef], "NextToken": str},
    total=False,
)

PatchTypeDef = TypedDict(
    "PatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

DescribeAvailablePatchesResultTypeDef = TypedDict(
    "DescribeAvailablePatchesResultTypeDef",
    {"Patches": List[PatchTypeDef], "NextToken": str},
    total=False,
)

InstanceAssociationTypeDef = TypedDict(
    "InstanceAssociationTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)

DescribeEffectiveInstanceAssociationsResultTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    {"Associations": List[InstanceAssociationTypeDef], "NextToken": str},
    total=False,
)

PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)

EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef", {"Patch": PatchTypeDef, "PatchStatus": PatchStatusTypeDef}, total=False
)

DescribeEffectivePatchesForPatchBaselineResultTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    {"EffectivePatches": List[EffectivePatchTypeDef], "NextToken": str},
    total=False,
)

S3OutputUrlTypeDef = TypedDict("S3OutputUrlTypeDef", {"OutputUrl": str}, total=False)

InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef", {"S3OutputUrl": S3OutputUrlTypeDef}, total=False
)

InstanceAssociationStatusInfoTypeDef = TypedDict(
    "InstanceAssociationStatusInfoTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": InstanceAssociationOutputUrlTypeDef,
        "AssociationName": str,
    },
    total=False,
)

DescribeInstanceAssociationsStatusResultTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultTypeDef",
    {
        "InstanceAssociationStatusInfos": List[InstanceAssociationStatusInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)

InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": InstanceAggregatedAssociationOverviewTypeDef,
    },
    total=False,
)

DescribeInstanceInformationResultTypeDef = TypedDict(
    "DescribeInstanceInformationResultTypeDef",
    {"InstanceInformationList": List[InstanceInformationTypeDef], "NextToken": str},
    total=False,
)

_RequiredInstancePatchStateTypeDef = TypedDict(
    "_RequiredInstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
    },
)
_OptionalInstancePatchStateTypeDef = TypedDict(
    "_OptionalInstancePatchStateTypeDef",
    {
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)


class InstancePatchStateTypeDef(
    _RequiredInstancePatchStateTypeDef, _OptionalInstancePatchStateTypeDef
):
    pass


DescribeInstancePatchStatesForPatchGroupResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    {"InstancePatchStates": List[InstancePatchStateTypeDef], "NextToken": str},
    total=False,
)

DescribeInstancePatchStatesResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultTypeDef",
    {"InstancePatchStates": List[InstancePatchStateTypeDef], "NextToken": str},
    total=False,
)

PatchComplianceDataTypeDef = TypedDict(
    "PatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
)

DescribeInstancePatchesResultTypeDef = TypedDict(
    "DescribeInstancePatchesResultTypeDef",
    {"Patches": List[PatchComplianceDataTypeDef], "NextToken": str},
    total=False,
)

InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

InventoryDeletionSummaryTypeDef = TypedDict(
    "InventoryDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[InventoryDeletionSummaryItemTypeDef],
    },
    total=False,
)

InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": InventoryDeletionSummaryTypeDef,
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

DescribeInventoryDeletionsResultTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultTypeDef",
    {"InventoryDeletions": List[InventoryDeletionStatusItemTypeDef], "NextToken": str},
    total=False,
)

MaintenanceWindowExecutionTaskInvocationIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            MaintenanceWindowExecutionTaskInvocationIdentityTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    {
        "WindowExecutionTaskIdentities": List[MaintenanceWindowExecutionTaskIdentityTypeDef],
        "NextToken": str,
    },
    total=False,
)

MaintenanceWindowExecutionTypeDef = TypedDict(
    "MaintenanceWindowExecutionTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    {"WindowExecutions": List[MaintenanceWindowExecutionTypeDef], "NextToken": str},
    total=False,
)

ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)

DescribeMaintenanceWindowScheduleResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    {"ScheduledWindowExecutions": List[ScheduledWindowExecutionTypeDef], "NextToken": str},
    total=False,
)

MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List[TargetTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

DescribeMaintenanceWindowTargetsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    {"Targets": List[MaintenanceWindowTargetTypeDef], "NextToken": str},
    total=False,
)

_RequiredLoggingInfoTypeDef = TypedDict(
    "_RequiredLoggingInfoTypeDef", {"S3BucketName": str, "S3Region": str}
)
_OptionalLoggingInfoTypeDef = TypedDict(
    "_OptionalLoggingInfoTypeDef", {"S3KeyPrefix": str}, total=False
)


class LoggingInfoTypeDef(_RequiredLoggingInfoTypeDef, _OptionalLoggingInfoTypeDef):
    pass


MaintenanceWindowTaskParameterValueExpressionTypeDef = TypedDict(
    "MaintenanceWindowTaskParameterValueExpressionTypeDef", {"Values": List[str]}, total=False
)

MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List[TargetTypeDef],
        "TaskParameters": Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef],
        "Priority": int,
        "LoggingInfo": LoggingInfoTypeDef,
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

DescribeMaintenanceWindowTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultTypeDef",
    {"Tasks": List[MaintenanceWindowTaskTypeDef], "NextToken": str},
    total=False,
)

MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef", {"WindowId": str, "Name": str}, total=False
)

DescribeMaintenanceWindowsForTargetResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    {"WindowIdentities": List[MaintenanceWindowIdentityForTargetTypeDef], "NextToken": str},
    total=False,
)

MaintenanceWindowIdentityTypeDef = TypedDict(
    "MaintenanceWindowIdentityTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

DescribeMaintenanceWindowsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultTypeDef",
    {"WindowIdentities": List[MaintenanceWindowIdentityTypeDef], "NextToken": str},
    total=False,
)

ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ParameterInlinePolicyTypeDef],
    },
    total=False,
)

DescribeParametersResultTypeDef = TypedDict(
    "DescribeParametersResultTypeDef",
    {"Parameters": List[ParameterMetadataTypeDef], "NextToken": str},
    total=False,
)

PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

DescribePatchBaselinesResultTypeDef = TypedDict(
    "DescribePatchBaselinesResultTypeDef",
    {"BaselineIdentities": List[PatchBaselineIdentityTypeDef], "NextToken": str},
    total=False,
)

PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {"PatchGroup": str, "BaselineIdentity": PatchBaselineIdentityTypeDef},
    total=False,
)

DescribePatchGroupsResultTypeDef = TypedDict(
    "DescribePatchGroupsResultTypeDef",
    {"Mappings": List[PatchGroupPatchBaselineMappingTypeDef], "NextToken": str},
    total=False,
)

SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef", {"S3OutputUrl": str, "CloudWatchOutputUrl": str}, total=False
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": SessionManagerOutputUrlTypeDef,
    },
    total=False,
)

DescribeSessionsResponseTypeDef = TypedDict(
    "DescribeSessionsResponseTypeDef",
    {"Sessions": List[SessionTypeDef], "NextToken": str},
    total=False,
)

DocumentFilterTypeDef = TypedDict(
    "DocumentFilterTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"], "value": str},
)

DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

_RequiredInventoryResultItemTypeDef = TypedDict(
    "_RequiredInventoryResultItemTypeDef",
    {"TypeName": str, "SchemaVersion": str, "Content": List[Dict[str, str]]},
)
_OptionalInventoryResultItemTypeDef = TypedDict(
    "_OptionalInventoryResultItemTypeDef", {"CaptureTime": str, "ContentHash": str}, total=False
)


class InventoryResultItemTypeDef(
    _RequiredInventoryResultItemTypeDef, _OptionalInventoryResultItemTypeDef
):
    pass


InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {"Id": str, "Data": Dict[str, InventoryResultItemTypeDef]},
    total=False,
)

GetInventoryResultTypeDef = TypedDict(
    "GetInventoryResultTypeDef",
    {"Entities": List[InventoryResultEntityTypeDef], "NextToken": str},
    total=False,
)

InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef", {"Name": str, "DataType": Literal["string", "number"]}
)

_RequiredInventoryItemSchemaTypeDef = TypedDict(
    "_RequiredInventoryItemSchemaTypeDef",
    {"TypeName": str, "Attributes": List[InventoryItemAttributeTypeDef]},
)
_OptionalInventoryItemSchemaTypeDef = TypedDict(
    "_OptionalInventoryItemSchemaTypeDef", {"Version": str, "DisplayName": str}, total=False
)


class InventoryItemSchemaTypeDef(
    _RequiredInventoryItemSchemaTypeDef, _OptionalInventoryItemSchemaTypeDef
):
    pass


GetInventorySchemaResultTypeDef = TypedDict(
    "GetInventorySchemaResultTypeDef",
    {"Schemas": List[InventoryItemSchemaTypeDef], "NextToken": str},
    total=False,
)

ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ParameterInlinePolicyTypeDef],
    },
    total=False,
)

GetParameterHistoryResultTypeDef = TypedDict(
    "GetParameterHistoryResultTypeDef",
    {"Parameters": List[ParameterHistoryTypeDef], "NextToken": str},
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

GetParametersByPathResultTypeDef = TypedDict(
    "GetParametersByPathResultTypeDef",
    {"Parameters": List[ParameterTypeDef], "NextToken": str},
    total=False,
)

InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ],
        "valueSet": List[str],
    },
)

InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef", {"Key": str, "Values": List[str]}
)

InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"],
    },
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef", {"Key": str, "Values": List[str]}
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {"Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"]},
    total=False,
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef", {"Name": str, "Filters": List[InventoryFilterTypeDef]}
)

InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": str,
        "Aggregators": List["InventoryAggregatorTypeDef"],
        "Groups": List[InventoryGroupTypeDef],
    },
    total=False,
)

S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef", {"S3Location": S3OutputLocationTypeDef}, total=False
)

AssociationVersionInfoTypeDef = TypedDict(
    "AssociationVersionInfoTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List[TargetTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": InstanceAssociationOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ListAssociationVersionsResultTypeDef = TypedDict(
    "ListAssociationVersionsResultTypeDef",
    {"AssociationVersions": List[AssociationVersionInfoTypeDef], "NextToken": str},
    total=False,
)

AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List[TargetTypeDef],
        "LastExecutionDate": datetime,
        "Overview": AssociationOverviewTypeDef,
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

ListAssociationsResultTypeDef = TypedDict(
    "ListAssociationsResultTypeDef",
    {"Associations": List[AssociationTypeDef], "NextToken": str},
    total=False,
)

CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

CommandPluginTypeDef = TypedDict(
    "CommandPluginTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

CommandInvocationTypeDef = TypedDict(
    "CommandInvocationTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List[CommandPluginTypeDef],
        "ServiceRole": str,
        "NotificationConfig": NotificationConfigTypeDef,
        "CloudWatchOutputConfig": CloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ListCommandInvocationsResultTypeDef = TypedDict(
    "ListCommandInvocationsResultTypeDef",
    {"CommandInvocations": List[CommandInvocationTypeDef], "NextToken": str},
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[TargetTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": NotificationConfigTypeDef,
        "CloudWatchOutputConfig": CloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ListCommandsResultTypeDef = TypedDict(
    "ListCommandsResultTypeDef", {"Commands": List[CommandTypeDef], "NextToken": str}, total=False
)

_RequiredComplianceExecutionSummaryTypeDef = TypedDict(
    "_RequiredComplianceExecutionSummaryTypeDef", {"ExecutionTime": datetime}
)
_OptionalComplianceExecutionSummaryTypeDef = TypedDict(
    "_OptionalComplianceExecutionSummaryTypeDef",
    {"ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ComplianceExecutionSummaryTypeDef(
    _RequiredComplianceExecutionSummaryTypeDef, _OptionalComplianceExecutionSummaryTypeDef
):
    pass


ComplianceItemTypeDef = TypedDict(
    "ComplianceItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": ComplianceExecutionSummaryTypeDef,
        "Details": Dict[str, str],
    },
    total=False,
)

ListComplianceItemsResultTypeDef = TypedDict(
    "ListComplianceItemsResultTypeDef",
    {"ComplianceItems": List[ComplianceItemTypeDef], "NextToken": str},
    total=False,
)

SeveritySummaryTypeDef = TypedDict(
    "SeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

CompliantSummaryTypeDef = TypedDict(
    "CompliantSummaryTypeDef",
    {"CompliantCount": int, "SeveritySummary": SeveritySummaryTypeDef},
    total=False,
)

NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {"NonCompliantCount": int, "SeveritySummary": SeveritySummaryTypeDef},
    total=False,
)

ComplianceSummaryItemTypeDef = TypedDict(
    "ComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": CompliantSummaryTypeDef,
        "NonCompliantSummary": NonCompliantSummaryTypeDef,
    },
    total=False,
)

ListComplianceSummariesResultTypeDef = TypedDict(
    "ListComplianceSummariesResultTypeDef",
    {"ComplianceSummaryItems": List[ComplianceSummaryItemTypeDef], "NextToken": str},
    total=False,
)

DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)

ListDocumentVersionsResultTypeDef = TypedDict(
    "ListDocumentVersionsResultTypeDef",
    {"DocumentVersions": List[DocumentVersionInfoTypeDef], "NextToken": str},
    total=False,
)

_RequiredDocumentRequiresTypeDef = TypedDict("_RequiredDocumentRequiresTypeDef", {"Name": str})
_OptionalDocumentRequiresTypeDef = TypedDict(
    "_OptionalDocumentRequiresTypeDef", {"Version": str}, total=False
)


class DocumentRequiresTypeDef(_RequiredDocumentRequiresTypeDef, _OptionalDocumentRequiresTypeDef):
    pass


DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List[TagTypeDef],
        "Requires": List[DocumentRequiresTypeDef],
    },
    total=False,
)

ListDocumentsResultTypeDef = TypedDict(
    "ListDocumentsResultTypeDef",
    {"DocumentIdentifiers": List[DocumentIdentifierTypeDef], "NextToken": str},
    total=False,
)

ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": ComplianceExecutionSummaryTypeDef,
        "CompliantSummary": CompliantSummaryTypeDef,
        "NonCompliantSummary": NonCompliantSummaryTypeDef,
    },
    total=False,
)

ListResourceComplianceSummariesResultTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultTypeDef",
    {
        "ResourceComplianceSummaryItems": List[ResourceComplianceSummaryItemTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredResourceDataSyncS3DestinationTypeDef",
    {"BucketName": str, "SyncFormat": Literal["JsonSerDe"], "Region": str},
)
_OptionalResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalResourceDataSyncS3DestinationTypeDef",
    {"Prefix": str, "AWSKMSKeyARN": str},
    total=False,
)


class ResourceDataSyncS3DestinationTypeDef(
    _RequiredResourceDataSyncS3DestinationTypeDef, _OptionalResourceDataSyncS3DestinationTypeDef
):
    pass


ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef", {"OrganizationalUnitId": str}, total=False
)

_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef", {"OrganizationSourceType": str}
)
_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef",
    {"OrganizationalUnits": List[ResourceDataSyncOrganizationalUnitTypeDef]},
    total=False,
)


class ResourceDataSyncAwsOrganizationsSourceTypeDef(
    _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef,
    _OptionalResourceDataSyncAwsOrganizationsSourceTypeDef,
):
    pass


ResourceDataSyncSourceWithStateTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStateTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": ResourceDataSyncAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)

ResourceDataSyncItemTypeDef = TypedDict(
    "ResourceDataSyncItemTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ResourceDataSyncSourceWithStateTypeDef,
        "S3Destination": ResourceDataSyncS3DestinationTypeDef,
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ListResourceDataSyncResultTypeDef = TypedDict(
    "ListResourceDataSyncResultTypeDef",
    {"ResourceDataSyncItems": List[ResourceDataSyncItemTypeDef], "NextToken": str},
    total=False,
)

MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredParameterStringFilterTypeDef = TypedDict(
    "_RequiredParameterStringFilterTypeDef", {"Key": str}
)
_OptionalParameterStringFilterTypeDef = TypedDict(
    "_OptionalParameterStringFilterTypeDef", {"Option": str, "Values": List[str]}, total=False
)


class ParameterStringFilterTypeDef(
    _RequiredParameterStringFilterTypeDef, _OptionalParameterStringFilterTypeDef
):
    pass


ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef", {"Key": Literal["Name", "Type", "KeyId"], "Values": List[str]}
)

PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ResultAttributeTypeDef = TypedDict("ResultAttributeTypeDef", {"TypeName": str})

SessionFilterTypeDef = TypedDict(
    "SessionFilterTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"], "value": str},
)

StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ],
        "Values": List[str],
    },
)
