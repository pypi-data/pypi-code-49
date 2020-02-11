"""
Main interface for mgh service client

Usage::

    import boto3
    from mypy_boto3.mgh import MigrationHubClient

    session = boto3.Session()

    client: MigrationHubClient = boto3.client("mgh")
    session_client: MigrationHubClient = session.client("mgh")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mgh.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mgh.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_mgh.type_defs import (
    ClientAssociateCreatedArtifactCreatedArtifactTypeDef,
    ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
    ClientDescribeApplicationStateResponseTypeDef,
    ClientDescribeMigrationTaskResponseTypeDef,
    ClientListApplicationStatesResponseTypeDef,
    ClientListCreatedArtifactsResponseTypeDef,
    ClientListDiscoveredResourcesResponseTypeDef,
    ClientListMigrationTasksResponseTypeDef,
    ClientListProgressUpdateStreamsResponseTypeDef,
    ClientNotifyMigrationTaskStateTaskTypeDef,
    ClientPutResourceAttributesResourceAttributeListTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MigrationHubClient",)


class MigrationHubClient:
    """
    [MigrationHub.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_created_artifact(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifact: ClientAssociateCreatedArtifactCreatedArtifactTypeDef,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_created_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.associate_created_artifact)
        """

    def associate_discovered_resource(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        DiscoveredResource: ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_discovered_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.associate_discovered_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.can_paginate)
        """

    def create_progress_update_stream(
        self, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.create_progress_update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.create_progress_update_stream)
        """

    def delete_progress_update_stream(
        self, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_progress_update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.delete_progress_update_stream)
        """

    def describe_application_state(
        self, ApplicationId: str
    ) -> ClientDescribeApplicationStateResponseTypeDef:
        """
        [Client.describe_application_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.describe_application_state)
        """

    def describe_migration_task(
        self, ProgressUpdateStream: str, MigrationTaskName: str
    ) -> ClientDescribeMigrationTaskResponseTypeDef:
        """
        [Client.describe_migration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.describe_migration_task)
        """

    def disassociate_created_artifact(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifactName: str,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_created_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.disassociate_created_artifact)
        """

    def disassociate_discovered_resource(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ConfigurationId: str,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_discovered_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.disassociate_discovered_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.generate_presigned_url)
        """

    def import_migration_task(
        self, ProgressUpdateStream: str, MigrationTaskName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.import_migration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.import_migration_task)
        """

    def list_application_states(
        self, ApplicationIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListApplicationStatesResponseTypeDef:
        """
        [Client.list_application_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.list_application_states)
        """

    def list_created_artifacts(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListCreatedArtifactsResponseTypeDef:
        """
        [Client.list_created_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.list_created_artifacts)
        """

    def list_discovered_resources(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDiscoveredResourcesResponseTypeDef:
        """
        [Client.list_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.list_discovered_resources)
        """

    def list_migration_tasks(
        self, NextToken: str = None, MaxResults: int = None, ResourceName: str = None
    ) -> ClientListMigrationTasksResponseTypeDef:
        """
        [Client.list_migration_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.list_migration_tasks)
        """

    def list_progress_update_streams(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListProgressUpdateStreamsResponseTypeDef:
        """
        [Client.list_progress_update_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.list_progress_update_streams)
        """

    def notify_application_state(
        self,
        ApplicationId: str,
        Status: Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        UpdateDateTime: datetime = None,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.notify_application_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.notify_application_state)
        """

    def notify_migration_task_state(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        Task: ClientNotifyMigrationTaskStateTaskTypeDef,
        UpdateDateTime: datetime,
        NextUpdateSeconds: int,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.notify_migration_task_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.notify_migration_task_state)
        """

    def put_resource_attributes(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ResourceAttributeList: List[ClientPutResourceAttributesResourceAttributeListTypeDef],
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_resource_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Client.put_resource_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_states"]
    ) -> "paginator_scope.ListApplicationStatesPaginator":
        """
        [Paginator.ListApplicationStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Paginator.ListApplicationStates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_created_artifacts"]
    ) -> "paginator_scope.ListCreatedArtifactsPaginator":
        """
        [Paginator.ListCreatedArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discovered_resources"]
    ) -> "paginator_scope.ListDiscoveredResourcesPaginator":
        """
        [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_migration_tasks"]
    ) -> "paginator_scope.ListMigrationTasksPaginator":
        """
        [Paginator.ListMigrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_progress_update_streams"]
    ) -> "paginator_scope.ListProgressUpdateStreamsPaginator":
        """
        [Paginator.ListProgressUpdateStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    DryRunOperation: Boto3ClientError
    HomeRegionNotSetException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    PolicyErrorException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    UnauthorizedOperation: Boto3ClientError
