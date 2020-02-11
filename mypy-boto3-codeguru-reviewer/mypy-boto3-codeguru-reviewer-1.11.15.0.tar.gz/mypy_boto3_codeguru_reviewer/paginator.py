"""
Main interface for codeguru-reviewer service client paginators.

Usage::

    import boto3
    from mypy_boto3.codeguru_reviewer import (
        ListRepositoryAssociationsPaginator,
    )

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")

    list_repository_associations_paginator: ListRepositoryAssociationsPaginator = client.get_paginator("list_repository_associations")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codeguru_reviewer.type_defs import (
    ListRepositoryAssociationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListRepositoryAssociationsPaginator",)


class ListRepositoryAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
    """

    def paginate(
        self,
        ProviderTypes: List[Literal["CodeCommit", "GitHub"]] = None,
        States: List[Literal["Associated", "Associating", "Failed", "Disassociating"]] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRepositoryAssociationsResponseTypeDef, None, None]:
        """
        [ListRepositoryAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations.paginate)
        """
