"""
Main interface for backup service client

Usage::

    import boto3
    from mypy_boto3.backup import BackupClient

    session = boto3.Session()

    client: BackupClient = boto3.client("backup")
    session_client: BackupClient = session.client("backup")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_backup.client as client_scope
else:
    client_scope = object
from mypy_boto3_backup.type_defs import (
    ClientCreateBackupPlanBackupPlanTypeDef,
    ClientCreateBackupPlanResponseTypeDef,
    ClientCreateBackupSelectionBackupSelectionTypeDef,
    ClientCreateBackupSelectionResponseTypeDef,
    ClientCreateBackupVaultResponseTypeDef,
    ClientDeleteBackupPlanResponseTypeDef,
    ClientDescribeBackupJobResponseTypeDef,
    ClientDescribeBackupVaultResponseTypeDef,
    ClientDescribeCopyJobResponseTypeDef,
    ClientDescribeProtectedResourceResponseTypeDef,
    ClientDescribeRecoveryPointResponseTypeDef,
    ClientDescribeRestoreJobResponseTypeDef,
    ClientExportBackupPlanTemplateResponseTypeDef,
    ClientGetBackupPlanFromJsonResponseTypeDef,
    ClientGetBackupPlanFromTemplateResponseTypeDef,
    ClientGetBackupPlanResponseTypeDef,
    ClientGetBackupSelectionResponseTypeDef,
    ClientGetBackupVaultAccessPolicyResponseTypeDef,
    ClientGetBackupVaultNotificationsResponseTypeDef,
    ClientGetRecoveryPointRestoreMetadataResponseTypeDef,
    ClientGetSupportedResourceTypesResponseTypeDef,
    ClientListBackupJobsResponseTypeDef,
    ClientListBackupPlanTemplatesResponseTypeDef,
    ClientListBackupPlanVersionsResponseTypeDef,
    ClientListBackupPlansResponseTypeDef,
    ClientListBackupSelectionsResponseTypeDef,
    ClientListBackupVaultsResponseTypeDef,
    ClientListCopyJobsResponseTypeDef,
    ClientListProtectedResourcesResponseTypeDef,
    ClientListRecoveryPointsByBackupVaultResponseTypeDef,
    ClientListRecoveryPointsByResourceResponseTypeDef,
    ClientListRestoreJobsResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientStartBackupJobLifecycleTypeDef,
    ClientStartBackupJobResponseTypeDef,
    ClientStartCopyJobLifecycleTypeDef,
    ClientStartCopyJobResponseTypeDef,
    ClientStartRestoreJobResponseTypeDef,
    ClientUpdateBackupPlanBackupPlanTypeDef,
    ClientUpdateBackupPlanResponseTypeDef,
    ClientUpdateRecoveryPointLifecycleLifecycleTypeDef,
    ClientUpdateRecoveryPointLifecycleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BackupClient",)


class BackupClient:
    """
    [Backup.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.can_paginate)
        """

    def create_backup_plan(
        self,
        BackupPlan: ClientCreateBackupPlanBackupPlanTypeDef,
        BackupPlanTags: Dict[str, str] = None,
        CreatorRequestId: str = None,
    ) -> ClientCreateBackupPlanResponseTypeDef:
        """
        [Client.create_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.create_backup_plan)
        """

    def create_backup_selection(
        self,
        BackupPlanId: str,
        BackupSelection: ClientCreateBackupSelectionBackupSelectionTypeDef,
        CreatorRequestId: str = None,
    ) -> ClientCreateBackupSelectionResponseTypeDef:
        """
        [Client.create_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.create_backup_selection)
        """

    def create_backup_vault(
        self,
        BackupVaultName: str,
        BackupVaultTags: Dict[str, str] = None,
        EncryptionKeyArn: str = None,
        CreatorRequestId: str = None,
    ) -> ClientCreateBackupVaultResponseTypeDef:
        """
        [Client.create_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.create_backup_vault)
        """

    def delete_backup_plan(self, BackupPlanId: str) -> ClientDeleteBackupPlanResponseTypeDef:
        """
        [Client.delete_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.delete_backup_plan)
        """

    def delete_backup_selection(self, BackupPlanId: str, SelectionId: str) -> None:
        """
        [Client.delete_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.delete_backup_selection)
        """

    def delete_backup_vault(self, BackupVaultName: str) -> None:
        """
        [Client.delete_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.delete_backup_vault)
        """

    def delete_backup_vault_access_policy(self, BackupVaultName: str) -> None:
        """
        [Client.delete_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)
        """

    def delete_backup_vault_notifications(self, BackupVaultName: str) -> None:
        """
        [Client.delete_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)
        """

    def delete_recovery_point(self, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        [Client.delete_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.delete_recovery_point)
        """

    def describe_backup_job(self, BackupJobId: str) -> ClientDescribeBackupJobResponseTypeDef:
        """
        [Client.describe_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.describe_backup_job)
        """

    def describe_backup_vault(
        self, BackupVaultName: str
    ) -> ClientDescribeBackupVaultResponseTypeDef:
        """
        [Client.describe_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.describe_backup_vault)
        """

    def describe_copy_job(self, CopyJobId: str) -> ClientDescribeCopyJobResponseTypeDef:
        """
        [Client.describe_copy_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.describe_copy_job)
        """

    def describe_protected_resource(
        self, ResourceArn: str
    ) -> ClientDescribeProtectedResourceResponseTypeDef:
        """
        [Client.describe_protected_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.describe_protected_resource)
        """

    def describe_recovery_point(
        self, BackupVaultName: str, RecoveryPointArn: str
    ) -> ClientDescribeRecoveryPointResponseTypeDef:
        """
        [Client.describe_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.describe_recovery_point)
        """

    def describe_restore_job(self, RestoreJobId: str) -> ClientDescribeRestoreJobResponseTypeDef:
        """
        [Client.describe_restore_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.describe_restore_job)
        """

    def export_backup_plan_template(
        self, BackupPlanId: str
    ) -> ClientExportBackupPlanTemplateResponseTypeDef:
        """
        [Client.export_backup_plan_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.export_backup_plan_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.generate_presigned_url)
        """

    def get_backup_plan(
        self, BackupPlanId: str, VersionId: str = None
    ) -> ClientGetBackupPlanResponseTypeDef:
        """
        [Client.get_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_backup_plan)
        """

    def get_backup_plan_from_json(
        self, BackupPlanTemplateJson: str
    ) -> ClientGetBackupPlanFromJsonResponseTypeDef:
        """
        [Client.get_backup_plan_from_json documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)
        """

    def get_backup_plan_from_template(
        self, BackupPlanTemplateId: str
    ) -> ClientGetBackupPlanFromTemplateResponseTypeDef:
        """
        [Client.get_backup_plan_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)
        """

    def get_backup_selection(
        self, BackupPlanId: str, SelectionId: str
    ) -> ClientGetBackupSelectionResponseTypeDef:
        """
        [Client.get_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_backup_selection)
        """

    def get_backup_vault_access_policy(
        self, BackupVaultName: str
    ) -> ClientGetBackupVaultAccessPolicyResponseTypeDef:
        """
        [Client.get_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)
        """

    def get_backup_vault_notifications(
        self, BackupVaultName: str
    ) -> ClientGetBackupVaultNotificationsResponseTypeDef:
        """
        [Client.get_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)
        """

    def get_recovery_point_restore_metadata(
        self, BackupVaultName: str, RecoveryPointArn: str
    ) -> ClientGetRecoveryPointRestoreMetadataResponseTypeDef:
        """
        [Client.get_recovery_point_restore_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)
        """

    def get_supported_resource_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetSupportedResourceTypesResponseTypeDef:
        """
        [Client.get_supported_resource_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.get_supported_resource_types)
        """

    def list_backup_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByState: Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ] = None,
        ByBackupVaultName: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
        ByResourceType: str = None,
    ) -> ClientListBackupJobsResponseTypeDef:
        """
        [Client.list_backup_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_backup_jobs)
        """

    def list_backup_plan_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListBackupPlanTemplatesResponseTypeDef:
        """
        [Client.list_backup_plan_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_backup_plan_templates)
        """

    def list_backup_plan_versions(
        self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListBackupPlanVersionsResponseTypeDef:
        """
        [Client.list_backup_plan_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_backup_plan_versions)
        """

    def list_backup_plans(
        self, NextToken: str = None, MaxResults: int = None, IncludeDeleted: bool = None
    ) -> ClientListBackupPlansResponseTypeDef:
        """
        [Client.list_backup_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_backup_plans)
        """

    def list_backup_selections(
        self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListBackupSelectionsResponseTypeDef:
        """
        [Client.list_backup_selections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_backup_selections)
        """

    def list_backup_vaults(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListBackupVaultsResponseTypeDef:
        """
        [Client.list_backup_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_backup_vaults)
        """

    def list_copy_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByState: Literal["CREATED", "RUNNING", "COMPLETED", "FAILED"] = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
        ByResourceType: str = None,
        ByDestinationVaultArn: str = None,
    ) -> ClientListCopyJobsResponseTypeDef:
        """
        [Client.list_copy_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_copy_jobs)
        """

    def list_protected_resources(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListProtectedResourcesResponseTypeDef:
        """
        [Client.list_protected_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_protected_resources)
        """

    def list_recovery_points_by_backup_vault(
        self,
        BackupVaultName: str,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByResourceType: str = None,
        ByBackupPlanId: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
    ) -> ClientListRecoveryPointsByBackupVaultResponseTypeDef:
        """
        [Client.list_recovery_points_by_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)
        """

    def list_recovery_points_by_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListRecoveryPointsByResourceResponseTypeDef:
        """
        [Client.list_recovery_points_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)
        """

    def list_restore_jobs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListRestoreJobsResponseTypeDef:
        """
        [Client.list_restore_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_restore_jobs)
        """

    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.list_tags)
        """

    def put_backup_vault_access_policy(self, BackupVaultName: str, Policy: str = None) -> None:
        """
        [Client.put_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)
        """

    def put_backup_vault_notifications(
        self,
        BackupVaultName: str,
        SNSTopicArn: str,
        BackupVaultEvents: List[
            Literal[
                "BACKUP_JOB_STARTED",
                "BACKUP_JOB_COMPLETED",
                "BACKUP_JOB_SUCCESSFUL",
                "BACKUP_JOB_FAILED",
                "BACKUP_JOB_EXPIRED",
                "RESTORE_JOB_STARTED",
                "RESTORE_JOB_COMPLETED",
                "RESTORE_JOB_SUCCESSFUL",
                "RESTORE_JOB_FAILED",
                "COPY_JOB_STARTED",
                "COPY_JOB_SUCCESSFUL",
                "COPY_JOB_FAILED",
                "RECOVERY_POINT_MODIFIED",
                "BACKUP_PLAN_CREATED",
                "BACKUP_PLAN_MODIFIED",
            ]
        ],
    ) -> None:
        """
        [Client.put_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)
        """

    def start_backup_job(
        self,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        StartWindowMinutes: int = None,
        CompleteWindowMinutes: int = None,
        Lifecycle: ClientStartBackupJobLifecycleTypeDef = None,
        RecoveryPointTags: Dict[str, str] = None,
    ) -> ClientStartBackupJobResponseTypeDef:
        """
        [Client.start_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.start_backup_job)
        """

    def start_copy_job(
        self,
        RecoveryPointArn: str,
        SourceBackupVaultName: str,
        DestinationBackupVaultArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        Lifecycle: ClientStartCopyJobLifecycleTypeDef = None,
    ) -> ClientStartCopyJobResponseTypeDef:
        """
        [Client.start_copy_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.start_copy_job)
        """

    def start_restore_job(
        self,
        RecoveryPointArn: str,
        Metadata: Dict[str, str],
        IamRoleArn: str,
        IdempotencyToken: str = None,
        ResourceType: str = None,
    ) -> ClientStartRestoreJobResponseTypeDef:
        """
        [Client.start_restore_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.start_restore_job)
        """

    def stop_backup_job(self, BackupJobId: str) -> None:
        """
        [Client.stop_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.stop_backup_job)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeyList: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.untag_resource)
        """

    def update_backup_plan(
        self, BackupPlanId: str, BackupPlan: ClientUpdateBackupPlanBackupPlanTypeDef
    ) -> ClientUpdateBackupPlanResponseTypeDef:
        """
        [Client.update_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.update_backup_plan)
        """

    def update_recovery_point_lifecycle(
        self,
        BackupVaultName: str,
        RecoveryPointArn: str,
        Lifecycle: ClientUpdateRecoveryPointLifecycleLifecycleTypeDef = None,
    ) -> ClientUpdateRecoveryPointLifecycleResponseTypeDef:
        """
        [Client.update_recovery_point_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyFailureException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MissingParameterValueException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
