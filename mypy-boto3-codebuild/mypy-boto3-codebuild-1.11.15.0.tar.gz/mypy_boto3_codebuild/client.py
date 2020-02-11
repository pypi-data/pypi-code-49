"""
Main interface for codebuild service client

Usage::

    import boto3
    from mypy_boto3.codebuild import CodeBuildClient

    session = boto3.Session()

    client: CodeBuildClient = boto3.client("codebuild")
    session_client: CodeBuildClient = session.client("codebuild")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codebuild.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codebuild.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_codebuild.type_defs import (
    ClientBatchDeleteBuildsResponseTypeDef,
    ClientBatchGetBuildsResponseTypeDef,
    ClientBatchGetProjectsResponseTypeDef,
    ClientBatchGetReportGroupsResponseTypeDef,
    ClientBatchGetReportsResponseTypeDef,
    ClientCreateProjectArtifactsTypeDef,
    ClientCreateProjectCacheTypeDef,
    ClientCreateProjectEnvironmentTypeDef,
    ClientCreateProjectFileSystemLocationsTypeDef,
    ClientCreateProjectLogsConfigTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateProjectSecondaryArtifactsTypeDef,
    ClientCreateProjectSecondarySourceVersionsTypeDef,
    ClientCreateProjectSecondarySourcesTypeDef,
    ClientCreateProjectSourceTypeDef,
    ClientCreateProjectTagsTypeDef,
    ClientCreateProjectVpcConfigTypeDef,
    ClientCreateReportGroupExportConfigTypeDef,
    ClientCreateReportGroupResponseTypeDef,
    ClientCreateWebhookFilterGroupsTypeDef,
    ClientCreateWebhookResponseTypeDef,
    ClientDeleteSourceCredentialsResponseTypeDef,
    ClientDescribeTestCasesFilterTypeDef,
    ClientDescribeTestCasesResponseTypeDef,
    ClientGetResourcePolicyResponseTypeDef,
    ClientImportSourceCredentialsResponseTypeDef,
    ClientListBuildsForProjectResponseTypeDef,
    ClientListBuildsResponseTypeDef,
    ClientListCuratedEnvironmentImagesResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientListReportGroupsResponseTypeDef,
    ClientListReportsFilterTypeDef,
    ClientListReportsForReportGroupFilterTypeDef,
    ClientListReportsForReportGroupResponseTypeDef,
    ClientListReportsResponseTypeDef,
    ClientListSharedProjectsResponseTypeDef,
    ClientListSharedReportGroupsResponseTypeDef,
    ClientListSourceCredentialsResponseTypeDef,
    ClientPutResourcePolicyResponseTypeDef,
    ClientStartBuildArtifactsOverrideTypeDef,
    ClientStartBuildCacheOverrideTypeDef,
    ClientStartBuildEnvironmentVariablesOverrideTypeDef,
    ClientStartBuildGitSubmodulesConfigOverrideTypeDef,
    ClientStartBuildLogsConfigOverrideTypeDef,
    ClientStartBuildRegistryCredentialOverrideTypeDef,
    ClientStartBuildResponseTypeDef,
    ClientStartBuildSecondaryArtifactsOverrideTypeDef,
    ClientStartBuildSecondarySourcesOverrideTypeDef,
    ClientStartBuildSecondarySourcesVersionOverrideTypeDef,
    ClientStartBuildSourceAuthOverrideTypeDef,
    ClientStopBuildResponseTypeDef,
    ClientUpdateProjectArtifactsTypeDef,
    ClientUpdateProjectCacheTypeDef,
    ClientUpdateProjectEnvironmentTypeDef,
    ClientUpdateProjectFileSystemLocationsTypeDef,
    ClientUpdateProjectLogsConfigTypeDef,
    ClientUpdateProjectResponseTypeDef,
    ClientUpdateProjectSecondaryArtifactsTypeDef,
    ClientUpdateProjectSecondarySourceVersionsTypeDef,
    ClientUpdateProjectSecondarySourcesTypeDef,
    ClientUpdateProjectSourceTypeDef,
    ClientUpdateProjectTagsTypeDef,
    ClientUpdateProjectVpcConfigTypeDef,
    ClientUpdateReportGroupExportConfigTypeDef,
    ClientUpdateReportGroupResponseTypeDef,
    ClientUpdateWebhookFilterGroupsTypeDef,
    ClientUpdateWebhookResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeBuildClient",)


class CodeBuildClient:
    """
    [CodeBuild.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_delete_builds(self, ids: List[str]) -> ClientBatchDeleteBuildsResponseTypeDef:
        """
        [Client.batch_delete_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)
        """

    def batch_get_builds(self, ids: List[str]) -> ClientBatchGetBuildsResponseTypeDef:
        """
        [Client.batch_get_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)
        """

    def batch_get_projects(self, names: List[str]) -> ClientBatchGetProjectsResponseTypeDef:
        """
        [Client.batch_get_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)
        """

    def batch_get_report_groups(
        self, reportGroupArns: List[str]
    ) -> ClientBatchGetReportGroupsResponseTypeDef:
        """
        [Client.batch_get_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)
        """

    def batch_get_reports(self, reportArns: List[str]) -> ClientBatchGetReportsResponseTypeDef:
        """
        [Client.batch_get_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.can_paginate)
        """

    def create_project(
        self,
        name: str,
        source: ClientCreateProjectSourceTypeDef,
        artifacts: ClientCreateProjectArtifactsTypeDef,
        environment: ClientCreateProjectEnvironmentTypeDef,
        serviceRole: str,
        description: str = None,
        secondarySources: List[ClientCreateProjectSecondarySourcesTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ClientCreateProjectSecondarySourceVersionsTypeDef] = None,
        secondaryArtifacts: List[ClientCreateProjectSecondaryArtifactsTypeDef] = None,
        cache: ClientCreateProjectCacheTypeDef = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[ClientCreateProjectTagsTypeDef] = None,
        vpcConfig: ClientCreateProjectVpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: ClientCreateProjectLogsConfigTypeDef = None,
        fileSystemLocations: List[ClientCreateProjectFileSystemLocationsTypeDef] = None,
    ) -> ClientCreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.create_project)
        """

    def create_report_group(
        self, name: str, type: str, exportConfig: ClientCreateReportGroupExportConfigTypeDef
    ) -> ClientCreateReportGroupResponseTypeDef:
        """
        [Client.create_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.create_report_group)
        """

    def create_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List[ClientCreateWebhookFilterGroupsTypeDef]] = None,
    ) -> ClientCreateWebhookResponseTypeDef:
        """
        [Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.create_webhook)
        """

    def delete_project(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.delete_project)
        """

    def delete_report(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.delete_report)
        """

    def delete_report_group(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)
        """

    def delete_resource_policy(self, resourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.delete_resource_policy)
        """

    def delete_source_credentials(self, arn: str) -> ClientDeleteSourceCredentialsResponseTypeDef:
        """
        [Client.delete_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)
        """

    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)
        """

    def describe_test_cases(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientDescribeTestCasesFilterTypeDef = None,
    ) -> ClientDescribeTestCasesResponseTypeDef:
        """
        [Client.describe_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)
        """

    def get_resource_policy(self, resourceArn: str) -> ClientGetResourcePolicyResponseTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.get_resource_policy)
        """

    def import_source_credentials(
        self,
        token: str,
        serverType: Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        authType: Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> ClientImportSourceCredentialsResponseTypeDef:
        """
        [Client.import_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)
        """

    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.invalidate_project_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)
        """

    def list_builds(
        self, sortOrder: Literal["ASCENDING", "DESCENDING"] = None, nextToken: str = None
    ) -> ClientListBuildsResponseTypeDef:
        """
        [Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_builds)
        """

    def list_builds_for_project(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ClientListBuildsForProjectResponseTypeDef:
        """
        [Client.list_builds_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)
        """

    def list_curated_environment_images(
        self, *args: Any, **kwargs: Any
    ) -> ClientListCuratedEnvironmentImagesResponseTypeDef:
        """
        [Client.list_curated_environment_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)
        """

    def list_projects(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ClientListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_projects)
        """

    def list_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListReportGroupsResponseTypeDef:
        """
        [Client.list_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)
        """

    def list_reports(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientListReportsFilterTypeDef = None,
    ) -> ClientListReportsResponseTypeDef:
        """
        [Client.list_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_reports)
        """

    def list_reports_for_report_group(
        self,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        filter: ClientListReportsForReportGroupFilterTypeDef = None,
    ) -> ClientListReportsForReportGroupResponseTypeDef:
        """
        [Client.list_reports_for_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)
        """

    def list_shared_projects(
        self,
        sortBy: Literal["ARN", "MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListSharedProjectsResponseTypeDef:
        """
        [Client.list_shared_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_shared_projects)
        """

    def list_shared_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["ARN", "MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListSharedReportGroupsResponseTypeDef:
        """
        [Client.list_shared_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_shared_report_groups)
        """

    def list_source_credentials(
        self, *args: Any, **kwargs: Any
    ) -> ClientListSourceCredentialsResponseTypeDef:
        """
        [Client.list_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)
        """

    def put_resource_policy(
        self, policy: str, resourceArn: str
    ) -> ClientPutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.put_resource_policy)
        """

    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List[ClientStartBuildSecondarySourcesOverrideTypeDef] = None,
        secondarySourcesVersionOverride: List[
            ClientStartBuildSecondarySourcesVersionOverrideTypeDef
        ] = None,
        sourceVersion: str = None,
        artifactsOverride: ClientStartBuildArtifactsOverrideTypeDef = None,
        secondaryArtifactsOverride: List[ClientStartBuildSecondaryArtifactsOverrideTypeDef] = None,
        environmentVariablesOverride: List[
            ClientStartBuildEnvironmentVariablesOverrideTypeDef
        ] = None,
        sourceTypeOverride: Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ] = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: ClientStartBuildSourceAuthOverrideTypeDef = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: ClientStartBuildGitSubmodulesConfigOverrideTypeDef = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        environmentTypeOverride: Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ] = None,
        imageOverride: str = None,
        computeTypeOverride: Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ] = None,
        certificateOverride: str = None,
        cacheOverride: ClientStartBuildCacheOverrideTypeDef = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        encryptionKeyOverride: str = None,
        idempotencyToken: str = None,
        logsConfigOverride: ClientStartBuildLogsConfigOverrideTypeDef = None,
        registryCredentialOverride: ClientStartBuildRegistryCredentialOverrideTypeDef = None,
        imagePullCredentialsTypeOverride: Literal["CODEBUILD", "SERVICE_ROLE"] = None,
    ) -> ClientStartBuildResponseTypeDef:
        """
        [Client.start_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.start_build)
        """

    def stop_build(self, id: str) -> ClientStopBuildResponseTypeDef:
        """
        [Client.stop_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.stop_build)
        """

    def update_project(
        self,
        name: str,
        description: str = None,
        source: ClientUpdateProjectSourceTypeDef = None,
        secondarySources: List[ClientUpdateProjectSecondarySourcesTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ClientUpdateProjectSecondarySourceVersionsTypeDef] = None,
        artifacts: ClientUpdateProjectArtifactsTypeDef = None,
        secondaryArtifacts: List[ClientUpdateProjectSecondaryArtifactsTypeDef] = None,
        cache: ClientUpdateProjectCacheTypeDef = None,
        environment: ClientUpdateProjectEnvironmentTypeDef = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[ClientUpdateProjectTagsTypeDef] = None,
        vpcConfig: ClientUpdateProjectVpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: ClientUpdateProjectLogsConfigTypeDef = None,
        fileSystemLocations: List[ClientUpdateProjectFileSystemLocationsTypeDef] = None,
    ) -> ClientUpdateProjectResponseTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.update_project)
        """

    def update_report_group(
        self, arn: str, exportConfig: ClientUpdateReportGroupExportConfigTypeDef = None
    ) -> ClientUpdateReportGroupResponseTypeDef:
        """
        [Client.update_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.update_report_group)
        """

    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List[ClientUpdateWebhookFilterGroupsTypeDef]] = None,
    ) -> ClientUpdateWebhookResponseTypeDef:
        """
        [Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Client.update_webhook)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_builds"]
    ) -> "paginator_scope.ListBuildsPaginator":
        """
        [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> "paginator_scope.ListBuildsForProjectPaginator":
        """
        [Paginator.ListBuildsForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> "paginator_scope.ListProjectsPaginator":
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
        """


class Exceptions:
    AccountLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    OAuthProviderException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
