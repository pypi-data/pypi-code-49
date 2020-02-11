"""
Main interface for acm service client

Usage::

    import boto3
    from mypy_boto3.acm import ACMClient

    session = boto3.Session()

    client: ACMClient = boto3.client("acm")
    session_client: ACMClient = session.client("acm")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_acm.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_acm.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_acm.type_defs import (
    ClientAddTagsToCertificateTagsTypeDef,
    ClientDescribeCertificateResponseTypeDef,
    ClientExportCertificateResponseTypeDef,
    ClientGetCertificateResponseTypeDef,
    ClientImportCertificateResponseTypeDef,
    ClientImportCertificateTagsTypeDef,
    ClientListCertificatesIncludesTypeDef,
    ClientListCertificatesResponseTypeDef,
    ClientListTagsForCertificateResponseTypeDef,
    ClientRemoveTagsFromCertificateTagsTypeDef,
    ClientRequestCertificateDomainValidationOptionsTypeDef,
    ClientRequestCertificateOptionsTypeDef,
    ClientRequestCertificateResponseTypeDef,
    ClientRequestCertificateTagsTypeDef,
    ClientUpdateCertificateOptionsOptionsTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_acm.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ACMClient",)


class ACMClient:
    """
    [ACM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags_to_certificate(
        self, CertificateArn: str, Tags: List[ClientAddTagsToCertificateTagsTypeDef]
    ) -> None:
        """
        [Client.add_tags_to_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.add_tags_to_certificate)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.can_paginate)
        """

    def delete_certificate(self, CertificateArn: str) -> None:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.delete_certificate)
        """

    def describe_certificate(self, CertificateArn: str) -> ClientDescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.describe_certificate)
        """

    def export_certificate(
        self, CertificateArn: str, Passphrase: bytes
    ) -> ClientExportCertificateResponseTypeDef:
        """
        [Client.export_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.export_certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.generate_presigned_url)
        """

    def get_certificate(self, CertificateArn: str) -> ClientGetCertificateResponseTypeDef:
        """
        [Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.get_certificate)
        """

    def import_certificate(
        self,
        Certificate: bytes,
        PrivateKey: bytes,
        CertificateArn: str = None,
        CertificateChain: bytes = None,
        Tags: List[ClientImportCertificateTagsTypeDef] = None,
    ) -> ClientImportCertificateResponseTypeDef:
        """
        [Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.import_certificate)
        """

    def list_certificates(
        self,
        CertificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        Includes: ClientListCertificatesIncludesTypeDef = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ClientListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.list_certificates)
        """

    def list_tags_for_certificate(
        self, CertificateArn: str
    ) -> ClientListTagsForCertificateResponseTypeDef:
        """
        [Client.list_tags_for_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.list_tags_for_certificate)
        """

    def remove_tags_from_certificate(
        self, CertificateArn: str, Tags: List[ClientRemoveTagsFromCertificateTagsTypeDef]
    ) -> None:
        """
        [Client.remove_tags_from_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.remove_tags_from_certificate)
        """

    def renew_certificate(self, CertificateArn: str) -> None:
        """
        [Client.renew_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.renew_certificate)
        """

    def request_certificate(
        self,
        DomainName: str,
        ValidationMethod: Literal["EMAIL", "DNS"] = None,
        SubjectAlternativeNames: List[str] = None,
        IdempotencyToken: str = None,
        DomainValidationOptions: List[
            ClientRequestCertificateDomainValidationOptionsTypeDef
        ] = None,
        Options: ClientRequestCertificateOptionsTypeDef = None,
        CertificateAuthorityArn: str = None,
        Tags: List[ClientRequestCertificateTagsTypeDef] = None,
    ) -> ClientRequestCertificateResponseTypeDef:
        """
        [Client.request_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.request_certificate)
        """

    def resend_validation_email(
        self, CertificateArn: str, Domain: str, ValidationDomain: str
    ) -> None:
        """
        [Client.resend_validation_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.resend_validation_email)
        """

    def update_certificate_options(
        self, CertificateArn: str, Options: ClientUpdateCertificateOptionsOptionsTypeDef
    ) -> None:
        """
        [Client.update_certificate_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Client.update_certificate_options)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> "paginator_scope.ListCertificatesPaginator":
        """
        [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Paginator.ListCertificates)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["certificate_validated"]
    ) -> "waiter_scope.CertificateValidatedWaiter":
        """
        [Waiter.CertificateValidated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/acm.html#ACM.Waiter.CertificateValidated)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidArgsException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidDomainValidationOptionsException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RequestInProgressException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
