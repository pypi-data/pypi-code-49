"""
Main interface for sms-voice service client

Usage::

    import boto3
    from mypy_boto3.sms_voice import SMSVoiceClient

    session = boto3.Session()

    client: SMSVoiceClient = boto3.client("sms-voice")
    session_client: SMSVoiceClient = session.client("sms-voice")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sms_voice.client as client_scope
else:
    client_scope = object
from mypy_boto3_sms_voice.type_defs import (
    ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    ClientGetConfigurationSetEventDestinationsResponseTypeDef,
    ClientListConfigurationSetsResponseTypeDef,
    ClientSendVoiceMessageContentTypeDef,
    ClientSendVoiceMessageResponseTypeDef,
    ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
)


__all__ = ("SMSVoiceClient",)


class SMSVoiceClient:
    """
    [SMSVoice.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.can_paginate)
        """

    def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set_event_destination)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set_event_destination)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.generate_presigned_url)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> ClientGetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.get_configuration_set_event_destinations)
        """

    def list_configuration_sets(
        self, NextToken: str = None, PageSize: str = None
    ) -> ClientListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.list_configuration_sets)
        """

    def send_voice_message(
        self,
        CallerId: str = None,
        ConfigurationSetName: str = None,
        Content: ClientSendVoiceMessageContentTypeDef = None,
        DestinationPhoneNumber: str = None,
        OriginationPhoneNumber: str = None,
    ) -> ClientSendVoiceMessageResponseTypeDef:
        """
        [Client.send_voice_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.send_voice_message)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms-voice.html#SMSVoice.Client.update_configuration_set_event_destination)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
