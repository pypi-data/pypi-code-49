"""
Main interface for sdb service client

Usage::

    import boto3
    from mypy_boto3.sdb import SimpleDBClient

    session = boto3.Session()

    client: SimpleDBClient = boto3.client("sdb")
    session_client: SimpleDBClient = session.client("sdb")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sdb.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sdb.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_sdb.type_defs import (
    ClientBatchDeleteAttributesItemsTypeDef,
    ClientBatchPutAttributesItemsTypeDef,
    ClientDeleteAttributesAttributesTypeDef,
    ClientDeleteAttributesExpectedTypeDef,
    ClientDomainMetadataResponseTypeDef,
    ClientGetAttributesResponseTypeDef,
    ClientListDomainsResponseTypeDef,
    ClientPutAttributesAttributesTypeDef,
    ClientPutAttributesExpectedTypeDef,
    ClientSelectResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SimpleDBClient",)


class SimpleDBClient:
    """
    [SimpleDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_delete_attributes(
        self, DomainName: str, Items: List[ClientBatchDeleteAttributesItemsTypeDef]
    ) -> None:
        """
        [Client.batch_delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.batch_delete_attributes)
        """

    def batch_put_attributes(
        self, DomainName: str, Items: List[ClientBatchPutAttributesItemsTypeDef]
    ) -> None:
        """
        [Client.batch_put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.batch_put_attributes)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.can_paginate)
        """

    def create_domain(self, DomainName: str) -> None:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.create_domain)
        """

    def delete_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List[ClientDeleteAttributesAttributesTypeDef] = None,
        Expected: ClientDeleteAttributesExpectedTypeDef = None,
    ) -> None:
        """
        [Client.delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.delete_attributes)
        """

    def delete_domain(self, DomainName: str) -> None:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.delete_domain)
        """

    def domain_metadata(self, DomainName: str) -> ClientDomainMetadataResponseTypeDef:
        """
        [Client.domain_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.domain_metadata)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.generate_presigned_url)
        """

    def get_attributes(
        self,
        DomainName: str,
        ItemName: str,
        AttributeNames: List[str] = None,
        ConsistentRead: bool = None,
    ) -> ClientGetAttributesResponseTypeDef:
        """
        [Client.get_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.get_attributes)
        """

    def list_domains(
        self, MaxNumberOfDomains: int = None, NextToken: str = None
    ) -> ClientListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.list_domains)
        """

    def put_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List[ClientPutAttributesAttributesTypeDef],
        Expected: ClientPutAttributesExpectedTypeDef = None,
    ) -> None:
        """
        [Client.put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.put_attributes)
        """

    def select(
        self, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None
    ) -> ClientSelectResponseTypeDef:
        """
        [Client.select documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Client.select)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domains"]
    ) -> "paginator_scope.ListDomainsPaginator":
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)
        """

    @overload
    def get_paginator(self, operation_name: Literal["select"]) -> "paginator_scope.SelectPaginator":
        """
        [Paginator.Select documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Paginator.Select)
        """


class Exceptions:
    AttributeDoesNotExist: Boto3ClientError
    ClientError: Boto3ClientError
    DuplicateItemName: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    InvalidNumberPredicates: Boto3ClientError
    InvalidNumberValueTests: Boto3ClientError
    InvalidParameterValue: Boto3ClientError
    InvalidQueryExpression: Boto3ClientError
    MissingParameter: Boto3ClientError
    NoSuchDomain: Boto3ClientError
    NumberDomainAttributesExceeded: Boto3ClientError
    NumberDomainBytesExceeded: Boto3ClientError
    NumberDomainsExceeded: Boto3ClientError
    NumberItemAttributesExceeded: Boto3ClientError
    NumberSubmittedAttributesExceeded: Boto3ClientError
    NumberSubmittedItemsExceeded: Boto3ClientError
    RequestTimeout: Boto3ClientError
    TooManyRequestedAttributes: Boto3ClientError
