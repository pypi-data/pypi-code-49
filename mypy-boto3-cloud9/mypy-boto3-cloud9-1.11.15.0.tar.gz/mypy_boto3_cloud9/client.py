"""
Main interface for cloud9 service client

Usage::

    import boto3
    from mypy_boto3.cloud9 import Cloud9Client

    session = boto3.Session()

    client: Cloud9Client = boto3.client("cloud9")
    session_client: Cloud9Client = session.client("cloud9")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloud9.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloud9.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_cloud9.type_defs import (
    ClientCreateEnvironmentEc2ResponseTypeDef,
    ClientCreateEnvironmentMembershipResponseTypeDef,
    ClientDescribeEnvironmentMembershipsResponseTypeDef,
    ClientDescribeEnvironmentStatusResponseTypeDef,
    ClientDescribeEnvironmentsResponseTypeDef,
    ClientListEnvironmentsResponseTypeDef,
    ClientUpdateEnvironmentMembershipResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Cloud9Client",)


class Cloud9Client:
    """
    [Cloud9.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.can_paginate)
        """

    def create_environment_ec2(
        self,
        name: str,
        instanceType: str,
        description: str = None,
        clientRequestToken: str = None,
        subnetId: str = None,
        automaticStopTimeMinutes: int = None,
        ownerArn: str = None,
    ) -> ClientCreateEnvironmentEc2ResponseTypeDef:
        """
        [Client.create_environment_ec2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)
        """

    def create_environment_membership(
        self, environmentId: str, userArn: str, permissions: Literal["read-write", "read-only"]
    ) -> ClientCreateEnvironmentMembershipResponseTypeDef:
        """
        [Client.create_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.create_environment_membership)
        """

    def delete_environment(self, environmentId: str) -> Dict[str, Any]:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.delete_environment)
        """

    def delete_environment_membership(self, environmentId: str, userArn: str) -> Dict[str, Any]:
        """
        [Client.delete_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)
        """

    def describe_environment_memberships(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Literal["owner", "read-write", "read-only"]] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeEnvironmentMembershipsResponseTypeDef:
        """
        [Client.describe_environment_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.describe_environment_memberships)
        """

    def describe_environment_status(
        self, environmentId: str
    ) -> ClientDescribeEnvironmentStatusResponseTypeDef:
        """
        [Client.describe_environment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.describe_environment_status)
        """

    def describe_environments(
        self, environmentIds: List[str]
    ) -> ClientDescribeEnvironmentsResponseTypeDef:
        """
        [Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.describe_environments)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.generate_presigned_url)
        """

    def list_environments(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListEnvironmentsResponseTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.list_environments)
        """

    def update_environment(
        self, environmentId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.update_environment)
        """

    def update_environment_membership(
        self, environmentId: str, userArn: str, permissions: Literal["read-write", "read-only"]
    ) -> ClientUpdateEnvironmentMembershipResponseTypeDef:
        """
        [Client.update_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Client.update_environment_membership)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environment_memberships"]
    ) -> "paginator_scope.DescribeEnvironmentMembershipsPaginator":
        """
        [Paginator.DescribeEnvironmentMemberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> "paginator_scope.ListEnvironmentsPaginator":
        """
        [Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
