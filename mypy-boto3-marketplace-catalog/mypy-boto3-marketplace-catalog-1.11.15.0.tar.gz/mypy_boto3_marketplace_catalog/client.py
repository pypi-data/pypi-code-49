"""
Main interface for marketplace-catalog service client

Usage::

    import boto3
    from mypy_boto3.marketplace_catalog import MarketplaceCatalogClient

    session = boto3.Session()

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    session_client: MarketplaceCatalogClient = session.client("marketplace-catalog")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_marketplace_catalog.client as client_scope
else:
    client_scope = object
from mypy_boto3_marketplace_catalog.type_defs import (
    ClientCancelChangeSetResponseTypeDef,
    ClientDescribeChangeSetResponseTypeDef,
    ClientDescribeEntityResponseTypeDef,
    ClientListChangeSetsFilterListTypeDef,
    ClientListChangeSetsResponseTypeDef,
    ClientListChangeSetsSortTypeDef,
    ClientListEntitiesFilterListTypeDef,
    ClientListEntitiesResponseTypeDef,
    ClientListEntitiesSortTypeDef,
    ClientStartChangeSetChangeSetTypeDef,
    ClientStartChangeSetResponseTypeDef,
)


__all__ = ("MarketplaceCatalogClient",)


class MarketplaceCatalogClient:
    """
    [MarketplaceCatalog.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.can_paginate)
        """

    def cancel_change_set(
        self, Catalog: str, ChangeSetId: str
    ) -> ClientCancelChangeSetResponseTypeDef:
        """
        [Client.cancel_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.cancel_change_set)
        """

    def describe_change_set(
        self, Catalog: str, ChangeSetId: str
    ) -> ClientDescribeChangeSetResponseTypeDef:
        """
        [Client.describe_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_change_set)
        """

    def describe_entity(self, Catalog: str, EntityId: str) -> ClientDescribeEntityResponseTypeDef:
        """
        [Client.describe_entity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_entity)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.generate_presigned_url)
        """

    def list_change_sets(
        self,
        Catalog: str,
        FilterList: List[ClientListChangeSetsFilterListTypeDef] = None,
        Sort: ClientListChangeSetsSortTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListChangeSetsResponseTypeDef:
        """
        [Client.list_change_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_change_sets)
        """

    def list_entities(
        self,
        Catalog: str,
        EntityType: str,
        FilterList: List[ClientListEntitiesFilterListTypeDef] = None,
        Sort: ClientListEntitiesSortTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntitiesResponseTypeDef:
        """
        [Client.list_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_entities)
        """

    def start_change_set(
        self,
        Catalog: str,
        ChangeSet: List[ClientStartChangeSetChangeSetTypeDef],
        ChangeSetName: str = None,
        ClientRequestToken: str = None,
    ) -> ClientStartChangeSetResponseTypeDef:
        """
        [Client.start_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.start_change_set)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotSupportedException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
