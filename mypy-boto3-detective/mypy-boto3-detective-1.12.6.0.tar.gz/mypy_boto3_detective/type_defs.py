"""
Main interface for detective service type definitions.

Usage::

    from mypy_boto3.detective.type_defs import ClientCreateGraphResponseTypeDef

    data: ClientCreateGraphResponseTypeDef = {...}
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
    "ClientCreateGraphResponseTypeDef",
    "ClientCreateMembersAccountsTypeDef",
    "ClientCreateMembersResponseMembersTypeDef",
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    "ClientCreateMembersResponseTypeDef",
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    "ClientDeleteMembersResponseTypeDef",
    "ClientGetMembersResponseMemberDetailsTypeDef",
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    "ClientGetMembersResponseTypeDef",
    "ClientListGraphsResponseGraphListTypeDef",
    "ClientListGraphsResponseTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListMembersResponseMemberDetailsTypeDef",
    "ClientListMembersResponseTypeDef",
)

ClientCreateGraphResponseTypeDef = TypedDict(
    "ClientCreateGraphResponseTypeDef", {"GraphArn": str}, total=False
)

_RequiredClientCreateMembersAccountsTypeDef = TypedDict(
    "_RequiredClientCreateMembersAccountsTypeDef", {"AccountId": str}
)
_OptionalClientCreateMembersAccountsTypeDef = TypedDict(
    "_OptionalClientCreateMembersAccountsTypeDef", {"EmailAddress": str}, total=False
)


class ClientCreateMembersAccountsTypeDef(
    _RequiredClientCreateMembersAccountsTypeDef, _OptionalClientCreateMembersAccountsTypeDef
):
    pass


ClientCreateMembersResponseMembersTypeDef = TypedDict(
    "ClientCreateMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "Status": Literal["INVITED", "VERIFICATION_IN_PROGRESS", "VERIFICATION_FAILED", "ENABLED"],
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
    },
    total=False,
)

ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Reason": str},
    total=False,
)

ClientCreateMembersResponseTypeDef = TypedDict(
    "ClientCreateMembersResponseTypeDef",
    {
        "Members": List[ClientCreateMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientCreateMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)

ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Reason": str},
    total=False,
)

ClientDeleteMembersResponseTypeDef = TypedDict(
    "ClientDeleteMembersResponseTypeDef",
    {
        "AccountIds": List[str],
        "UnprocessedAccounts": List[ClientDeleteMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)

ClientGetMembersResponseMemberDetailsTypeDef = TypedDict(
    "ClientGetMembersResponseMemberDetailsTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "Status": Literal["INVITED", "VERIFICATION_IN_PROGRESS", "VERIFICATION_FAILED", "ENABLED"],
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
    },
    total=False,
)

ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Reason": str},
    total=False,
)

ClientGetMembersResponseTypeDef = TypedDict(
    "ClientGetMembersResponseTypeDef",
    {
        "MemberDetails": List[ClientGetMembersResponseMemberDetailsTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)

ClientListGraphsResponseGraphListTypeDef = TypedDict(
    "ClientListGraphsResponseGraphListTypeDef", {"Arn": str, "CreatedTime": datetime}, total=False
)

ClientListGraphsResponseTypeDef = TypedDict(
    "ClientListGraphsResponseTypeDef",
    {"GraphList": List[ClientListGraphsResponseGraphListTypeDef], "NextToken": str},
    total=False,
)

ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "ClientListInvitationsResponseInvitationsTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "Status": Literal["INVITED", "VERIFICATION_IN_PROGRESS", "VERIFICATION_FAILED", "ENABLED"],
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
    },
    total=False,
)

ClientListInvitationsResponseTypeDef = TypedDict(
    "ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)

ClientListMembersResponseMemberDetailsTypeDef = TypedDict(
    "ClientListMembersResponseMemberDetailsTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "Status": Literal["INVITED", "VERIFICATION_IN_PROGRESS", "VERIFICATION_FAILED", "ENABLED"],
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
    },
    total=False,
)

ClientListMembersResponseTypeDef = TypedDict(
    "ClientListMembersResponseTypeDef",
    {"MemberDetails": List[ClientListMembersResponseMemberDetailsTypeDef], "NextToken": str},
    total=False,
)
