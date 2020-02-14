"""
Main interface for savingsplans service type definitions.

Usage::

    from mypy_boto3.savingsplans.type_defs import ClientCreateSavingsPlanResponseTypeDef

    data: ClientCreateSavingsPlanResponseTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateSavingsPlanResponseTypeDef",
    "ClientDescribeSavingsPlanRatesFiltersTypeDef",
    "ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlanRatesResponseTypeDef",
    "ClientDescribeSavingsPlansFiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponseTypeDef",
    "ClientDescribeSavingsPlansOfferingsFiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponseTypeDef",
    "ClientDescribeSavingsPlansResponsesavingsPlansTypeDef",
    "ClientDescribeSavingsPlansResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
)

ClientCreateSavingsPlanResponseTypeDef = TypedDict(
    "ClientCreateSavingsPlanResponseTypeDef", {"savingsPlanId": str}, total=False
)

ClientDescribeSavingsPlanRatesFiltersTypeDef = TypedDict(
    "ClientDescribeSavingsPlanRatesFiltersTypeDef",
    {
        "name": Literal[
            "region",
            "instanceType",
            "productDescription",
            "tenancy",
            "productType",
            "serviceCode",
            "usageType",
            "operation",
        ],
        "values": List[str],
    },
    total=False,
)

ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef = TypedDict(
    "ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef",
    {
        "name": Literal[
            "region", "instanceType", "instanceFamily", "productDescription", "tenancy"
        ],
        "value": str,
    },
    total=False,
)

ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef = TypedDict(
    "ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef",
    {
        "rate": str,
        "currency": Literal["CNY", "USD"],
        "unit": str,
        "productType": Literal["EC2", "Fargate"],
        "serviceCode": Literal["AmazonEC2", "AmazonECS"],
        "usageType": str,
        "operation": str,
        "properties": List[ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef],
    },
    total=False,
)

ClientDescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "ClientDescribeSavingsPlanRatesResponseTypeDef",
    {
        "savingsPlanId": str,
        "searchResults": List[ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeSavingsPlansFiltersTypeDef = TypedDict(
    "ClientDescribeSavingsPlansFiltersTypeDef",
    {
        "name": Literal[
            "region",
            "ec2-instance-family",
            "commitment",
            "upfront",
            "term",
            "savings-plan-type",
            "payment-option",
            "start",
            "end",
        ],
        "values": List[str],
    },
    total=False,
)

ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef",
    {
        "name": Literal[
            "region", "instanceFamily", "instanceType", "productDescription", "tenancy", "productId"
        ],
        "values": List[str],
    },
    total=False,
)

ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "planType": Literal["Compute", "EC2Instance"],
        "durationSeconds": int,
        "currency": Literal["CNY", "USD"],
        "planDescription": str,
    },
    total=False,
)

ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef",
    {
        "savingsPlanOffering": ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef,
        "rate": str,
        "unit": str,
        "productType": Literal["EC2", "Fargate"],
        "serviceCode": Literal["AmazonEC2", "AmazonECS"],
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)

ClientDescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingRatesResponseTypeDef",
    {
        "searchResults": List[ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeSavingsPlansOfferingsFiltersTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingsFiltersTypeDef",
    {"name": Literal["region", "instanceFamily"], "values": List[str]},
    total=False,
)

ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef",
    {"name": Literal["region", "instanceFamily"], "value": str},
    total=False,
)

ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef",
    {
        "offeringId": str,
        "productTypes": List[Literal["EC2", "Fargate"]],
        "planType": Literal["Compute", "EC2Instance"],
        "description": str,
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "durationSeconds": int,
        "currency": Literal["CNY", "USD"],
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)

ClientDescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "ClientDescribeSavingsPlansOfferingsResponseTypeDef",
    {
        "searchResults": List[ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeSavingsPlansResponsesavingsPlansTypeDef = TypedDict(
    "ClientDescribeSavingsPlansResponsesavingsPlansTypeDef",
    {
        "offeringId": str,
        "savingsPlanId": str,
        "savingsPlanArn": str,
        "description": str,
        "start": str,
        "end": str,
        "state": Literal["payment-pending", "payment-failed", "active", "retired"],
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": Literal["Compute", "EC2Instance"],
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "productTypes": List[Literal["EC2", "Fargate"]],
        "currency": Literal["CNY", "USD"],
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeSavingsPlansResponseTypeDef = TypedDict(
    "ClientDescribeSavingsPlansResponseTypeDef",
    {"savingsPlans": List[ClientDescribeSavingsPlansResponsesavingsPlansTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)
