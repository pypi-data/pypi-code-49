"""
Main interface for resource-groups service client paginators.

Usage::

    import boto3
    from mypy_boto3.resource_groups import (
        ListGroupResourcesPaginator,
        ListGroupsPaginator,
        SearchResourcesPaginator,
    )

    client: ResourceGroupsClient = boto3.client("resource-groups")

    list_group_resources_paginator: ListGroupResourcesPaginator = client.get_paginator("list_group_resources")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resource_groups.type_defs import (
    GroupFilterTypeDef,
    ListGroupResourcesOutputTypeDef,
    ListGroupsOutputTypeDef,
    PaginatorConfigTypeDef,
    ResourceFilterTypeDef,
    ResourceQueryTypeDef,
    SearchResourcesOutputTypeDef,
)


__all__ = ("ListGroupResourcesPaginator", "ListGroupsPaginator", "SearchResourcesPaginator")


class ListGroupResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)
    """

    def paginate(
        self,
        GroupName: str,
        Filters: List[ResourceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListGroupResourcesOutputTypeDef, None, None]:
        """
        [ListGroupResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)
    """

    def paginate(
        self,
        Filters: List[GroupFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListGroupsOutputTypeDef, None, None]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups.paginate)
        """


class SearchResourcesPaginator(Boto3Paginator):
    """
    [Paginator.SearchResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)
    """

    def paginate(
        self, ResourceQuery: ResourceQueryTypeDef, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[SearchResourcesOutputTypeDef, None, None]:
        """
        [SearchResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources.paginate)
        """
