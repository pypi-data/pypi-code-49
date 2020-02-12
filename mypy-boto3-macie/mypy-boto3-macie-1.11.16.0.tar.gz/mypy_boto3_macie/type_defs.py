"""
Main interface for macie service type definitions.

Usage::

    from mypy_boto3.macie.type_defs import ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef

    data: ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = {...}
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
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientAssociateS3ResourcesResponseTypeDef",
    "ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef",
    "ClientAssociateS3ResourcesS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesResponseTypeDef",
    "ClientListMemberAccountsResponsememberAccountsTypeDef",
    "ClientListMemberAccountsResponseTypeDef",
    "ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    "ClientListS3ResourcesResponses3ResourcesTypeDef",
    "ClientListS3ResourcesResponseTypeDef",
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientUpdateS3ResourcesResponseTypeDef",
    "ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef",
    "ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef",
    "MemberAccountTypeDef",
    "ListMemberAccountsResultTypeDef",
    "ClassificationTypeTypeDef",
    "S3ResourceClassificationTypeDef",
    "ListS3ResourcesResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)

ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientAssociateS3ResourcesResponseTypeDef = TypedDict(
    "ClientAssociateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)

ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef = TypedDict(
    "ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

_RequiredClientAssociateS3ResourcesS3ResourcesTypeDef = TypedDict(
    "_RequiredClientAssociateS3ResourcesS3ResourcesTypeDef", {"bucketName": str}
)
_OptionalClientAssociateS3ResourcesS3ResourcesTypeDef = TypedDict(
    "_OptionalClientAssociateS3ResourcesS3ResourcesTypeDef",
    {
        "prefix": str,
        "classificationType": ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ClientAssociateS3ResourcesS3ResourcesTypeDef(
    _RequiredClientAssociateS3ResourcesS3ResourcesTypeDef,
    _OptionalClientAssociateS3ResourcesS3ResourcesTypeDef,
):
    pass


_RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef = TypedDict(
    "_RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef", {"bucketName": str}
)
_OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef = TypedDict(
    "_OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef",
    {"prefix": str},
    total=False,
)


class ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef(
    _RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
    _OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
):
    pass


ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)

ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientDisassociateS3ResourcesResponseTypeDef = TypedDict(
    "ClientDisassociateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)

ClientListMemberAccountsResponsememberAccountsTypeDef = TypedDict(
    "ClientListMemberAccountsResponsememberAccountsTypeDef", {"accountId": str}, total=False
)

ClientListMemberAccountsResponseTypeDef = TypedDict(
    "ClientListMemberAccountsResponseTypeDef",
    {
        "memberAccounts": List[ClientListMemberAccountsResponsememberAccountsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

ClientListS3ResourcesResponses3ResourcesTypeDef = TypedDict(
    "ClientListS3ResourcesResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)

ClientListS3ResourcesResponseTypeDef = TypedDict(
    "ClientListS3ResourcesResponseTypeDef",
    {"s3Resources": List[ClientListS3ResourcesResponses3ResourcesTypeDef], "nextToken": str},
    total=False,
)

ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)

ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientUpdateS3ResourcesResponseTypeDef = TypedDict(
    "ClientUpdateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)

ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef = TypedDict(
    "ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

_RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef", {"bucketName": str}
)
_OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef",
    {
        "prefix": str,
        "classificationTypeUpdate": ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef(
    _RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
    _OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
):
    pass


MemberAccountTypeDef = TypedDict("MemberAccountTypeDef", {"accountId": str}, total=False)

ListMemberAccountsResultTypeDef = TypedDict(
    "ListMemberAccountsResultTypeDef",
    {"memberAccounts": List[MemberAccountTypeDef], "nextToken": str},
    total=False,
)

ClassificationTypeTypeDef = TypedDict(
    "ClassificationTypeTypeDef", {"oneTime": Literal["FULL", "NONE"], "continuous": Literal["FULL"]}
)

_RequiredS3ResourceClassificationTypeDef = TypedDict(
    "_RequiredS3ResourceClassificationTypeDef",
    {"bucketName": str, "classificationType": ClassificationTypeTypeDef},
)
_OptionalS3ResourceClassificationTypeDef = TypedDict(
    "_OptionalS3ResourceClassificationTypeDef", {"prefix": str}, total=False
)


class S3ResourceClassificationTypeDef(
    _RequiredS3ResourceClassificationTypeDef, _OptionalS3ResourceClassificationTypeDef
):
    pass


ListS3ResourcesResultTypeDef = TypedDict(
    "ListS3ResourcesResultTypeDef",
    {"s3Resources": List[S3ResourceClassificationTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
