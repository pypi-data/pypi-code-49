"""
Main interface for appconfig service client

Usage::

    import boto3
    from mypy_boto3.appconfig import AppConfigClient

    session = boto3.Session()

    client: AppConfigClient = boto3.client("appconfig")
    session_client: AppConfigClient = session.client("appconfig")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_appconfig.client as client_scope
else:
    client_scope = object
from mypy_boto3_appconfig.type_defs import (
    ClientCreateApplicationResponseTypeDef,
    ClientCreateConfigurationProfileResponseTypeDef,
    ClientCreateConfigurationProfileValidatorsTypeDef,
    ClientCreateDeploymentStrategyResponseTypeDef,
    ClientCreateEnvironmentMonitorsTypeDef,
    ClientCreateEnvironmentResponseTypeDef,
    ClientGetApplicationResponseTypeDef,
    ClientGetConfigurationProfileResponseTypeDef,
    ClientGetConfigurationResponseTypeDef,
    ClientGetDeploymentResponseTypeDef,
    ClientGetDeploymentStrategyResponseTypeDef,
    ClientGetEnvironmentResponseTypeDef,
    ClientListApplicationsResponseTypeDef,
    ClientListConfigurationProfilesResponseTypeDef,
    ClientListDeploymentStrategiesResponseTypeDef,
    ClientListDeploymentsResponseTypeDef,
    ClientListEnvironmentsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientStartDeploymentResponseTypeDef,
    ClientStopDeploymentResponseTypeDef,
    ClientUpdateApplicationResponseTypeDef,
    ClientUpdateConfigurationProfileResponseTypeDef,
    ClientUpdateConfigurationProfileValidatorsTypeDef,
    ClientUpdateDeploymentStrategyResponseTypeDef,
    ClientUpdateEnvironmentMonitorsTypeDef,
    ClientUpdateEnvironmentResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppConfigClient",)


class AppConfigClient:
    """
    [AppConfig.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.can_paginate)
        """

    def create_application(
        self, Name: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.create_application)
        """

    def create_configuration_profile(
        self,
        ApplicationId: str,
        Name: str,
        LocationUri: str,
        RetrievalRoleArn: str,
        Description: str = None,
        Validators: List[ClientCreateConfigurationProfileValidatorsTypeDef] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateConfigurationProfileResponseTypeDef:
        """
        [Client.create_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)
        """

    def create_deployment_strategy(
        self,
        Name: str,
        DeploymentDurationInMinutes: int,
        GrowthFactor: Any,
        ReplicateTo: Literal["NONE", "SSM_DOCUMENT"],
        Description: str = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthType: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateDeploymentStrategyResponseTypeDef:
        """
        [Client.create_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)
        """

    def create_environment(
        self,
        ApplicationId: str,
        Name: str,
        Description: str = None,
        Monitors: List[ClientCreateEnvironmentMonitorsTypeDef] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateEnvironmentResponseTypeDef:
        """
        [Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.create_environment)
        """

    def delete_application(self, ApplicationId: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.delete_application)
        """

    def delete_configuration_profile(self, ApplicationId: str, ConfigurationProfileId: str) -> None:
        """
        [Client.delete_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)
        """

    def delete_deployment_strategy(self, DeploymentStrategyId: str) -> None:
        """
        [Client.delete_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)
        """

    def delete_environment(self, ApplicationId: str, EnvironmentId: str) -> None:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.delete_environment)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)
        """

    def get_application(self, ApplicationId: str) -> ClientGetApplicationResponseTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.get_application)
        """

    def get_configuration(
        self,
        Application: str,
        Environment: str,
        Configuration: str,
        ClientId: str,
        ClientConfigurationVersion: str = None,
    ) -> ClientGetConfigurationResponseTypeDef:
        """
        [Client.get_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.get_configuration)
        """

    def get_configuration_profile(
        self, ApplicationId: str, ConfigurationProfileId: str
    ) -> ClientGetConfigurationProfileResponseTypeDef:
        """
        [Client.get_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)
        """

    def get_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> ClientGetDeploymentResponseTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.get_deployment)
        """

    def get_deployment_strategy(
        self, DeploymentStrategyId: str
    ) -> ClientGetDeploymentStrategyResponseTypeDef:
        """
        [Client.get_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)
        """

    def get_environment(
        self, ApplicationId: str, EnvironmentId: str
    ) -> ClientGetEnvironmentResponseTypeDef:
        """
        [Client.get_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.get_environment)
        """

    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.list_applications)
        """

    def list_configuration_profiles(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationProfilesResponseTypeDef:
        """
        [Client.list_configuration_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)
        """

    def list_deployment_strategies(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDeploymentStrategiesResponseTypeDef:
        """
        [Client.list_deployment_strategies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)
        """

    def list_deployments(
        self, ApplicationId: str, EnvironmentId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDeploymentsResponseTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.list_deployments)
        """

    def list_environments(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListEnvironmentsResponseTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.list_environments)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)
        """

    def start_deployment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        DeploymentStrategyId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientStartDeploymentResponseTypeDef:
        """
        [Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.start_deployment)
        """

    def stop_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> ClientStopDeploymentResponseTypeDef:
        """
        [Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.stop_deployment)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.untag_resource)
        """

    def update_application(
        self, ApplicationId: str, Name: str = None, Description: str = None
    ) -> ClientUpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.update_application)
        """

    def update_configuration_profile(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Name: str = None,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List[ClientUpdateConfigurationProfileValidatorsTypeDef] = None,
    ) -> ClientUpdateConfigurationProfileResponseTypeDef:
        """
        [Client.update_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)
        """

    def update_deployment_strategy(
        self,
        DeploymentStrategyId: str,
        Description: str = None,
        DeploymentDurationInMinutes: int = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthFactor: Any = None,
        GrowthType: str = None,
    ) -> ClientUpdateDeploymentStrategyResponseTypeDef:
        """
        [Client.update_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)
        """

    def update_environment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        Name: str = None,
        Description: str = None,
        Monitors: List[ClientUpdateEnvironmentMonitorsTypeDef] = None,
    ) -> ClientUpdateEnvironmentResponseTypeDef:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.update_environment)
        """

    def validate_configuration(
        self, ApplicationId: str, ConfigurationProfileId: str, ConfigurationVersion: str
    ) -> None:
        """
        [Client.validate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appconfig.html#AppConfig.Client.validate_configuration)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
