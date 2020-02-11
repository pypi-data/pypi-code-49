"""
Main interface for connect service client

Usage::

    import boto3
    from mypy_boto3.connect import ConnectClient

    session = boto3.Session()

    client: ConnectClient = boto3.client("connect")
    session_client: ConnectClient = session.client("connect")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_connect.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_connect.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_connect.type_defs import (
    ClientCreateUserIdentityInfoTypeDef,
    ClientCreateUserPhoneConfigTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientDescribeUserHierarchyGroupResponseTypeDef,
    ClientDescribeUserHierarchyStructureResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientGetContactAttributesResponseTypeDef,
    ClientGetCurrentMetricDataCurrentMetricsTypeDef,
    ClientGetCurrentMetricDataFiltersTypeDef,
    ClientGetCurrentMetricDataResponseTypeDef,
    ClientGetFederationTokenResponseTypeDef,
    ClientGetMetricDataFiltersTypeDef,
    ClientGetMetricDataHistoricalMetricsTypeDef,
    ClientGetMetricDataResponseTypeDef,
    ClientListContactFlowsResponseTypeDef,
    ClientListHoursOfOperationsResponseTypeDef,
    ClientListPhoneNumbersResponseTypeDef,
    ClientListQueuesResponseTypeDef,
    ClientListRoutingProfilesResponseTypeDef,
    ClientListSecurityProfilesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUserHierarchyGroupsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientStartChatContactInitialMessageTypeDef,
    ClientStartChatContactParticipantDetailsTypeDef,
    ClientStartChatContactResponseTypeDef,
    ClientStartOutboundVoiceContactResponseTypeDef,
    ClientUpdateUserIdentityInfoIdentityInfoTypeDef,
    ClientUpdateUserPhoneConfigPhoneConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectClient",)


class ConnectClient:
    """
    [Connect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.can_paginate)
        """

    def create_user(
        self,
        Username: str,
        PhoneConfig: ClientCreateUserPhoneConfigTypeDef,
        SecurityProfileIds: List[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str = None,
        IdentityInfo: ClientCreateUserIdentityInfoTypeDef = None,
        DirectoryUserId: str = None,
        HierarchyGroupId: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.create_user)
        """

    def delete_user(self, InstanceId: str, UserId: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.delete_user)
        """

    def describe_user(self, UserId: str, InstanceId: str) -> ClientDescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.describe_user)
        """

    def describe_user_hierarchy_group(
        self, HierarchyGroupId: str, InstanceId: str
    ) -> ClientDescribeUserHierarchyGroupResponseTypeDef:
        """
        [Client.describe_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.describe_user_hierarchy_group)
        """

    def describe_user_hierarchy_structure(
        self, InstanceId: str
    ) -> ClientDescribeUserHierarchyStructureResponseTypeDef:
        """
        [Client.describe_user_hierarchy_structure documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.describe_user_hierarchy_structure)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.generate_presigned_url)
        """

    def get_contact_attributes(
        self, InstanceId: str, InitialContactId: str
    ) -> ClientGetContactAttributesResponseTypeDef:
        """
        [Client.get_contact_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.get_contact_attributes)
        """

    def get_current_metric_data(
        self,
        InstanceId: str,
        Filters: ClientGetCurrentMetricDataFiltersTypeDef,
        CurrentMetrics: List[ClientGetCurrentMetricDataCurrentMetricsTypeDef],
        Groupings: List[Literal["QUEUE", "CHANNEL"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetCurrentMetricDataResponseTypeDef:
        """
        [Client.get_current_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.get_current_metric_data)
        """

    def get_federation_token(self, InstanceId: str) -> ClientGetFederationTokenResponseTypeDef:
        """
        [Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.get_federation_token)
        """

    def get_metric_data(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: ClientGetMetricDataFiltersTypeDef,
        HistoricalMetrics: List[ClientGetMetricDataHistoricalMetricsTypeDef],
        Groupings: List[Literal["QUEUE", "CHANNEL"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetMetricDataResponseTypeDef:
        """
        [Client.get_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.get_metric_data)
        """

    def list_contact_flows(
        self,
        InstanceId: str,
        ContactFlowTypes: List[
            Literal[
                "CONTACT_FLOW",
                "CUSTOMER_QUEUE",
                "CUSTOMER_HOLD",
                "CUSTOMER_WHISPER",
                "AGENT_HOLD",
                "AGENT_WHISPER",
                "OUTBOUND_WHISPER",
                "AGENT_TRANSFER",
                "QUEUE_TRANSFER",
            ]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListContactFlowsResponseTypeDef:
        """
        [Client.list_contact_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_contact_flows)
        """

    def list_hours_of_operations(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListHoursOfOperationsResponseTypeDef:
        """
        [Client.list_hours_of_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_hours_of_operations)
        """

    def list_phone_numbers(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[Literal["TOLL_FREE", "DID"]] = None,
        PhoneNumberCountryCodes: List[
            Literal[
                "AF",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BA",
                "BW",
                "BR",
                "IO",
                "VG",
                "BN",
                "BG",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CK",
                "CR",
                "HR",
                "CU",
                "CW",
                "CY",
                "CZ",
                "CD",
                "DK",
                "DJ",
                "DM",
                "DO",
                "TL",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "PF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GU",
                "GT",
                "GG",
                "GN",
                "GW",
                "GY",
                "HT",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IM",
                "IL",
                "IT",
                "CI",
                "JM",
                "JP",
                "JE",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MK",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "ME",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "AN",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "KP",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "CG",
                "RE",
                "RO",
                "RU",
                "RW",
                "BL",
                "SH",
                "KN",
                "LC",
                "MF",
                "PM",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "RS",
                "SC",
                "SL",
                "SG",
                "SX",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "KR",
                "ES",
                "LK",
                "SD",
                "SR",
                "SJ",
                "SZ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "VI",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UY",
                "UZ",
                "VU",
                "VA",
                "VE",
                "VN",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW",
            ]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPhoneNumbersResponseTypeDef:
        """
        [Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_phone_numbers)
        """

    def list_queues(
        self,
        InstanceId: str,
        QueueTypes: List[Literal["STANDARD", "AGENT"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListQueuesResponseTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_queues)
        """

    def list_routing_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListRoutingProfilesResponseTypeDef:
        """
        [Client.list_routing_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_routing_profiles)
        """

    def list_security_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListSecurityProfilesResponseTypeDef:
        """
        [Client.list_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_security_profiles)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_tags_for_resource)
        """

    def list_user_hierarchy_groups(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUserHierarchyGroupsResponseTypeDef:
        """
        [Client.list_user_hierarchy_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_user_hierarchy_groups)
        """

    def list_users(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.list_users)
        """

    def start_chat_contact(
        self,
        InstanceId: str,
        ContactFlowId: str,
        ParticipantDetails: ClientStartChatContactParticipantDetailsTypeDef,
        Attributes: Dict[str, str] = None,
        InitialMessage: ClientStartChatContactInitialMessageTypeDef = None,
        ClientToken: str = None,
    ) -> ClientStartChatContactResponseTypeDef:
        """
        [Client.start_chat_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.start_chat_contact)
        """

    def start_outbound_voice_contact(
        self,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        ClientToken: str = None,
        SourcePhoneNumber: str = None,
        QueueId: str = None,
        Attributes: Dict[str, str] = None,
    ) -> ClientStartOutboundVoiceContactResponseTypeDef:
        """
        [Client.start_outbound_voice_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.start_outbound_voice_contact)
        """

    def stop_contact(self, ContactId: str, InstanceId: str) -> Dict[str, Any]:
        """
        [Client.stop_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.stop_contact)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.untag_resource)
        """

    def update_contact_attributes(
        self, InitialContactId: str, InstanceId: str, Attributes: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Client.update_contact_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.update_contact_attributes)
        """

    def update_user_hierarchy(
        self, UserId: str, InstanceId: str, HierarchyGroupId: str = None
    ) -> None:
        """
        [Client.update_user_hierarchy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.update_user_hierarchy)
        """

    def update_user_identity_info(
        self,
        IdentityInfo: ClientUpdateUserIdentityInfoIdentityInfoTypeDef,
        UserId: str,
        InstanceId: str,
    ) -> None:
        """
        [Client.update_user_identity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.update_user_identity_info)
        """

    def update_user_phone_config(
        self,
        PhoneConfig: ClientUpdateUserPhoneConfigPhoneConfigTypeDef,
        UserId: str,
        InstanceId: str,
    ) -> None:
        """
        [Client.update_user_phone_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.update_user_phone_config)
        """

    def update_user_routing_profile(
        self, RoutingProfileId: str, UserId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.update_user_routing_profile)
        """

    def update_user_security_profiles(
        self, SecurityProfileIds: List[str], UserId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Client.update_user_security_profiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_metric_data"]
    ) -> "paginator_scope.GetMetricDataPaginator":
        """
        [Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.GetMetricData)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flows"]
    ) -> "paginator_scope.ListContactFlowsPaginator":
        """
        [Paginator.ListContactFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListContactFlows)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> "paginator_scope.ListHoursOfOperationsPaginator":
        """
        [Paginator.ListHoursOfOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers"]
    ) -> "paginator_scope.ListPhoneNumbersPaginator":
        """
        [Paginator.ListPhoneNumbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queues"]
    ) -> "paginator_scope.ListQueuesPaginator":
        """
        [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListQueues)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profiles"]
    ) -> "paginator_scope.ListRoutingProfilesPaginator":
        """
        [Paginator.ListRoutingProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> "paginator_scope.ListSecurityProfilesPaginator":
        """
        [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> "paginator_scope.ListUserHierarchyGroupsPaginator":
        """
        [Paginator.ListUserHierarchyGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> "paginator_scope.ListUsersPaginator":
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connect.html#Connect.Paginator.ListUsers)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ContactNotFoundException: Boto3ClientError
    DestinationNotAllowedException: Boto3ClientError
    DuplicateResourceException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OutboundContactNotPermittedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UserNotFoundException: Boto3ClientError
