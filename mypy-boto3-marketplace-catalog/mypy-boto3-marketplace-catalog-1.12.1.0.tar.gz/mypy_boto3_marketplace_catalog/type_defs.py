"""
Main interface for marketplace-catalog service type definitions.

Usage::

    from mypy_boto3.marketplace_catalog.type_defs import ClientCancelChangeSetResponseTypeDef

    data: ClientCancelChangeSetResponseTypeDef = {...}
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
    "ClientCancelChangeSetResponseTypeDef",
    "ClientDescribeChangeSetResponseChangeSetEntityTypeDef",
    "ClientDescribeChangeSetResponseChangeSetErrorDetailListTypeDef",
    "ClientDescribeChangeSetResponseChangeSetTypeDef",
    "ClientDescribeChangeSetResponseTypeDef",
    "ClientDescribeEntityResponseTypeDef",
    "ClientListChangeSetsFilterListTypeDef",
    "ClientListChangeSetsResponseChangeSetSummaryListTypeDef",
    "ClientListChangeSetsResponseTypeDef",
    "ClientListChangeSetsSortTypeDef",
    "ClientListEntitiesFilterListTypeDef",
    "ClientListEntitiesResponseEntitySummaryListTypeDef",
    "ClientListEntitiesResponseTypeDef",
    "ClientListEntitiesSortTypeDef",
    "ClientStartChangeSetChangeSetEntityTypeDef",
    "ClientStartChangeSetChangeSetTypeDef",
    "ClientStartChangeSetResponseTypeDef",
)

ClientCancelChangeSetResponseTypeDef = TypedDict(
    "ClientCancelChangeSetResponseTypeDef", {"ChangeSetId": str, "ChangeSetArn": str}, total=False
)

ClientDescribeChangeSetResponseChangeSetEntityTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangeSetEntityTypeDef",
    {"Type": str, "Identifier": str},
    total=False,
)

ClientDescribeChangeSetResponseChangeSetErrorDetailListTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangeSetErrorDetailListTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientDescribeChangeSetResponseChangeSetTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangeSetTypeDef",
    {
        "ChangeType": str,
        "Entity": ClientDescribeChangeSetResponseChangeSetEntityTypeDef,
        "ErrorDetailList": List[ClientDescribeChangeSetResponseChangeSetErrorDetailListTypeDef],
    },
    total=False,
)

ClientDescribeChangeSetResponseTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": Literal["PREPARING", "APPLYING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "FailureDescription": str,
        "ChangeSet": List[ClientDescribeChangeSetResponseChangeSetTypeDef],
    },
    total=False,
)

ClientDescribeEntityResponseTypeDef = TypedDict(
    "ClientDescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
    },
    total=False,
)

ClientListChangeSetsFilterListTypeDef = TypedDict(
    "ClientListChangeSetsFilterListTypeDef", {"Name": str, "ValueList": List[str]}, total=False
)

ClientListChangeSetsResponseChangeSetSummaryListTypeDef = TypedDict(
    "ClientListChangeSetsResponseChangeSetSummaryListTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": Literal["PREPARING", "APPLYING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "EntityIdList": List[str],
    },
    total=False,
)

ClientListChangeSetsResponseTypeDef = TypedDict(
    "ClientListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List[ClientListChangeSetsResponseChangeSetSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListChangeSetsSortTypeDef = TypedDict(
    "ClientListChangeSetsSortTypeDef",
    {"SortBy": str, "SortOrder": Literal["ASCENDING", "DESCENDING"]},
    total=False,
)

ClientListEntitiesFilterListTypeDef = TypedDict(
    "ClientListEntitiesFilterListTypeDef", {"Name": str, "ValueList": List[str]}, total=False
)

ClientListEntitiesResponseEntitySummaryListTypeDef = TypedDict(
    "ClientListEntitiesResponseEntitySummaryListTypeDef",
    {
        "Name": str,
        "EntityType": str,
        "EntityId": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Visibility": str,
    },
    total=False,
)

ClientListEntitiesResponseTypeDef = TypedDict(
    "ClientListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List[ClientListEntitiesResponseEntitySummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListEntitiesSortTypeDef = TypedDict(
    "ClientListEntitiesSortTypeDef",
    {"SortBy": str, "SortOrder": Literal["ASCENDING", "DESCENDING"]},
    total=False,
)

ClientStartChangeSetChangeSetEntityTypeDef = TypedDict(
    "ClientStartChangeSetChangeSetEntityTypeDef", {"Type": str, "Identifier": str}, total=False
)

_RequiredClientStartChangeSetChangeSetTypeDef = TypedDict(
    "_RequiredClientStartChangeSetChangeSetTypeDef", {"ChangeType": str}
)
_OptionalClientStartChangeSetChangeSetTypeDef = TypedDict(
    "_OptionalClientStartChangeSetChangeSetTypeDef",
    {"Entity": ClientStartChangeSetChangeSetEntityTypeDef, "Details": str},
    total=False,
)


class ClientStartChangeSetChangeSetTypeDef(
    _RequiredClientStartChangeSetChangeSetTypeDef, _OptionalClientStartChangeSetChangeSetTypeDef
):
    pass


ClientStartChangeSetResponseTypeDef = TypedDict(
    "ClientStartChangeSetResponseTypeDef", {"ChangeSetId": str, "ChangeSetArn": str}, total=False
)
