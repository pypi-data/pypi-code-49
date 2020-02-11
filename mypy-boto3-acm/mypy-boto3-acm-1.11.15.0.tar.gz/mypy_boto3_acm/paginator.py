"""
Main interface for acm service client paginators.

Usage::

    import boto3
    from mypy_boto3.acm import (
        ListCertificatesPaginator,
    )

    client: ACMClient = boto3.client("acm")

    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_acm.type_defs import (
    FiltersTypeDef,
    ListCertificatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListCertificatesPaginator",)


class ListCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Paginator.ListCertificates)
    """

    def paginate(
        self,
        CertificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        Includes: FiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCertificatesResponseTypeDef, None, None]:
        """
        [ListCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Paginator.ListCertificates.paginate)
        """
