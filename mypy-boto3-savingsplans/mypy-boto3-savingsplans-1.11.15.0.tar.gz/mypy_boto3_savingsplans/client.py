"""
Main interface for savingsplans service client

Usage::

    import boto3
    from mypy_boto3.savingsplans import SavingsPlansClient

    session = boto3.Session()

    client: SavingsPlansClient = boto3.client("savingsplans")
    session_client: SavingsPlansClient = session.client("savingsplans")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_savingsplans.client as client_scope
else:
    client_scope = object
from mypy_boto3_savingsplans.type_defs import (
    ClientCreateSavingsPlanResponseTypeDef,
    ClientDescribeSavingsPlanRatesFiltersTypeDef,
    ClientDescribeSavingsPlanRatesResponseTypeDef,
    ClientDescribeSavingsPlansFiltersTypeDef,
    ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef,
    ClientDescribeSavingsPlansOfferingRatesResponseTypeDef,
    ClientDescribeSavingsPlansOfferingsFiltersTypeDef,
    ClientDescribeSavingsPlansOfferingsResponseTypeDef,
    ClientDescribeSavingsPlansResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SavingsPlansClient",)


class SavingsPlansClient:
    """
    [SavingsPlans.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.can_paginate)
        """

    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateSavingsPlanResponseTypeDef:
        """
        [Client.create_savings_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.create_savings_plan)
        """

    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: List[ClientDescribeSavingsPlanRatesFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeSavingsPlanRatesResponseTypeDef:
        """
        [Client.describe_savings_plan_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plan_rates)
        """

    def describe_savings_plans(
        self,
        savingsPlanArns: List[str] = None,
        savingsPlanIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        states: List[Literal["payment-pending", "payment-failed", "active", "retired"]] = None,
        filters: List[ClientDescribeSavingsPlansFiltersTypeDef] = None,
    ) -> ClientDescribeSavingsPlansResponseTypeDef:
        """
        [Client.describe_savings_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans)
        """

    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: List[str] = None,
        savingsPlanPaymentOptions: List[
            Literal["All Upfront", "Partial Upfront", "No Upfront"]
        ] = None,
        savingsPlanTypes: List[Literal["Compute", "EC2Instance"]] = None,
        products: List[Literal["EC2", "Fargate"]] = None,
        serviceCodes: List[Literal["AmazonEC2", "AmazonECS"]] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeSavingsPlansOfferingRatesResponseTypeDef:
        """
        [Client.describe_savings_plans_offering_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offering_rates)
        """

    def describe_savings_plans_offerings(
        self,
        offeringIds: List[str] = None,
        paymentOptions: List[Literal["All Upfront", "Partial Upfront", "No Upfront"]] = None,
        productType: Literal["EC2", "Fargate"] = None,
        planTypes: List[Literal["Compute", "EC2Instance"]] = None,
        durations: List[int] = None,
        currencies: List[Literal["CNY", "USD"]] = None,
        descriptions: List[str] = None,
        serviceCodes: List[str] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[ClientDescribeSavingsPlansOfferingsFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeSavingsPlansOfferingsResponseTypeDef:
        """
        [Client.describe_savings_plans_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offerings)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/savingsplans.html#SavingsPlans.Client.untag_resource)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ValidationException: Boto3ClientError
