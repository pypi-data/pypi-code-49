"""
Main interface for guardduty service type definitions.

Usage::

    from mypy_boto3.guardduty.type_defs import ClientCreateDetectorResponseTypeDef

    data: ClientCreateDetectorResponseTypeDef = {...}
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
    "ClientCreateDetectorResponseTypeDef",
    "ClientCreateFilterFindingCriteriaCriterionTypeDef",
    "ClientCreateFilterFindingCriteriaTypeDef",
    "ClientCreateFilterResponseTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateMembersAccountDetailsTypeDef",
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    "ClientCreateMembersResponseTypeDef",
    "ClientCreatePublishingDestinationDestinationPropertiesTypeDef",
    "ClientCreatePublishingDestinationResponseTypeDef",
    "ClientCreateThreatIntelSetResponseTypeDef",
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeclineInvitationsResponseTypeDef",
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeleteInvitationsResponseTypeDef",
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    "ClientDeleteMembersResponseTypeDef",
    "ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef",
    "ClientDescribePublishingDestinationResponseTypeDef",
    "ClientDisassociateMembersResponseUnprocessedAccountsTypeDef",
    "ClientDisassociateMembersResponseTypeDef",
    "ClientGetDetectorResponseTypeDef",
    "ClientGetFilterResponseFindingCriteriaCriterionTypeDef",
    "ClientGetFilterResponseFindingCriteriaTypeDef",
    "ClientGetFilterResponseTypeDef",
    "ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourceTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceEvidenceTypeDef",
    "ClientGetFindingsResponseFindingsServiceTypeDef",
    "ClientGetFindingsResponseFindingsTypeDef",
    "ClientGetFindingsResponseTypeDef",
    "ClientGetFindingsSortCriteriaTypeDef",
    "ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef",
    "ClientGetFindingsStatisticsFindingCriteriaTypeDef",
    "ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef",
    "ClientGetFindingsStatisticsResponseTypeDef",
    "ClientGetInvitationsCountResponseTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetMasterAccountResponseMasterTypeDef",
    "ClientGetMasterAccountResponseTypeDef",
    "ClientGetMembersResponseMembersTypeDef",
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    "ClientGetMembersResponseTypeDef",
    "ClientGetThreatIntelSetResponseTypeDef",
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    "ClientInviteMembersResponseTypeDef",
    "ClientListDetectorsResponseTypeDef",
    "ClientListFiltersResponseTypeDef",
    "ClientListFindingsFindingCriteriaCriterionTypeDef",
    "ClientListFindingsFindingCriteriaTypeDef",
    "ClientListFindingsResponseTypeDef",
    "ClientListFindingsSortCriteriaTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListPublishingDestinationsResponseDestinationsTypeDef",
    "ClientListPublishingDestinationsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListThreatIntelSetsResponseTypeDef",
    "ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef",
    "ClientStartMonitoringMembersResponseTypeDef",
    "ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef",
    "ClientStopMonitoringMembersResponseTypeDef",
    "ClientUpdateFilterFindingCriteriaCriterionTypeDef",
    "ClientUpdateFilterFindingCriteriaTypeDef",
    "ClientUpdateFilterResponseTypeDef",
    "ClientUpdatePublishingDestinationDestinationPropertiesTypeDef",
    "ConditionTypeDef",
    "FindingCriteriaTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "InvitationTypeDef",
    "ListInvitationsResponseTypeDef",
    "MemberTypeDef",
    "ListMembersResponseTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SortCriteriaTypeDef",
)

ClientCreateDetectorResponseTypeDef = TypedDict(
    "ClientCreateDetectorResponseTypeDef", {"DetectorId": str}, total=False
)

ClientCreateFilterFindingCriteriaCriterionTypeDef = TypedDict(
    "ClientCreateFilterFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

ClientCreateFilterFindingCriteriaTypeDef = TypedDict(
    "ClientCreateFilterFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientCreateFilterFindingCriteriaCriterionTypeDef]},
    total=False,
)

ClientCreateFilterResponseTypeDef = TypedDict(
    "ClientCreateFilterResponseTypeDef", {"Name": str}, total=False
)

ClientCreateIpSetResponseTypeDef = TypedDict(
    "ClientCreateIpSetResponseTypeDef", {"IpSetId": str}, total=False
)

_RequiredClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "_RequiredClientCreateMembersAccountDetailsTypeDef", {"AccountId": str}
)
_OptionalClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "_OptionalClientCreateMembersAccountDetailsTypeDef", {"Email": str}, total=False
)


class ClientCreateMembersAccountDetailsTypeDef(
    _RequiredClientCreateMembersAccountDetailsTypeDef,
    _OptionalClientCreateMembersAccountDetailsTypeDef,
):
    pass


ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientCreateMembersResponseTypeDef = TypedDict(
    "ClientCreateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientCreateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientCreatePublishingDestinationDestinationPropertiesTypeDef = TypedDict(
    "ClientCreatePublishingDestinationDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)

ClientCreatePublishingDestinationResponseTypeDef = TypedDict(
    "ClientCreatePublishingDestinationResponseTypeDef", {"DestinationId": str}, total=False
)

ClientCreateThreatIntelSetResponseTypeDef = TypedDict(
    "ClientCreateThreatIntelSetResponseTypeDef", {"ThreatIntelSetId": str}, total=False
)

ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientDeclineInvitationsResponseTypeDef = TypedDict(
    "ClientDeclineInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientDeleteInvitationsResponseTypeDef = TypedDict(
    "ClientDeleteInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientDeleteMembersResponseTypeDef = TypedDict(
    "ClientDeleteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef = TypedDict(
    "ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)

ClientDescribePublishingDestinationResponseTypeDef = TypedDict(
    "ClientDescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": str,
        "Status": Literal[
            "PENDING_VERIFICATION",
            "PUBLISHING",
            "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
            "STOPPED",
        ],
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef,
    },
    total=False,
)

ClientDisassociateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDisassociateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientDisassociateMembersResponseTypeDef = TypedDict(
    "ClientDisassociateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDisassociateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientGetDetectorResponseTypeDef = TypedDict(
    "ClientGetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"],
        "ServiceRole": str,
        "Status": Literal["ENABLED", "DISABLED"],
        "UpdatedAt": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetFilterResponseFindingCriteriaCriterionTypeDef = TypedDict(
    "ClientGetFilterResponseFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

ClientGetFilterResponseFindingCriteriaTypeDef = TypedDict(
    "ClientGetFilterResponseFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientGetFilterResponseFindingCriteriaCriterionTypeDef]},
    total=False,
)

ClientGetFilterResponseTypeDef = TypedDict(
    "ClientGetFilterResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": Literal["NOOP", "ARCHIVE"],
        "Rank": int,
        "FindingCriteria": ClientGetFilterResponseFindingCriteriaTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef",
    {"AccessKeyId": str, "PrincipalId": str, "UserName": str, "UserType": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef",
    {"Arn": str, "Id": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef",
    {"PrivateDnsName": str, "PrivateIpAddress": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef",
    {"GroupId": str, "GroupName": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef",
    {
        "Ipv6Addresses": List[str],
        "NetworkInterfaceId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef
        ],
        "PublicDnsName": str,
        "PublicIp": str,
        "SecurityGroups": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef
        ],
        "SubnetId": str,
        "VpcId": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef",
    {"Code": str, "ProductType": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "IamInstanceProfile": ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef,
        "ImageDescription": str,
        "ImageId": str,
        "InstanceId": str,
        "InstanceState": str,
        "InstanceType": str,
        "LaunchTime": str,
        "NetworkInterfaces": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef
        ],
        "Platform": str,
        "ProductCodes": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef
        ],
        "Tags": List[ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourceTypeDef",
    {
        "AccessKeyDetails": ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef,
        "InstanceDetails": ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef,
        "ResourceType": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef",
    {"Domain": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef",
    {
        "Api": str,
        "CallerType": str,
        "DomainDetails": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef,
        "ServiceName": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef",
    {"Domain": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef",
    {
        "Blocked": bool,
        "ConnectionDirection": str,
        "LocalPortDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef,
        "Protocol": str,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef,
        "RemotePortDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef",
    {
        "LocalPortDetails": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef",
    {
        "Blocked": bool,
        "PortProbeDetails": List[
            ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef
        ],
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceActionTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceActionTypeDef",
    {
        "ActionType": str,
        "AwsApiCallAction": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef,
        "DnsRequestAction": ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef,
        "NetworkConnectionAction": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef,
        "PortProbeAction": ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef",
    {"ThreatListName": str, "ThreatNames": List[str]},
    total=False,
)

ClientGetFindingsResponseFindingsServiceEvidenceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceEvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": List[
            ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef
        ]
    },
    total=False,
)

ClientGetFindingsResponseFindingsServiceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsServiceTypeDef",
    {
        "Action": ClientGetFindingsResponseFindingsServiceActionTypeDef,
        "Evidence": ClientGetFindingsResponseFindingsServiceEvidenceTypeDef,
        "Archived": bool,
        "Count": int,
        "DetectorId": str,
        "EventFirstSeen": str,
        "EventLastSeen": str,
        "ResourceRole": str,
        "ServiceName": str,
        "UserFeedback": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "Confidence": float,
        "CreatedAt": str,
        "Description": str,
        "Id": str,
        "Partition": str,
        "Region": str,
        "Resource": ClientGetFindingsResponseFindingsResourceTypeDef,
        "SchemaVersion": str,
        "Service": ClientGetFindingsResponseFindingsServiceTypeDef,
        "Severity": float,
        "Title": str,
        "Type": str,
        "UpdatedAt": str,
    },
    total=False,
)

ClientGetFindingsResponseTypeDef = TypedDict(
    "ClientGetFindingsResponseTypeDef",
    {"Findings": List[ClientGetFindingsResponseFindingsTypeDef]},
    total=False,
)

ClientGetFindingsSortCriteriaTypeDef = TypedDict(
    "ClientGetFindingsSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": Literal["ASC", "DESC"]},
    total=False,
)

ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef = TypedDict(
    "ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

ClientGetFindingsStatisticsFindingCriteriaTypeDef = TypedDict(
    "ClientGetFindingsStatisticsFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef]},
    total=False,
)

ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef = TypedDict(
    "ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef",
    {"CountBySeverity": Dict[str, int]},
    total=False,
)

ClientGetFindingsStatisticsResponseTypeDef = TypedDict(
    "ClientGetFindingsStatisticsResponseTypeDef",
    {"FindingStatistics": ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef},
    total=False,
)

ClientGetInvitationsCountResponseTypeDef = TypedDict(
    "ClientGetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)

ClientGetIpSetResponseTypeDef = TypedDict(
    "ClientGetIpSetResponseTypeDef",
    {
        "Name": str,
        "Format": Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        "Location": str,
        "Status": Literal[
            "INACTIVE", "ACTIVATING", "ACTIVE", "DEACTIVATING", "ERROR", "DELETE_PENDING", "DELETED"
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetMasterAccountResponseMasterTypeDef = TypedDict(
    "ClientGetMasterAccountResponseMasterTypeDef",
    {"AccountId": str, "InvitationId": str, "RelationshipStatus": str, "InvitedAt": str},
    total=False,
)

ClientGetMasterAccountResponseTypeDef = TypedDict(
    "ClientGetMasterAccountResponseTypeDef",
    {"Master": ClientGetMasterAccountResponseMasterTypeDef},
    total=False,
)

ClientGetMembersResponseMembersTypeDef = TypedDict(
    "ClientGetMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)

ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientGetMembersResponseTypeDef = TypedDict(
    "ClientGetMembersResponseTypeDef",
    {
        "Members": List[ClientGetMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)

ClientGetThreatIntelSetResponseTypeDef = TypedDict(
    "ClientGetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        "Location": str,
        "Status": Literal[
            "INACTIVE", "ACTIVATING", "ACTIVE", "DEACTIVATING", "ERROR", "DELETE_PENDING", "DELETED"
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientInviteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientInviteMembersResponseTypeDef = TypedDict(
    "ClientInviteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientInviteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientListDetectorsResponseTypeDef = TypedDict(
    "ClientListDetectorsResponseTypeDef", {"DetectorIds": List[str], "NextToken": str}, total=False
)

ClientListFiltersResponseTypeDef = TypedDict(
    "ClientListFiltersResponseTypeDef", {"FilterNames": List[str], "NextToken": str}, total=False
)

ClientListFindingsFindingCriteriaCriterionTypeDef = TypedDict(
    "ClientListFindingsFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

ClientListFindingsFindingCriteriaTypeDef = TypedDict(
    "ClientListFindingsFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientListFindingsFindingCriteriaCriterionTypeDef]},
    total=False,
)

ClientListFindingsResponseTypeDef = TypedDict(
    "ClientListFindingsResponseTypeDef", {"FindingIds": List[str], "NextToken": str}, total=False
)

ClientListFindingsSortCriteriaTypeDef = TypedDict(
    "ClientListFindingsSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": Literal["ASC", "DESC"]},
    total=False,
)

ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "ClientListInvitationsResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "RelationshipStatus": str, "InvitedAt": str},
    total=False,
)

ClientListInvitationsResponseTypeDef = TypedDict(
    "ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)

ClientListIpSetsResponseTypeDef = TypedDict(
    "ClientListIpSetsResponseTypeDef", {"IpSetIds": List[str], "NextToken": str}, total=False
)

ClientListMembersResponseMembersTypeDef = TypedDict(
    "ClientListMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)

ClientListMembersResponseTypeDef = TypedDict(
    "ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)

ClientListPublishingDestinationsResponseDestinationsTypeDef = TypedDict(
    "ClientListPublishingDestinationsResponseDestinationsTypeDef",
    {
        "DestinationId": str,
        "DestinationType": str,
        "Status": Literal[
            "PENDING_VERIFICATION",
            "PUBLISHING",
            "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
            "STOPPED",
        ],
    },
    total=False,
)

ClientListPublishingDestinationsResponseTypeDef = TypedDict(
    "ClientListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List[ClientListPublishingDestinationsResponseDestinationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListThreatIntelSetsResponseTypeDef = TypedDict(
    "ClientListThreatIntelSetsResponseTypeDef",
    {"ThreatIntelSetIds": List[str], "NextToken": str},
    total=False,
)

ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientStartMonitoringMembersResponseTypeDef = TypedDict(
    "ClientStartMonitoringMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)

ClientStopMonitoringMembersResponseTypeDef = TypedDict(
    "ClientStopMonitoringMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientUpdateFilterFindingCriteriaCriterionTypeDef = TypedDict(
    "ClientUpdateFilterFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

ClientUpdateFilterFindingCriteriaTypeDef = TypedDict(
    "ClientUpdateFilterFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientUpdateFilterFindingCriteriaCriterionTypeDef]},
    total=False,
)

ClientUpdateFilterResponseTypeDef = TypedDict(
    "ClientUpdateFilterResponseTypeDef", {"Name": str}, total=False
)

ClientUpdatePublishingDestinationDestinationPropertiesTypeDef = TypedDict(
    "ClientUpdatePublishingDestinationDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef", {"Criterion": Dict[str, ConditionTypeDef]}, total=False
)

_RequiredListDetectorsResponseTypeDef = TypedDict(
    "_RequiredListDetectorsResponseTypeDef", {"DetectorIds": List[str]}
)
_OptionalListDetectorsResponseTypeDef = TypedDict(
    "_OptionalListDetectorsResponseTypeDef", {"NextToken": str}, total=False
)


class ListDetectorsResponseTypeDef(
    _RequiredListDetectorsResponseTypeDef, _OptionalListDetectorsResponseTypeDef
):
    pass


_RequiredListFiltersResponseTypeDef = TypedDict(
    "_RequiredListFiltersResponseTypeDef", {"FilterNames": List[str]}
)
_OptionalListFiltersResponseTypeDef = TypedDict(
    "_OptionalListFiltersResponseTypeDef", {"NextToken": str}, total=False
)


class ListFiltersResponseTypeDef(
    _RequiredListFiltersResponseTypeDef, _OptionalListFiltersResponseTypeDef
):
    pass


_RequiredListFindingsResponseTypeDef = TypedDict(
    "_RequiredListFindingsResponseTypeDef", {"FindingIds": List[str]}
)
_OptionalListFindingsResponseTypeDef = TypedDict(
    "_OptionalListFindingsResponseTypeDef", {"NextToken": str}, total=False
)


class ListFindingsResponseTypeDef(
    _RequiredListFindingsResponseTypeDef, _OptionalListFindingsResponseTypeDef
):
    pass


_RequiredListIPSetsResponseTypeDef = TypedDict(
    "_RequiredListIPSetsResponseTypeDef", {"IpSetIds": List[str]}
)
_OptionalListIPSetsResponseTypeDef = TypedDict(
    "_OptionalListIPSetsResponseTypeDef", {"NextToken": str}, total=False
)


class ListIPSetsResponseTypeDef(
    _RequiredListIPSetsResponseTypeDef, _OptionalListIPSetsResponseTypeDef
):
    pass


InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {"AccountId": str, "InvitationId": str, "RelationshipStatus": str, "InvitedAt": str},
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {"Invitations": List[InvitationTypeDef], "NextToken": str},
    total=False,
)

_RequiredMemberTypeDef = TypedDict(
    "_RequiredMemberTypeDef",
    {"AccountId": str, "MasterId": str, "Email": str, "RelationshipStatus": str, "UpdatedAt": str},
)
_OptionalMemberTypeDef = TypedDict(
    "_OptionalMemberTypeDef", {"DetectorId": str, "InvitedAt": str}, total=False
)


class MemberTypeDef(_RequiredMemberTypeDef, _OptionalMemberTypeDef):
    pass


ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef", {"Members": List[MemberTypeDef], "NextToken": str}, total=False
)

_RequiredListThreatIntelSetsResponseTypeDef = TypedDict(
    "_RequiredListThreatIntelSetsResponseTypeDef", {"ThreatIntelSetIds": List[str]}
)
_OptionalListThreatIntelSetsResponseTypeDef = TypedDict(
    "_OptionalListThreatIntelSetsResponseTypeDef", {"NextToken": str}, total=False
)


class ListThreatIntelSetsResponseTypeDef(
    _RequiredListThreatIntelSetsResponseTypeDef, _OptionalListThreatIntelSetsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef", {"AttributeName": str, "OrderBy": Literal["ASC", "DESC"]}, total=False
)
