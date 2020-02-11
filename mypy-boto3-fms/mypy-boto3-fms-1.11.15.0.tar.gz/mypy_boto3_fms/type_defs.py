"""
Main interface for fms service type definitions.

Usage::

    from mypy_boto3.fms.type_defs import ClientGetAdminAccountResponseTypeDef

    data: ClientGetAdminAccountResponseTypeDef = {...}
"""
from datetime import datetime
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
    "ClientGetAdminAccountResponseTypeDef",
    "ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
    "ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
    "ClientGetComplianceDetailResponseTypeDef",
    "ClientGetNotificationChannelResponseTypeDef",
    "ClientGetPolicyResponsePolicyResourceTagsTypeDef",
    "ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    "ClientGetPolicyResponsePolicyTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientGetProtectionStatusResponseTypeDef",
    "ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    "ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
    "ClientListComplianceStatusResponseTypeDef",
    "ClientListMemberAccountsResponseTypeDef",
    "ClientListPoliciesResponsePolicyListTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutPolicyPolicyResourceTagsTypeDef",
    "ClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
    "ClientPutPolicyPolicyTypeDef",
    "ClientPutPolicyResponsePolicyResourceTagsTypeDef",
    "ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    "ClientPutPolicyResponsePolicyTypeDef",
    "ClientPutPolicyResponseTypeDef",
    "ClientPutPolicyTagListTypeDef",
    "ClientTagResourceTagListTypeDef",
    "EvaluationResultTypeDef",
    "PolicyComplianceStatusTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "PolicySummaryTypeDef",
    "ListPoliciesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientGetAdminAccountResponseTypeDef = TypedDict(
    "ClientGetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": Literal["READY", "CREATING", "PENDING_DELETION", "DELETING", "DELETED"],
    },
    total=False,
)

ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef = TypedDict(
    "ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
    {
        "ResourceId": str,
        "ViolationReason": Literal[
            "WEB_ACL_MISSING_RULE_GROUP",
            "RESOURCE_MISSING_WEB_ACL",
            "RESOURCE_INCORRECT_WEB_ACL",
            "RESOURCE_MISSING_SHIELD_PROTECTION",
            "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
            "RESOURCE_MISSING_SECURITY_GROUP",
            "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
            "SECURITY_GROUP_UNUSED",
            "SECURITY_GROUP_REDUNDANT",
        ],
        "ResourceType": str,
    },
    total=False,
)

ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef = TypedDict(
    "ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "MemberAccount": str,
        "Violators": List[ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef],
        "EvaluationLimitExceeded": bool,
        "ExpiredAt": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)

ClientGetComplianceDetailResponseTypeDef = TypedDict(
    "ClientGetComplianceDetailResponseTypeDef",
    {"PolicyComplianceDetail": ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef},
    total=False,
)

ClientGetNotificationChannelResponseTypeDef = TypedDict(
    "ClientGetNotificationChannelResponseTypeDef",
    {"SnsTopicArn": str, "SnsRoleName": str},
    total=False,
)

ClientGetPolicyResponsePolicyResourceTagsTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "ManagedServiceData": str,
    },
    total=False,
)

ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyName": str,
        "PolicyUpdateToken": str,
        "SecurityServicePolicyData": ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ClientGetPolicyResponsePolicyResourceTagsTypeDef],
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "IncludeMap": Dict[str, List[str]],
        "ExcludeMap": Dict[str, List[str]],
    },
    total=False,
)

ClientGetPolicyResponseTypeDef = TypedDict(
    "ClientGetPolicyResponseTypeDef",
    {"Policy": ClientGetPolicyResponsePolicyTypeDef, "PolicyArn": str},
    total=False,
)

ClientGetProtectionStatusResponseTypeDef = TypedDict(
    "ClientGetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "Data": str,
        "NextToken": str,
    },
    total=False,
)

ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef
        ],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)

ClientListComplianceStatusResponseTypeDef = TypedDict(
    "ClientListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListMemberAccountsResponseTypeDef = TypedDict(
    "ClientListMemberAccountsResponseTypeDef",
    {"MemberAccounts": List[str], "NextToken": str},
    total=False,
)

ClientListPoliciesResponsePolicyListTypeDef = TypedDict(
    "ClientListPoliciesResponsePolicyListTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "RemediationEnabled": bool,
    },
    total=False,
)

ClientListPoliciesResponseTypeDef = TypedDict(
    "ClientListPoliciesResponseTypeDef",
    {"PolicyList": List[ClientListPoliciesResponsePolicyListTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientPutPolicyPolicyResourceTagsTypeDef = TypedDict(
    "ClientPutPolicyPolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientPutPolicyPolicySecurityServicePolicyDataTypeDef = TypedDict(
    "ClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "ManagedServiceData": str,
    },
    total=False,
)

ClientPutPolicyPolicyTypeDef = TypedDict(
    "ClientPutPolicyPolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyName": str,
        "PolicyUpdateToken": str,
        "SecurityServicePolicyData": ClientPutPolicyPolicySecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ClientPutPolicyPolicyResourceTagsTypeDef],
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "IncludeMap": Dict[str, List[str]],
        "ExcludeMap": Dict[str, List[str]],
    },
    total=False,
)

ClientPutPolicyResponsePolicyResourceTagsTypeDef = TypedDict(
    "ClientPutPolicyResponsePolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef = TypedDict(
    "ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "ManagedServiceData": str,
    },
    total=False,
)

ClientPutPolicyResponsePolicyTypeDef = TypedDict(
    "ClientPutPolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyName": str,
        "PolicyUpdateToken": str,
        "SecurityServicePolicyData": ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ClientPutPolicyResponsePolicyResourceTagsTypeDef],
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "IncludeMap": Dict[str, List[str]],
        "ExcludeMap": Dict[str, List[str]],
    },
    total=False,
)

ClientPutPolicyResponseTypeDef = TypedDict(
    "ClientPutPolicyResponseTypeDef",
    {"Policy": ClientPutPolicyResponsePolicyTypeDef, "PolicyArn": str},
    total=False,
)

_RequiredClientPutPolicyTagListTypeDef = TypedDict(
    "_RequiredClientPutPolicyTagListTypeDef", {"Key": str}
)
_OptionalClientPutPolicyTagListTypeDef = TypedDict(
    "_OptionalClientPutPolicyTagListTypeDef", {"Value": str}, total=False
)


class ClientPutPolicyTagListTypeDef(
    _RequiredClientPutPolicyTagListTypeDef, _OptionalClientPutPolicyTagListTypeDef
):
    pass


_RequiredClientTagResourceTagListTypeDef = TypedDict(
    "_RequiredClientTagResourceTagListTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagListTypeDef = TypedDict(
    "_OptionalClientTagResourceTagListTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagListTypeDef(
    _RequiredClientTagResourceTagListTypeDef, _OptionalClientTagResourceTagListTypeDef
):
    pass


EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[EvaluationResultTypeDef],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[Literal["AWSCONFIG", "AWSWAF", "AWSSHIELD_ADVANCED", "AWSVPC"], str],
    },
    total=False,
)

ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {"PolicyComplianceStatusList": List[PolicyComplianceStatusTypeDef], "NextToken": str},
    total=False,
)

ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {"MemberAccounts": List[str], "NextToken": str},
    total=False,
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "RemediationEnabled": bool,
    },
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {"PolicyList": List[PolicySummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
