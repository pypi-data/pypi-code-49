"""
Main interface for marketplacecommerceanalytics service client

Usage::

    import boto3
    from mypy_boto3.marketplacecommerceanalytics import MarketplaceCommerceAnalyticsClient

    session = boto3.Session()

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    session_client: MarketplaceCommerceAnalyticsClient = session.client("marketplacecommerceanalytics")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_marketplacecommerceanalytics.client as client_scope
else:
    client_scope = object
from mypy_boto3_marketplacecommerceanalytics.type_defs import (
    ClientGenerateDataSetResponseTypeDef,
    ClientStartSupportDataExportResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MarketplaceCommerceAnalyticsClient",)


class MarketplaceCommerceAnalyticsClient:
    """
    [MarketplaceCommerceAnalytics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.can_paginate)
        """

    def generate_data_set(
        self,
        dataSetType: Literal[
            "customer_subscriber_hourly_monthly_subscriptions",
            "customer_subscriber_annual_subscriptions",
            "daily_business_usage_by_instance_type",
            "daily_business_fees",
            "daily_business_free_trial_conversions",
            "daily_business_new_instances",
            "daily_business_new_product_subscribers",
            "daily_business_canceled_product_subscribers",
            "monthly_revenue_billing_and_revenue_data",
            "monthly_revenue_annual_subscriptions",
            "monthly_revenue_field_demonstration_usage",
            "monthly_revenue_flexible_payment_schedule",
            "disbursed_amount_by_product",
            "disbursed_amount_by_product_with_uncollected_funds",
            "disbursed_amount_by_instance_hours",
            "disbursed_amount_by_customer_geo",
            "disbursed_amount_by_age_of_uncollected_funds",
            "disbursed_amount_by_age_of_disbursed_funds",
            "disbursed_amount_by_age_of_past_due_funds",
            "disbursed_amount_by_uncollected_funds_breakdown",
            "customer_profile_by_industry",
            "customer_profile_by_revenue",
            "customer_profile_by_geography",
            "sales_compensation_billed_revenue",
            "us_sales_and_use_tax_records",
        ],
        dataSetPublicationDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None,
    ) -> ClientGenerateDataSetResponseTypeDef:
        """
        [Client.generate_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_data_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_presigned_url)
        """

    def start_support_data_export(
        self,
        dataSetType: Literal[
            "customer_support_contacts_data", "test_customer_support_contacts_data"
        ],
        fromDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None,
    ) -> ClientStartSupportDataExportResponseTypeDef:
        """
        [Client.start_support_data_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.start_support_data_export)
        """


class Exceptions:
    ClientError: Boto3ClientError
    MarketplaceCommerceAnalyticsException: Boto3ClientError
