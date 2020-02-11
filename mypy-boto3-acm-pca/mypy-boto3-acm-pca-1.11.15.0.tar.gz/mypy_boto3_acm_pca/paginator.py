"""
Main interface for acm-pca service client paginators.

Usage::

    import boto3
    from mypy_boto3.acm_pca import (
        ListCertificateAuthoritiesPaginator,
        ListPermissionsPaginator,
        ListTagsPaginator,
    )

    client: ACMPCAClient = boto3.client("acm-pca")

    list_certificate_authorities_paginator: ListCertificateAuthoritiesPaginator = client.get_paginator("list_certificate_authorities")
    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_acm_pca.type_defs import (
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListCertificateAuthoritiesPaginator", "ListPermissionsPaginator", "ListTagsPaginator")


class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCertificateAuthoritiesResponseTypeDef, None, None]:
        """
        [ListCertificateAuthorities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities.paginate)
        """


class ListPermissionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
    """

    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPermissionsResponseTypeDef, None, None]:
        """
        [ListPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
    """

    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsResponseTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags.paginate)
        """
