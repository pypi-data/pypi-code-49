"""
Main interface for chime service client

Usage::

    import boto3
    from mypy_boto3.chime import ChimeClient

    session = boto3.Session()

    client: ChimeClient = boto3.client("chime")
    session_client: ChimeClient = session.client("chime")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_chime.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_chime.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_chime.type_defs import (
    ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    ClientAssociateSigninDelegateGroupsWithAccountSigninDelegateGroupsTypeDef,
    ClientBatchCreateAttendeeAttendeesTypeDef,
    ClientBatchCreateAttendeeResponseTypeDef,
    ClientBatchCreateRoomMembershipMembershipItemListTypeDef,
    ClientBatchCreateRoomMembershipResponseTypeDef,
    ClientBatchDeletePhoneNumberResponseTypeDef,
    ClientBatchSuspendUserResponseTypeDef,
    ClientBatchUnsuspendUserResponseTypeDef,
    ClientBatchUpdatePhoneNumberResponseTypeDef,
    ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
    ClientBatchUpdateUserResponseTypeDef,
    ClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
    ClientCreateAccountResponseTypeDef,
    ClientCreateAttendeeResponseTypeDef,
    ClientCreateBotResponseTypeDef,
    ClientCreateMeetingNotificationsConfigurationTypeDef,
    ClientCreateMeetingResponseTypeDef,
    ClientCreatePhoneNumberOrderResponseTypeDef,
    ClientCreateRoomMembershipResponseTypeDef,
    ClientCreateRoomResponseTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientCreateVoiceConnectorGroupResponseTypeDef,
    ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    ClientCreateVoiceConnectorResponseTypeDef,
    ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    ClientGetAccountResponseTypeDef,
    ClientGetAccountSettingsResponseTypeDef,
    ClientGetAttendeeResponseTypeDef,
    ClientGetBotResponseTypeDef,
    ClientGetEventsConfigurationResponseTypeDef,
    ClientGetGlobalSettingsResponseTypeDef,
    ClientGetMeetingResponseTypeDef,
    ClientGetPhoneNumberOrderResponseTypeDef,
    ClientGetPhoneNumberResponseTypeDef,
    ClientGetPhoneNumberSettingsResponseTypeDef,
    ClientGetRoomResponseTypeDef,
    ClientGetUserResponseTypeDef,
    ClientGetUserSettingsResponseTypeDef,
    ClientGetVoiceConnectorGroupResponseTypeDef,
    ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef,
    ClientGetVoiceConnectorOriginationResponseTypeDef,
    ClientGetVoiceConnectorResponseTypeDef,
    ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef,
    ClientGetVoiceConnectorTerminationHealthResponseTypeDef,
    ClientGetVoiceConnectorTerminationResponseTypeDef,
    ClientInviteUsersResponseTypeDef,
    ClientListAccountsResponseTypeDef,
    ClientListAttendeesResponseTypeDef,
    ClientListBotsResponseTypeDef,
    ClientListMeetingsResponseTypeDef,
    ClientListPhoneNumberOrdersResponseTypeDef,
    ClientListPhoneNumbersResponseTypeDef,
    ClientListRoomMembershipsResponseTypeDef,
    ClientListRoomsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientListVoiceConnectorGroupsResponseTypeDef,
    ClientListVoiceConnectorTerminationCredentialsResponseTypeDef,
    ClientListVoiceConnectorsResponseTypeDef,
    ClientPutEventsConfigurationResponseTypeDef,
    ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef,
    ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef,
    ClientPutVoiceConnectorOriginationOriginationTypeDef,
    ClientPutVoiceConnectorOriginationResponseTypeDef,
    ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef,
    ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef,
    ClientPutVoiceConnectorTerminationResponseTypeDef,
    ClientPutVoiceConnectorTerminationTerminationTypeDef,
    ClientRegenerateSecurityTokenResponseTypeDef,
    ClientResetPersonalPinResponseTypeDef,
    ClientRestorePhoneNumberResponseTypeDef,
    ClientSearchAvailablePhoneNumbersResponseTypeDef,
    ClientUpdateAccountResponseTypeDef,
    ClientUpdateAccountSettingsAccountSettingsTypeDef,
    ClientUpdateBotResponseTypeDef,
    ClientUpdateGlobalSettingsBusinessCallingTypeDef,
    ClientUpdateGlobalSettingsVoiceConnectorTypeDef,
    ClientUpdatePhoneNumberResponseTypeDef,
    ClientUpdateRoomMembershipResponseTypeDef,
    ClientUpdateRoomResponseTypeDef,
    ClientUpdateUserAlexaForBusinessMetadataTypeDef,
    ClientUpdateUserResponseTypeDef,
    ClientUpdateUserSettingsUserSettingsTypeDef,
    ClientUpdateVoiceConnectorGroupResponseTypeDef,
    ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    ClientUpdateVoiceConnectorResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ChimeClient",)


class ChimeClient:
    """
    [Chime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_phone_number_with_user(
        self, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_phone_number_with_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.associate_phone_number_with_user)
        """

    def associate_phone_numbers_with_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str] = None, ForceAssociate: bool = None
    ) -> ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        [Client.associate_phone_numbers_with_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector)
        """

    def associate_phone_numbers_with_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[str] = None,
        ForceAssociate: bool = None,
    ) -> ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        [Client.associate_phone_numbers_with_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector_group)
        """

    def associate_signin_delegate_groups_with_account(
        self,
        AccountId: str,
        SigninDelegateGroups: List[
            ClientAssociateSigninDelegateGroupsWithAccountSigninDelegateGroupsTypeDef
        ],
    ) -> Dict[str, Any]:
        """
        [Client.associate_signin_delegate_groups_with_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.associate_signin_delegate_groups_with_account)
        """

    def batch_create_attendee(
        self, MeetingId: str, Attendees: List[ClientBatchCreateAttendeeAttendeesTypeDef]
    ) -> ClientBatchCreateAttendeeResponseTypeDef:
        """
        [Client.batch_create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_create_attendee)
        """

    def batch_create_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MembershipItemList: List[ClientBatchCreateRoomMembershipMembershipItemListTypeDef],
    ) -> ClientBatchCreateRoomMembershipResponseTypeDef:
        """
        [Client.batch_create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_create_room_membership)
        """

    def batch_delete_phone_number(
        self, PhoneNumberIds: List[str]
    ) -> ClientBatchDeletePhoneNumberResponseTypeDef:
        """
        [Client.batch_delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_delete_phone_number)
        """

    def batch_suspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> ClientBatchSuspendUserResponseTypeDef:
        """
        [Client.batch_suspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_suspend_user)
        """

    def batch_unsuspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> ClientBatchUnsuspendUserResponseTypeDef:
        """
        [Client.batch_unsuspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_unsuspend_user)
        """

    def batch_update_phone_number(
        self,
        UpdatePhoneNumberRequestItems: List[
            ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef
        ],
    ) -> ClientBatchUpdatePhoneNumberResponseTypeDef:
        """
        [Client.batch_update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_update_phone_number)
        """

    def batch_update_user(
        self,
        AccountId: str,
        UpdateUserRequestItems: List[ClientBatchUpdateUserUpdateUserRequestItemsTypeDef],
    ) -> ClientBatchUpdateUserResponseTypeDef:
        """
        [Client.batch_update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.batch_update_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.can_paginate)
        """

    def create_account(self, Name: str) -> ClientCreateAccountResponseTypeDef:
        """
        [Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_account)
        """

    def create_attendee(
        self, MeetingId: str, ExternalUserId: str
    ) -> ClientCreateAttendeeResponseTypeDef:
        """
        [Client.create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_attendee)
        """

    def create_bot(
        self, AccountId: str, DisplayName: str, Domain: str = None
    ) -> ClientCreateBotResponseTypeDef:
        """
        [Client.create_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_bot)
        """

    def create_meeting(
        self,
        ClientRequestToken: str,
        MeetingHostId: str = None,
        MediaRegion: str = None,
        NotificationsConfiguration: ClientCreateMeetingNotificationsConfigurationTypeDef = None,
    ) -> ClientCreateMeetingResponseTypeDef:
        """
        [Client.create_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_meeting)
        """

    def create_phone_number_order(
        self, ProductType: Literal["BusinessCalling", "VoiceConnector"], E164PhoneNumbers: List[str]
    ) -> ClientCreatePhoneNumberOrderResponseTypeDef:
        """
        [Client.create_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_phone_number_order)
        """

    def create_room(
        self, AccountId: str, Name: str, ClientRequestToken: str = None
    ) -> ClientCreateRoomResponseTypeDef:
        """
        [Client.create_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_room)
        """

    def create_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MemberId: str,
        Role: Literal["Administrator", "Member"] = None,
    ) -> ClientCreateRoomMembershipResponseTypeDef:
        """
        [Client.create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_room_membership)
        """

    def create_user(
        self,
        AccountId: str,
        Username: str = None,
        Email: str = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
    ) -> ClientCreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_user)
        """

    def create_voice_connector(
        self,
        Name: str,
        RequireEncryption: bool,
        AwsRegion: Literal["us-east-1", "us-west-2"] = None,
    ) -> ClientCreateVoiceConnectorResponseTypeDef:
        """
        [Client.create_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_voice_connector)
        """

    def create_voice_connector_group(
        self,
        Name: str,
        VoiceConnectorItems: List[ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef] = None,
    ) -> ClientCreateVoiceConnectorGroupResponseTypeDef:
        """
        [Client.create_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.create_voice_connector_group)
        """

    def delete_account(self, AccountId: str) -> Dict[str, Any]:
        """
        [Client.delete_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_account)
        """

    def delete_attendee(self, MeetingId: str, AttendeeId: str) -> None:
        """
        [Client.delete_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_attendee)
        """

    def delete_events_configuration(self, AccountId: str, BotId: str) -> None:
        """
        [Client.delete_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_events_configuration)
        """

    def delete_meeting(self, MeetingId: str) -> None:
        """
        [Client.delete_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_meeting)
        """

    def delete_phone_number(self, PhoneNumberId: str) -> None:
        """
        [Client.delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_phone_number)
        """

    def delete_room(self, AccountId: str, RoomId: str) -> None:
        """
        [Client.delete_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_room)
        """

    def delete_room_membership(self, AccountId: str, RoomId: str, MemberId: str) -> None:
        """
        [Client.delete_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_room_membership)
        """

    def delete_voice_connector(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_voice_connector)
        """

    def delete_voice_connector_group(self, VoiceConnectorGroupId: str) -> None:
        """
        [Client.delete_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_voice_connector_group)
        """

    def delete_voice_connector_origination(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_voice_connector_origination)
        """

    def delete_voice_connector_streaming_configuration(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_voice_connector_streaming_configuration)
        """

    def delete_voice_connector_termination(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_voice_connector_termination)
        """

    def delete_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Usernames: List[str] = None
    ) -> None:
        """
        [Client.delete_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.delete_voice_connector_termination_credentials)
        """

    def disassociate_phone_number_from_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_phone_number_from_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.disassociate_phone_number_from_user)
        """

    def disassociate_phone_numbers_from_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str] = None
    ) -> ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        [Client.disassociate_phone_numbers_from_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector)
        """

    def disassociate_phone_numbers_from_voice_connector_group(
        self, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str] = None
    ) -> ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        [Client.disassociate_phone_numbers_from_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector_group)
        """

    def disassociate_signin_delegate_groups_from_account(
        self, AccountId: str, GroupNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_signin_delegate_groups_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.disassociate_signin_delegate_groups_from_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.generate_presigned_url)
        """

    def get_account(self, AccountId: str) -> ClientGetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_account)
        """

    def get_account_settings(self, AccountId: str) -> ClientGetAccountSettingsResponseTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_account_settings)
        """

    def get_attendee(self, MeetingId: str, AttendeeId: str) -> ClientGetAttendeeResponseTypeDef:
        """
        [Client.get_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_attendee)
        """

    def get_bot(self, AccountId: str, BotId: str) -> ClientGetBotResponseTypeDef:
        """
        [Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_bot)
        """

    def get_events_configuration(
        self, AccountId: str, BotId: str
    ) -> ClientGetEventsConfigurationResponseTypeDef:
        """
        [Client.get_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_events_configuration)
        """

    def get_global_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetGlobalSettingsResponseTypeDef:
        """
        [Client.get_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_global_settings)
        """

    def get_meeting(self, MeetingId: str) -> ClientGetMeetingResponseTypeDef:
        """
        [Client.get_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_meeting)
        """

    def get_phone_number(self, PhoneNumberId: str) -> ClientGetPhoneNumberResponseTypeDef:
        """
        [Client.get_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_phone_number)
        """

    def get_phone_number_order(
        self, PhoneNumberOrderId: str
    ) -> ClientGetPhoneNumberOrderResponseTypeDef:
        """
        [Client.get_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_phone_number_order)
        """

    def get_phone_number_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetPhoneNumberSettingsResponseTypeDef:
        """
        [Client.get_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_phone_number_settings)
        """

    def get_room(self, AccountId: str, RoomId: str) -> ClientGetRoomResponseTypeDef:
        """
        [Client.get_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_room)
        """

    def get_user(self, AccountId: str, UserId: str) -> ClientGetUserResponseTypeDef:
        """
        [Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_user)
        """

    def get_user_settings(
        self, AccountId: str, UserId: str
    ) -> ClientGetUserSettingsResponseTypeDef:
        """
        [Client.get_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_user_settings)
        """

    def get_voice_connector(self, VoiceConnectorId: str) -> ClientGetVoiceConnectorResponseTypeDef:
        """
        [Client.get_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector)
        """

    def get_voice_connector_group(
        self, VoiceConnectorGroupId: str
    ) -> ClientGetVoiceConnectorGroupResponseTypeDef:
        """
        [Client.get_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector_group)
        """

    def get_voice_connector_logging_configuration(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector_logging_configuration)
        """

    def get_voice_connector_origination(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorOriginationResponseTypeDef:
        """
        [Client.get_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector_origination)
        """

    def get_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector_streaming_configuration)
        """

    def get_voice_connector_termination(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorTerminationResponseTypeDef:
        """
        [Client.get_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector_termination)
        """

    def get_voice_connector_termination_health(
        self, VoiceConnectorId: str
    ) -> ClientGetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        [Client.get_voice_connector_termination_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.get_voice_connector_termination_health)
        """

    def invite_users(
        self,
        AccountId: str,
        UserEmailList: List[str],
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
    ) -> ClientInviteUsersResponseTypeDef:
        """
        [Client.invite_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.invite_users)
        """

    def list_accounts(
        self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_accounts)
        """

    def list_attendees(
        self, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAttendeesResponseTypeDef:
        """
        [Client.list_attendees documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_attendees)
        """

    def list_bots(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListBotsResponseTypeDef:
        """
        [Client.list_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_bots)
        """

    def list_meetings(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListMeetingsResponseTypeDef:
        """
        [Client.list_meetings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_meetings)
        """

    def list_phone_number_orders(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListPhoneNumberOrdersResponseTypeDef:
        """
        [Client.list_phone_number_orders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_phone_number_orders)
        """

    def list_phone_numbers(
        self,
        Status: Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ] = None,
        ProductType: Literal["BusinessCalling", "VoiceConnector"] = None,
        FilterName: Literal[
            "AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"
        ] = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListPhoneNumbersResponseTypeDef:
        """
        [Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_phone_numbers)
        """

    def list_room_memberships(
        self, AccountId: str, RoomId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListRoomMembershipsResponseTypeDef:
        """
        [Client.list_room_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_room_memberships)
        """

    def list_rooms(
        self, AccountId: str, MemberId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListRoomsResponseTypeDef:
        """
        [Client.list_rooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_rooms)
        """

    def list_users(
        self,
        AccountId: str,
        UserEmail: str = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_users)
        """

    def list_voice_connector_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListVoiceConnectorGroupsResponseTypeDef:
        """
        [Client.list_voice_connector_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_voice_connector_groups)
        """

    def list_voice_connector_termination_credentials(
        self, VoiceConnectorId: str
    ) -> ClientListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        [Client.list_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_voice_connector_termination_credentials)
        """

    def list_voice_connectors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListVoiceConnectorsResponseTypeDef:
        """
        [Client.list_voice_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.list_voice_connectors)
        """

    def logout_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.logout_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.logout_user)
        """

    def put_events_configuration(
        self,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None,
    ) -> ClientPutEventsConfigurationResponseTypeDef:
        """
        [Client.put_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.put_events_configuration)
        """

    def put_voice_connector_logging_configuration(
        self,
        VoiceConnectorId: str,
        LoggingConfiguration: ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef,
    ) -> ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.put_voice_connector_logging_configuration)
        """

    def put_voice_connector_origination(
        self,
        VoiceConnectorId: str,
        Origination: ClientPutVoiceConnectorOriginationOriginationTypeDef,
    ) -> ClientPutVoiceConnectorOriginationResponseTypeDef:
        """
        [Client.put_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.put_voice_connector_origination)
        """

    def put_voice_connector_streaming_configuration(
        self,
        VoiceConnectorId: str,
        StreamingConfiguration: ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    ) -> ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.put_voice_connector_streaming_configuration)
        """

    def put_voice_connector_termination(
        self,
        VoiceConnectorId: str,
        Termination: ClientPutVoiceConnectorTerminationTerminationTypeDef,
    ) -> ClientPutVoiceConnectorTerminationResponseTypeDef:
        """
        [Client.put_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.put_voice_connector_termination)
        """

    def put_voice_connector_termination_credentials(
        self,
        VoiceConnectorId: str,
        Credentials: List[ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef] = None,
    ) -> None:
        """
        [Client.put_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.put_voice_connector_termination_credentials)
        """

    def regenerate_security_token(
        self, AccountId: str, BotId: str
    ) -> ClientRegenerateSecurityTokenResponseTypeDef:
        """
        [Client.regenerate_security_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.regenerate_security_token)
        """

    def reset_personal_pin(
        self, AccountId: str, UserId: str
    ) -> ClientResetPersonalPinResponseTypeDef:
        """
        [Client.reset_personal_pin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.reset_personal_pin)
        """

    def restore_phone_number(self, PhoneNumberId: str) -> ClientRestorePhoneNumberResponseTypeDef:
        """
        [Client.restore_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.restore_phone_number)
        """

    def search_available_phone_numbers(
        self,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientSearchAvailablePhoneNumbersResponseTypeDef:
        """
        [Client.search_available_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.search_available_phone_numbers)
        """

    def update_account(
        self, AccountId: str, Name: str = None
    ) -> ClientUpdateAccountResponseTypeDef:
        """
        [Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_account)
        """

    def update_account_settings(
        self, AccountId: str, AccountSettings: ClientUpdateAccountSettingsAccountSettingsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_account_settings)
        """

    def update_bot(
        self, AccountId: str, BotId: str, Disabled: bool = None
    ) -> ClientUpdateBotResponseTypeDef:
        """
        [Client.update_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_bot)
        """

    def update_global_settings(
        self,
        BusinessCalling: ClientUpdateGlobalSettingsBusinessCallingTypeDef,
        VoiceConnector: ClientUpdateGlobalSettingsVoiceConnectorTypeDef,
    ) -> None:
        """
        [Client.update_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_global_settings)
        """

    def update_phone_number(
        self,
        PhoneNumberId: str,
        ProductType: Literal["BusinessCalling", "VoiceConnector"] = None,
        CallingName: str = None,
    ) -> ClientUpdatePhoneNumberResponseTypeDef:
        """
        [Client.update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_phone_number)
        """

    def update_phone_number_settings(self, CallingName: str) -> None:
        """
        [Client.update_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_phone_number_settings)
        """

    def update_room(
        self, AccountId: str, RoomId: str, Name: str = None
    ) -> ClientUpdateRoomResponseTypeDef:
        """
        [Client.update_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_room)
        """

    def update_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MemberId: str,
        Role: Literal["Administrator", "Member"] = None,
    ) -> ClientUpdateRoomMembershipResponseTypeDef:
        """
        [Client.update_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_room_membership)
        """

    def update_user(
        self,
        AccountId: str,
        UserId: str,
        LicenseType: Literal["Basic", "Plus", "Pro", "ProTrial"] = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
        AlexaForBusinessMetadata: ClientUpdateUserAlexaForBusinessMetadataTypeDef = None,
    ) -> ClientUpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_user)
        """

    def update_user_settings(
        self, AccountId: str, UserId: str, UserSettings: ClientUpdateUserSettingsUserSettingsTypeDef
    ) -> None:
        """
        [Client.update_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_user_settings)
        """

    def update_voice_connector(
        self, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> ClientUpdateVoiceConnectorResponseTypeDef:
        """
        [Client.update_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_voice_connector)
        """

    def update_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List[ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef],
    ) -> ClientUpdateVoiceConnectorGroupResponseTypeDef:
        """
        [Client.update_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Client.update_voice_connector_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> "paginator_scope.ListAccountsPaginator":
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Paginator.ListAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> "paginator_scope.ListUsersPaginator":
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Paginator.ListUsers)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottledClientException: Boto3ClientError
    UnauthorizedClientException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError
