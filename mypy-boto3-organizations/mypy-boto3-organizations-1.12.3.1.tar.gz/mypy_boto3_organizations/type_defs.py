"""
Main interface for organizations service type definitions.

Usage::

    from mypy_boto3.organizations.type_defs import ClientAcceptHandshakeResponseHandshakePartiesTypeDef

    data: ClientAcceptHandshakeResponseHandshakePartiesTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAcceptHandshakeResponseHandshakePartiesTypeDef",
    "ClientAcceptHandshakeResponseHandshakeResourcesTypeDef",
    "ClientAcceptHandshakeResponseHandshakeTypeDef",
    "ClientAcceptHandshakeResponseTypeDef",
    "ClientCancelHandshakeResponseHandshakePartiesTypeDef",
    "ClientCancelHandshakeResponseHandshakeResourcesTypeDef",
    "ClientCancelHandshakeResponseHandshakeTypeDef",
    "ClientCancelHandshakeResponseTypeDef",
    "ClientCreateAccountResponseCreateAccountStatusTypeDef",
    "ClientCreateAccountResponseTypeDef",
    "ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef",
    "ClientCreateGovCloudAccountResponseTypeDef",
    "ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    "ClientCreateOrganizationResponseOrganizationTypeDef",
    "ClientCreateOrganizationResponseTypeDef",
    "ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientCreateOrganizationalUnitResponseTypeDef",
    "ClientCreatePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientCreatePolicyResponsePolicyTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientDeclineHandshakeResponseHandshakePartiesTypeDef",
    "ClientDeclineHandshakeResponseHandshakeResourcesTypeDef",
    "ClientDeclineHandshakeResponseHandshakeTypeDef",
    "ClientDeclineHandshakeResponseTypeDef",
    "ClientDescribeAccountResponseAccountTypeDef",
    "ClientDescribeAccountResponseTypeDef",
    "ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef",
    "ClientDescribeCreateAccountStatusResponseTypeDef",
    "ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef",
    "ClientDescribeEffectivePolicyResponseTypeDef",
    "ClientDescribeHandshakeResponseHandshakePartiesTypeDef",
    "ClientDescribeHandshakeResponseHandshakeResourcesTypeDef",
    "ClientDescribeHandshakeResponseHandshakeTypeDef",
    "ClientDescribeHandshakeResponseTypeDef",
    "ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    "ClientDescribeOrganizationResponseOrganizationTypeDef",
    "ClientDescribeOrganizationResponseTypeDef",
    "ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientDescribeOrganizationalUnitResponseTypeDef",
    "ClientDescribePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientDescribePolicyResponsePolicyTypeDef",
    "ClientDescribePolicyResponseTypeDef",
    "ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef",
    "ClientDisablePolicyTypeResponseRootTypeDef",
    "ClientDisablePolicyTypeResponseTypeDef",
    "ClientEnableAllFeaturesResponseHandshakePartiesTypeDef",
    "ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef",
    "ClientEnableAllFeaturesResponseHandshakeTypeDef",
    "ClientEnableAllFeaturesResponseTypeDef",
    "ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef",
    "ClientEnablePolicyTypeResponseRootTypeDef",
    "ClientEnablePolicyTypeResponseTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakeTypeDef",
    "ClientInviteAccountToOrganizationResponseTypeDef",
    "ClientInviteAccountToOrganizationTargetTypeDef",
    "ClientListAccountsForParentResponseAccountsTypeDef",
    "ClientListAccountsForParentResponseTypeDef",
    "ClientListAccountsResponseAccountsTypeDef",
    "ClientListAccountsResponseTypeDef",
    "ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef",
    "ClientListAwsServiceAccessForOrganizationResponseTypeDef",
    "ClientListChildrenResponseChildrenTypeDef",
    "ClientListChildrenResponseTypeDef",
    "ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef",
    "ClientListCreateAccountStatusResponseTypeDef",
    "ClientListHandshakesForAccountFilterTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesTypeDef",
    "ClientListHandshakesForAccountResponseTypeDef",
    "ClientListHandshakesForOrganizationFilterTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesTypeDef",
    "ClientListHandshakesForOrganizationResponseTypeDef",
    "ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef",
    "ClientListOrganizationalUnitsForParentResponseTypeDef",
    "ClientListParentsResponseParentsTypeDef",
    "ClientListParentsResponseTypeDef",
    "ClientListPoliciesForTargetResponsePoliciesTypeDef",
    "ClientListPoliciesForTargetResponseTypeDef",
    "ClientListPoliciesResponsePoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListRootsResponseRootsPolicyTypesTypeDef",
    "ClientListRootsResponseRootsTypeDef",
    "ClientListRootsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsForPolicyResponseTargetsTypeDef",
    "ClientListTargetsForPolicyResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientUpdateOrganizationalUnitResponseTypeDef",
    "ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientUpdatePolicyResponsePolicyTypeDef",
    "ClientUpdatePolicyResponseTypeDef",
    "HandshakeFilterTypeDef",
    "EnabledServicePrincipalTypeDef",
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    "AccountTypeDef",
    "ListAccountsForParentResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "ChildTypeDef",
    "ListChildrenResponseTypeDef",
    "CreateAccountStatusTypeDef",
    "ListCreateAccountStatusResponseTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeResourceTypeDef",
    "HandshakeTypeDef",
    "ListHandshakesForAccountResponseTypeDef",
    "ListHandshakesForOrganizationResponseTypeDef",
    "OrganizationalUnitTypeDef",
    "ListOrganizationalUnitsForParentResponseTypeDef",
    "ParentTypeDef",
    "ListParentsResponseTypeDef",
    "PolicySummaryTypeDef",
    "ListPoliciesForTargetResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "PolicyTypeSummaryTypeDef",
    "RootTypeDef",
    "ListRootsResponseTypeDef",
    "TagTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PolicyTargetSummaryTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAcceptHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "ClientAcceptHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientAcceptHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "ClientAcceptHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientAcceptHandshakeResponseHandshakeTypeDef = TypedDict(
    "ClientAcceptHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientAcceptHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientAcceptHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)

ClientAcceptHandshakeResponseTypeDef = TypedDict(
    "ClientAcceptHandshakeResponseTypeDef",
    {"Handshake": ClientAcceptHandshakeResponseHandshakeTypeDef},
    total=False,
)

ClientCancelHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "ClientCancelHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientCancelHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "ClientCancelHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientCancelHandshakeResponseHandshakeTypeDef = TypedDict(
    "ClientCancelHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientCancelHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientCancelHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)

ClientCancelHandshakeResponseTypeDef = TypedDict(
    "ClientCancelHandshakeResponseTypeDef",
    {"Handshake": ClientCancelHandshakeResponseHandshakeTypeDef},
    total=False,
)

ClientCreateAccountResponseCreateAccountStatusTypeDef = TypedDict(
    "ClientCreateAccountResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)

ClientCreateAccountResponseTypeDef = TypedDict(
    "ClientCreateAccountResponseTypeDef",
    {"CreateAccountStatus": ClientCreateAccountResponseCreateAccountStatusTypeDef},
    total=False,
)

ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef = TypedDict(
    "ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)

ClientCreateGovCloudAccountResponseTypeDef = TypedDict(
    "ClientCreateGovCloudAccountResponseTypeDef",
    {"CreateAccountStatus": ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef},
    total=False,
)

ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef = TypedDict(
    "ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)

ClientCreateOrganizationResponseOrganizationTypeDef = TypedDict(
    "ClientCreateOrganizationResponseOrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": Literal["ALL", "CONSOLIDATED_BILLING"],
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List[
            ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
        ],
    },
    total=False,
)

ClientCreateOrganizationResponseTypeDef = TypedDict(
    "ClientCreateOrganizationResponseTypeDef",
    {"Organization": ClientCreateOrganizationResponseOrganizationTypeDef},
    total=False,
)

ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientCreateOrganizationalUnitResponseTypeDef = TypedDict(
    "ClientCreateOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef},
    total=False,
)

ClientCreatePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "ClientCreatePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)

ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "ClientCreatePolicyResponsePolicyTypeDef",
    {"PolicySummary": ClientCreatePolicyResponsePolicyPolicySummaryTypeDef, "Content": str},
    total=False,
)

ClientCreatePolicyResponseTypeDef = TypedDict(
    "ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)

ClientDeclineHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "ClientDeclineHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientDeclineHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "ClientDeclineHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientDeclineHandshakeResponseHandshakeTypeDef = TypedDict(
    "ClientDeclineHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientDeclineHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientDeclineHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)

ClientDeclineHandshakeResponseTypeDef = TypedDict(
    "ClientDeclineHandshakeResponseTypeDef",
    {"Handshake": ClientDeclineHandshakeResponseHandshakeTypeDef},
    total=False,
)

ClientDescribeAccountResponseAccountTypeDef = TypedDict(
    "ClientDescribeAccountResponseAccountTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)

ClientDescribeAccountResponseTypeDef = TypedDict(
    "ClientDescribeAccountResponseTypeDef",
    {"Account": ClientDescribeAccountResponseAccountTypeDef},
    total=False,
)

ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef = TypedDict(
    "ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)

ClientDescribeCreateAccountStatusResponseTypeDef = TypedDict(
    "ClientDescribeCreateAccountStatusResponseTypeDef",
    {"CreateAccountStatus": ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef},
    total=False,
)

ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef = TypedDict(
    "ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef",
    {"PolicyContent": str, "LastUpdatedTimestamp": datetime, "TargetId": str, "PolicyType": str},
    total=False,
)

ClientDescribeEffectivePolicyResponseTypeDef = TypedDict(
    "ClientDescribeEffectivePolicyResponseTypeDef",
    {"EffectivePolicy": ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef},
    total=False,
)

ClientDescribeHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "ClientDescribeHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientDescribeHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "ClientDescribeHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientDescribeHandshakeResponseHandshakeTypeDef = TypedDict(
    "ClientDescribeHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientDescribeHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientDescribeHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)

ClientDescribeHandshakeResponseTypeDef = TypedDict(
    "ClientDescribeHandshakeResponseTypeDef",
    {"Handshake": ClientDescribeHandshakeResponseHandshakeTypeDef},
    total=False,
)

ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef = TypedDict(
    "ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)

ClientDescribeOrganizationResponseOrganizationTypeDef = TypedDict(
    "ClientDescribeOrganizationResponseOrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": Literal["ALL", "CONSOLIDATED_BILLING"],
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List[
            ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
        ],
    },
    total=False,
)

ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationResponseTypeDef",
    {"Organization": ClientDescribeOrganizationResponseOrganizationTypeDef},
    total=False,
)

ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef},
    total=False,
)

ClientDescribePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "ClientDescribePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)

ClientDescribePolicyResponsePolicyTypeDef = TypedDict(
    "ClientDescribePolicyResponsePolicyTypeDef",
    {"PolicySummary": ClientDescribePolicyResponsePolicyPolicySummaryTypeDef, "Content": str},
    total=False,
)

ClientDescribePolicyResponseTypeDef = TypedDict(
    "ClientDescribePolicyResponseTypeDef",
    {"Policy": ClientDescribePolicyResponsePolicyTypeDef},
    total=False,
)

ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef = TypedDict(
    "ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)

ClientDisablePolicyTypeResponseRootTypeDef = TypedDict(
    "ClientDisablePolicyTypeResponseRootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef],
    },
    total=False,
)

ClientDisablePolicyTypeResponseTypeDef = TypedDict(
    "ClientDisablePolicyTypeResponseTypeDef",
    {"Root": ClientDisablePolicyTypeResponseRootTypeDef},
    total=False,
)

ClientEnableAllFeaturesResponseHandshakePartiesTypeDef = TypedDict(
    "ClientEnableAllFeaturesResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef = TypedDict(
    "ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientEnableAllFeaturesResponseHandshakeTypeDef = TypedDict(
    "ClientEnableAllFeaturesResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientEnableAllFeaturesResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef],
    },
    total=False,
)

ClientEnableAllFeaturesResponseTypeDef = TypedDict(
    "ClientEnableAllFeaturesResponseTypeDef",
    {"Handshake": ClientEnableAllFeaturesResponseHandshakeTypeDef},
    total=False,
)

ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef = TypedDict(
    "ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)

ClientEnablePolicyTypeResponseRootTypeDef = TypedDict(
    "ClientEnablePolicyTypeResponseRootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef],
    },
    total=False,
)

ClientEnablePolicyTypeResponseTypeDef = TypedDict(
    "ClientEnablePolicyTypeResponseTypeDef",
    {"Root": ClientEnablePolicyTypeResponseRootTypeDef},
    total=False,
)

ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef = TypedDict(
    "ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef = TypedDict(
    "ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientInviteAccountToOrganizationResponseHandshakeTypeDef = TypedDict(
    "ClientInviteAccountToOrganizationResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef],
    },
    total=False,
)

ClientInviteAccountToOrganizationResponseTypeDef = TypedDict(
    "ClientInviteAccountToOrganizationResponseTypeDef",
    {"Handshake": ClientInviteAccountToOrganizationResponseHandshakeTypeDef},
    total=False,
)

ClientInviteAccountToOrganizationTargetTypeDef = TypedDict(
    "ClientInviteAccountToOrganizationTargetTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientListAccountsForParentResponseAccountsTypeDef = TypedDict(
    "ClientListAccountsForParentResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)

ClientListAccountsForParentResponseTypeDef = TypedDict(
    "ClientListAccountsForParentResponseTypeDef",
    {"Accounts": List[ClientListAccountsForParentResponseAccountsTypeDef], "NextToken": str},
    total=False,
)

ClientListAccountsResponseAccountsTypeDef = TypedDict(
    "ClientListAccountsResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)

ClientListAccountsResponseTypeDef = TypedDict(
    "ClientListAccountsResponseTypeDef",
    {"Accounts": List[ClientListAccountsResponseAccountsTypeDef], "NextToken": str},
    total=False,
)

ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef = TypedDict(
    "ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)

ClientListAwsServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "ClientListAwsServiceAccessForOrganizationResponseTypeDef",
    {
        "EnabledServicePrincipals": List[
            ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListChildrenResponseChildrenTypeDef = TypedDict(
    "ClientListChildrenResponseChildrenTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]},
    total=False,
)

ClientListChildrenResponseTypeDef = TypedDict(
    "ClientListChildrenResponseTypeDef",
    {"Children": List[ClientListChildrenResponseChildrenTypeDef], "NextToken": str},
    total=False,
)

ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef = TypedDict(
    "ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)

ClientListCreateAccountStatusResponseTypeDef = TypedDict(
    "ClientListCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatuses": List[
            ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListHandshakesForAccountFilterTypeDef = TypedDict(
    "ClientListHandshakesForAccountFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)

ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef = TypedDict(
    "ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef = TypedDict(
    "ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientListHandshakesForAccountResponseHandshakesTypeDef = TypedDict(
    "ClientListHandshakesForAccountResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef],
    },
    total=False,
)

ClientListHandshakesForAccountResponseTypeDef = TypedDict(
    "ClientListHandshakesForAccountResponseTypeDef",
    {"Handshakes": List[ClientListHandshakesForAccountResponseHandshakesTypeDef], "NextToken": str},
    total=False,
)

ClientListHandshakesForOrganizationFilterTypeDef = TypedDict(
    "ClientListHandshakesForOrganizationFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)

ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef = TypedDict(
    "ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)

ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef = TypedDict(
    "ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)

ClientListHandshakesForOrganizationResponseHandshakesTypeDef = TypedDict(
    "ClientListHandshakesForOrganizationResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef],
    },
    total=False,
)

ClientListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "ClientListHandshakesForOrganizationResponseTypeDef",
    {
        "Handshakes": List[ClientListHandshakesForOrganizationResponseHandshakesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef = TypedDict(
    "ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "ClientListOrganizationalUnitsForParentResponseTypeDef",
    {
        "OrganizationalUnits": List[
            ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListParentsResponseParentsTypeDef = TypedDict(
    "ClientListParentsResponseParentsTypeDef",
    {"Id": str, "Type": Literal["ROOT", "ORGANIZATIONAL_UNIT"]},
    total=False,
)

ClientListParentsResponseTypeDef = TypedDict(
    "ClientListParentsResponseTypeDef",
    {"Parents": List[ClientListParentsResponseParentsTypeDef], "NextToken": str},
    total=False,
)

ClientListPoliciesForTargetResponsePoliciesTypeDef = TypedDict(
    "ClientListPoliciesForTargetResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)

ClientListPoliciesForTargetResponseTypeDef = TypedDict(
    "ClientListPoliciesForTargetResponseTypeDef",
    {"Policies": List[ClientListPoliciesForTargetResponsePoliciesTypeDef], "NextToken": str},
    total=False,
)

ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "ClientListPoliciesResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)

ClientListPoliciesResponseTypeDef = TypedDict(
    "ClientListPoliciesResponseTypeDef",
    {"Policies": List[ClientListPoliciesResponsePoliciesTypeDef], "NextToken": str},
    total=False,
)

ClientListRootsResponseRootsPolicyTypesTypeDef = TypedDict(
    "ClientListRootsResponseRootsPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)

ClientListRootsResponseRootsTypeDef = TypedDict(
    "ClientListRootsResponseRootsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientListRootsResponseRootsPolicyTypesTypeDef],
    },
    total=False,
)

ClientListRootsResponseTypeDef = TypedDict(
    "ClientListRootsResponseTypeDef",
    {"Roots": List[ClientListRootsResponseRootsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientListTargetsForPolicyResponseTargetsTypeDef = TypedDict(
    "ClientListTargetsForPolicyResponseTargetsTypeDef",
    {
        "TargetId": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"],
    },
    total=False,
)

ClientListTargetsForPolicyResponseTypeDef = TypedDict(
    "ClientListTargetsForPolicyResponseTypeDef",
    {"Targets": List[ClientListTargetsForPolicyResponseTargetsTypeDef], "NextToken": str},
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


ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientUpdateOrganizationalUnitResponseTypeDef = TypedDict(
    "ClientUpdateOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef},
    total=False,
)

ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)

ClientUpdatePolicyResponsePolicyTypeDef = TypedDict(
    "ClientUpdatePolicyResponsePolicyTypeDef",
    {"PolicySummary": ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef, "Content": str},
    total=False,
)

ClientUpdatePolicyResponseTypeDef = TypedDict(
    "ClientUpdatePolicyResponseTypeDef",
    {"Policy": ClientUpdatePolicyResponsePolicyTypeDef},
    total=False,
)

HandshakeFilterTypeDef = TypedDict(
    "HandshakeFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)

EnabledServicePrincipalTypeDef = TypedDict(
    "EnabledServicePrincipalTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)

ListAWSServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    {"EnabledServicePrincipals": List[EnabledServicePrincipalTypeDef], "NextToken": str},
    total=False,
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)

ListAccountsForParentResponseTypeDef = TypedDict(
    "ListAccountsForParentResponseTypeDef",
    {"Accounts": List[AccountTypeDef], "NextToken": str},
    total=False,
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef", {"Accounts": List[AccountTypeDef], "NextToken": str}, total=False
)

ChildTypeDef = TypedDict(
    "ChildTypeDef", {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]}, total=False
)

ListChildrenResponseTypeDef = TypedDict(
    "ListChildrenResponseTypeDef", {"Children": List[ChildTypeDef], "NextToken": str}, total=False
)

CreateAccountStatusTypeDef = TypedDict(
    "CreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)

ListCreateAccountStatusResponseTypeDef = TypedDict(
    "ListCreateAccountStatusResponseTypeDef",
    {"CreateAccountStatuses": List[CreateAccountStatusTypeDef], "NextToken": str},
    total=False,
)

HandshakePartyTypeDef = TypedDict(
    "HandshakePartyTypeDef", {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]}
)

HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": List["HandshakeResourceTypeDef"],
    },
    total=False,
)

HandshakeTypeDef = TypedDict(
    "HandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[HandshakePartyTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[HandshakeResourceTypeDef],
    },
    total=False,
)

ListHandshakesForAccountResponseTypeDef = TypedDict(
    "ListHandshakesForAccountResponseTypeDef",
    {"Handshakes": List[HandshakeTypeDef], "NextToken": str},
    total=False,
)

ListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "ListHandshakesForOrganizationResponseTypeDef",
    {"Handshakes": List[HandshakeTypeDef], "NextToken": str},
    total=False,
)

OrganizationalUnitTypeDef = TypedDict(
    "OrganizationalUnitTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

ListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentResponseTypeDef",
    {"OrganizationalUnits": List[OrganizationalUnitTypeDef], "NextToken": str},
    total=False,
)

ParentTypeDef = TypedDict(
    "ParentTypeDef", {"Id": str, "Type": Literal["ROOT", "ORGANIZATIONAL_UNIT"]}, total=False
)

ListParentsResponseTypeDef = TypedDict(
    "ListParentsResponseTypeDef", {"Parents": List[ParentTypeDef], "NextToken": str}, total=False
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)

ListPoliciesForTargetResponseTypeDef = TypedDict(
    "ListPoliciesForTargetResponseTypeDef",
    {"Policies": List[PolicySummaryTypeDef], "NextToken": str},
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {"Policies": List[PolicySummaryTypeDef], "NextToken": str},
    total=False,
)

PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)

RootTypeDef = TypedDict(
    "RootTypeDef",
    {"Id": str, "Arn": str, "Name": str, "PolicyTypes": List[PolicyTypeSummaryTypeDef]},
    total=False,
)

ListRootsResponseTypeDef = TypedDict(
    "ListRootsResponseTypeDef", {"Roots": List[RootTypeDef], "NextToken": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PolicyTargetSummaryTypeDef = TypedDict(
    "PolicyTargetSummaryTypeDef",
    {
        "TargetId": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"],
    },
    total=False,
)

ListTargetsForPolicyResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseTypeDef",
    {"Targets": List[PolicyTargetSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
