"""
Main interface for support service client

Usage::

    import boto3
    from mypy_boto3.support import SupportClient

    session = boto3.Session()

    client: SupportClient = boto3.client("support")
    session_client: SupportClient = session.client("support")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_support.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_support.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_support.type_defs import (
    ClientAddAttachmentsToSetAttachmentsTypeDef,
    ClientAddAttachmentsToSetResponseTypeDef,
    ClientAddCommunicationToCaseResponseTypeDef,
    ClientCreateCaseResponseTypeDef,
    ClientDescribeAttachmentResponseTypeDef,
    ClientDescribeCasesResponseTypeDef,
    ClientDescribeCommunicationsResponseTypeDef,
    ClientDescribeServicesResponseTypeDef,
    ClientDescribeSeverityLevelsResponseTypeDef,
    ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef,
    ClientDescribeTrustedAdvisorCheckResultResponseTypeDef,
    ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef,
    ClientDescribeTrustedAdvisorChecksResponseTypeDef,
    ClientRefreshTrustedAdvisorCheckResponseTypeDef,
    ClientResolveCaseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SupportClient",)


class SupportClient:
    """
    [Support.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_attachments_to_set(
        self,
        attachments: List[ClientAddAttachmentsToSetAttachmentsTypeDef],
        attachmentSetId: str = None,
    ) -> ClientAddAttachmentsToSetResponseTypeDef:
        """
        [Client.add_attachments_to_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.add_attachments_to_set)
        """

    def add_communication_to_case(
        self,
        communicationBody: str,
        caseId: str = None,
        ccEmailAddresses: List[str] = None,
        attachmentSetId: str = None,
    ) -> ClientAddCommunicationToCaseResponseTypeDef:
        """
        [Client.add_communication_to_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.add_communication_to_case)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.can_paginate)
        """

    def create_case(
        self,
        subject: str,
        communicationBody: str,
        serviceCode: str = None,
        severityCode: str = None,
        categoryCode: str = None,
        ccEmailAddresses: List[str] = None,
        language: str = None,
        issueType: str = None,
        attachmentSetId: str = None,
    ) -> ClientCreateCaseResponseTypeDef:
        """
        [Client.create_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.create_case)
        """

    def describe_attachment(self, attachmentId: str) -> ClientDescribeAttachmentResponseTypeDef:
        """
        [Client.describe_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_attachment)
        """

    def describe_cases(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        nextToken: str = None,
        maxResults: int = None,
        language: str = None,
        includeCommunications: bool = None,
    ) -> ClientDescribeCasesResponseTypeDef:
        """
        [Client.describe_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_cases)
        """

    def describe_communications(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeCommunicationsResponseTypeDef:
        """
        [Client.describe_communications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_communications)
        """

    def describe_services(
        self, serviceCodeList: List[str] = None, language: str = None
    ) -> ClientDescribeServicesResponseTypeDef:
        """
        [Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_services)
        """

    def describe_severity_levels(
        self, language: str = None
    ) -> ClientDescribeSeverityLevelsResponseTypeDef:
        """
        [Client.describe_severity_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_severity_levels)
        """

    def describe_trusted_advisor_check_refresh_statuses(
        self, checkIds: List[str]
    ) -> ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_refresh_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_trusted_advisor_check_refresh_statuses)
        """

    def describe_trusted_advisor_check_result(
        self, checkId: str, language: str = None
    ) -> ClientDescribeTrustedAdvisorCheckResultResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_trusted_advisor_check_result)
        """

    def describe_trusted_advisor_check_summaries(
        self, checkIds: List[str]
    ) -> ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_trusted_advisor_check_summaries)
        """

    def describe_trusted_advisor_checks(
        self, language: str
    ) -> ClientDescribeTrustedAdvisorChecksResponseTypeDef:
        """
        [Client.describe_trusted_advisor_checks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.describe_trusted_advisor_checks)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.generate_presigned_url)
        """

    def refresh_trusted_advisor_check(
        self, checkId: str
    ) -> ClientRefreshTrustedAdvisorCheckResponseTypeDef:
        """
        [Client.refresh_trusted_advisor_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.refresh_trusted_advisor_check)
        """

    def resolve_case(self, caseId: str = None) -> ClientResolveCaseResponseTypeDef:
        """
        [Client.resolve_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Client.resolve_case)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cases"]
    ) -> "paginator_scope.DescribeCasesPaginator":
        """
        [Paginator.DescribeCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Paginator.DescribeCases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_communications"]
    ) -> "paginator_scope.DescribeCommunicationsPaginator":
        """
        [Paginator.DescribeCommunications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/support.html#Support.Paginator.DescribeCommunications)
        """


class Exceptions:
    AttachmentIdNotFound: Boto3ClientError
    AttachmentLimitExceeded: Boto3ClientError
    AttachmentSetExpired: Boto3ClientError
    AttachmentSetIdNotFound: Boto3ClientError
    AttachmentSetSizeLimitExceeded: Boto3ClientError
    CaseCreationLimitExceeded: Boto3ClientError
    CaseIdNotFound: Boto3ClientError
    ClientError: Boto3ClientError
    DescribeAttachmentLimitExceeded: Boto3ClientError
    InternalServerError: Boto3ClientError
