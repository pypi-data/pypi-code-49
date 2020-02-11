"""
Main interface for mturk service client paginators.

Usage::

    import boto3
    from mypy_boto3.mturk import (
        ListAssignmentsForHITPaginator,
        ListBonusPaymentsPaginator,
        ListHITsPaginator,
        ListHITsForQualificationTypePaginator,
        ListQualificationRequestsPaginator,
        ListQualificationTypesPaginator,
        ListReviewableHITsPaginator,
        ListWorkerBlocksPaginator,
        ListWorkersWithQualificationTypePaginator,
    )

    client: MTurkClient = boto3.client("mturk")

    list_assignments_for_hit_paginator: ListAssignmentsForHITPaginator = client.get_paginator("list_assignments_for_hit")
    list_bonus_payments_paginator: ListBonusPaymentsPaginator = client.get_paginator("list_bonus_payments")
    list_hits_paginator: ListHITsPaginator = client.get_paginator("list_hits")
    list_hits_for_qualification_type_paginator: ListHITsForQualificationTypePaginator = client.get_paginator("list_hits_for_qualification_type")
    list_qualification_requests_paginator: ListQualificationRequestsPaginator = client.get_paginator("list_qualification_requests")
    list_qualification_types_paginator: ListQualificationTypesPaginator = client.get_paginator("list_qualification_types")
    list_reviewable_hits_paginator: ListReviewableHITsPaginator = client.get_paginator("list_reviewable_hits")
    list_worker_blocks_paginator: ListWorkerBlocksPaginator = client.get_paginator("list_worker_blocks")
    list_workers_with_qualification_type_paginator: ListWorkersWithQualificationTypePaginator = client.get_paginator("list_workers_with_qualification_type")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mturk.type_defs import (
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
)


class ListAssignmentsForHITPaginator(Boto3Paginator):
    """
    [Paginator.ListAssignmentsForHIT documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)
    """

    def paginate(
        self,
        HITId: str,
        AssignmentStatuses: List[Literal["Submitted", "Approved", "Rejected"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAssignmentsForHITResponseTypeDef, None, None]:
        """
        [ListAssignmentsForHIT.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT.paginate)
        """


class ListBonusPaymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListBonusPayments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)
    """

    def paginate(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListBonusPaymentsResponseTypeDef, None, None]:
        """
        [ListBonusPayments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments.paginate)
        """


class ListHITsPaginator(Boto3Paginator):
    """
    [Paginator.ListHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListHITs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHITsResponseTypeDef, None, None]:
        """
        [ListHITs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListHITs.paginate)
        """


class ListHITsForQualificationTypePaginator(Boto3Paginator):
    """
    [Paginator.ListHITsForQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)
    """

    def paginate(
        self, QualificationTypeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHITsForQualificationTypeResponseTypeDef, None, None]:
        """
        [ListHITsForQualificationType.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType.paginate)
        """


class ListQualificationRequestsPaginator(Boto3Paginator):
    """
    [Paginator.ListQualificationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)
    """

    def paginate(
        self, QualificationTypeId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListQualificationRequestsResponseTypeDef, None, None]:
        """
        [ListQualificationRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests.paginate)
        """


class ListQualificationTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListQualificationTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)
    """

    def paginate(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListQualificationTypesResponseTypeDef, None, None]:
        """
        [ListQualificationTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes.paginate)
        """


class ListReviewableHITsPaginator(Boto3Paginator):
    """
    [Paginator.ListReviewableHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)
    """

    def paginate(
        self,
        HITTypeId: str = None,
        Status: Literal["Reviewable", "Reviewing"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListReviewableHITsResponseTypeDef, None, None]:
        """
        [ListReviewableHITs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs.paginate)
        """


class ListWorkerBlocksPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkerBlocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListWorkerBlocksResponseTypeDef, None, None]:
        """
        [ListWorkerBlocks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks.paginate)
        """


class ListWorkersWithQualificationTypePaginator(Boto3Paginator):
    """
    [Paginator.ListWorkersWithQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)
    """

    def paginate(
        self,
        QualificationTypeId: str,
        Status: Literal["Granted", "Revoked"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListWorkersWithQualificationTypeResponseTypeDef, None, None]:
        """
        [ListWorkersWithQualificationType.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType.paginate)
        """
