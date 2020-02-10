"""
Main interface for chime service type definitions.

Usage::

    from mypy_boto3.chime.type_defs import ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef

    data: ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "ClientAssociateSigninDelegateGroupsWithAccountSigninDelegateGroupsTypeDef",
    "ClientBatchCreateAttendeeAttendeesTypeDef",
    "ClientBatchCreateAttendeeResponseAttendeesTypeDef",
    "ClientBatchCreateAttendeeResponseErrorsTypeDef",
    "ClientBatchCreateAttendeeResponseTypeDef",
    "ClientBatchCreateRoomMembershipMembershipItemListTypeDef",
    "ClientBatchCreateRoomMembershipResponseErrorsTypeDef",
    "ClientBatchCreateRoomMembershipResponseTypeDef",
    "ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef",
    "ClientBatchDeletePhoneNumberResponseTypeDef",
    "ClientBatchSuspendUserResponseUserErrorsTypeDef",
    "ClientBatchSuspendUserResponseTypeDef",
    "ClientBatchUnsuspendUserResponseUserErrorsTypeDef",
    "ClientBatchUnsuspendUserResponseTypeDef",
    "ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef",
    "ClientBatchUpdatePhoneNumberResponseTypeDef",
    "ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    "ClientBatchUpdateUserResponseUserErrorsTypeDef",
    "ClientBatchUpdateUserResponseTypeDef",
    "ClientBatchUpdateUserUpdateUserRequestItemsAlexaForBusinessMetadataTypeDef",
    "ClientBatchUpdateUserUpdateUserRequestItemsTypeDef",
    "ClientCreateAccountResponseAccountSigninDelegateGroupsTypeDef",
    "ClientCreateAccountResponseAccountTypeDef",
    "ClientCreateAccountResponseTypeDef",
    "ClientCreateAttendeeResponseAttendeeTypeDef",
    "ClientCreateAttendeeResponseTypeDef",
    "ClientCreateBotResponseBotTypeDef",
    "ClientCreateBotResponseTypeDef",
    "ClientCreateMeetingNotificationsConfigurationTypeDef",
    "ClientCreateMeetingResponseMeetingMediaPlacementTypeDef",
    "ClientCreateMeetingResponseMeetingTypeDef",
    "ClientCreateMeetingResponseTypeDef",
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    "ClientCreatePhoneNumberOrderResponseTypeDef",
    "ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef",
    "ClientCreateRoomMembershipResponseRoomMembershipTypeDef",
    "ClientCreateRoomMembershipResponseTypeDef",
    "ClientCreateRoomResponseRoomTypeDef",
    "ClientCreateRoomResponseTypeDef",
    "ClientCreateUserResponseUserAlexaForBusinessMetadataTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientCreateVoiceConnectorGroupResponseTypeDef",
    "ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientCreateVoiceConnectorResponseTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "ClientGetAccountResponseAccountSigninDelegateGroupsTypeDef",
    "ClientGetAccountResponseAccountTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetAccountSettingsResponseAccountSettingsTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetAttendeeResponseAttendeeTypeDef",
    "ClientGetAttendeeResponseTypeDef",
    "ClientGetBotResponseBotTypeDef",
    "ClientGetBotResponseTypeDef",
    "ClientGetEventsConfigurationResponseEventsConfigurationTypeDef",
    "ClientGetEventsConfigurationResponseTypeDef",
    "ClientGetGlobalSettingsResponseBusinessCallingTypeDef",
    "ClientGetGlobalSettingsResponseVoiceConnectorTypeDef",
    "ClientGetGlobalSettingsResponseTypeDef",
    "ClientGetMeetingResponseMeetingMediaPlacementTypeDef",
    "ClientGetMeetingResponseMeetingTypeDef",
    "ClientGetMeetingResponseTypeDef",
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    "ClientGetPhoneNumberOrderResponseTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberTypeDef",
    "ClientGetPhoneNumberResponseTypeDef",
    "ClientGetPhoneNumberSettingsResponseTypeDef",
    "ClientGetRoomResponseRoomTypeDef",
    "ClientGetRoomResponseTypeDef",
    "ClientGetUserResponseUserAlexaForBusinessMetadataTypeDef",
    "ClientGetUserResponseUserTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef",
    "ClientGetUserSettingsResponseUserSettingsTypeDef",
    "ClientGetUserSettingsResponseTypeDef",
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientGetVoiceConnectorGroupResponseTypeDef",
    "ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    "ClientGetVoiceConnectorOriginationResponseOriginationTypeDef",
    "ClientGetVoiceConnectorOriginationResponseTypeDef",
    "ClientGetVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientGetVoiceConnectorResponseTypeDef",
    "ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    "ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef",
    "ClientGetVoiceConnectorTerminationHealthResponseTypeDef",
    "ClientGetVoiceConnectorTerminationResponseTerminationTypeDef",
    "ClientGetVoiceConnectorTerminationResponseTypeDef",
    "ClientInviteUsersResponseInvitesTypeDef",
    "ClientInviteUsersResponseTypeDef",
    "ClientListAccountsResponseAccountsSigninDelegateGroupsTypeDef",
    "ClientListAccountsResponseAccountsTypeDef",
    "ClientListAccountsResponseTypeDef",
    "ClientListAttendeesResponseAttendeesTypeDef",
    "ClientListAttendeesResponseTypeDef",
    "ClientListBotsResponseBotsTypeDef",
    "ClientListBotsResponseTypeDef",
    "ClientListMeetingsResponseMeetingsMediaPlacementTypeDef",
    "ClientListMeetingsResponseMeetingsTypeDef",
    "ClientListMeetingsResponseTypeDef",
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef",
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef",
    "ClientListPhoneNumberOrdersResponseTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersTypeDef",
    "ClientListPhoneNumbersResponseTypeDef",
    "ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef",
    "ClientListRoomMembershipsResponseRoomMembershipsTypeDef",
    "ClientListRoomMembershipsResponseTypeDef",
    "ClientListRoomsResponseRoomsTypeDef",
    "ClientListRoomsResponseTypeDef",
    "ClientListUsersResponseUsersAlexaForBusinessMetadataTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef",
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef",
    "ClientListVoiceConnectorGroupsResponseTypeDef",
    "ClientListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef",
    "ClientListVoiceConnectorsResponseTypeDef",
    "ClientPutEventsConfigurationResponseEventsConfigurationTypeDef",
    "ClientPutEventsConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef",
    "ClientPutVoiceConnectorOriginationOriginationTypeDef",
    "ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    "ClientPutVoiceConnectorOriginationResponseOriginationTypeDef",
    "ClientPutVoiceConnectorOriginationResponseTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    "ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef",
    "ClientPutVoiceConnectorTerminationResponseTerminationTypeDef",
    "ClientPutVoiceConnectorTerminationResponseTypeDef",
    "ClientPutVoiceConnectorTerminationTerminationTypeDef",
    "ClientRegenerateSecurityTokenResponseBotTypeDef",
    "ClientRegenerateSecurityTokenResponseTypeDef",
    "ClientResetPersonalPinResponseUserAlexaForBusinessMetadataTypeDef",
    "ClientResetPersonalPinResponseUserTypeDef",
    "ClientResetPersonalPinResponseTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberTypeDef",
    "ClientRestorePhoneNumberResponseTypeDef",
    "ClientSearchAvailablePhoneNumbersResponseTypeDef",
    "ClientUpdateAccountResponseAccountSigninDelegateGroupsTypeDef",
    "ClientUpdateAccountResponseAccountTypeDef",
    "ClientUpdateAccountResponseTypeDef",
    "ClientUpdateAccountSettingsAccountSettingsTypeDef",
    "ClientUpdateBotResponseBotTypeDef",
    "ClientUpdateBotResponseTypeDef",
    "ClientUpdateGlobalSettingsBusinessCallingTypeDef",
    "ClientUpdateGlobalSettingsVoiceConnectorTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberTypeDef",
    "ClientUpdatePhoneNumberResponseTypeDef",
    "ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef",
    "ClientUpdateRoomMembershipResponseRoomMembershipTypeDef",
    "ClientUpdateRoomMembershipResponseTypeDef",
    "ClientUpdateRoomResponseRoomTypeDef",
    "ClientUpdateRoomResponseTypeDef",
    "ClientUpdateUserAlexaForBusinessMetadataTypeDef",
    "ClientUpdateUserResponseUserAlexaForBusinessMetadataTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ClientUpdateUserSettingsUserSettingsTelephonyTypeDef",
    "ClientUpdateUserSettingsUserSettingsTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseTypeDef",
    "ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientUpdateVoiceConnectorResponseTypeDef",
    "SigninDelegateGroupTypeDef",
    "AccountTypeDef",
    "ListAccountsResponseTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "UserTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = TypedDict(
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)

ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef = TypedDict(
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)

ClientAssociateSigninDelegateGroupsWithAccountSigninDelegateGroupsTypeDef = TypedDict(
    "ClientAssociateSigninDelegateGroupsWithAccountSigninDelegateGroupsTypeDef",
    {"GroupName": str},
    total=False,
)

ClientBatchCreateAttendeeAttendeesTypeDef = TypedDict(
    "ClientBatchCreateAttendeeAttendeesTypeDef", {"ExternalUserId": str}
)

ClientBatchCreateAttendeeResponseAttendeesTypeDef = TypedDict(
    "ClientBatchCreateAttendeeResponseAttendeesTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)

ClientBatchCreateAttendeeResponseErrorsTypeDef = TypedDict(
    "ClientBatchCreateAttendeeResponseErrorsTypeDef",
    {"ExternalUserId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchCreateAttendeeResponseTypeDef = TypedDict(
    "ClientBatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List[ClientBatchCreateAttendeeResponseAttendeesTypeDef],
        "Errors": List[ClientBatchCreateAttendeeResponseErrorsTypeDef],
    },
    total=False,
)

ClientBatchCreateRoomMembershipMembershipItemListTypeDef = TypedDict(
    "ClientBatchCreateRoomMembershipMembershipItemListTypeDef",
    {"MemberId": str, "Role": Literal["Administrator", "Member"]},
    total=False,
)

ClientBatchCreateRoomMembershipResponseErrorsTypeDef = TypedDict(
    "ClientBatchCreateRoomMembershipResponseErrorsTypeDef",
    {
        "MemberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "ClientBatchCreateRoomMembershipResponseTypeDef",
    {"Errors": List[ClientBatchCreateRoomMembershipResponseErrorsTypeDef]},
    total=False,
)

ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef = TypedDict(
    "ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "ClientBatchDeletePhoneNumberResponseTypeDef",
    {"PhoneNumberErrors": List[ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef]},
    total=False,
)

ClientBatchSuspendUserResponseUserErrorsTypeDef = TypedDict(
    "ClientBatchSuspendUserResponseUserErrorsTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchSuspendUserResponseTypeDef = TypedDict(
    "ClientBatchSuspendUserResponseTypeDef",
    {"UserErrors": List[ClientBatchSuspendUserResponseUserErrorsTypeDef]},
    total=False,
)

ClientBatchUnsuspendUserResponseUserErrorsTypeDef = TypedDict(
    "ClientBatchUnsuspendUserResponseUserErrorsTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchUnsuspendUserResponseTypeDef = TypedDict(
    "ClientBatchUnsuspendUserResponseTypeDef",
    {"UserErrors": List[ClientBatchUnsuspendUserResponseUserErrorsTypeDef]},
    total=False,
)

ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef = TypedDict(
    "ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "ClientBatchUpdatePhoneNumberResponseTypeDef",
    {"PhoneNumberErrors": List[ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef]},
    total=False,
)

_RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef = TypedDict(
    "_RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    {"PhoneNumberId": str},
)
_OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef = TypedDict(
    "_OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    {"ProductType": Literal["BusinessCalling", "VoiceConnector"], "CallingName": str},
    total=False,
)


class ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef(
    _RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
    _OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
):
    pass


ClientBatchUpdateUserResponseUserErrorsTypeDef = TypedDict(
    "ClientBatchUpdateUserResponseUserErrorsTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchUpdateUserResponseTypeDef = TypedDict(
    "ClientBatchUpdateUserResponseTypeDef",
    {"UserErrors": List[ClientBatchUpdateUserResponseUserErrorsTypeDef]},
    total=False,
)

ClientBatchUpdateUserUpdateUserRequestItemsAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientBatchUpdateUserUpdateUserRequestItemsAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

_RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef = TypedDict(
    "_RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef", {"UserId": str}
)
_OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef = TypedDict(
    "_OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef",
    {
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "AlexaForBusinessMetadata": ClientBatchUpdateUserUpdateUserRequestItemsAlexaForBusinessMetadataTypeDef,
    },
    total=False,
)


class ClientBatchUpdateUserUpdateUserRequestItemsTypeDef(
    _RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
    _OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
):
    pass


ClientCreateAccountResponseAccountSigninDelegateGroupsTypeDef = TypedDict(
    "ClientCreateAccountResponseAccountSigninDelegateGroupsTypeDef", {"GroupName": str}, total=False
)

ClientCreateAccountResponseAccountTypeDef = TypedDict(
    "ClientCreateAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
        "SigninDelegateGroups": List[ClientCreateAccountResponseAccountSigninDelegateGroupsTypeDef],
    },
    total=False,
)

ClientCreateAccountResponseTypeDef = TypedDict(
    "ClientCreateAccountResponseTypeDef",
    {"Account": ClientCreateAccountResponseAccountTypeDef},
    total=False,
)

ClientCreateAttendeeResponseAttendeeTypeDef = TypedDict(
    "ClientCreateAttendeeResponseAttendeeTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)

ClientCreateAttendeeResponseTypeDef = TypedDict(
    "ClientCreateAttendeeResponseTypeDef",
    {"Attendee": ClientCreateAttendeeResponseAttendeeTypeDef},
    total=False,
)

ClientCreateBotResponseBotTypeDef = TypedDict(
    "ClientCreateBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

ClientCreateBotResponseTypeDef = TypedDict(
    "ClientCreateBotResponseTypeDef", {"Bot": ClientCreateBotResponseBotTypeDef}, total=False
)

ClientCreateMeetingNotificationsConfigurationTypeDef = TypedDict(
    "ClientCreateMeetingNotificationsConfigurationTypeDef",
    {"SnsTopicArn": str, "SqsQueueArn": str},
    total=False,
)

ClientCreateMeetingResponseMeetingMediaPlacementTypeDef = TypedDict(
    "ClientCreateMeetingResponseMeetingMediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)

ClientCreateMeetingResponseMeetingTypeDef = TypedDict(
    "ClientCreateMeetingResponseMeetingTypeDef",
    {
        "MeetingId": str,
        "MediaPlacement": ClientCreateMeetingResponseMeetingMediaPlacementTypeDef,
        "MediaRegion": str,
    },
    total=False,
)

ClientCreateMeetingResponseTypeDef = TypedDict(
    "ClientCreateMeetingResponseTypeDef",
    {"Meeting": ClientCreateMeetingResponseMeetingTypeDef},
    total=False,
)

ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef = TypedDict(
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)

ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef = TypedDict(
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List[
            ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientCreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "ClientCreatePhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef},
    total=False,
)

ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef = TypedDict(
    "ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)

ClientCreateRoomMembershipResponseRoomMembershipTypeDef = TypedDict(
    "ClientCreateRoomMembershipResponseRoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef,
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientCreateRoomMembershipResponseTypeDef = TypedDict(
    "ClientCreateRoomMembershipResponseTypeDef",
    {"RoomMembership": ClientCreateRoomMembershipResponseRoomMembershipTypeDef},
    total=False,
)

ClientCreateRoomResponseRoomTypeDef = TypedDict(
    "ClientCreateRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientCreateRoomResponseTypeDef = TypedDict(
    "ClientCreateRoomResponseTypeDef", {"Room": ClientCreateRoomResponseRoomTypeDef}, total=False
)

ClientCreateUserResponseUserAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientCreateUserResponseUserAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

ClientCreateUserResponseUserTypeDef = TypedDict(
    "ClientCreateUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": ClientCreateUserResponseUserAlexaForBusinessMetadataTypeDef,
        "PersonalPIN": str,
    },
    total=False,
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)

ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)

ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientCreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "ClientCreateVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef},
    total=False,
)

_RequiredClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_RequiredClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef", {"VoiceConnectorId": str}
)
_OptionalClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_OptionalClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"Priority": int},
    total=False,
)


class ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _RequiredClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    _OptionalClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
):
    pass


ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientCreateVoiceConnectorResponseTypeDef = TypedDict(
    "ClientCreateVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)

ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = TypedDict(
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)

ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef = TypedDict(
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)

ClientGetAccountResponseAccountSigninDelegateGroupsTypeDef = TypedDict(
    "ClientGetAccountResponseAccountSigninDelegateGroupsTypeDef", {"GroupName": str}, total=False
)

ClientGetAccountResponseAccountTypeDef = TypedDict(
    "ClientGetAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
        "SigninDelegateGroups": List[ClientGetAccountResponseAccountSigninDelegateGroupsTypeDef],
    },
    total=False,
)

ClientGetAccountResponseTypeDef = TypedDict(
    "ClientGetAccountResponseTypeDef",
    {"Account": ClientGetAccountResponseAccountTypeDef},
    total=False,
)

ClientGetAccountSettingsResponseAccountSettingsTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseAccountSettingsTypeDef",
    {"DisableRemoteControl": bool, "EnableDialOut": bool},
    total=False,
)

ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseTypeDef",
    {"AccountSettings": ClientGetAccountSettingsResponseAccountSettingsTypeDef},
    total=False,
)

ClientGetAttendeeResponseAttendeeTypeDef = TypedDict(
    "ClientGetAttendeeResponseAttendeeTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)

ClientGetAttendeeResponseTypeDef = TypedDict(
    "ClientGetAttendeeResponseTypeDef",
    {"Attendee": ClientGetAttendeeResponseAttendeeTypeDef},
    total=False,
)

ClientGetBotResponseBotTypeDef = TypedDict(
    "ClientGetBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

ClientGetBotResponseTypeDef = TypedDict(
    "ClientGetBotResponseTypeDef", {"Bot": ClientGetBotResponseBotTypeDef}, total=False
)

ClientGetEventsConfigurationResponseEventsConfigurationTypeDef = TypedDict(
    "ClientGetEventsConfigurationResponseEventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)

ClientGetEventsConfigurationResponseTypeDef = TypedDict(
    "ClientGetEventsConfigurationResponseTypeDef",
    {"EventsConfiguration": ClientGetEventsConfigurationResponseEventsConfigurationTypeDef},
    total=False,
)

ClientGetGlobalSettingsResponseBusinessCallingTypeDef = TypedDict(
    "ClientGetGlobalSettingsResponseBusinessCallingTypeDef", {"CdrBucket": str}, total=False
)

ClientGetGlobalSettingsResponseVoiceConnectorTypeDef = TypedDict(
    "ClientGetGlobalSettingsResponseVoiceConnectorTypeDef", {"CdrBucket": str}, total=False
)

ClientGetGlobalSettingsResponseTypeDef = TypedDict(
    "ClientGetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": ClientGetGlobalSettingsResponseBusinessCallingTypeDef,
        "VoiceConnector": ClientGetGlobalSettingsResponseVoiceConnectorTypeDef,
    },
    total=False,
)

ClientGetMeetingResponseMeetingMediaPlacementTypeDef = TypedDict(
    "ClientGetMeetingResponseMeetingMediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)

ClientGetMeetingResponseMeetingTypeDef = TypedDict(
    "ClientGetMeetingResponseMeetingTypeDef",
    {
        "MeetingId": str,
        "MediaPlacement": ClientGetMeetingResponseMeetingMediaPlacementTypeDef,
        "MediaRegion": str,
    },
    total=False,
)

ClientGetMeetingResponseTypeDef = TypedDict(
    "ClientGetMeetingResponseTypeDef",
    {"Meeting": ClientGetMeetingResponseMeetingTypeDef},
    total=False,
)

ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef = TypedDict(
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)

ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef = TypedDict(
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List[
            ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientGetPhoneNumberOrderResponseTypeDef = TypedDict(
    "ClientGetPhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef},
    total=False,
)

ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

ClientGetPhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "ClientGetPhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)

ClientGetPhoneNumberResponseTypeDef = TypedDict(
    "ClientGetPhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientGetPhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)

ClientGetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "ClientGetPhoneNumberSettingsResponseTypeDef",
    {"CallingName": str, "CallingNameUpdatedTimestamp": datetime},
    total=False,
)

ClientGetRoomResponseRoomTypeDef = TypedDict(
    "ClientGetRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientGetRoomResponseTypeDef = TypedDict(
    "ClientGetRoomResponseTypeDef", {"Room": ClientGetRoomResponseRoomTypeDef}, total=False
)

ClientGetUserResponseUserAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientGetUserResponseUserAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

ClientGetUserResponseUserTypeDef = TypedDict(
    "ClientGetUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": ClientGetUserResponseUserAlexaForBusinessMetadataTypeDef,
        "PersonalPIN": str,
    },
    total=False,
)

ClientGetUserResponseTypeDef = TypedDict(
    "ClientGetUserResponseTypeDef", {"User": ClientGetUserResponseUserTypeDef}, total=False
)

ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef = TypedDict(
    "ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef",
    {"InboundCalling": bool, "OutboundCalling": bool, "SMS": bool},
    total=False,
)

ClientGetUserSettingsResponseUserSettingsTypeDef = TypedDict(
    "ClientGetUserSettingsResponseUserSettingsTypeDef",
    {"Telephony": ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef},
    total=False,
)

ClientGetUserSettingsResponseTypeDef = TypedDict(
    "ClientGetUserSettingsResponseTypeDef",
    {"UserSettings": ClientGetUserSettingsResponseUserSettingsTypeDef},
    total=False,
)

ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)

ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientGetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef},
    total=False,
)

ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)

ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)

ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef = TypedDict(
    "ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)

ClientGetVoiceConnectorOriginationResponseOriginationTypeDef = TypedDict(
    "ClientGetVoiceConnectorOriginationResponseOriginationTypeDef",
    {
        "Routes": List[ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef],
        "Disabled": bool,
    },
    total=False,
)

ClientGetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorOriginationResponseTypeDef",
    {"Origination": ClientGetVoiceConnectorOriginationResponseOriginationTypeDef},
    total=False,
)

ClientGetVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "ClientGetVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientGetVoiceConnectorResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientGetVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)

ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef = TypedDict(
    "ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int, "Disabled": bool},
    total=False,
)

ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
    },
    total=False,
)

ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef = TypedDict(
    "ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef",
    {"Timestamp": datetime, "Source": str},
    total=False,
)

ClientGetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorTerminationHealthResponseTypeDef",
    {"TerminationHealth": ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef},
    total=False,
)

ClientGetVoiceConnectorTerminationResponseTerminationTypeDef = TypedDict(
    "ClientGetVoiceConnectorTerminationResponseTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

ClientGetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "ClientGetVoiceConnectorTerminationResponseTypeDef",
    {"Termination": ClientGetVoiceConnectorTerminationResponseTerminationTypeDef},
    total=False,
)

ClientInviteUsersResponseInvitesTypeDef = TypedDict(
    "ClientInviteUsersResponseInvitesTypeDef",
    {
        "InviteId": str,
        "Status": Literal["Pending", "Accepted", "Failed"],
        "EmailAddress": str,
        "EmailStatus": Literal["NotSent", "Sent", "Failed"],
    },
    total=False,
)

ClientInviteUsersResponseTypeDef = TypedDict(
    "ClientInviteUsersResponseTypeDef",
    {"Invites": List[ClientInviteUsersResponseInvitesTypeDef]},
    total=False,
)

ClientListAccountsResponseAccountsSigninDelegateGroupsTypeDef = TypedDict(
    "ClientListAccountsResponseAccountsSigninDelegateGroupsTypeDef", {"GroupName": str}, total=False
)

ClientListAccountsResponseAccountsTypeDef = TypedDict(
    "ClientListAccountsResponseAccountsTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
        "SigninDelegateGroups": List[ClientListAccountsResponseAccountsSigninDelegateGroupsTypeDef],
    },
    total=False,
)

ClientListAccountsResponseTypeDef = TypedDict(
    "ClientListAccountsResponseTypeDef",
    {"Accounts": List[ClientListAccountsResponseAccountsTypeDef], "NextToken": str},
    total=False,
)

ClientListAttendeesResponseAttendeesTypeDef = TypedDict(
    "ClientListAttendeesResponseAttendeesTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)

ClientListAttendeesResponseTypeDef = TypedDict(
    "ClientListAttendeesResponseTypeDef",
    {"Attendees": List[ClientListAttendeesResponseAttendeesTypeDef], "NextToken": str},
    total=False,
)

ClientListBotsResponseBotsTypeDef = TypedDict(
    "ClientListBotsResponseBotsTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

ClientListBotsResponseTypeDef = TypedDict(
    "ClientListBotsResponseTypeDef",
    {"Bots": List[ClientListBotsResponseBotsTypeDef], "NextToken": str},
    total=False,
)

ClientListMeetingsResponseMeetingsMediaPlacementTypeDef = TypedDict(
    "ClientListMeetingsResponseMeetingsMediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)

ClientListMeetingsResponseMeetingsTypeDef = TypedDict(
    "ClientListMeetingsResponseMeetingsTypeDef",
    {
        "MeetingId": str,
        "MediaPlacement": ClientListMeetingsResponseMeetingsMediaPlacementTypeDef,
        "MediaRegion": str,
    },
    total=False,
)

ClientListMeetingsResponseTypeDef = TypedDict(
    "ClientListMeetingsResponseTypeDef",
    {"Meetings": List[ClientListMeetingsResponseMeetingsTypeDef], "NextToken": str},
    total=False,
)

ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef = TypedDict(
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)

ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef = TypedDict(
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List[
            ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ClientListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List[ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef = TypedDict(
    "ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef = TypedDict(
    "ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

ClientListPhoneNumbersResponsePhoneNumbersTypeDef = TypedDict(
    "ClientListPhoneNumbersResponsePhoneNumbersTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef,
        "Associations": List[ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)

ClientListPhoneNumbersResponseTypeDef = TypedDict(
    "ClientListPhoneNumbersResponseTypeDef",
    {"PhoneNumbers": List[ClientListPhoneNumbersResponsePhoneNumbersTypeDef], "NextToken": str},
    total=False,
)

ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef = TypedDict(
    "ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)

ClientListRoomMembershipsResponseRoomMembershipsTypeDef = TypedDict(
    "ClientListRoomMembershipsResponseRoomMembershipsTypeDef",
    {
        "RoomId": str,
        "Member": ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef,
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientListRoomMembershipsResponseTypeDef = TypedDict(
    "ClientListRoomMembershipsResponseTypeDef",
    {
        "RoomMemberships": List[ClientListRoomMembershipsResponseRoomMembershipsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListRoomsResponseRoomsTypeDef = TypedDict(
    "ClientListRoomsResponseRoomsTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientListRoomsResponseTypeDef = TypedDict(
    "ClientListRoomsResponseTypeDef",
    {"Rooms": List[ClientListRoomsResponseRoomsTypeDef], "NextToken": str},
    total=False,
)

ClientListUsersResponseUsersAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientListUsersResponseUsersAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": ClientListUsersResponseUsersAlexaForBusinessMetadataTypeDef,
        "PersonalPIN": str,
    },
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)

ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef = TypedDict(
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)

ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef = TypedDict(
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ClientListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List[
            ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ClientListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {"Usernames": List[str]},
    total=False,
)

ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef = TypedDict(
    "ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientListVoiceConnectorsResponseTypeDef = TypedDict(
    "ClientListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List[ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientPutEventsConfigurationResponseEventsConfigurationTypeDef = TypedDict(
    "ClientPutEventsConfigurationResponseEventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)

ClientPutEventsConfigurationResponseTypeDef = TypedDict(
    "ClientPutEventsConfigurationResponseTypeDef",
    {"EventsConfiguration": ClientPutEventsConfigurationResponseEventsConfigurationTypeDef},
    total=False,
)

ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)

ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)

ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)

ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef = TypedDict(
    "ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)

ClientPutVoiceConnectorOriginationOriginationTypeDef = TypedDict(
    "ClientPutVoiceConnectorOriginationOriginationTypeDef",
    {"Routes": List[ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef], "Disabled": bool},
    total=False,
)

ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef = TypedDict(
    "ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)

ClientPutVoiceConnectorOriginationResponseOriginationTypeDef = TypedDict(
    "ClientPutVoiceConnectorOriginationResponseOriginationTypeDef",
    {
        "Routes": List[ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef],
        "Disabled": bool,
    },
    total=False,
)

ClientPutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "ClientPutVoiceConnectorOriginationResponseTypeDef",
    {"Origination": ClientPutVoiceConnectorOriginationResponseOriginationTypeDef},
    total=False,
)

ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef = TypedDict(
    "ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int, "Disabled": bool},
    total=False,
)

ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
    },
    total=False,
)

_RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef = TypedDict(
    "_RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int},
)
_OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef = TypedDict(
    "_OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    {"Disabled": bool},
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef(
    _RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    _OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
):
    pass


ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef = TypedDict(
    "ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)

ClientPutVoiceConnectorTerminationResponseTerminationTypeDef = TypedDict(
    "ClientPutVoiceConnectorTerminationResponseTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

ClientPutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "ClientPutVoiceConnectorTerminationResponseTypeDef",
    {"Termination": ClientPutVoiceConnectorTerminationResponseTerminationTypeDef},
    total=False,
)

ClientPutVoiceConnectorTerminationTerminationTypeDef = TypedDict(
    "ClientPutVoiceConnectorTerminationTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

ClientRegenerateSecurityTokenResponseBotTypeDef = TypedDict(
    "ClientRegenerateSecurityTokenResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

ClientRegenerateSecurityTokenResponseTypeDef = TypedDict(
    "ClientRegenerateSecurityTokenResponseTypeDef",
    {"Bot": ClientRegenerateSecurityTokenResponseBotTypeDef},
    total=False,
)

ClientResetPersonalPinResponseUserAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientResetPersonalPinResponseUserAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

ClientResetPersonalPinResponseUserTypeDef = TypedDict(
    "ClientResetPersonalPinResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": ClientResetPersonalPinResponseUserAlexaForBusinessMetadataTypeDef,
        "PersonalPIN": str,
    },
    total=False,
)

ClientResetPersonalPinResponseTypeDef = TypedDict(
    "ClientResetPersonalPinResponseTypeDef",
    {"User": ClientResetPersonalPinResponseUserTypeDef},
    total=False,
)

ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

ClientRestorePhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "ClientRestorePhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)

ClientRestorePhoneNumberResponseTypeDef = TypedDict(
    "ClientRestorePhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientRestorePhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)

ClientSearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "ClientSearchAvailablePhoneNumbersResponseTypeDef", {"E164PhoneNumbers": List[str]}, total=False
)

ClientUpdateAccountResponseAccountSigninDelegateGroupsTypeDef = TypedDict(
    "ClientUpdateAccountResponseAccountSigninDelegateGroupsTypeDef", {"GroupName": str}, total=False
)

ClientUpdateAccountResponseAccountTypeDef = TypedDict(
    "ClientUpdateAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
        "SigninDelegateGroups": List[ClientUpdateAccountResponseAccountSigninDelegateGroupsTypeDef],
    },
    total=False,
)

ClientUpdateAccountResponseTypeDef = TypedDict(
    "ClientUpdateAccountResponseTypeDef",
    {"Account": ClientUpdateAccountResponseAccountTypeDef},
    total=False,
)

ClientUpdateAccountSettingsAccountSettingsTypeDef = TypedDict(
    "ClientUpdateAccountSettingsAccountSettingsTypeDef",
    {"DisableRemoteControl": bool, "EnableDialOut": bool},
    total=False,
)

ClientUpdateBotResponseBotTypeDef = TypedDict(
    "ClientUpdateBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

ClientUpdateBotResponseTypeDef = TypedDict(
    "ClientUpdateBotResponseTypeDef", {"Bot": ClientUpdateBotResponseBotTypeDef}, total=False
)

ClientUpdateGlobalSettingsBusinessCallingTypeDef = TypedDict(
    "ClientUpdateGlobalSettingsBusinessCallingTypeDef", {"CdrBucket": str}, total=False
)

ClientUpdateGlobalSettingsVoiceConnectorTypeDef = TypedDict(
    "ClientUpdateGlobalSettingsVoiceConnectorTypeDef", {"CdrBucket": str}, total=False
)

ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

ClientUpdatePhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "ClientUpdatePhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)

ClientUpdatePhoneNumberResponseTypeDef = TypedDict(
    "ClientUpdatePhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientUpdatePhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)

ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef = TypedDict(
    "ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)

ClientUpdateRoomMembershipResponseRoomMembershipTypeDef = TypedDict(
    "ClientUpdateRoomMembershipResponseRoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef,
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientUpdateRoomMembershipResponseTypeDef = TypedDict(
    "ClientUpdateRoomMembershipResponseTypeDef",
    {"RoomMembership": ClientUpdateRoomMembershipResponseRoomMembershipTypeDef},
    total=False,
)

ClientUpdateRoomResponseRoomTypeDef = TypedDict(
    "ClientUpdateRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientUpdateRoomResponseTypeDef = TypedDict(
    "ClientUpdateRoomResponseTypeDef", {"Room": ClientUpdateRoomResponseRoomTypeDef}, total=False
)

ClientUpdateUserAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientUpdateUserAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

ClientUpdateUserResponseUserAlexaForBusinessMetadataTypeDef = TypedDict(
    "ClientUpdateUserResponseUserAlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

ClientUpdateUserResponseUserTypeDef = TypedDict(
    "ClientUpdateUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": ClientUpdateUserResponseUserAlexaForBusinessMetadataTypeDef,
        "PersonalPIN": str,
    },
    total=False,
)

ClientUpdateUserResponseTypeDef = TypedDict(
    "ClientUpdateUserResponseTypeDef", {"User": ClientUpdateUserResponseUserTypeDef}, total=False
)

_RequiredClientUpdateUserSettingsUserSettingsTelephonyTypeDef = TypedDict(
    "_RequiredClientUpdateUserSettingsUserSettingsTelephonyTypeDef", {"InboundCalling": bool}
)
_OptionalClientUpdateUserSettingsUserSettingsTelephonyTypeDef = TypedDict(
    "_OptionalClientUpdateUserSettingsUserSettingsTelephonyTypeDef",
    {"OutboundCalling": bool, "SMS": bool},
    total=False,
)


class ClientUpdateUserSettingsUserSettingsTelephonyTypeDef(
    _RequiredClientUpdateUserSettingsUserSettingsTelephonyTypeDef,
    _OptionalClientUpdateUserSettingsUserSettingsTelephonyTypeDef,
):
    pass


ClientUpdateUserSettingsUserSettingsTypeDef = TypedDict(
    "ClientUpdateUserSettingsUserSettingsTypeDef",
    {"Telephony": ClientUpdateUserSettingsUserSettingsTelephonyTypeDef},
)

ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)

ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientUpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "ClientUpdateVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef},
    total=False,
)

_RequiredClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_RequiredClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef", {"VoiceConnectorId": str}
)
_OptionalClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_OptionalClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"Priority": int},
    total=False,
)


class ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _RequiredClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    _OptionalClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
):
    pass


ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

ClientUpdateVoiceConnectorResponseTypeDef = TypedDict(
    "ClientUpdateVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)

SigninDelegateGroupTypeDef = TypedDict(
    "SigninDelegateGroupTypeDef", {"GroupName": str}, total=False
)

_RequiredAccountTypeDef = TypedDict(
    "_RequiredAccountTypeDef", {"AwsAccountId": str, "AccountId": str, "Name": str}
)
_OptionalAccountTypeDef = TypedDict(
    "_OptionalAccountTypeDef",
    {
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
        "SigninDelegateGroups": List[SigninDelegateGroupTypeDef],
    },
    total=False,
)


class AccountTypeDef(_RequiredAccountTypeDef, _OptionalAccountTypeDef):
    pass


ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef", {"Accounts": List[AccountTypeDef], "NextToken": str}, total=False
)

AlexaForBusinessMetadataTypeDef = TypedDict(
    "AlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

_RequiredUserTypeDef = TypedDict("_RequiredUserTypeDef", {"UserId": str})
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": AlexaForBusinessMetadataTypeDef,
        "PersonalPIN": str,
    },
    total=False,
)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass


ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef", {"Users": List[UserTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
