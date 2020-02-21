"""
Main interface for pricing service type definitions.

Usage::

    from mypy_boto3.pricing.type_defs import ClientDescribeServicesResponseServicesTypeDef

    data: ClientDescribeServicesResponseServicesTypeDef = {...}
"""
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
    "ClientDescribeServicesResponseServicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientGetAttributeValuesResponseAttributeValuesTypeDef",
    "ClientGetAttributeValuesResponseTypeDef",
    "ClientGetProductsFiltersTypeDef",
    "ClientGetProductsResponseTypeDef",
    "ServiceTypeDef",
    "DescribeServicesResponseTypeDef",
    "FilterTypeDef",
    "AttributeValueTypeDef",
    "GetAttributeValuesResponseTypeDef",
    "GetProductsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientDescribeServicesResponseServicesTypeDef = TypedDict(
    "ClientDescribeServicesResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)

ClientDescribeServicesResponseTypeDef = TypedDict(
    "ClientDescribeServicesResponseTypeDef",
    {
        "Services": List[ClientDescribeServicesResponseServicesTypeDef],
        "FormatVersion": str,
        "NextToken": str,
    },
    total=False,
)

ClientGetAttributeValuesResponseAttributeValuesTypeDef = TypedDict(
    "ClientGetAttributeValuesResponseAttributeValuesTypeDef", {"Value": str}, total=False
)

ClientGetAttributeValuesResponseTypeDef = TypedDict(
    "ClientGetAttributeValuesResponseTypeDef",
    {
        "AttributeValues": List[ClientGetAttributeValuesResponseAttributeValuesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientGetProductsFiltersTypeDef = TypedDict(
    "_RequiredClientGetProductsFiltersTypeDef", {"Type": str}
)
_OptionalClientGetProductsFiltersTypeDef = TypedDict(
    "_OptionalClientGetProductsFiltersTypeDef", {"Field": str, "Value": str}, total=False
)


class ClientGetProductsFiltersTypeDef(
    _RequiredClientGetProductsFiltersTypeDef, _OptionalClientGetProductsFiltersTypeDef
):
    pass


ClientGetProductsResponseTypeDef = TypedDict(
    "ClientGetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef", {"ServiceCode": str, "AttributeNames": List[str]}, total=False
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {"Services": List[ServiceTypeDef], "FormatVersion": str, "NextToken": str},
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef", {"Type": Literal["TERM_MATCH"], "Field": str, "Value": str}
)

AttributeValueTypeDef = TypedDict("AttributeValueTypeDef", {"Value": str}, total=False)

GetAttributeValuesResponseTypeDef = TypedDict(
    "GetAttributeValuesResponseTypeDef",
    {"AttributeValues": List[AttributeValueTypeDef], "NextToken": str},
    total=False,
)

GetProductsResponseTypeDef = TypedDict(
    "GetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
