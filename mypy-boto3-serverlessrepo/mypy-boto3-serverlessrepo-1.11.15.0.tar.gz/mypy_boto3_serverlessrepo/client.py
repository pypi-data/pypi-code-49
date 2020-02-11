"""
Main interface for serverlessrepo service client

Usage::

    import boto3
    from mypy_boto3.serverlessrepo import ServerlessApplicationRepositoryClient

    session = boto3.Session()

    client: ServerlessApplicationRepositoryClient = boto3.client("serverlessrepo")
    session_client: ServerlessApplicationRepositoryClient = session.client("serverlessrepo")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_serverlessrepo.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_serverlessrepo.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_serverlessrepo.type_defs import (
    ClientCreateApplicationResponseTypeDef,
    ClientCreateApplicationVersionResponseTypeDef,
    ClientCreateCloudFormationChangeSetParameterOverridesTypeDef,
    ClientCreateCloudFormationChangeSetResponseTypeDef,
    ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef,
    ClientCreateCloudFormationChangeSetTagsTypeDef,
    ClientCreateCloudFormationTemplateResponseTypeDef,
    ClientGetApplicationPolicyResponseTypeDef,
    ClientGetApplicationResponseTypeDef,
    ClientGetCloudFormationTemplateResponseTypeDef,
    ClientListApplicationDependenciesResponseTypeDef,
    ClientListApplicationVersionsResponseTypeDef,
    ClientListApplicationsResponseTypeDef,
    ClientPutApplicationPolicyResponseTypeDef,
    ClientPutApplicationPolicyStatementsTypeDef,
    ClientUpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServerlessApplicationRepositoryClient",)


class ServerlessApplicationRepositoryClient:
    """
    [ServerlessApplicationRepository.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.can_paginate)
        """

    def create_application(
        self,
        Author: str,
        Description: str,
        Name: str,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        LicenseBody: str = None,
        LicenseUrl: str = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
        SemanticVersion: str = None,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        SpdxLicenseId: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application)
        """

    def create_application_version(
        self,
        ApplicationId: str,
        SemanticVersion: str,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> ClientCreateApplicationVersionResponseTypeDef:
        """
        [Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application_version)
        """

    def create_cloud_formation_change_set(
        self,
        ApplicationId: str,
        StackName: str,
        Capabilities: List[str] = None,
        ChangeSetName: str = None,
        ClientToken: str = None,
        Description: str = None,
        NotificationArns: List[str] = None,
        ParameterOverrides: List[
            ClientCreateCloudFormationChangeSetParameterOverridesTypeDef
        ] = None,
        ResourceTypes: List[str] = None,
        RollbackConfiguration: ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef = None,
        SemanticVersion: str = None,
        Tags: List[ClientCreateCloudFormationChangeSetTagsTypeDef] = None,
        TemplateId: str = None,
    ) -> ClientCreateCloudFormationChangeSetResponseTypeDef:
        """
        [Client.create_cloud_formation_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_change_set)
        """

    def create_cloud_formation_template(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> ClientCreateCloudFormationTemplateResponseTypeDef:
        """
        [Client.create_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_template)
        """

    def delete_application(self, ApplicationId: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.delete_application)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.generate_presigned_url)
        """

    def get_application(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> ClientGetApplicationResponseTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application)
        """

    def get_application_policy(
        self, ApplicationId: str
    ) -> ClientGetApplicationPolicyResponseTypeDef:
        """
        [Client.get_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application_policy)
        """

    def get_cloud_formation_template(
        self, ApplicationId: str, TemplateId: str
    ) -> ClientGetCloudFormationTemplateResponseTypeDef:
        """
        [Client.get_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_cloud_formation_template)
        """

    def list_application_dependencies(
        self,
        ApplicationId: str,
        MaxItems: int = None,
        NextToken: str = None,
        SemanticVersion: str = None,
    ) -> ClientListApplicationDependenciesResponseTypeDef:
        """
        [Client.list_application_dependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_dependencies)
        """

    def list_application_versions(
        self, ApplicationId: str, MaxItems: int = None, NextToken: str = None
    ) -> ClientListApplicationVersionsResponseTypeDef:
        """
        [Client.list_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_versions)
        """

    def list_applications(
        self, MaxItems: int = None, NextToken: str = None
    ) -> ClientListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_applications)
        """

    def put_application_policy(
        self, ApplicationId: str, Statements: List[ClientPutApplicationPolicyStatementsTypeDef]
    ) -> ClientPutApplicationPolicyResponseTypeDef:
        """
        [Client.put_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.put_application_policy)
        """

    def update_application(
        self,
        ApplicationId: str,
        Author: str = None,
        Description: str = None,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
    ) -> ClientUpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.update_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_dependencies"]
    ) -> "paginator_scope.ListApplicationDependenciesPaginator":
        """
        [Paginator.ListApplicationDependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_versions"]
    ) -> "paginator_scope.ListApplicationVersionsPaginator":
        """
        [Paginator.ListApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> "paginator_scope.ListApplicationsPaginator":
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
