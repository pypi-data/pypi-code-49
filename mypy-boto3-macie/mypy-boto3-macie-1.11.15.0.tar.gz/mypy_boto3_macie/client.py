"""
Main interface for macie service client

Usage::

    import boto3
    from mypy_boto3.macie import MacieClient

    session = boto3.Session()

    client: MacieClient = boto3.client("macie")
    session_client: MacieClient = session.client("macie")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_macie.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_macie.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_macie.type_defs import (
    ClientAssociateS3ResourcesResponseTypeDef,
    ClientAssociateS3ResourcesS3ResourcesTypeDef,
    ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
    ClientDisassociateS3ResourcesResponseTypeDef,
    ClientListMemberAccountsResponseTypeDef,
    ClientListS3ResourcesResponseTypeDef,
    ClientUpdateS3ResourcesResponseTypeDef,
    ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MacieClient",)


class MacieClient:
    """
    [Macie.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_member_account(self, memberAccountId: str) -> None:
        """
        [Client.associate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.associate_member_account)
        """

    def associate_s3_resources(
        self,
        s3Resources: List[ClientAssociateS3ResourcesS3ResourcesTypeDef],
        memberAccountId: str = None,
    ) -> ClientAssociateS3ResourcesResponseTypeDef:
        """
        [Client.associate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.associate_s3_resources)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.can_paginate)
        """

    def disassociate_member_account(self, memberAccountId: str) -> None:
        """
        [Client.disassociate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.disassociate_member_account)
        """

    def disassociate_s3_resources(
        self,
        associatedS3Resources: List[ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef],
        memberAccountId: str = None,
    ) -> ClientDisassociateS3ResourcesResponseTypeDef:
        """
        [Client.disassociate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.disassociate_s3_resources)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.generate_presigned_url)
        """

    def list_member_accounts(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListMemberAccountsResponseTypeDef:
        """
        [Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.list_member_accounts)
        """

    def list_s3_resources(
        self, memberAccountId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListS3ResourcesResponseTypeDef:
        """
        [Client.list_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.list_s3_resources)
        """

    def update_s3_resources(
        self,
        s3ResourcesUpdate: List[ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef],
        memberAccountId: str = None,
    ) -> ClientUpdateS3ResourcesResponseTypeDef:
        """
        [Client.update_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Client.update_s3_resources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> "paginator_scope.ListMemberAccountsPaginator":
        """
        [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_s3_resources"]
    ) -> "paginator_scope.ListS3ResourcesPaginator":
        """
        [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Paginator.ListS3Resources)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
