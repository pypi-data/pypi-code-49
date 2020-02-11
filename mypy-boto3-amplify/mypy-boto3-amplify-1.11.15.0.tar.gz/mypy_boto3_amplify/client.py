"""
Main interface for amplify service client

Usage::

    import boto3
    from mypy_boto3.amplify import AmplifyClient

    session = boto3.Session()

    client: AmplifyClient = boto3.client("amplify")
    session_client: AmplifyClient = session.client("amplify")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_amplify.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_amplify.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_amplify.type_defs import (
    ClientCreateAppAutoBranchCreationConfigTypeDef,
    ClientCreateAppCustomRulesTypeDef,
    ClientCreateAppResponseTypeDef,
    ClientCreateBackendEnvironmentResponseTypeDef,
    ClientCreateBranchResponseTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDomainAssociationResponseTypeDef,
    ClientCreateDomainAssociationSubDomainSettingsTypeDef,
    ClientCreateWebhookResponseTypeDef,
    ClientDeleteAppResponseTypeDef,
    ClientDeleteBackendEnvironmentResponseTypeDef,
    ClientDeleteBranchResponseTypeDef,
    ClientDeleteDomainAssociationResponseTypeDef,
    ClientDeleteJobResponseTypeDef,
    ClientDeleteWebhookResponseTypeDef,
    ClientGenerateAccessLogsResponseTypeDef,
    ClientGetAppResponseTypeDef,
    ClientGetArtifactUrlResponseTypeDef,
    ClientGetBackendEnvironmentResponseTypeDef,
    ClientGetBranchResponseTypeDef,
    ClientGetDomainAssociationResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetWebhookResponseTypeDef,
    ClientListAppsResponseTypeDef,
    ClientListArtifactsResponseTypeDef,
    ClientListBackendEnvironmentsResponseTypeDef,
    ClientListBranchesResponseTypeDef,
    ClientListDomainAssociationsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWebhooksResponseTypeDef,
    ClientStartDeploymentResponseTypeDef,
    ClientStartJobResponseTypeDef,
    ClientStopJobResponseTypeDef,
    ClientUpdateAppAutoBranchCreationConfigTypeDef,
    ClientUpdateAppCustomRulesTypeDef,
    ClientUpdateAppResponseTypeDef,
    ClientUpdateBranchResponseTypeDef,
    ClientUpdateDomainAssociationResponseTypeDef,
    ClientUpdateDomainAssociationSubDomainSettingsTypeDef,
    ClientUpdateWebhookResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AmplifyClient",)


class AmplifyClient:
    """
    [Amplify.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.can_paginate)
        """

    def create_app(
        self,
        name: str,
        description: str = None,
        repository: str = None,
        platform: str = None,
        iamServiceRoleArn: str = None,
        oauthToken: str = None,
        accessToken: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[ClientCreateAppCustomRulesTypeDef] = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: ClientCreateAppAutoBranchCreationConfigTypeDef = None,
    ) -> ClientCreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.create_app)
        """

    def create_backend_environment(
        self,
        appId: str,
        environmentName: str,
        stackName: str = None,
        deploymentArtifacts: str = None,
    ) -> ClientCreateBackendEnvironmentResponseTypeDef:
        """
        [Client.create_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.create_backend_environment)
        """

    def create_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        stage: Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"] = None,
        framework: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> ClientCreateBranchResponseTypeDef:
        """
        [Client.create_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.create_branch)
        """

    def create_deployment(
        self, appId: str, branchName: str, fileMap: Dict[str, str] = None
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.create_deployment)
        """

    def create_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[ClientCreateDomainAssociationSubDomainSettingsTypeDef],
        enableAutoSubDomain: bool = None,
    ) -> ClientCreateDomainAssociationResponseTypeDef:
        """
        [Client.create_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.create_domain_association)
        """

    def create_webhook(
        self, appId: str, branchName: str, description: str = None
    ) -> ClientCreateWebhookResponseTypeDef:
        """
        [Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.create_webhook)
        """

    def delete_app(self, appId: str) -> ClientDeleteAppResponseTypeDef:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.delete_app)
        """

    def delete_backend_environment(
        self, appId: str, environmentName: str
    ) -> ClientDeleteBackendEnvironmentResponseTypeDef:
        """
        [Client.delete_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.delete_backend_environment)
        """

    def delete_branch(self, appId: str, branchName: str) -> ClientDeleteBranchResponseTypeDef:
        """
        [Client.delete_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.delete_branch)
        """

    def delete_domain_association(
        self, appId: str, domainName: str
    ) -> ClientDeleteDomainAssociationResponseTypeDef:
        """
        [Client.delete_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.delete_domain_association)
        """

    def delete_job(self, appId: str, branchName: str, jobId: str) -> ClientDeleteJobResponseTypeDef:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.delete_job)
        """

    def delete_webhook(self, webhookId: str) -> ClientDeleteWebhookResponseTypeDef:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.delete_webhook)
        """

    def generate_access_logs(
        self, domainName: str, appId: str, startTime: datetime = None, endTime: datetime = None
    ) -> ClientGenerateAccessLogsResponseTypeDef:
        """
        [Client.generate_access_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.generate_access_logs)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.generate_presigned_url)
        """

    def get_app(self, appId: str) -> ClientGetAppResponseTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_app)
        """

    def get_artifact_url(self, artifactId: str) -> ClientGetArtifactUrlResponseTypeDef:
        """
        [Client.get_artifact_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_artifact_url)
        """

    def get_backend_environment(
        self, appId: str, environmentName: str
    ) -> ClientGetBackendEnvironmentResponseTypeDef:
        """
        [Client.get_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_backend_environment)
        """

    def get_branch(self, appId: str, branchName: str) -> ClientGetBranchResponseTypeDef:
        """
        [Client.get_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_branch)
        """

    def get_domain_association(
        self, appId: str, domainName: str
    ) -> ClientGetDomainAssociationResponseTypeDef:
        """
        [Client.get_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_domain_association)
        """

    def get_job(self, appId: str, branchName: str, jobId: str) -> ClientGetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_job)
        """

    def get_webhook(self, webhookId: str) -> ClientGetWebhookResponseTypeDef:
        """
        [Client.get_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.get_webhook)
        """

    def list_apps(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListAppsResponseTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_apps)
        """

    def list_artifacts(
        self, appId: str, branchName: str, jobId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListArtifactsResponseTypeDef:
        """
        [Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_artifacts)
        """

    def list_backend_environments(
        self, appId: str, environmentName: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListBackendEnvironmentsResponseTypeDef:
        """
        [Client.list_backend_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_backend_environments)
        """

    def list_branches(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListBranchesResponseTypeDef:
        """
        [Client.list_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_branches)
        """

    def list_domain_associations(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListDomainAssociationsResponseTypeDef:
        """
        [Client.list_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_domain_associations)
        """

    def list_jobs(
        self, appId: str, branchName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_jobs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_tags_for_resource)
        """

    def list_webhooks(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListWebhooksResponseTypeDef:
        """
        [Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.list_webhooks)
        """

    def start_deployment(
        self, appId: str, branchName: str, jobId: str = None, sourceUrl: str = None
    ) -> ClientStartDeploymentResponseTypeDef:
        """
        [Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.start_deployment)
        """

    def start_job(
        self,
        appId: str,
        branchName: str,
        jobType: Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
        jobId: str = None,
        jobReason: str = None,
        commitId: str = None,
        commitMessage: str = None,
        commitTime: datetime = None,
    ) -> ClientStartJobResponseTypeDef:
        """
        [Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.start_job)
        """

    def stop_job(self, appId: str, branchName: str, jobId: str) -> ClientStopJobResponseTypeDef:
        """
        [Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.stop_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.untag_resource)
        """

    def update_app(
        self,
        appId: str,
        name: str = None,
        description: str = None,
        platform: str = None,
        iamServiceRoleArn: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[ClientUpdateAppCustomRulesTypeDef] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: ClientUpdateAppAutoBranchCreationConfigTypeDef = None,
        repository: str = None,
        oauthToken: str = None,
        accessToken: str = None,
    ) -> ClientUpdateAppResponseTypeDef:
        """
        [Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.update_app)
        """

    def update_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        framework: str = None,
        stage: Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"] = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> ClientUpdateBranchResponseTypeDef:
        """
        [Client.update_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.update_branch)
        """

    def update_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[ClientUpdateDomainAssociationSubDomainSettingsTypeDef],
        enableAutoSubDomain: bool = None,
    ) -> ClientUpdateDomainAssociationResponseTypeDef:
        """
        [Client.update_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.update_domain_association)
        """

    def update_webhook(
        self, webhookId: str, branchName: str = None, description: str = None
    ) -> ClientUpdateWebhookResponseTypeDef:
        """
        [Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Client.update_webhook)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_apps"]
    ) -> "paginator_scope.ListAppsPaginator":
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListApps)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_branches"]
    ) -> "paginator_scope.ListBranchesPaginator":
        """
        [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListBranches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domain_associations"]
    ) -> "paginator_scope.ListDomainAssociationsPaginator":
        """
        [Paginator.ListDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListJobs)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    DependentServiceFailureException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
