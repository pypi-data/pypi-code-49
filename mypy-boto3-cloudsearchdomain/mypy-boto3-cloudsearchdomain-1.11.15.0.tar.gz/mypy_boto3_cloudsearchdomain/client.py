"""
Main interface for cloudsearchdomain service client

Usage::

    import boto3
    from mypy_boto3.cloudsearchdomain import CloudSearchDomainClient

    session = boto3.Session()

    client: CloudSearchDomainClient = boto3.client("cloudsearchdomain")
    session_client: CloudSearchDomainClient = session.client("cloudsearchdomain")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, IO, TYPE_CHECKING, Union
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudsearchdomain.client as client_scope
else:
    client_scope = object
from mypy_boto3_cloudsearchdomain.type_defs import (
    ClientSearchResponseTypeDef,
    ClientSuggestResponseTypeDef,
    ClientUploadDocumentsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudSearchDomainClient",)


class CloudSearchDomainClient:
    """
    [CloudSearchDomain.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)
        """

    def search(
        self,
        query: str,
        cursor: str = None,
        expr: str = None,
        facet: str = None,
        filterQuery: str = None,
        highlight: str = None,
        partial: bool = None,
        queryOptions: str = None,
        queryParser: Literal["simple", "structured", "lucene", "dismax"] = None,
        returnFields: str = None,
        size: int = None,
        sort: str = None,
        start: int = None,
        stats: str = None,
    ) -> ClientSearchResponseTypeDef:
        """
        [Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)
        """

    def suggest(self, query: str, suggester: str, size: int = None) -> ClientSuggestResponseTypeDef:
        """
        [Client.suggest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)
        """

    def upload_documents(
        self,
        documents: Union[bytes, IO],
        contentType: Literal["application/json", "application/xml"],
    ) -> ClientUploadDocumentsResponseTypeDef:
        """
        [Client.upload_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DocumentServiceException: Boto3ClientError
    SearchException: Boto3ClientError
