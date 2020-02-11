"""
Main interface for ce service client

Usage::

    import boto3
    from mypy_boto3.ce import CostExplorerClient

    session = boto3.Session()

    client: CostExplorerClient = boto3.client("ce")
    session_client: CostExplorerClient = session.client("ce")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ce.client as client_scope
else:
    client_scope = object
from mypy_boto3_ce.type_defs import (
    ClientCreateCostCategoryDefinitionResponseTypeDef,
    ClientCreateCostCategoryDefinitionRulesTypeDef,
    ClientDeleteCostCategoryDefinitionResponseTypeDef,
    ClientDescribeCostCategoryDefinitionResponseTypeDef,
    ClientGetCostAndUsageFilterTypeDef,
    ClientGetCostAndUsageGroupByTypeDef,
    ClientGetCostAndUsageResponseTypeDef,
    ClientGetCostAndUsageTimePeriodTypeDef,
    ClientGetCostAndUsageWithResourcesFilterTypeDef,
    ClientGetCostAndUsageWithResourcesGroupByTypeDef,
    ClientGetCostAndUsageWithResourcesResponseTypeDef,
    ClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
    ClientGetCostForecastFilterTypeDef,
    ClientGetCostForecastResponseTypeDef,
    ClientGetCostForecastTimePeriodTypeDef,
    ClientGetDimensionValuesResponseTypeDef,
    ClientGetDimensionValuesTimePeriodTypeDef,
    ClientGetReservationCoverageFilterTypeDef,
    ClientGetReservationCoverageGroupByTypeDef,
    ClientGetReservationCoverageResponseTypeDef,
    ClientGetReservationCoverageTimePeriodTypeDef,
    ClientGetReservationPurchaseRecommendationResponseTypeDef,
    ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef,
    ClientGetReservationUtilizationFilterTypeDef,
    ClientGetReservationUtilizationGroupByTypeDef,
    ClientGetReservationUtilizationResponseTypeDef,
    ClientGetReservationUtilizationTimePeriodTypeDef,
    ClientGetRightsizingRecommendationFilterTypeDef,
    ClientGetRightsizingRecommendationResponseTypeDef,
    ClientGetSavingsPlansCoverageFilterTypeDef,
    ClientGetSavingsPlansCoverageGroupByTypeDef,
    ClientGetSavingsPlansCoverageResponseTypeDef,
    ClientGetSavingsPlansCoverageTimePeriodTypeDef,
    ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef,
    ClientGetSavingsPlansUtilizationDetailsFilterTypeDef,
    ClientGetSavingsPlansUtilizationDetailsResponseTypeDef,
    ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
    ClientGetSavingsPlansUtilizationFilterTypeDef,
    ClientGetSavingsPlansUtilizationResponseTypeDef,
    ClientGetSavingsPlansUtilizationTimePeriodTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientGetTagsTimePeriodTypeDef,
    ClientGetUsageForecastFilterTypeDef,
    ClientGetUsageForecastResponseTypeDef,
    ClientGetUsageForecastTimePeriodTypeDef,
    ClientListCostCategoryDefinitionsResponseTypeDef,
    ClientUpdateCostCategoryDefinitionResponseTypeDef,
    ClientUpdateCostCategoryDefinitionRulesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CostExplorerClient",)


class CostExplorerClient:
    """
    [CostExplorer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.can_paginate)
        """

    def create_cost_category_definition(
        self,
        Name: str,
        RuleVersion: str,
        Rules: List[ClientCreateCostCategoryDefinitionRulesTypeDef],
    ) -> ClientCreateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.create_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)
        """

    def delete_cost_category_definition(
        self, CostCategoryArn: str
    ) -> ClientDeleteCostCategoryDefinitionResponseTypeDef:
        """
        [Client.delete_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)
        """

    def describe_cost_category_definition(
        self, CostCategoryArn: str, EffectiveOn: str = None
    ) -> ClientDescribeCostCategoryDefinitionResponseTypeDef:
        """
        [Client.describe_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)
        """

    def get_cost_and_usage(
        self,
        TimePeriod: ClientGetCostAndUsageTimePeriodTypeDef,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ClientGetCostAndUsageFilterTypeDef = None,
        Metrics: List[str] = None,
        GroupBy: List[ClientGetCostAndUsageGroupByTypeDef] = None,
        NextPageToken: str = None,
    ) -> ClientGetCostAndUsageResponseTypeDef:
        """
        [Client.get_cost_and_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)
        """

    def get_cost_and_usage_with_resources(
        self,
        TimePeriod: ClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ClientGetCostAndUsageWithResourcesFilterTypeDef = None,
        Metrics: List[str] = None,
        GroupBy: List[ClientGetCostAndUsageWithResourcesGroupByTypeDef] = None,
        NextPageToken: str = None,
    ) -> ClientGetCostAndUsageWithResourcesResponseTypeDef:
        """
        [Client.get_cost_and_usage_with_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)
        """

    def get_cost_forecast(
        self,
        TimePeriod: ClientGetCostForecastTimePeriodTypeDef,
        Metric: Literal[
            "BLENDED_COST",
            "UNBLENDED_COST",
            "AMORTIZED_COST",
            "NET_UNBLENDED_COST",
            "NET_AMORTIZED_COST",
            "USAGE_QUANTITY",
            "NORMALIZED_USAGE_AMOUNT",
        ],
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"],
        Filter: ClientGetCostForecastFilterTypeDef = None,
        PredictionIntervalLevel: int = None,
    ) -> ClientGetCostForecastResponseTypeDef:
        """
        [Client.get_cost_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)
        """

    def get_dimension_values(
        self,
        TimePeriod: ClientGetDimensionValuesTimePeriodTypeDef,
        Dimension: Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        SearchString: str = None,
        Context: Literal["COST_AND_USAGE", "RESERVATIONS", "SAVINGS_PLANS"] = None,
        NextPageToken: str = None,
    ) -> ClientGetDimensionValuesResponseTypeDef:
        """
        [Client.get_dimension_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_dimension_values)
        """

    def get_reservation_coverage(
        self,
        TimePeriod: ClientGetReservationCoverageTimePeriodTypeDef,
        GroupBy: List[ClientGetReservationCoverageGroupByTypeDef] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ClientGetReservationCoverageFilterTypeDef = None,
        Metrics: List[str] = None,
        NextPageToken: str = None,
    ) -> ClientGetReservationCoverageResponseTypeDef:
        """
        [Client.get_reservation_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)
        """

    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: str = None,
        AccountScope: Literal["PAYER", "LINKED"] = None,
        LookbackPeriodInDays: Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"] = None,
        TermInYears: Literal["ONE_YEAR", "THREE_YEARS"] = None,
        PaymentOption: Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ] = None,
        ServiceSpecification: ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> ClientGetReservationPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_reservation_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)
        """

    def get_reservation_utilization(
        self,
        TimePeriod: ClientGetReservationUtilizationTimePeriodTypeDef,
        GroupBy: List[ClientGetReservationUtilizationGroupByTypeDef] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ClientGetReservationUtilizationFilterTypeDef = None,
        NextPageToken: str = None,
    ) -> ClientGetReservationUtilizationResponseTypeDef:
        """
        [Client.get_reservation_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)
        """

    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: ClientGetRightsizingRecommendationFilterTypeDef = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> ClientGetRightsizingRecommendationResponseTypeDef:
        """
        [Client.get_rightsizing_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)
        """

    def get_savings_plans_coverage(
        self,
        TimePeriod: ClientGetSavingsPlansCoverageTimePeriodTypeDef,
        GroupBy: List[ClientGetSavingsPlansCoverageGroupByTypeDef] = None,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ClientGetSavingsPlansCoverageFilterTypeDef = None,
        Metrics: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetSavingsPlansCoverageResponseTypeDef:
        """
        [Client.get_savings_plans_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)
        """

    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: Literal["COMPUTE_SP", "EC2_INSTANCE_SP"],
        TermInYears: Literal["ONE_YEAR", "THREE_YEARS"],
        PaymentOption: Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        LookbackPeriodInDays: Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        NextPageToken: str = None,
        PageSize: int = None,
    ) -> ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_savings_plans_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)
        """

    def get_savings_plans_utilization(
        self,
        TimePeriod: ClientGetSavingsPlansUtilizationTimePeriodTypeDef,
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"] = None,
        Filter: ClientGetSavingsPlansUtilizationFilterTypeDef = None,
    ) -> ClientGetSavingsPlansUtilizationResponseTypeDef:
        """
        [Client.get_savings_plans_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)
        """

    def get_savings_plans_utilization_details(
        self,
        TimePeriod: ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
        Filter: ClientGetSavingsPlansUtilizationDetailsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        [Client.get_savings_plans_utilization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)
        """

    def get_tags(
        self,
        TimePeriod: ClientGetTagsTimePeriodTypeDef,
        SearchString: str = None,
        TagKey: str = None,
        NextPageToken: str = None,
    ) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_tags)
        """

    def get_usage_forecast(
        self,
        TimePeriod: ClientGetUsageForecastTimePeriodTypeDef,
        Metric: Literal[
            "BLENDED_COST",
            "UNBLENDED_COST",
            "AMORTIZED_COST",
            "NET_UNBLENDED_COST",
            "NET_AMORTIZED_COST",
            "USAGE_QUANTITY",
            "NORMALIZED_USAGE_AMOUNT",
        ],
        Granularity: Literal["DAILY", "MONTHLY", "HOURLY"],
        Filter: ClientGetUsageForecastFilterTypeDef = None,
        PredictionIntervalLevel: int = None,
    ) -> ClientGetUsageForecastResponseTypeDef:
        """
        [Client.get_usage_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)
        """

    def list_cost_category_definitions(
        self, EffectiveOn: str = None, NextToken: str = None
    ) -> ClientListCostCategoryDefinitionsResponseTypeDef:
        """
        [Client.list_cost_category_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)
        """

    def update_cost_category_definition(
        self,
        CostCategoryArn: str,
        RuleVersion: str,
        Rules: List[ClientUpdateCostCategoryDefinitionRulesTypeDef],
    ) -> ClientUpdateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.update_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)
        """


class Exceptions:
    BillExpirationException: Boto3ClientError
    ClientError: Boto3ClientError
    DataUnavailableException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RequestChangedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    UnresolvableUsageUnitException: Boto3ClientError
