"""
Main interface for route53domains service client

Usage::

    import boto3
    from mypy_boto3.route53domains import Route53DomainsClient

    session = boto3.Session()

    client: Route53DomainsClient = boto3.client("route53domains")
    session_client: Route53DomainsClient = session.client("route53domains")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_route53domains.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_route53domains.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_route53domains.type_defs import (
    ClientCheckDomainAvailabilityResponseTypeDef,
    ClientCheckDomainTransferabilityResponseTypeDef,
    ClientDisableDomainTransferLockResponseTypeDef,
    ClientEnableDomainTransferLockResponseTypeDef,
    ClientGetContactReachabilityStatusResponseTypeDef,
    ClientGetDomainDetailResponseTypeDef,
    ClientGetDomainSuggestionsResponseTypeDef,
    ClientGetOperationDetailResponseTypeDef,
    ClientListDomainsResponseTypeDef,
    ClientListOperationsResponseTypeDef,
    ClientListTagsForDomainResponseTypeDef,
    ClientRegisterDomainAdminContactTypeDef,
    ClientRegisterDomainRegistrantContactTypeDef,
    ClientRegisterDomainResponseTypeDef,
    ClientRegisterDomainTechContactTypeDef,
    ClientRenewDomainResponseTypeDef,
    ClientResendContactReachabilityEmailResponseTypeDef,
    ClientRetrieveDomainAuthCodeResponseTypeDef,
    ClientTransferDomainAdminContactTypeDef,
    ClientTransferDomainNameserversTypeDef,
    ClientTransferDomainRegistrantContactTypeDef,
    ClientTransferDomainResponseTypeDef,
    ClientTransferDomainTechContactTypeDef,
    ClientUpdateDomainContactAdminContactTypeDef,
    ClientUpdateDomainContactPrivacyResponseTypeDef,
    ClientUpdateDomainContactRegistrantContactTypeDef,
    ClientUpdateDomainContactResponseTypeDef,
    ClientUpdateDomainContactTechContactTypeDef,
    ClientUpdateDomainNameserversNameserversTypeDef,
    ClientUpdateDomainNameserversResponseTypeDef,
    ClientUpdateTagsForDomainTagsToUpdateTypeDef,
    ClientViewBillingResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53DomainsClient",)


class Route53DomainsClient:
    """
    [Route53Domains.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.can_paginate)
        """

    def check_domain_availability(
        self, DomainName: str, IdnLangCode: str = None
    ) -> ClientCheckDomainAvailabilityResponseTypeDef:
        """
        [Client.check_domain_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability)
        """

    def check_domain_transferability(
        self, DomainName: str, AuthCode: str = None
    ) -> ClientCheckDomainTransferabilityResponseTypeDef:
        """
        [Client.check_domain_transferability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.check_domain_transferability)
        """

    def delete_tags_for_domain(self, DomainName: str, TagsToDelete: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.delete_tags_for_domain)
        """

    def disable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        """
        [Client.disable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.disable_domain_auto_renew)
        """

    def disable_domain_transfer_lock(
        self, DomainName: str
    ) -> ClientDisableDomainTransferLockResponseTypeDef:
        """
        [Client.disable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.disable_domain_transfer_lock)
        """

    def enable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        """
        [Client.enable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.enable_domain_auto_renew)
        """

    def enable_domain_transfer_lock(
        self, DomainName: str
    ) -> ClientEnableDomainTransferLockResponseTypeDef:
        """
        [Client.enable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.enable_domain_transfer_lock)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.generate_presigned_url)
        """

    def get_contact_reachability_status(
        self, domainName: str = None
    ) -> ClientGetContactReachabilityStatusResponseTypeDef:
        """
        [Client.get_contact_reachability_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.get_contact_reachability_status)
        """

    def get_domain_detail(self, DomainName: str) -> ClientGetDomainDetailResponseTypeDef:
        """
        [Client.get_domain_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail)
        """

    def get_domain_suggestions(
        self, DomainName: str, SuggestionCount: int, OnlyAvailable: bool
    ) -> ClientGetDomainSuggestionsResponseTypeDef:
        """
        [Client.get_domain_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.get_domain_suggestions)
        """

    def get_operation_detail(self, OperationId: str) -> ClientGetOperationDetailResponseTypeDef:
        """
        [Client.get_operation_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.get_operation_detail)
        """

    def list_domains(
        self, Marker: str = None, MaxItems: int = None
    ) -> ClientListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.list_domains)
        """

    def list_operations(
        self, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListOperationsResponseTypeDef:
        """
        [Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.list_operations)
        """

    def list_tags_for_domain(self, DomainName: str) -> ClientListTagsForDomainResponseTypeDef:
        """
        [Client.list_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.list_tags_for_domain)
        """

    def register_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: ClientRegisterDomainAdminContactTypeDef,
        RegistrantContact: ClientRegisterDomainRegistrantContactTypeDef,
        TechContact: ClientRegisterDomainTechContactTypeDef,
        IdnLangCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> ClientRegisterDomainResponseTypeDef:
        """
        [Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.register_domain)
        """

    def renew_domain(
        self, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None
    ) -> ClientRenewDomainResponseTypeDef:
        """
        [Client.renew_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.renew_domain)
        """

    def resend_contact_reachability_email(
        self, domainName: str = None
    ) -> ClientResendContactReachabilityEmailResponseTypeDef:
        """
        [Client.resend_contact_reachability_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.resend_contact_reachability_email)
        """

    def retrieve_domain_auth_code(
        self, DomainName: str
    ) -> ClientRetrieveDomainAuthCodeResponseTypeDef:
        """
        [Client.retrieve_domain_auth_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.retrieve_domain_auth_code)
        """

    def transfer_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: ClientTransferDomainAdminContactTypeDef,
        RegistrantContact: ClientTransferDomainRegistrantContactTypeDef,
        TechContact: ClientTransferDomainTechContactTypeDef,
        IdnLangCode: str = None,
        Nameservers: List[ClientTransferDomainNameserversTypeDef] = None,
        AuthCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> ClientTransferDomainResponseTypeDef:
        """
        [Client.transfer_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.transfer_domain)
        """

    def update_domain_contact(
        self,
        DomainName: str,
        AdminContact: ClientUpdateDomainContactAdminContactTypeDef = None,
        RegistrantContact: ClientUpdateDomainContactRegistrantContactTypeDef = None,
        TechContact: ClientUpdateDomainContactTechContactTypeDef = None,
    ) -> ClientUpdateDomainContactResponseTypeDef:
        """
        [Client.update_domain_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact)
        """

    def update_domain_contact_privacy(
        self,
        DomainName: str,
        AdminPrivacy: bool = None,
        RegistrantPrivacy: bool = None,
        TechPrivacy: bool = None,
    ) -> ClientUpdateDomainContactPrivacyResponseTypeDef:
        """
        [Client.update_domain_contact_privacy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact_privacy)
        """

    def update_domain_nameservers(
        self,
        DomainName: str,
        Nameservers: List[ClientUpdateDomainNameserversNameserversTypeDef],
        FIAuthKey: str = None,
    ) -> ClientUpdateDomainNameserversResponseTypeDef:
        """
        [Client.update_domain_nameservers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.update_domain_nameservers)
        """

    def update_tags_for_domain(
        self,
        DomainName: str,
        TagsToUpdate: List[ClientUpdateTagsForDomainTagsToUpdateTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain)
        """

    def view_billing(
        self, Start: datetime = None, End: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ClientViewBillingResponseTypeDef:
        """
        [Client.view_billing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Client.view_billing)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domains"]
    ) -> "paginator_scope.ListDomainsPaginator":
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_operations"]
    ) -> "paginator_scope.ListOperationsPaginator":
        """
        [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["view_billing"]
    ) -> "paginator_scope.ViewBillingPaginator":
        """
        [Paginator.ViewBilling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DomainLimitExceeded: Boto3ClientError
    DuplicateRequest: Boto3ClientError
    InvalidInput: Boto3ClientError
    OperationLimitExceeded: Boto3ClientError
    TLDRulesViolation: Boto3ClientError
    UnsupportedTLD: Boto3ClientError
