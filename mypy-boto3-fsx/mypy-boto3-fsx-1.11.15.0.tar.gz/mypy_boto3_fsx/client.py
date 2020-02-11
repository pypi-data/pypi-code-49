"""
Main interface for fsx service client

Usage::

    import boto3
    from mypy_boto3.fsx import FSxClient

    session = boto3.Session()

    client: FSxClient = boto3.client("fsx")
    session_client: FSxClient = session.client("fsx")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_fsx.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_fsx.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_fsx.type_defs import (
    ClientCancelDataRepositoryTaskResponseTypeDef,
    ClientCreateBackupResponseTypeDef,
    ClientCreateBackupTagsTypeDef,
    ClientCreateDataRepositoryTaskReportTypeDef,
    ClientCreateDataRepositoryTaskResponseTypeDef,
    ClientCreateDataRepositoryTaskTagsTypeDef,
    ClientCreateFileSystemFromBackupResponseTypeDef,
    ClientCreateFileSystemFromBackupTagsTypeDef,
    ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef,
    ClientCreateFileSystemLustreConfigurationTypeDef,
    ClientCreateFileSystemResponseTypeDef,
    ClientCreateFileSystemTagsTypeDef,
    ClientCreateFileSystemWindowsConfigurationTypeDef,
    ClientDeleteBackupResponseTypeDef,
    ClientDeleteFileSystemResponseTypeDef,
    ClientDeleteFileSystemWindowsConfigurationTypeDef,
    ClientDescribeBackupsFiltersTypeDef,
    ClientDescribeBackupsResponseTypeDef,
    ClientDescribeDataRepositoryTasksFiltersTypeDef,
    ClientDescribeDataRepositoryTasksResponseTypeDef,
    ClientDescribeFileSystemsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateFileSystemLustreConfigurationTypeDef,
    ClientUpdateFileSystemResponseTypeDef,
    ClientUpdateFileSystemWindowsConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FSxClient",)


class FSxClient:
    """
    [FSx.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.can_paginate)
        """

    def cancel_data_repository_task(
        self, TaskId: str
    ) -> ClientCancelDataRepositoryTaskResponseTypeDef:
        """
        [Client.cancel_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)
        """

    def create_backup(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateBackupTagsTypeDef] = None,
    ) -> ClientCreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.create_backup)
        """

    def create_data_repository_task(
        self,
        Type: str,
        FileSystemId: str,
        Report: ClientCreateDataRepositoryTaskReportTypeDef,
        Paths: List[str] = None,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateDataRepositoryTaskTagsTypeDef] = None,
    ) -> ClientCreateDataRepositoryTaskResponseTypeDef:
        """
        [Client.create_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.create_data_repository_task)
        """

    def create_file_system(
        self,
        FileSystemType: Literal["WINDOWS", "LUSTRE"],
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateFileSystemTagsTypeDef] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: ClientCreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: ClientCreateFileSystemLustreConfigurationTypeDef = None,
    ) -> ClientCreateFileSystemResponseTypeDef:
        """
        [Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.create_file_system)
        """

    def create_file_system_from_backup(
        self,
        BackupId: str,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateFileSystemFromBackupTagsTypeDef] = None,
        WindowsConfiguration: ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = None,
    ) -> ClientCreateFileSystemFromBackupResponseTypeDef:
        """
        [Client.create_file_system_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        """

    def delete_backup(
        self, BackupId: str, ClientRequestToken: str = None
    ) -> ClientDeleteBackupResponseTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.delete_backup)
        """

    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: ClientDeleteFileSystemWindowsConfigurationTypeDef = None,
    ) -> ClientDeleteFileSystemResponseTypeDef:
        """
        [Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.delete_file_system)
        """

    def describe_backups(
        self,
        BackupIds: List[str] = None,
        Filters: List[ClientDescribeBackupsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.describe_backups)
        """

    def describe_data_repository_tasks(
        self,
        TaskIds: List[str] = None,
        Filters: List[ClientDescribeDataRepositoryTasksFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeDataRepositoryTasksResponseTypeDef:
        """
        [Client.describe_data_repository_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)
        """

    def describe_file_systems(
        self, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeFileSystemsResponseTypeDef:
        """
        [Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.describe_file_systems)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.untag_resource)
        """

    def update_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: ClientUpdateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: ClientUpdateFileSystemLustreConfigurationTypeDef = None,
    ) -> ClientUpdateFileSystemResponseTypeDef:
        """
        [Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Client.update_file_system)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> "paginator_scope.DescribeBackupsPaginator":
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> "paginator_scope.DescribeFileSystemsPaginator":
        """
        [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
        """


class Exceptions:
    ActiveDirectoryError: Boto3ClientError
    BackupInProgress: Boto3ClientError
    BackupNotFound: Boto3ClientError
    BackupRestoring: Boto3ClientError
    BadRequest: Boto3ClientError
    ClientError: Boto3ClientError
    DataRepositoryTaskEnded: Boto3ClientError
    DataRepositoryTaskExecuting: Boto3ClientError
    DataRepositoryTaskNotFound: Boto3ClientError
    FileSystemNotFound: Boto3ClientError
    IncompatibleParameterError: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidExportPath: Boto3ClientError
    InvalidImportPath: Boto3ClientError
    InvalidNetworkSettings: Boto3ClientError
    MissingFileSystemConfiguration: Boto3ClientError
    NotServiceResourceError: Boto3ClientError
    ResourceDoesNotSupportTagging: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    ServiceLimitExceeded: Boto3ClientError
    UnsupportedOperation: Boto3ClientError
