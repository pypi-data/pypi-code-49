"""
Main interface for cognito-sync service client

Usage::

    import boto3
    from mypy_boto3.cognito_sync import CognitoSyncClient

    session = boto3.Session()

    client: CognitoSyncClient = boto3.client("cognito-sync")
    session_client: CognitoSyncClient = session.client("cognito-sync")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cognito_sync.client as client_scope
else:
    client_scope = object
from mypy_boto3_cognito_sync.type_defs import (
    ClientBulkPublishResponseTypeDef,
    ClientDeleteDatasetResponseTypeDef,
    ClientDescribeDatasetResponseTypeDef,
    ClientDescribeIdentityPoolUsageResponseTypeDef,
    ClientDescribeIdentityUsageResponseTypeDef,
    ClientGetBulkPublishDetailsResponseTypeDef,
    ClientGetCognitoEventsResponseTypeDef,
    ClientGetIdentityPoolConfigurationResponseTypeDef,
    ClientListDatasetsResponseTypeDef,
    ClientListIdentityPoolUsageResponseTypeDef,
    ClientListRecordsResponseTypeDef,
    ClientRegisterDeviceResponseTypeDef,
    ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef,
    ClientSetIdentityPoolConfigurationPushSyncTypeDef,
    ClientSetIdentityPoolConfigurationResponseTypeDef,
    ClientUpdateRecordsRecordPatchesTypeDef,
    ClientUpdateRecordsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CognitoSyncClient",)


class CognitoSyncClient:
    """
    [CognitoSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client)
    """

    exceptions: "client_scope.Exceptions"

    def bulk_publish(self, IdentityPoolId: str) -> ClientBulkPublishResponseTypeDef:
        """
        [Client.bulk_publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.bulk_publish)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.can_paginate)
        """

    def delete_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> ClientDeleteDatasetResponseTypeDef:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.delete_dataset)
        """

    def describe_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> ClientDescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.describe_dataset)
        """

    def describe_identity_pool_usage(
        self, IdentityPoolId: str
    ) -> ClientDescribeIdentityPoolUsageResponseTypeDef:
        """
        [Client.describe_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_pool_usage)
        """

    def describe_identity_usage(
        self, IdentityPoolId: str, IdentityId: str
    ) -> ClientDescribeIdentityUsageResponseTypeDef:
        """
        [Client.describe_identity_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_usage)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.generate_presigned_url)
        """

    def get_bulk_publish_details(
        self, IdentityPoolId: str
    ) -> ClientGetBulkPublishDetailsResponseTypeDef:
        """
        [Client.get_bulk_publish_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.get_bulk_publish_details)
        """

    def get_cognito_events(self, IdentityPoolId: str) -> ClientGetCognitoEventsResponseTypeDef:
        """
        [Client.get_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.get_cognito_events)
        """

    def get_identity_pool_configuration(
        self, IdentityPoolId: str
    ) -> ClientGetIdentityPoolConfigurationResponseTypeDef:
        """
        [Client.get_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.get_identity_pool_configuration)
        """

    def list_datasets(
        self, IdentityPoolId: str, IdentityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.list_datasets)
        """

    def list_identity_pool_usage(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListIdentityPoolUsageResponseTypeDef:
        """
        [Client.list_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.list_identity_pool_usage)
        """

    def list_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        LastSyncCount: int = None,
        NextToken: str = None,
        MaxResults: int = None,
        SyncSessionToken: str = None,
    ) -> ClientListRecordsResponseTypeDef:
        """
        [Client.list_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.list_records)
        """

    def register_device(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        Platform: Literal["APNS", "APNS_SANDBOX", "GCM", "ADM"],
        Token: str,
    ) -> ClientRegisterDeviceResponseTypeDef:
        """
        [Client.register_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.register_device)
        """

    def set_cognito_events(self, IdentityPoolId: str, Events: Dict[str, str]) -> None:
        """
        [Client.set_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.set_cognito_events)
        """

    def set_identity_pool_configuration(
        self,
        IdentityPoolId: str,
        PushSync: ClientSetIdentityPoolConfigurationPushSyncTypeDef = None,
        CognitoStreams: ClientSetIdentityPoolConfigurationCognitoStreamsTypeDef = None,
    ) -> ClientSetIdentityPoolConfigurationResponseTypeDef:
        """
        [Client.set_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.set_identity_pool_configuration)
        """

    def subscribe_to_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        [Client.subscribe_to_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.subscribe_to_dataset)
        """

    def unsubscribe_from_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        [Client.unsubscribe_from_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.unsubscribe_from_dataset)
        """

    def update_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        SyncSessionToken: str,
        DeviceId: str = None,
        RecordPatches: List[ClientUpdateRecordsRecordPatchesTypeDef] = None,
        ClientContext: str = None,
    ) -> ClientUpdateRecordsResponseTypeDef:
        """
        [Client.update_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-sync.html#CognitoSync.Client.update_records)
        """


class Exceptions:
    AlreadyStreamedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DuplicateRequestException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidConfigurationException: Boto3ClientError
    InvalidLambdaFunctionOutputException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LambdaThrottledException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
