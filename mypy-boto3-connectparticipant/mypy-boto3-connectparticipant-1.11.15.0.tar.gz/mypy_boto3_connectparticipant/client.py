"""
Main interface for connectparticipant service client

Usage::

    import boto3
    from mypy_boto3.connectparticipant import ConnectParticipantClient

    session = boto3.Session()

    client: ConnectParticipantClient = boto3.client("connectparticipant")
    session_client: ConnectParticipantClient = session.client("connectparticipant")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_connectparticipant.client as client_scope
else:
    client_scope = object
from mypy_boto3_connectparticipant.type_defs import (
    ClientCreateParticipantConnectionResponseTypeDef,
    ClientGetTranscriptResponseTypeDef,
    ClientGetTranscriptStartPositionTypeDef,
    ClientSendEventResponseTypeDef,
    ClientSendMessageResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectParticipantClient",)


class ConnectParticipantClient:
    """
    [ConnectParticipant.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.can_paginate)
        """

    def create_participant_connection(
        self, Type: List[Literal["WEBSOCKET", "CONNECTION_CREDENTIALS"]], ParticipantToken: str
    ) -> ClientCreateParticipantConnectionResponseTypeDef:
        """
        [Client.create_participant_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.create_participant_connection)
        """

    def disconnect_participant(
        self, ConnectionToken: str, ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disconnect_participant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.disconnect_participant)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.generate_presigned_url)
        """

    def get_transcript(
        self,
        ConnectionToken: str,
        ContactId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScanDirection: Literal["FORWARD", "BACKWARD"] = None,
        SortOrder: Literal["DESCENDING", "ASCENDING"] = None,
        StartPosition: ClientGetTranscriptStartPositionTypeDef = None,
    ) -> ClientGetTranscriptResponseTypeDef:
        """
        [Client.get_transcript documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.get_transcript)
        """

    def send_event(
        self, ContentType: str, ConnectionToken: str, Content: str = None, ClientToken: str = None
    ) -> ClientSendEventResponseTypeDef:
        """
        [Client.send_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.send_event)
        """

    def send_message(
        self, ContentType: str, Content: str, ConnectionToken: str, ClientToken: str = None
    ) -> ClientSendMessageResponseTypeDef:
        """
        [Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/connectparticipant.html#ConnectParticipant.Client.send_message)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
