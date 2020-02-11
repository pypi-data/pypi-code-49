"""
Main interface for sns service client

Usage::

    import boto3
    from mypy_boto3.sns import SNSClient

    session = boto3.Session()

    client: SNSClient = boto3.client("sns")
    session_client: SNSClient = session.client("sns")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sns.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sns.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_sns.type_defs import (
    ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef,
    ClientConfirmSubscriptionResponseTypeDef,
    ClientCreatePlatformApplicationResponseTypeDef,
    ClientCreatePlatformEndpointResponseTypeDef,
    ClientCreateTopicResponseTypeDef,
    ClientCreateTopicTagsTypeDef,
    ClientGetEndpointAttributesResponseTypeDef,
    ClientGetPlatformApplicationAttributesResponseTypeDef,
    ClientGetSmsAttributesResponseTypeDef,
    ClientGetSubscriptionAttributesResponseTypeDef,
    ClientGetTopicAttributesResponseTypeDef,
    ClientListEndpointsByPlatformApplicationResponseTypeDef,
    ClientListPhoneNumbersOptedOutResponseTypeDef,
    ClientListPlatformApplicationsResponseTypeDef,
    ClientListSubscriptionsByTopicResponseTypeDef,
    ClientListSubscriptionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTopicsResponseTypeDef,
    ClientPublishMessageAttributesTypeDef,
    ClientPublishResponseTypeDef,
    ClientSubscribeResponseTypeDef,
    ClientTagResourceTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SNSClient",)


class SNSClient:
    """
    [SNS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_permission(
        self, TopicArn: str, Label: str, AWSAccountId: List[str], ActionName: List[str]
    ) -> None:
        """
        [Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.add_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.can_paginate)
        """

    def check_if_phone_number_is_opted_out(
        self, phoneNumber: str
    ) -> ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef:
        """
        [Client.check_if_phone_number_is_opted_out documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.check_if_phone_number_is_opted_out)
        """

    def confirm_subscription(
        self, TopicArn: str, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> ClientConfirmSubscriptionResponseTypeDef:
        """
        [Client.confirm_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.confirm_subscription)
        """

    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> ClientCreatePlatformApplicationResponseTypeDef:
        """
        [Client.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.create_platform_application)
        """

    def create_platform_endpoint(
        self,
        PlatformApplicationArn: str,
        Token: str,
        CustomUserData: str = None,
        Attributes: Dict[str, str] = None,
    ) -> ClientCreatePlatformEndpointResponseTypeDef:
        """
        [Client.create_platform_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.create_platform_endpoint)
        """

    def create_topic(
        self,
        Name: str,
        Attributes: Dict[str, str] = None,
        Tags: List[ClientCreateTopicTagsTypeDef] = None,
    ) -> ClientCreateTopicResponseTypeDef:
        """
        [Client.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.create_topic)
        """

    def delete_endpoint(self, EndpointArn: str) -> None:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.delete_endpoint)
        """

    def delete_platform_application(self, PlatformApplicationArn: str) -> None:
        """
        [Client.delete_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.delete_platform_application)
        """

    def delete_topic(self, TopicArn: str) -> None:
        """
        [Client.delete_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.delete_topic)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.generate_presigned_url)
        """

    def get_endpoint_attributes(
        self, EndpointArn: str
    ) -> ClientGetEndpointAttributesResponseTypeDef:
        """
        [Client.get_endpoint_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.get_endpoint_attributes)
        """

    def get_platform_application_attributes(
        self, PlatformApplicationArn: str
    ) -> ClientGetPlatformApplicationAttributesResponseTypeDef:
        """
        [Client.get_platform_application_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.get_platform_application_attributes)
        """

    def get_sms_attributes(
        self, attributes: List[str] = None
    ) -> ClientGetSmsAttributesResponseTypeDef:
        """
        [Client.get_sms_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.get_sms_attributes)
        """

    def get_subscription_attributes(
        self, SubscriptionArn: str
    ) -> ClientGetSubscriptionAttributesResponseTypeDef:
        """
        [Client.get_subscription_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.get_subscription_attributes)
        """

    def get_topic_attributes(self, TopicArn: str) -> ClientGetTopicAttributesResponseTypeDef:
        """
        [Client.get_topic_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.get_topic_attributes)
        """

    def list_endpoints_by_platform_application(
        self, PlatformApplicationArn: str, NextToken: str = None
    ) -> ClientListEndpointsByPlatformApplicationResponseTypeDef:
        """
        [Client.list_endpoints_by_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_endpoints_by_platform_application)
        """

    def list_phone_numbers_opted_out(
        self, nextToken: str = None
    ) -> ClientListPhoneNumbersOptedOutResponseTypeDef:
        """
        [Client.list_phone_numbers_opted_out documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_phone_numbers_opted_out)
        """

    def list_platform_applications(
        self, NextToken: str = None
    ) -> ClientListPlatformApplicationsResponseTypeDef:
        """
        [Client.list_platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_platform_applications)
        """

    def list_subscriptions(self, NextToken: str = None) -> ClientListSubscriptionsResponseTypeDef:
        """
        [Client.list_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_subscriptions)
        """

    def list_subscriptions_by_topic(
        self, TopicArn: str, NextToken: str = None
    ) -> ClientListSubscriptionsByTopicResponseTypeDef:
        """
        [Client.list_subscriptions_by_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_subscriptions_by_topic)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_tags_for_resource)
        """

    def list_topics(self, NextToken: str = None) -> ClientListTopicsResponseTypeDef:
        """
        [Client.list_topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.list_topics)
        """

    def opt_in_phone_number(self, phoneNumber: str) -> Dict[str, Any]:
        """
        [Client.opt_in_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.opt_in_phone_number)
        """

    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, ClientPublishMessageAttributesTypeDef] = None,
    ) -> ClientPublishResponseTypeDef:
        """
        [Client.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.publish)
        """

    def remove_permission(self, TopicArn: str, Label: str) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.remove_permission)
        """

    def set_endpoint_attributes(self, EndpointArn: str, Attributes: Dict[str, str]) -> None:
        """
        [Client.set_endpoint_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.set_endpoint_attributes)
        """

    def set_platform_application_attributes(
        self, PlatformApplicationArn: str, Attributes: Dict[str, str]
    ) -> None:
        """
        [Client.set_platform_application_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.set_platform_application_attributes)
        """

    def set_sms_attributes(self, attributes: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.set_sms_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.set_sms_attributes)
        """

    def set_subscription_attributes(
        self, SubscriptionArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        [Client.set_subscription_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.set_subscription_attributes)
        """

    def set_topic_attributes(
        self, TopicArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        [Client.set_topic_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.set_topic_attributes)
        """

    def subscribe(
        self,
        TopicArn: str,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> ClientSubscribeResponseTypeDef:
        """
        [Client.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.subscribe)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.tag_resource)
        """

    def unsubscribe(self, SubscriptionArn: str) -> None:
        """
        [Client.unsubscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.unsubscribe)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoints_by_platform_application"]
    ) -> "paginator_scope.ListEndpointsByPlatformApplicationPaginator":
        """
        [Paginator.ListEndpointsByPlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers_opted_out"]
    ) -> "paginator_scope.ListPhoneNumbersOptedOutPaginator":
        """
        [Paginator.ListPhoneNumbersOptedOut documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_platform_applications"]
    ) -> "paginator_scope.ListPlatformApplicationsPaginator":
        """
        [Paginator.ListPlatformApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> "paginator_scope.ListSubscriptionsPaginator":
        """
        [Paginator.ListSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions_by_topic"]
    ) -> "paginator_scope.ListSubscriptionsByTopicPaginator":
        """
        [Paginator.ListSubscriptionsByTopic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topics"]
    ) -> "paginator_scope.ListTopicsPaginator":
        """
        [Paginator.ListTopics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sns.html#SNS.Paginator.ListTopics)
        """


class Exceptions:
    AuthorizationErrorException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentAccessException: Boto3ClientError
    EndpointDisabledException: Boto3ClientError
    FilterPolicyLimitExceededException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidSecurityException: Boto3ClientError
    KMSAccessDeniedException: Boto3ClientError
    KMSDisabledException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KMSNotFoundException: Boto3ClientError
    KMSOptInRequired: Boto3ClientError
    KMSThrottlingException: Boto3ClientError
    NotFoundException: Boto3ClientError
    PlatformApplicationDisabledException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    StaleTagException: Boto3ClientError
    SubscriptionLimitExceededException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    ThrottledException: Boto3ClientError
    TopicLimitExceededException: Boto3ClientError
