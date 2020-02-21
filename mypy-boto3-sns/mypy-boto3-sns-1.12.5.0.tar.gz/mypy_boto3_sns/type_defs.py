"""
Main interface for sns service type definitions.

Usage::

    from mypy_boto3.sns.type_defs import ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef

    data: ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef = {...}
"""
import sys
from typing import Dict, IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ClientConfirmSubscriptionResponseTypeDef",
    "ClientCreatePlatformApplicationResponseTypeDef",
    "ClientCreatePlatformEndpointResponseTypeDef",
    "ClientCreateTopicResponseTypeDef",
    "ClientCreateTopicTagsTypeDef",
    "ClientGetEndpointAttributesResponseTypeDef",
    "ClientGetPlatformApplicationAttributesResponseTypeDef",
    "ClientGetSmsAttributesResponseTypeDef",
    "ClientGetSubscriptionAttributesResponseTypeDef",
    "ClientGetTopicAttributesResponseTypeDef",
    "ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    "ClientListEndpointsByPlatformApplicationResponseTypeDef",
    "ClientListPhoneNumbersOptedOutResponseTypeDef",
    "ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    "ClientListPlatformApplicationsResponseTypeDef",
    "ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    "ClientListSubscriptionsByTopicResponseTypeDef",
    "ClientListSubscriptionsResponseSubscriptionsTypeDef",
    "ClientListSubscriptionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTopicsResponseTopicsTypeDef",
    "ClientListTopicsResponseTypeDef",
    "ClientPublishMessageAttributesTypeDef",
    "ClientPublishResponseTypeDef",
    "ClientSubscribeResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ConfirmSubscriptionResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreatePlatformApplicationResponseTypeDef",
    "CreateTopicResponseTypeDef",
    "EndpointTypeDef",
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    "ListPhoneNumbersOptedOutResponseTypeDef",
    "PlatformApplicationTypeDef",
    "ListPlatformApplicationsResponseTypeDef",
    "SubscriptionTypeDef",
    "ListSubscriptionsByTopicResponseTypeDef",
    "ListSubscriptionsResponseTypeDef",
    "TopicTypeDef",
    "ListTopicsResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "PaginatorConfigTypeDef",
    "PublishResponseTypeDef",
    "SubscribeResponseTypeDef",
    "TagTypeDef",
)

ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef", {"isOptedOut": bool}, total=False
)

ClientConfirmSubscriptionResponseTypeDef = TypedDict(
    "ClientConfirmSubscriptionResponseTypeDef", {"SubscriptionArn": str}, total=False
)

ClientCreatePlatformApplicationResponseTypeDef = TypedDict(
    "ClientCreatePlatformApplicationResponseTypeDef", {"PlatformApplicationArn": str}, total=False
)

ClientCreatePlatformEndpointResponseTypeDef = TypedDict(
    "ClientCreatePlatformEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

ClientCreateTopicResponseTypeDef = TypedDict(
    "ClientCreateTopicResponseTypeDef", {"TopicArn": str}, total=False
)

ClientCreateTopicTagsTypeDef = TypedDict(
    "ClientCreateTopicTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetEndpointAttributesResponseTypeDef = TypedDict(
    "ClientGetEndpointAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "ClientGetPlatformApplicationAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)

ClientGetSmsAttributesResponseTypeDef = TypedDict(
    "ClientGetSmsAttributesResponseTypeDef", {"attributes": Dict[str, str]}, total=False
)

ClientGetSubscriptionAttributesResponseTypeDef = TypedDict(
    "ClientGetSubscriptionAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetTopicAttributesResponseTypeDef = TypedDict(
    "ClientGetTopicAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef = TypedDict(
    "ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "ClientListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List[ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "ClientListPhoneNumbersOptedOutResponseTypeDef",
    {"phoneNumbers": List[str], "nextToken": str},
    total=False,
)

ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef = TypedDict(
    "ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientListPlatformApplicationsResponseTypeDef = TypedDict(
    "ClientListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List[
            ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef = TypedDict(
    "ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ClientListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "ClientListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List[ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "ClientListSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ClientListSubscriptionsResponseTypeDef = TypedDict(
    "ClientListSubscriptionsResponseTypeDef",
    {"Subscriptions": List[ClientListSubscriptionsResponseSubscriptionsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListTopicsResponseTopicsTypeDef = TypedDict(
    "ClientListTopicsResponseTopicsTypeDef", {"TopicArn": str}, total=False
)

ClientListTopicsResponseTypeDef = TypedDict(
    "ClientListTopicsResponseTypeDef",
    {"Topics": List[ClientListTopicsResponseTopicsTypeDef], "NextToken": str},
    total=False,
)

ClientPublishMessageAttributesTypeDef = TypedDict(
    "ClientPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)

ClientPublishResponseTypeDef = TypedDict(
    "ClientPublishResponseTypeDef", {"MessageId": str}, total=False
)

ClientSubscribeResponseTypeDef = TypedDict(
    "ClientSubscribeResponseTypeDef", {"SubscriptionArn": str}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ConfirmSubscriptionResponseTypeDef = TypedDict(
    "ConfirmSubscriptionResponseTypeDef", {"SubscriptionArn": str}, total=False
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

CreatePlatformApplicationResponseTypeDef = TypedDict(
    "CreatePlatformApplicationResponseTypeDef", {"PlatformApplicationArn": str}, total=False
)

CreateTopicResponseTypeDef = TypedDict("CreateTopicResponseTypeDef", {"TopicArn": str}, total=False)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef", {"EndpointArn": str, "Attributes": Dict[str, str]}, total=False
)

ListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    {"Endpoints": List[EndpointTypeDef], "NextToken": str},
    total=False,
)

ListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutResponseTypeDef",
    {"phoneNumbers": List[str], "nextToken": str},
    total=False,
)

PlatformApplicationTypeDef = TypedDict(
    "PlatformApplicationTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ListPlatformApplicationsResponseTypeDef = TypedDict(
    "ListPlatformApplicationsResponseTypeDef",
    {"PlatformApplications": List[PlatformApplicationTypeDef], "NextToken": str},
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "ListSubscriptionsByTopicResponseTypeDef",
    {"Subscriptions": List[SubscriptionTypeDef], "NextToken": str},
    total=False,
)

ListSubscriptionsResponseTypeDef = TypedDict(
    "ListSubscriptionsResponseTypeDef",
    {"Subscriptions": List[SubscriptionTypeDef], "NextToken": str},
    total=False,
)

TopicTypeDef = TypedDict("TopicTypeDef", {"TopicArn": str}, total=False)

ListTopicsResponseTypeDef = TypedDict(
    "ListTopicsResponseTypeDef", {"Topics": List[TopicTypeDef], "NextToken": str}, total=False
)

_RequiredMessageAttributeValueTypeDef = TypedDict(
    "_RequiredMessageAttributeValueTypeDef", {"DataType": str}
)
_OptionalMessageAttributeValueTypeDef = TypedDict(
    "_OptionalMessageAttributeValueTypeDef",
    {"StringValue": str, "BinaryValue": Union[bytes, IO]},
    total=False,
)


class MessageAttributeValueTypeDef(
    _RequiredMessageAttributeValueTypeDef, _OptionalMessageAttributeValueTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PublishResponseTypeDef = TypedDict("PublishResponseTypeDef", {"MessageId": str}, total=False)

SubscribeResponseTypeDef = TypedDict(
    "SubscribeResponseTypeDef", {"SubscriptionArn": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})
