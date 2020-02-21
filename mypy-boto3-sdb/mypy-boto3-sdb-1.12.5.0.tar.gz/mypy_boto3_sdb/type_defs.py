"""
Main interface for sdb service type definitions.

Usage::

    from mypy_boto3.sdb.type_defs import ClientBatchDeleteAttributesItemsAttributesTypeDef

    data: ClientBatchDeleteAttributesItemsAttributesTypeDef = {...}
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDeleteAttributesItemsAttributesTypeDef",
    "ClientBatchDeleteAttributesItemsTypeDef",
    "ClientBatchPutAttributesItemsAttributesTypeDef",
    "ClientBatchPutAttributesItemsTypeDef",
    "ClientDeleteAttributesAttributesTypeDef",
    "ClientDeleteAttributesExpectedTypeDef",
    "ClientDomainMetadataResponseTypeDef",
    "ClientGetAttributesResponseAttributesTypeDef",
    "ClientGetAttributesResponseTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientPutAttributesAttributesTypeDef",
    "ClientPutAttributesExpectedTypeDef",
    "ClientSelectResponseItemsAttributesTypeDef",
    "ClientSelectResponseItemsTypeDef",
    "ClientSelectResponseTypeDef",
    "ListDomainsResultTypeDef",
    "PaginatorConfigTypeDef",
    "AttributeTypeDef",
    "ItemTypeDef",
    "SelectResultTypeDef",
)

_RequiredClientBatchDeleteAttributesItemsAttributesTypeDef = TypedDict(
    "_RequiredClientBatchDeleteAttributesItemsAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientBatchDeleteAttributesItemsAttributesTypeDef = TypedDict(
    "_OptionalClientBatchDeleteAttributesItemsAttributesTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientBatchDeleteAttributesItemsAttributesTypeDef(
    _RequiredClientBatchDeleteAttributesItemsAttributesTypeDef,
    _OptionalClientBatchDeleteAttributesItemsAttributesTypeDef,
):
    pass


_RequiredClientBatchDeleteAttributesItemsTypeDef = TypedDict(
    "_RequiredClientBatchDeleteAttributesItemsTypeDef", {"Name": str}
)
_OptionalClientBatchDeleteAttributesItemsTypeDef = TypedDict(
    "_OptionalClientBatchDeleteAttributesItemsTypeDef",
    {"Attributes": List[ClientBatchDeleteAttributesItemsAttributesTypeDef]},
    total=False,
)


class ClientBatchDeleteAttributesItemsTypeDef(
    _RequiredClientBatchDeleteAttributesItemsTypeDef,
    _OptionalClientBatchDeleteAttributesItemsTypeDef,
):
    pass


_RequiredClientBatchPutAttributesItemsAttributesTypeDef = TypedDict(
    "_RequiredClientBatchPutAttributesItemsAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientBatchPutAttributesItemsAttributesTypeDef = TypedDict(
    "_OptionalClientBatchPutAttributesItemsAttributesTypeDef", {"Replace": bool}, total=False
)


class ClientBatchPutAttributesItemsAttributesTypeDef(
    _RequiredClientBatchPutAttributesItemsAttributesTypeDef,
    _OptionalClientBatchPutAttributesItemsAttributesTypeDef,
):
    pass


ClientBatchPutAttributesItemsTypeDef = TypedDict(
    "ClientBatchPutAttributesItemsTypeDef",
    {"Name": str, "Attributes": List[ClientBatchPutAttributesItemsAttributesTypeDef]},
)

_RequiredClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientDeleteAttributesAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientDeleteAttributesAttributesTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientDeleteAttributesAttributesTypeDef(
    _RequiredClientDeleteAttributesAttributesTypeDef,
    _OptionalClientDeleteAttributesAttributesTypeDef,
):
    pass


ClientDeleteAttributesExpectedTypeDef = TypedDict(
    "ClientDeleteAttributesExpectedTypeDef",
    {"Name": str, "Value": str, "Exists": bool},
    total=False,
)

ClientDomainMetadataResponseTypeDef = TypedDict(
    "ClientDomainMetadataResponseTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
    },
    total=False,
)

ClientGetAttributesResponseAttributesTypeDef = TypedDict(
    "ClientGetAttributesResponseAttributesTypeDef",
    {"Name": str, "AlternateNameEncoding": str, "Value": str, "AlternateValueEncoding": str},
    total=False,
)

ClientGetAttributesResponseTypeDef = TypedDict(
    "ClientGetAttributesResponseTypeDef",
    {"Attributes": List[ClientGetAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientListDomainsResponseTypeDef = TypedDict(
    "ClientListDomainsResponseTypeDef", {"DomainNames": List[str], "NextToken": str}, total=False
)

_RequiredClientPutAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientPutAttributesAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientPutAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientPutAttributesAttributesTypeDef", {"Replace": bool}, total=False
)


class ClientPutAttributesAttributesTypeDef(
    _RequiredClientPutAttributesAttributesTypeDef, _OptionalClientPutAttributesAttributesTypeDef
):
    pass


ClientPutAttributesExpectedTypeDef = TypedDict(
    "ClientPutAttributesExpectedTypeDef", {"Name": str, "Value": str, "Exists": bool}, total=False
)

ClientSelectResponseItemsAttributesTypeDef = TypedDict(
    "ClientSelectResponseItemsAttributesTypeDef",
    {"Name": str, "AlternateNameEncoding": str, "Value": str, "AlternateValueEncoding": str},
    total=False,
)

ClientSelectResponseItemsTypeDef = TypedDict(
    "ClientSelectResponseItemsTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Attributes": List[ClientSelectResponseItemsAttributesTypeDef],
    },
    total=False,
)

ClientSelectResponseTypeDef = TypedDict(
    "ClientSelectResponseTypeDef",
    {"Items": List[ClientSelectResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef", {"DomainNames": List[str], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"Name": str, "Value": str})
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


_RequiredItemTypeDef = TypedDict(
    "_RequiredItemTypeDef", {"Name": str, "Attributes": List[AttributeTypeDef]}
)
_OptionalItemTypeDef = TypedDict(
    "_OptionalItemTypeDef", {"AlternateNameEncoding": str}, total=False
)


class ItemTypeDef(_RequiredItemTypeDef, _OptionalItemTypeDef):
    pass


SelectResultTypeDef = TypedDict(
    "SelectResultTypeDef", {"Items": List[ItemTypeDef], "NextToken": str}, total=False
)
