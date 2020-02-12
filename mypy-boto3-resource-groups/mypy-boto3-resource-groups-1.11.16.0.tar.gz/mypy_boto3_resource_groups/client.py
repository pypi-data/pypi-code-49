"""
Main interface for resource-groups service client

Usage::

    import boto3
    from mypy_boto3.resource_groups import ResourceGroupsClient

    session = boto3.Session()

    client: ResourceGroupsClient = boto3.client("resource-groups")
    session_client: ResourceGroupsClient = session.client("resource-groups")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_resource_groups.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_resource_groups.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_resource_groups.type_defs import (
    ClientCreateGroupResourceQueryTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientDeleteGroupResponseTypeDef,
    ClientGetGroupQueryResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientListGroupResourcesFiltersTypeDef,
    ClientListGroupResourcesResponseTypeDef,
    ClientListGroupsFiltersTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientSearchResourcesResourceQueryTypeDef,
    ClientSearchResourcesResponseTypeDef,
    ClientTagResponseTypeDef,
    ClientUntagResponseTypeDef,
    ClientUpdateGroupQueryResourceQueryTypeDef,
    ClientUpdateGroupQueryResponseTypeDef,
    ClientUpdateGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ResourceGroupsClient",)


class ResourceGroupsClient:
    """
    [ResourceGroups.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.can_paginate)
        """

    def create_group(
        self,
        Name: str,
        ResourceQuery: ClientCreateGroupResourceQueryTypeDef,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.create_group)
        """

    def delete_group(self, GroupName: str) -> ClientDeleteGroupResponseTypeDef:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.delete_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.generate_presigned_url)
        """

    def get_group(self, GroupName: str) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.get_group)
        """

    def get_group_query(self, GroupName: str) -> ClientGetGroupQueryResponseTypeDef:
        """
        [Client.get_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.get_group_query)
        """

    def get_tags(self, Arn: str) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.get_tags)
        """

    def list_group_resources(
        self,
        GroupName: str,
        Filters: List[ClientListGroupResourcesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListGroupResourcesResponseTypeDef:
        """
        [Client.list_group_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.list_group_resources)
        """

    def list_groups(
        self,
        Filters: List[ClientListGroupsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.list_groups)
        """

    def search_resources(
        self,
        ResourceQuery: ClientSearchResourcesResourceQueryTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientSearchResourcesResponseTypeDef:
        """
        [Client.search_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.search_resources)
        """

    def tag(self, Arn: str, Tags: Dict[str, str]) -> ClientTagResponseTypeDef:
        """
        [Client.tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.tag)
        """

    def untag(self, Arn: str, Keys: List[str]) -> ClientUntagResponseTypeDef:
        """
        [Client.untag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.untag)
        """

    def update_group(
        self, GroupName: str, Description: str = None
    ) -> ClientUpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.update_group)
        """

    def update_group_query(
        self, GroupName: str, ResourceQuery: ClientUpdateGroupQueryResourceQueryTypeDef
    ) -> ClientUpdateGroupQueryResponseTypeDef:
        """
        [Client.update_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Client.update_group_query)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_resources"]
    ) -> "paginator_scope.ListGroupResourcesPaginator":
        """
        [Paginator.ListGroupResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> "paginator_scope.ListGroupsPaginator":
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> "paginator_scope.SearchResourcesPaginator":
        """
        [Paginator.SearchResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
