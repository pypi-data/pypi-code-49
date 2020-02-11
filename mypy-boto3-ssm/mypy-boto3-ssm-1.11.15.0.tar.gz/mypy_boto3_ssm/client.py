"""
Main interface for ssm service client

Usage::

    import boto3
    from mypy_boto3.ssm import SSMClient

    session = boto3.Session()

    client: SSMClient = boto3.client("ssm")
    session_client: SSMClient = session.client("ssm")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ssm.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ssm.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ssm.type_defs import (
    ClientAddTagsToResourceTagsTypeDef,
    ClientCancelMaintenanceWindowExecutionResponseTypeDef,
    ClientCreateActivationResponseTypeDef,
    ClientCreateActivationTagsTypeDef,
    ClientCreateAssociationBatchEntriesTypeDef,
    ClientCreateAssociationBatchResponseTypeDef,
    ClientCreateAssociationOutputLocationTypeDef,
    ClientCreateAssociationResponseTypeDef,
    ClientCreateAssociationTargetsTypeDef,
    ClientCreateDocumentAttachmentsTypeDef,
    ClientCreateDocumentRequiresTypeDef,
    ClientCreateDocumentResponseTypeDef,
    ClientCreateDocumentTagsTypeDef,
    ClientCreateMaintenanceWindowResponseTypeDef,
    ClientCreateMaintenanceWindowTagsTypeDef,
    ClientCreateOpsItemNotificationsTypeDef,
    ClientCreateOpsItemOperationalDataTypeDef,
    ClientCreateOpsItemRelatedOpsItemsTypeDef,
    ClientCreateOpsItemResponseTypeDef,
    ClientCreateOpsItemTagsTypeDef,
    ClientCreatePatchBaselineApprovalRulesTypeDef,
    ClientCreatePatchBaselineGlobalFiltersTypeDef,
    ClientCreatePatchBaselineResponseTypeDef,
    ClientCreatePatchBaselineSourcesTypeDef,
    ClientCreatePatchBaselineTagsTypeDef,
    ClientCreateResourceDataSyncS3DestinationTypeDef,
    ClientCreateResourceDataSyncSyncSourceTypeDef,
    ClientDeleteInventoryResponseTypeDef,
    ClientDeleteMaintenanceWindowResponseTypeDef,
    ClientDeleteParametersResponseTypeDef,
    ClientDeletePatchBaselineResponseTypeDef,
    ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef,
    ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef,
    ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef,
    ClientDescribeActivationsFiltersTypeDef,
    ClientDescribeActivationsResponseTypeDef,
    ClientDescribeAssociationExecutionTargetsFiltersTypeDef,
    ClientDescribeAssociationExecutionTargetsResponseTypeDef,
    ClientDescribeAssociationExecutionsFiltersTypeDef,
    ClientDescribeAssociationExecutionsResponseTypeDef,
    ClientDescribeAssociationResponseTypeDef,
    ClientDescribeAutomationExecutionsFiltersTypeDef,
    ClientDescribeAutomationExecutionsResponseTypeDef,
    ClientDescribeAutomationStepExecutionsFiltersTypeDef,
    ClientDescribeAutomationStepExecutionsResponseTypeDef,
    ClientDescribeAvailablePatchesFiltersTypeDef,
    ClientDescribeAvailablePatchesResponseTypeDef,
    ClientDescribeDocumentPermissionResponseTypeDef,
    ClientDescribeDocumentResponseTypeDef,
    ClientDescribeEffectiveInstanceAssociationsResponseTypeDef,
    ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef,
    ClientDescribeInstanceAssociationsStatusResponseTypeDef,
    ClientDescribeInstanceInformationFiltersTypeDef,
    ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
    ClientDescribeInstanceInformationResponseTypeDef,
    ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
    ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef,
    ClientDescribeInstancePatchStatesResponseTypeDef,
    ClientDescribeInstancePatchesFiltersTypeDef,
    ClientDescribeInstancePatchesResponseTypeDef,
    ClientDescribeInventoryDeletionsResponseTypeDef,
    ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef,
    ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef,
    ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef,
    ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef,
    ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef,
    ClientDescribeMaintenanceWindowExecutionsResponseTypeDef,
    ClientDescribeMaintenanceWindowScheduleFiltersTypeDef,
    ClientDescribeMaintenanceWindowScheduleResponseTypeDef,
    ClientDescribeMaintenanceWindowScheduleTargetsTypeDef,
    ClientDescribeMaintenanceWindowTargetsFiltersTypeDef,
    ClientDescribeMaintenanceWindowTargetsResponseTypeDef,
    ClientDescribeMaintenanceWindowTasksFiltersTypeDef,
    ClientDescribeMaintenanceWindowTasksResponseTypeDef,
    ClientDescribeMaintenanceWindowsFiltersTypeDef,
    ClientDescribeMaintenanceWindowsForTargetResponseTypeDef,
    ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef,
    ClientDescribeMaintenanceWindowsResponseTypeDef,
    ClientDescribeOpsItemsOpsItemFiltersTypeDef,
    ClientDescribeOpsItemsResponseTypeDef,
    ClientDescribeParametersFiltersTypeDef,
    ClientDescribeParametersParameterFiltersTypeDef,
    ClientDescribeParametersResponseTypeDef,
    ClientDescribePatchBaselinesFiltersTypeDef,
    ClientDescribePatchBaselinesResponseTypeDef,
    ClientDescribePatchGroupStateResponseTypeDef,
    ClientDescribePatchGroupsFiltersTypeDef,
    ClientDescribePatchGroupsResponseTypeDef,
    ClientDescribePatchPropertiesResponseTypeDef,
    ClientDescribeSessionsFiltersTypeDef,
    ClientDescribeSessionsResponseTypeDef,
    ClientGetAutomationExecutionResponseTypeDef,
    ClientGetCalendarStateResponseTypeDef,
    ClientGetCommandInvocationResponseTypeDef,
    ClientGetConnectionStatusResponseTypeDef,
    ClientGetDefaultPatchBaselineResponseTypeDef,
    ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef,
    ClientGetDocumentResponseTypeDef,
    ClientGetInventoryAggregatorsTypeDef,
    ClientGetInventoryFiltersTypeDef,
    ClientGetInventoryResponseTypeDef,
    ClientGetInventoryResultAttributesTypeDef,
    ClientGetInventorySchemaResponseTypeDef,
    ClientGetMaintenanceWindowExecutionResponseTypeDef,
    ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef,
    ClientGetMaintenanceWindowExecutionTaskResponseTypeDef,
    ClientGetMaintenanceWindowResponseTypeDef,
    ClientGetMaintenanceWindowTaskResponseTypeDef,
    ClientGetOpsItemResponseTypeDef,
    ClientGetOpsSummaryAggregatorsTypeDef,
    ClientGetOpsSummaryFiltersTypeDef,
    ClientGetOpsSummaryResponseTypeDef,
    ClientGetOpsSummaryResultAttributesTypeDef,
    ClientGetParameterHistoryResponseTypeDef,
    ClientGetParameterResponseTypeDef,
    ClientGetParametersByPathParameterFiltersTypeDef,
    ClientGetParametersByPathResponseTypeDef,
    ClientGetParametersResponseTypeDef,
    ClientGetPatchBaselineForPatchGroupResponseTypeDef,
    ClientGetPatchBaselineResponseTypeDef,
    ClientGetServiceSettingResponseTypeDef,
    ClientLabelParameterVersionResponseTypeDef,
    ClientListAssociationVersionsResponseTypeDef,
    ClientListAssociationsAssociationFilterListTypeDef,
    ClientListAssociationsResponseTypeDef,
    ClientListCommandInvocationsFiltersTypeDef,
    ClientListCommandInvocationsResponseTypeDef,
    ClientListCommandsFiltersTypeDef,
    ClientListCommandsResponseTypeDef,
    ClientListComplianceItemsFiltersTypeDef,
    ClientListComplianceItemsResponseTypeDef,
    ClientListComplianceSummariesFiltersTypeDef,
    ClientListComplianceSummariesResponseTypeDef,
    ClientListDocumentVersionsResponseTypeDef,
    ClientListDocumentsDocumentFilterListTypeDef,
    ClientListDocumentsFiltersTypeDef,
    ClientListDocumentsResponseTypeDef,
    ClientListInventoryEntriesFiltersTypeDef,
    ClientListInventoryEntriesResponseTypeDef,
    ClientListResourceComplianceSummariesFiltersTypeDef,
    ClientListResourceComplianceSummariesResponseTypeDef,
    ClientListResourceDataSyncResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutComplianceItemsExecutionSummaryTypeDef,
    ClientPutComplianceItemsItemsTypeDef,
    ClientPutInventoryItemsTypeDef,
    ClientPutInventoryResponseTypeDef,
    ClientPutParameterResponseTypeDef,
    ClientPutParameterTagsTypeDef,
    ClientRegisterDefaultPatchBaselineResponseTypeDef,
    ClientRegisterPatchBaselineForPatchGroupResponseTypeDef,
    ClientRegisterTargetWithMaintenanceWindowResponseTypeDef,
    ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef,
    ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef,
    ClientRegisterTaskWithMaintenanceWindowResponseTypeDef,
    ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef,
    ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef,
    ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef,
    ClientResetServiceSettingResponseTypeDef,
    ClientResumeSessionResponseTypeDef,
    ClientSendCommandCloudWatchOutputConfigTypeDef,
    ClientSendCommandNotificationConfigTypeDef,
    ClientSendCommandResponseTypeDef,
    ClientSendCommandTargetsTypeDef,
    ClientStartAutomationExecutionResponseTypeDef,
    ClientStartAutomationExecutionTagsTypeDef,
    ClientStartAutomationExecutionTargetLocationsTypeDef,
    ClientStartAutomationExecutionTargetsTypeDef,
    ClientStartSessionResponseTypeDef,
    ClientTerminateSessionResponseTypeDef,
    ClientUpdateAssociationOutputLocationTypeDef,
    ClientUpdateAssociationResponseTypeDef,
    ClientUpdateAssociationStatusAssociationStatusTypeDef,
    ClientUpdateAssociationStatusResponseTypeDef,
    ClientUpdateAssociationTargetsTypeDef,
    ClientUpdateDocumentAttachmentsTypeDef,
    ClientUpdateDocumentDefaultVersionResponseTypeDef,
    ClientUpdateDocumentResponseTypeDef,
    ClientUpdateMaintenanceWindowResponseTypeDef,
    ClientUpdateMaintenanceWindowTargetResponseTypeDef,
    ClientUpdateMaintenanceWindowTargetTargetsTypeDef,
    ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef,
    ClientUpdateMaintenanceWindowTaskResponseTypeDef,
    ClientUpdateMaintenanceWindowTaskTargetsTypeDef,
    ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef,
    ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef,
    ClientUpdateOpsItemNotificationsTypeDef,
    ClientUpdateOpsItemOperationalDataTypeDef,
    ClientUpdateOpsItemRelatedOpsItemsTypeDef,
    ClientUpdatePatchBaselineApprovalRulesTypeDef,
    ClientUpdatePatchBaselineGlobalFiltersTypeDef,
    ClientUpdatePatchBaselineResponseTypeDef,
    ClientUpdatePatchBaselineSourcesTypeDef,
    ClientUpdateResourceDataSyncSyncSourceTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSMClient",)


class SSMClient:
    """
    [SSM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags_to_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
        Tags: List[ClientAddTagsToResourceTagsTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.can_paginate)
        """

    def cancel_command(self, CommandId: str, InstanceIds: List[str] = None) -> Dict[str, Any]:
        """
        [Client.cancel_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.cancel_command)
        """

    def cancel_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> ClientCancelMaintenanceWindowExecutionResponseTypeDef:
        """
        [Client.cancel_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.cancel_maintenance_window_execution)
        """

    def create_activation(
        self,
        IamRole: str,
        Description: str = None,
        DefaultInstanceName: str = None,
        RegistrationLimit: int = None,
        ExpirationDate: datetime = None,
        Tags: List[ClientCreateActivationTagsTypeDef] = None,
    ) -> ClientCreateActivationResponseTypeDef:
        """
        [Client.create_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_activation)
        """

    def create_association(
        self,
        Name: str,
        DocumentVersion: str = None,
        InstanceId: str = None,
        Parameters: Dict[str, List[str]] = None,
        Targets: List[ClientCreateAssociationTargetsTypeDef] = None,
        ScheduleExpression: str = None,
        OutputLocation: ClientCreateAssociationOutputLocationTypeDef = None,
        AssociationName: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"] = None,
    ) -> ClientCreateAssociationResponseTypeDef:
        """
        [Client.create_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_association)
        """

    def create_association_batch(
        self, Entries: List[ClientCreateAssociationBatchEntriesTypeDef]
    ) -> ClientCreateAssociationBatchResponseTypeDef:
        """
        [Client.create_association_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_association_batch)
        """

    def create_document(
        self,
        Content: str,
        Name: str,
        Requires: List[ClientCreateDocumentRequiresTypeDef] = None,
        Attachments: List[ClientCreateDocumentAttachmentsTypeDef] = None,
        VersionName: str = None,
        DocumentType: Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ] = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
        TargetType: str = None,
        Tags: List[ClientCreateDocumentTagsTypeDef] = None,
    ) -> ClientCreateDocumentResponseTypeDef:
        """
        [Client.create_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_document)
        """

    def create_maintenance_window(
        self,
        Name: str,
        Schedule: str,
        Duration: int,
        Cutoff: int,
        AllowUnassociatedTargets: bool,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        ScheduleTimezone: str = None,
        ClientToken: str = None,
        Tags: List[ClientCreateMaintenanceWindowTagsTypeDef] = None,
    ) -> ClientCreateMaintenanceWindowResponseTypeDef:
        """
        [Client.create_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_maintenance_window)
        """

    def create_ops_item(
        self,
        Description: str,
        Source: str,
        Title: str,
        OperationalData: Dict[str, ClientCreateOpsItemOperationalDataTypeDef] = None,
        Notifications: List[ClientCreateOpsItemNotificationsTypeDef] = None,
        Priority: int = None,
        RelatedOpsItems: List[ClientCreateOpsItemRelatedOpsItemsTypeDef] = None,
        Tags: List[ClientCreateOpsItemTagsTypeDef] = None,
        Category: str = None,
        Severity: str = None,
    ) -> ClientCreateOpsItemResponseTypeDef:
        """
        [Client.create_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_ops_item)
        """

    def create_patch_baseline(
        self,
        Name: str,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ] = None,
        GlobalFilters: ClientCreatePatchBaselineGlobalFiltersTypeDef = None,
        ApprovalRules: ClientCreatePatchBaselineApprovalRulesTypeDef = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ] = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = None,
        Description: str = None,
        Sources: List[ClientCreatePatchBaselineSourcesTypeDef] = None,
        ClientToken: str = None,
        Tags: List[ClientCreatePatchBaselineTagsTypeDef] = None,
    ) -> ClientCreatePatchBaselineResponseTypeDef:
        """
        [Client.create_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_patch_baseline)
        """

    def create_resource_data_sync(
        self,
        SyncName: str,
        S3Destination: ClientCreateResourceDataSyncS3DestinationTypeDef = None,
        SyncType: str = None,
        SyncSource: ClientCreateResourceDataSyncSyncSourceTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.create_resource_data_sync)
        """

    def delete_activation(self, ActivationId: str) -> Dict[str, Any]:
        """
        [Client.delete_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_activation)
        """

    def delete_association(
        self, Name: str = None, InstanceId: str = None, AssociationId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_association)
        """

    def delete_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None, Force: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_document)
        """

    def delete_inventory(
        self,
        TypeName: str,
        SchemaDeleteOption: Literal["DisableSchema", "DeleteSchema"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ClientDeleteInventoryResponseTypeDef:
        """
        [Client.delete_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_inventory)
        """

    def delete_maintenance_window(
        self, WindowId: str
    ) -> ClientDeleteMaintenanceWindowResponseTypeDef:
        """
        [Client.delete_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_maintenance_window)
        """

    def delete_parameter(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_parameter)
        """

    def delete_parameters(self, Names: List[str]) -> ClientDeleteParametersResponseTypeDef:
        """
        [Client.delete_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_parameters)
        """

    def delete_patch_baseline(self, BaselineId: str) -> ClientDeletePatchBaselineResponseTypeDef:
        """
        [Client.delete_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_patch_baseline)
        """

    def delete_resource_data_sync(self, SyncName: str, SyncType: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.delete_resource_data_sync)
        """

    def deregister_managed_instance(self, InstanceId: str) -> Dict[str, Any]:
        """
        [Client.deregister_managed_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.deregister_managed_instance)
        """

    def deregister_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef:
        """
        [Client.deregister_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.deregister_patch_baseline_for_patch_group)
        """

    def deregister_target_from_maintenance_window(
        self, WindowId: str, WindowTargetId: str, Safe: bool = None
    ) -> ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef:
        """
        [Client.deregister_target_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.deregister_target_from_maintenance_window)
        """

    def deregister_task_from_maintenance_window(
        self, WindowId: str, WindowTaskId: str
    ) -> ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef:
        """
        [Client.deregister_task_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.deregister_task_from_maintenance_window)
        """

    def describe_activations(
        self,
        Filters: List[ClientDescribeActivationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeActivationsResponseTypeDef:
        """
        [Client.describe_activations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_activations)
        """

    def describe_association(
        self,
        Name: str = None,
        InstanceId: str = None,
        AssociationId: str = None,
        AssociationVersion: str = None,
    ) -> ClientDescribeAssociationResponseTypeDef:
        """
        [Client.describe_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_association)
        """

    def describe_association_execution_targets(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[ClientDescribeAssociationExecutionTargetsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAssociationExecutionTargetsResponseTypeDef:
        """
        [Client.describe_association_execution_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_association_execution_targets)
        """

    def describe_association_executions(
        self,
        AssociationId: str,
        Filters: List[ClientDescribeAssociationExecutionsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAssociationExecutionsResponseTypeDef:
        """
        [Client.describe_association_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_association_executions)
        """

    def describe_automation_executions(
        self,
        Filters: List[ClientDescribeAutomationExecutionsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAutomationExecutionsResponseTypeDef:
        """
        [Client.describe_automation_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_automation_executions)
        """

    def describe_automation_step_executions(
        self,
        AutomationExecutionId: str,
        Filters: List[ClientDescribeAutomationStepExecutionsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ReverseOrder: bool = None,
    ) -> ClientDescribeAutomationStepExecutionsResponseTypeDef:
        """
        [Client.describe_automation_step_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_automation_step_executions)
        """

    def describe_available_patches(
        self,
        Filters: List[ClientDescribeAvailablePatchesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAvailablePatchesResponseTypeDef:
        """
        [Client.describe_available_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_available_patches)
        """

    def describe_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None
    ) -> ClientDescribeDocumentResponseTypeDef:
        """
        [Client.describe_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_document)
        """

    def describe_document_permission(
        self, Name: str, PermissionType: str
    ) -> ClientDescribeDocumentPermissionResponseTypeDef:
        """
        [Client.describe_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_document_permission)
        """

    def describe_effective_instance_associations(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeEffectiveInstanceAssociationsResponseTypeDef:
        """
        [Client.describe_effective_instance_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_effective_instance_associations)
        """

    def describe_effective_patches_for_patch_baseline(
        self, BaselineId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef:
        """
        [Client.describe_effective_patches_for_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_effective_patches_for_patch_baseline)
        """

    def describe_instance_associations_status(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeInstanceAssociationsStatusResponseTypeDef:
        """
        [Client.describe_instance_associations_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_instance_associations_status)
        """

    def describe_instance_information(
        self,
        InstanceInformationFilterList: List[
            ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef
        ] = None,
        Filters: List[ClientDescribeInstanceInformationFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeInstanceInformationResponseTypeDef:
        """
        [Client.describe_instance_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_instance_information)
        """

    def describe_instance_patch_states(
        self, InstanceIds: List[str], NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeInstancePatchStatesResponseTypeDef:
        """
        [Client.describe_instance_patch_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_instance_patch_states)
        """

    def describe_instance_patch_states_for_patch_group(
        self,
        PatchGroup: str,
        Filters: List[ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef:
        """
        [Client.describe_instance_patch_states_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_instance_patch_states_for_patch_group)
        """

    def describe_instance_patches(
        self,
        InstanceId: str,
        Filters: List[ClientDescribeInstancePatchesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeInstancePatchesResponseTypeDef:
        """
        [Client.describe_instance_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_instance_patches)
        """

    def describe_inventory_deletions(
        self, DeletionId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeInventoryDeletionsResponseTypeDef:
        """
        [Client.describe_inventory_deletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_inventory_deletions)
        """

    def describe_maintenance_window_execution_task_invocations(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef:
        """
        [Client.describe_maintenance_window_execution_task_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_task_invocations)
        """

    def describe_maintenance_window_execution_tasks(
        self,
        WindowExecutionId: str,
        Filters: List[ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef:
        """
        [Client.describe_maintenance_window_execution_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_tasks)
        """

    def describe_maintenance_window_executions(
        self,
        WindowId: str,
        Filters: List[ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowExecutionsResponseTypeDef:
        """
        [Client.describe_maintenance_window_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_window_executions)
        """

    def describe_maintenance_window_schedule(
        self,
        WindowId: str = None,
        Targets: List[ClientDescribeMaintenanceWindowScheduleTargetsTypeDef] = None,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"] = None,
        Filters: List[ClientDescribeMaintenanceWindowScheduleFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowScheduleResponseTypeDef:
        """
        [Client.describe_maintenance_window_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_window_schedule)
        """

    def describe_maintenance_window_targets(
        self,
        WindowId: str,
        Filters: List[ClientDescribeMaintenanceWindowTargetsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowTargetsResponseTypeDef:
        """
        [Client.describe_maintenance_window_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_window_targets)
        """

    def describe_maintenance_window_tasks(
        self,
        WindowId: str,
        Filters: List[ClientDescribeMaintenanceWindowTasksFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowTasksResponseTypeDef:
        """
        [Client.describe_maintenance_window_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_window_tasks)
        """

    def describe_maintenance_windows(
        self,
        Filters: List[ClientDescribeMaintenanceWindowsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowsResponseTypeDef:
        """
        [Client.describe_maintenance_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_windows)
        """

    def describe_maintenance_windows_for_target(
        self,
        Targets: List[ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef],
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeMaintenanceWindowsForTargetResponseTypeDef:
        """
        [Client.describe_maintenance_windows_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_maintenance_windows_for_target)
        """

    def describe_ops_items(
        self,
        OpsItemFilters: List[ClientDescribeOpsItemsOpsItemFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeOpsItemsResponseTypeDef:
        """
        [Client.describe_ops_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_ops_items)
        """

    def describe_parameters(
        self,
        Filters: List[ClientDescribeParametersFiltersTypeDef] = None,
        ParameterFilters: List[ClientDescribeParametersParameterFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeParametersResponseTypeDef:
        """
        [Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_parameters)
        """

    def describe_patch_baselines(
        self,
        Filters: List[ClientDescribePatchBaselinesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribePatchBaselinesResponseTypeDef:
        """
        [Client.describe_patch_baselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_patch_baselines)
        """

    def describe_patch_group_state(
        self, PatchGroup: str
    ) -> ClientDescribePatchGroupStateResponseTypeDef:
        """
        [Client.describe_patch_group_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_patch_group_state)
        """

    def describe_patch_groups(
        self,
        MaxResults: int = None,
        Filters: List[ClientDescribePatchGroupsFiltersTypeDef] = None,
        NextToken: str = None,
    ) -> ClientDescribePatchGroupsResponseTypeDef:
        """
        [Client.describe_patch_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_patch_groups)
        """

    def describe_patch_properties(
        self,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        Property: Literal[
            "PRODUCT", "PRODUCT_FAMILY", "CLASSIFICATION", "MSRC_SEVERITY", "PRIORITY", "SEVERITY"
        ],
        PatchSet: Literal["OS", "APPLICATION"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribePatchPropertiesResponseTypeDef:
        """
        [Client.describe_patch_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_patch_properties)
        """

    def describe_sessions(
        self,
        State: Literal["Active", "History"],
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientDescribeSessionsFiltersTypeDef] = None,
    ) -> ClientDescribeSessionsResponseTypeDef:
        """
        [Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.describe_sessions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.generate_presigned_url)
        """

    def get_automation_execution(
        self, AutomationExecutionId: str
    ) -> ClientGetAutomationExecutionResponseTypeDef:
        """
        [Client.get_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_automation_execution)
        """

    def get_calendar_state(
        self, CalendarNames: List[str], AtTime: str = None
    ) -> ClientGetCalendarStateResponseTypeDef:
        """
        [Client.get_calendar_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_calendar_state)
        """

    def get_command_invocation(
        self, CommandId: str, InstanceId: str, PluginName: str = None
    ) -> ClientGetCommandInvocationResponseTypeDef:
        """
        [Client.get_command_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_command_invocation)
        """

    def get_connection_status(self, Target: str) -> ClientGetConnectionStatusResponseTypeDef:
        """
        [Client.get_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_connection_status)
        """

    def get_default_patch_baseline(
        self,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ] = None,
    ) -> ClientGetDefaultPatchBaselineResponseTypeDef:
        """
        [Client.get_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_default_patch_baseline)
        """

    def get_deployable_patch_snapshot_for_instance(
        self, InstanceId: str, SnapshotId: str
    ) -> ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef:
        """
        [Client.get_deployable_patch_snapshot_for_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_deployable_patch_snapshot_for_instance)
        """

    def get_document(
        self,
        Name: str,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
    ) -> ClientGetDocumentResponseTypeDef:
        """
        [Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_document)
        """

    def get_inventory(
        self,
        Filters: List[ClientGetInventoryFiltersTypeDef] = None,
        Aggregators: List[ClientGetInventoryAggregatorsTypeDef] = None,
        ResultAttributes: List[ClientGetInventoryResultAttributesTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetInventoryResponseTypeDef:
        """
        [Client.get_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_inventory)
        """

    def get_inventory_schema(
        self,
        TypeName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Aggregator: bool = None,
        SubType: bool = None,
    ) -> ClientGetInventorySchemaResponseTypeDef:
        """
        [Client.get_inventory_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_inventory_schema)
        """

    def get_maintenance_window(self, WindowId: str) -> ClientGetMaintenanceWindowResponseTypeDef:
        """
        [Client.get_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_maintenance_window)
        """

    def get_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> ClientGetMaintenanceWindowExecutionResponseTypeDef:
        """
        [Client.get_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution)
        """

    def get_maintenance_window_execution_task(
        self, WindowExecutionId: str, TaskId: str
    ) -> ClientGetMaintenanceWindowExecutionTaskResponseTypeDef:
        """
        [Client.get_maintenance_window_execution_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task)
        """

    def get_maintenance_window_execution_task_invocation(
        self, WindowExecutionId: str, TaskId: str, InvocationId: str
    ) -> ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef:
        """
        [Client.get_maintenance_window_execution_task_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task_invocation)
        """

    def get_maintenance_window_task(
        self, WindowId: str, WindowTaskId: str
    ) -> ClientGetMaintenanceWindowTaskResponseTypeDef:
        """
        [Client.get_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_maintenance_window_task)
        """

    def get_ops_item(self, OpsItemId: str) -> ClientGetOpsItemResponseTypeDef:
        """
        [Client.get_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_ops_item)
        """

    def get_ops_summary(
        self,
        SyncName: str = None,
        Filters: List[ClientGetOpsSummaryFiltersTypeDef] = None,
        Aggregators: List[ClientGetOpsSummaryAggregatorsTypeDef] = None,
        ResultAttributes: List[ClientGetOpsSummaryResultAttributesTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetOpsSummaryResponseTypeDef:
        """
        [Client.get_ops_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_ops_summary)
        """

    def get_parameter(
        self, Name: str, WithDecryption: bool = None
    ) -> ClientGetParameterResponseTypeDef:
        """
        [Client.get_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_parameter)
        """

    def get_parameter_history(
        self, Name: str, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetParameterHistoryResponseTypeDef:
        """
        [Client.get_parameter_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_parameter_history)
        """

    def get_parameters(
        self, Names: List[str], WithDecryption: bool = None
    ) -> ClientGetParametersResponseTypeDef:
        """
        [Client.get_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_parameters)
        """

    def get_parameters_by_path(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[ClientGetParametersByPathParameterFiltersTypeDef] = None,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetParametersByPathResponseTypeDef:
        """
        [Client.get_parameters_by_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_parameters_by_path)
        """

    def get_patch_baseline(self, BaselineId: str) -> ClientGetPatchBaselineResponseTypeDef:
        """
        [Client.get_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_patch_baseline)
        """

    def get_patch_baseline_for_patch_group(
        self,
        PatchGroup: str,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ] = None,
    ) -> ClientGetPatchBaselineForPatchGroupResponseTypeDef:
        """
        [Client.get_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_patch_baseline_for_patch_group)
        """

    def get_service_setting(self, SettingId: str) -> ClientGetServiceSettingResponseTypeDef:
        """
        [Client.get_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.get_service_setting)
        """

    def label_parameter_version(
        self, Name: str, Labels: List[str], ParameterVersion: int = None
    ) -> ClientLabelParameterVersionResponseTypeDef:
        """
        [Client.label_parameter_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.label_parameter_version)
        """

    def list_association_versions(
        self, AssociationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAssociationVersionsResponseTypeDef:
        """
        [Client.list_association_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_association_versions)
        """

    def list_associations(
        self,
        AssociationFilterList: List[ClientListAssociationsAssociationFilterListTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListAssociationsResponseTypeDef:
        """
        [Client.list_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_associations)
        """

    def list_command_invocations(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListCommandInvocationsFiltersTypeDef] = None,
        Details: bool = None,
    ) -> ClientListCommandInvocationsResponseTypeDef:
        """
        [Client.list_command_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_command_invocations)
        """

    def list_commands(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListCommandsFiltersTypeDef] = None,
    ) -> ClientListCommandsResponseTypeDef:
        """
        [Client.list_commands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_commands)
        """

    def list_compliance_items(
        self,
        Filters: List[ClientListComplianceItemsFiltersTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListComplianceItemsResponseTypeDef:
        """
        [Client.list_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_compliance_items)
        """

    def list_compliance_summaries(
        self,
        Filters: List[ClientListComplianceSummariesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListComplianceSummariesResponseTypeDef:
        """
        [Client.list_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_compliance_summaries)
        """

    def list_document_versions(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDocumentVersionsResponseTypeDef:
        """
        [Client.list_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_document_versions)
        """

    def list_documents(
        self,
        DocumentFilterList: List[ClientListDocumentsDocumentFilterListTypeDef] = None,
        Filters: List[ClientListDocumentsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListDocumentsResponseTypeDef:
        """
        [Client.list_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_documents)
        """

    def list_inventory_entries(
        self,
        InstanceId: str,
        TypeName: str,
        Filters: List[ClientListInventoryEntriesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListInventoryEntriesResponseTypeDef:
        """
        [Client.list_inventory_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_inventory_entries)
        """

    def list_resource_compliance_summaries(
        self,
        Filters: List[ClientListResourceComplianceSummariesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListResourceComplianceSummariesResponseTypeDef:
        """
        [Client.list_resource_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_resource_compliance_summaries)
        """

    def list_resource_data_sync(
        self, SyncType: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListResourceDataSyncResponseTypeDef:
        """
        [Client.list_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_resource_data_sync)
        """

    def list_tags_for_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.list_tags_for_resource)
        """

    def modify_document_permission(
        self,
        Name: str,
        PermissionType: str,
        AccountIdsToAdd: List[str] = None,
        AccountIdsToRemove: List[str] = None,
        SharedDocumentVersion: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.modify_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.modify_document_permission)
        """

    def put_compliance_items(
        self,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: ClientPutComplianceItemsExecutionSummaryTypeDef,
        Items: List[ClientPutComplianceItemsItemsTypeDef],
        ItemContentHash: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.put_compliance_items)
        """

    def put_inventory(
        self, InstanceId: str, Items: List[ClientPutInventoryItemsTypeDef]
    ) -> ClientPutInventoryResponseTypeDef:
        """
        [Client.put_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.put_inventory)
        """

    def put_parameter(
        self,
        Name: str,
        Value: str,
        Type: Literal["String", "StringList", "SecureString"],
        Description: str = None,
        KeyId: str = None,
        Overwrite: bool = None,
        AllowedPattern: str = None,
        Tags: List[ClientPutParameterTagsTypeDef] = None,
        Tier: Literal["Standard", "Advanced", "Intelligent-Tiering"] = None,
        Policies: str = None,
    ) -> ClientPutParameterResponseTypeDef:
        """
        [Client.put_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.put_parameter)
        """

    def register_default_patch_baseline(
        self, BaselineId: str
    ) -> ClientRegisterDefaultPatchBaselineResponseTypeDef:
        """
        [Client.register_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.register_default_patch_baseline)
        """

    def register_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> ClientRegisterPatchBaselineForPatchGroupResponseTypeDef:
        """
        [Client.register_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.register_patch_baseline_for_patch_group)
        """

    def register_target_with_maintenance_window(
        self,
        WindowId: str,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        Targets: List[ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef],
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> ClientRegisterTargetWithMaintenanceWindowResponseTypeDef:
        """
        [Client.register_target_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.register_target_with_maintenance_window)
        """

    def register_task_with_maintenance_window(
        self,
        WindowId: str,
        Targets: List[ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef],
        TaskArn: str,
        TaskType: Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        MaxConcurrency: str,
        MaxErrors: str,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[
            str, ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef
        ] = None,
        TaskInvocationParameters: ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef = None,
        Priority: int = None,
        LoggingInfo: ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> ClientRegisterTaskWithMaintenanceWindowResponseTypeDef:
        """
        [Client.register_task_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.register_task_with_maintenance_window)
        """

    def remove_tags_from_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
        TagKeys: List[str],
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.remove_tags_from_resource)
        """

    def reset_service_setting(self, SettingId: str) -> ClientResetServiceSettingResponseTypeDef:
        """
        [Client.reset_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.reset_service_setting)
        """

    def resume_session(self, SessionId: str) -> ClientResumeSessionResponseTypeDef:
        """
        [Client.resume_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.resume_session)
        """

    def send_automation_signal(
        self,
        AutomationExecutionId: str,
        SignalType: Literal["Approve", "Reject", "StartStep", "StopStep", "Resume"],
        Payload: Dict[str, List[str]] = None,
    ) -> Dict[str, Any]:
        """
        [Client.send_automation_signal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.send_automation_signal)
        """

    def send_command(
        self,
        DocumentName: str,
        InstanceIds: List[str] = None,
        Targets: List[ClientSendCommandTargetsTypeDef] = None,
        DocumentVersion: str = None,
        DocumentHash: str = None,
        DocumentHashType: Literal["Sha256", "Sha1"] = None,
        TimeoutSeconds: int = None,
        Comment: str = None,
        Parameters: Dict[str, List[str]] = None,
        OutputS3Region: str = None,
        OutputS3BucketName: str = None,
        OutputS3KeyPrefix: str = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        ServiceRoleArn: str = None,
        NotificationConfig: ClientSendCommandNotificationConfigTypeDef = None,
        CloudWatchOutputConfig: ClientSendCommandCloudWatchOutputConfigTypeDef = None,
    ) -> ClientSendCommandResponseTypeDef:
        """
        [Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.send_command)
        """

    def start_associations_once(self, AssociationIds: List[str]) -> Dict[str, Any]:
        """
        [Client.start_associations_once documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.start_associations_once)
        """

    def start_automation_execution(
        self,
        DocumentName: str,
        DocumentVersion: str = None,
        Parameters: Dict[str, List[str]] = None,
        ClientToken: str = None,
        Mode: Literal["Auto", "Interactive"] = None,
        TargetParameterName: str = None,
        Targets: List[ClientStartAutomationExecutionTargetsTypeDef] = None,
        TargetMaps: List[Dict[str, List[str]]] = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        TargetLocations: List[ClientStartAutomationExecutionTargetLocationsTypeDef] = None,
        Tags: List[ClientStartAutomationExecutionTagsTypeDef] = None,
    ) -> ClientStartAutomationExecutionResponseTypeDef:
        """
        [Client.start_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.start_automation_execution)
        """

    def start_session(
        self, Target: str, DocumentName: str = None, Parameters: Dict[str, List[str]] = None
    ) -> ClientStartSessionResponseTypeDef:
        """
        [Client.start_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.start_session)
        """

    def stop_automation_execution(
        self, AutomationExecutionId: str, Type: Literal["Complete", "Cancel"] = None
    ) -> Dict[str, Any]:
        """
        [Client.stop_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.stop_automation_execution)
        """

    def terminate_session(self, SessionId: str) -> ClientTerminateSessionResponseTypeDef:
        """
        [Client.terminate_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.terminate_session)
        """

    def update_association(
        self,
        AssociationId: str,
        Parameters: Dict[str, List[str]] = None,
        DocumentVersion: str = None,
        ScheduleExpression: str = None,
        OutputLocation: ClientUpdateAssociationOutputLocationTypeDef = None,
        Name: str = None,
        Targets: List[ClientUpdateAssociationTargetsTypeDef] = None,
        AssociationName: str = None,
        AssociationVersion: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"] = None,
    ) -> ClientUpdateAssociationResponseTypeDef:
        """
        [Client.update_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_association)
        """

    def update_association_status(
        self,
        Name: str,
        InstanceId: str,
        AssociationStatus: ClientUpdateAssociationStatusAssociationStatusTypeDef,
    ) -> ClientUpdateAssociationStatusResponseTypeDef:
        """
        [Client.update_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_association_status)
        """

    def update_document(
        self,
        Content: str,
        Name: str,
        Attachments: List[ClientUpdateDocumentAttachmentsTypeDef] = None,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
        TargetType: str = None,
    ) -> ClientUpdateDocumentResponseTypeDef:
        """
        [Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_document)
        """

    def update_document_default_version(
        self, Name: str, DocumentVersion: str
    ) -> ClientUpdateDocumentDefaultVersionResponseTypeDef:
        """
        [Client.update_document_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_document_default_version)
        """

    def update_maintenance_window(
        self,
        WindowId: str,
        Name: str = None,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        Schedule: str = None,
        ScheduleTimezone: str = None,
        Duration: int = None,
        Cutoff: int = None,
        AllowUnassociatedTargets: bool = None,
        Enabled: bool = None,
        Replace: bool = None,
    ) -> ClientUpdateMaintenanceWindowResponseTypeDef:
        """
        [Client.update_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_maintenance_window)
        """

    def update_maintenance_window_target(
        self,
        WindowId: str,
        WindowTargetId: str,
        Targets: List[ClientUpdateMaintenanceWindowTargetTargetsTypeDef] = None,
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> ClientUpdateMaintenanceWindowTargetResponseTypeDef:
        """
        [Client.update_maintenance_window_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_maintenance_window_target)
        """

    def update_maintenance_window_task(
        self,
        WindowId: str,
        WindowTaskId: str,
        Targets: List[ClientUpdateMaintenanceWindowTaskTargetsTypeDef] = None,
        TaskArn: str = None,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef] = None,
        TaskInvocationParameters: ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef = None,
        Priority: int = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        LoggingInfo: ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> ClientUpdateMaintenanceWindowTaskResponseTypeDef:
        """
        [Client.update_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_maintenance_window_task)
        """

    def update_managed_instance_role(self, InstanceId: str, IamRole: str) -> Dict[str, Any]:
        """
        [Client.update_managed_instance_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_managed_instance_role)
        """

    def update_ops_item(
        self,
        OpsItemId: str,
        Description: str = None,
        OperationalData: Dict[str, ClientUpdateOpsItemOperationalDataTypeDef] = None,
        OperationalDataToDelete: List[str] = None,
        Notifications: List[ClientUpdateOpsItemNotificationsTypeDef] = None,
        Priority: int = None,
        RelatedOpsItems: List[ClientUpdateOpsItemRelatedOpsItemsTypeDef] = None,
        Status: Literal["Open", "InProgress", "Resolved"] = None,
        Title: str = None,
        Category: str = None,
        Severity: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_ops_item)
        """

    def update_patch_baseline(
        self,
        BaselineId: str,
        Name: str = None,
        GlobalFilters: ClientUpdatePatchBaselineGlobalFiltersTypeDef = None,
        ApprovalRules: ClientUpdatePatchBaselineApprovalRulesTypeDef = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ] = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = None,
        Description: str = None,
        Sources: List[ClientUpdatePatchBaselineSourcesTypeDef] = None,
        Replace: bool = None,
    ) -> ClientUpdatePatchBaselineResponseTypeDef:
        """
        [Client.update_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_patch_baseline)
        """

    def update_resource_data_sync(
        self,
        SyncName: str,
        SyncType: str,
        SyncSource: ClientUpdateResourceDataSyncSyncSourceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_resource_data_sync)
        """

    def update_service_setting(self, SettingId: str, SettingValue: str) -> Dict[str, Any]:
        """
        [Client.update_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Client.update_service_setting)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_activations"]
    ) -> "paginator_scope.DescribeActivationsPaginator":
        """
        [Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_association_execution_targets"]
    ) -> "paginator_scope.DescribeAssociationExecutionTargetsPaginator":
        """
        [Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_association_executions"]
    ) -> "paginator_scope.DescribeAssociationExecutionsPaginator":
        """
        [Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_automation_executions"]
    ) -> "paginator_scope.DescribeAutomationExecutionsPaginator":
        """
        [Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_automation_step_executions"]
    ) -> "paginator_scope.DescribeAutomationStepExecutionsPaginator":
        """
        [Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_available_patches"]
    ) -> "paginator_scope.DescribeAvailablePatchesPaginator":
        """
        [Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_effective_instance_associations"]
    ) -> "paginator_scope.DescribeEffectiveInstanceAssociationsPaginator":
        """
        [Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_effective_patches_for_patch_baseline"]
    ) -> "paginator_scope.DescribeEffectivePatchesForPatchBaselinePaginator":
        """
        [Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_associations_status"]
    ) -> "paginator_scope.DescribeInstanceAssociationsStatusPaginator":
        """
        [Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_information"]
    ) -> "paginator_scope.DescribeInstanceInformationPaginator":
        """
        [Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states"]
    ) -> "paginator_scope.DescribeInstancePatchStatesPaginator":
        """
        [Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states_for_patch_group"]
    ) -> "paginator_scope.DescribeInstancePatchStatesForPatchGroupPaginator":
        """
        [Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patches"]
    ) -> "paginator_scope.DescribeInstancePatchesPaginator":
        """
        [Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_inventory_deletions"]
    ) -> "paginator_scope.DescribeInventoryDeletionsPaginator":
        """
        [Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_task_invocations"]
    ) -> "paginator_scope.DescribeMaintenanceWindowExecutionTaskInvocationsPaginator":
        """
        [Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_tasks"]
    ) -> "paginator_scope.DescribeMaintenanceWindowExecutionTasksPaginator":
        """
        [Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_executions"]
    ) -> "paginator_scope.DescribeMaintenanceWindowExecutionsPaginator":
        """
        [Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_schedule"]
    ) -> "paginator_scope.DescribeMaintenanceWindowSchedulePaginator":
        """
        [Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_targets"]
    ) -> "paginator_scope.DescribeMaintenanceWindowTargetsPaginator":
        """
        [Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_tasks"]
    ) -> "paginator_scope.DescribeMaintenanceWindowTasksPaginator":
        """
        [Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows"]
    ) -> "paginator_scope.DescribeMaintenanceWindowsPaginator":
        """
        [Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows_for_target"]
    ) -> "paginator_scope.DescribeMaintenanceWindowsForTargetPaginator":
        """
        [Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> "paginator_scope.DescribeParametersPaginator":
        """
        [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_baselines"]
    ) -> "paginator_scope.DescribePatchBaselinesPaginator":
        """
        [Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_groups"]
    ) -> "paginator_scope.DescribePatchGroupsPaginator":
        """
        [Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> "paginator_scope.DescribeSessionsPaginator":
        """
        [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_inventory"]
    ) -> "paginator_scope.GetInventoryPaginator":
        """
        [Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.GetInventory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_inventory_schema"]
    ) -> "paginator_scope.GetInventorySchemaPaginator":
        """
        [Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_parameter_history"]
    ) -> "paginator_scope.GetParameterHistoryPaginator":
        """
        [Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_parameters_by_path"]
    ) -> "paginator_scope.GetParametersByPathPaginator":
        """
        [Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_association_versions"]
    ) -> "paginator_scope.ListAssociationVersionsPaginator":
        """
        [Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> "paginator_scope.ListAssociationsPaginator":
        """
        [Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_command_invocations"]
    ) -> "paginator_scope.ListCommandInvocationsPaginator":
        """
        [Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_commands"]
    ) -> "paginator_scope.ListCommandsPaginator":
        """
        [Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListCommands)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_items"]
    ) -> "paginator_scope.ListComplianceItemsPaginator":
        """
        [Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_summaries"]
    ) -> "paginator_scope.ListComplianceSummariesPaginator":
        """
        [Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_versions"]
    ) -> "paginator_scope.ListDocumentVersionsPaginator":
        """
        [Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_documents"]
    ) -> "paginator_scope.ListDocumentsPaginator":
        """
        [Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListDocuments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_compliance_summaries"]
    ) -> "paginator_scope.ListResourceComplianceSummariesPaginator":
        """
        [Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_data_sync"]
    ) -> "paginator_scope.ListResourceDataSyncPaginator":
        """
        [Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    AssociatedInstances: Boto3ClientError
    AssociationAlreadyExists: Boto3ClientError
    AssociationDoesNotExist: Boto3ClientError
    AssociationExecutionDoesNotExist: Boto3ClientError
    AssociationLimitExceeded: Boto3ClientError
    AssociationVersionLimitExceeded: Boto3ClientError
    AutomationDefinitionNotFoundException: Boto3ClientError
    AutomationDefinitionVersionNotFoundException: Boto3ClientError
    AutomationExecutionLimitExceededException: Boto3ClientError
    AutomationExecutionNotFoundException: Boto3ClientError
    AutomationStepNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    ComplianceTypeCountLimitExceededException: Boto3ClientError
    CustomSchemaCountLimitExceededException: Boto3ClientError
    DocumentAlreadyExists: Boto3ClientError
    DocumentLimitExceeded: Boto3ClientError
    DocumentPermissionLimit: Boto3ClientError
    DocumentVersionLimitExceeded: Boto3ClientError
    DoesNotExistException: Boto3ClientError
    DuplicateDocumentContent: Boto3ClientError
    DuplicateDocumentVersionName: Boto3ClientError
    DuplicateInstanceId: Boto3ClientError
    FeatureNotAvailableException: Boto3ClientError
    HierarchyLevelLimitExceededException: Boto3ClientError
    HierarchyTypeMismatchException: Boto3ClientError
    IdempotentParameterMismatch: Boto3ClientError
    IncompatiblePolicyException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidActivation: Boto3ClientError
    InvalidActivationId: Boto3ClientError
    InvalidAggregatorException: Boto3ClientError
    InvalidAllowedPatternException: Boto3ClientError
    InvalidAssociation: Boto3ClientError
    InvalidAssociationVersion: Boto3ClientError
    InvalidAutomationExecutionParametersException: Boto3ClientError
    InvalidAutomationSignalException: Boto3ClientError
    InvalidAutomationStatusUpdateException: Boto3ClientError
    InvalidCommandId: Boto3ClientError
    InvalidDeleteInventoryParametersException: Boto3ClientError
    InvalidDeletionIdException: Boto3ClientError
    InvalidDocument: Boto3ClientError
    InvalidDocumentContent: Boto3ClientError
    InvalidDocumentOperation: Boto3ClientError
    InvalidDocumentSchemaVersion: Boto3ClientError
    InvalidDocumentType: Boto3ClientError
    InvalidDocumentVersion: Boto3ClientError
    InvalidFilter: Boto3ClientError
    InvalidFilterKey: Boto3ClientError
    InvalidFilterOption: Boto3ClientError
    InvalidFilterValue: Boto3ClientError
    InvalidInstanceId: Boto3ClientError
    InvalidInstanceInformationFilterValue: Boto3ClientError
    InvalidInventoryGroupException: Boto3ClientError
    InvalidInventoryItemContextException: Boto3ClientError
    InvalidInventoryRequestException: Boto3ClientError
    InvalidItemContentException: Boto3ClientError
    InvalidKeyId: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    InvalidNotificationConfig: Boto3ClientError
    InvalidOptionException: Boto3ClientError
    InvalidOutputFolder: Boto3ClientError
    InvalidOutputLocation: Boto3ClientError
    InvalidParameters: Boto3ClientError
    InvalidPermissionType: Boto3ClientError
    InvalidPluginName: Boto3ClientError
    InvalidPolicyAttributeException: Boto3ClientError
    InvalidPolicyTypeException: Boto3ClientError
    InvalidResourceId: Boto3ClientError
    InvalidResourceType: Boto3ClientError
    InvalidResultAttributeException: Boto3ClientError
    InvalidRole: Boto3ClientError
    InvalidSchedule: Boto3ClientError
    InvalidTarget: Boto3ClientError
    InvalidTypeNameException: Boto3ClientError
    InvalidUpdate: Boto3ClientError
    InvocationDoesNotExist: Boto3ClientError
    ItemContentMismatchException: Boto3ClientError
    ItemSizeLimitExceededException: Boto3ClientError
    MaxDocumentSizeExceeded: Boto3ClientError
    OpsItemAlreadyExistsException: Boto3ClientError
    OpsItemInvalidParameterException: Boto3ClientError
    OpsItemLimitExceededException: Boto3ClientError
    OpsItemNotFoundException: Boto3ClientError
    ParameterAlreadyExists: Boto3ClientError
    ParameterLimitExceeded: Boto3ClientError
    ParameterMaxVersionLimitExceeded: Boto3ClientError
    ParameterNotFound: Boto3ClientError
    ParameterPatternMismatchException: Boto3ClientError
    ParameterVersionLabelLimitExceeded: Boto3ClientError
    ParameterVersionNotFound: Boto3ClientError
    PoliciesLimitExceededException: Boto3ClientError
    ResourceDataSyncAlreadyExistsException: Boto3ClientError
    ResourceDataSyncConflictException: Boto3ClientError
    ResourceDataSyncCountExceededException: Boto3ClientError
    ResourceDataSyncInvalidConfigurationException: Boto3ClientError
    ResourceDataSyncNotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServiceSettingNotFound: Boto3ClientError
    StatusUnchanged: Boto3ClientError
    SubTypeCountLimitExceededException: Boto3ClientError
    TargetInUseException: Boto3ClientError
    TargetNotConnected: Boto3ClientError
    TooManyTagsError: Boto3ClientError
    TooManyUpdates: Boto3ClientError
    TotalSizeLimitExceededException: Boto3ClientError
    UnsupportedCalendarException: Boto3ClientError
    UnsupportedFeatureRequiredException: Boto3ClientError
    UnsupportedInventoryItemContextException: Boto3ClientError
    UnsupportedInventorySchemaVersionException: Boto3ClientError
    UnsupportedOperatingSystem: Boto3ClientError
    UnsupportedParameterType: Boto3ClientError
    UnsupportedPlatformType: Boto3ClientError
