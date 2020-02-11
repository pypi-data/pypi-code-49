"""
Main interface for elasticbeanstalk service client

Usage::

    import boto3
    from mypy_boto3.elasticbeanstalk import ElasticBeanstalkClient

    session = boto3.Session()

    client: ElasticBeanstalkClient = boto3.client("elasticbeanstalk")
    session_client: ElasticBeanstalkClient = session.client("elasticbeanstalk")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elasticbeanstalk.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elasticbeanstalk.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_elasticbeanstalk.type_defs import (
    ClientApplyEnvironmentManagedActionResponseTypeDef,
    ClientCheckDnsAvailabilityResponseTypeDef,
    ClientComposeEnvironmentsResponseTypeDef,
    ClientCreateApplicationResourceLifecycleConfigTypeDef,
    ClientCreateApplicationResponseTypeDef,
    ClientCreateApplicationTagsTypeDef,
    ClientCreateApplicationVersionBuildConfigurationTypeDef,
    ClientCreateApplicationVersionResponseTypeDef,
    ClientCreateApplicationVersionSourceBuildInformationTypeDef,
    ClientCreateApplicationVersionSourceBundleTypeDef,
    ClientCreateApplicationVersionTagsTypeDef,
    ClientCreateConfigurationTemplateOptionSettingsTypeDef,
    ClientCreateConfigurationTemplateResponseTypeDef,
    ClientCreateConfigurationTemplateSourceConfigurationTypeDef,
    ClientCreateConfigurationTemplateTagsTypeDef,
    ClientCreateEnvironmentOptionSettingsTypeDef,
    ClientCreateEnvironmentOptionsToRemoveTypeDef,
    ClientCreateEnvironmentResponseTypeDef,
    ClientCreateEnvironmentTagsTypeDef,
    ClientCreateEnvironmentTierTypeDef,
    ClientCreatePlatformVersionOptionSettingsTypeDef,
    ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef,
    ClientCreatePlatformVersionResponseTypeDef,
    ClientCreatePlatformVersionTagsTypeDef,
    ClientCreateStorageLocationResponseTypeDef,
    ClientDeletePlatformVersionResponseTypeDef,
    ClientDescribeAccountAttributesResponseTypeDef,
    ClientDescribeApplicationVersionsResponseTypeDef,
    ClientDescribeApplicationsResponseTypeDef,
    ClientDescribeConfigurationOptionsOptionsTypeDef,
    ClientDescribeConfigurationOptionsResponseTypeDef,
    ClientDescribeConfigurationSettingsResponseTypeDef,
    ClientDescribeEnvironmentHealthResponseTypeDef,
    ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef,
    ClientDescribeEnvironmentManagedActionsResponseTypeDef,
    ClientDescribeEnvironmentResourcesResponseTypeDef,
    ClientDescribeEnvironmentsResponseTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeInstancesHealthResponseTypeDef,
    ClientDescribePlatformVersionResponseTypeDef,
    ClientListAvailableSolutionStacksResponseTypeDef,
    ClientListPlatformVersionsFiltersTypeDef,
    ClientListPlatformVersionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientRetrieveEnvironmentInfoResponseTypeDef,
    ClientTerminateEnvironmentResponseTypeDef,
    ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef,
    ClientUpdateApplicationResourceLifecycleResponseTypeDef,
    ClientUpdateApplicationResponseTypeDef,
    ClientUpdateApplicationVersionResponseTypeDef,
    ClientUpdateConfigurationTemplateOptionSettingsTypeDef,
    ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef,
    ClientUpdateConfigurationTemplateResponseTypeDef,
    ClientUpdateEnvironmentOptionSettingsTypeDef,
    ClientUpdateEnvironmentOptionsToRemoveTypeDef,
    ClientUpdateEnvironmentResponseTypeDef,
    ClientUpdateEnvironmentTierTypeDef,
    ClientUpdateTagsForResourceTagsToAddTypeDef,
    ClientValidateConfigurationSettingsOptionSettingsTypeDef,
    ClientValidateConfigurationSettingsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticBeanstalkClient",)


class ElasticBeanstalkClient:
    """
    [ElasticBeanstalk.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client)
    """

    exceptions: "client_scope.Exceptions"

    def abort_environment_update(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        """
        [Client.abort_environment_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.abort_environment_update)
        """

    def apply_environment_managed_action(
        self, ActionId: str, EnvironmentName: str = None, EnvironmentId: str = None
    ) -> ClientApplyEnvironmentManagedActionResponseTypeDef:
        """
        [Client.apply_environment_managed_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.apply_environment_managed_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.can_paginate)
        """

    def check_dns_availability(self, CNAMEPrefix: str) -> ClientCheckDnsAvailabilityResponseTypeDef:
        """
        [Client.check_dns_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.check_dns_availability)
        """

    def compose_environments(
        self, ApplicationName: str = None, GroupName: str = None, VersionLabels: List[str] = None
    ) -> ClientComposeEnvironmentsResponseTypeDef:
        """
        [Client.compose_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.compose_environments)
        """

    def create_application(
        self,
        ApplicationName: str,
        Description: str = None,
        ResourceLifecycleConfig: ClientCreateApplicationResourceLifecycleConfigTypeDef = None,
        Tags: List[ClientCreateApplicationTagsTypeDef] = None,
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application)
        """

    def create_application_version(
        self,
        ApplicationName: str,
        VersionLabel: str,
        Description: str = None,
        SourceBuildInformation: ClientCreateApplicationVersionSourceBuildInformationTypeDef = None,
        SourceBundle: ClientCreateApplicationVersionSourceBundleTypeDef = None,
        BuildConfiguration: ClientCreateApplicationVersionBuildConfigurationTypeDef = None,
        AutoCreateApplication: bool = None,
        Process: bool = None,
        Tags: List[ClientCreateApplicationVersionTagsTypeDef] = None,
    ) -> ClientCreateApplicationVersionResponseTypeDef:
        """
        [Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application_version)
        """

    def create_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        SourceConfiguration: ClientCreateConfigurationTemplateSourceConfigurationTypeDef = None,
        EnvironmentId: str = None,
        Description: str = None,
        OptionSettings: List[ClientCreateConfigurationTemplateOptionSettingsTypeDef] = None,
        Tags: List[ClientCreateConfigurationTemplateTagsTypeDef] = None,
    ) -> ClientCreateConfigurationTemplateResponseTypeDef:
        """
        [Client.create_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_configuration_template)
        """

    def create_environment(
        self,
        ApplicationName: str,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        CNAMEPrefix: str = None,
        Tier: ClientCreateEnvironmentTierTypeDef = None,
        Tags: List[ClientCreateEnvironmentTagsTypeDef] = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List[ClientCreateEnvironmentOptionSettingsTypeDef] = None,
        OptionsToRemove: List[ClientCreateEnvironmentOptionsToRemoveTypeDef] = None,
    ) -> ClientCreateEnvironmentResponseTypeDef:
        """
        [Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_environment)
        """

    def create_platform_version(
        self,
        PlatformName: str,
        PlatformVersion: str,
        PlatformDefinitionBundle: ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef,
        EnvironmentName: str = None,
        OptionSettings: List[ClientCreatePlatformVersionOptionSettingsTypeDef] = None,
        Tags: List[ClientCreatePlatformVersionTagsTypeDef] = None,
    ) -> ClientCreatePlatformVersionResponseTypeDef:
        """
        [Client.create_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_platform_version)
        """

    def create_storage_location(
        self, *args: Any, **kwargs: Any
    ) -> ClientCreateStorageLocationResponseTypeDef:
        """
        [Client.create_storage_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_storage_location)
        """

    def delete_application(self, ApplicationName: str, TerminateEnvByForce: bool = None) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application)
        """

    def delete_application_version(
        self, ApplicationName: str, VersionLabel: str, DeleteSourceBundle: bool = None
    ) -> None:
        """
        [Client.delete_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application_version)
        """

    def delete_configuration_template(self, ApplicationName: str, TemplateName: str) -> None:
        """
        [Client.delete_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_configuration_template)
        """

    def delete_environment_configuration(self, ApplicationName: str, EnvironmentName: str) -> None:
        """
        [Client.delete_environment_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_environment_configuration)
        """

    def delete_platform_version(
        self, PlatformArn: str = None
    ) -> ClientDeletePlatformVersionResponseTypeDef:
        """
        [Client.delete_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_platform_version)
        """

    def describe_account_attributes(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_account_attributes)
        """

    def describe_application_versions(
        self,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeApplicationVersionsResponseTypeDef:
        """
        [Client.describe_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_application_versions)
        """

    def describe_applications(
        self, ApplicationNames: List[str] = None
    ) -> ClientDescribeApplicationsResponseTypeDef:
        """
        [Client.describe_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_applications)
        """

    def describe_configuration_options(
        self,
        ApplicationName: str = None,
        TemplateName: str = None,
        EnvironmentName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        Options: List[ClientDescribeConfigurationOptionsOptionsTypeDef] = None,
    ) -> ClientDescribeConfigurationOptionsResponseTypeDef:
        """
        [Client.describe_configuration_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_options)
        """

    def describe_configuration_settings(
        self, ApplicationName: str, TemplateName: str = None, EnvironmentName: str = None
    ) -> ClientDescribeConfigurationSettingsResponseTypeDef:
        """
        [Client.describe_configuration_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_settings)
        """

    def describe_environment_health(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[
            Literal[
                "Status",
                "Color",
                "Causes",
                "ApplicationMetrics",
                "InstancesHealth",
                "All",
                "HealthStatus",
                "RefreshedAt",
            ]
        ] = None,
    ) -> ClientDescribeEnvironmentHealthResponseTypeDef:
        """
        [Client.describe_environment_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_health)
        """

    def describe_environment_managed_action_history(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef:
        """
        [Client.describe_environment_managed_action_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_action_history)
        """

    def describe_environment_managed_actions(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        Status: Literal["Scheduled", "Pending", "Running", "Unknown"] = None,
    ) -> ClientDescribeEnvironmentManagedActionsResponseTypeDef:
        """
        [Client.describe_environment_managed_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_actions)
        """

    def describe_environment_resources(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> ClientDescribeEnvironmentResourcesResponseTypeDef:
        """
        [Client.describe_environment_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_resources)
        """

    def describe_environments(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeEnvironmentsResponseTypeDef:
        """
        [Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environments)
        """

    def describe_events(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_events)
        """

    def describe_instances_health(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[
            Literal[
                "HealthStatus",
                "Color",
                "Causes",
                "ApplicationMetrics",
                "RefreshedAt",
                "LaunchedAt",
                "System",
                "Deployment",
                "AvailabilityZone",
                "InstanceType",
                "All",
            ]
        ] = None,
        NextToken: str = None,
    ) -> ClientDescribeInstancesHealthResponseTypeDef:
        """
        [Client.describe_instances_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_instances_health)
        """

    def describe_platform_version(
        self, PlatformArn: str = None
    ) -> ClientDescribePlatformVersionResponseTypeDef:
        """
        [Client.describe_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_platform_version)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.generate_presigned_url)
        """

    def list_available_solution_stacks(
        self, *args: Any, **kwargs: Any
    ) -> ClientListAvailableSolutionStacksResponseTypeDef:
        """
        [Client.list_available_solution_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_available_solution_stacks)
        """

    def list_platform_versions(
        self,
        Filters: List[ClientListPlatformVersionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientListPlatformVersionsResponseTypeDef:
        """
        [Client.list_platform_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_versions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_tags_for_resource)
        """

    def rebuild_environment(self, EnvironmentId: str = None, EnvironmentName: str = None) -> None:
        """
        [Client.rebuild_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.rebuild_environment)
        """

    def request_environment_info(
        self,
        InfoType: Literal["tail", "bundle"],
        EnvironmentId: str = None,
        EnvironmentName: str = None,
    ) -> None:
        """
        [Client.request_environment_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.request_environment_info)
        """

    def restart_app_server(self, EnvironmentId: str = None, EnvironmentName: str = None) -> None:
        """
        [Client.restart_app_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.restart_app_server)
        """

    def retrieve_environment_info(
        self,
        InfoType: Literal["tail", "bundle"],
        EnvironmentId: str = None,
        EnvironmentName: str = None,
    ) -> ClientRetrieveEnvironmentInfoResponseTypeDef:
        """
        [Client.retrieve_environment_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.retrieve_environment_info)
        """

    def swap_environment_cnames(
        self,
        SourceEnvironmentId: str = None,
        SourceEnvironmentName: str = None,
        DestinationEnvironmentId: str = None,
        DestinationEnvironmentName: str = None,
    ) -> None:
        """
        [Client.swap_environment_cnames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.swap_environment_cnames)
        """

    def terminate_environment(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        TerminateResources: bool = None,
        ForceTerminate: bool = None,
    ) -> ClientTerminateEnvironmentResponseTypeDef:
        """
        [Client.terminate_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.terminate_environment)
        """

    def update_application(
        self, ApplicationName: str, Description: str = None
    ) -> ClientUpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application)
        """

    def update_application_resource_lifecycle(
        self,
        ApplicationName: str,
        ResourceLifecycleConfig: ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef,
    ) -> ClientUpdateApplicationResourceLifecycleResponseTypeDef:
        """
        [Client.update_application_resource_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_resource_lifecycle)
        """

    def update_application_version(
        self, ApplicationName: str, VersionLabel: str, Description: str = None
    ) -> ClientUpdateApplicationVersionResponseTypeDef:
        """
        [Client.update_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_version)
        """

    def update_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        Description: str = None,
        OptionSettings: List[ClientUpdateConfigurationTemplateOptionSettingsTypeDef] = None,
        OptionsToRemove: List[ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef] = None,
    ) -> ClientUpdateConfigurationTemplateResponseTypeDef:
        """
        [Client.update_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_configuration_template)
        """

    def update_environment(
        self,
        ApplicationName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        Tier: ClientUpdateEnvironmentTierTypeDef = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List[ClientUpdateEnvironmentOptionSettingsTypeDef] = None,
        OptionsToRemove: List[ClientUpdateEnvironmentOptionsToRemoveTypeDef] = None,
    ) -> ClientUpdateEnvironmentResponseTypeDef:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_environment)
        """

    def update_tags_for_resource(
        self,
        ResourceArn: str,
        TagsToAdd: List[ClientUpdateTagsForResourceTagsToAddTypeDef] = None,
        TagsToRemove: List[str] = None,
    ) -> None:
        """
        [Client.update_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_tags_for_resource)
        """

    def validate_configuration_settings(
        self,
        ApplicationName: str,
        OptionSettings: List[ClientValidateConfigurationSettingsOptionSettingsTypeDef],
        TemplateName: str = None,
        EnvironmentName: str = None,
    ) -> ClientValidateConfigurationSettingsResponseTypeDef:
        """
        [Client.validate_configuration_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.validate_configuration_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_application_versions"]
    ) -> "paginator_scope.DescribeApplicationVersionsPaginator":
        """
        [Paginator.DescribeApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environment_managed_action_history"]
    ) -> "paginator_scope.DescribeEnvironmentManagedActionHistoryPaginator":
        """
        [Paginator.DescribeEnvironmentManagedActionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environments"]
    ) -> "paginator_scope.DescribeEnvironmentsPaginator":
        """
        [Paginator.DescribeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_platform_versions"]
    ) -> "paginator_scope.ListPlatformVersionsPaginator":
        """
        [Paginator.ListPlatformVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CodeBuildNotInServiceRegionException: Boto3ClientError
    ElasticBeanstalkServiceException: Boto3ClientError
    InsufficientPrivilegesException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ManagedActionInvalidStateException: Boto3ClientError
    OperationInProgressException: Boto3ClientError
    PlatformVersionStillReferencedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceTypeNotSupportedException: Boto3ClientError
    S3LocationNotInServiceRegionException: Boto3ClientError
    S3SubscriptionRequiredException: Boto3ClientError
    SourceBundleDeletionException: Boto3ClientError
    TooManyApplicationVersionsException: Boto3ClientError
    TooManyApplicationsException: Boto3ClientError
    TooManyBucketsException: Boto3ClientError
    TooManyConfigurationTemplatesException: Boto3ClientError
    TooManyEnvironmentsException: Boto3ClientError
    TooManyPlatformsException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
