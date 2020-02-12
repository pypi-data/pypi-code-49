"""
Main interface for mediastore-data service client

Usage::

    import boto3
    from mypy_boto3.mediastore_data import MediaStoreDataClient

    session = boto3.Session()

    client: MediaStoreDataClient = boto3.client("mediastore-data")
    session_client: MediaStoreDataClient = session.client("mediastore-data")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, IO, TYPE_CHECKING, Union, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mediastore_data.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mediastore_data.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_mediastore_data.type_defs import (
    ClientDescribeObjectResponseTypeDef,
    ClientGetObjectResponseTypeDef,
    ClientListItemsResponseTypeDef,
    ClientPutObjectResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaStoreDataClient",)


class MediaStoreDataClient:
    """
    [MediaStoreData.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.can_paginate)
        """

    def delete_object(self, Path: str) -> Dict[str, Any]:
        """
        [Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.delete_object)
        """

    def describe_object(self, Path: str) -> ClientDescribeObjectResponseTypeDef:
        """
        [Client.describe_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.describe_object)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.generate_presigned_url)
        """

    def get_object(self, Path: str, Range: str = None) -> ClientGetObjectResponseTypeDef:
        """
        [Client.get_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.get_object)
        """

    def list_items(
        self, Path: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListItemsResponseTypeDef:
        """
        [Client.list_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.list_items)
        """

    def put_object(
        self,
        Body: Union[bytes, IO],
        Path: str,
        ContentType: str = None,
        CacheControl: str = None,
        StorageClass: str = None,
        UploadAvailability: Literal["STANDARD", "STREAMING"] = None,
    ) -> ClientPutObjectResponseTypeDef:
        """
        [Client.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Client.put_object)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_items"]
    ) -> "paginator_scope.ListItemsPaginator":
        """
        [Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ContainerNotFoundException: Boto3ClientError
    InternalServerError: Boto3ClientError
    ObjectNotFoundException: Boto3ClientError
    RequestedRangeNotSatisfiableException: Boto3ClientError
