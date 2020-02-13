"""
Main interface for elasticbeanstalk service type definitions.

Usage::

    from mypy_boto3.elasticbeanstalk.type_defs import S3LocationTypeDef

    data: S3LocationTypeDef = {...}
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
    "S3LocationTypeDef",
    "SourceBuildInformationTypeDef",
    "ApplicationVersionDescriptionTypeDef",
    "ApplicationVersionDescriptionsMessageTypeDef",
    "ClientApplyEnvironmentManagedActionResponseTypeDef",
    "ClientCheckDnsAvailabilityResponseTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsTypeDef",
    "ClientComposeEnvironmentsResponseTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateApplicationVersionBuildConfigurationTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionTypeDef",
    "ClientCreateApplicationVersionResponseTypeDef",
    "ClientCreateApplicationVersionSourceBuildInformationTypeDef",
    "ClientCreateApplicationVersionSourceBundleTypeDef",
    "ClientCreateApplicationVersionTagsTypeDef",
    "ClientCreateConfigurationTemplateOptionSettingsTypeDef",
    "ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef",
    "ClientCreateConfigurationTemplateResponseTypeDef",
    "ClientCreateConfigurationTemplateSourceConfigurationTypeDef",
    "ClientCreateConfigurationTemplateTagsTypeDef",
    "ClientCreateEnvironmentOptionSettingsTypeDef",
    "ClientCreateEnvironmentOptionsToRemoveTypeDef",
    "ClientCreateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientCreateEnvironmentResponseResourcesTypeDef",
    "ClientCreateEnvironmentResponseTierTypeDef",
    "ClientCreateEnvironmentResponseTypeDef",
    "ClientCreateEnvironmentTagsTypeDef",
    "ClientCreateEnvironmentTierTypeDef",
    "ClientCreatePlatformVersionOptionSettingsTypeDef",
    "ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef",
    "ClientCreatePlatformVersionResponseBuilderTypeDef",
    "ClientCreatePlatformVersionResponsePlatformSummaryTypeDef",
    "ClientCreatePlatformVersionResponseTypeDef",
    "ClientCreatePlatformVersionTagsTypeDef",
    "ClientCreateStorageLocationResponseTypeDef",
    "ClientDeletePlatformVersionResponsePlatformSummaryTypeDef",
    "ClientDeletePlatformVersionResponseTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef",
    "ClientDescribeApplicationVersionsResponseTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef",
    "ClientDescribeApplicationsResponseApplicationsTypeDef",
    "ClientDescribeApplicationsResponseTypeDef",
    "ClientDescribeConfigurationOptionsOptionsTypeDef",
    "ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef",
    "ClientDescribeConfigurationOptionsResponseOptionsTypeDef",
    "ClientDescribeConfigurationOptionsResponseTypeDef",
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef",
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef",
    "ClientDescribeConfigurationSettingsResponseTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef",
    "ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef",
    "ClientDescribeEnvironmentHealthResponseTypeDef",
    "ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef",
    "ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef",
    "ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef",
    "ClientDescribeEnvironmentManagedActionsResponseTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsTypeDef",
    "ClientDescribeEnvironmentsResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef",
    "ClientDescribeInstancesHealthResponseTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef",
    "ClientDescribePlatformVersionResponseTypeDef",
    "ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef",
    "ClientListAvailableSolutionStacksResponseTypeDef",
    "ClientListPlatformVersionsFiltersTypeDef",
    "ClientListPlatformVersionsResponsePlatformSummaryListTypeDef",
    "ClientListPlatformVersionsResponseTypeDef",
    "ClientListTagsForResourceResponseResourceTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef",
    "ClientRetrieveEnvironmentInfoResponseTypeDef",
    "ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientTerminateEnvironmentResponseResourcesTypeDef",
    "ClientTerminateEnvironmentResponseTierTypeDef",
    "ClientTerminateEnvironmentResponseTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResponseApplicationTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionTypeDef",
    "ClientUpdateApplicationVersionResponseTypeDef",
    "ClientUpdateConfigurationTemplateOptionSettingsTypeDef",
    "ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef",
    "ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef",
    "ClientUpdateConfigurationTemplateResponseTypeDef",
    "ClientUpdateEnvironmentOptionSettingsTypeDef",
    "ClientUpdateEnvironmentOptionsToRemoveTypeDef",
    "ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientUpdateEnvironmentResponseResourcesTypeDef",
    "ClientUpdateEnvironmentResponseTierTypeDef",
    "ClientUpdateEnvironmentResponseTypeDef",
    "ClientUpdateEnvironmentTierTypeDef",
    "ClientUpdateTagsForResourceTagsToAddTypeDef",
    "ClientValidateConfigurationSettingsOptionSettingsTypeDef",
    "ClientValidateConfigurationSettingsResponseMessagesTypeDef",
    "ClientValidateConfigurationSettingsResponseTypeDef",
    "ManagedActionHistoryItemTypeDef",
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    "EnvironmentLinkTypeDef",
    "ListenerTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "EnvironmentResourcesDescriptionTypeDef",
    "EnvironmentTierTypeDef",
    "EnvironmentDescriptionTypeDef",
    "EnvironmentDescriptionsMessageTypeDef",
    "EventDescriptionTypeDef",
    "EventDescriptionsMessageTypeDef",
    "PlatformSummaryTypeDef",
    "ListPlatformVersionsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformFilterTypeDef",
)

S3LocationTypeDef = TypedDict("S3LocationTypeDef", {"S3Bucket": str, "S3Key": str}, total=False)

SourceBuildInformationTypeDef = TypedDict(
    "SourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
)

ApplicationVersionDescriptionTypeDef = TypedDict(
    "ApplicationVersionDescriptionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": SourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": S3LocationTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)

ApplicationVersionDescriptionsMessageTypeDef = TypedDict(
    "ApplicationVersionDescriptionsMessageTypeDef",
    {"ApplicationVersions": List[ApplicationVersionDescriptionTypeDef], "NextToken": str},
    total=False,
)

ClientApplyEnvironmentManagedActionResponseTypeDef = TypedDict(
    "ClientApplyEnvironmentManagedActionResponseTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "Status": str,
    },
    total=False,
)

ClientCheckDnsAvailabilityResponseTypeDef = TypedDict(
    "ClientCheckDnsAvailabilityResponseTypeDef",
    {"Available": bool, "FullyQualifiedCNAME": str},
    total=False,
)

ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)

ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)

ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)

ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    {"LoadBalancer": ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef},
    total=False,
)

ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)

ClientComposeEnvironmentsResponseEnvironmentsTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef,
        "Tier": ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)

ClientComposeEnvironmentsResponseTypeDef = TypedDict(
    "ClientComposeEnvironmentsResponseTypeDef",
    {"Environments": List[ClientComposeEnvironmentsResponseEnvironmentsTypeDef], "NextToken": str},
    total=False,
)

ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)

ClientCreateApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "ClientCreateApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)

ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)

ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)

ClientCreateApplicationResponseApplicationTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef,
    },
    total=False,
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef",
    {"Application": ClientCreateApplicationResponseApplicationTypeDef},
    total=False,
)

ClientCreateApplicationTagsTypeDef = TypedDict(
    "ClientCreateApplicationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateApplicationVersionBuildConfigurationTypeDef = TypedDict(
    "ClientCreateApplicationVersionBuildConfigurationTypeDef",
    {
        "ArtifactName": str,
        "CodeBuildServiceRole": str,
        "ComputeType": Literal[
            "BUILD_GENERAL1_SMALL", "BUILD_GENERAL1_MEDIUM", "BUILD_GENERAL1_LARGE"
        ],
        "Image": str,
        "TimeoutInMinutes": int,
    },
    total=False,
)

ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)

ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef = TypedDict(
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientCreateApplicationVersionResponseApplicationVersionTypeDef = TypedDict(
    "ClientCreateApplicationVersionResponseApplicationVersionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)

ClientCreateApplicationVersionResponseTypeDef = TypedDict(
    "ClientCreateApplicationVersionResponseTypeDef",
    {"ApplicationVersion": ClientCreateApplicationVersionResponseApplicationVersionTypeDef},
    total=False,
)

_RequiredClientCreateApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationVersionSourceBuildInformationTypeDef",
    {"SourceType": Literal["Git", "Zip"]},
)
_OptionalClientCreateApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationVersionSourceBuildInformationTypeDef",
    {"SourceRepository": Literal["CodeCommit", "S3"], "SourceLocation": str},
    total=False,
)


class ClientCreateApplicationVersionSourceBuildInformationTypeDef(
    _RequiredClientCreateApplicationVersionSourceBuildInformationTypeDef,
    _OptionalClientCreateApplicationVersionSourceBuildInformationTypeDef,
):
    pass


ClientCreateApplicationVersionSourceBundleTypeDef = TypedDict(
    "ClientCreateApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientCreateApplicationVersionTagsTypeDef = TypedDict(
    "ClientCreateApplicationVersionTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateConfigurationTemplateOptionSettingsTypeDef = TypedDict(
    "ClientCreateConfigurationTemplateOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef = TypedDict(
    "ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientCreateConfigurationTemplateResponseTypeDef = TypedDict(
    "ClientCreateConfigurationTemplateResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": Literal["deployed", "pending", "failed"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef],
    },
    total=False,
)

ClientCreateConfigurationTemplateSourceConfigurationTypeDef = TypedDict(
    "ClientCreateConfigurationTemplateSourceConfigurationTypeDef",
    {"ApplicationName": str, "TemplateName": str},
    total=False,
)

ClientCreateConfigurationTemplateTagsTypeDef = TypedDict(
    "ClientCreateConfigurationTemplateTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateEnvironmentOptionSettingsTypeDef = TypedDict(
    "ClientCreateEnvironmentOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientCreateEnvironmentOptionsToRemoveTypeDef = TypedDict(
    "ClientCreateEnvironmentOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)

ClientCreateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)

ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)

ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef],
    },
    total=False,
)

ClientCreateEnvironmentResponseResourcesTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)

ClientCreateEnvironmentResponseTierTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)

ClientCreateEnvironmentResponseTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientCreateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientCreateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[ClientCreateEnvironmentResponseEnvironmentLinksTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)

ClientCreateEnvironmentTagsTypeDef = TypedDict(
    "ClientCreateEnvironmentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateEnvironmentTierTypeDef = TypedDict(
    "ClientCreateEnvironmentTierTypeDef", {"Name": str, "Type": str, "Version": str}, total=False
)

ClientCreatePlatformVersionOptionSettingsTypeDef = TypedDict(
    "ClientCreatePlatformVersionOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef = TypedDict(
    "ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientCreatePlatformVersionResponseBuilderTypeDef = TypedDict(
    "ClientCreatePlatformVersionResponseBuilderTypeDef", {"ARN": str}, total=False
)

ClientCreatePlatformVersionResponsePlatformSummaryTypeDef = TypedDict(
    "ClientCreatePlatformVersionResponsePlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)

ClientCreatePlatformVersionResponseTypeDef = TypedDict(
    "ClientCreatePlatformVersionResponseTypeDef",
    {
        "PlatformSummary": ClientCreatePlatformVersionResponsePlatformSummaryTypeDef,
        "Builder": ClientCreatePlatformVersionResponseBuilderTypeDef,
    },
    total=False,
)

ClientCreatePlatformVersionTagsTypeDef = TypedDict(
    "ClientCreatePlatformVersionTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateStorageLocationResponseTypeDef = TypedDict(
    "ClientCreateStorageLocationResponseTypeDef", {"S3Bucket": str}, total=False
)

ClientDeletePlatformVersionResponsePlatformSummaryTypeDef = TypedDict(
    "ClientDeletePlatformVersionResponsePlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)

ClientDeletePlatformVersionResponseTypeDef = TypedDict(
    "ClientDeletePlatformVersionResponseTypeDef",
    {"PlatformSummary": ClientDeletePlatformVersionResponsePlatformSummaryTypeDef},
    total=False,
)

ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef",
    {"Maximum": int},
    total=False,
)

ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef",
    {"Maximum": int},
    total=False,
)

ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef",
    {"Maximum": int},
    total=False,
)

ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef",
    {"Maximum": int},
    total=False,
)

ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef",
    {"Maximum": int},
    total=False,
)

ClientDescribeAccountAttributesResponseResourceQuotasTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseResourceQuotasTypeDef",
    {
        "ApplicationQuota": ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef,
        "ApplicationVersionQuota": ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef,
        "EnvironmentQuota": ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef,
        "ConfigurationTemplateQuota": ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef,
        "CustomPlatformQuota": ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef,
    },
    total=False,
)

ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseTypeDef",
    {"ResourceQuotas": ClientDescribeAccountAttributesResponseResourceQuotasTypeDef},
    total=False,
)

ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef = TypedDict(
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)

ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef = TypedDict(
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef = TypedDict(
    "ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)

ClientDescribeApplicationVersionsResponseTypeDef = TypedDict(
    "ClientDescribeApplicationVersionsResponseTypeDef",
    {
        "ApplicationVersions": List[
            ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)

ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef = TypedDict(
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)

ClientDescribeApplicationsResponseApplicationsTypeDef = TypedDict(
    "ClientDescribeApplicationsResponseApplicationsTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef,
    },
    total=False,
)

ClientDescribeApplicationsResponseTypeDef = TypedDict(
    "ClientDescribeApplicationsResponseTypeDef",
    {"Applications": List[ClientDescribeApplicationsResponseApplicationsTypeDef]},
    total=False,
)

ClientDescribeConfigurationOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeConfigurationOptionsOptionsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)

ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef = TypedDict(
    "ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef",
    {"Pattern": str, "Label": str},
    total=False,
)

ClientDescribeConfigurationOptionsResponseOptionsTypeDef = TypedDict(
    "ClientDescribeConfigurationOptionsResponseOptionsTypeDef",
    {
        "Namespace": str,
        "Name": str,
        "DefaultValue": str,
        "ChangeSeverity": str,
        "UserDefined": bool,
        "ValueType": Literal["Scalar", "List"],
        "ValueOptions": List[str],
        "MinValue": int,
        "MaxValue": int,
        "MaxLength": int,
        "Regex": ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef,
    },
    total=False,
)

ClientDescribeConfigurationOptionsResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationOptionsResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List[ClientDescribeConfigurationOptionsResponseOptionsTypeDef],
    },
    total=False,
)

ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef = TypedDict(
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef = TypedDict(
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": Literal["deployed", "pending", "failed"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[
            ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeConfigurationSettingsResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationSettingsResponseTypeDef",
    {
        "ConfigurationSettings": List[
            ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef = TypedDict(
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)

ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef = TypedDict(
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef",
    {"Status2xx": int, "Status3xx": int, "Status4xx": int, "Status5xx": int},
    total=False,
)

ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef = TypedDict(
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef,
        "Latency": ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef,
    },
    total=False,
)

ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef = TypedDict(
    "ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef",
    {
        "NoData": int,
        "Unknown": int,
        "Pending": int,
        "Ok": int,
        "Info": int,
        "Warning": int,
        "Degraded": int,
        "Severe": int,
    },
    total=False,
)

ClientDescribeEnvironmentHealthResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentHealthResponseTypeDef",
    {
        "EnvironmentName": str,
        "HealthStatus": str,
        "Status": Literal["Green", "Yellow", "Red", "Grey"],
        "Color": str,
        "Causes": List[str],
        "ApplicationMetrics": ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef,
        "InstancesHealth": ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef,
        "RefreshedAt": datetime,
    },
    total=False,
)

ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef = TypedDict(
    "ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef",
    {
        "ActionId": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "ActionDescription": str,
        "FailureType": Literal[
            "UpdateCancelled",
            "CancellationFailed",
            "RollbackFailed",
            "RollbackSuccessful",
            "InternalFailure",
            "InvalidEnvironmentState",
            "PermissionsError",
        ],
        "Status": Literal["Completed", "Failed", "Unknown"],
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)

ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef",
    {
        "ManagedActionHistoryItems": List[
            ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef = TypedDict(
    "ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "Status": Literal["Scheduled", "Pending", "Running", "Unknown"],
        "WindowStartTime": datetime,
    },
    total=False,
)

ClientDescribeEnvironmentManagedActionsResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentManagedActionsResponseTypeDef",
    {"ManagedActions": List[ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef]},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef",
    {"Id": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef",
    {"Id": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef",
    {"Name": str, "URL": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef",
    {
        "EnvironmentName": str,
        "AutoScalingGroups": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef
        ],
        "Instances": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef
        ],
        "LaunchConfigurations": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef
        ],
        "LaunchTemplates": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef
        ],
        "LoadBalancers": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef
        ],
        "Triggers": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef
        ],
        "Queues": List[ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef],
    },
    total=False,
)

ClientDescribeEnvironmentResourcesResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentResourcesResponseTypeDef",
    {"EnvironmentResources": ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef},
    total=False,
)

ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)

ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)

ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)

ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    {"LoadBalancer": ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef},
    total=False,
)

ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)

ClientDescribeEnvironmentsResponseEnvironmentsTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef,
        "Tier": ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)

ClientDescribeEnvironmentsResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseTypeDef",
    {"Environments": List[ClientDescribeEnvironmentsResponseEnvironmentsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Events": List[ClientDescribeEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef",
    {"Status2xx": int, "Status3xx": int, "Status4xx": int, "Status5xx": int},
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef,
        "Latency": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef,
    },
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef",
    {"VersionLabel": str, "DeploymentId": int, "Status": str, "DeploymentTime": datetime},
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef",
    {
        "User": float,
        "Nice": float,
        "System": float,
        "Idle": float,
        "IOWait": float,
        "IRQ": float,
        "SoftIRQ": float,
        "Privileged": float,
    },
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef",
    {
        "CPUUtilization": ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef,
        "LoadAverage": List[float],
    },
    total=False,
)

ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "Color": str,
        "Causes": List[str],
        "LaunchedAt": datetime,
        "ApplicationMetrics": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef,
        "System": ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef,
        "Deployment": ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef,
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)

ClientDescribeInstancesHealthResponseTypeDef = TypedDict(
    "ClientDescribeInstancesHealthResponseTypeDef",
    {
        "InstanceHealthList": List[ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef],
        "RefreshedAt": datetime,
        "NextToken": str,
    },
    total=False,
)

ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef = TypedDict(
    "ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef",
    {"VirtualizationType": str, "ImageId": str},
    total=False,
)

ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef = TypedDict(
    "ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef = TypedDict(
    "ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef = TypedDict(
    "ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformName": str,
        "PlatformVersion": str,
        "SolutionStackName": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "PlatformCategory": str,
        "Description": str,
        "Maintainer": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "ProgrammingLanguages": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef
        ],
        "Frameworks": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef
        ],
        "CustomAmiList": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef
        ],
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)

ClientDescribePlatformVersionResponseTypeDef = TypedDict(
    "ClientDescribePlatformVersionResponseTypeDef",
    {"PlatformDescription": ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef},
    total=False,
)

ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef = TypedDict(
    "ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef",
    {"SolutionStackName": str, "PermittedFileTypes": List[str]},
    total=False,
)

ClientListAvailableSolutionStacksResponseTypeDef = TypedDict(
    "ClientListAvailableSolutionStacksResponseTypeDef",
    {
        "SolutionStacks": List[str],
        "SolutionStackDetails": List[
            ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef
        ],
    },
    total=False,
)

ClientListPlatformVersionsFiltersTypeDef = TypedDict(
    "ClientListPlatformVersionsFiltersTypeDef",
    {"Type": str, "Operator": str, "Values": List[str]},
    total=False,
)

ClientListPlatformVersionsResponsePlatformSummaryListTypeDef = TypedDict(
    "ClientListPlatformVersionsResponsePlatformSummaryListTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)

ClientListPlatformVersionsResponseTypeDef = TypedDict(
    "ClientListPlatformVersionsResponseTypeDef",
    {
        "PlatformSummaryList": List[ClientListPlatformVersionsResponsePlatformSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseResourceTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List[ClientListTagsForResourceResponseResourceTagsTypeDef],
    },
    total=False,
)

ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef = TypedDict(
    "ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef",
    {
        "InfoType": Literal["tail", "bundle"],
        "Ec2InstanceId": str,
        "SampleTimestamp": datetime,
        "Message": str,
    },
    total=False,
)

ClientRetrieveEnvironmentInfoResponseTypeDef = TypedDict(
    "ClientRetrieveEnvironmentInfoResponseTypeDef",
    {"EnvironmentInfo": List[ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef]},
    total=False,
)

ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)

ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)

ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef],
    },
    total=False,
)

ClientTerminateEnvironmentResponseResourcesTypeDef = TypedDict(
    "ClientTerminateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)

ClientTerminateEnvironmentResponseTierTypeDef = TypedDict(
    "ClientTerminateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)

ClientTerminateEnvironmentResponseTypeDef = TypedDict(
    "ClientTerminateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientTerminateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientTerminateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)

ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResourceLifecycleResponseTypeDef = TypedDict(
    "ClientUpdateApplicationResourceLifecycleResponseTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)

ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResponseApplicationTypeDef = TypedDict(
    "ClientUpdateApplicationResponseApplicationTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef,
    },
    total=False,
)

ClientUpdateApplicationResponseTypeDef = TypedDict(
    "ClientUpdateApplicationResponseTypeDef",
    {"Application": ClientUpdateApplicationResponseApplicationTypeDef},
    total=False,
)

ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)

ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef = TypedDict(
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientUpdateApplicationVersionResponseApplicationVersionTypeDef = TypedDict(
    "ClientUpdateApplicationVersionResponseApplicationVersionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)

ClientUpdateApplicationVersionResponseTypeDef = TypedDict(
    "ClientUpdateApplicationVersionResponseTypeDef",
    {"ApplicationVersion": ClientUpdateApplicationVersionResponseApplicationVersionTypeDef},
    total=False,
)

ClientUpdateConfigurationTemplateOptionSettingsTypeDef = TypedDict(
    "ClientUpdateConfigurationTemplateOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef = TypedDict(
    "ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)

ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef = TypedDict(
    "ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientUpdateConfigurationTemplateResponseTypeDef = TypedDict(
    "ClientUpdateConfigurationTemplateResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": Literal["deployed", "pending", "failed"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef],
    },
    total=False,
)

ClientUpdateEnvironmentOptionSettingsTypeDef = TypedDict(
    "ClientUpdateEnvironmentOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientUpdateEnvironmentOptionsToRemoveTypeDef = TypedDict(
    "ClientUpdateEnvironmentOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)

ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)

ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)

ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef],
    },
    total=False,
)

ClientUpdateEnvironmentResponseResourcesTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)

ClientUpdateEnvironmentResponseTierTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)

ClientUpdateEnvironmentResponseTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientUpdateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientUpdateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)

ClientUpdateEnvironmentTierTypeDef = TypedDict(
    "ClientUpdateEnvironmentTierTypeDef", {"Name": str, "Type": str, "Version": str}, total=False
)

ClientUpdateTagsForResourceTagsToAddTypeDef = TypedDict(
    "ClientUpdateTagsForResourceTagsToAddTypeDef", {"Key": str, "Value": str}, total=False
)

ClientValidateConfigurationSettingsOptionSettingsTypeDef = TypedDict(
    "ClientValidateConfigurationSettingsOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)

ClientValidateConfigurationSettingsResponseMessagesTypeDef = TypedDict(
    "ClientValidateConfigurationSettingsResponseMessagesTypeDef",
    {"Message": str, "Severity": Literal["error", "warning"], "Namespace": str, "OptionName": str},
    total=False,
)

ClientValidateConfigurationSettingsResponseTypeDef = TypedDict(
    "ClientValidateConfigurationSettingsResponseTypeDef",
    {"Messages": List[ClientValidateConfigurationSettingsResponseMessagesTypeDef]},
    total=False,
)

ManagedActionHistoryItemTypeDef = TypedDict(
    "ManagedActionHistoryItemTypeDef",
    {
        "ActionId": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "ActionDescription": str,
        "FailureType": Literal[
            "UpdateCancelled",
            "CancellationFailed",
            "RollbackFailed",
            "RollbackSuccessful",
            "InternalFailure",
            "InvalidEnvironmentState",
            "PermissionsError",
        ],
        "Status": Literal["Completed", "Failed", "Unknown"],
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)

DescribeEnvironmentManagedActionHistoryResultTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    {"ManagedActionHistoryItems": List[ManagedActionHistoryItemTypeDef], "NextToken": str},
    total=False,
)

EnvironmentLinkTypeDef = TypedDict(
    "EnvironmentLinkTypeDef", {"LinkName": str, "EnvironmentName": str}, total=False
)

ListenerTypeDef = TypedDict("ListenerTypeDef", {"Protocol": str, "Port": int}, total=False)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {"LoadBalancerName": str, "Domain": str, "Listeners": List[ListenerTypeDef]},
    total=False,
)

EnvironmentResourcesDescriptionTypeDef = TypedDict(
    "EnvironmentResourcesDescriptionTypeDef",
    {"LoadBalancer": LoadBalancerDescriptionTypeDef},
    total=False,
)

EnvironmentTierTypeDef = TypedDict(
    "EnvironmentTierTypeDef", {"Name": str, "Type": str, "Version": str}, total=False
)

EnvironmentDescriptionTypeDef = TypedDict(
    "EnvironmentDescriptionTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": EnvironmentResourcesDescriptionTypeDef,
        "Tier": EnvironmentTierTypeDef,
        "EnvironmentLinks": List[EnvironmentLinkTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)

EnvironmentDescriptionsMessageTypeDef = TypedDict(
    "EnvironmentDescriptionsMessageTypeDef",
    {"Environments": List[EnvironmentDescriptionTypeDef], "NextToken": str},
    total=False,
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    },
    total=False,
)

EventDescriptionsMessageTypeDef = TypedDict(
    "EventDescriptionsMessageTypeDef",
    {"Events": List[EventDescriptionTypeDef], "NextToken": str},
    total=False,
)

PlatformSummaryTypeDef = TypedDict(
    "PlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)

ListPlatformVersionsResultTypeDef = TypedDict(
    "ListPlatformVersionsResultTypeDef",
    {"PlatformSummaryList": List[PlatformSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PlatformFilterTypeDef = TypedDict(
    "PlatformFilterTypeDef", {"Type": str, "Operator": str, "Values": List[str]}, total=False
)
