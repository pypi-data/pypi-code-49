"""
Main interface for amplify service client paginators.

Usage::

    import boto3
    from mypy_boto3.amplify import (
        ListAppsPaginator,
        ListBranchesPaginator,
        ListDomainAssociationsPaginator,
        ListJobsPaginator,
    )

    client: AmplifyClient = boto3.client("amplify")

    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_branches_paginator: ListBranchesPaginator = client.get_paginator("list_branches")
    list_domain_associations_paginator: ListDomainAssociationsPaginator = client.get_paginator("list_domain_associations")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_amplify.type_defs import (
    ListAppsResultTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)


class ListAppsPaginator(Boto3Paginator):
    """
    [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListApps)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAppsResultTypeDef, None, None]:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListApps.paginate)
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListBranches)
    """

    def paginate(
        self, appId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBranchesResultTypeDef, None, None]:
        """
        [ListBranches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListBranches.paginate)
        """


class ListDomainAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)
    """

    def paginate(
        self, appId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainAssociationsResultTypeDef, None, None]:
        """
        [ListDomainAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListJobs)
    """

    def paginate(
        self, appId: str, branchName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsResultTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/amplify.html#Amplify.Paginator.ListJobs.paginate)
        """
