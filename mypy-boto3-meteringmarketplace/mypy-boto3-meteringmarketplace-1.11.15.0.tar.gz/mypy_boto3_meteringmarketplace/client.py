"""
Main interface for meteringmarketplace service client

Usage::

    import boto3
    from mypy_boto3.meteringmarketplace import MarketplaceMeteringClient

    session = boto3.Session()

    client: MarketplaceMeteringClient = boto3.client("meteringmarketplace")
    session_client: MarketplaceMeteringClient = session.client("meteringmarketplace")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_meteringmarketplace.client as client_scope
else:
    client_scope = object
from mypy_boto3_meteringmarketplace.type_defs import (
    ClientBatchMeterUsageResponseTypeDef,
    ClientBatchMeterUsageUsageRecordsTypeDef,
    ClientMeterUsageResponseTypeDef,
    ClientRegisterUsageResponseTypeDef,
    ClientResolveCustomerResponseTypeDef,
)


__all__ = ("MarketplaceMeteringClient",)


class MarketplaceMeteringClient:
    """
    [MarketplaceMetering.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_meter_usage(
        self, UsageRecords: List[ClientBatchMeterUsageUsageRecordsTypeDef], ProductCode: str
    ) -> ClientBatchMeterUsageResponseTypeDef:
        """
        [Client.batch_meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)
        """

    def meter_usage(
        self,
        ProductCode: str,
        Timestamp: datetime,
        UsageDimension: str,
        UsageQuantity: int = None,
        DryRun: bool = None,
    ) -> ClientMeterUsageResponseTypeDef:
        """
        [Client.meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)
        """

    def register_usage(
        self, ProductCode: str, PublicKeyVersion: int, Nonce: str = None
    ) -> ClientRegisterUsageResponseTypeDef:
        """
        [Client.register_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)
        """

    def resolve_customer(self, RegistrationToken: str) -> ClientResolveCustomerResponseTypeDef:
        """
        [Client.resolve_customer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CustomerNotEntitledException: Boto3ClientError
    DisabledApiException: Boto3ClientError
    DuplicateRequestException: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidCustomerIdentifierException: Boto3ClientError
    InvalidEndpointRegionException: Boto3ClientError
    InvalidProductCodeException: Boto3ClientError
    InvalidPublicKeyVersionException: Boto3ClientError
    InvalidRegionException: Boto3ClientError
    InvalidTokenException: Boto3ClientError
    InvalidUsageDimensionException: Boto3ClientError
    PlatformNotSupportedException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TimestampOutOfBoundsException: Boto3ClientError
