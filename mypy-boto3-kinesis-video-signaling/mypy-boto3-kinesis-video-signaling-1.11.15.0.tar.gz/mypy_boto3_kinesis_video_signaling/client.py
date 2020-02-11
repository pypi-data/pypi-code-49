"""
Main interface for kinesis-video-signaling service client

Usage::

    import boto3
    from mypy_boto3.kinesis_video_signaling import KinesisVideoSignalingChannelsClient

    session = boto3.Session()

    client: KinesisVideoSignalingChannelsClient = boto3.client("kinesis-video-signaling")
    session_client: KinesisVideoSignalingChannelsClient = session.client("kinesis-video-signaling")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kinesis_video_signaling.client as client_scope
else:
    client_scope = object
from mypy_boto3_kinesis_video_signaling.type_defs import (
    ClientGetIceServerConfigResponseTypeDef,
    ClientSendAlexaOfferToMasterResponseTypeDef,
)


__all__ = ("KinesisVideoSignalingChannelsClient",)


class KinesisVideoSignalingChannelsClient:
    """
    [KinesisVideoSignalingChannels.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.generate_presigned_url)
        """

    def get_ice_server_config(
        self, ChannelARN: str, ClientId: str = None, Service: str = None, Username: str = None
    ) -> ClientGetIceServerConfigResponseTypeDef:
        """
        [Client.get_ice_server_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.get_ice_server_config)
        """

    def send_alexa_offer_to_master(
        self, ChannelARN: str, SenderClientId: str, MessagePayload: str
    ) -> ClientSendAlexaOfferToMasterResponseTypeDef:
        """
        [Client.send_alexa_offer_to_master documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.send_alexa_offer_to_master)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidClientException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    SessionExpiredException: Boto3ClientError
