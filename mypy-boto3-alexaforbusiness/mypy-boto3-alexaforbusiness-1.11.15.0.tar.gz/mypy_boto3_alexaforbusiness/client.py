"""
Main interface for alexaforbusiness service client

Usage::

    import boto3
    from mypy_boto3.alexaforbusiness import AlexaForBusinessClient

    session = boto3.Session()

    client: AlexaForBusinessClient = boto3.client("alexaforbusiness")
    session_client: AlexaForBusinessClient = session.client("alexaforbusiness")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_alexaforbusiness.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_alexaforbusiness.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_alexaforbusiness.type_defs import (
    ClientCreateAddressBookResponseTypeDef,
    ClientCreateBusinessReportScheduleContentRangeTypeDef,
    ClientCreateBusinessReportScheduleRecurrenceTypeDef,
    ClientCreateBusinessReportScheduleResponseTypeDef,
    ClientCreateConferenceProviderIPDialInTypeDef,
    ClientCreateConferenceProviderMeetingSettingTypeDef,
    ClientCreateConferenceProviderPSTNDialInTypeDef,
    ClientCreateConferenceProviderResponseTypeDef,
    ClientCreateContactPhoneNumbersTypeDef,
    ClientCreateContactResponseTypeDef,
    ClientCreateContactSipAddressesTypeDef,
    ClientCreateGatewayGroupResponseTypeDef,
    ClientCreateNetworkProfileResponseTypeDef,
    ClientCreateProfileMeetingRoomConfigurationTypeDef,
    ClientCreateProfileResponseTypeDef,
    ClientCreateRoomResponseTypeDef,
    ClientCreateRoomTagsTypeDef,
    ClientCreateSkillGroupResponseTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientCreateUserTagsTypeDef,
    ClientGetAddressBookResponseTypeDef,
    ClientGetConferencePreferenceResponseTypeDef,
    ClientGetConferenceProviderResponseTypeDef,
    ClientGetContactResponseTypeDef,
    ClientGetDeviceResponseTypeDef,
    ClientGetGatewayGroupResponseTypeDef,
    ClientGetGatewayResponseTypeDef,
    ClientGetInvitationConfigurationResponseTypeDef,
    ClientGetNetworkProfileResponseTypeDef,
    ClientGetProfileResponseTypeDef,
    ClientGetRoomResponseTypeDef,
    ClientGetRoomSkillParameterResponseTypeDef,
    ClientGetSkillGroupResponseTypeDef,
    ClientListBusinessReportSchedulesResponseTypeDef,
    ClientListConferenceProvidersResponseTypeDef,
    ClientListDeviceEventsResponseTypeDef,
    ClientListGatewayGroupsResponseTypeDef,
    ClientListGatewaysResponseTypeDef,
    ClientListSkillsResponseTypeDef,
    ClientListSkillsStoreCategoriesResponseTypeDef,
    ClientListSkillsStoreSkillsByCategoryResponseTypeDef,
    ClientListSmartHomeAppliancesResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientPutConferencePreferenceConferencePreferenceTypeDef,
    ClientPutRoomSkillParameterRoomSkillParameterTypeDef,
    ClientRegisterAvsDeviceResponseTypeDef,
    ClientResolveRoomResponseTypeDef,
    ClientSearchAddressBooksFiltersTypeDef,
    ClientSearchAddressBooksResponseTypeDef,
    ClientSearchAddressBooksSortCriteriaTypeDef,
    ClientSearchContactsFiltersTypeDef,
    ClientSearchContactsResponseTypeDef,
    ClientSearchContactsSortCriteriaTypeDef,
    ClientSearchDevicesFiltersTypeDef,
    ClientSearchDevicesResponseTypeDef,
    ClientSearchDevicesSortCriteriaTypeDef,
    ClientSearchNetworkProfilesFiltersTypeDef,
    ClientSearchNetworkProfilesResponseTypeDef,
    ClientSearchNetworkProfilesSortCriteriaTypeDef,
    ClientSearchProfilesFiltersTypeDef,
    ClientSearchProfilesResponseTypeDef,
    ClientSearchProfilesSortCriteriaTypeDef,
    ClientSearchRoomsFiltersTypeDef,
    ClientSearchRoomsResponseTypeDef,
    ClientSearchRoomsSortCriteriaTypeDef,
    ClientSearchSkillGroupsFiltersTypeDef,
    ClientSearchSkillGroupsResponseTypeDef,
    ClientSearchSkillGroupsSortCriteriaTypeDef,
    ClientSearchUsersFiltersTypeDef,
    ClientSearchUsersResponseTypeDef,
    ClientSearchUsersSortCriteriaTypeDef,
    ClientSendAnnouncementContentTypeDef,
    ClientSendAnnouncementResponseTypeDef,
    ClientSendAnnouncementRoomFiltersTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateBusinessReportScheduleRecurrenceTypeDef,
    ClientUpdateConferenceProviderIPDialInTypeDef,
    ClientUpdateConferenceProviderMeetingSettingTypeDef,
    ClientUpdateConferenceProviderPSTNDialInTypeDef,
    ClientUpdateContactPhoneNumbersTypeDef,
    ClientUpdateContactSipAddressesTypeDef,
    ClientUpdateProfileMeetingRoomConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AlexaForBusinessClient",)


class AlexaForBusinessClient:
    """
    [AlexaForBusiness.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client)
    """

    exceptions: "client_scope.Exceptions"

    def approve_skill(self, SkillId: str) -> Dict[str, Any]:
        """
        [Client.approve_skill documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.approve_skill)
        """

    def associate_contact_with_address_book(
        self, ContactArn: str, AddressBookArn: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_contact_with_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_contact_with_address_book)
        """

    def associate_device_with_network_profile(
        self, DeviceArn: str, NetworkProfileArn: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_device_with_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_device_with_network_profile)
        """

    def associate_device_with_room(
        self, DeviceArn: str = None, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_device_with_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_device_with_room)
        """

    def associate_skill_group_with_room(
        self, SkillGroupArn: str = None, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_skill_group_with_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_group_with_room)
        """

    def associate_skill_with_skill_group(
        self, SkillId: str, SkillGroupArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_skill_with_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_with_skill_group)
        """

    def associate_skill_with_users(self, SkillId: str) -> Dict[str, Any]:
        """
        [Client.associate_skill_with_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_with_users)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.can_paginate)
        """

    def create_address_book(
        self, Name: str, Description: str = None, ClientRequestToken: str = None
    ) -> ClientCreateAddressBookResponseTypeDef:
        """
        [Client.create_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_address_book)
        """

    def create_business_report_schedule(
        self,
        Format: Literal["CSV", "CSV_ZIP"],
        ContentRange: ClientCreateBusinessReportScheduleContentRangeTypeDef,
        ScheduleName: str = None,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        Recurrence: ClientCreateBusinessReportScheduleRecurrenceTypeDef = None,
        ClientRequestToken: str = None,
    ) -> ClientCreateBusinessReportScheduleResponseTypeDef:
        """
        [Client.create_business_report_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_business_report_schedule)
        """

    def create_conference_provider(
        self,
        ConferenceProviderName: str,
        ConferenceProviderType: Literal[
            "CHIME",
            "BLUEJEANS",
            "FUZE",
            "GOOGLE_HANGOUTS",
            "POLYCOM",
            "RINGCENTRAL",
            "SKYPE_FOR_BUSINESS",
            "WEBEX",
            "ZOOM",
            "CUSTOM",
        ],
        MeetingSetting: ClientCreateConferenceProviderMeetingSettingTypeDef,
        IPDialIn: ClientCreateConferenceProviderIPDialInTypeDef = None,
        PSTNDialIn: ClientCreateConferenceProviderPSTNDialInTypeDef = None,
        ClientRequestToken: str = None,
    ) -> ClientCreateConferenceProviderResponseTypeDef:
        """
        [Client.create_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_conference_provider)
        """

    def create_contact(
        self,
        FirstName: str,
        DisplayName: str = None,
        LastName: str = None,
        PhoneNumber: str = None,
        PhoneNumbers: List[ClientCreateContactPhoneNumbersTypeDef] = None,
        SipAddresses: List[ClientCreateContactSipAddressesTypeDef] = None,
        ClientRequestToken: str = None,
    ) -> ClientCreateContactResponseTypeDef:
        """
        [Client.create_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_contact)
        """

    def create_gateway_group(
        self, Name: str, ClientRequestToken: str, Description: str = None
    ) -> ClientCreateGatewayGroupResponseTypeDef:
        """
        [Client.create_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_gateway_group)
        """

    def create_network_profile(
        self,
        NetworkProfileName: str,
        Ssid: str,
        SecurityType: Literal["OPEN", "WEP", "WPA_PSK", "WPA2_PSK", "WPA2_ENTERPRISE"],
        ClientRequestToken: str,
        Description: str = None,
        EapMethod: str = None,
        CurrentPassword: str = None,
        NextPassword: str = None,
        CertificateAuthorityArn: str = None,
        TrustAnchors: List[str] = None,
    ) -> ClientCreateNetworkProfileResponseTypeDef:
        """
        [Client.create_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_network_profile)
        """

    def create_profile(
        self,
        ProfileName: str,
        Timezone: str,
        Address: str,
        DistanceUnit: Literal["METRIC", "IMPERIAL"],
        TemperatureUnit: Literal["FAHRENHEIT", "CELSIUS"],
        WakeWord: Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        Locale: str = None,
        ClientRequestToken: str = None,
        SetupModeDisabled: bool = None,
        MaxVolumeLimit: int = None,
        PSTNEnabled: bool = None,
        MeetingRoomConfiguration: ClientCreateProfileMeetingRoomConfigurationTypeDef = None,
    ) -> ClientCreateProfileResponseTypeDef:
        """
        [Client.create_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_profile)
        """

    def create_room(
        self,
        RoomName: str,
        Description: str = None,
        ProfileArn: str = None,
        ProviderCalendarId: str = None,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateRoomTagsTypeDef] = None,
    ) -> ClientCreateRoomResponseTypeDef:
        """
        [Client.create_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_room)
        """

    def create_skill_group(
        self, SkillGroupName: str, Description: str = None, ClientRequestToken: str = None
    ) -> ClientCreateSkillGroupResponseTypeDef:
        """
        [Client.create_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_skill_group)
        """

    def create_user(
        self,
        UserId: str,
        FirstName: str = None,
        LastName: str = None,
        Email: str = None,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateUserTagsTypeDef] = None,
    ) -> ClientCreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_user)
        """

    def delete_address_book(self, AddressBookArn: str) -> Dict[str, Any]:
        """
        [Client.delete_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_address_book)
        """

    def delete_business_report_schedule(self, ScheduleArn: str) -> Dict[str, Any]:
        """
        [Client.delete_business_report_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_business_report_schedule)
        """

    def delete_conference_provider(self, ConferenceProviderArn: str) -> Dict[str, Any]:
        """
        [Client.delete_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_conference_provider)
        """

    def delete_contact(self, ContactArn: str) -> Dict[str, Any]:
        """
        [Client.delete_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_contact)
        """

    def delete_device(self, DeviceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_device)
        """

    def delete_device_usage_data(self, DeviceArn: str, DeviceUsageType: str) -> Dict[str, Any]:
        """
        [Client.delete_device_usage_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_device_usage_data)
        """

    def delete_gateway_group(self, GatewayGroupArn: str) -> Dict[str, Any]:
        """
        [Client.delete_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_gateway_group)
        """

    def delete_network_profile(self, NetworkProfileArn: str) -> Dict[str, Any]:
        """
        [Client.delete_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_network_profile)
        """

    def delete_profile(self, ProfileArn: str = None) -> Dict[str, Any]:
        """
        [Client.delete_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_profile)
        """

    def delete_room(self, RoomArn: str = None) -> Dict[str, Any]:
        """
        [Client.delete_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_room)
        """

    def delete_room_skill_parameter(
        self, SkillId: str, ParameterKey: str, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_room_skill_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_room_skill_parameter)
        """

    def delete_skill_authorization(self, SkillId: str, RoomArn: str = None) -> Dict[str, Any]:
        """
        [Client.delete_skill_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_skill_authorization)
        """

    def delete_skill_group(self, SkillGroupArn: str = None) -> Dict[str, Any]:
        """
        [Client.delete_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_skill_group)
        """

    def delete_user(self, EnrollmentId: str, UserArn: str = None) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_user)
        """

    def disassociate_contact_from_address_book(
        self, ContactArn: str, AddressBookArn: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_contact_from_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_contact_from_address_book)
        """

    def disassociate_device_from_room(self, DeviceArn: str = None) -> Dict[str, Any]:
        """
        [Client.disassociate_device_from_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_device_from_room)
        """

    def disassociate_skill_from_skill_group(
        self, SkillId: str, SkillGroupArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_skill_from_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_from_skill_group)
        """

    def disassociate_skill_from_users(self, SkillId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_skill_from_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_from_users)
        """

    def disassociate_skill_group_from_room(
        self, SkillGroupArn: str = None, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_skill_group_from_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_group_from_room)
        """

    def forget_smart_home_appliances(self, RoomArn: str) -> Dict[str, Any]:
        """
        [Client.forget_smart_home_appliances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.forget_smart_home_appliances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.generate_presigned_url)
        """

    def get_address_book(self, AddressBookArn: str) -> ClientGetAddressBookResponseTypeDef:
        """
        [Client.get_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_address_book)
        """

    def get_conference_preference(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetConferencePreferenceResponseTypeDef:
        """
        [Client.get_conference_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_conference_preference)
        """

    def get_conference_provider(
        self, ConferenceProviderArn: str
    ) -> ClientGetConferenceProviderResponseTypeDef:
        """
        [Client.get_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_conference_provider)
        """

    def get_contact(self, ContactArn: str) -> ClientGetContactResponseTypeDef:
        """
        [Client.get_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_contact)
        """

    def get_device(self, DeviceArn: str = None) -> ClientGetDeviceResponseTypeDef:
        """
        [Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_device)
        """

    def get_gateway(self, GatewayArn: str) -> ClientGetGatewayResponseTypeDef:
        """
        [Client.get_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_gateway)
        """

    def get_gateway_group(self, GatewayGroupArn: str) -> ClientGetGatewayGroupResponseTypeDef:
        """
        [Client.get_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_gateway_group)
        """

    def get_invitation_configuration(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetInvitationConfigurationResponseTypeDef:
        """
        [Client.get_invitation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_invitation_configuration)
        """

    def get_network_profile(self, NetworkProfileArn: str) -> ClientGetNetworkProfileResponseTypeDef:
        """
        [Client.get_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_network_profile)
        """

    def get_profile(self, ProfileArn: str = None) -> ClientGetProfileResponseTypeDef:
        """
        [Client.get_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_profile)
        """

    def get_room(self, RoomArn: str = None) -> ClientGetRoomResponseTypeDef:
        """
        [Client.get_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_room)
        """

    def get_room_skill_parameter(
        self, SkillId: str, ParameterKey: str, RoomArn: str = None
    ) -> ClientGetRoomSkillParameterResponseTypeDef:
        """
        [Client.get_room_skill_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_room_skill_parameter)
        """

    def get_skill_group(self, SkillGroupArn: str = None) -> ClientGetSkillGroupResponseTypeDef:
        """
        [Client.get_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_skill_group)
        """

    def list_business_report_schedules(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListBusinessReportSchedulesResponseTypeDef:
        """
        [Client.list_business_report_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_business_report_schedules)
        """

    def list_conference_providers(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListConferenceProvidersResponseTypeDef:
        """
        [Client.list_conference_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_conference_providers)
        """

    def list_device_events(
        self,
        DeviceArn: str,
        EventType: Literal["CONNECTION_STATUS", "DEVICE_STATUS"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDeviceEventsResponseTypeDef:
        """
        [Client.list_device_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_device_events)
        """

    def list_gateway_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGatewayGroupsResponseTypeDef:
        """
        [Client.list_gateway_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_gateway_groups)
        """

    def list_gateways(
        self, GatewayGroupArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGatewaysResponseTypeDef:
        """
        [Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_gateways)
        """

    def list_skills(
        self,
        SkillGroupArn: str = None,
        EnablementType: Literal["ENABLED", "PENDING"] = None,
        SkillType: Literal["PUBLIC", "PRIVATE", "ALL"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListSkillsResponseTypeDef:
        """
        [Client.list_skills documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills)
        """

    def list_skills_store_categories(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListSkillsStoreCategoriesResponseTypeDef:
        """
        [Client.list_skills_store_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills_store_categories)
        """

    def list_skills_store_skills_by_category(
        self, CategoryId: int, NextToken: str = None, MaxResults: int = None
    ) -> ClientListSkillsStoreSkillsByCategoryResponseTypeDef:
        """
        [Client.list_skills_store_skills_by_category documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills_store_skills_by_category)
        """

    def list_smart_home_appliances(
        self, RoomArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListSmartHomeAppliancesResponseTypeDef:
        """
        [Client.list_smart_home_appliances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_smart_home_appliances)
        """

    def list_tags(
        self, Arn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_tags)
        """

    def put_conference_preference(
        self, ConferencePreference: ClientPutConferencePreferenceConferencePreferenceTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.put_conference_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_conference_preference)
        """

    def put_invitation_configuration(
        self, OrganizationName: str, ContactEmail: str = None, PrivateSkillIds: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Client.put_invitation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_invitation_configuration)
        """

    def put_room_skill_parameter(
        self,
        SkillId: str,
        RoomSkillParameter: ClientPutRoomSkillParameterRoomSkillParameterTypeDef,
        RoomArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_room_skill_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_room_skill_parameter)
        """

    def put_skill_authorization(
        self, AuthorizationResult: Dict[str, str], SkillId: str, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.put_skill_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_skill_authorization)
        """

    def register_avs_device(
        self, ClientId: str, UserCode: str, ProductId: str, DeviceSerialNumber: str, AmazonId: str
    ) -> ClientRegisterAvsDeviceResponseTypeDef:
        """
        [Client.register_avs_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.register_avs_device)
        """

    def reject_skill(self, SkillId: str) -> Dict[str, Any]:
        """
        [Client.reject_skill documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.reject_skill)
        """

    def resolve_room(self, UserId: str, SkillId: str) -> ClientResolveRoomResponseTypeDef:
        """
        [Client.resolve_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.resolve_room)
        """

    def revoke_invitation(self, UserArn: str = None, EnrollmentId: str = None) -> Dict[str, Any]:
        """
        [Client.revoke_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.revoke_invitation)
        """

    def search_address_books(
        self,
        Filters: List[ClientSearchAddressBooksFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchAddressBooksSortCriteriaTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientSearchAddressBooksResponseTypeDef:
        """
        [Client.search_address_books documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_address_books)
        """

    def search_contacts(
        self,
        Filters: List[ClientSearchContactsFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchContactsSortCriteriaTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientSearchContactsResponseTypeDef:
        """
        [Client.search_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_contacts)
        """

    def search_devices(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientSearchDevicesFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchDevicesSortCriteriaTypeDef] = None,
    ) -> ClientSearchDevicesResponseTypeDef:
        """
        [Client.search_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_devices)
        """

    def search_network_profiles(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientSearchNetworkProfilesFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchNetworkProfilesSortCriteriaTypeDef] = None,
    ) -> ClientSearchNetworkProfilesResponseTypeDef:
        """
        [Client.search_network_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_network_profiles)
        """

    def search_profiles(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientSearchProfilesFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchProfilesSortCriteriaTypeDef] = None,
    ) -> ClientSearchProfilesResponseTypeDef:
        """
        [Client.search_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_profiles)
        """

    def search_rooms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientSearchRoomsFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchRoomsSortCriteriaTypeDef] = None,
    ) -> ClientSearchRoomsResponseTypeDef:
        """
        [Client.search_rooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_rooms)
        """

    def search_skill_groups(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientSearchSkillGroupsFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchSkillGroupsSortCriteriaTypeDef] = None,
    ) -> ClientSearchSkillGroupsResponseTypeDef:
        """
        [Client.search_skill_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_skill_groups)
        """

    def search_users(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientSearchUsersFiltersTypeDef] = None,
        SortCriteria: List[ClientSearchUsersSortCriteriaTypeDef] = None,
    ) -> ClientSearchUsersResponseTypeDef:
        """
        [Client.search_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_users)
        """

    def send_announcement(
        self,
        RoomFilters: List[ClientSendAnnouncementRoomFiltersTypeDef],
        Content: ClientSendAnnouncementContentTypeDef,
        ClientRequestToken: str,
        TimeToLiveInSeconds: int = None,
    ) -> ClientSendAnnouncementResponseTypeDef:
        """
        [Client.send_announcement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.send_announcement)
        """

    def send_invitation(self, UserArn: str = None) -> Dict[str, Any]:
        """
        [Client.send_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.send_invitation)
        """

    def start_device_sync(
        self,
        Features: List[
            Literal[
                "BLUETOOTH",
                "VOLUME",
                "NOTIFICATIONS",
                "LISTS",
                "SKILLS",
                "NETWORK_PROFILE",
                "SETTINGS",
                "ALL",
            ]
        ],
        RoomArn: str = None,
        DeviceArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.start_device_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.start_device_sync)
        """

    def start_smart_home_appliance_discovery(self, RoomArn: str) -> Dict[str, Any]:
        """
        [Client.start_smart_home_appliance_discovery documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.start_smart_home_appliance_discovery)
        """

    def tag_resource(self, Arn: str, Tags: List[ClientTagResourceTagsTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.tag_resource)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.untag_resource)
        """

    def update_address_book(
        self, AddressBookArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_address_book)
        """

    def update_business_report_schedule(
        self,
        ScheduleArn: str,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        Format: Literal["CSV", "CSV_ZIP"] = None,
        ScheduleName: str = None,
        Recurrence: ClientUpdateBusinessReportScheduleRecurrenceTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_business_report_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_business_report_schedule)
        """

    def update_conference_provider(
        self,
        ConferenceProviderArn: str,
        ConferenceProviderType: Literal[
            "CHIME",
            "BLUEJEANS",
            "FUZE",
            "GOOGLE_HANGOUTS",
            "POLYCOM",
            "RINGCENTRAL",
            "SKYPE_FOR_BUSINESS",
            "WEBEX",
            "ZOOM",
            "CUSTOM",
        ],
        MeetingSetting: ClientUpdateConferenceProviderMeetingSettingTypeDef,
        IPDialIn: ClientUpdateConferenceProviderIPDialInTypeDef = None,
        PSTNDialIn: ClientUpdateConferenceProviderPSTNDialInTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_conference_provider)
        """

    def update_contact(
        self,
        ContactArn: str,
        DisplayName: str = None,
        FirstName: str = None,
        LastName: str = None,
        PhoneNumber: str = None,
        PhoneNumbers: List[ClientUpdateContactPhoneNumbersTypeDef] = None,
        SipAddresses: List[ClientUpdateContactSipAddressesTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_contact)
        """

    def update_device(self, DeviceArn: str = None, DeviceName: str = None) -> Dict[str, Any]:
        """
        [Client.update_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_device)
        """

    def update_gateway(
        self,
        GatewayArn: str,
        Name: str = None,
        Description: str = None,
        SoftwareVersion: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_gateway)
        """

    def update_gateway_group(
        self, GatewayGroupArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_gateway_group)
        """

    def update_network_profile(
        self,
        NetworkProfileArn: str,
        NetworkProfileName: str = None,
        Description: str = None,
        CurrentPassword: str = None,
        NextPassword: str = None,
        CertificateAuthorityArn: str = None,
        TrustAnchors: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_network_profile)
        """

    def update_profile(
        self,
        ProfileArn: str = None,
        ProfileName: str = None,
        IsDefault: bool = None,
        Timezone: str = None,
        Address: str = None,
        DistanceUnit: Literal["METRIC", "IMPERIAL"] = None,
        TemperatureUnit: Literal["FAHRENHEIT", "CELSIUS"] = None,
        WakeWord: Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"] = None,
        Locale: str = None,
        SetupModeDisabled: bool = None,
        MaxVolumeLimit: int = None,
        PSTNEnabled: bool = None,
        MeetingRoomConfiguration: ClientUpdateProfileMeetingRoomConfigurationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_profile)
        """

    def update_room(
        self,
        RoomArn: str = None,
        RoomName: str = None,
        Description: str = None,
        ProviderCalendarId: str = None,
        ProfileArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_room)
        """

    def update_skill_group(
        self, SkillGroupArn: str = None, SkillGroupName: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_skill_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_business_report_schedules"]
    ) -> "paginator_scope.ListBusinessReportSchedulesPaginator":
        """
        [Paginator.ListBusinessReportSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_conference_providers"]
    ) -> "paginator_scope.ListConferenceProvidersPaginator":
        """
        [Paginator.ListConferenceProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_events"]
    ) -> "paginator_scope.ListDeviceEventsPaginator":
        """
        [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_skills"]
    ) -> "paginator_scope.ListSkillsPaginator":
        """
        [Paginator.ListSkills documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_skills_store_categories"]
    ) -> "paginator_scope.ListSkillsStoreCategoriesPaginator":
        """
        [Paginator.ListSkillsStoreCategories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_skills_store_skills_by_category"]
    ) -> "paginator_scope.ListSkillsStoreSkillsByCategoryPaginator":
        """
        [Paginator.ListSkillsStoreSkillsByCategory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_smart_home_appliances"]
    ) -> "paginator_scope.ListSmartHomeAppliancesPaginator":
        """
        [Paginator.ListSmartHomeAppliances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags"]
    ) -> "paginator_scope.ListTagsPaginator":
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_devices"]
    ) -> "paginator_scope.SearchDevicesPaginator":
        """
        [Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_profiles"]
    ) -> "paginator_scope.SearchProfilesPaginator":
        """
        [Paginator.SearchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_rooms"]
    ) -> "paginator_scope.SearchRoomsPaginator":
        """
        [Paginator.SearchRooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_skill_groups"]
    ) -> "paginator_scope.SearchSkillGroupsPaginator":
        """
        [Paginator.SearchSkillGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_users"]
    ) -> "paginator_scope.SearchUsersPaginator":
        """
        [Paginator.SearchUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DeviceNotRegisteredException: Boto3ClientError
    InvalidCertificateAuthorityException: Boto3ClientError
    InvalidDeviceException: Boto3ClientError
    InvalidSecretsManagerResourceException: Boto3ClientError
    InvalidServiceLinkedRoleStateException: Boto3ClientError
    InvalidUserStatusException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NameInUseException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceAssociatedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    SkillNotLinkedException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
