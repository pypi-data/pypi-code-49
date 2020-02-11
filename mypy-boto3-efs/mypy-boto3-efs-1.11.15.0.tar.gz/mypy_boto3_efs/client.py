"""
Main interface for efs service client

Usage::

    import boto3
    from mypy_boto3.efs import EFSClient

    session = boto3.Session()

    client: EFSClient = boto3.client("efs")
    session_client: EFSClient = session.client("efs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_efs.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_efs.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_efs.type_defs import (
    ClientCreateAccessPointPosixUserTypeDef,
    ClientCreateAccessPointResponseTypeDef,
    ClientCreateAccessPointRootDirectoryTypeDef,
    ClientCreateAccessPointTagsTypeDef,
    ClientCreateFileSystemResponseTypeDef,
    ClientCreateFileSystemTagsTypeDef,
    ClientCreateMountTargetResponseTypeDef,
    ClientCreateTagsTagsTypeDef,
    ClientDescribeAccessPointsResponseTypeDef,
    ClientDescribeFileSystemPolicyResponseTypeDef,
    ClientDescribeFileSystemsResponseTypeDef,
    ClientDescribeLifecycleConfigurationResponseTypeDef,
    ClientDescribeMountTargetSecurityGroupsResponseTypeDef,
    ClientDescribeMountTargetsResponseTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutFileSystemPolicyResponseTypeDef,
    ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef,
    ClientPutLifecycleConfigurationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateFileSystemResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EFSClient",)


class EFSClient:
    """
    [EFS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.can_paginate)
        """

    def create_access_point(
        self,
        ClientToken: str,
        FileSystemId: str,
        Tags: List[ClientCreateAccessPointTagsTypeDef] = None,
        PosixUser: ClientCreateAccessPointPosixUserTypeDef = None,
        RootDirectory: ClientCreateAccessPointRootDirectoryTypeDef = None,
    ) -> ClientCreateAccessPointResponseTypeDef:
        """
        [Client.create_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.create_access_point)
        """

    def create_file_system(
        self,
        CreationToken: str,
        PerformanceMode: Literal["generalPurpose", "maxIO"] = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        ThroughputMode: Literal["bursting", "provisioned"] = None,
        ProvisionedThroughputInMibps: float = None,
        Tags: List[ClientCreateFileSystemTagsTypeDef] = None,
    ) -> ClientCreateFileSystemResponseTypeDef:
        """
        [Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.create_file_system)
        """

    def create_mount_target(
        self,
        FileSystemId: str,
        SubnetId: str,
        IpAddress: str = None,
        SecurityGroups: List[str] = None,
    ) -> ClientCreateMountTargetResponseTypeDef:
        """
        [Client.create_mount_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.create_mount_target)
        """

    def create_tags(self, FileSystemId: str, Tags: List[ClientCreateTagsTagsTypeDef]) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.create_tags)
        """

    def delete_access_point(self, AccessPointId: str) -> None:
        """
        [Client.delete_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.delete_access_point)
        """

    def delete_file_system(self, FileSystemId: str) -> None:
        """
        [Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.delete_file_system)
        """

    def delete_file_system_policy(self, FileSystemId: str) -> None:
        """
        [Client.delete_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.delete_file_system_policy)
        """

    def delete_mount_target(self, MountTargetId: str) -> None:
        """
        [Client.delete_mount_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.delete_mount_target)
        """

    def delete_tags(self, FileSystemId: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.delete_tags)
        """

    def describe_access_points(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        AccessPointId: str = None,
        FileSystemId: str = None,
    ) -> ClientDescribeAccessPointsResponseTypeDef:
        """
        [Client.describe_access_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_access_points)
        """

    def describe_file_system_policy(
        self, FileSystemId: str
    ) -> ClientDescribeFileSystemPolicyResponseTypeDef:
        """
        [Client.describe_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_file_system_policy)
        """

    def describe_file_systems(
        self,
        MaxItems: int = None,
        Marker: str = None,
        CreationToken: str = None,
        FileSystemId: str = None,
    ) -> ClientDescribeFileSystemsResponseTypeDef:
        """
        [Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_file_systems)
        """

    def describe_lifecycle_configuration(
        self, FileSystemId: str
    ) -> ClientDescribeLifecycleConfigurationResponseTypeDef:
        """
        [Client.describe_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_lifecycle_configuration)
        """

    def describe_mount_target_security_groups(
        self, MountTargetId: str
    ) -> ClientDescribeMountTargetSecurityGroupsResponseTypeDef:
        """
        [Client.describe_mount_target_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_mount_target_security_groups)
        """

    def describe_mount_targets(
        self,
        MaxItems: int = None,
        Marker: str = None,
        FileSystemId: str = None,
        MountTargetId: str = None,
        AccessPointId: str = None,
    ) -> ClientDescribeMountTargetsResponseTypeDef:
        """
        [Client.describe_mount_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_mount_targets)
        """

    def describe_tags(
        self, FileSystemId: str, MaxItems: int = None, Marker: str = None
    ) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.describe_tags)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.list_tags_for_resource)
        """

    def modify_mount_target_security_groups(
        self, MountTargetId: str, SecurityGroups: List[str] = None
    ) -> None:
        """
        [Client.modify_mount_target_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.modify_mount_target_security_groups)
        """

    def put_file_system_policy(
        self, FileSystemId: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None
    ) -> ClientPutFileSystemPolicyResponseTypeDef:
        """
        [Client.put_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.put_file_system_policy)
        """

    def put_lifecycle_configuration(
        self,
        FileSystemId: str,
        LifecyclePolicies: List[ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef],
    ) -> ClientPutLifecycleConfigurationResponseTypeDef:
        """
        [Client.put_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.put_lifecycle_configuration)
        """

    def tag_resource(self, ResourceId: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.tag_resource)
        """

    def untag_resource(self, ResourceId: str, TagKeys: List[str] = None) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.untag_resource)
        """

    def update_file_system(
        self,
        FileSystemId: str,
        ThroughputMode: Literal["bursting", "provisioned"] = None,
        ProvisionedThroughputInMibps: float = None,
    ) -> ClientUpdateFileSystemResponseTypeDef:
        """
        [Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Client.update_file_system)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> "paginator_scope.DescribeFileSystemsPaginator":
        """
        [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_mount_targets"]
    ) -> "paginator_scope.DescribeMountTargetsPaginator":
        """
        [Paginator.DescribeMountTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> "paginator_scope.DescribeTagsPaginator":
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/efs.html#EFS.Paginator.DescribeTags)
        """


class Exceptions:
    AccessPointAlreadyExists: Boto3ClientError
    AccessPointLimitExceeded: Boto3ClientError
    AccessPointNotFound: Boto3ClientError
    BadRequest: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyTimeout: Boto3ClientError
    FileSystemAlreadyExists: Boto3ClientError
    FileSystemInUse: Boto3ClientError
    FileSystemLimitExceeded: Boto3ClientError
    FileSystemNotFound: Boto3ClientError
    IncorrectFileSystemLifeCycleState: Boto3ClientError
    IncorrectMountTargetState: Boto3ClientError
    InsufficientThroughputCapacity: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidPolicyException: Boto3ClientError
    IpAddressInUse: Boto3ClientError
    MountTargetConflict: Boto3ClientError
    MountTargetNotFound: Boto3ClientError
    NetworkInterfaceLimitExceeded: Boto3ClientError
    NoFreeAddressesInSubnet: Boto3ClientError
    PolicyNotFound: Boto3ClientError
    SecurityGroupLimitExceeded: Boto3ClientError
    SecurityGroupNotFound: Boto3ClientError
    SubnetNotFound: Boto3ClientError
    ThroughputLimitExceeded: Boto3ClientError
    TooManyRequests: Boto3ClientError
    UnsupportedAvailabilityZone: Boto3ClientError
