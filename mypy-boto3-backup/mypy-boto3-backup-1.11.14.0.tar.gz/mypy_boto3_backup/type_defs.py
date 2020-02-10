"""
Main interface for backup service type definitions.

Usage::

    from mypy_boto3.backup.type_defs import ClientCreateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef

    data: ClientCreateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef = {...}
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
    "ClientCreateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef",
    "ClientCreateBackupPlanBackupPlanRulesCopyActionsTypeDef",
    "ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef",
    "ClientCreateBackupPlanBackupPlanRulesTypeDef",
    "ClientCreateBackupPlanBackupPlanTypeDef",
    "ClientCreateBackupPlanResponseTypeDef",
    "ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef",
    "ClientCreateBackupSelectionBackupSelectionTypeDef",
    "ClientCreateBackupSelectionResponseTypeDef",
    "ClientCreateBackupVaultResponseTypeDef",
    "ClientDeleteBackupPlanResponseTypeDef",
    "ClientDescribeBackupJobResponseCreatedByTypeDef",
    "ClientDescribeBackupJobResponseTypeDef",
    "ClientDescribeBackupVaultResponseTypeDef",
    "ClientDescribeCopyJobResponseCopyJobCreatedByTypeDef",
    "ClientDescribeCopyJobResponseCopyJobTypeDef",
    "ClientDescribeCopyJobResponseTypeDef",
    "ClientDescribeProtectedResourceResponseTypeDef",
    "ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef",
    "ClientDescribeRecoveryPointResponseCreatedByTypeDef",
    "ClientDescribeRecoveryPointResponseLifecycleTypeDef",
    "ClientDescribeRecoveryPointResponseTypeDef",
    "ClientDescribeRestoreJobResponseTypeDef",
    "ClientExportBackupPlanTemplateResponseTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsLifecycleTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef",
    "ClientGetBackupPlanFromJsonResponseTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsLifecycleTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef",
    "ClientGetBackupPlanFromTemplateResponseTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesCopyActionsLifecycleTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesCopyActionsTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesTypeDef",
    "ClientGetBackupPlanResponseBackupPlanTypeDef",
    "ClientGetBackupPlanResponseTypeDef",
    "ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef",
    "ClientGetBackupSelectionResponseBackupSelectionTypeDef",
    "ClientGetBackupSelectionResponseTypeDef",
    "ClientGetBackupVaultAccessPolicyResponseTypeDef",
    "ClientGetBackupVaultNotificationsResponseTypeDef",
    "ClientGetRecoveryPointRestoreMetadataResponseTypeDef",
    "ClientGetSupportedResourceTypesResponseTypeDef",
    "ClientListBackupJobsResponseBackupJobsCreatedByTypeDef",
    "ClientListBackupJobsResponseBackupJobsTypeDef",
    "ClientListBackupJobsResponseTypeDef",
    "ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef",
    "ClientListBackupPlanTemplatesResponseTypeDef",
    "ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef",
    "ClientListBackupPlanVersionsResponseTypeDef",
    "ClientListBackupPlansResponseBackupPlansListTypeDef",
    "ClientListBackupPlansResponseTypeDef",
    "ClientListBackupSelectionsResponseBackupSelectionsListTypeDef",
    "ClientListBackupSelectionsResponseTypeDef",
    "ClientListBackupVaultsResponseBackupVaultListTypeDef",
    "ClientListBackupVaultsResponseTypeDef",
    "ClientListCopyJobsResponseCopyJobsCreatedByTypeDef",
    "ClientListCopyJobsResponseCopyJobsTypeDef",
    "ClientListCopyJobsResponseTypeDef",
    "ClientListProtectedResourcesResponseResultsTypeDef",
    "ClientListProtectedResourcesResponseTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseTypeDef",
    "ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef",
    "ClientListRecoveryPointsByResourceResponseTypeDef",
    "ClientListRestoreJobsResponseRestoreJobsTypeDef",
    "ClientListRestoreJobsResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientStartBackupJobLifecycleTypeDef",
    "ClientStartBackupJobResponseTypeDef",
    "ClientStartCopyJobLifecycleTypeDef",
    "ClientStartCopyJobResponseTypeDef",
    "ClientStartRestoreJobResponseTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesCopyActionsTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesTypeDef",
    "ClientUpdateBackupPlanBackupPlanTypeDef",
    "ClientUpdateBackupPlanResponseTypeDef",
    "ClientUpdateRecoveryPointLifecycleLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseTypeDef",
)

ClientCreateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef = TypedDict(
    "ClientCreateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientCreateBackupPlanBackupPlanRulesCopyActionsTypeDef = TypedDict(
    "ClientCreateBackupPlanBackupPlanRulesCopyActionsTypeDef",
    {
        "Lifecycle": ClientCreateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef,
        "DestinationBackupVaultArn": str,
    },
    total=False,
)

ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef = TypedDict(
    "ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientCreateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "ClientCreateBackupPlanBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "CopyActions": List[ClientCreateBackupPlanBackupPlanRulesCopyActionsTypeDef],
    },
    total=False,
)

_RequiredClientCreateBackupPlanBackupPlanTypeDef = TypedDict(
    "_RequiredClientCreateBackupPlanBackupPlanTypeDef", {"BackupPlanName": str}
)
_OptionalClientCreateBackupPlanBackupPlanTypeDef = TypedDict(
    "_OptionalClientCreateBackupPlanBackupPlanTypeDef",
    {"Rules": List[ClientCreateBackupPlanBackupPlanRulesTypeDef]},
    total=False,
)


class ClientCreateBackupPlanBackupPlanTypeDef(
    _RequiredClientCreateBackupPlanBackupPlanTypeDef,
    _OptionalClientCreateBackupPlanBackupPlanTypeDef,
):
    pass


ClientCreateBackupPlanResponseTypeDef = TypedDict(
    "ClientCreateBackupPlanResponseTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "CreationDate": datetime, "VersionId": str},
    total=False,
)

ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef = TypedDict(
    "ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef",
    {"ConditionType": str, "ConditionKey": str, "ConditionValue": str},
    total=False,
)

_RequiredClientCreateBackupSelectionBackupSelectionTypeDef = TypedDict(
    "_RequiredClientCreateBackupSelectionBackupSelectionTypeDef", {"SelectionName": str}
)
_OptionalClientCreateBackupSelectionBackupSelectionTypeDef = TypedDict(
    "_OptionalClientCreateBackupSelectionBackupSelectionTypeDef",
    {
        "IamRoleArn": str,
        "Resources": List[str],
        "ListOfTags": List[ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef],
    },
    total=False,
)


class ClientCreateBackupSelectionBackupSelectionTypeDef(
    _RequiredClientCreateBackupSelectionBackupSelectionTypeDef,
    _OptionalClientCreateBackupSelectionBackupSelectionTypeDef,
):
    pass


ClientCreateBackupSelectionResponseTypeDef = TypedDict(
    "ClientCreateBackupSelectionResponseTypeDef",
    {"SelectionId": str, "BackupPlanId": str, "CreationDate": datetime},
    total=False,
)

ClientCreateBackupVaultResponseTypeDef = TypedDict(
    "ClientCreateBackupVaultResponseTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "CreationDate": datetime},
    total=False,
)

ClientDeleteBackupPlanResponseTypeDef = TypedDict(
    "ClientDeleteBackupPlanResponseTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "DeletionDate": datetime, "VersionId": str},
    total=False,
)

ClientDescribeBackupJobResponseCreatedByTypeDef = TypedDict(
    "ClientDescribeBackupJobResponseCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

ClientDescribeBackupJobResponseTypeDef = TypedDict(
    "ClientDescribeBackupJobResponseTypeDef",
    {
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientDescribeBackupJobResponseCreatedByTypeDef,
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
    },
    total=False,
)

ClientDescribeBackupVaultResponseTypeDef = TypedDict(
    "ClientDescribeBackupVaultResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)

ClientDescribeCopyJobResponseCopyJobCreatedByTypeDef = TypedDict(
    "ClientDescribeCopyJobResponseCopyJobCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

ClientDescribeCopyJobResponseCopyJobTypeDef = TypedDict(
    "ClientDescribeCopyJobResponseCopyJobTypeDef",
    {
        "CopyJobId": str,
        "SourceBackupVaultArn": str,
        "SourceRecoveryPointArn": str,
        "DestinationBackupVaultArn": str,
        "DestinationRecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal["CREATED", "RUNNING", "COMPLETED", "FAILED"],
        "StatusMessage": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientDescribeCopyJobResponseCopyJobCreatedByTypeDef,
        "ResourceType": str,
    },
    total=False,
)

ClientDescribeCopyJobResponseTypeDef = TypedDict(
    "ClientDescribeCopyJobResponseTypeDef",
    {"CopyJob": ClientDescribeCopyJobResponseCopyJobTypeDef},
    total=False,
)

ClientDescribeProtectedResourceResponseTypeDef = TypedDict(
    "ClientDescribeProtectedResourceResponseTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)

ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef = TypedDict(
    "ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)

ClientDescribeRecoveryPointResponseCreatedByTypeDef = TypedDict(
    "ClientDescribeRecoveryPointResponseCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

ClientDescribeRecoveryPointResponseLifecycleTypeDef = TypedDict(
    "ClientDescribeRecoveryPointResponseLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientDescribeRecoveryPointResponseTypeDef = TypedDict(
    "ClientDescribeRecoveryPointResponseTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": ClientDescribeRecoveryPointResponseCreatedByTypeDef,
        "IamRoleArn": str,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef,
        "Lifecycle": ClientDescribeRecoveryPointResponseLifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": Literal["WARM", "COLD", "DELETED"],
        "LastRestoreTime": datetime,
    },
    total=False,
)

ClientDescribeRestoreJobResponseTypeDef = TypedDict(
    "ClientDescribeRestoreJobResponseTypeDef",
    {
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal["PENDING", "RUNNING", "COMPLETED", "ABORTED", "FAILED"],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
    },
    total=False,
)

ClientExportBackupPlanTemplateResponseTypeDef = TypedDict(
    "ClientExportBackupPlanTemplateResponseTypeDef", {"BackupPlanTemplateJson": str}, total=False
)

ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsLifecycleTypeDef = TypedDict(
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsTypeDef = TypedDict(
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsTypeDef",
    {
        "Lifecycle": ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsLifecycleTypeDef,
        "DestinationBackupVaultArn": str,
    },
    total=False,
)

ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef = TypedDict(
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef = TypedDict(
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
        "CopyActions": List[ClientGetBackupPlanFromJsonResponseBackupPlanRulesCopyActionsTypeDef],
    },
    total=False,
)

ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef = TypedDict(
    "ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef],
    },
    total=False,
)

ClientGetBackupPlanFromJsonResponseTypeDef = TypedDict(
    "ClientGetBackupPlanFromJsonResponseTypeDef",
    {"BackupPlan": ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef},
    total=False,
)

ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsLifecycleTypeDef = TypedDict(
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsTypeDef = TypedDict(
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsTypeDef",
    {
        "Lifecycle": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsLifecycleTypeDef,
        "DestinationBackupVaultArn": str,
    },
    total=False,
)

ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef = TypedDict(
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef = TypedDict(
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
        "CopyActions": List[
            ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesCopyActionsTypeDef
        ],
    },
    total=False,
)

ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef = TypedDict(
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef],
    },
    total=False,
)

ClientGetBackupPlanFromTemplateResponseTypeDef = TypedDict(
    "ClientGetBackupPlanFromTemplateResponseTypeDef",
    {"BackupPlanDocument": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef},
    total=False,
)

ClientGetBackupPlanResponseBackupPlanRulesCopyActionsLifecycleTypeDef = TypedDict(
    "ClientGetBackupPlanResponseBackupPlanRulesCopyActionsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientGetBackupPlanResponseBackupPlanRulesCopyActionsTypeDef = TypedDict(
    "ClientGetBackupPlanResponseBackupPlanRulesCopyActionsTypeDef",
    {
        "Lifecycle": ClientGetBackupPlanResponseBackupPlanRulesCopyActionsLifecycleTypeDef,
        "DestinationBackupVaultArn": str,
    },
    total=False,
)

ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef = TypedDict(
    "ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientGetBackupPlanResponseBackupPlanRulesTypeDef = TypedDict(
    "ClientGetBackupPlanResponseBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
        "CopyActions": List[ClientGetBackupPlanResponseBackupPlanRulesCopyActionsTypeDef],
    },
    total=False,
)

ClientGetBackupPlanResponseBackupPlanTypeDef = TypedDict(
    "ClientGetBackupPlanResponseBackupPlanTypeDef",
    {"BackupPlanName": str, "Rules": List[ClientGetBackupPlanResponseBackupPlanRulesTypeDef]},
    total=False,
)

ClientGetBackupPlanResponseTypeDef = TypedDict(
    "ClientGetBackupPlanResponseTypeDef",
    {
        "BackupPlan": ClientGetBackupPlanResponseBackupPlanTypeDef,
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
    },
    total=False,
)

ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef = TypedDict(
    "ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef",
    {"ConditionType": str, "ConditionKey": str, "ConditionValue": str},
    total=False,
)

ClientGetBackupSelectionResponseBackupSelectionTypeDef = TypedDict(
    "ClientGetBackupSelectionResponseBackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
        "Resources": List[str],
        "ListOfTags": List[ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef],
    },
    total=False,
)

ClientGetBackupSelectionResponseTypeDef = TypedDict(
    "ClientGetBackupSelectionResponseTypeDef",
    {
        "BackupSelection": ClientGetBackupSelectionResponseBackupSelectionTypeDef,
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

ClientGetBackupVaultAccessPolicyResponseTypeDef = TypedDict(
    "ClientGetBackupVaultAccessPolicyResponseTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "Policy": str},
    total=False,
)

ClientGetBackupVaultNotificationsResponseTypeDef = TypedDict(
    "ClientGetBackupVaultNotificationsResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[
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
    },
    total=False,
)

ClientGetRecoveryPointRestoreMetadataResponseTypeDef = TypedDict(
    "ClientGetRecoveryPointRestoreMetadataResponseTypeDef",
    {"BackupVaultArn": str, "RecoveryPointArn": str, "RestoreMetadata": Dict[str, str]},
    total=False,
)

ClientGetSupportedResourceTypesResponseTypeDef = TypedDict(
    "ClientGetSupportedResourceTypesResponseTypeDef", {"ResourceTypes": List[str]}, total=False
)

ClientListBackupJobsResponseBackupJobsCreatedByTypeDef = TypedDict(
    "ClientListBackupJobsResponseBackupJobsCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

ClientListBackupJobsResponseBackupJobsTypeDef = TypedDict(
    "ClientListBackupJobsResponseBackupJobsTypeDef",
    {
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientListBackupJobsResponseBackupJobsCreatedByTypeDef,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
    },
    total=False,
)

ClientListBackupJobsResponseTypeDef = TypedDict(
    "ClientListBackupJobsResponseTypeDef",
    {"BackupJobs": List[ClientListBackupJobsResponseBackupJobsTypeDef], "NextToken": str},
    total=False,
)

ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef = TypedDict(
    "ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef",
    {"BackupPlanTemplateId": str, "BackupPlanTemplateName": str},
    total=False,
)

ClientListBackupPlanTemplatesResponseTypeDef = TypedDict(
    "ClientListBackupPlanTemplatesResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List[
            ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef
        ],
    },
    total=False,
)

ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef = TypedDict(
    "ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)

ClientListBackupPlanVersionsResponseTypeDef = TypedDict(
    "ClientListBackupPlanVersionsResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List[
            ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef
        ],
    },
    total=False,
)

ClientListBackupPlansResponseBackupPlansListTypeDef = TypedDict(
    "ClientListBackupPlansResponseBackupPlansListTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)

ClientListBackupPlansResponseTypeDef = TypedDict(
    "ClientListBackupPlansResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List[ClientListBackupPlansResponseBackupPlansListTypeDef],
    },
    total=False,
)

ClientListBackupSelectionsResponseBackupSelectionsListTypeDef = TypedDict(
    "ClientListBackupSelectionsResponseBackupSelectionsListTypeDef",
    {
        "SelectionId": str,
        "SelectionName": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "IamRoleArn": str,
    },
    total=False,
)

ClientListBackupSelectionsResponseTypeDef = TypedDict(
    "ClientListBackupSelectionsResponseTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List[ClientListBackupSelectionsResponseBackupSelectionsListTypeDef],
    },
    total=False,
)

ClientListBackupVaultsResponseBackupVaultListTypeDef = TypedDict(
    "ClientListBackupVaultsResponseBackupVaultListTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)

ClientListBackupVaultsResponseTypeDef = TypedDict(
    "ClientListBackupVaultsResponseTypeDef",
    {
        "BackupVaultList": List[ClientListBackupVaultsResponseBackupVaultListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCopyJobsResponseCopyJobsCreatedByTypeDef = TypedDict(
    "ClientListCopyJobsResponseCopyJobsCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

ClientListCopyJobsResponseCopyJobsTypeDef = TypedDict(
    "ClientListCopyJobsResponseCopyJobsTypeDef",
    {
        "CopyJobId": str,
        "SourceBackupVaultArn": str,
        "SourceRecoveryPointArn": str,
        "DestinationBackupVaultArn": str,
        "DestinationRecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal["CREATED", "RUNNING", "COMPLETED", "FAILED"],
        "StatusMessage": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientListCopyJobsResponseCopyJobsCreatedByTypeDef,
        "ResourceType": str,
    },
    total=False,
)

ClientListCopyJobsResponseTypeDef = TypedDict(
    "ClientListCopyJobsResponseTypeDef",
    {"CopyJobs": List[ClientListCopyJobsResponseCopyJobsTypeDef], "NextToken": str},
    total=False,
)

ClientListProtectedResourcesResponseResultsTypeDef = TypedDict(
    "ClientListProtectedResourcesResponseResultsTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)

ClientListProtectedResourcesResponseTypeDef = TypedDict(
    "ClientListProtectedResourcesResponseTypeDef",
    {"Results": List[ClientListProtectedResourcesResponseResultsTypeDef], "NextToken": str},
    total=False,
)

ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef = TypedDict(
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)

ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef = TypedDict(
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef = TypedDict(
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef = TypedDict(
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef,
        "IamRoleArn": str,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef,
        "Lifecycle": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
    },
    total=False,
)

ClientListRecoveryPointsByBackupVaultResponseTypeDef = TypedDict(
    "ClientListRecoveryPointsByBackupVaultResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef],
    },
    total=False,
)

ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef = TypedDict(
    "ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
    },
    total=False,
)

ClientListRecoveryPointsByResourceResponseTypeDef = TypedDict(
    "ClientListRecoveryPointsByResourceResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef],
    },
    total=False,
)

ClientListRestoreJobsResponseRestoreJobsTypeDef = TypedDict(
    "ClientListRestoreJobsResponseRestoreJobsTypeDef",
    {
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal["PENDING", "RUNNING", "COMPLETED", "ABORTED", "FAILED"],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
    },
    total=False,
)

ClientListRestoreJobsResponseTypeDef = TypedDict(
    "ClientListRestoreJobsResponseTypeDef",
    {"RestoreJobs": List[ClientListRestoreJobsResponseRestoreJobsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef", {"NextToken": str, "Tags": Dict[str, str]}, total=False
)

ClientStartBackupJobLifecycleTypeDef = TypedDict(
    "ClientStartBackupJobLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientStartBackupJobResponseTypeDef = TypedDict(
    "ClientStartBackupJobResponseTypeDef",
    {"BackupJobId": str, "RecoveryPointArn": str, "CreationDate": datetime},
    total=False,
)

ClientStartCopyJobLifecycleTypeDef = TypedDict(
    "ClientStartCopyJobLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientStartCopyJobResponseTypeDef = TypedDict(
    "ClientStartCopyJobResponseTypeDef", {"CopyJobId": str, "CreationDate": datetime}, total=False
)

ClientStartRestoreJobResponseTypeDef = TypedDict(
    "ClientStartRestoreJobResponseTypeDef", {"RestoreJobId": str}, total=False
)

ClientUpdateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef = TypedDict(
    "ClientUpdateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientUpdateBackupPlanBackupPlanRulesCopyActionsTypeDef = TypedDict(
    "ClientUpdateBackupPlanBackupPlanRulesCopyActionsTypeDef",
    {
        "Lifecycle": ClientUpdateBackupPlanBackupPlanRulesCopyActionsLifecycleTypeDef,
        "DestinationBackupVaultArn": str,
    },
    total=False,
)

ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef = TypedDict(
    "ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientUpdateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "ClientUpdateBackupPlanBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "CopyActions": List[ClientUpdateBackupPlanBackupPlanRulesCopyActionsTypeDef],
    },
    total=False,
)

_RequiredClientUpdateBackupPlanBackupPlanTypeDef = TypedDict(
    "_RequiredClientUpdateBackupPlanBackupPlanTypeDef", {"BackupPlanName": str}
)
_OptionalClientUpdateBackupPlanBackupPlanTypeDef = TypedDict(
    "_OptionalClientUpdateBackupPlanBackupPlanTypeDef",
    {"Rules": List[ClientUpdateBackupPlanBackupPlanRulesTypeDef]},
    total=False,
)


class ClientUpdateBackupPlanBackupPlanTypeDef(
    _RequiredClientUpdateBackupPlanBackupPlanTypeDef,
    _OptionalClientUpdateBackupPlanBackupPlanTypeDef,
):
    pass


ClientUpdateBackupPlanResponseTypeDef = TypedDict(
    "ClientUpdateBackupPlanResponseTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "CreationDate": datetime, "VersionId": str},
    total=False,
)

ClientUpdateRecoveryPointLifecycleLifecycleTypeDef = TypedDict(
    "ClientUpdateRecoveryPointLifecycleLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef = TypedDict(
    "ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)

ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef = TypedDict(
    "ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)

ClientUpdateRecoveryPointLifecycleResponseTypeDef = TypedDict(
    "ClientUpdateRecoveryPointLifecycleResponseTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef,
        "CalculatedLifecycle": ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef,
    },
    total=False,
)
