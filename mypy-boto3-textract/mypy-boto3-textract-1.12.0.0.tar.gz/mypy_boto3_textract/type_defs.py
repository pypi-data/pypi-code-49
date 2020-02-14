"""
Main interface for textract service type definitions.

Usage::

    from mypy_boto3.textract.type_defs import ClientAnalyzeDocumentDocumentS3ObjectTypeDef

    data: ClientAnalyzeDocumentDocumentS3ObjectTypeDef = {...}
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
    "ClientAnalyzeDocumentDocumentS3ObjectTypeDef",
    "ClientAnalyzeDocumentDocumentTypeDef",
    "ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef",
    "ClientAnalyzeDocumentHumanLoopConfigTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryTypeDef",
    "ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef",
    "ClientAnalyzeDocumentResponseBlocksTypeDef",
    "ClientAnalyzeDocumentResponseDocumentMetadataTypeDef",
    "ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef",
    "ClientAnalyzeDocumentResponseTypeDef",
    "ClientDetectDocumentTextDocumentS3ObjectTypeDef",
    "ClientDetectDocumentTextDocumentTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryTypeDef",
    "ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef",
    "ClientDetectDocumentTextResponseBlocksTypeDef",
    "ClientDetectDocumentTextResponseDocumentMetadataTypeDef",
    "ClientDetectDocumentTextResponseTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksTypeDef",
    "ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef",
    "ClientGetDocumentAnalysisResponseWarningsTypeDef",
    "ClientGetDocumentAnalysisResponseTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksTypeDef",
    "ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef",
    "ClientGetDocumentTextDetectionResponseWarningsTypeDef",
    "ClientGetDocumentTextDetectionResponseTypeDef",
    "ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef",
    "ClientStartDocumentAnalysisDocumentLocationTypeDef",
    "ClientStartDocumentAnalysisNotificationChannelTypeDef",
    "ClientStartDocumentAnalysisResponseTypeDef",
    "ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef",
    "ClientStartDocumentTextDetectionDocumentLocationTypeDef",
    "ClientStartDocumentTextDetectionNotificationChannelTypeDef",
    "ClientStartDocumentTextDetectionResponseTypeDef",
)

ClientAnalyzeDocumentDocumentS3ObjectTypeDef = TypedDict(
    "ClientAnalyzeDocumentDocumentS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientAnalyzeDocumentDocumentTypeDef = TypedDict(
    "ClientAnalyzeDocumentDocumentTypeDef",
    {"Bytes": bytes, "S3Object": ClientAnalyzeDocumentDocumentS3ObjectTypeDef},
    total=False,
)

ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef = TypedDict(
    "ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

_RequiredClientAnalyzeDocumentHumanLoopConfigTypeDef = TypedDict(
    "_RequiredClientAnalyzeDocumentHumanLoopConfigTypeDef", {"HumanLoopName": str}
)
_OptionalClientAnalyzeDocumentHumanLoopConfigTypeDef = TypedDict(
    "_OptionalClientAnalyzeDocumentHumanLoopConfigTypeDef",
    {
        "FlowDefinitionArn": str,
        "DataAttributes": ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef,
    },
    total=False,
)


class ClientAnalyzeDocumentHumanLoopConfigTypeDef(
    _RequiredClientAnalyzeDocumentHumanLoopConfigTypeDef,
    _OptionalClientAnalyzeDocumentHumanLoopConfigTypeDef,
):
    pass


ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef", {"X": Any, "Y": Any}, total=False
)

ClientAnalyzeDocumentResponseBlocksGeometryTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)

ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)

ClientAnalyzeDocumentResponseBlocksTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientAnalyzeDocumentResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)

ClientAnalyzeDocumentResponseDocumentMetadataTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)

ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)

ClientAnalyzeDocumentResponseTypeDef = TypedDict(
    "ClientAnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": ClientAnalyzeDocumentResponseDocumentMetadataTypeDef,
        "Blocks": List[ClientAnalyzeDocumentResponseBlocksTypeDef],
        "HumanLoopActivationOutput": ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef,
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)

ClientDetectDocumentTextDocumentS3ObjectTypeDef = TypedDict(
    "ClientDetectDocumentTextDocumentS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDetectDocumentTextDocumentTypeDef = TypedDict(
    "ClientDetectDocumentTextDocumentTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectDocumentTextDocumentS3ObjectTypeDef},
    total=False,
)

ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)

ClientDetectDocumentTextResponseBlocksGeometryTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)

ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)

ClientDetectDocumentTextResponseBlocksTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientDetectDocumentTextResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)

ClientDetectDocumentTextResponseDocumentMetadataTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)

ClientDetectDocumentTextResponseTypeDef = TypedDict(
    "ClientDetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": ClientDetectDocumentTextResponseDocumentMetadataTypeDef,
        "Blocks": List[ClientDetectDocumentTextResponseBlocksTypeDef],
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)

ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)

ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)

ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)

ClientGetDocumentAnalysisResponseBlocksTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)

ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)

ClientGetDocumentAnalysisResponseWarningsTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseWarningsTypeDef",
    {"ErrorCode": str, "Pages": List[int]},
    total=False,
)

ClientGetDocumentAnalysisResponseTypeDef = TypedDict(
    "ClientGetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef,
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED", "PARTIAL_SUCCESS"],
        "NextToken": str,
        "Blocks": List[ClientGetDocumentAnalysisResponseBlocksTypeDef],
        "Warnings": List[ClientGetDocumentAnalysisResponseWarningsTypeDef],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)

ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)

ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)

ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)

ClientGetDocumentTextDetectionResponseBlocksTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)

ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)

ClientGetDocumentTextDetectionResponseWarningsTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseWarningsTypeDef",
    {"ErrorCode": str, "Pages": List[int]},
    total=False,
)

ClientGetDocumentTextDetectionResponseTypeDef = TypedDict(
    "ClientGetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef,
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED", "PARTIAL_SUCCESS"],
        "NextToken": str,
        "Blocks": List[ClientGetDocumentTextDetectionResponseBlocksTypeDef],
        "Warnings": List[ClientGetDocumentTextDetectionResponseWarningsTypeDef],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)

ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef = TypedDict(
    "ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartDocumentAnalysisDocumentLocationTypeDef = TypedDict(
    "ClientStartDocumentAnalysisDocumentLocationTypeDef",
    {"S3Object": ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartDocumentAnalysisNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartDocumentAnalysisNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartDocumentAnalysisNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartDocumentAnalysisNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartDocumentAnalysisNotificationChannelTypeDef(
    _RequiredClientStartDocumentAnalysisNotificationChannelTypeDef,
    _OptionalClientStartDocumentAnalysisNotificationChannelTypeDef,
):
    pass


ClientStartDocumentAnalysisResponseTypeDef = TypedDict(
    "ClientStartDocumentAnalysisResponseTypeDef", {"JobId": str}, total=False
)

ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef = TypedDict(
    "ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartDocumentTextDetectionDocumentLocationTypeDef = TypedDict(
    "ClientStartDocumentTextDetectionDocumentLocationTypeDef",
    {"S3Object": ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartDocumentTextDetectionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartDocumentTextDetectionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartDocumentTextDetectionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartDocumentTextDetectionNotificationChannelTypeDef",
    {"RoleArn": str},
    total=False,
)


class ClientStartDocumentTextDetectionNotificationChannelTypeDef(
    _RequiredClientStartDocumentTextDetectionNotificationChannelTypeDef,
    _OptionalClientStartDocumentTextDetectionNotificationChannelTypeDef,
):
    pass


ClientStartDocumentTextDetectionResponseTypeDef = TypedDict(
    "ClientStartDocumentTextDetectionResponseTypeDef", {"JobId": str}, total=False
)
