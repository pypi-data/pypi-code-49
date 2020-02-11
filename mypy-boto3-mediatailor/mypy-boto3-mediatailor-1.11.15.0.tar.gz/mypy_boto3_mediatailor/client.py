"""
Main interface for mediatailor service client

Usage::

    import boto3
    from mypy_boto3.mediatailor import MediaTailorClient

    session = boto3.Session()

    client: MediaTailorClient = boto3.client("mediatailor")
    session_client: MediaTailorClient = session.client("mediatailor")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mediatailor.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mediatailor.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_mediatailor.type_defs import (
    ClientGetPlaybackConfigurationResponseTypeDef,
    ClientListPlaybackConfigurationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutPlaybackConfigurationCdnConfigurationTypeDef,
    ClientPutPlaybackConfigurationDashConfigurationTypeDef,
    ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef,
    ClientPutPlaybackConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaTailorClient",)


class MediaTailorClient:
    """
    [MediaTailor.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.can_paginate)
        """

    def delete_playback_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.delete_playback_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.generate_presigned_url)
        """

    def get_playback_configuration(
        self, Name: str
    ) -> ClientGetPlaybackConfigurationResponseTypeDef:
        """
        [Client.get_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.get_playback_configuration)
        """

    def list_playback_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListPlaybackConfigurationsResponseTypeDef:
        """
        [Client.list_playback_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.list_playback_configurations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.list_tags_for_resource)
        """

    def put_playback_configuration(
        self,
        AdDecisionServerUrl: str = None,
        CdnConfiguration: ClientPutPlaybackConfigurationCdnConfigurationTypeDef = None,
        DashConfiguration: ClientPutPlaybackConfigurationDashConfigurationTypeDef = None,
        LivePreRollConfiguration: ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef = None,
        Name: str = None,
        SlateAdUrl: str = None,
        Tags: Dict[str, str] = None,
        TranscodeProfileName: str = None,
        VideoContentSourceUrl: str = None,
    ) -> ClientPutPlaybackConfigurationResponseTypeDef:
        """
        [Client.put_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.put_playback_configuration)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_playback_configurations"]
    ) -> "paginator_scope.ListPlaybackConfigurationsPaginator":
        """
        [Paginator.ListPlaybackConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
