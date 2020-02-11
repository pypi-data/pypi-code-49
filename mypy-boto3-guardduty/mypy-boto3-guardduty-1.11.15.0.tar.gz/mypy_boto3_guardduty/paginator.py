"""
Main interface for guardduty service client paginators.

Usage::

    import boto3
    from mypy_boto3.guardduty import (
        ListDetectorsPaginator,
        ListFiltersPaginator,
        ListFindingsPaginator,
        ListIPSetsPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
        ListThreatIntelSetsPaginator,
    )

    client: GuardDutyClient = boto3.client("guardduty")

    list_detectors_paginator: ListDetectorsPaginator = client.get_paginator("list_detectors")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_ip_sets_paginator: ListIPSetsPaginator = client.get_paginator("list_ip_sets")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_threat_intel_sets_paginator: ListThreatIntelSetsPaginator = client.get_paginator("list_threat_intel_sets")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_guardduty.type_defs import (
    FindingCriteriaTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    PaginatorConfigTypeDef,
    SortCriteriaTypeDef,
)


__all__ = (
    "ListDetectorsPaginator",
    "ListFiltersPaginator",
    "ListFindingsPaginator",
    "ListIPSetsPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListThreatIntelSetsPaginator",
)


class ListDetectorsPaginator(Boto3Paginator):
    """
    [Paginator.ListDetectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDetectorsResponseTypeDef, None, None]:
        """
        [ListDetectors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors.paginate)
        """


class ListFiltersPaginator(Boto3Paginator):
    """
    [Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)
    """

    def paginate(
        self, DetectorId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFiltersResponseTypeDef, None, None]:
        """
        [ListFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)
    """

    def paginate(
        self,
        DetectorId: str,
        FindingCriteria: FindingCriteriaTypeDef = None,
        SortCriteria: SortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListFindingsResponseTypeDef, None, None]:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings.paginate)
        """


class ListIPSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)
    """

    def paginate(
        self, DetectorId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListIPSetsResponseTypeDef, None, None]:
        """
        [ListIPSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets.paginate)
        """


class ListInvitationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInvitationsResponseTypeDef, None, None]:
        """
        [ListInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations.paginate)
        """


class ListMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)
    """

    def paginate(
        self,
        DetectorId: str,
        OnlyAssociated: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListMembersResponseTypeDef, None, None]:
        """
        [ListMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers.paginate)
        """


class ListThreatIntelSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListThreatIntelSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)
    """

    def paginate(
        self, DetectorId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListThreatIntelSetsResponseTypeDef, None, None]:
        """
        [ListThreatIntelSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets.paginate)
        """
