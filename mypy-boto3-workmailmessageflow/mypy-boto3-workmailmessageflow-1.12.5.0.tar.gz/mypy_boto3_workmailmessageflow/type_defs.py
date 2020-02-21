"""
Main interface for workmailmessageflow service type definitions.

Usage::

    from mypy_boto3.workmailmessageflow.type_defs import ClientGetRawMessageContentResponseTypeDef

    data: ClientGetRawMessageContentResponseTypeDef = {...}
"""
import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientGetRawMessageContentResponseTypeDef",)

ClientGetRawMessageContentResponseTypeDef = TypedDict(
    "ClientGetRawMessageContentResponseTypeDef", {"messageContent": StreamingBody}, total=False
)
