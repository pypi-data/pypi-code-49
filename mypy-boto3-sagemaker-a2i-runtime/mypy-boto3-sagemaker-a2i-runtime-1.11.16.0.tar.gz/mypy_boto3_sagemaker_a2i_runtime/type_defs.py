"""
Main interface for sagemaker-a2i-runtime service type definitions.

Usage::

    from mypy_boto3.sagemaker_a2i_runtime.type_defs import ClientDescribeHumanLoopResponseHumanLoopInputTypeDef

    data: ClientDescribeHumanLoopResponseHumanLoopInputTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeHumanLoopResponseHumanLoopInputTypeDef",
    "ClientDescribeHumanLoopResponseHumanLoopOutputTypeDef",
    "ClientDescribeHumanLoopResponseTypeDef",
    "ClientListHumanLoopsResponseHumanLoopSummariesTypeDef",
    "ClientListHumanLoopsResponseTypeDef",
    "ClientStartHumanLoopDataAttributesTypeDef",
    "ClientStartHumanLoopHumanLoopInputTypeDef",
    "ClientStartHumanLoopResponseHumanLoopActivationResultsHumanLoopActivationReasonTypeDef",
    "ClientStartHumanLoopResponseHumanLoopActivationResultsTypeDef",
    "ClientStartHumanLoopResponseTypeDef",
    "HumanLoopSummaryTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientDescribeHumanLoopResponseHumanLoopInputTypeDef = TypedDict(
    "ClientDescribeHumanLoopResponseHumanLoopInputTypeDef", {"InputContent": str}, total=False
)

ClientDescribeHumanLoopResponseHumanLoopOutputTypeDef = TypedDict(
    "ClientDescribeHumanLoopResponseHumanLoopOutputTypeDef", {"OutputS3Uri": str}, total=False
)

ClientDescribeHumanLoopResponseTypeDef = TypedDict(
    "ClientDescribeHumanLoopResponseTypeDef",
    {
        "CreationTimestamp": datetime,
        "FailureReason": str,
        "FailureCode": str,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
        "HumanLoopInput": ClientDescribeHumanLoopResponseHumanLoopInputTypeDef,
        "HumanLoopOutput": ClientDescribeHumanLoopResponseHumanLoopOutputTypeDef,
    },
    total=False,
)

ClientListHumanLoopsResponseHumanLoopSummariesTypeDef = TypedDict(
    "ClientListHumanLoopsResponseHumanLoopSummariesTypeDef",
    {
        "HumanLoopName": str,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "CreationTime": datetime,
        "FailureReason": str,
        "FlowDefinitionArn": str,
    },
    total=False,
)

ClientListHumanLoopsResponseTypeDef = TypedDict(
    "ClientListHumanLoopsResponseTypeDef",
    {
        "HumanLoopSummaries": List[ClientListHumanLoopsResponseHumanLoopSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientStartHumanLoopDataAttributesTypeDef = TypedDict(
    "ClientStartHumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
)

ClientStartHumanLoopHumanLoopInputTypeDef = TypedDict(
    "ClientStartHumanLoopHumanLoopInputTypeDef", {"InputContent": str}
)

ClientStartHumanLoopResponseHumanLoopActivationResultsHumanLoopActivationReasonTypeDef = TypedDict(
    "ClientStartHumanLoopResponseHumanLoopActivationResultsHumanLoopActivationReasonTypeDef",
    {"ConditionsMatched": bool},
    total=False,
)

ClientStartHumanLoopResponseHumanLoopActivationResultsTypeDef = TypedDict(
    "ClientStartHumanLoopResponseHumanLoopActivationResultsTypeDef",
    {
        "HumanLoopActivationReason": ClientStartHumanLoopResponseHumanLoopActivationResultsHumanLoopActivationReasonTypeDef,
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)

ClientStartHumanLoopResponseTypeDef = TypedDict(
    "ClientStartHumanLoopResponseTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationResults": ClientStartHumanLoopResponseHumanLoopActivationResultsTypeDef,
    },
    total=False,
)

HumanLoopSummaryTypeDef = TypedDict(
    "HumanLoopSummaryTypeDef",
    {
        "HumanLoopName": str,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "CreationTime": datetime,
        "FailureReason": str,
        "FlowDefinitionArn": str,
    },
    total=False,
)

_RequiredListHumanLoopsResponseTypeDef = TypedDict(
    "_RequiredListHumanLoopsResponseTypeDef", {"HumanLoopSummaries": List[HumanLoopSummaryTypeDef]}
)
_OptionalListHumanLoopsResponseTypeDef = TypedDict(
    "_OptionalListHumanLoopsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHumanLoopsResponseTypeDef(
    _RequiredListHumanLoopsResponseTypeDef, _OptionalListHumanLoopsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
