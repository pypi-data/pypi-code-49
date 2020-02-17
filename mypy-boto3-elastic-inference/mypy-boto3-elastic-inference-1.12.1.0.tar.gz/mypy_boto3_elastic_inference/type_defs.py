"""
Main interface for elastic-inference service type definitions.

Usage::

    from mypy_boto3.elastic_inference.type_defs import ClientListTagsForResourceResponseTypeDef

    data: ClientListTagsForResourceResponseTypeDef = {...}
"""
import sys
from typing import Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientListTagsForResourceResponseTypeDef",)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)
