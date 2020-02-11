"""
Main interface for budgets service client

Usage::

    import boto3
    from mypy_boto3.budgets import BudgetsClient

    session = boto3.Session()

    client: BudgetsClient = boto3.client("budgets")
    session_client: BudgetsClient = session.client("budgets")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_budgets.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_budgets.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_budgets.type_defs import (
    ClientCreateBudgetBudgetTypeDef,
    ClientCreateBudgetNotificationsWithSubscribersTypeDef,
    ClientCreateNotificationNotificationTypeDef,
    ClientCreateNotificationSubscribersTypeDef,
    ClientCreateSubscriberNotificationTypeDef,
    ClientCreateSubscriberSubscriberTypeDef,
    ClientDeleteNotificationNotificationTypeDef,
    ClientDeleteSubscriberNotificationTypeDef,
    ClientDeleteSubscriberSubscriberTypeDef,
    ClientDescribeBudgetPerformanceHistoryResponseTypeDef,
    ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef,
    ClientDescribeBudgetResponseTypeDef,
    ClientDescribeBudgetsResponseTypeDef,
    ClientDescribeNotificationsForBudgetResponseTypeDef,
    ClientDescribeSubscribersForNotificationNotificationTypeDef,
    ClientDescribeSubscribersForNotificationResponseTypeDef,
    ClientUpdateBudgetNewBudgetTypeDef,
    ClientUpdateNotificationNewNotificationTypeDef,
    ClientUpdateNotificationOldNotificationTypeDef,
    ClientUpdateSubscriberNewSubscriberTypeDef,
    ClientUpdateSubscriberNotificationTypeDef,
    ClientUpdateSubscriberOldSubscriberTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BudgetsClient",)


class BudgetsClient:
    """
    [Budgets.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.can_paginate)
        """

    def create_budget(
        self,
        AccountId: str,
        Budget: ClientCreateBudgetBudgetTypeDef,
        NotificationsWithSubscribers: List[
            ClientCreateBudgetNotificationsWithSubscribersTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.create_budget)
        """

    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientCreateNotificationNotificationTypeDef,
        Subscribers: List[ClientCreateNotificationSubscribersTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.create_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.create_notification)
        """

    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientCreateSubscriberNotificationTypeDef,
        Subscriber: ClientCreateSubscriberSubscriberTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.create_subscriber)
        """

    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        """
        [Client.delete_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.delete_budget)
        """

    def delete_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientDeleteNotificationNotificationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.delete_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.delete_notification)
        """

    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientDeleteSubscriberNotificationTypeDef,
        Subscriber: ClientDeleteSubscriberSubscriberTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.delete_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.delete_subscriber)
        """

    def describe_budget(
        self, AccountId: str, BudgetName: str
    ) -> ClientDescribeBudgetResponseTypeDef:
        """
        [Client.describe_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.describe_budget)
        """

    def describe_budget_performance_history(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeBudgetPerformanceHistoryResponseTypeDef:
        """
        [Client.describe_budget_performance_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)
        """

    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeBudgetsResponseTypeDef:
        """
        [Client.describe_budgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.describe_budgets)
        """

    def describe_notifications_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeNotificationsForBudgetResponseTypeDef:
        """
        [Client.describe_notifications_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)
        """

    def describe_subscribers_for_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientDescribeSubscribersForNotificationNotificationTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeSubscribersForNotificationResponseTypeDef:
        """
        [Client.describe_subscribers_for_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.generate_presigned_url)
        """

    def update_budget(
        self, AccountId: str, NewBudget: ClientUpdateBudgetNewBudgetTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.update_budget)
        """

    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: ClientUpdateNotificationOldNotificationTypeDef,
        NewNotification: ClientUpdateNotificationNewNotificationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.update_notification)
        """

    def update_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientUpdateSubscriberNotificationTypeDef,
        OldSubscriber: ClientUpdateSubscriberOldSubscriberTypeDef,
        NewSubscriber: ClientUpdateSubscriberNewSubscriberTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Client.update_subscriber)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> "paginator_scope.DescribeBudgetsPaginator":
        """
        [Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> "paginator_scope.DescribeNotificationsForBudgetPaginator":
        """
        [Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> "paginator_scope.DescribeSubscribersForNotificationPaginator":
        """
        [Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    CreationLimitExceededException: Boto3ClientError
    DuplicateRecordException: Boto3ClientError
    ExpiredNextTokenException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    NotFoundException: Boto3ClientError
