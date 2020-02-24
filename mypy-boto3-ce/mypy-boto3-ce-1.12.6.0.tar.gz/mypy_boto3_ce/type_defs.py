"""
Main interface for ce service type definitions.

Usage::

    from mypy_boto3.ce.type_defs import ClientCreateCostCategoryDefinitionResponseTypeDef

    data: ClientCreateCostCategoryDefinitionResponseTypeDef = {...}
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateCostCategoryDefinitionResponseTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleTypeDef",
    "ClientCreateCostCategoryDefinitionRulesTypeDef",
    "ClientDeleteCostCategoryDefinitionResponseTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseTypeDef",
    "ClientGetCostAndUsageFilterCostCategoriesTypeDef",
    "ClientGetCostAndUsageFilterDimensionsTypeDef",
    "ClientGetCostAndUsageFilterTagsTypeDef",
    "ClientGetCostAndUsageFilterTypeDef",
    "ClientGetCostAndUsageGroupByTypeDef",
    "ClientGetCostAndUsageResponseGroupDefinitionsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTypeDef",
    "ClientGetCostAndUsageResponseTypeDef",
    "ClientGetCostAndUsageTimePeriodTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterTagsTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterTypeDef",
    "ClientGetCostAndUsageWithResourcesGroupByTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseTypeDef",
    "ClientGetCostAndUsageWithResourcesTimePeriodTypeDef",
    "ClientGetCostForecastFilterCostCategoriesTypeDef",
    "ClientGetCostForecastFilterDimensionsTypeDef",
    "ClientGetCostForecastFilterTagsTypeDef",
    "ClientGetCostForecastFilterTypeDef",
    "ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    "ClientGetCostForecastResponseForecastResultsByTimeTypeDef",
    "ClientGetCostForecastResponseTotalTypeDef",
    "ClientGetCostForecastResponseTypeDef",
    "ClientGetCostForecastTimePeriodTypeDef",
    "ClientGetDimensionValuesResponseDimensionValuesTypeDef",
    "ClientGetDimensionValuesResponseTypeDef",
    "ClientGetDimensionValuesTimePeriodTypeDef",
    "ClientGetReservationCoverageFilterCostCategoriesTypeDef",
    "ClientGetReservationCoverageFilterDimensionsTypeDef",
    "ClientGetReservationCoverageFilterTagsTypeDef",
    "ClientGetReservationCoverageFilterTypeDef",
    "ClientGetReservationCoverageGroupByTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseTotalTypeDef",
    "ClientGetReservationCoverageResponseTypeDef",
    "ClientGetReservationCoverageTimePeriodTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseTypeDef",
    "ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef",
    "ClientGetReservationUtilizationFilterCostCategoriesTypeDef",
    "ClientGetReservationUtilizationFilterDimensionsTypeDef",
    "ClientGetReservationUtilizationFilterTagsTypeDef",
    "ClientGetReservationUtilizationFilterTypeDef",
    "ClientGetReservationUtilizationGroupByTypeDef",
    "ClientGetReservationUtilizationResponseTotalTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef",
    "ClientGetReservationUtilizationResponseTypeDef",
    "ClientGetReservationUtilizationTimePeriodTypeDef",
    "ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef",
    "ClientGetRightsizingRecommendationFilterDimensionsTypeDef",
    "ClientGetRightsizingRecommendationFilterTagsTypeDef",
    "ClientGetRightsizingRecommendationFilterTypeDef",
    "ClientGetRightsizingRecommendationResponseMetadataTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef",
    "ClientGetRightsizingRecommendationResponseSummaryTypeDef",
    "ClientGetRightsizingRecommendationResponseTypeDef",
    "ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef",
    "ClientGetSavingsPlansCoverageFilterDimensionsTypeDef",
    "ClientGetSavingsPlansCoverageFilterTagsTypeDef",
    "ClientGetSavingsPlansCoverageFilterTypeDef",
    "ClientGetSavingsPlansCoverageGroupByTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef",
    "ClientGetSavingsPlansCoverageResponseTypeDef",
    "ClientGetSavingsPlansCoverageTimePeriodTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef",
    "ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef",
    "ClientGetSavingsPlansUtilizationFilterTagsTypeDef",
    "ClientGetSavingsPlansUtilizationFilterTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTypeDef",
    "ClientGetSavingsPlansUtilizationTimePeriodTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetTagsTimePeriodTypeDef",
    "ClientGetUsageForecastFilterCostCategoriesTypeDef",
    "ClientGetUsageForecastFilterDimensionsTypeDef",
    "ClientGetUsageForecastFilterTagsTypeDef",
    "ClientGetUsageForecastFilterTypeDef",
    "ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    "ClientGetUsageForecastResponseForecastResultsByTimeTypeDef",
    "ClientGetUsageForecastResponseTotalTypeDef",
    "ClientGetUsageForecastResponseTypeDef",
    "ClientGetUsageForecastTimePeriodTypeDef",
    "ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef",
    "ClientListCostCategoryDefinitionsResponseTypeDef",
    "ClientUpdateCostCategoryDefinitionResponseTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesTypeDef",
)

ClientCreateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "ClientCreateCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveStart": str},
    total=False,
)

ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef = TypedDict(
    "ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef = TypedDict(
    "ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef = TypedDict(
    "ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateCostCategoryDefinitionRulesRuleTypeDef = TypedDict(
    "ClientCreateCostCategoryDefinitionRulesRuleTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef,
        "Tags": ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef,
        "CostCategories": ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef,
    },
    total=False,
)

ClientCreateCostCategoryDefinitionRulesTypeDef = TypedDict(
    "ClientCreateCostCategoryDefinitionRulesTypeDef",
    {"Value": str, "Rule": ClientCreateCostCategoryDefinitionRulesRuleTypeDef},
    total=False,
)

ClientDeleteCostCategoryDefinitionResponseTypeDef = TypedDict(
    "ClientDeleteCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveEnd": str},
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef,
        "Tags": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef,
        "CostCategories": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef,
    },
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef",
    {
        "Value": str,
        "Rule": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef,
    },
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "EffectiveEnd": str,
        "Name": str,
        "RuleVersion": str,
        "Rules": List[ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef],
    },
    total=False,
)

ClientDescribeCostCategoryDefinitionResponseTypeDef = TypedDict(
    "ClientDescribeCostCategoryDefinitionResponseTypeDef",
    {"CostCategory": ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef},
    total=False,
)

ClientGetCostAndUsageFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetCostAndUsageFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetCostAndUsageFilterDimensionsTypeDef = TypedDict(
    "ClientGetCostAndUsageFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetCostAndUsageFilterTagsTypeDef = TypedDict(
    "ClientGetCostAndUsageFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetCostAndUsageFilterTypeDef = TypedDict(
    "ClientGetCostAndUsageFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetCostAndUsageFilterDimensionsTypeDef,
        "Tags": ClientGetCostAndUsageFilterTagsTypeDef,
        "CostCategories": ClientGetCostAndUsageFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetCostAndUsageGroupByTypeDef = TypedDict(
    "ClientGetCostAndUsageGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetCostAndUsageResponseGroupDefinitionsTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseGroupDefinitionsTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[str, ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef],
    },
    total=False,
)

ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientGetCostAndUsageResponseResultsByTimeTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef,
        "Total": Dict[str, ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef],
        "Groups": List[ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef],
        "Estimated": bool,
    },
    total=False,
)

ClientGetCostAndUsageResponseTypeDef = TypedDict(
    "ClientGetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[ClientGetCostAndUsageResponseGroupDefinitionsTypeDef],
        "ResultsByTime": List[ClientGetCostAndUsageResponseResultsByTimeTypeDef],
    },
    total=False,
)

_RequiredClientGetCostAndUsageTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetCostAndUsageTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetCostAndUsageTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetCostAndUsageTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetCostAndUsageTimePeriodTypeDef(
    _RequiredClientGetCostAndUsageTimePeriodTypeDef, _OptionalClientGetCostAndUsageTimePeriodTypeDef
):
    pass


ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetCostAndUsageWithResourcesFilterTagsTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetCostAndUsageWithResourcesFilterTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef,
        "Tags": ClientGetCostAndUsageWithResourcesFilterTagsTypeDef,
        "CostCategories": ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetCostAndUsageWithResourcesGroupByTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[
            str, ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef
        ],
    },
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef,
        "Total": Dict[str, ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef],
        "Groups": List[ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef],
        "Estimated": bool,
    },
    total=False,
)

ClientGetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "ClientGetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef],
        "ResultsByTime": List[ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef],
    },
    total=False,
)

_RequiredClientGetCostAndUsageWithResourcesTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetCostAndUsageWithResourcesTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetCostAndUsageWithResourcesTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetCostAndUsageWithResourcesTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetCostAndUsageWithResourcesTimePeriodTypeDef(
    _RequiredClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
    _OptionalClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
):
    pass


ClientGetCostForecastFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetCostForecastFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetCostForecastFilterDimensionsTypeDef = TypedDict(
    "ClientGetCostForecastFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetCostForecastFilterTagsTypeDef = TypedDict(
    "ClientGetCostForecastFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetCostForecastFilterTypeDef = TypedDict(
    "ClientGetCostForecastFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetCostForecastFilterDimensionsTypeDef,
        "Tags": ClientGetCostForecastFilterTagsTypeDef,
        "CostCategories": ClientGetCostForecastFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetCostForecastResponseForecastResultsByTimeTypeDef = TypedDict(
    "ClientGetCostForecastResponseForecastResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef,
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)

ClientGetCostForecastResponseTotalTypeDef = TypedDict(
    "ClientGetCostForecastResponseTotalTypeDef", {"Amount": str, "Unit": str}, total=False
)

ClientGetCostForecastResponseTypeDef = TypedDict(
    "ClientGetCostForecastResponseTypeDef",
    {
        "Total": ClientGetCostForecastResponseTotalTypeDef,
        "ForecastResultsByTime": List[ClientGetCostForecastResponseForecastResultsByTimeTypeDef],
    },
    total=False,
)

_RequiredClientGetCostForecastTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetCostForecastTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetCostForecastTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetCostForecastTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetCostForecastTimePeriodTypeDef(
    _RequiredClientGetCostForecastTimePeriodTypeDef, _OptionalClientGetCostForecastTimePeriodTypeDef
):
    pass


ClientGetDimensionValuesResponseDimensionValuesTypeDef = TypedDict(
    "ClientGetDimensionValuesResponseDimensionValuesTypeDef",
    {"Value": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientGetDimensionValuesResponseTypeDef = TypedDict(
    "ClientGetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List[ClientGetDimensionValuesResponseDimensionValuesTypeDef],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
    },
    total=False,
)

_RequiredClientGetDimensionValuesTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetDimensionValuesTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetDimensionValuesTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetDimensionValuesTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetDimensionValuesTimePeriodTypeDef(
    _RequiredClientGetDimensionValuesTimePeriodTypeDef,
    _OptionalClientGetDimensionValuesTimePeriodTypeDef,
):
    pass


ClientGetReservationCoverageFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetReservationCoverageFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetReservationCoverageFilterDimensionsTypeDef = TypedDict(
    "ClientGetReservationCoverageFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetReservationCoverageFilterTagsTypeDef = TypedDict(
    "ClientGetReservationCoverageFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetReservationCoverageFilterTypeDef = TypedDict(
    "ClientGetReservationCoverageFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetReservationCoverageFilterDimensionsTypeDef,
        "Tags": ClientGetReservationCoverageFilterTagsTypeDef,
        "CostCategories": ClientGetReservationCoverageFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetReservationCoverageGroupByTypeDef = TypedDict(
    "ClientGetReservationCoverageGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef,
    },
    total=False,
)

ClientGetReservationCoverageResponseCoveragesByTimeTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseCoveragesByTimeTypeDef",
    {
        "TimePeriod": ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef,
        "Groups": List[ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef],
        "Total": ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef,
    },
    total=False,
)

ClientGetReservationCoverageResponseTotalCoverageCostTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseTotalCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)

ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)

ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)

ClientGetReservationCoverageResponseTotalTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseTotalTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseTotalCoverageCostTypeDef,
    },
    total=False,
)

ClientGetReservationCoverageResponseTypeDef = TypedDict(
    "ClientGetReservationCoverageResponseTypeDef",
    {
        "CoveragesByTime": List[ClientGetReservationCoverageResponseCoveragesByTimeTypeDef],
        "Total": ClientGetReservationCoverageResponseTotalTypeDef,
        "NextPageToken": str,
    },
    total=False,
)

_RequiredClientGetReservationCoverageTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetReservationCoverageTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetReservationCoverageTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetReservationCoverageTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetReservationCoverageTimePeriodTypeDef(
    _RequiredClientGetReservationCoverageTimePeriodTypeDef,
    _OptionalClientGetReservationCoverageTimePeriodTypeDef,
):
    pass


ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "AvailabilityZone": str,
        "Platform": str,
        "Tenancy": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef",
    {
        "InstanceClass": str,
        "InstanceSize": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "ProductDescription": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "DatabaseEngine": str,
        "DatabaseEdition": str,
        "DeploymentOption": str,
        "LicenseModel": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef,
        "RDSInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef,
        "RedshiftInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef,
        "ElastiCacheInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef,
        "ESInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef",
    {
        "AccountId": str,
        "InstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef,
        "RecommendedNumberOfInstancesToPurchase": str,
        "RecommendedNormalizedUnitsToPurchase": str,
        "MinimumNumberOfInstancesUsedPerHour": str,
        "MinimumNormalizedUnitsUsedPerHour": str,
        "MaximumNumberOfInstancesUsedPerHour": str,
        "MaximumNormalizedUnitsUsedPerHour": str,
        "AverageNumberOfInstancesUsedPerHour": str,
        "AverageNormalizedUnitsUsedPerHour": str,
        "AverageUtilization": str,
        "EstimatedBreakEvenInMonths": str,
        "CurrencyCode": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedMonthlySavingsPercentage": str,
        "EstimatedMonthlyOnDemandCost": str,
        "EstimatedReservationCostForLookbackPeriod": str,
        "UpfrontCost": str,
        "RecurringStandardMonthlyCost": str,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": str,
        "TotalEstimatedMonthlySavingsPercentage": str,
        "CurrencyCode": str,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef",
    {"OfferingClass": Literal["STANDARD", "CONVERTIBLE"]},
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef",
    {
        "EC2Specification": ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef",
    {
        "AccountScope": Literal["PAYER", "LINKED"],
        "LookbackPeriodInDays": Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        "TermInYears": Literal["ONE_YEAR", "THREE_YEARS"],
        "PaymentOption": Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        "ServiceSpecification": ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef,
        "RecommendationDetails": List[
            ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef
        ],
        "RecommendationSummary": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef,
        "Recommendations": List[
            ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef",
    {"OfferingClass": Literal["STANDARD", "CONVERTIBLE"]},
    total=False,
)

ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef = TypedDict(
    "ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef",
    {
        "EC2Specification": ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef
    },
    total=False,
)

ClientGetReservationUtilizationFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetReservationUtilizationFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetReservationUtilizationFilterDimensionsTypeDef = TypedDict(
    "ClientGetReservationUtilizationFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetReservationUtilizationFilterTagsTypeDef = TypedDict(
    "ClientGetReservationUtilizationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetReservationUtilizationFilterTypeDef = TypedDict(
    "ClientGetReservationUtilizationFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetReservationUtilizationFilterDimensionsTypeDef,
        "Tags": ClientGetReservationUtilizationFilterTagsTypeDef,
        "CostCategories": ClientGetReservationUtilizationFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetReservationUtilizationGroupByTypeDef = TypedDict(
    "ClientGetReservationUtilizationGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetReservationUtilizationResponseTotalTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseTotalTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)

ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)

ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef",
    {
        "Key": str,
        "Value": str,
        "Attributes": Dict[str, str],
        "Utilization": ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef,
    },
    total=False,
)

ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)

ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef",
    {
        "TimePeriod": ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef,
        "Groups": List[ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef],
        "Total": ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef,
    },
    total=False,
)

ClientGetReservationUtilizationResponseTypeDef = TypedDict(
    "ClientGetReservationUtilizationResponseTypeDef",
    {
        "UtilizationsByTime": List[
            ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef
        ],
        "Total": ClientGetReservationUtilizationResponseTotalTypeDef,
        "NextPageToken": str,
    },
    total=False,
)

_RequiredClientGetReservationUtilizationTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetReservationUtilizationTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetReservationUtilizationTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetReservationUtilizationTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetReservationUtilizationTimePeriodTypeDef(
    _RequiredClientGetReservationUtilizationTimePeriodTypeDef,
    _OptionalClientGetReservationUtilizationTimePeriodTypeDef,
):
    pass


ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetRightsizingRecommendationFilterDimensionsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetRightsizingRecommendationFilterTagsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetRightsizingRecommendationFilterTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetRightsizingRecommendationFilterDimensionsTypeDef,
        "Tags": ClientGetRightsizingRecommendationFilterTagsTypeDef,
        "CostCategories": ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseMetadataTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "LookbackPeriodInDays": Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef",
    {
        "ResourceId": str,
        "Tags": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef
        ],
        "ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef,
        "ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef,
        "ReservationCoveredHoursInLookbackPeriod": str,
        "SavingsPlansCoveredHoursInLookbackPeriod": str,
        "OnDemandHoursInLookbackPeriod": str,
        "TotalRunningHoursInLookbackPeriod": str,
        "MonthlyCost": str,
        "CurrencyCode": str,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef",
    {
        "EstimatedMonthlyCost": str,
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
        "DefaultTargetInstance": bool,
        "ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef,
        "ExpectedResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef
        ]
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef",
    {"EstimatedMonthlySavings": str, "CurrencyCode": str},
    total=False,
)

ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef",
    {
        "AccountId": str,
        "CurrentInstance": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef,
        "RightsizingType": Literal["TERMINATE", "MODIFY"],
        "ModifyRecommendationDetail": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef,
        "TerminateRecommendationDetail": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseSummaryTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseSummaryTypeDef",
    {
        "TotalRecommendationCount": str,
        "EstimatedTotalMonthlySavingsAmount": str,
        "SavingsCurrencyCode": str,
        "SavingsPercentage": str,
    },
    total=False,
)

ClientGetRightsizingRecommendationResponseTypeDef = TypedDict(
    "ClientGetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetRightsizingRecommendationResponseMetadataTypeDef,
        "Summary": ClientGetRightsizingRecommendationResponseSummaryTypeDef,
        "RightsizingRecommendations": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetSavingsPlansCoverageFilterDimensionsTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetSavingsPlansCoverageFilterTagsTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetSavingsPlansCoverageFilterTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetSavingsPlansCoverageFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansCoverageFilterTagsTypeDef,
        "CostCategories": ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansCoverageGroupByTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)

ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef",
    {
        "SpendCoveredBySavingsPlans": str,
        "OnDemandCost": str,
        "TotalCost": str,
        "CoveragePercentage": str,
    },
    total=False,
)

ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef,
        "TimePeriod": ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "ClientGetSavingsPlansCoverageResponseTypeDef",
    {
        "SavingsPlansCoverages": List[
            ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientGetSavingsPlansCoverageTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetSavingsPlansCoverageTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetSavingsPlansCoverageTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetSavingsPlansCoverageTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetSavingsPlansCoverageTimePeriodTypeDef(
    _RequiredClientGetSavingsPlansCoverageTimePeriodTypeDef,
    _OptionalClientGetSavingsPlansCoverageTimePeriodTypeDef,
):
    pass


ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef = TypedDict(
    "ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)

ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef = TypedDict(
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef",
    {"Region": str, "InstanceFamily": str, "OfferingId": str},
    total=False,
)

ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef = TypedDict(
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef",
    {
        "SavingsPlansDetails": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef,
        "AccountId": str,
        "UpfrontCost": str,
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedSPCost": str,
        "EstimatedOnDemandCost": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
        "EstimatedSavingsAmount": str,
        "EstimatedSavingsPercentage": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedAverageUtilization": str,
        "EstimatedMonthlySavingsAmount": str,
        "CurrentMinimumHourlyOnDemandSpend": str,
        "CurrentMaximumHourlyOnDemandSpend": str,
        "CurrentAverageHourlyOnDemandSpend": str,
    },
    total=False,
)

ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedTotalCost": str,
        "CurrentOnDemandSpend": str,
        "EstimatedSavingsAmount": str,
        "TotalRecommendationCount": str,
        "DailyCommitmentToPurchase": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedSavingsPercentage": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
    },
    total=False,
)

ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef",
    {
        "SavingsPlansType": Literal["COMPUTE_SP", "EC2_INSTANCE_SP"],
        "TermInYears": Literal["ONE_YEAR", "THREE_YEARS"],
        "PaymentOption": Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        "LookbackPeriodInDays": Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        "SavingsPlansPurchaseRecommendationDetails": List[
            ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef
        ],
        "SavingsPlansPurchaseRecommendationSummary": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef,
        "SavingsPlansPurchaseRecommendation": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef,
        "NextPageToken": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsFilterTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef,
        "CostCategories": ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef",
    {
        "SavingsPlanArn": str,
        "Attributes": Dict[str, str],
        "Utilization": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef",
    {
        "Utilization": ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List[
            ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef
        ],
        "Total": ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef,
        "TimePeriod": ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef,
        "NextToken": str,
    },
    total=False,
)

_RequiredClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef(
    _RequiredClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
    _OptionalClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
):
    pass


ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetSavingsPlansUtilizationFilterTagsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetSavingsPlansUtilizationFilterTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansUtilizationFilterTagsTypeDef,
        "CostCategories": ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)

ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef",
    {
        "TimePeriod": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef,
        "Utilization": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)

ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseTotalTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseTotalTypeDef",
    {
        "Utilization": ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef,
    },
    total=False,
)

ClientGetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "ClientGetSavingsPlansUtilizationResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List[
            ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef
        ],
        "Total": ClientGetSavingsPlansUtilizationResponseTotalTypeDef,
    },
    total=False,
)

_RequiredClientGetSavingsPlansUtilizationTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetSavingsPlansUtilizationTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetSavingsPlansUtilizationTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetSavingsPlansUtilizationTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetSavingsPlansUtilizationTimePeriodTypeDef(
    _RequiredClientGetSavingsPlansUtilizationTimePeriodTypeDef,
    _OptionalClientGetSavingsPlansUtilizationTimePeriodTypeDef,
):
    pass


ClientGetTagsResponseTypeDef = TypedDict(
    "ClientGetTagsResponseTypeDef",
    {"NextPageToken": str, "Tags": List[str], "ReturnSize": int, "TotalSize": int},
    total=False,
)

_RequiredClientGetTagsTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetTagsTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetTagsTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetTagsTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetTagsTimePeriodTypeDef(
    _RequiredClientGetTagsTimePeriodTypeDef, _OptionalClientGetTagsTimePeriodTypeDef
):
    pass


ClientGetUsageForecastFilterCostCategoriesTypeDef = TypedDict(
    "ClientGetUsageForecastFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetUsageForecastFilterDimensionsTypeDef = TypedDict(
    "ClientGetUsageForecastFilterDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientGetUsageForecastFilterTagsTypeDef = TypedDict(
    "ClientGetUsageForecastFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetUsageForecastFilterTypeDef = TypedDict(
    "ClientGetUsageForecastFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetUsageForecastFilterDimensionsTypeDef,
        "Tags": ClientGetUsageForecastFilterTagsTypeDef,
        "CostCategories": ClientGetUsageForecastFilterCostCategoriesTypeDef,
    },
    total=False,
)

ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef = TypedDict(
    "ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)

ClientGetUsageForecastResponseForecastResultsByTimeTypeDef = TypedDict(
    "ClientGetUsageForecastResponseForecastResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef,
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)

ClientGetUsageForecastResponseTotalTypeDef = TypedDict(
    "ClientGetUsageForecastResponseTotalTypeDef", {"Amount": str, "Unit": str}, total=False
)

ClientGetUsageForecastResponseTypeDef = TypedDict(
    "ClientGetUsageForecastResponseTypeDef",
    {
        "Total": ClientGetUsageForecastResponseTotalTypeDef,
        "ForecastResultsByTime": List[ClientGetUsageForecastResponseForecastResultsByTimeTypeDef],
    },
    total=False,
)

_RequiredClientGetUsageForecastTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetUsageForecastTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetUsageForecastTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetUsageForecastTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetUsageForecastTimePeriodTypeDef(
    _RequiredClientGetUsageForecastTimePeriodTypeDef,
    _OptionalClientGetUsageForecastTimePeriodTypeDef,
):
    pass


ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef = TypedDict(
    "ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef",
    {"CostCategoryArn": str, "Name": str, "EffectiveStart": str, "EffectiveEnd": str},
    total=False,
)

ClientListCostCategoryDefinitionsResponseTypeDef = TypedDict(
    "ClientListCostCategoryDefinitionsResponseTypeDef",
    {
        "CostCategoryReferences": List[
            ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientUpdateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "ClientUpdateCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveStart": str},
    total=False,
)

ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef = TypedDict(
    "ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef = TypedDict(
    "ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    {
        "Key": Literal[
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
        "Values": List[str],
    },
    total=False,
)

ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef = TypedDict(
    "ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateCostCategoryDefinitionRulesRuleTypeDef = TypedDict(
    "ClientUpdateCostCategoryDefinitionRulesRuleTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef,
        "Tags": ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef,
        "CostCategories": ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef,
    },
    total=False,
)

ClientUpdateCostCategoryDefinitionRulesTypeDef = TypedDict(
    "ClientUpdateCostCategoryDefinitionRulesTypeDef",
    {"Value": str, "Rule": ClientUpdateCostCategoryDefinitionRulesRuleTypeDef},
    total=False,
)
