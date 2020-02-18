"""
Main interface for transfer service type definitions.

Usage::

    from mypy_boto3.transfer.type_defs import ClientCreateServerEndpointDetailsTypeDef

    data: ClientCreateServerEndpointDetailsTypeDef = {...}
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
    "ClientCreateServerEndpointDetailsTypeDef",
    "ClientCreateServerIdentityProviderDetailsTypeDef",
    "ClientCreateServerResponseTypeDef",
    "ClientCreateServerTagsTypeDef",
    "ClientCreateUserHomeDirectoryMappingsTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientDescribeServerResponseServerEndpointDetailsTypeDef",
    "ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef",
    "ClientDescribeServerResponseServerTagsTypeDef",
    "ClientDescribeServerResponseServerTypeDef",
    "ClientDescribeServerResponseTypeDef",
    "ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef",
    "ClientDescribeUserResponseUserSshPublicKeysTypeDef",
    "ClientDescribeUserResponseUserTagsTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientImportSshPublicKeyResponseTypeDef",
    "ClientListServersResponseServersTypeDef",
    "ClientListServersResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestIdentityProviderResponseTypeDef",
    "ClientUpdateServerEndpointDetailsTypeDef",
    "ClientUpdateServerIdentityProviderDetailsTypeDef",
    "ClientUpdateServerResponseTypeDef",
    "ClientUpdateUserHomeDirectoryMappingsTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ListedServerTypeDef",
    "ListServersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateServerEndpointDetailsTypeDef = TypedDict(
    "ClientCreateServerEndpointDetailsTypeDef",
    {"AddressAllocationIds": List[str], "SubnetIds": List[str], "VpcEndpointId": str, "VpcId": str},
    total=False,
)

ClientCreateServerIdentityProviderDetailsTypeDef = TypedDict(
    "ClientCreateServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)

ClientCreateServerResponseTypeDef = TypedDict(
    "ClientCreateServerResponseTypeDef", {"ServerId": str}, total=False
)

_RequiredClientCreateServerTagsTypeDef = TypedDict(
    "_RequiredClientCreateServerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateServerTagsTypeDef = TypedDict(
    "_OptionalClientCreateServerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateServerTagsTypeDef(
    _RequiredClientCreateServerTagsTypeDef, _OptionalClientCreateServerTagsTypeDef
):
    pass


ClientCreateUserHomeDirectoryMappingsTypeDef = TypedDict(
    "ClientCreateUserHomeDirectoryMappingsTypeDef", {"Entry": str, "Target": str}, total=False
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"ServerId": str, "UserName": str}, total=False
)

_RequiredClientCreateUserTagsTypeDef = TypedDict(
    "_RequiredClientCreateUserTagsTypeDef", {"Key": str}
)
_OptionalClientCreateUserTagsTypeDef = TypedDict(
    "_OptionalClientCreateUserTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateUserTagsTypeDef(
    _RequiredClientCreateUserTagsTypeDef, _OptionalClientCreateUserTagsTypeDef
):
    pass


ClientDescribeServerResponseServerEndpointDetailsTypeDef = TypedDict(
    "ClientDescribeServerResponseServerEndpointDetailsTypeDef",
    {"AddressAllocationIds": List[str], "SubnetIds": List[str], "VpcEndpointId": str, "VpcId": str},
    total=False,
)

ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef = TypedDict(
    "ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)

ClientDescribeServerResponseServerTagsTypeDef = TypedDict(
    "ClientDescribeServerResponseServerTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeServerResponseServerTypeDef = TypedDict(
    "ClientDescribeServerResponseServerTypeDef",
    {
        "Arn": str,
        "EndpointDetails": ClientDescribeServerResponseServerEndpointDetailsTypeDef,
        "EndpointType": Literal["PUBLIC", "VPC", "VPC_ENDPOINT"],
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef,
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "Tags": List[ClientDescribeServerResponseServerTagsTypeDef],
        "UserCount": int,
    },
    total=False,
)

ClientDescribeServerResponseTypeDef = TypedDict(
    "ClientDescribeServerResponseTypeDef",
    {"Server": ClientDescribeServerResponseServerTypeDef},
    total=False,
)

ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef = TypedDict(
    "ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef",
    {"Entry": str, "Target": str},
    total=False,
)

ClientDescribeUserResponseUserSshPublicKeysTypeDef = TypedDict(
    "ClientDescribeUserResponseUserSshPublicKeysTypeDef",
    {"DateImported": datetime, "SshPublicKeyBody": str, "SshPublicKeyId": str},
    total=False,
)

ClientDescribeUserResponseUserTagsTypeDef = TypedDict(
    "ClientDescribeUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeUserResponseUserTypeDef = TypedDict(
    "ClientDescribeUserResponseUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": str,
        "HomeDirectoryMappings": List[ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef],
        "HomeDirectoryType": Literal["PATH", "LOGICAL"],
        "Policy": str,
        "Role": str,
        "SshPublicKeys": List[ClientDescribeUserResponseUserSshPublicKeysTypeDef],
        "Tags": List[ClientDescribeUserResponseUserTagsTypeDef],
        "UserName": str,
    },
    total=False,
)

ClientDescribeUserResponseTypeDef = TypedDict(
    "ClientDescribeUserResponseTypeDef",
    {"ServerId": str, "User": ClientDescribeUserResponseUserTypeDef},
    total=False,
)

ClientImportSshPublicKeyResponseTypeDef = TypedDict(
    "ClientImportSshPublicKeyResponseTypeDef",
    {"ServerId": str, "SshPublicKeyId": str, "UserName": str},
    total=False,
)

ClientListServersResponseServersTypeDef = TypedDict(
    "ClientListServersResponseServersTypeDef",
    {
        "Arn": str,
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "EndpointType": Literal["PUBLIC", "VPC", "VPC_ENDPOINT"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "UserCount": int,
    },
    total=False,
)

ClientListServersResponseTypeDef = TypedDict(
    "ClientListServersResponseTypeDef",
    {"NextToken": str, "Servers": List[ClientListServersResponseServersTypeDef]},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Arn": str, "NextToken": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
    {
        "Arn": str,
        "HomeDirectory": str,
        "HomeDirectoryType": Literal["PATH", "LOGICAL"],
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"NextToken": str, "ServerId": str, "Users": List[ClientListUsersResponseUsersTypeDef]},
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientTestIdentityProviderResponseTypeDef = TypedDict(
    "ClientTestIdentityProviderResponseTypeDef",
    {"Response": str, "StatusCode": int, "Message": str, "Url": str},
    total=False,
)

ClientUpdateServerEndpointDetailsTypeDef = TypedDict(
    "ClientUpdateServerEndpointDetailsTypeDef",
    {"AddressAllocationIds": List[str], "SubnetIds": List[str], "VpcEndpointId": str, "VpcId": str},
    total=False,
)

ClientUpdateServerIdentityProviderDetailsTypeDef = TypedDict(
    "ClientUpdateServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)

ClientUpdateServerResponseTypeDef = TypedDict(
    "ClientUpdateServerResponseTypeDef", {"ServerId": str}, total=False
)

ClientUpdateUserHomeDirectoryMappingsTypeDef = TypedDict(
    "ClientUpdateUserHomeDirectoryMappingsTypeDef", {"Entry": str, "Target": str}, total=False
)

ClientUpdateUserResponseTypeDef = TypedDict(
    "ClientUpdateUserResponseTypeDef", {"ServerId": str, "UserName": str}, total=False
)

_RequiredListedServerTypeDef = TypedDict("_RequiredListedServerTypeDef", {"Arn": str})
_OptionalListedServerTypeDef = TypedDict(
    "_OptionalListedServerTypeDef",
    {
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "EndpointType": Literal["PUBLIC", "VPC", "VPC_ENDPOINT"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "UserCount": int,
    },
    total=False,
)


class ListedServerTypeDef(_RequiredListedServerTypeDef, _OptionalListedServerTypeDef):
    pass


_RequiredListServersResponseTypeDef = TypedDict(
    "_RequiredListServersResponseTypeDef", {"Servers": List[ListedServerTypeDef]}
)
_OptionalListServersResponseTypeDef = TypedDict(
    "_OptionalListServersResponseTypeDef", {"NextToken": str}, total=False
)


class ListServersResponseTypeDef(
    _RequiredListServersResponseTypeDef, _OptionalListServersResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
