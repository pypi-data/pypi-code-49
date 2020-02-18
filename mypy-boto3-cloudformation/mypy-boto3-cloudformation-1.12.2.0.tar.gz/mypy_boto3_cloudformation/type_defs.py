"""
Main interface for cloudformation service type definitions.

Usage::

    from mypy_boto3.cloudformation.type_defs import ClientCreateChangeSetParametersTypeDef

    data: ClientCreateChangeSetParametersTypeDef = {...}
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
    "ClientCreateChangeSetParametersTypeDef",
    "ClientCreateChangeSetResourcesToImportTypeDef",
    "ClientCreateChangeSetResponseTypeDef",
    "ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateChangeSetRollbackConfigurationTypeDef",
    "ClientCreateChangeSetTagsTypeDef",
    "ClientCreateStackInstancesDeploymentTargetsTypeDef",
    "ClientCreateStackInstancesOperationPreferencesTypeDef",
    "ClientCreateStackInstancesParameterOverridesTypeDef",
    "ClientCreateStackInstancesResponseTypeDef",
    "ClientCreateStackParametersTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateStackRollbackConfigurationTypeDef",
    "ClientCreateStackSetAutoDeploymentTypeDef",
    "ClientCreateStackSetParametersTypeDef",
    "ClientCreateStackSetResponseTypeDef",
    "ClientCreateStackSetTagsTypeDef",
    "ClientCreateStackTagsTypeDef",
    "ClientDeleteStackInstancesDeploymentTargetsTypeDef",
    "ClientDeleteStackInstancesOperationPreferencesTypeDef",
    "ClientDeleteStackInstancesResponseTypeDef",
    "ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    "ClientDescribeChangeSetResponseChangesTypeDef",
    "ClientDescribeChangeSetResponseParametersTypeDef",
    "ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    "ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    "ClientDescribeChangeSetResponseTagsTypeDef",
    "ClientDescribeChangeSetResponseTypeDef",
    "ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    "ClientDescribeStackEventsResponseStackEventsTypeDef",
    "ClientDescribeStackEventsResponseTypeDef",
    "ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    "ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    "ClientDescribeStackInstanceResponseTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    "ClientDescribeStackResourceDriftsResponseTypeDef",
    "ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    "ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    "ClientDescribeStackResourceResponseTypeDef",
    "ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    "ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    "ClientDescribeStackResourcesResponseTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationDeploymentTargetsTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    "ClientDescribeStackSetOperationResponseTypeDef",
    "ClientDescribeStackSetResponseStackSetAutoDeploymentTypeDef",
    "ClientDescribeStackSetResponseStackSetParametersTypeDef",
    "ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef",
    "ClientDescribeStackSetResponseStackSetTagsTypeDef",
    "ClientDescribeStackSetResponseStackSetTypeDef",
    "ClientDescribeStackSetResponseTypeDef",
    "ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    "ClientDescribeStacksResponseStacksOutputsTypeDef",
    "ClientDescribeStacksResponseStacksParametersTypeDef",
    "ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    "ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    "ClientDescribeStacksResponseStacksTagsTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeTypeRegistrationResponseTypeDef",
    "ClientDescribeTypeResponseLoggingConfigTypeDef",
    "ClientDescribeTypeResponseTypeDef",
    "ClientDetectStackDriftResponseTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    "ClientDetectStackResourceDriftResponseTypeDef",
    "ClientDetectStackSetDriftOperationPreferencesTypeDef",
    "ClientDetectStackSetDriftResponseTypeDef",
    "ClientEstimateTemplateCostParametersTypeDef",
    "ClientEstimateTemplateCostResponseTypeDef",
    "ClientGetStackPolicyResponseTypeDef",
    "ClientGetTemplateResponseTypeDef",
    "ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    "ClientGetTemplateSummaryResponseParametersTypeDef",
    "ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    "ClientGetTemplateSummaryResponseTypeDef",
    "ClientListChangeSetsResponseSummariesTypeDef",
    "ClientListChangeSetsResponseTypeDef",
    "ClientListExportsResponseExportsTypeDef",
    "ClientListExportsResponseTypeDef",
    "ClientListImportsResponseTypeDef",
    "ClientListStackInstancesResponseSummariesTypeDef",
    "ClientListStackInstancesResponseTypeDef",
    "ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    "ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    "ClientListStackResourcesResponseTypeDef",
    "ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    "ClientListStackSetOperationResultsResponseSummariesTypeDef",
    "ClientListStackSetOperationResultsResponseTypeDef",
    "ClientListStackSetOperationsResponseSummariesTypeDef",
    "ClientListStackSetOperationsResponseTypeDef",
    "ClientListStackSetsResponseSummariesAutoDeploymentTypeDef",
    "ClientListStackSetsResponseSummariesTypeDef",
    "ClientListStackSetsResponseTypeDef",
    "ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    "ClientListStacksResponseStackSummariesTypeDef",
    "ClientListStacksResponseTypeDef",
    "ClientListTypeRegistrationsResponseTypeDef",
    "ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    "ClientListTypeVersionsResponseTypeDef",
    "ClientListTypesResponseTypeSummariesTypeDef",
    "ClientListTypesResponseTypeDef",
    "ClientRegisterTypeLoggingConfigTypeDef",
    "ClientRegisterTypeResponseTypeDef",
    "ClientUpdateStackInstancesDeploymentTargetsTypeDef",
    "ClientUpdateStackInstancesOperationPreferencesTypeDef",
    "ClientUpdateStackInstancesParameterOverridesTypeDef",
    "ClientUpdateStackInstancesResponseTypeDef",
    "ClientUpdateStackParametersTypeDef",
    "ClientUpdateStackResponseTypeDef",
    "ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ClientUpdateStackRollbackConfigurationTypeDef",
    "ClientUpdateStackSetAutoDeploymentTypeDef",
    "ClientUpdateStackSetDeploymentTargetsTypeDef",
    "ClientUpdateStackSetOperationPreferencesTypeDef",
    "ClientUpdateStackSetParametersTypeDef",
    "ClientUpdateStackSetResponseTypeDef",
    "ClientUpdateStackSetTagsTypeDef",
    "ClientUpdateStackTagsTypeDef",
    "ClientUpdateTerminationProtectionResponseTypeDef",
    "ClientValidateTemplateResponseParametersTypeDef",
    "ClientValidateTemplateResponseTypeDef",
    "CreateStackOutputTypeDef",
    "AccountLimitTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ChangeTypeDef",
    "ParameterTypeDef",
    "RollbackTriggerTypeDef",
    "RollbackConfigurationTypeDef",
    "TagTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "StackEventTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "OutputTypeDef",
    "StackDriftInformationTypeDef",
    "StackTypeDef",
    "DescribeStacksOutputTypeDef",
    "ChangeSetSummaryTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ExportTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsOutputTypeDef",
    "StackInstanceSummaryTypeDef",
    "ListStackInstancesOutputTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceSummaryTypeDef",
    "ListStackResourcesOutputTypeDef",
    "AccountGateResultTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "StackSetOperationSummaryTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "AutoDeploymentTypeDef",
    "StackSetSummaryTypeDef",
    "ListStackSetsOutputTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackSummaryTypeDef",
    "ListStacksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateStackOutputTypeDef",
    "WaiterConfigTypeDef",
)

ClientCreateChangeSetParametersTypeDef = TypedDict(
    "ClientCreateChangeSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

_RequiredClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetResourcesToImportTypeDef", {"ResourceType": str}
)
_OptionalClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetResourcesToImportTypeDef",
    {"LogicalResourceId": str, "ResourceIdentifier": Dict[str, str]},
    total=False,
)


class ClientCreateChangeSetResourcesToImportTypeDef(
    _RequiredClientCreateChangeSetResourcesToImportTypeDef,
    _OptionalClientCreateChangeSetResourcesToImportTypeDef,
):
    pass


ClientCreateChangeSetResponseTypeDef = TypedDict(
    "ClientCreateChangeSetResponseTypeDef", {"Id": str, "StackId": str}, total=False
)

_RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ClientCreateChangeSetRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateChangeSetRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

_RequiredClientCreateChangeSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateChangeSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateChangeSetTagsTypeDef(
    _RequiredClientCreateChangeSetTagsTypeDef, _OptionalClientCreateChangeSetTagsTypeDef
):
    pass


ClientCreateStackInstancesDeploymentTargetsTypeDef = TypedDict(
    "ClientCreateStackInstancesDeploymentTargetsTypeDef",
    {"Accounts": List[str], "OrganizationalUnitIds": List[str]},
    total=False,
)

ClientCreateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "ClientCreateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientCreateStackInstancesParameterOverridesTypeDef = TypedDict(
    "ClientCreateStackInstancesParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientCreateStackInstancesResponseTypeDef = TypedDict(
    "ClientCreateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)

ClientCreateStackParametersTypeDef = TypedDict(
    "ClientCreateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientCreateStackResponseTypeDef = TypedDict(
    "ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)

_RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ClientCreateStackRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientCreateStackSetAutoDeploymentTypeDef = TypedDict(
    "ClientCreateStackSetAutoDeploymentTypeDef",
    {"Enabled": bool, "RetainStacksOnAccountRemoval": bool},
    total=False,
)

ClientCreateStackSetParametersTypeDef = TypedDict(
    "ClientCreateStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientCreateStackSetResponseTypeDef = TypedDict(
    "ClientCreateStackSetResponseTypeDef", {"StackSetId": str}, total=False
)

_RequiredClientCreateStackSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateStackSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateStackSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateStackSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateStackSetTagsTypeDef(
    _RequiredClientCreateStackSetTagsTypeDef, _OptionalClientCreateStackSetTagsTypeDef
):
    pass


_RequiredClientCreateStackTagsTypeDef = TypedDict(
    "_RequiredClientCreateStackTagsTypeDef", {"Key": str}
)
_OptionalClientCreateStackTagsTypeDef = TypedDict(
    "_OptionalClientCreateStackTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateStackTagsTypeDef(
    _RequiredClientCreateStackTagsTypeDef, _OptionalClientCreateStackTagsTypeDef
):
    pass


ClientDeleteStackInstancesDeploymentTargetsTypeDef = TypedDict(
    "ClientDeleteStackInstancesDeploymentTargetsTypeDef",
    {"Accounts": List[str], "OrganizationalUnitIds": List[str]},
    total=False,
)

ClientDeleteStackInstancesOperationPreferencesTypeDef = TypedDict(
    "ClientDeleteStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientDeleteStackInstancesResponseTypeDef = TypedDict(
    "ClientDeleteStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)

ClientDescribeAccountLimitsResponseAccountLimitsTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {
        "AccountLimits": List[ClientDescribeAccountLimitsResponseAccountLimitsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesResourceChangeTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List[ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef],
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesTypeDef",
    {"Type": str, "ResourceChange": ClientDescribeChangeSetResponseChangesResourceChangeTypeDef},
    total=False,
)

ClientDescribeChangeSetResponseParametersTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

ClientDescribeChangeSetResponseRollbackConfigurationTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientDescribeChangeSetResponseTagsTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeChangeSetResponseTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[ClientDescribeChangeSetResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": ClientDescribeChangeSetResponseRollbackConfigurationTypeDef,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[ClientDescribeChangeSetResponseTagsTypeDef],
        "Changes": List[ClientDescribeChangeSetResponseChangesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeStackDriftDetectionStatusResponseTypeDef = TypedDict(
    "ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "DetectionStatus": Literal[
            "DETECTION_IN_PROGRESS", "DETECTION_FAILED", "DETECTION_COMPLETE"
        ],
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
    },
    total=False,
)

ClientDescribeStackEventsResponseStackEventsTypeDef = TypedDict(
    "ClientDescribeStackEventsResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)

ClientDescribeStackEventsResponseTypeDef = TypedDict(
    "ClientDescribeStackEventsResponseTypeDef",
    {"StackEvents": List[ClientDescribeStackEventsResponseStackEventsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef = TypedDict(
    "ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeStackInstanceResponseStackInstanceTypeDef = TypedDict(
    "ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List[
            ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef
        ],
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStackInstanceResponseTypeDef = TypedDict(
    "ClientDescribeStackInstanceResponseTypeDef",
    {"StackInstance": ClientDescribeStackInstanceResponseStackInstanceTypeDef},
    total=False,
)

ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
    total=False,
)

ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
    total=False,
)

ClientDescribeStackResourceDriftsResponseTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseTypeDef",
    {
        "StackResourceDrifts": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef = TypedDict(
    "ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStackResourceResponseStackResourceDetailTypeDef = TypedDict(
    "ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef,
    },
    total=False,
)

ClientDescribeStackResourceResponseTypeDef = TypedDict(
    "ClientDescribeStackResourceResponseTypeDef",
    {"StackResourceDetail": ClientDescribeStackResourceResponseStackResourceDetailTypeDef},
    total=False,
)

ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef = TypedDict(
    "ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStackResourcesResponseStackResourcesTypeDef = TypedDict(
    "ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef,
    },
    total=False,
)

ClientDescribeStackResourcesResponseTypeDef = TypedDict(
    "ClientDescribeStackResourcesResponseTypeDef",
    {"StackResources": List[ClientDescribeStackResourcesResponseStackResourcesTypeDef]},
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationDeploymentTargetsTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationDeploymentTargetsTypeDef",
    {"Accounts": List[str], "OrganizationalUnitIds": List[str]},
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED", "QUEUED"],
        "OperationPreferences": ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef,
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "DeploymentTargets": ClientDescribeStackSetOperationResponseStackSetOperationDeploymentTargetsTypeDef,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef,
    },
    total=False,
)

ClientDescribeStackSetOperationResponseTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseTypeDef",
    {"StackSetOperation": ClientDescribeStackSetOperationResponseStackSetOperationTypeDef},
    total=False,
)

ClientDescribeStackSetResponseStackSetAutoDeploymentTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetAutoDeploymentTypeDef",
    {"Enabled": bool, "RetainStacksOnAccountRemoval": bool},
    total=False,
)

ClientDescribeStackSetResponseStackSetParametersTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

ClientDescribeStackSetResponseStackSetTagsTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeStackSetResponseStackSetTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "TemplateBody": str,
        "Parameters": List[ClientDescribeStackSetResponseStackSetParametersTypeDef],
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[ClientDescribeStackSetResponseStackSetTagsTypeDef],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef,
        "AutoDeployment": ClientDescribeStackSetResponseStackSetAutoDeploymentTypeDef,
        "PermissionModel": Literal["SERVICE_MANAGED", "SELF_MANAGED"],
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

ClientDescribeStackSetResponseTypeDef = TypedDict(
    "ClientDescribeStackSetResponseTypeDef",
    {"StackSet": ClientDescribeStackSetResponseStackSetTypeDef},
    total=False,
)

ClientDescribeStacksResponseStacksDriftInformationTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStacksResponseStacksOutputsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)

ClientDescribeStacksResponseStacksParametersTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientDescribeStacksResponseStacksTagsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[ClientDescribeStacksResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List[ClientDescribeStacksResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[ClientDescribeStacksResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientDescribeStacksResponseStacksDriftInformationTypeDef,
    },
    total=False,
)

ClientDescribeStacksResponseTypeDef = TypedDict(
    "ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTypeRegistrationResponseTypeDef = TypedDict(
    "ClientDescribeTypeRegistrationResponseTypeDef",
    {
        "ProgressStatus": Literal["COMPLETE", "IN_PROGRESS", "FAILED"],
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
    },
    total=False,
)

ClientDescribeTypeResponseLoggingConfigTypeDef = TypedDict(
    "ClientDescribeTypeResponseLoggingConfigTypeDef",
    {"LogRoleArn": str, "LogGroupName": str},
    total=False,
)

ClientDescribeTypeResponseTypeDef = TypedDict(
    "ClientDescribeTypeResponseTypeDef",
    {
        "Arn": str,
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": Literal["NON_PROVISIONABLE", "IMMUTABLE", "FULLY_MUTABLE"],
        "DeprecatedStatus": Literal["LIVE", "DEPRECATED"],
        "LoggingConfig": ClientDescribeTypeResponseLoggingConfigTypeDef,
        "ExecutionRoleArn": str,
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
    },
    total=False,
)

ClientDetectStackDriftResponseTypeDef = TypedDict(
    "ClientDetectStackDriftResponseTypeDef", {"StackDriftDetectionId": str}, total=False
)

ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
    total=False,
)

ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
    total=False,
)

ClientDetectStackResourceDriftResponseTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseTypeDef",
    {"StackResourceDrift": ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef},
    total=False,
)

ClientDetectStackSetDriftOperationPreferencesTypeDef = TypedDict(
    "ClientDetectStackSetDriftOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientDetectStackSetDriftResponseTypeDef = TypedDict(
    "ClientDetectStackSetDriftResponseTypeDef", {"OperationId": str}, total=False
)

ClientEstimateTemplateCostParametersTypeDef = TypedDict(
    "ClientEstimateTemplateCostParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientEstimateTemplateCostResponseTypeDef = TypedDict(
    "ClientEstimateTemplateCostResponseTypeDef", {"Url": str}, total=False
)

ClientGetStackPolicyResponseTypeDef = TypedDict(
    "ClientGetStackPolicyResponseTypeDef", {"StackPolicyBody": str}, total=False
)

ClientGetTemplateResponseTypeDef = TypedDict(
    "ClientGetTemplateResponseTypeDef",
    {"TemplateBody": Dict[str, Any], "StagesAvailable": List[Literal["Original", "Processed"]]},
    total=False,
)

ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)

ClientGetTemplateSummaryResponseParametersTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef,
    },
    total=False,
)

ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    {"ResourceType": str, "LogicalResourceIds": List[str], "ResourceIdentifiers": List[str]},
    total=False,
)

ClientGetTemplateSummaryResponseTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseTypeDef",
    {
        "Parameters": List[ClientGetTemplateSummaryResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List[
            ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef
        ],
    },
    total=False,
)

ClientListChangeSetsResponseSummariesTypeDef = TypedDict(
    "ClientListChangeSetsResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)

ClientListChangeSetsResponseTypeDef = TypedDict(
    "ClientListChangeSetsResponseTypeDef",
    {"Summaries": List[ClientListChangeSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListExportsResponseExportsTypeDef = TypedDict(
    "ClientListExportsResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)

ClientListExportsResponseTypeDef = TypedDict(
    "ClientListExportsResponseTypeDef",
    {"Exports": List[ClientListExportsResponseExportsTypeDef], "NextToken": str},
    total=False,
)

ClientListImportsResponseTypeDef = TypedDict(
    "ClientListImportsResponseTypeDef", {"Imports": List[str], "NextToken": str}, total=False
)

ClientListStackInstancesResponseSummariesTypeDef = TypedDict(
    "ClientListStackInstancesResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStackInstancesResponseTypeDef = TypedDict(
    "ClientListStackInstancesResponseTypeDef",
    {"Summaries": List[ClientListStackInstancesResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStackResourcesResponseStackResourceSummariesTypeDef = TypedDict(
    "ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "DriftInformation": ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)

ClientListStackResourcesResponseTypeDef = TypedDict(
    "ClientListStackResourcesResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ClientListStackResourcesResponseStackResourceSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef = TypedDict(
    "ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)

ClientListStackSetOperationResultsResponseSummariesTypeDef = TypedDict(
    "ClientListStackSetOperationResultsResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef,
        "OrganizationalUnitId": str,
    },
    total=False,
)

ClientListStackSetOperationResultsResponseTypeDef = TypedDict(
    "ClientListStackSetOperationResultsResponseTypeDef",
    {
        "Summaries": List[ClientListStackSetOperationResultsResponseSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListStackSetOperationsResponseSummariesTypeDef = TypedDict(
    "ClientListStackSetOperationsResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED", "QUEUED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

ClientListStackSetOperationsResponseTypeDef = TypedDict(
    "ClientListStackSetOperationsResponseTypeDef",
    {"Summaries": List[ClientListStackSetOperationsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListStackSetsResponseSummariesAutoDeploymentTypeDef = TypedDict(
    "ClientListStackSetsResponseSummariesAutoDeploymentTypeDef",
    {"Enabled": bool, "RetainStacksOnAccountRemoval": bool},
    total=False,
)

ClientListStackSetsResponseSummariesTypeDef = TypedDict(
    "ClientListStackSetsResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "AutoDeployment": ClientListStackSetsResponseSummariesAutoDeploymentTypeDef,
        "PermissionModel": Literal["SERVICE_MANAGED", "SELF_MANAGED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStackSetsResponseTypeDef = TypedDict(
    "ClientListStackSetsResponseTypeDef",
    {"Summaries": List[ClientListStackSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListStacksResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStacksResponseStackSummariesTypeDef = TypedDict(
    "ClientListStacksResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientListStacksResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)

ClientListStacksResponseTypeDef = TypedDict(
    "ClientListStacksResponseTypeDef",
    {"StackSummaries": List[ClientListStacksResponseStackSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListTypeRegistrationsResponseTypeDef = TypedDict(
    "ClientListTypeRegistrationsResponseTypeDef",
    {"RegistrationTokenList": List[str], "NextToken": str},
    total=False,
)

ClientListTypeVersionsResponseTypeVersionSummariesTypeDef = TypedDict(
    "ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "VersionId": str,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)

ClientListTypeVersionsResponseTypeDef = TypedDict(
    "ClientListTypeVersionsResponseTypeDef",
    {
        "TypeVersionSummaries": List[ClientListTypeVersionsResponseTypeVersionSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTypesResponseTypeSummariesTypeDef = TypedDict(
    "ClientListTypesResponseTypeSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)

ClientListTypesResponseTypeDef = TypedDict(
    "ClientListTypesResponseTypeDef",
    {"TypeSummaries": List[ClientListTypesResponseTypeSummariesTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_RequiredClientRegisterTypeLoggingConfigTypeDef", {"LogRoleArn": str}
)
_OptionalClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_OptionalClientRegisterTypeLoggingConfigTypeDef", {"LogGroupName": str}, total=False
)


class ClientRegisterTypeLoggingConfigTypeDef(
    _RequiredClientRegisterTypeLoggingConfigTypeDef, _OptionalClientRegisterTypeLoggingConfigTypeDef
):
    pass


ClientRegisterTypeResponseTypeDef = TypedDict(
    "ClientRegisterTypeResponseTypeDef", {"RegistrationToken": str}, total=False
)

ClientUpdateStackInstancesDeploymentTargetsTypeDef = TypedDict(
    "ClientUpdateStackInstancesDeploymentTargetsTypeDef",
    {"Accounts": List[str], "OrganizationalUnitIds": List[str]},
    total=False,
)

ClientUpdateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "ClientUpdateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientUpdateStackInstancesParameterOverridesTypeDef = TypedDict(
    "ClientUpdateStackInstancesParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientUpdateStackInstancesResponseTypeDef = TypedDict(
    "ClientUpdateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)

ClientUpdateStackParametersTypeDef = TypedDict(
    "ClientUpdateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientUpdateStackResponseTypeDef = TypedDict(
    "ClientUpdateStackResponseTypeDef", {"StackId": str}, total=False
)

_RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ClientUpdateStackRollbackConfigurationTypeDef = TypedDict(
    "ClientUpdateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientUpdateStackSetAutoDeploymentTypeDef = TypedDict(
    "ClientUpdateStackSetAutoDeploymentTypeDef",
    {"Enabled": bool, "RetainStacksOnAccountRemoval": bool},
    total=False,
)

ClientUpdateStackSetDeploymentTargetsTypeDef = TypedDict(
    "ClientUpdateStackSetDeploymentTargetsTypeDef",
    {"Accounts": List[str], "OrganizationalUnitIds": List[str]},
    total=False,
)

ClientUpdateStackSetOperationPreferencesTypeDef = TypedDict(
    "ClientUpdateStackSetOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientUpdateStackSetParametersTypeDef = TypedDict(
    "ClientUpdateStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientUpdateStackSetResponseTypeDef = TypedDict(
    "ClientUpdateStackSetResponseTypeDef", {"OperationId": str}, total=False
)

_RequiredClientUpdateStackSetTagsTypeDef = TypedDict(
    "_RequiredClientUpdateStackSetTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateStackSetTagsTypeDef = TypedDict(
    "_OptionalClientUpdateStackSetTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateStackSetTagsTypeDef(
    _RequiredClientUpdateStackSetTagsTypeDef, _OptionalClientUpdateStackSetTagsTypeDef
):
    pass


_RequiredClientUpdateStackTagsTypeDef = TypedDict(
    "_RequiredClientUpdateStackTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateStackTagsTypeDef = TypedDict(
    "_OptionalClientUpdateStackTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateStackTagsTypeDef(
    _RequiredClientUpdateStackTagsTypeDef, _OptionalClientUpdateStackTagsTypeDef
):
    pass


ClientUpdateTerminationProtectionResponseTypeDef = TypedDict(
    "ClientUpdateTerminationProtectionResponseTypeDef", {"StackId": str}, total=False
)

ClientValidateTemplateResponseParametersTypeDef = TypedDict(
    "ClientValidateTemplateResponseParametersTypeDef",
    {"ParameterKey": str, "DefaultValue": str, "NoEcho": bool, "Description": str},
    total=False,
)

ClientValidateTemplateResponseTypeDef = TypedDict(
    "ClientValidateTemplateResponseTypeDef",
    {
        "Parameters": List[ClientValidateTemplateResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
    },
    total=False,
)

CreateStackOutputTypeDef = TypedDict("CreateStackOutputTypeDef", {"StackId": str}, total=False)

AccountLimitTypeDef = TypedDict("AccountLimitTypeDef", {"Name": str, "Value": int}, total=False)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {"AccountLimits": List[AccountLimitTypeDef], "NextToken": str},
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": ResourceTargetDefinitionTypeDef,
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List[ResourceChangeDetailTypeDef],
    },
    total=False,
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {"Type": Literal["Resource"], "ResourceChange": ResourceChangeTypeDef},
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

RollbackTriggerTypeDef = TypedDict("RollbackTriggerTypeDef", {"Arn": str, "Type": str})

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {"RollbackTriggers": List[RollbackTriggerTypeDef], "MonitoringTimeInMinutes": int},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[ParameterTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": RollbackConfigurationTypeDef,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[TagTypeDef],
        "Changes": List[ChangeTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredStackEventTypeDef = TypedDict(
    "_RequiredStackEventTypeDef",
    {"StackId": str, "EventId": str, "StackName": str, "Timestamp": datetime},
)
_OptionalStackEventTypeDef = TypedDict(
    "_OptionalStackEventTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StackEventTypeDef(_RequiredStackEventTypeDef, _OptionalStackEventTypeDef):
    pass


DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {"StackEvents": List[StackEventTypeDef], "NextToken": str},
    total=False,
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)

_RequiredStackDriftInformationTypeDef = TypedDict(
    "_RequiredStackDriftInformationTypeDef",
    {"StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"]},
)
_OptionalStackDriftInformationTypeDef = TypedDict(
    "_OptionalStackDriftInformationTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackDriftInformationTypeDef(
    _RequiredStackDriftInformationTypeDef, _OptionalStackDriftInformationTypeDef
):
    pass


_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "StackId": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[ParameterTypeDef],
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": RollbackConfigurationTypeDef,
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List[OutputTypeDef],
        "RoleARN": str,
        "Tags": List[TagTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": StackDriftInformationTypeDef,
    },
    total=False,
)


class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass


DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef", {"Stacks": List[StackTypeDef], "NextToken": str}, total=False
)

ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)

ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {"Summaries": List[ChangeSetSummaryTypeDef], "NextToken": str},
    total=False,
)

ExportTypeDef = TypedDict(
    "ExportTypeDef", {"ExportingStackId": str, "Name": str, "Value": str}, total=False
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef", {"Exports": List[ExportTypeDef], "NextToken": str}, total=False
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef", {"Imports": List[str], "NextToken": str}, total=False
)

StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {"Summaries": List[StackInstanceSummaryTypeDef], "NextToken": str},
    total=False,
)

_RequiredStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationSummaryTypeDef",
    {"StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"]},
)
_OptionalStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationSummaryTypeDef",
    {"LastCheckTimestamp": datetime},
    total=False,
)


class StackResourceDriftInformationSummaryTypeDef(
    _RequiredStackResourceDriftInformationSummaryTypeDef,
    _OptionalStackResourceDriftInformationSummaryTypeDef,
):
    pass


_RequiredStackResourceSummaryTypeDef = TypedDict(
    "_RequiredStackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackResourceSummaryTypeDef = TypedDict(
    "_OptionalStackResourceSummaryTypeDef",
    {
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "DriftInformation": StackResourceDriftInformationSummaryTypeDef,
    },
    total=False,
)


class StackResourceSummaryTypeDef(
    _RequiredStackResourceSummaryTypeDef, _OptionalStackResourceSummaryTypeDef
):
    pass


ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {"StackResourceSummaries": List[StackResourceSummaryTypeDef], "NextToken": str},
    total=False,
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)

StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": AccountGateResultTypeDef,
        "OrganizationalUnitId": str,
    },
    total=False,
)

ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {"Summaries": List[StackSetOperationResultSummaryTypeDef], "NextToken": str},
    total=False,
)

StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED", "QUEUED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {"Summaries": List[StackSetOperationSummaryTypeDef], "NextToken": str},
    total=False,
)

AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef", {"Enabled": bool, "RetainStacksOnAccountRemoval": bool}, total=False
)

StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "AutoDeployment": AutoDeploymentTypeDef,
        "PermissionModel": Literal["SERVICE_MANAGED", "SELF_MANAGED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {"Summaries": List[StackSetSummaryTypeDef], "NextToken": str},
    total=False,
)

_RequiredStackDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackDriftInformationSummaryTypeDef",
    {"StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"]},
)
_OptionalStackDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackDriftInformationSummaryTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackDriftInformationSummaryTypeDef(
    _RequiredStackDriftInformationSummaryTypeDef, _OptionalStackDriftInformationSummaryTypeDef
):
    pass


_RequiredStackSummaryTypeDef = TypedDict(
    "_RequiredStackSummaryTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackSummaryTypeDef = TypedDict(
    "_OptionalStackSummaryTypeDef",
    {
        "StackId": str,
        "TemplateDescription": str,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": StackDriftInformationSummaryTypeDef,
    },
    total=False,
)


class StackSummaryTypeDef(_RequiredStackSummaryTypeDef, _OptionalStackSummaryTypeDef):
    pass


ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {"StackSummaries": List[StackSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateStackOutputTypeDef = TypedDict("UpdateStackOutputTypeDef", {"StackId": str}, total=False)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
