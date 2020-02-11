"""
Main interface for iot1click-projects service client paginators.

Usage::

    import boto3
    from mypy_boto3.iot1click_projects import (
        ListPlacementsPaginator,
        ListProjectsPaginator,
    )

    client: IoT1ClickProjectsClient = boto3.client("iot1click-projects")

    list_placements_paginator: ListPlacementsPaginator = client.get_paginator("list_placements")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot1click_projects.type_defs import (
    ListPlacementsResponseTypeDef,
    ListProjectsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListPlacementsPaginator", "ListProjectsPaginator")


class ListPlacementsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlacements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)
    """

    def paginate(
        self, projectName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPlacementsResponseTypeDef, None, None]:
        """
        [ListPlacements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProjectsResponseTypeDef, None, None]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects.paginate)
        """
