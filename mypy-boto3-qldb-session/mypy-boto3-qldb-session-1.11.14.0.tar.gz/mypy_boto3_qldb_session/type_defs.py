"""
Main interface for qldb-session service type definitions.

Usage::

    from mypy_boto3.qldb_session.type_defs import ClientSendCommandCommitTransactionTypeDef

    data: ClientSendCommandCommitTransactionTypeDef = {...}
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientSendCommandCommitTransactionTypeDef",
    "ClientSendCommandExecuteStatementParametersTypeDef",
    "ClientSendCommandExecuteStatementTypeDef",
    "ClientSendCommandFetchPageTypeDef",
    "ClientSendCommandResponseCommitTransactionTypeDef",
    "ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef",
    "ClientSendCommandResponseExecuteStatementFirstPageTypeDef",
    "ClientSendCommandResponseExecuteStatementTypeDef",
    "ClientSendCommandResponseFetchPagePageValuesTypeDef",
    "ClientSendCommandResponseFetchPagePageTypeDef",
    "ClientSendCommandResponseFetchPageTypeDef",
    "ClientSendCommandResponseStartSessionTypeDef",
    "ClientSendCommandResponseStartTransactionTypeDef",
    "ClientSendCommandResponseTypeDef",
    "ClientSendCommandStartSessionTypeDef",
)

_RequiredClientSendCommandCommitTransactionTypeDef = TypedDict(
    "_RequiredClientSendCommandCommitTransactionTypeDef", {"TransactionId": str}
)
_OptionalClientSendCommandCommitTransactionTypeDef = TypedDict(
    "_OptionalClientSendCommandCommitTransactionTypeDef", {"CommitDigest": bytes}, total=False
)


class ClientSendCommandCommitTransactionTypeDef(
    _RequiredClientSendCommandCommitTransactionTypeDef,
    _OptionalClientSendCommandCommitTransactionTypeDef,
):
    pass


ClientSendCommandExecuteStatementParametersTypeDef = TypedDict(
    "ClientSendCommandExecuteStatementParametersTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)

_RequiredClientSendCommandExecuteStatementTypeDef = TypedDict(
    "_RequiredClientSendCommandExecuteStatementTypeDef", {"TransactionId": str}
)
_OptionalClientSendCommandExecuteStatementTypeDef = TypedDict(
    "_OptionalClientSendCommandExecuteStatementTypeDef",
    {"Statement": str, "Parameters": List[ClientSendCommandExecuteStatementParametersTypeDef]},
    total=False,
)


class ClientSendCommandExecuteStatementTypeDef(
    _RequiredClientSendCommandExecuteStatementTypeDef,
    _OptionalClientSendCommandExecuteStatementTypeDef,
):
    pass


_RequiredClientSendCommandFetchPageTypeDef = TypedDict(
    "_RequiredClientSendCommandFetchPageTypeDef", {"TransactionId": str}
)
_OptionalClientSendCommandFetchPageTypeDef = TypedDict(
    "_OptionalClientSendCommandFetchPageTypeDef", {"NextPageToken": str}, total=False
)


class ClientSendCommandFetchPageTypeDef(
    _RequiredClientSendCommandFetchPageTypeDef, _OptionalClientSendCommandFetchPageTypeDef
):
    pass


ClientSendCommandResponseCommitTransactionTypeDef = TypedDict(
    "ClientSendCommandResponseCommitTransactionTypeDef",
    {"TransactionId": str, "CommitDigest": bytes},
    total=False,
)

ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef = TypedDict(
    "ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)

ClientSendCommandResponseExecuteStatementFirstPageTypeDef = TypedDict(
    "ClientSendCommandResponseExecuteStatementFirstPageTypeDef",
    {
        "Values": List[ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientSendCommandResponseExecuteStatementTypeDef = TypedDict(
    "ClientSendCommandResponseExecuteStatementTypeDef",
    {"FirstPage": ClientSendCommandResponseExecuteStatementFirstPageTypeDef},
    total=False,
)

ClientSendCommandResponseFetchPagePageValuesTypeDef = TypedDict(
    "ClientSendCommandResponseFetchPagePageValuesTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)

ClientSendCommandResponseFetchPagePageTypeDef = TypedDict(
    "ClientSendCommandResponseFetchPagePageTypeDef",
    {"Values": List[ClientSendCommandResponseFetchPagePageValuesTypeDef], "NextPageToken": str},
    total=False,
)

ClientSendCommandResponseFetchPageTypeDef = TypedDict(
    "ClientSendCommandResponseFetchPageTypeDef",
    {"Page": ClientSendCommandResponseFetchPagePageTypeDef},
    total=False,
)

ClientSendCommandResponseStartSessionTypeDef = TypedDict(
    "ClientSendCommandResponseStartSessionTypeDef", {"SessionToken": str}, total=False
)

ClientSendCommandResponseStartTransactionTypeDef = TypedDict(
    "ClientSendCommandResponseStartTransactionTypeDef", {"TransactionId": str}, total=False
)

ClientSendCommandResponseTypeDef = TypedDict(
    "ClientSendCommandResponseTypeDef",
    {
        "StartSession": ClientSendCommandResponseStartSessionTypeDef,
        "StartTransaction": ClientSendCommandResponseStartTransactionTypeDef,
        "EndSession": Dict[str, Any],
        "CommitTransaction": ClientSendCommandResponseCommitTransactionTypeDef,
        "AbortTransaction": Dict[str, Any],
        "ExecuteStatement": ClientSendCommandResponseExecuteStatementTypeDef,
        "FetchPage": ClientSendCommandResponseFetchPageTypeDef,
    },
    total=False,
)

ClientSendCommandStartSessionTypeDef = TypedDict(
    "ClientSendCommandStartSessionTypeDef", {"LedgerName": str}
)
