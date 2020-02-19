"""
Main interface for marketplacecommerceanalytics service type definitions.

Usage::

    from mypy_boto3.marketplacecommerceanalytics.type_defs import ClientGenerateDataSetResponseTypeDef

    data: ClientGenerateDataSetResponseTypeDef = {...}
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientGenerateDataSetResponseTypeDef", "ClientStartSupportDataExportResponseTypeDef")

ClientGenerateDataSetResponseTypeDef = TypedDict(
    "ClientGenerateDataSetResponseTypeDef", {"dataSetRequestId": str}, total=False
)

ClientStartSupportDataExportResponseTypeDef = TypedDict(
    "ClientStartSupportDataExportResponseTypeDef", {"dataSetRequestId": str}, total=False
)
