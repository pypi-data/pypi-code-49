"""
Main interface for rds-data service type definitions.

Usage::

    from mypy_boto3.rds_data.type_defs import ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef

    data: ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef = {...}
"""
import sys
from typing import Any, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef",
    "ClientBatchExecuteStatementParameterSetsvalueTypeDef",
    "ClientBatchExecuteStatementParameterSetsTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsTypeDef",
    "ClientBatchExecuteStatementResponseTypeDef",
    "ClientBeginTransactionResponseTypeDef",
    "ClientCommitTransactionResponseTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsTypeDef",
    "ClientExecuteSqlResponseTypeDef",
    "ClientExecuteStatementParametersvaluearrayValueTypeDef",
    "ClientExecuteStatementParametersvalueTypeDef",
    "ClientExecuteStatementParametersTypeDef",
    "ClientExecuteStatementResponsecolumnMetadataTypeDef",
    "ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef",
    "ClientExecuteStatementResponsegeneratedFieldsTypeDef",
    "ClientExecuteStatementResponserecordsarrayValueTypeDef",
    "ClientExecuteStatementResponserecordsTypeDef",
    "ClientExecuteStatementResponseTypeDef",
    "ClientExecuteStatementResultSetOptionsTypeDef",
    "ClientRollbackTransactionResponseTypeDef",
)

ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef = TypedDict(
    "ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

ClientBatchExecuteStatementParameterSetsvalueTypeDef = TypedDict(
    "ClientBatchExecuteStatementParameterSetsvalueTypeDef",
    {
        "arrayValue": ClientBatchExecuteStatementParameterSetsvaluearrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

ClientBatchExecuteStatementParameterSetsTypeDef = TypedDict(
    "ClientBatchExecuteStatementParameterSetsTypeDef",
    {
        "name": str,
        "typeHint": Literal["DATE", "DECIMAL", "TIME", "TIMESTAMP"],
        "value": ClientBatchExecuteStatementParameterSetsvalueTypeDef,
    },
    total=False,
)

ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef = TypedDict(
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef = TypedDict(
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef",
    {
        "arrayValue": ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

ClientBatchExecuteStatementResponseupdateResultsTypeDef = TypedDict(
    "ClientBatchExecuteStatementResponseupdateResultsTypeDef",
    {
        "generatedFields": List[
            ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef
        ]
    },
    total=False,
)

ClientBatchExecuteStatementResponseTypeDef = TypedDict(
    "ClientBatchExecuteStatementResponseTypeDef",
    {"updateResults": List[ClientBatchExecuteStatementResponseupdateResultsTypeDef]},
    total=False,
)

ClientBeginTransactionResponseTypeDef = TypedDict(
    "ClientBeginTransactionResponseTypeDef", {"transactionId": str}, total=False
)

ClientCommitTransactionResponseTypeDef = TypedDict(
    "ClientCommitTransactionResponseTypeDef", {"transactionStatus": str}, total=False
)

ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef",
    {"attributes": List[Any]},
    total=False,
)

ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef",
    {
        "arrayValues": List[Any],
        "bigIntValue": int,
        "bitValue": bool,
        "blobValue": bytes,
        "doubleValue": float,
        "intValue": int,
        "isNull": bool,
        "realValue": Any,
        "stringValue": str,
        "structValue": ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef,
    },
    total=False,
)

ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef",
    {"values": List[ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef]},
    total=False,
)

ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)

ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef",
    {
        "columnCount": int,
        "columnMetadata": List[
            ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef
        ],
    },
    total=False,
)

ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef",
    {
        "records": List[ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef],
        "resultSetMetadata": ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef,
    },
    total=False,
)

ClientExecuteSqlResponsesqlStatementResultsTypeDef = TypedDict(
    "ClientExecuteSqlResponsesqlStatementResultsTypeDef",
    {
        "numberOfRecordsUpdated": int,
        "resultFrame": ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef,
    },
    total=False,
)

ClientExecuteSqlResponseTypeDef = TypedDict(
    "ClientExecuteSqlResponseTypeDef",
    {"sqlStatementResults": List[ClientExecuteSqlResponsesqlStatementResultsTypeDef]},
    total=False,
)

ClientExecuteStatementParametersvaluearrayValueTypeDef = TypedDict(
    "ClientExecuteStatementParametersvaluearrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

ClientExecuteStatementParametersvalueTypeDef = TypedDict(
    "ClientExecuteStatementParametersvalueTypeDef",
    {
        "arrayValue": ClientExecuteStatementParametersvaluearrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

ClientExecuteStatementParametersTypeDef = TypedDict(
    "ClientExecuteStatementParametersTypeDef",
    {
        "name": str,
        "typeHint": Literal["DATE", "DECIMAL", "TIME", "TIMESTAMP"],
        "value": ClientExecuteStatementParametersvalueTypeDef,
    },
    total=False,
)

ClientExecuteStatementResponsecolumnMetadataTypeDef = TypedDict(
    "ClientExecuteStatementResponsecolumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)

ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef = TypedDict(
    "ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

ClientExecuteStatementResponsegeneratedFieldsTypeDef = TypedDict(
    "ClientExecuteStatementResponsegeneratedFieldsTypeDef",
    {
        "arrayValue": ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

ClientExecuteStatementResponserecordsarrayValueTypeDef = TypedDict(
    "ClientExecuteStatementResponserecordsarrayValueTypeDef",
    {
        "arrayValues": List[Any],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

ClientExecuteStatementResponserecordsTypeDef = TypedDict(
    "ClientExecuteStatementResponserecordsTypeDef",
    {
        "arrayValue": ClientExecuteStatementResponserecordsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

ClientExecuteStatementResponseTypeDef = TypedDict(
    "ClientExecuteStatementResponseTypeDef",
    {
        "columnMetadata": List[ClientExecuteStatementResponsecolumnMetadataTypeDef],
        "generatedFields": List[ClientExecuteStatementResponsegeneratedFieldsTypeDef],
        "numberOfRecordsUpdated": int,
        "records": List[List[ClientExecuteStatementResponserecordsTypeDef]],
    },
    total=False,
)

ClientExecuteStatementResultSetOptionsTypeDef = TypedDict(
    "ClientExecuteStatementResultSetOptionsTypeDef",
    {"decimalReturnType": Literal["DOUBLE_OR_LONG", "STRING"]},
    total=False,
)

ClientRollbackTransactionResponseTypeDef = TypedDict(
    "ClientRollbackTransactionResponseTypeDef", {"transactionStatus": str}, total=False
)
