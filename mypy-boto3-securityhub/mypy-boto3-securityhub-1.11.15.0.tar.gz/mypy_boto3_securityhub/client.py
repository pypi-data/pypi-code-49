"""
Main interface for securityhub service client

Usage::

    import boto3
    from mypy_boto3.securityhub import SecurityHubClient

    session = boto3.Session()

    client: SecurityHubClient = boto3.client("securityhub")
    session_client: SecurityHubClient = session.client("securityhub")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_securityhub.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_securityhub.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_securityhub.type_defs import (
    ClientBatchDisableStandardsResponseTypeDef,
    ClientBatchEnableStandardsResponseTypeDef,
    ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef,
    ClientBatchImportFindingsFindingsTypeDef,
    ClientBatchImportFindingsResponseTypeDef,
    ClientCreateActionTargetResponseTypeDef,
    ClientCreateInsightFiltersTypeDef,
    ClientCreateInsightResponseTypeDef,
    ClientCreateMembersAccountDetailsTypeDef,
    ClientCreateMembersResponseTypeDef,
    ClientDeclineInvitationsResponseTypeDef,
    ClientDeleteActionTargetResponseTypeDef,
    ClientDeleteInsightResponseTypeDef,
    ClientDeleteInvitationsResponseTypeDef,
    ClientDeleteMembersResponseTypeDef,
    ClientDescribeActionTargetsResponseTypeDef,
    ClientDescribeHubResponseTypeDef,
    ClientDescribeProductsResponseTypeDef,
    ClientDescribeStandardsControlsResponseTypeDef,
    ClientEnableImportFindingsForProductResponseTypeDef,
    ClientGetEnabledStandardsResponseTypeDef,
    ClientGetFindingsFiltersTypeDef,
    ClientGetFindingsResponseTypeDef,
    ClientGetFindingsSortCriteriaTypeDef,
    ClientGetInsightResultsResponseTypeDef,
    ClientGetInsightsResponseTypeDef,
    ClientGetInvitationsCountResponseTypeDef,
    ClientGetMasterAccountResponseTypeDef,
    ClientGetMembersResponseTypeDef,
    ClientInviteMembersResponseTypeDef,
    ClientListEnabledProductsForImportResponseTypeDef,
    ClientListInvitationsResponseTypeDef,
    ClientListMembersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateFindingsFiltersTypeDef,
    ClientUpdateFindingsNoteTypeDef,
    ClientUpdateInsightFiltersTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SecurityHubClient",)


class SecurityHubClient:
    """
    [SecurityHub.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_invitation(self, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)
        """

    def batch_disable_standards(
        self, StandardsSubscriptionArns: List[str]
    ) -> ClientBatchDisableStandardsResponseTypeDef:
        """
        [Client.batch_disable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)
        """

    def batch_enable_standards(
        self,
        StandardsSubscriptionRequests: List[
            ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef
        ],
    ) -> ClientBatchEnableStandardsResponseTypeDef:
        """
        [Client.batch_enable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)
        """

    def batch_import_findings(
        self, Findings: List[ClientBatchImportFindingsFindingsTypeDef]
    ) -> ClientBatchImportFindingsResponseTypeDef:
        """
        [Client.batch_import_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.can_paginate)
        """

    def create_action_target(
        self, Name: str, Description: str, Id: str
    ) -> ClientCreateActionTargetResponseTypeDef:
        """
        [Client.create_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.create_action_target)
        """

    def create_insight(
        self, Name: str, Filters: ClientCreateInsightFiltersTypeDef, GroupByAttribute: str
    ) -> ClientCreateInsightResponseTypeDef:
        """
        [Client.create_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.create_insight)
        """

    def create_members(
        self, AccountDetails: List[ClientCreateMembersAccountDetailsTypeDef] = None
    ) -> ClientCreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.create_members)
        """

    def decline_invitations(self, AccountIds: List[str]) -> ClientDeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)
        """

    def delete_action_target(self, ActionTargetArn: str) -> ClientDeleteActionTargetResponseTypeDef:
        """
        [Client.delete_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)
        """

    def delete_insight(self, InsightArn: str) -> ClientDeleteInsightResponseTypeDef:
        """
        [Client.delete_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.delete_insight)
        """

    def delete_invitations(self, AccountIds: List[str]) -> ClientDeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)
        """

    def delete_members(self, AccountIds: List[str] = None) -> ClientDeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.delete_members)
        """

    def describe_action_targets(
        self, ActionTargetArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeActionTargetsResponseTypeDef:
        """
        [Client.describe_action_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)
        """

    def describe_hub(self, HubArn: str = None) -> ClientDescribeHubResponseTypeDef:
        """
        [Client.describe_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.describe_hub)
        """

    def describe_products(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeProductsResponseTypeDef:
        """
        [Client.describe_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.describe_products)
        """

    def describe_standards_controls(
        self, StandardsSubscriptionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeStandardsControlsResponseTypeDef:
        """
        [Client.describe_standards_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.describe_standards_controls)
        """

    def disable_import_findings_for_product(self, ProductSubscriptionArn: str) -> Dict[str, Any]:
        """
        [Client.disable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)
        """

    def disable_security_hub(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.disable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)
        """

    def disassociate_from_master_account(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)
        """

    def disassociate_members(self, AccountIds: List[str] = None) -> Dict[str, Any]:
        """
        [Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)
        """

    def enable_import_findings_for_product(
        self, ProductArn: str
    ) -> ClientEnableImportFindingsForProductResponseTypeDef:
        """
        [Client.enable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)
        """

    def enable_security_hub(self, Tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Client.enable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)
        """

    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetEnabledStandardsResponseTypeDef:
        """
        [Client.get_enabled_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)
        """

    def get_findings(
        self,
        Filters: ClientGetFindingsFiltersTypeDef = None,
        SortCriteria: List[ClientGetFindingsSortCriteriaTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_findings)
        """

    def get_insight_results(self, InsightArn: str) -> ClientGetInsightResultsResponseTypeDef:
        """
        [Client.get_insight_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)
        """

    def get_insights(
        self, InsightArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetInsightsResponseTypeDef:
        """
        [Client.get_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_insights)
        """

    def get_invitations_count(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)
        """

    def get_master_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_master_account)
        """

    def get_members(self, AccountIds: List[str]) -> ClientGetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.get_members)
        """

    def invite_members(self, AccountIds: List[str] = None) -> ClientInviteMembersResponseTypeDef:
        """
        [Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.invite_members)
        """

    def list_enabled_products_for_import(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListEnabledProductsForImportResponseTypeDef:
        """
        [Client.list_enabled_products_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.list_invitations)
        """

    def list_members(
        self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.list_members)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.untag_resource)
        """

    def update_action_target(
        self, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.update_action_target)
        """

    def update_findings(
        self,
        Filters: ClientUpdateFindingsFiltersTypeDef,
        Note: ClientUpdateFindingsNoteTypeDef = None,
        RecordState: Literal["ACTIVE", "ARCHIVED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.update_findings)
        """

    def update_insight(
        self,
        InsightArn: str,
        Name: str = None,
        Filters: ClientUpdateInsightFiltersTypeDef = None,
        GroupByAttribute: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.update_insight)
        """

    def update_standards_control(
        self,
        StandardsControlArn: str,
        ControlStatus: Literal["ENABLED", "DISABLED"] = None,
        DisabledReason: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_standards_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Client.update_standards_control)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_enabled_standards"]
    ) -> "paginator_scope.GetEnabledStandardsPaginator":
        """
        [Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_findings"]
    ) -> "paginator_scope.GetFindingsPaginator":
        """
        [Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_insights"]
    ) -> "paginator_scope.GetInsightsPaginator":
        """
        [Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> "paginator_scope.ListEnabledProductsForImportPaginator":
        """
        [Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> "paginator_scope.ListInvitationsPaginator":
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_members"]
    ) -> "paginator_scope.ListMembersPaginator":
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidAccessException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
