"""
Main interface for cloud9 service type definitions.

Usage::

    from mypy_boto3.cloud9.type_defs import ClientCreateEnvironmentEc2ResponseTypeDef

    data: ClientCreateEnvironmentEc2ResponseTypeDef = {...}
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
    "ClientCreateEnvironmentEc2ResponseTypeDef",
    "ClientCreateEnvironmentMembershipResponsemembershipTypeDef",
    "ClientCreateEnvironmentMembershipResponseTypeDef",
    "ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef",
    "ClientDescribeEnvironmentMembershipsResponseTypeDef",
    "ClientDescribeEnvironmentStatusResponseTypeDef",
    "ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef",
    "ClientDescribeEnvironmentsResponseenvironmentsTypeDef",
    "ClientDescribeEnvironmentsResponseTypeDef",
    "ClientListEnvironmentsResponseTypeDef",
    "ClientUpdateEnvironmentMembershipResponsemembershipTypeDef",
    "ClientUpdateEnvironmentMembershipResponseTypeDef",
    "EnvironmentMemberTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "ListEnvironmentsResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateEnvironmentEc2ResponseTypeDef = TypedDict(
    "ClientCreateEnvironmentEc2ResponseTypeDef", {"environmentId": str}, total=False
)

ClientCreateEnvironmentMembershipResponsemembershipTypeDef = TypedDict(
    "ClientCreateEnvironmentMembershipResponsemembershipTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)

ClientCreateEnvironmentMembershipResponseTypeDef = TypedDict(
    "ClientCreateEnvironmentMembershipResponseTypeDef",
    {"membership": ClientCreateEnvironmentMembershipResponsemembershipTypeDef},
    total=False,
)

ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef = TypedDict(
    "ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)

ClientDescribeEnvironmentMembershipsResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentMembershipsResponseTypeDef",
    {
        "memberships": List[ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeEnvironmentStatusResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentStatusResponseTypeDef",
    {
        "status": Literal[
            "error", "creating", "connecting", "ready", "stopping", "stopped", "deleting"
        ],
        "message": str,
    },
    total=False,
)

ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef",
    {
        "status": Literal["CREATING", "CREATED", "CREATE_FAILED", "DELETING", "DELETE_FAILED"],
        "reason": str,
        "failureResource": str,
    },
    total=False,
)

ClientDescribeEnvironmentsResponseenvironmentsTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseenvironmentsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "type": Literal["ssh", "ec2"],
        "arn": str,
        "ownerArn": str,
        "lifecycle": ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef,
    },
    total=False,
)

ClientDescribeEnvironmentsResponseTypeDef = TypedDict(
    "ClientDescribeEnvironmentsResponseTypeDef",
    {"environments": List[ClientDescribeEnvironmentsResponseenvironmentsTypeDef]},
    total=False,
)

ClientListEnvironmentsResponseTypeDef = TypedDict(
    "ClientListEnvironmentsResponseTypeDef",
    {"nextToken": str, "environmentIds": List[str]},
    total=False,
)

ClientUpdateEnvironmentMembershipResponsemembershipTypeDef = TypedDict(
    "ClientUpdateEnvironmentMembershipResponsemembershipTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)

ClientUpdateEnvironmentMembershipResponseTypeDef = TypedDict(
    "ClientUpdateEnvironmentMembershipResponseTypeDef",
    {"membership": ClientUpdateEnvironmentMembershipResponsemembershipTypeDef},
    total=False,
)

EnvironmentMemberTypeDef = TypedDict(
    "EnvironmentMemberTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)

DescribeEnvironmentMembershipsResultTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultTypeDef",
    {"memberships": List[EnvironmentMemberTypeDef], "nextToken": str},
    total=False,
)

ListEnvironmentsResultTypeDef = TypedDict(
    "ListEnvironmentsResultTypeDef", {"nextToken": str, "environmentIds": List[str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
