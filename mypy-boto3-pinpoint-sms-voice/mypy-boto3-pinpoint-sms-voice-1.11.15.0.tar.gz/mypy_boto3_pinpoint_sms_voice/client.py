"""
Main interface for pinpoint-sms-voice service client

Usage::

    import boto3
    from mypy_boto3.pinpoint_sms_voice import PinpointSMSVoiceClient

    session = boto3.Session()

    client: PinpointSMSVoiceClient = boto3.client("pinpoint-sms-voice")
    session_client: PinpointSMSVoiceClient = session.client("pinpoint-sms-voice")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_pinpoint_sms_voice.client as client_scope
else:
    client_scope = object
from mypy_boto3_pinpoint_sms_voice.type_defs import (
    ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    ClientGetConfigurationSetEventDestinationsResponseTypeDef,
    ClientSendVoiceMessageContentTypeDef,
    ClientSendVoiceMessageResponseTypeDef,
    ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
)


__all__ = ("PinpointSMSVoiceClient",)


class PinpointSMSVoiceClient:
    """
    [PinpointSMSVoice.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.can_paginate)
        """

    def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.create_configuration_set_event_destination)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.delete_configuration_set_event_destination)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.generate_presigned_url)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> ClientGetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.get_configuration_set_event_destinations)
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
        [Client.send_voice_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.send_voice_message)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.update_configuration_set_event_destination)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
