"""
Main interface for sns service client paginators.

Usage::

    import boto3
    from mypy_boto3.sns import (
        ListEndpointsByPlatformApplicationPaginator,
        ListPhoneNumbersOptedOutPaginator,
        ListPlatformApplicationsPaginator,
        ListSubscriptionsPaginator,
        ListSubscriptionsByTopicPaginator,
        ListTopicsPaginator,
    )

    client: SNSClient = boto3.client("sns")

    list_endpoints_by_platform_application_paginator: ListEndpointsByPlatformApplicationPaginator = client.get_paginator("list_endpoints_by_platform_application")
    list_phone_numbers_opted_out_paginator: ListPhoneNumbersOptedOutPaginator = client.get_paginator("list_phone_numbers_opted_out")
    list_platform_applications_paginator: ListPlatformApplicationsPaginator = client.get_paginator("list_platform_applications")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_subscriptions_by_topic_paginator: ListSubscriptionsByTopicPaginator = client.get_paginator("list_subscriptions_by_topic")
    list_topics_paginator: ListTopicsPaginator = client.get_paginator("list_topics")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sns.type_defs import (
    ListEndpointsByPlatformApplicationResponseTypeDef,
    ListPhoneNumbersOptedOutResponseTypeDef,
    ListPlatformApplicationsResponseTypeDef,
    ListSubscriptionsByTopicResponseTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTopicsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListTopicsPaginator",
)


class ListEndpointsByPlatformApplicationPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointsByPlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)
    """

    def paginate(
        self, PlatformApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEndpointsByPlatformApplicationResponseTypeDef, None, None]:
        """
        [ListEndpointsByPlatformApplication.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication.paginate)
        """


class ListPhoneNumbersOptedOutPaginator(Boto3Paginator):
    """
    [Paginator.ListPhoneNumbersOptedOut documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPhoneNumbersOptedOutResponseTypeDef, None, None]:
        """
        [ListPhoneNumbersOptedOut.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut.paginate)
        """


class ListPlatformApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlatformApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPlatformApplicationsResponseTypeDef, None, None]:
        """
        [ListPlatformApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListPlatformApplications.paginate)
        """


class ListSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListSubscriptions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscriptionsResponseTypeDef, None, None]:
        """
        [ListSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListSubscriptions.paginate)
        """


class ListSubscriptionsByTopicPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionsByTopic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)
    """

    def paginate(
        self, TopicArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscriptionsByTopicResponseTypeDef, None, None]:
        """
        [ListSubscriptionsByTopic.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic.paginate)
        """


class ListTopicsPaginator(Boto3Paginator):
    """
    [Paginator.ListTopics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListTopics)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTopicsResponseTypeDef, None, None]:
        """
        [ListTopics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListTopics.paginate)
        """
