"""
Main interface for outposts service client

Usage::

    import boto3
    from mypy_boto3.outposts import OutpostsClient

    session = boto3.Session()

    client: OutpostsClient = boto3.client("outposts")
    session_client: OutpostsClient = session.client("outposts")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_outposts.client as client_scope
else:
    client_scope = object
from mypy_boto3_outposts.type_defs import (
    ClientCreateOutpostResponseTypeDef,
    ClientGetOutpostInstanceTypesResponseTypeDef,
    ClientGetOutpostResponseTypeDef,
    ClientListOutpostsResponseTypeDef,
    ClientListSitesResponseTypeDef,
)


__all__ = ("OutpostsClient",)


class OutpostsClient:
    """
    [Outposts.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.can_paginate)
        """

    def create_outpost(
        self,
        SiteId: str,
        Name: str = None,
        Description: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
    ) -> ClientCreateOutpostResponseTypeDef:
        """
        [Client.create_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.create_outpost)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.generate_presigned_url)
        """

    def get_outpost(self, OutpostId: str) -> ClientGetOutpostResponseTypeDef:
        """
        [Client.get_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.get_outpost)
        """

    def get_outpost_instance_types(
        self, OutpostId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetOutpostInstanceTypesResponseTypeDef:
        """
        [Client.get_outpost_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.get_outpost_instance_types)
        """

    def list_outposts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListOutpostsResponseTypeDef:
        """
        [Client.list_outposts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.list_outposts)
        """

    def list_sites(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListSitesResponseTypeDef:
        """
        [Client.list_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/outposts.html#Outposts.Client.list_sites)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ValidationException: Boto3ClientError
