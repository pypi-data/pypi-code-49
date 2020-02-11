"""
Main interface for marketplace-entitlement service client

Usage::

    import boto3
    from mypy_boto3.marketplace_entitlement import MarketplaceEntitlementServiceClient

    session = boto3.Session()

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")
    session_client: MarketplaceEntitlementServiceClient = session.client("marketplace-entitlement")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_marketplace_entitlement.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_marketplace_entitlement.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_marketplace_entitlement.type_defs import ClientGetEntitlementsResponseTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MarketplaceEntitlementServiceClient",)


class MarketplaceEntitlementServiceClient:
    """
    [MarketplaceEntitlementService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.generate_presigned_url)
        """

    def get_entitlements(
        self,
        ProductCode: str,
        Filter: Dict[str, List[str]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetEntitlementsResponseTypeDef:
        """
        [Client.get_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.get_entitlements)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_entitlements"]
    ) -> "paginator_scope.GetEntitlementsPaginator":
        """
        [Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    ThrottlingException: Boto3ClientError
