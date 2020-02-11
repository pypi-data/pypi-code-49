"""
Main interface for kinesis-video-media service client

Usage::

    import boto3
    from mypy_boto3.kinesis_video_media import KinesisVideoMediaClient

    session = boto3.Session()

    client: KinesisVideoMediaClient = boto3.client("kinesis-video-media")
    session_client: KinesisVideoMediaClient = session.client("kinesis-video-media")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kinesis_video_media.client as client_scope
else:
    client_scope = object
from mypy_boto3_kinesis_video_media.type_defs import (
    ClientGetMediaResponseTypeDef,
    ClientGetMediaStartSelectorTypeDef,
)


__all__ = ("KinesisVideoMediaClient",)


class KinesisVideoMediaClient:
    """
    [KinesisVideoMedia.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.generate_presigned_url)
        """

    def get_media(
        self,
        StartSelector: ClientGetMediaStartSelectorTypeDef,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> ClientGetMediaResponseTypeDef:
        """
        [Client.get_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.get_media)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    ConnectionLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidEndpointException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
