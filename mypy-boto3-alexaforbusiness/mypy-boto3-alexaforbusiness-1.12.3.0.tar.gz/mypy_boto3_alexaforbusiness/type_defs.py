"""
Main interface for alexaforbusiness service type definitions.

Usage::

    from mypy_boto3.alexaforbusiness.type_defs import ClientCreateAddressBookResponseTypeDef

    data: ClientCreateAddressBookResponseTypeDef = {...}
"""
from datetime import datetime
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
    "ClientCreateAddressBookResponseTypeDef",
    "ClientCreateBusinessReportScheduleContentRangeTypeDef",
    "ClientCreateBusinessReportScheduleRecurrenceTypeDef",
    "ClientCreateBusinessReportScheduleResponseTypeDef",
    "ClientCreateConferenceProviderIPDialInTypeDef",
    "ClientCreateConferenceProviderMeetingSettingTypeDef",
    "ClientCreateConferenceProviderPSTNDialInTypeDef",
    "ClientCreateConferenceProviderResponseTypeDef",
    "ClientCreateContactPhoneNumbersTypeDef",
    "ClientCreateContactResponseTypeDef",
    "ClientCreateContactSipAddressesTypeDef",
    "ClientCreateGatewayGroupResponseTypeDef",
    "ClientCreateNetworkProfileResponseTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationTypeDef",
    "ClientCreateProfileResponseTypeDef",
    "ClientCreateRoomResponseTypeDef",
    "ClientCreateRoomTagsTypeDef",
    "ClientCreateSkillGroupResponseTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientGetAddressBookResponseAddressBookTypeDef",
    "ClientGetAddressBookResponseTypeDef",
    "ClientGetConferencePreferenceResponsePreferenceTypeDef",
    "ClientGetConferencePreferenceResponseTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderTypeDef",
    "ClientGetConferenceProviderResponseTypeDef",
    "ClientGetContactResponseContactPhoneNumbersTypeDef",
    "ClientGetContactResponseContactSipAddressesTypeDef",
    "ClientGetContactResponseContactTypeDef",
    "ClientGetContactResponseTypeDef",
    "ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef",
    "ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef",
    "ClientGetDeviceResponseDeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetGatewayGroupResponseGatewayGroupTypeDef",
    "ClientGetGatewayGroupResponseTypeDef",
    "ClientGetGatewayResponseGatewayTypeDef",
    "ClientGetGatewayResponseTypeDef",
    "ClientGetInvitationConfigurationResponseTypeDef",
    "ClientGetNetworkProfileResponseNetworkProfileTypeDef",
    "ClientGetNetworkProfileResponseTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef",
    "ClientGetProfileResponseProfileTypeDef",
    "ClientGetProfileResponseTypeDef",
    "ClientGetRoomResponseRoomTypeDef",
    "ClientGetRoomResponseTypeDef",
    "ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef",
    "ClientGetRoomSkillParameterResponseTypeDef",
    "ClientGetSkillGroupResponseSkillGroupTypeDef",
    "ClientGetSkillGroupResponseTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef",
    "ClientListBusinessReportSchedulesResponseTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersTypeDef",
    "ClientListConferenceProvidersResponseTypeDef",
    "ClientListDeviceEventsResponseDeviceEventsTypeDef",
    "ClientListDeviceEventsResponseTypeDef",
    "ClientListGatewayGroupsResponseGatewayGroupsTypeDef",
    "ClientListGatewayGroupsResponseTypeDef",
    "ClientListGatewaysResponseGatewaysTypeDef",
    "ClientListGatewaysResponseTypeDef",
    "ClientListSkillsResponseSkillSummariesTypeDef",
    "ClientListSkillsResponseTypeDef",
    "ClientListSkillsStoreCategoriesResponseCategoryListTypeDef",
    "ClientListSkillsStoreCategoriesResponseTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseTypeDef",
    "ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef",
    "ClientListSmartHomeAppliancesResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientPutConferencePreferenceConferencePreferenceTypeDef",
    "ClientPutRoomSkillParameterRoomSkillParameterTypeDef",
    "ClientRegisterAvsDeviceResponseTypeDef",
    "ClientResolveRoomResponseRoomSkillParametersTypeDef",
    "ClientResolveRoomResponseTypeDef",
    "ClientSearchAddressBooksFiltersTypeDef",
    "ClientSearchAddressBooksResponseAddressBooksTypeDef",
    "ClientSearchAddressBooksResponseTypeDef",
    "ClientSearchAddressBooksSortCriteriaTypeDef",
    "ClientSearchContactsFiltersTypeDef",
    "ClientSearchContactsResponseContactsPhoneNumbersTypeDef",
    "ClientSearchContactsResponseContactsSipAddressesTypeDef",
    "ClientSearchContactsResponseContactsTypeDef",
    "ClientSearchContactsResponseTypeDef",
    "ClientSearchContactsSortCriteriaTypeDef",
    "ClientSearchDevicesFiltersTypeDef",
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef",
    "ClientSearchDevicesResponseDevicesTypeDef",
    "ClientSearchDevicesResponseTypeDef",
    "ClientSearchDevicesSortCriteriaTypeDef",
    "ClientSearchNetworkProfilesFiltersTypeDef",
    "ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef",
    "ClientSearchNetworkProfilesResponseTypeDef",
    "ClientSearchNetworkProfilesSortCriteriaTypeDef",
    "ClientSearchProfilesFiltersTypeDef",
    "ClientSearchProfilesResponseProfilesTypeDef",
    "ClientSearchProfilesResponseTypeDef",
    "ClientSearchProfilesSortCriteriaTypeDef",
    "ClientSearchRoomsFiltersTypeDef",
    "ClientSearchRoomsResponseRoomsTypeDef",
    "ClientSearchRoomsResponseTypeDef",
    "ClientSearchRoomsSortCriteriaTypeDef",
    "ClientSearchSkillGroupsFiltersTypeDef",
    "ClientSearchSkillGroupsResponseSkillGroupsTypeDef",
    "ClientSearchSkillGroupsResponseTypeDef",
    "ClientSearchSkillGroupsSortCriteriaTypeDef",
    "ClientSearchUsersFiltersTypeDef",
    "ClientSearchUsersResponseUsersTypeDef",
    "ClientSearchUsersResponseTypeDef",
    "ClientSearchUsersSortCriteriaTypeDef",
    "ClientSendAnnouncementContentAudioListTypeDef",
    "ClientSendAnnouncementContentSsmlListTypeDef",
    "ClientSendAnnouncementContentTextListTypeDef",
    "ClientSendAnnouncementContentTypeDef",
    "ClientSendAnnouncementResponseTypeDef",
    "ClientSendAnnouncementRoomFiltersTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateBusinessReportScheduleRecurrenceTypeDef",
    "ClientUpdateConferenceProviderIPDialInTypeDef",
    "ClientUpdateConferenceProviderMeetingSettingTypeDef",
    "ClientUpdateConferenceProviderPSTNDialInTypeDef",
    "ClientUpdateContactPhoneNumbersTypeDef",
    "ClientUpdateContactSipAddressesTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationTypeDef",
    "FilterTypeDef",
    "BusinessReportContentRangeTypeDef",
    "BusinessReportRecurrenceTypeDef",
    "BusinessReportS3LocationTypeDef",
    "BusinessReportTypeDef",
    "BusinessReportScheduleTypeDef",
    "ListBusinessReportSchedulesResponseTypeDef",
    "IPDialInTypeDef",
    "MeetingSettingTypeDef",
    "PSTNDialInTypeDef",
    "ConferenceProviderTypeDef",
    "ListConferenceProvidersResponseTypeDef",
    "DeviceEventTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "SkillSummaryTypeDef",
    "ListSkillsResponseTypeDef",
    "CategoryTypeDef",
    "ListSkillsStoreCategoriesResponseTypeDef",
    "DeveloperInfoTypeDef",
    "SkillDetailsTypeDef",
    "SkillsStoreSkillTypeDef",
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    "SmartHomeApplianceTypeDef",
    "ListSmartHomeAppliancesResponseTypeDef",
    "TagTypeDef",
    "ListTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "DeviceStatusDetailTypeDef",
    "DeviceStatusInfoTypeDef",
    "DeviceDataTypeDef",
    "SearchDevicesResponseTypeDef",
    "ProfileDataTypeDef",
    "SearchProfilesResponseTypeDef",
    "RoomDataTypeDef",
    "SearchRoomsResponseTypeDef",
    "SkillGroupDataTypeDef",
    "SearchSkillGroupsResponseTypeDef",
    "UserDataTypeDef",
    "SearchUsersResponseTypeDef",
    "SortTypeDef",
)

ClientCreateAddressBookResponseTypeDef = TypedDict(
    "ClientCreateAddressBookResponseTypeDef", {"AddressBookArn": str}, total=False
)

ClientCreateBusinessReportScheduleContentRangeTypeDef = TypedDict(
    "ClientCreateBusinessReportScheduleContentRangeTypeDef",
    {"Interval": Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]},
    total=False,
)

ClientCreateBusinessReportScheduleRecurrenceTypeDef = TypedDict(
    "ClientCreateBusinessReportScheduleRecurrenceTypeDef", {"StartDate": str}, total=False
)

ClientCreateBusinessReportScheduleResponseTypeDef = TypedDict(
    "ClientCreateBusinessReportScheduleResponseTypeDef", {"ScheduleArn": str}, total=False
)

_RequiredClientCreateConferenceProviderIPDialInTypeDef = TypedDict(
    "_RequiredClientCreateConferenceProviderIPDialInTypeDef", {"Endpoint": str}
)
_OptionalClientCreateConferenceProviderIPDialInTypeDef = TypedDict(
    "_OptionalClientCreateConferenceProviderIPDialInTypeDef",
    {"CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ClientCreateConferenceProviderIPDialInTypeDef(
    _RequiredClientCreateConferenceProviderIPDialInTypeDef,
    _OptionalClientCreateConferenceProviderIPDialInTypeDef,
):
    pass


ClientCreateConferenceProviderMeetingSettingTypeDef = TypedDict(
    "ClientCreateConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
)

_RequiredClientCreateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_RequiredClientCreateConferenceProviderPSTNDialInTypeDef", {"CountryCode": str}
)
_OptionalClientCreateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_OptionalClientCreateConferenceProviderPSTNDialInTypeDef",
    {"PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ClientCreateConferenceProviderPSTNDialInTypeDef(
    _RequiredClientCreateConferenceProviderPSTNDialInTypeDef,
    _OptionalClientCreateConferenceProviderPSTNDialInTypeDef,
):
    pass


ClientCreateConferenceProviderResponseTypeDef = TypedDict(
    "ClientCreateConferenceProviderResponseTypeDef", {"ConferenceProviderArn": str}, total=False
)

_RequiredClientCreateContactPhoneNumbersTypeDef = TypedDict(
    "_RequiredClientCreateContactPhoneNumbersTypeDef", {"Number": str}
)
_OptionalClientCreateContactPhoneNumbersTypeDef = TypedDict(
    "_OptionalClientCreateContactPhoneNumbersTypeDef",
    {"Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)


class ClientCreateContactPhoneNumbersTypeDef(
    _RequiredClientCreateContactPhoneNumbersTypeDef, _OptionalClientCreateContactPhoneNumbersTypeDef
):
    pass


ClientCreateContactResponseTypeDef = TypedDict(
    "ClientCreateContactResponseTypeDef", {"ContactArn": str}, total=False
)

_RequiredClientCreateContactSipAddressesTypeDef = TypedDict(
    "_RequiredClientCreateContactSipAddressesTypeDef", {"Uri": str}
)
_OptionalClientCreateContactSipAddressesTypeDef = TypedDict(
    "_OptionalClientCreateContactSipAddressesTypeDef", {"Type": str}, total=False
)


class ClientCreateContactSipAddressesTypeDef(
    _RequiredClientCreateContactSipAddressesTypeDef, _OptionalClientCreateContactSipAddressesTypeDef
):
    pass


ClientCreateGatewayGroupResponseTypeDef = TypedDict(
    "ClientCreateGatewayGroupResponseTypeDef", {"GatewayGroupArn": str}, total=False
)

ClientCreateNetworkProfileResponseTypeDef = TypedDict(
    "ClientCreateNetworkProfileResponseTypeDef", {"NetworkProfileArn": str}, total=False
)

ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef = TypedDict(
    "ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": Literal[
            "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
        ],
        "Enabled": bool,
    },
    total=False,
)

ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef = TypedDict(
    "ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    {"DurationInMinutes": int, "Enabled": bool},
    total=False,
)

ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef = TypedDict(
    "ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    {"ReleaseAfterMinutes": int, "Enabled": bool},
    total=False,
)

ClientCreateProfileMeetingRoomConfigurationTypeDef = TypedDict(
    "ClientCreateProfileMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef,
        "InstantBooking": ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef,
        "RequireCheckIn": ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef,
    },
    total=False,
)

ClientCreateProfileResponseTypeDef = TypedDict(
    "ClientCreateProfileResponseTypeDef", {"ProfileArn": str}, total=False
)

ClientCreateRoomResponseTypeDef = TypedDict(
    "ClientCreateRoomResponseTypeDef", {"RoomArn": str}, total=False
)

_RequiredClientCreateRoomTagsTypeDef = TypedDict(
    "_RequiredClientCreateRoomTagsTypeDef", {"Key": str}
)
_OptionalClientCreateRoomTagsTypeDef = TypedDict(
    "_OptionalClientCreateRoomTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateRoomTagsTypeDef(
    _RequiredClientCreateRoomTagsTypeDef, _OptionalClientCreateRoomTagsTypeDef
):
    pass


ClientCreateSkillGroupResponseTypeDef = TypedDict(
    "ClientCreateSkillGroupResponseTypeDef", {"SkillGroupArn": str}, total=False
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"UserArn": str}, total=False
)

_RequiredClientCreateUserTagsTypeDef = TypedDict(
    "_RequiredClientCreateUserTagsTypeDef", {"Key": str}
)
_OptionalClientCreateUserTagsTypeDef = TypedDict(
    "_OptionalClientCreateUserTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateUserTagsTypeDef(
    _RequiredClientCreateUserTagsTypeDef, _OptionalClientCreateUserTagsTypeDef
):
    pass


ClientGetAddressBookResponseAddressBookTypeDef = TypedDict(
    "ClientGetAddressBookResponseAddressBookTypeDef",
    {"AddressBookArn": str, "Name": str, "Description": str},
    total=False,
)

ClientGetAddressBookResponseTypeDef = TypedDict(
    "ClientGetAddressBookResponseTypeDef",
    {"AddressBook": ClientGetAddressBookResponseAddressBookTypeDef},
    total=False,
)

ClientGetConferencePreferenceResponsePreferenceTypeDef = TypedDict(
    "ClientGetConferencePreferenceResponsePreferenceTypeDef",
    {"DefaultConferenceProviderArn": str},
    total=False,
)

ClientGetConferencePreferenceResponseTypeDef = TypedDict(
    "ClientGetConferencePreferenceResponseTypeDef",
    {"Preference": ClientGetConferencePreferenceResponsePreferenceTypeDef},
    total=False,
)

ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef = TypedDict(
    "ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)

ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef = TypedDict(
    "ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
    total=False,
)

ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef = TypedDict(
    "ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)

ClientGetConferenceProviderResponseConferenceProviderTypeDef = TypedDict(
    "ClientGetConferenceProviderResponseConferenceProviderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal[
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
        "IPDialIn": ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef,
        "PSTNDialIn": ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef,
        "MeetingSetting": ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef,
    },
    total=False,
)

ClientGetConferenceProviderResponseTypeDef = TypedDict(
    "ClientGetConferenceProviderResponseTypeDef",
    {"ConferenceProvider": ClientGetConferenceProviderResponseConferenceProviderTypeDef},
    total=False,
)

ClientGetContactResponseContactPhoneNumbersTypeDef = TypedDict(
    "ClientGetContactResponseContactPhoneNumbersTypeDef",
    {"Number": str, "Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)

ClientGetContactResponseContactSipAddressesTypeDef = TypedDict(
    "ClientGetContactResponseContactSipAddressesTypeDef", {"Uri": str, "Type": str}, total=False
)

ClientGetContactResponseContactTypeDef = TypedDict(
    "ClientGetContactResponseContactTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List[ClientGetContactResponseContactPhoneNumbersTypeDef],
        "SipAddresses": List[ClientGetContactResponseContactSipAddressesTypeDef],
    },
    total=False,
)

ClientGetContactResponseTypeDef = TypedDict(
    "ClientGetContactResponseTypeDef",
    {"Contact": ClientGetContactResponseContactTypeDef},
    total=False,
)

ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {
        "Feature": Literal[
            "BLUETOOTH",
            "VOLUME",
            "NOTIFICATIONS",
            "LISTS",
            "SKILLS",
            "NETWORK_PROFILE",
            "SETTINGS",
            "ALL",
        ],
        "Code": Literal[
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "CREDENTIALS_ACCESS_FAILURE",
            "TLS_VERSION_MISMATCH",
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "DHCP_FAILURE",
            "INTERNET_UNAVAILABLE",
            "DNS_FAILURE",
            "UNKNOWN_FAILURE",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "INVALID_CERTIFICATE_AUTHORITY",
            "NETWORK_PROFILE_NOT_FOUND",
            "INVALID_PASSWORD_STATE",
            "PASSWORD_NOT_FOUND",
        ],
    },
    total=False,
)

ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef = TypedDict(
    "ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": Literal["ONLINE", "OFFLINE"],
        "ConnectionStatusUpdatedTime": datetime,
    },
    total=False,
)

ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef = TypedDict(
    "ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef",
    {"NetworkProfileArn": str, "CertificateArn": str, "CertificateExpirationTime": datetime},
    total=False,
)

ClientGetDeviceResponseDeviceTypeDef = TypedDict(
    "ClientGetDeviceResponseDeviceTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "RoomArn": str,
        "DeviceStatus": Literal["READY", "PENDING", "WAS_OFFLINE", "DEREGISTERED", "FAILED"],
        "DeviceStatusInfo": ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef,
        "NetworkProfileInfo": ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef,
    },
    total=False,
)

ClientGetDeviceResponseTypeDef = TypedDict(
    "ClientGetDeviceResponseTypeDef", {"Device": ClientGetDeviceResponseDeviceTypeDef}, total=False
)

ClientGetGatewayGroupResponseGatewayGroupTypeDef = TypedDict(
    "ClientGetGatewayGroupResponseGatewayGroupTypeDef",
    {"Arn": str, "Name": str, "Description": str},
    total=False,
)

ClientGetGatewayGroupResponseTypeDef = TypedDict(
    "ClientGetGatewayGroupResponseTypeDef",
    {"GatewayGroup": ClientGetGatewayGroupResponseGatewayGroupTypeDef},
    total=False,
)

ClientGetGatewayResponseGatewayTypeDef = TypedDict(
    "ClientGetGatewayResponseGatewayTypeDef",
    {"Arn": str, "Name": str, "Description": str, "GatewayGroupArn": str, "SoftwareVersion": str},
    total=False,
)

ClientGetGatewayResponseTypeDef = TypedDict(
    "ClientGetGatewayResponseTypeDef",
    {"Gateway": ClientGetGatewayResponseGatewayTypeDef},
    total=False,
)

ClientGetInvitationConfigurationResponseTypeDef = TypedDict(
    "ClientGetInvitationConfigurationResponseTypeDef",
    {"OrganizationName": str, "ContactEmail": str, "PrivateSkillIds": List[str]},
    total=False,
)

ClientGetNetworkProfileResponseNetworkProfileTypeDef = TypedDict(
    "ClientGetNetworkProfileResponseNetworkProfileTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": Literal["OPEN", "WEP", "WPA_PSK", "WPA2_PSK", "WPA2_ENTERPRISE"],
        "EapMethod": str,
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
    },
    total=False,
)

ClientGetNetworkProfileResponseTypeDef = TypedDict(
    "ClientGetNetworkProfileResponseTypeDef",
    {"NetworkProfile": ClientGetNetworkProfileResponseNetworkProfileTypeDef},
    total=False,
)

ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef = TypedDict(
    "ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": Literal[
            "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
        ],
        "Enabled": bool,
    },
    total=False,
)

ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef = TypedDict(
    "ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef",
    {"DurationInMinutes": int, "Enabled": bool},
    total=False,
)

ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef = TypedDict(
    "ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    {"ReleaseAfterMinutes": int, "Enabled": bool},
    total=False,
)

ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef = TypedDict(
    "ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef,
        "InstantBooking": ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef,
        "RequireCheckIn": ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef,
    },
    total=False,
)

ClientGetProfileResponseProfileTypeDef = TypedDict(
    "ClientGetProfileResponseProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": Literal["METRIC", "IMPERIAL"],
        "TemperatureUnit": Literal["FAHRENHEIT", "CELSIUS"],
        "WakeWord": Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        "Locale": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "AddressBookArn": str,
        "MeetingRoomConfiguration": ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef,
    },
    total=False,
)

ClientGetProfileResponseTypeDef = TypedDict(
    "ClientGetProfileResponseTypeDef",
    {"Profile": ClientGetProfileResponseProfileTypeDef},
    total=False,
)

ClientGetRoomResponseRoomTypeDef = TypedDict(
    "ClientGetRoomResponseRoomTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
    },
    total=False,
)

ClientGetRoomResponseTypeDef = TypedDict(
    "ClientGetRoomResponseTypeDef", {"Room": ClientGetRoomResponseRoomTypeDef}, total=False
)

ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef = TypedDict(
    "ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
    total=False,
)

ClientGetRoomSkillParameterResponseTypeDef = TypedDict(
    "ClientGetRoomSkillParameterResponseTypeDef",
    {"RoomSkillParameter": ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef},
    total=False,
)

ClientGetSkillGroupResponseSkillGroupTypeDef = TypedDict(
    "ClientGetSkillGroupResponseSkillGroupTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)

ClientGetSkillGroupResponseTypeDef = TypedDict(
    "ClientGetSkillGroupResponseTypeDef",
    {"SkillGroup": ClientGetSkillGroupResponseSkillGroupTypeDef},
    total=False,
)

ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef = TypedDict(
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef",
    {"Interval": Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]},
    total=False,
)

ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef = TypedDict(
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    {"Path": str, "BucketName": str},
    total=False,
)

ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef = TypedDict(
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    {
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED"],
        "FailureCode": Literal["ACCESS_DENIED", "NO_SUCH_BUCKET", "INTERNAL_FAILURE"],
        "S3Location": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef,
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)

ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef = TypedDict(
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)

ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef = TypedDict(
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": Literal["CSV", "CSV_ZIP"],
        "ContentRange": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef,
        "Recurrence": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef,
        "LastBusinessReport": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef,
    },
    total=False,
)

ClientListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "ClientListBusinessReportSchedulesResponseTypeDef",
    {
        "BusinessReportSchedules": List[
            ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef = TypedDict(
    "ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)

ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef = TypedDict(
    "ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
    total=False,
)

ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef = TypedDict(
    "ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)

ClientListConferenceProvidersResponseConferenceProvidersTypeDef = TypedDict(
    "ClientListConferenceProvidersResponseConferenceProvidersTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal[
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
        "IPDialIn": ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef,
        "PSTNDialIn": ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef,
        "MeetingSetting": ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef,
    },
    total=False,
)

ClientListConferenceProvidersResponseTypeDef = TypedDict(
    "ClientListConferenceProvidersResponseTypeDef",
    {
        "ConferenceProviders": List[
            ClientListConferenceProvidersResponseConferenceProvidersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDeviceEventsResponseDeviceEventsTypeDef = TypedDict(
    "ClientListDeviceEventsResponseDeviceEventsTypeDef",
    {"Type": Literal["CONNECTION_STATUS", "DEVICE_STATUS"], "Value": str, "Timestamp": datetime},
    total=False,
)

ClientListDeviceEventsResponseTypeDef = TypedDict(
    "ClientListDeviceEventsResponseTypeDef",
    {"DeviceEvents": List[ClientListDeviceEventsResponseDeviceEventsTypeDef], "NextToken": str},
    total=False,
)

ClientListGatewayGroupsResponseGatewayGroupsTypeDef = TypedDict(
    "ClientListGatewayGroupsResponseGatewayGroupsTypeDef",
    {"Arn": str, "Name": str, "Description": str},
    total=False,
)

ClientListGatewayGroupsResponseTypeDef = TypedDict(
    "ClientListGatewayGroupsResponseTypeDef",
    {"GatewayGroups": List[ClientListGatewayGroupsResponseGatewayGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListGatewaysResponseGatewaysTypeDef = TypedDict(
    "ClientListGatewaysResponseGatewaysTypeDef",
    {"Arn": str, "Name": str, "Description": str, "GatewayGroupArn": str, "SoftwareVersion": str},
    total=False,
)

ClientListGatewaysResponseTypeDef = TypedDict(
    "ClientListGatewaysResponseTypeDef",
    {"Gateways": List[ClientListGatewaysResponseGatewaysTypeDef], "NextToken": str},
    total=False,
)

ClientListSkillsResponseSkillSummariesTypeDef = TypedDict(
    "ClientListSkillsResponseSkillSummariesTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": Literal["ENABLED", "PENDING"],
        "SkillType": Literal["PUBLIC", "PRIVATE"],
    },
    total=False,
)

ClientListSkillsResponseTypeDef = TypedDict(
    "ClientListSkillsResponseTypeDef",
    {"SkillSummaries": List[ClientListSkillsResponseSkillSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListSkillsStoreCategoriesResponseCategoryListTypeDef = TypedDict(
    "ClientListSkillsStoreCategoriesResponseCategoryListTypeDef",
    {"CategoryId": int, "CategoryName": str},
    total=False,
)

ClientListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "ClientListSkillsStoreCategoriesResponseTypeDef",
    {
        "CategoryList": List[ClientListSkillsStoreCategoriesResponseCategoryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef = TypedDict(
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)

ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef = TypedDict(
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef,
    },
    total=False,
)

ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef = TypedDict(
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef,
        "SupportsLinking": bool,
    },
    total=False,
)

ClientListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "ClientListSkillsStoreSkillsByCategoryResponseTypeDef",
    {
        "SkillsStoreSkills": List[
            ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef = TypedDict(
    "ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)

ClientListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "ClientListSmartHomeAppliancesResponseTypeDef",
    {
        "SmartHomeAppliances": List[
            ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsResponseTagsTypeDef = TypedDict(
    "ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientPutConferencePreferenceConferencePreferenceTypeDef = TypedDict(
    "ClientPutConferencePreferenceConferencePreferenceTypeDef",
    {"DefaultConferenceProviderArn": str},
    total=False,
)

_RequiredClientPutRoomSkillParameterRoomSkillParameterTypeDef = TypedDict(
    "_RequiredClientPutRoomSkillParameterRoomSkillParameterTypeDef", {"ParameterKey": str}
)
_OptionalClientPutRoomSkillParameterRoomSkillParameterTypeDef = TypedDict(
    "_OptionalClientPutRoomSkillParameterRoomSkillParameterTypeDef",
    {"ParameterValue": str},
    total=False,
)


class ClientPutRoomSkillParameterRoomSkillParameterTypeDef(
    _RequiredClientPutRoomSkillParameterRoomSkillParameterTypeDef,
    _OptionalClientPutRoomSkillParameterRoomSkillParameterTypeDef,
):
    pass


ClientRegisterAvsDeviceResponseTypeDef = TypedDict(
    "ClientRegisterAvsDeviceResponseTypeDef", {"DeviceArn": str}, total=False
)

ClientResolveRoomResponseRoomSkillParametersTypeDef = TypedDict(
    "ClientResolveRoomResponseRoomSkillParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
    total=False,
)

ClientResolveRoomResponseTypeDef = TypedDict(
    "ClientResolveRoomResponseTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "RoomSkillParameters": List[ClientResolveRoomResponseRoomSkillParametersTypeDef],
    },
    total=False,
)

_RequiredClientSearchAddressBooksFiltersTypeDef = TypedDict(
    "_RequiredClientSearchAddressBooksFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchAddressBooksFiltersTypeDef = TypedDict(
    "_OptionalClientSearchAddressBooksFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchAddressBooksFiltersTypeDef(
    _RequiredClientSearchAddressBooksFiltersTypeDef, _OptionalClientSearchAddressBooksFiltersTypeDef
):
    pass


ClientSearchAddressBooksResponseAddressBooksTypeDef = TypedDict(
    "ClientSearchAddressBooksResponseAddressBooksTypeDef",
    {"AddressBookArn": str, "Name": str, "Description": str},
    total=False,
)

ClientSearchAddressBooksResponseTypeDef = TypedDict(
    "ClientSearchAddressBooksResponseTypeDef",
    {
        "AddressBooks": List[ClientSearchAddressBooksResponseAddressBooksTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

_RequiredClientSearchAddressBooksSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchAddressBooksSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchAddressBooksSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchAddressBooksSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchAddressBooksSortCriteriaTypeDef(
    _RequiredClientSearchAddressBooksSortCriteriaTypeDef,
    _OptionalClientSearchAddressBooksSortCriteriaTypeDef,
):
    pass


_RequiredClientSearchContactsFiltersTypeDef = TypedDict(
    "_RequiredClientSearchContactsFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchContactsFiltersTypeDef = TypedDict(
    "_OptionalClientSearchContactsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchContactsFiltersTypeDef(
    _RequiredClientSearchContactsFiltersTypeDef, _OptionalClientSearchContactsFiltersTypeDef
):
    pass


ClientSearchContactsResponseContactsPhoneNumbersTypeDef = TypedDict(
    "ClientSearchContactsResponseContactsPhoneNumbersTypeDef",
    {"Number": str, "Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)

ClientSearchContactsResponseContactsSipAddressesTypeDef = TypedDict(
    "ClientSearchContactsResponseContactsSipAddressesTypeDef",
    {"Uri": str, "Type": str},
    total=False,
)

ClientSearchContactsResponseContactsTypeDef = TypedDict(
    "ClientSearchContactsResponseContactsTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List[ClientSearchContactsResponseContactsPhoneNumbersTypeDef],
        "SipAddresses": List[ClientSearchContactsResponseContactsSipAddressesTypeDef],
    },
    total=False,
)

ClientSearchContactsResponseTypeDef = TypedDict(
    "ClientSearchContactsResponseTypeDef",
    {
        "Contacts": List[ClientSearchContactsResponseContactsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

_RequiredClientSearchContactsSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchContactsSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchContactsSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchContactsSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchContactsSortCriteriaTypeDef(
    _RequiredClientSearchContactsSortCriteriaTypeDef,
    _OptionalClientSearchContactsSortCriteriaTypeDef,
):
    pass


_RequiredClientSearchDevicesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchDevicesFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchDevicesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchDevicesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchDevicesFiltersTypeDef(
    _RequiredClientSearchDevicesFiltersTypeDef, _OptionalClientSearchDevicesFiltersTypeDef
):
    pass


ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {
        "Feature": Literal[
            "BLUETOOTH",
            "VOLUME",
            "NOTIFICATIONS",
            "LISTS",
            "SKILLS",
            "NETWORK_PROFILE",
            "SETTINGS",
            "ALL",
        ],
        "Code": Literal[
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "CREDENTIALS_ACCESS_FAILURE",
            "TLS_VERSION_MISMATCH",
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "DHCP_FAILURE",
            "INTERNET_UNAVAILABLE",
            "DNS_FAILURE",
            "UNKNOWN_FAILURE",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "INVALID_CERTIFICATE_AUTHORITY",
            "NETWORK_PROFILE_NOT_FOUND",
            "INVALID_PASSWORD_STATE",
            "PASSWORD_NOT_FOUND",
        ],
    },
    total=False,
)

ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef = TypedDict(
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": Literal["ONLINE", "OFFLINE"],
        "ConnectionStatusUpdatedTime": datetime,
    },
    total=False,
)

ClientSearchDevicesResponseDevicesTypeDef = TypedDict(
    "ClientSearchDevicesResponseDevicesTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": Literal["READY", "PENDING", "WAS_OFFLINE", "DEREGISTERED", "FAILED"],
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientSearchDevicesResponseTypeDef = TypedDict(
    "ClientSearchDevicesResponseTypeDef",
    {
        "Devices": List[ClientSearchDevicesResponseDevicesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

_RequiredClientSearchDevicesSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchDevicesSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchDevicesSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchDevicesSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchDevicesSortCriteriaTypeDef(
    _RequiredClientSearchDevicesSortCriteriaTypeDef, _OptionalClientSearchDevicesSortCriteriaTypeDef
):
    pass


_RequiredClientSearchNetworkProfilesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchNetworkProfilesFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchNetworkProfilesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchNetworkProfilesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchNetworkProfilesFiltersTypeDef(
    _RequiredClientSearchNetworkProfilesFiltersTypeDef,
    _OptionalClientSearchNetworkProfilesFiltersTypeDef,
):
    pass


ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef = TypedDict(
    "ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": Literal["OPEN", "WEP", "WPA_PSK", "WPA2_PSK", "WPA2_ENTERPRISE"],
        "EapMethod": str,
        "CertificateAuthorityArn": str,
    },
    total=False,
)

ClientSearchNetworkProfilesResponseTypeDef = TypedDict(
    "ClientSearchNetworkProfilesResponseTypeDef",
    {
        "NetworkProfiles": List[ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

_RequiredClientSearchNetworkProfilesSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchNetworkProfilesSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchNetworkProfilesSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchNetworkProfilesSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchNetworkProfilesSortCriteriaTypeDef(
    _RequiredClientSearchNetworkProfilesSortCriteriaTypeDef,
    _OptionalClientSearchNetworkProfilesSortCriteriaTypeDef,
):
    pass


_RequiredClientSearchProfilesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchProfilesFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchProfilesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchProfilesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchProfilesFiltersTypeDef(
    _RequiredClientSearchProfilesFiltersTypeDef, _OptionalClientSearchProfilesFiltersTypeDef
):
    pass


ClientSearchProfilesResponseProfilesTypeDef = TypedDict(
    "ClientSearchProfilesResponseProfilesTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": Literal["METRIC", "IMPERIAL"],
        "TemperatureUnit": Literal["FAHRENHEIT", "CELSIUS"],
        "WakeWord": Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        "Locale": str,
    },
    total=False,
)

ClientSearchProfilesResponseTypeDef = TypedDict(
    "ClientSearchProfilesResponseTypeDef",
    {
        "Profiles": List[ClientSearchProfilesResponseProfilesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

_RequiredClientSearchProfilesSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchProfilesSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchProfilesSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchProfilesSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchProfilesSortCriteriaTypeDef(
    _RequiredClientSearchProfilesSortCriteriaTypeDef,
    _OptionalClientSearchProfilesSortCriteriaTypeDef,
):
    pass


_RequiredClientSearchRoomsFiltersTypeDef = TypedDict(
    "_RequiredClientSearchRoomsFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchRoomsFiltersTypeDef = TypedDict(
    "_OptionalClientSearchRoomsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchRoomsFiltersTypeDef(
    _RequiredClientSearchRoomsFiltersTypeDef, _OptionalClientSearchRoomsFiltersTypeDef
):
    pass


ClientSearchRoomsResponseRoomsTypeDef = TypedDict(
    "ClientSearchRoomsResponseRoomsTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)

ClientSearchRoomsResponseTypeDef = TypedDict(
    "ClientSearchRoomsResponseTypeDef",
    {"Rooms": List[ClientSearchRoomsResponseRoomsTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

_RequiredClientSearchRoomsSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchRoomsSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchRoomsSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchRoomsSortCriteriaTypeDef", {"Value": Literal["ASC", "DESC"]}, total=False
)


class ClientSearchRoomsSortCriteriaTypeDef(
    _RequiredClientSearchRoomsSortCriteriaTypeDef, _OptionalClientSearchRoomsSortCriteriaTypeDef
):
    pass


_RequiredClientSearchSkillGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientSearchSkillGroupsFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchSkillGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientSearchSkillGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchSkillGroupsFiltersTypeDef(
    _RequiredClientSearchSkillGroupsFiltersTypeDef, _OptionalClientSearchSkillGroupsFiltersTypeDef
):
    pass


ClientSearchSkillGroupsResponseSkillGroupsTypeDef = TypedDict(
    "ClientSearchSkillGroupsResponseSkillGroupsTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)

ClientSearchSkillGroupsResponseTypeDef = TypedDict(
    "ClientSearchSkillGroupsResponseTypeDef",
    {
        "SkillGroups": List[ClientSearchSkillGroupsResponseSkillGroupsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

_RequiredClientSearchSkillGroupsSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchSkillGroupsSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchSkillGroupsSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchSkillGroupsSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchSkillGroupsSortCriteriaTypeDef(
    _RequiredClientSearchSkillGroupsSortCriteriaTypeDef,
    _OptionalClientSearchSkillGroupsSortCriteriaTypeDef,
):
    pass


_RequiredClientSearchUsersFiltersTypeDef = TypedDict(
    "_RequiredClientSearchUsersFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchUsersFiltersTypeDef = TypedDict(
    "_OptionalClientSearchUsersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchUsersFiltersTypeDef(
    _RequiredClientSearchUsersFiltersTypeDef, _OptionalClientSearchUsersFiltersTypeDef
):
    pass


ClientSearchUsersResponseUsersTypeDef = TypedDict(
    "ClientSearchUsersResponseUsersTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": Literal[
            "INITIALIZED", "PENDING", "REGISTERED", "DISASSOCIATING", "DEREGISTERING"
        ],
        "EnrollmentId": str,
    },
    total=False,
)

ClientSearchUsersResponseTypeDef = TypedDict(
    "ClientSearchUsersResponseTypeDef",
    {"Users": List[ClientSearchUsersResponseUsersTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

_RequiredClientSearchUsersSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchUsersSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchUsersSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchUsersSortCriteriaTypeDef", {"Value": Literal["ASC", "DESC"]}, total=False
)


class ClientSearchUsersSortCriteriaTypeDef(
    _RequiredClientSearchUsersSortCriteriaTypeDef, _OptionalClientSearchUsersSortCriteriaTypeDef
):
    pass


ClientSendAnnouncementContentAudioListTypeDef = TypedDict(
    "ClientSendAnnouncementContentAudioListTypeDef", {"Locale": str, "Location": str}, total=False
)

ClientSendAnnouncementContentSsmlListTypeDef = TypedDict(
    "ClientSendAnnouncementContentSsmlListTypeDef", {"Locale": str, "Value": str}, total=False
)

_RequiredClientSendAnnouncementContentTextListTypeDef = TypedDict(
    "_RequiredClientSendAnnouncementContentTextListTypeDef", {"Locale": str}
)
_OptionalClientSendAnnouncementContentTextListTypeDef = TypedDict(
    "_OptionalClientSendAnnouncementContentTextListTypeDef", {"Value": str}, total=False
)


class ClientSendAnnouncementContentTextListTypeDef(
    _RequiredClientSendAnnouncementContentTextListTypeDef,
    _OptionalClientSendAnnouncementContentTextListTypeDef,
):
    pass


ClientSendAnnouncementContentTypeDef = TypedDict(
    "ClientSendAnnouncementContentTypeDef",
    {
        "TextList": List[ClientSendAnnouncementContentTextListTypeDef],
        "SsmlList": List[ClientSendAnnouncementContentSsmlListTypeDef],
        "AudioList": List[ClientSendAnnouncementContentAudioListTypeDef],
    },
    total=False,
)

ClientSendAnnouncementResponseTypeDef = TypedDict(
    "ClientSendAnnouncementResponseTypeDef", {"AnnouncementArn": str}, total=False
)

_RequiredClientSendAnnouncementRoomFiltersTypeDef = TypedDict(
    "_RequiredClientSendAnnouncementRoomFiltersTypeDef", {"Key": str}
)
_OptionalClientSendAnnouncementRoomFiltersTypeDef = TypedDict(
    "_OptionalClientSendAnnouncementRoomFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSendAnnouncementRoomFiltersTypeDef(
    _RequiredClientSendAnnouncementRoomFiltersTypeDef,
    _OptionalClientSendAnnouncementRoomFiltersTypeDef,
):
    pass


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


ClientUpdateBusinessReportScheduleRecurrenceTypeDef = TypedDict(
    "ClientUpdateBusinessReportScheduleRecurrenceTypeDef", {"StartDate": str}, total=False
)

_RequiredClientUpdateConferenceProviderIPDialInTypeDef = TypedDict(
    "_RequiredClientUpdateConferenceProviderIPDialInTypeDef", {"Endpoint": str}
)
_OptionalClientUpdateConferenceProviderIPDialInTypeDef = TypedDict(
    "_OptionalClientUpdateConferenceProviderIPDialInTypeDef",
    {"CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ClientUpdateConferenceProviderIPDialInTypeDef(
    _RequiredClientUpdateConferenceProviderIPDialInTypeDef,
    _OptionalClientUpdateConferenceProviderIPDialInTypeDef,
):
    pass


ClientUpdateConferenceProviderMeetingSettingTypeDef = TypedDict(
    "ClientUpdateConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
)

_RequiredClientUpdateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_RequiredClientUpdateConferenceProviderPSTNDialInTypeDef", {"CountryCode": str}
)
_OptionalClientUpdateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_OptionalClientUpdateConferenceProviderPSTNDialInTypeDef",
    {"PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ClientUpdateConferenceProviderPSTNDialInTypeDef(
    _RequiredClientUpdateConferenceProviderPSTNDialInTypeDef,
    _OptionalClientUpdateConferenceProviderPSTNDialInTypeDef,
):
    pass


_RequiredClientUpdateContactPhoneNumbersTypeDef = TypedDict(
    "_RequiredClientUpdateContactPhoneNumbersTypeDef", {"Number": str}
)
_OptionalClientUpdateContactPhoneNumbersTypeDef = TypedDict(
    "_OptionalClientUpdateContactPhoneNumbersTypeDef",
    {"Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)


class ClientUpdateContactPhoneNumbersTypeDef(
    _RequiredClientUpdateContactPhoneNumbersTypeDef, _OptionalClientUpdateContactPhoneNumbersTypeDef
):
    pass


_RequiredClientUpdateContactSipAddressesTypeDef = TypedDict(
    "_RequiredClientUpdateContactSipAddressesTypeDef", {"Uri": str}
)
_OptionalClientUpdateContactSipAddressesTypeDef = TypedDict(
    "_OptionalClientUpdateContactSipAddressesTypeDef", {"Type": str}, total=False
)


class ClientUpdateContactSipAddressesTypeDef(
    _RequiredClientUpdateContactSipAddressesTypeDef, _OptionalClientUpdateContactSipAddressesTypeDef
):
    pass


ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef = TypedDict(
    "ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": Literal[
            "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
        ],
        "Enabled": bool,
    },
    total=False,
)

ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef = TypedDict(
    "ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    {"DurationInMinutes": int, "Enabled": bool},
    total=False,
)

ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef = TypedDict(
    "ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    {"ReleaseAfterMinutes": int, "Enabled": bool},
    total=False,
)

ClientUpdateProfileMeetingRoomConfigurationTypeDef = TypedDict(
    "ClientUpdateProfileMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef,
        "InstantBooking": ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef,
        "RequireCheckIn": ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef,
    },
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Key": str, "Values": List[str]})

BusinessReportContentRangeTypeDef = TypedDict(
    "BusinessReportContentRangeTypeDef",
    {"Interval": Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]},
    total=False,
)

BusinessReportRecurrenceTypeDef = TypedDict(
    "BusinessReportRecurrenceTypeDef", {"StartDate": str}, total=False
)

BusinessReportS3LocationTypeDef = TypedDict(
    "BusinessReportS3LocationTypeDef", {"Path": str, "BucketName": str}, total=False
)

BusinessReportTypeDef = TypedDict(
    "BusinessReportTypeDef",
    {
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED"],
        "FailureCode": Literal["ACCESS_DENIED", "NO_SUCH_BUCKET", "INTERNAL_FAILURE"],
        "S3Location": BusinessReportS3LocationTypeDef,
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)

BusinessReportScheduleTypeDef = TypedDict(
    "BusinessReportScheduleTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": Literal["CSV", "CSV_ZIP"],
        "ContentRange": BusinessReportContentRangeTypeDef,
        "Recurrence": BusinessReportRecurrenceTypeDef,
        "LastBusinessReport": BusinessReportTypeDef,
    },
    total=False,
)

ListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "ListBusinessReportSchedulesResponseTypeDef",
    {"BusinessReportSchedules": List[BusinessReportScheduleTypeDef], "NextToken": str},
    total=False,
)

IPDialInTypeDef = TypedDict(
    "IPDialInTypeDef", {"Endpoint": str, "CommsProtocol": Literal["SIP", "SIPS", "H323"]}
)

MeetingSettingTypeDef = TypedDict(
    "MeetingSettingTypeDef", {"RequirePin": Literal["YES", "NO", "OPTIONAL"]}
)

PSTNDialInTypeDef = TypedDict(
    "PSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
)

ConferenceProviderTypeDef = TypedDict(
    "ConferenceProviderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal[
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
        "IPDialIn": IPDialInTypeDef,
        "PSTNDialIn": PSTNDialInTypeDef,
        "MeetingSetting": MeetingSettingTypeDef,
    },
    total=False,
)

ListConferenceProvidersResponseTypeDef = TypedDict(
    "ListConferenceProvidersResponseTypeDef",
    {"ConferenceProviders": List[ConferenceProviderTypeDef], "NextToken": str},
    total=False,
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {"Type": Literal["CONNECTION_STATUS", "DEVICE_STATUS"], "Value": str, "Timestamp": datetime},
    total=False,
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {"DeviceEvents": List[DeviceEventTypeDef], "NextToken": str},
    total=False,
)

SkillSummaryTypeDef = TypedDict(
    "SkillSummaryTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": Literal["ENABLED", "PENDING"],
        "SkillType": Literal["PUBLIC", "PRIVATE"],
    },
    total=False,
)

ListSkillsResponseTypeDef = TypedDict(
    "ListSkillsResponseTypeDef",
    {"SkillSummaries": List[SkillSummaryTypeDef], "NextToken": str},
    total=False,
)

CategoryTypeDef = TypedDict(
    "CategoryTypeDef", {"CategoryId": int, "CategoryName": str}, total=False
)

ListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "ListSkillsStoreCategoriesResponseTypeDef",
    {"CategoryList": List[CategoryTypeDef], "NextToken": str},
    total=False,
)

DeveloperInfoTypeDef = TypedDict(
    "DeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)

SkillDetailsTypeDef = TypedDict(
    "SkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": DeveloperInfoTypeDef,
    },
    total=False,
)

SkillsStoreSkillTypeDef = TypedDict(
    "SkillsStoreSkillTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": SkillDetailsTypeDef,
        "SupportsLinking": bool,
    },
    total=False,
)

ListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    {"SkillsStoreSkills": List[SkillsStoreSkillTypeDef], "NextToken": str},
    total=False,
)

SmartHomeApplianceTypeDef = TypedDict(
    "SmartHomeApplianceTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)

ListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "ListSmartHomeAppliancesResponseTypeDef",
    {"SmartHomeAppliances": List[SmartHomeApplianceTypeDef], "NextToken": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

DeviceStatusDetailTypeDef = TypedDict(
    "DeviceStatusDetailTypeDef",
    {
        "Feature": Literal[
            "BLUETOOTH",
            "VOLUME",
            "NOTIFICATIONS",
            "LISTS",
            "SKILLS",
            "NETWORK_PROFILE",
            "SETTINGS",
            "ALL",
        ],
        "Code": Literal[
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "CREDENTIALS_ACCESS_FAILURE",
            "TLS_VERSION_MISMATCH",
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "DHCP_FAILURE",
            "INTERNET_UNAVAILABLE",
            "DNS_FAILURE",
            "UNKNOWN_FAILURE",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "INVALID_CERTIFICATE_AUTHORITY",
            "NETWORK_PROFILE_NOT_FOUND",
            "INVALID_PASSWORD_STATE",
            "PASSWORD_NOT_FOUND",
        ],
    },
    total=False,
)

DeviceStatusInfoTypeDef = TypedDict(
    "DeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[DeviceStatusDetailTypeDef],
        "ConnectionStatus": Literal["ONLINE", "OFFLINE"],
        "ConnectionStatusUpdatedTime": datetime,
    },
    total=False,
)

DeviceDataTypeDef = TypedDict(
    "DeviceDataTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": Literal["READY", "PENDING", "WAS_OFFLINE", "DEREGISTERED", "FAILED"],
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": DeviceStatusInfoTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)

SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {"Devices": List[DeviceDataTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

ProfileDataTypeDef = TypedDict(
    "ProfileDataTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": Literal["METRIC", "IMPERIAL"],
        "TemperatureUnit": Literal["FAHRENHEIT", "CELSIUS"],
        "WakeWord": Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        "Locale": str,
    },
    total=False,
)

SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {"Profiles": List[ProfileDataTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

RoomDataTypeDef = TypedDict(
    "RoomDataTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)

SearchRoomsResponseTypeDef = TypedDict(
    "SearchRoomsResponseTypeDef",
    {"Rooms": List[RoomDataTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

SkillGroupDataTypeDef = TypedDict(
    "SkillGroupDataTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)

SearchSkillGroupsResponseTypeDef = TypedDict(
    "SearchSkillGroupsResponseTypeDef",
    {"SkillGroups": List[SkillGroupDataTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": Literal[
            "INITIALIZED", "PENDING", "REGISTERED", "DISASSOCIATING", "DEREGISTERING"
        ],
        "EnrollmentId": str,
    },
    total=False,
)

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {"Users": List[UserDataTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)

SortTypeDef = TypedDict("SortTypeDef", {"Key": str, "Value": Literal["ASC", "DESC"]})
