"""
Main interface for codeguru-reviewer service client

Usage::

    import boto3
    from mypy_boto3.codeguru_reviewer import CodeGuruReviewerClient

    session = boto3.Session()

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")
    session_client: CodeGuruReviewerClient = session.client("codeguru-reviewer")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codeguru_reviewer.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codeguru_reviewer.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_codeguru_reviewer.type_defs import (
    ClientAssociateRepositoryRepositoryTypeDef,
    ClientAssociateRepositoryResponseTypeDef,
    ClientDescribeRepositoryAssociationResponseTypeDef,
    ClientDisassociateRepositoryResponseTypeDef,
    ClientListRepositoryAssociationsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeGuruReviewerClient",)


class CodeGuruReviewerClient:
    """
    [CodeGuruReviewer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_repository(
        self, Repository: ClientAssociateRepositoryRepositoryTypeDef, ClientRequestToken: str = None
    ) -> ClientAssociateRepositoryResponseTypeDef:
        """
        [Client.associate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)
        """

    def describe_repository_association(
        self, AssociationArn: str
    ) -> ClientDescribeRepositoryAssociationResponseTypeDef:
        """
        [Client.describe_repository_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)
        """

    def disassociate_repository(
        self, AssociationArn: str
    ) -> ClientDisassociateRepositoryResponseTypeDef:
        """
        [Client.disassociate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)
        """

    def list_repository_associations(
        self,
        ProviderTypes: List[Literal["CodeCommit", "GitHub"]] = None,
        States: List[Literal["Associated", "Associating", "Failed", "Disassociating"]] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListRepositoryAssociationsResponseTypeDef:
        """
        [Client.list_repository_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repository_associations"]
    ) -> "paginator_scope.ListRepositoryAssociationsPaginator":
        """
        [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
