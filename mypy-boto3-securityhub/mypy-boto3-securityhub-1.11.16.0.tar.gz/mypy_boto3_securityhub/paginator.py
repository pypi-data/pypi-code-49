"""
Main interface for securityhub service client paginators.

Usage::

    import boto3
    from mypy_boto3.securityhub import (
        GetEnabledStandardsPaginator,
        GetFindingsPaginator,
        GetInsightsPaginator,
        ListEnabledProductsForImportPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
    )

    client: SecurityHubClient = boto3.client("securityhub")

    get_enabled_standards_paginator: GetEnabledStandardsPaginator = client.get_paginator("get_enabled_standards")
    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    get_insights_paginator: GetInsightsPaginator = client.get_paginator("get_insights")
    list_enabled_products_for_import_paginator: ListEnabledProductsForImportPaginator = client.get_paginator("list_enabled_products_for_import")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_securityhub.type_defs import (
    AwsSecurityFindingFiltersTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightsResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    PaginatorConfigTypeDef,
    SortCriterionTypeDef,
)


__all__ = (
    "GetEnabledStandardsPaginator",
    "GetFindingsPaginator",
    "GetInsightsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
)


class GetEnabledStandardsPaginator(Boto3Paginator):
    """
    [Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
    """

    def paginate(
        self,
        StandardsSubscriptionArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetEnabledStandardsResponseTypeDef, None, None]:
        """
        [GetEnabledStandards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards.paginate)
        """


class GetFindingsPaginator(Boto3Paginator):
    """
    [Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
    """

    def paginate(
        self,
        Filters: AwsSecurityFindingFiltersTypeDef = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetFindingsResponseTypeDef, None, None]:
        """
        [GetFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings.paginate)
        """


class GetInsightsPaginator(Boto3Paginator):
    """
    [Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
    """

    def paginate(
        self, InsightArns: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetInsightsResponseTypeDef, None, None]:
        """
        [GetInsights.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights.paginate)
        """


class ListEnabledProductsForImportPaginator(Boto3Paginator):
    """
    [Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEnabledProductsForImportResponseTypeDef, None, None]:
        """
        [ListEnabledProductsForImport.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport.paginate)
        """


class ListInvitationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInvitationsResponseTypeDef, None, None]:
        """
        [ListInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations.paginate)
        """


class ListMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
    """

    def paginate(
        self, OnlyAssociated: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMembersResponseTypeDef, None, None]:
        """
        [ListMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers.paginate)
        """
