"""
Main interface for qldb-session service client

Usage::

    import boto3
    from mypy_boto3.qldb_session import QLDBSessionClient

    session = boto3.Session()

    client: QLDBSessionClient = boto3.client("qldb-session")
    session_client: QLDBSessionClient = session.client("qldb-session")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_qldb_session.client as client_scope
else:
    client_scope = object
from mypy_boto3_qldb_session.type_defs import (
    ClientSendCommandCommitTransactionTypeDef,
    ClientSendCommandExecuteStatementTypeDef,
    ClientSendCommandFetchPageTypeDef,
    ClientSendCommandResponseTypeDef,
    ClientSendCommandStartSessionTypeDef,
)


__all__ = ("QLDBSessionClient",)


class QLDBSessionClient:
    """
    [QLDBSession.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb-session.html#QLDBSession.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb-session.html#QLDBSession.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb-session.html#QLDBSession.Client.generate_presigned_url)
        """

    def send_command(
        self,
        SessionToken: str = None,
        StartSession: ClientSendCommandStartSessionTypeDef = None,
        StartTransaction: Dict[str, Any] = None,
        EndSession: Dict[str, Any] = None,
        CommitTransaction: ClientSendCommandCommitTransactionTypeDef = None,
        AbortTransaction: Dict[str, Any] = None,
        ExecuteStatement: ClientSendCommandExecuteStatementTypeDef = None,
        FetchPage: ClientSendCommandFetchPageTypeDef = None,
    ) -> ClientSendCommandResponseTypeDef:
        """
        [Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/qldb-session.html#QLDBSession.Client.send_command)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidSessionException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OccConflictException: Boto3ClientError
    RateExceededException: Boto3ClientError
