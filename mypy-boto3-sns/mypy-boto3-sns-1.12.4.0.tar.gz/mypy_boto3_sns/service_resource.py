"""
Main interface for sns service ServiceResource

Usage::

    import boto3
    from mypy_boto3.sns import SNSServiceResource
    import mypy_boto3.sns.service_resource as sns_resources

    resource: SNSServiceResource = boto3.resource("sns")
    session_resource: SNSServiceResource = session.resource("sns")

    PlatformApplication: sns_resources.PlatformApplication = resource.PlatformApplication(...)
    ...
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING, Type, TypeVar
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from mypy_boto3_sns.type_defs import (
    ConfirmSubscriptionResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreatePlatformApplicationResponseTypeDef,
    CreateTopicResponseTypeDef,
    MessageAttributeValueTypeDef,
    PublishResponseTypeDef,
    SubscribeResponseTypeDef,
    TagTypeDef,
)


__all__ = (
    "SNSServiceResource",
    "PlatformApplication",
    "PlatformEndpoint",
    "Subscription",
    "Topic",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "PlatformApplicationEndpointsCollection",
    "TopicSubscriptionsCollection",
)

_ServiceResourcePlatformApplicationsCollectionType = TypeVar(
    "_ServiceResourcePlatformApplicationsCollectionType",
    bound="ServiceResourcePlatformApplicationsCollection",
)


class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [ServiceResource.platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.platform_applications)
    """

    @classmethod
    def all(
        cls: Type[_ServiceResourcePlatformApplicationsCollectionType],
    ) -> Type[_ServiceResourcePlatformApplicationsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_ServiceResourcePlatformApplicationsCollectionType], NextToken: str = None
    ) -> Type[_ServiceResourcePlatformApplicationsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_ServiceResourcePlatformApplicationsCollectionType], count: int
    ) -> Type[_ServiceResourcePlatformApplicationsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_ServiceResourcePlatformApplicationsCollectionType], count: int
    ) -> Type[_ServiceResourcePlatformApplicationsCollectionType]:
        pass

    @classmethod
    def pages(
        cls: Type[_ServiceResourcePlatformApplicationsCollectionType],
    ) -> List["PlatformApplication"]:
        pass


_ServiceResourceSubscriptionsCollectionType = TypeVar(
    "_ServiceResourceSubscriptionsCollectionType", bound="ServiceResourceSubscriptionsCollection"
)


class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [ServiceResource.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.subscriptions)
    """

    @classmethod
    def all(
        cls: Type[_ServiceResourceSubscriptionsCollectionType],
    ) -> Type[_ServiceResourceSubscriptionsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_ServiceResourceSubscriptionsCollectionType], NextToken: str = None
    ) -> Type[_ServiceResourceSubscriptionsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_ServiceResourceSubscriptionsCollectionType], count: int
    ) -> Type[_ServiceResourceSubscriptionsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_ServiceResourceSubscriptionsCollectionType], count: int
    ) -> Type[_ServiceResourceSubscriptionsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_ServiceResourceSubscriptionsCollectionType]) -> List["Subscription"]:
        pass


_ServiceResourceTopicsCollectionType = TypeVar(
    "_ServiceResourceTopicsCollectionType", bound="ServiceResourceTopicsCollection"
)


class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [ServiceResource.topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.topics)
    """

    @classmethod
    def all(
        cls: Type[_ServiceResourceTopicsCollectionType],
    ) -> Type[_ServiceResourceTopicsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_ServiceResourceTopicsCollectionType], NextToken: str = None
    ) -> Type[_ServiceResourceTopicsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_ServiceResourceTopicsCollectionType], count: int
    ) -> Type[_ServiceResourceTopicsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_ServiceResourceTopicsCollectionType], count: int
    ) -> Type[_ServiceResourceTopicsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_ServiceResourceTopicsCollectionType]) -> List["Topic"]:
        pass


_PlatformApplicationEndpointsCollectionType = TypeVar(
    "_PlatformApplicationEndpointsCollectionType", bound="PlatformApplicationEndpointsCollection"
)


class PlatformApplicationEndpointsCollection(ResourceCollection):
    """
    [PlatformApplication.endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.endpoints)
    """

    @classmethod
    def all(
        cls: Type[_PlatformApplicationEndpointsCollectionType],
    ) -> Type[_PlatformApplicationEndpointsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_PlatformApplicationEndpointsCollectionType], NextToken: str = None
    ) -> Type[_PlatformApplicationEndpointsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_PlatformApplicationEndpointsCollectionType], count: int
    ) -> Type[_PlatformApplicationEndpointsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_PlatformApplicationEndpointsCollectionType], count: int
    ) -> Type[_PlatformApplicationEndpointsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_PlatformApplicationEndpointsCollectionType]) -> List["PlatformEndpoint"]:
        pass


_TopicSubscriptionsCollectionType = TypeVar(
    "_TopicSubscriptionsCollectionType", bound="TopicSubscriptionsCollection"
)


class TopicSubscriptionsCollection(ResourceCollection):
    """
    [Topic.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.subscriptions)
    """

    @classmethod
    def all(
        cls: Type[_TopicSubscriptionsCollectionType],
    ) -> Type[_TopicSubscriptionsCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_TopicSubscriptionsCollectionType], NextToken: str = None
    ) -> Type[_TopicSubscriptionsCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_TopicSubscriptionsCollectionType], count: int
    ) -> Type[_TopicSubscriptionsCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_TopicSubscriptionsCollectionType], count: int
    ) -> Type[_TopicSubscriptionsCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_TopicSubscriptionsCollectionType]) -> List["Subscription"]:
        pass


_PlatformEndpointType = TypeVar("_PlatformEndpointType", bound="PlatformEndpoint")


class PlatformEndpoint(Boto3ServiceResource):
    """
    [PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
    """

    attributes: Dict[str, Any]
    arn: str

    def delete(self) -> None:
        """
        [PlatformEndpoint.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformEndpoint.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [PlatformEndpoint.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformEndpoint.get_available_subresources)
        """

    def load(self) -> None:
        """
        [PlatformEndpoint.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformEndpoint.load)
        """

    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
    ) -> PublishResponseTypeDef:
        """
        [PlatformEndpoint.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformEndpoint.publish)
        """

    def reload(self) -> None:
        """
        [PlatformEndpoint.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformEndpoint.reload)
        """

    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        """
        [PlatformEndpoint.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformEndpoint.set_attributes)
        """


_PlatformEndpoint = PlatformEndpoint


_SubscriptionType = TypeVar("_SubscriptionType", bound="Subscription")


class Subscription(Boto3ServiceResource):
    """
    [Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.Subscription)
    """

    attributes: Dict[str, Any]
    arn: str

    def delete(self) -> None:
        """
        [Subscription.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Subscription.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Subscription.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Subscription.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Subscription.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Subscription.load)
        """

    def reload(self) -> None:
        """
        [Subscription.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Subscription.reload)
        """

    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        """
        [Subscription.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Subscription.set_attributes)
        """


_Subscription = Subscription


_TopicType = TypeVar("_TopicType", bound="Topic")


class Topic(Boto3ServiceResource):
    """
    [Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.Topic)
    """

    attributes: Dict[str, Any]
    arn: str
    subscriptions: TopicSubscriptionsCollection

    def add_permission(self, Label: str, AWSAccountId: List[str], ActionName: List[str]) -> None:
        """
        [Topic.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.add_permission)
        """

    def confirm_subscription(
        self, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> ConfirmSubscriptionResponseTypeDef:
        """
        [Topic.confirm_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.confirm_subscription)
        """

    def delete(self) -> None:
        """
        [Topic.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Topic.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Topic.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.load)
        """

    def publish(
        self,
        Message: str,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
    ) -> PublishResponseTypeDef:
        """
        [Topic.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.publish)
        """

    def reload(self) -> None:
        """
        [Topic.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.reload)
        """

    def remove_permission(self, Label: str) -> None:
        """
        [Topic.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.remove_permission)
        """

    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        """
        [Topic.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.set_attributes)
        """

    def subscribe(
        self,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> SubscribeResponseTypeDef:
        """
        [Topic.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.Topic.subscribe)
        """


_Topic = Topic


_PlatformApplicationType = TypeVar("_PlatformApplicationType", bound="PlatformApplication")


class PlatformApplication(Boto3ServiceResource):
    """
    [PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
    """

    attributes: Dict[str, Any]
    arn: str
    endpoints: PlatformApplicationEndpointsCollection

    def create_platform_endpoint(
        self, Token: str, CustomUserData: str = None, Attributes: Dict[str, str] = None
    ) -> CreateEndpointResponseTypeDef:
        """
        [PlatformApplication.create_platform_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.create_platform_endpoint)
        """

    def delete(self) -> None:
        """
        [PlatformApplication.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [PlatformApplication.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.get_available_subresources)
        """

    def load(self) -> None:
        """
        [PlatformApplication.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.load)
        """

    def reload(self) -> None:
        """
        [PlatformApplication.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.reload)
        """

    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        """
        [PlatformApplication.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.PlatformApplication.set_attributes)
        """


_PlatformApplication = PlatformApplication


class SNSServiceResource(Boto3ServiceResource):
    """
    [SNS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource)
    """

    platform_applications: ServiceResourcePlatformApplicationsCollection
    subscriptions: ServiceResourceSubscriptionsCollection
    topics: ServiceResourceTopicsCollection

    def PlatformApplication(self, arn: str) -> _PlatformApplication:
        """
        [ServiceResource.PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
        """

    def PlatformEndpoint(self, arn: str) -> _PlatformEndpoint:
        """
        [ServiceResource.PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
        """

    def Subscription(self, arn: str) -> _Subscription:
        """
        [ServiceResource.Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.Subscription)
        """

    def Topic(self, arn: str) -> _Topic:
        """
        [ServiceResource.Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.Topic)
        """

    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> CreatePlatformApplicationResponseTypeDef:
        """
        [ServiceResource.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.create_platform_application)
        """

    def create_topic(
        self, Name: str, Attributes: Dict[str, str] = None, Tags: List[TagTypeDef] = None
    ) -> CreateTopicResponseTypeDef:
        """
        [ServiceResource.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.create_topic)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.4/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)
        """
