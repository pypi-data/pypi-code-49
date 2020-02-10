"""
Main interface for resource-groups service type definitions.

Usage::

    from mypy_boto3.resource_groups.type_defs import ClientCreateGroupResourceQueryTypeDef

    data: ClientCreateGroupResourceQueryTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateGroupResourceQueryTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseResourceQueryTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientDeleteGroupResponseGroupTypeDef",
    "ClientDeleteGroupResponseTypeDef",
    "ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef",
    "ClientGetGroupQueryResponseGroupQueryTypeDef",
    "ClientGetGroupQueryResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientListGroupResourcesFiltersTypeDef",
    "ClientListGroupResourcesResponseQueryErrorsTypeDef",
    "ClientListGroupResourcesResponseResourceIdentifiersTypeDef",
    "ClientListGroupResourcesResponseTypeDef",
    "ClientListGroupsFiltersTypeDef",
    "ClientListGroupsResponseGroupIdentifiersTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientSearchResourcesResourceQueryTypeDef",
    "ClientSearchResourcesResponseQueryErrorsTypeDef",
    "ClientSearchResourcesResponseResourceIdentifiersTypeDef",
    "ClientSearchResourcesResponseTypeDef",
    "ClientTagResponseTypeDef",
    "ClientUntagResponseTypeDef",
    "ClientUpdateGroupQueryResourceQueryTypeDef",
    "ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef",
    "ClientUpdateGroupQueryResponseGroupQueryTypeDef",
    "ClientUpdateGroupQueryResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "GroupFilterTypeDef",
    "QueryErrorTypeDef",
    "ResourceIdentifierTypeDef",
    "ListGroupResourcesOutputTypeDef",
    "GroupIdentifierTypeDef",
    "GroupTypeDef",
    "ListGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceFilterTypeDef",
    "ResourceQueryTypeDef",
    "SearchResourcesOutputTypeDef",
)

_RequiredClientCreateGroupResourceQueryTypeDef = TypedDict(
    "_RequiredClientCreateGroupResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalClientCreateGroupResourceQueryTypeDef = TypedDict(
    "_OptionalClientCreateGroupResourceQueryTypeDef", {"Query": str}, total=False
)


class ClientCreateGroupResourceQueryTypeDef(
    _RequiredClientCreateGroupResourceQueryTypeDef, _OptionalClientCreateGroupResourceQueryTypeDef
):
    pass


ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)

ClientCreateGroupResponseResourceQueryTypeDef = TypedDict(
    "ClientCreateGroupResponseResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {
        "Group": ClientCreateGroupResponseGroupTypeDef,
        "ResourceQuery": ClientCreateGroupResponseResourceQueryTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDeleteGroupResponseGroupTypeDef = TypedDict(
    "ClientDeleteGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)

ClientDeleteGroupResponseTypeDef = TypedDict(
    "ClientDeleteGroupResponseTypeDef",
    {"Group": ClientDeleteGroupResponseGroupTypeDef},
    total=False,
)

ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef = TypedDict(
    "ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
    total=False,
)

ClientGetGroupQueryResponseGroupQueryTypeDef = TypedDict(
    "ClientGetGroupQueryResponseGroupQueryTypeDef",
    {"GroupName": str, "ResourceQuery": ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef},
    total=False,
)

ClientGetGroupQueryResponseTypeDef = TypedDict(
    "ClientGetGroupQueryResponseTypeDef",
    {"GroupQuery": ClientGetGroupQueryResponseGroupQueryTypeDef},
    total=False,
)

ClientGetGroupResponseGroupTypeDef = TypedDict(
    "ClientGetGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)

ClientGetTagsResponseTypeDef = TypedDict(
    "ClientGetTagsResponseTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)

_RequiredClientListGroupResourcesFiltersTypeDef = TypedDict(
    "_RequiredClientListGroupResourcesFiltersTypeDef", {"Name": str}
)
_OptionalClientListGroupResourcesFiltersTypeDef = TypedDict(
    "_OptionalClientListGroupResourcesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientListGroupResourcesFiltersTypeDef(
    _RequiredClientListGroupResourcesFiltersTypeDef, _OptionalClientListGroupResourcesFiltersTypeDef
):
    pass


ClientListGroupResourcesResponseQueryErrorsTypeDef = TypedDict(
    "ClientListGroupResourcesResponseQueryErrorsTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)

ClientListGroupResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "ClientListGroupResourcesResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)

ClientListGroupResourcesResponseTypeDef = TypedDict(
    "ClientListGroupResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[ClientListGroupResourcesResponseResourceIdentifiersTypeDef],
        "NextToken": str,
        "QueryErrors": List[ClientListGroupResourcesResponseQueryErrorsTypeDef],
    },
    total=False,
)

_RequiredClientListGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientListGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientListGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientListGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientListGroupsFiltersTypeDef(
    _RequiredClientListGroupsFiltersTypeDef, _OptionalClientListGroupsFiltersTypeDef
):
    pass


ClientListGroupsResponseGroupIdentifiersTypeDef = TypedDict(
    "ClientListGroupsResponseGroupIdentifiersTypeDef",
    {"GroupName": str, "GroupArn": str},
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {
        "GroupIdentifiers": List[ClientListGroupsResponseGroupIdentifiersTypeDef],
        "Groups": List[ClientListGroupsResponseGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientSearchResourcesResourceQueryTypeDef = TypedDict(
    "_RequiredClientSearchResourcesResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalClientSearchResourcesResourceQueryTypeDef = TypedDict(
    "_OptionalClientSearchResourcesResourceQueryTypeDef", {"Query": str}, total=False
)


class ClientSearchResourcesResourceQueryTypeDef(
    _RequiredClientSearchResourcesResourceQueryTypeDef,
    _OptionalClientSearchResourcesResourceQueryTypeDef,
):
    pass


ClientSearchResourcesResponseQueryErrorsTypeDef = TypedDict(
    "ClientSearchResourcesResponseQueryErrorsTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)

ClientSearchResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "ClientSearchResourcesResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)

ClientSearchResourcesResponseTypeDef = TypedDict(
    "ClientSearchResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[ClientSearchResourcesResponseResourceIdentifiersTypeDef],
        "NextToken": str,
        "QueryErrors": List[ClientSearchResourcesResponseQueryErrorsTypeDef],
    },
    total=False,
)

ClientTagResponseTypeDef = TypedDict(
    "ClientTagResponseTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)

ClientUntagResponseTypeDef = TypedDict(
    "ClientUntagResponseTypeDef", {"Arn": str, "Keys": List[str]}, total=False
)

_RequiredClientUpdateGroupQueryResourceQueryTypeDef = TypedDict(
    "_RequiredClientUpdateGroupQueryResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalClientUpdateGroupQueryResourceQueryTypeDef = TypedDict(
    "_OptionalClientUpdateGroupQueryResourceQueryTypeDef", {"Query": str}, total=False
)


class ClientUpdateGroupQueryResourceQueryTypeDef(
    _RequiredClientUpdateGroupQueryResourceQueryTypeDef,
    _OptionalClientUpdateGroupQueryResourceQueryTypeDef,
):
    pass


ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef = TypedDict(
    "ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
    total=False,
)

ClientUpdateGroupQueryResponseGroupQueryTypeDef = TypedDict(
    "ClientUpdateGroupQueryResponseGroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef,
    },
    total=False,
)

ClientUpdateGroupQueryResponseTypeDef = TypedDict(
    "ClientUpdateGroupQueryResponseTypeDef",
    {"GroupQuery": ClientUpdateGroupQueryResponseGroupQueryTypeDef},
    total=False,
)

ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "ClientUpdateGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)

ClientUpdateGroupResponseTypeDef = TypedDict(
    "ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)

GroupFilterTypeDef = TypedDict(
    "GroupFilterTypeDef", {"Name": Literal["resource-type"], "Values": List[str]}
)

QueryErrorTypeDef = TypedDict(
    "QueryErrorTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef", {"ResourceArn": str, "ResourceType": str}, total=False
)

ListGroupResourcesOutputTypeDef = TypedDict(
    "ListGroupResourcesOutputTypeDef",
    {
        "ResourceIdentifiers": List[ResourceIdentifierTypeDef],
        "NextToken": str,
        "QueryErrors": List[QueryErrorTypeDef],
    },
    total=False,
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef", {"GroupName": str, "GroupArn": str}, total=False
)

_RequiredGroupTypeDef = TypedDict("_RequiredGroupTypeDef", {"GroupArn": str, "Name": str})
_OptionalGroupTypeDef = TypedDict("_OptionalGroupTypeDef", {"Description": str}, total=False)


class GroupTypeDef(_RequiredGroupTypeDef, _OptionalGroupTypeDef):
    pass


ListGroupsOutputTypeDef = TypedDict(
    "ListGroupsOutputTypeDef",
    {
        "GroupIdentifiers": List[GroupIdentifierTypeDef],
        "Groups": List[GroupTypeDef],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ResourceFilterTypeDef = TypedDict(
    "ResourceFilterTypeDef", {"Name": Literal["resource-type"], "Values": List[str]}
)

ResourceQueryTypeDef = TypedDict(
    "ResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
)

SearchResourcesOutputTypeDef = TypedDict(
    "SearchResourcesOutputTypeDef",
    {
        "ResourceIdentifiers": List[ResourceIdentifierTypeDef],
        "NextToken": str,
        "QueryErrors": List[QueryErrorTypeDef],
    },
    total=False,
)
