"""
Main interface for iot-data service type definitions.

Usage::

    from mypy_boto3.iot_data.type_defs import ClientDeleteThingShadowResponseTypeDef

    data: ClientDeleteThingShadowResponseTypeDef = {...}
"""
import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDeleteThingShadowResponseTypeDef",
    "ClientGetThingShadowResponseTypeDef",
    "ClientUpdateThingShadowResponseTypeDef",
)

ClientDeleteThingShadowResponseTypeDef = TypedDict(
    "ClientDeleteThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)

ClientGetThingShadowResponseTypeDef = TypedDict(
    "ClientGetThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)

ClientUpdateThingShadowResponseTypeDef = TypedDict(
    "ClientUpdateThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)
