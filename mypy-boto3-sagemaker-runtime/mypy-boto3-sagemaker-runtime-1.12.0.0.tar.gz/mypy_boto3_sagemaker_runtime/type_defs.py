"""
Main interface for sagemaker-runtime service type definitions.

Usage::

    from mypy_boto3.sagemaker_runtime.type_defs import ClientInvokeEndpointResponseTypeDef

    data: ClientInvokeEndpointResponseTypeDef = {...}
"""
import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientInvokeEndpointResponseTypeDef",)

ClientInvokeEndpointResponseTypeDef = TypedDict(
    "ClientInvokeEndpointResponseTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
    },
    total=False,
)
