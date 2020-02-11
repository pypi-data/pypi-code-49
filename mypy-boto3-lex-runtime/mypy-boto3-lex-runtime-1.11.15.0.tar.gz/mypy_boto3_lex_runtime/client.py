"""
Main interface for lex-runtime service client

Usage::

    import boto3
    from mypy_boto3.lex_runtime import LexRuntimeServiceClient

    session = boto3.Session()

    client: LexRuntimeServiceClient = boto3.client("lex-runtime")
    session_client: LexRuntimeServiceClient = session.client("lex-runtime")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, IO, List, TYPE_CHECKING, Union
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_lex_runtime.client as client_scope
else:
    client_scope = object
from mypy_boto3_lex_runtime.type_defs import (
    ClientDeleteSessionResponseTypeDef,
    ClientGetSessionResponseTypeDef,
    ClientPostContentResponseTypeDef,
    ClientPostTextResponseTypeDef,
    ClientPutSessionDialogActionTypeDef,
    ClientPutSessionRecentIntentSummaryViewTypeDef,
    ClientPutSessionResponseTypeDef,
)


__all__ = ("LexRuntimeServiceClient",)


class LexRuntimeServiceClient:
    """
    [LexRuntimeService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.can_paginate)
        """

    def delete_session(
        self, botName: str, botAlias: str, userId: str
    ) -> ClientDeleteSessionResponseTypeDef:
        """
        [Client.delete_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.delete_session)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.generate_presigned_url)
        """

    def get_session(
        self, botName: str, botAlias: str, userId: str, checkpointLabelFilter: str = None
    ) -> ClientGetSessionResponseTypeDef:
        """
        [Client.get_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.get_session)
        """

    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO],
        sessionAttributes: Union[Dict[str, Any], List[Any], int, float, str, bool, None] = None,
        requestAttributes: Union[Dict[str, Any], List[Any], int, float, str, bool, None] = None,
        accept: str = None,
    ) -> ClientPostContentResponseTypeDef:
        """
        [Client.post_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.post_content)
        """

    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, str] = None,
        requestAttributes: Dict[str, str] = None,
    ) -> ClientPostTextResponseTypeDef:
        """
        [Client.post_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.post_text)
        """

    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, str] = None,
        dialogAction: ClientPutSessionDialogActionTypeDef = None,
        recentIntentSummaryView: List[ClientPutSessionRecentIntentSummaryViewTypeDef] = None,
        accept: str = None,
    ) -> ClientPutSessionResponseTypeDef:
        """
        [Client.put_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-runtime.html#LexRuntimeService.Client.put_session)
        """


class Exceptions:
    BadGatewayException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    DependencyFailedException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LoopDetectedException: Boto3ClientError
    NotAcceptableException: Boto3ClientError
    NotFoundException: Boto3ClientError
    RequestTimeoutException: Boto3ClientError
    UnsupportedMediaTypeException: Boto3ClientError
