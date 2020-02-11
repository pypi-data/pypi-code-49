"""
Main interface for guardduty service client

Usage::

    import boto3
    from mypy_boto3.guardduty import GuardDutyClient

    session = boto3.Session()

    client: GuardDutyClient = boto3.client("guardduty")
    session_client: GuardDutyClient = session.client("guardduty")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_guardduty.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_guardduty.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_guardduty.type_defs import (
    ClientCreateDetectorResponseTypeDef,
    ClientCreateFilterFindingCriteriaTypeDef,
    ClientCreateFilterResponseTypeDef,
    ClientCreateIpSetResponseTypeDef,
    ClientCreateMembersAccountDetailsTypeDef,
    ClientCreateMembersResponseTypeDef,
    ClientCreatePublishingDestinationDestinationPropertiesTypeDef,
    ClientCreatePublishingDestinationResponseTypeDef,
    ClientCreateThreatIntelSetResponseTypeDef,
    ClientDeclineInvitationsResponseTypeDef,
    ClientDeleteInvitationsResponseTypeDef,
    ClientDeleteMembersResponseTypeDef,
    ClientDescribePublishingDestinationResponseTypeDef,
    ClientDisassociateMembersResponseTypeDef,
    ClientGetDetectorResponseTypeDef,
    ClientGetFilterResponseTypeDef,
    ClientGetFindingsResponseTypeDef,
    ClientGetFindingsSortCriteriaTypeDef,
    ClientGetFindingsStatisticsFindingCriteriaTypeDef,
    ClientGetFindingsStatisticsResponseTypeDef,
    ClientGetInvitationsCountResponseTypeDef,
    ClientGetIpSetResponseTypeDef,
    ClientGetMasterAccountResponseTypeDef,
    ClientGetMembersResponseTypeDef,
    ClientGetThreatIntelSetResponseTypeDef,
    ClientInviteMembersResponseTypeDef,
    ClientListDetectorsResponseTypeDef,
    ClientListFiltersResponseTypeDef,
    ClientListFindingsFindingCriteriaTypeDef,
    ClientListFindingsResponseTypeDef,
    ClientListFindingsSortCriteriaTypeDef,
    ClientListInvitationsResponseTypeDef,
    ClientListIpSetsResponseTypeDef,
    ClientListMembersResponseTypeDef,
    ClientListPublishingDestinationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListThreatIntelSetsResponseTypeDef,
    ClientStartMonitoringMembersResponseTypeDef,
    ClientStopMonitoringMembersResponseTypeDef,
    ClientUpdateFilterFindingCriteriaTypeDef,
    ClientUpdateFilterResponseTypeDef,
    ClientUpdatePublishingDestinationDestinationPropertiesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GuardDutyClient",)


class GuardDutyClient:
    """
    [GuardDuty.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_invitation(
        self, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)
        """

    def archive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Client.archive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.archive_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.can_paginate)
        """

    def create_detector(
        self,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateDetectorResponseTypeDef:
        """
        [Client.create_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_detector)
        """

    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: ClientCreateFilterFindingCriteriaTypeDef,
        Description: str = None,
        Action: Literal["NOOP", "ARCHIVE"] = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateFilterResponseTypeDef:
        """
        [Client.create_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_filter)
        """

    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateIpSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)
        """

    def create_members(
        self, DetectorId: str, AccountDetails: List[ClientCreateMembersAccountDetailsTypeDef]
    ) -> ClientCreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_members)
        """

    def create_publishing_destination(
        self,
        DetectorId: str,
        DestinationType: str,
        DestinationProperties: ClientCreatePublishingDestinationDestinationPropertiesTypeDef,
        ClientToken: str = None,
    ) -> ClientCreatePublishingDestinationResponseTypeDef:
        """
        [Client.create_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)
        """

    def create_sample_findings(
        self, DetectorId: str, FindingTypes: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_sample_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)
        """

    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateThreatIntelSetResponseTypeDef:
        """
        [Client.create_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)
        """

    def decline_invitations(self, AccountIds: List[str]) -> ClientDeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)
        """

    def delete_detector(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Client.delete_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_detector)
        """

    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        [Client.delete_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_filter)
        """

    def delete_invitations(self, AccountIds: List[str]) -> ClientDeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)
        """

    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)
        """

    def delete_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientDeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_members)
        """

    def delete_publishing_destination(self, DetectorId: str, DestinationId: str) -> Dict[str, Any]:
        """
        [Client.delete_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)
        """

    def delete_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict[str, Any]:
        """
        [Client.delete_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)
        """

    def describe_publishing_destination(
        self, DetectorId: str, DestinationId: str
    ) -> ClientDescribePublishingDestinationResponseTypeDef:
        """
        [Client.describe_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)
        """

    def disassociate_from_master_account(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)
        """

    def disassociate_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientDisassociateMembersResponseTypeDef:
        """
        [Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)
        """

    def get_detector(self, DetectorId: str) -> ClientGetDetectorResponseTypeDef:
        """
        [Client.get_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_detector)
        """

    def get_filter(self, DetectorId: str, FilterName: str) -> ClientGetFilterResponseTypeDef:
        """
        [Client.get_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_filter)
        """

    def get_findings(
        self,
        DetectorId: str,
        FindingIds: List[str],
        SortCriteria: ClientGetFindingsSortCriteriaTypeDef = None,
    ) -> ClientGetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_findings)
        """

    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List[str],
        FindingCriteria: ClientGetFindingsStatisticsFindingCriteriaTypeDef = None,
    ) -> ClientGetFindingsStatisticsResponseTypeDef:
        """
        [Client.get_findings_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)
        """

    def get_invitations_count(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)
        """

    def get_ip_set(self, DetectorId: str, IpSetId: str) -> ClientGetIpSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)
        """

    def get_master_account(self, DetectorId: str) -> ClientGetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_master_account)
        """

    def get_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientGetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_members)
        """

    def get_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> ClientGetThreatIntelSetResponseTypeDef:
        """
        [Client.get_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)
        """

    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DisableEmailNotification: bool = None,
        Message: str = None,
    ) -> ClientInviteMembersResponseTypeDef:
        """
        [Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.invite_members)
        """

    def list_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDetectorsResponseTypeDef:
        """
        [Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_detectors)
        """

    def list_filters(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListFiltersResponseTypeDef:
        """
        [Client.list_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_filters)
        """

    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: ClientListFindingsFindingCriteriaTypeDef = None,
        SortCriteria: ClientListFindingsSortCriteriaTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_findings)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_invitations)
        """

    def list_ip_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListIpSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)
        """

    def list_members(
        self,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None,
    ) -> ClientListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_members)
        """

    def list_publishing_destinations(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListPublishingDestinationsResponseTypeDef:
        """
        [Client.list_publishing_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)
        """

    def list_threat_intel_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListThreatIntelSetsResponseTypeDef:
        """
        [Client.list_threat_intel_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)
        """

    def start_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientStartMonitoringMembersResponseTypeDef:
        """
        [Client.start_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)
        """

    def stop_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> ClientStopMonitoringMembersResponseTypeDef:
        """
        [Client.stop_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.tag_resource)
        """

    def unarchive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Client.unarchive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.untag_resource)
        """

    def update_detector(
        self,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.update_detector)
        """

    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: Literal["NOOP", "ARCHIVE"] = None,
        Rank: int = None,
        FindingCriteria: ClientUpdateFilterFindingCriteriaTypeDef = None,
    ) -> ClientUpdateFilterResponseTypeDef:
        """
        [Client.update_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.update_filter)
        """

    def update_findings_feedback(
        self,
        DetectorId: str,
        FindingIds: List[str],
        Feedback: Literal["USEFUL", "NOT_USEFUL"],
        Comments: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_findings_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)
        """

    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)
        """

    def update_publishing_destination(
        self,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: ClientUpdatePublishingDestinationDestinationPropertiesTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)
        """

    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_detectors"]
    ) -> "paginator_scope.ListDetectorsPaginator":
        """
        [Paginator.ListDetectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_filters"]
    ) -> "paginator_scope.ListFiltersPaginator":
        """
        [Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_findings"]
    ) -> "paginator_scope.ListFindingsPaginator":
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ip_sets"]
    ) -> "paginator_scope.ListIPSetsPaginator":
        """
        [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> "paginator_scope.ListInvitationsPaginator":
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_members"]
    ) -> "paginator_scope.ListMembersPaginator":
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> "paginator_scope.ListThreatIntelSetsPaginator":
        """
        [Paginator.ListThreatIntelSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
