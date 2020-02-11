"""
Main interface for codeguru-reviewer service type definitions.

Usage::

    from mypy_boto3.codeguru_reviewer.type_defs import ClientAssociateRepositoryRepositoryCodeCommitTypeDef

    data: ClientAssociateRepositoryRepositoryCodeCommitTypeDef = {...}
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
    "ClientAssociateRepositoryRepositoryCodeCommitTypeDef",
    "ClientAssociateRepositoryRepositoryTypeDef",
    "ClientAssociateRepositoryResponseRepositoryAssociationTypeDef",
    "ClientAssociateRepositoryResponseTypeDef",
    "ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef",
    "ClientDescribeRepositoryAssociationResponseTypeDef",
    "ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef",
    "ClientDisassociateRepositoryResponseTypeDef",
    "ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef",
    "ClientListRepositoryAssociationsResponseTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAssociateRepositoryRepositoryCodeCommitTypeDef = TypedDict(
    "ClientAssociateRepositoryRepositoryCodeCommitTypeDef", {"Name": str}
)

ClientAssociateRepositoryRepositoryTypeDef = TypedDict(
    "ClientAssociateRepositoryRepositoryTypeDef",
    {"CodeCommit": ClientAssociateRepositoryRepositoryCodeCommitTypeDef},
    total=False,
)

ClientAssociateRepositoryResponseRepositoryAssociationTypeDef = TypedDict(
    "ClientAssociateRepositoryResponseRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

ClientAssociateRepositoryResponseTypeDef = TypedDict(
    "ClientAssociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": ClientAssociateRepositoryResponseRepositoryAssociationTypeDef},
    total=False,
)

ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef = TypedDict(
    "ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

ClientDescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "ClientDescribeRepositoryAssociationResponseTypeDef",
    {
        "RepositoryAssociation": ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef
    },
    total=False,
)

ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef = TypedDict(
    "ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

ClientDisassociateRepositoryResponseTypeDef = TypedDict(
    "ClientDisassociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef},
    total=False,
)

ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef = TypedDict(
    "ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef",
    {
        "AssociationArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
    },
    total=False,
)

ClientListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ClientListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List[
            ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
    },
    total=False,
)

ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {"RepositoryAssociationSummaries": List[RepositoryAssociationSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
