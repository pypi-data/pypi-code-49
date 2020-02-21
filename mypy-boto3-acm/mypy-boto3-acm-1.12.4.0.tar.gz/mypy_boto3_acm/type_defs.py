"""
Main interface for acm service type definitions.

Usage::

    from mypy_boto3.acm.type_defs import ClientAddTagsToCertificateTagsTypeDef

    data: ClientAddTagsToCertificateTagsTypeDef = {...}
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
    "ClientAddTagsToCertificateTagsTypeDef",
    "ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef",
    "ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef",
    "ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef",
    "ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef",
    "ClientDescribeCertificateResponseCertificateOptionsTypeDef",
    "ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef",
    "ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef",
    "ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef",
    "ClientDescribeCertificateResponseCertificateTypeDef",
    "ClientDescribeCertificateResponseTypeDef",
    "ClientExportCertificateResponseTypeDef",
    "ClientGetCertificateResponseTypeDef",
    "ClientImportCertificateResponseTypeDef",
    "ClientImportCertificateTagsTypeDef",
    "ClientListCertificatesIncludesTypeDef",
    "ClientListCertificatesResponseCertificateSummaryListTypeDef",
    "ClientListCertificatesResponseTypeDef",
    "ClientListTagsForCertificateResponseTagsTypeDef",
    "ClientListTagsForCertificateResponseTypeDef",
    "ClientRemoveTagsFromCertificateTagsTypeDef",
    "ClientRequestCertificateDomainValidationOptionsTypeDef",
    "ClientRequestCertificateOptionsTypeDef",
    "ClientRequestCertificateResponseTypeDef",
    "ClientRequestCertificateTagsTypeDef",
    "ClientUpdateCertificateOptionsOptionsTypeDef",
    "FiltersTypeDef",
    "CertificateSummaryTypeDef",
    "ListCertificatesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredClientAddTagsToCertificateTagsTypeDef = TypedDict(
    "_RequiredClientAddTagsToCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientAddTagsToCertificateTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsToCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToCertificateTagsTypeDef(
    _RequiredClientAddTagsToCertificateTagsTypeDef, _OptionalClientAddTagsToCertificateTagsTypeDef
):
    pass


ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef",
    {"Name": str, "Type": str, "Value": str},
    total=False,
)

ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef",
    {
        "DomainName": str,
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": Literal["PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "ResourceRecord": ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef,
        "ValidationMethod": Literal["EMAIL", "DNS"],
    },
    total=False,
)

ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef",
    {
        "Name": Literal[
            "TLS_WEB_SERVER_AUTHENTICATION",
            "TLS_WEB_CLIENT_AUTHENTICATION",
            "CODE_SIGNING",
            "EMAIL_PROTECTION",
            "TIME_STAMPING",
            "OCSP_SIGNING",
            "IPSEC_END_SYSTEM",
            "IPSEC_TUNNEL",
            "IPSEC_USER",
            "ANY",
            "NONE",
            "CUSTOM",
        ],
        "OID": str,
    },
    total=False,
)

ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef",
    {
        "Name": Literal[
            "DIGITAL_SIGNATURE",
            "NON_REPUDIATION",
            "KEY_ENCIPHERMENT",
            "DATA_ENCIPHERMENT",
            "KEY_AGREEMENT",
            "CERTIFICATE_SIGNING",
            "CRL_SIGNING",
            "ENCIPHER_ONLY",
            "DECIPHER_ONLY",
            "ANY",
            "CUSTOM",
        ]
    },
    total=False,
)

ClientDescribeCertificateResponseCertificateOptionsTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef",
    {"Name": str, "Type": str, "Value": str},
    total=False,
)

ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef",
    {
        "DomainName": str,
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": Literal["PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "ResourceRecord": ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef,
        "ValidationMethod": Literal["EMAIL", "DNS"],
    },
    total=False,
)

ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef",
    {
        "RenewalStatus": Literal["PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "DomainValidationOptions": List[
            ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef
        ],
        "RenewalStatusReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "DOMAIN_VALIDATION_DENIED",
            "CAA_ERROR",
            "PCA_LIMIT_EXCEEDED",
            "PCA_INVALID_ARN",
            "PCA_INVALID_STATE",
            "PCA_REQUEST_FAILED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_RESOURCE_NOT_FOUND",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_DURATION",
            "PCA_ACCESS_DENIED",
            "OTHER",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientDescribeCertificateResponseCertificateTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateTypeDef",
    {
        "CertificateArn": str,
        "DomainName": str,
        "SubjectAlternativeNames": List[str],
        "DomainValidationOptions": List[
            ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef
        ],
        "Serial": str,
        "Subject": str,
        "Issuer": str,
        "CreatedAt": datetime,
        "IssuedAt": datetime,
        "ImportedAt": datetime,
        "Status": Literal[
            "PENDING_VALIDATION",
            "ISSUED",
            "INACTIVE",
            "EXPIRED",
            "VALIDATION_TIMED_OUT",
            "REVOKED",
            "FAILED",
        ],
        "RevokedAt": datetime,
        "RevocationReason": Literal[
            "UNSPECIFIED",
            "KEY_COMPROMISE",
            "CA_COMPROMISE",
            "AFFILIATION_CHANGED",
            "SUPERCEDED",
            "CESSATION_OF_OPERATION",
            "CERTIFICATE_HOLD",
            "REMOVE_FROM_CRL",
            "PRIVILEGE_WITHDRAWN",
            "A_A_COMPROMISE",
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "KeyAlgorithm": Literal[
            "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
        ],
        "SignatureAlgorithm": str,
        "InUseBy": List[str],
        "FailureReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "DOMAIN_VALIDATION_DENIED",
            "CAA_ERROR",
            "PCA_LIMIT_EXCEEDED",
            "PCA_INVALID_ARN",
            "PCA_INVALID_STATE",
            "PCA_REQUEST_FAILED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_RESOURCE_NOT_FOUND",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_DURATION",
            "PCA_ACCESS_DENIED",
            "OTHER",
        ],
        "Type": Literal["IMPORTED", "AMAZON_ISSUED", "PRIVATE"],
        "RenewalSummary": ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef,
        "KeyUsages": List[ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef],
        "ExtendedKeyUsages": List[
            ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef
        ],
        "CertificateAuthorityArn": str,
        "RenewalEligibility": Literal["ELIGIBLE", "INELIGIBLE"],
        "Options": ClientDescribeCertificateResponseCertificateOptionsTypeDef,
    },
    total=False,
)

ClientDescribeCertificateResponseTypeDef = TypedDict(
    "ClientDescribeCertificateResponseTypeDef",
    {"Certificate": ClientDescribeCertificateResponseCertificateTypeDef},
    total=False,
)

ClientExportCertificateResponseTypeDef = TypedDict(
    "ClientExportCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str, "PrivateKey": str},
    total=False,
)

ClientGetCertificateResponseTypeDef = TypedDict(
    "ClientGetCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)

ClientImportCertificateResponseTypeDef = TypedDict(
    "ClientImportCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

_RequiredClientImportCertificateTagsTypeDef = TypedDict(
    "_RequiredClientImportCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientImportCertificateTagsTypeDef = TypedDict(
    "_OptionalClientImportCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientImportCertificateTagsTypeDef(
    _RequiredClientImportCertificateTagsTypeDef, _OptionalClientImportCertificateTagsTypeDef
):
    pass


ClientListCertificatesIncludesTypeDef = TypedDict(
    "ClientListCertificatesIncludesTypeDef",
    {
        "extendedKeyUsage": List[
            Literal[
                "TLS_WEB_SERVER_AUTHENTICATION",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "CODE_SIGNING",
                "EMAIL_PROTECTION",
                "TIME_STAMPING",
                "OCSP_SIGNING",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "ANY",
                "NONE",
                "CUSTOM",
            ]
        ],
        "keyUsage": List[
            Literal[
                "DIGITAL_SIGNATURE",
                "NON_REPUDIATION",
                "KEY_ENCIPHERMENT",
                "DATA_ENCIPHERMENT",
                "KEY_AGREEMENT",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "ENCIPHER_ONLY",
                "DECIPHER_ONLY",
                "ANY",
                "CUSTOM",
            ]
        ],
        "keyTypes": List[
            Literal[
                "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
            ]
        ],
    },
    total=False,
)

ClientListCertificatesResponseCertificateSummaryListTypeDef = TypedDict(
    "ClientListCertificatesResponseCertificateSummaryListTypeDef",
    {"CertificateArn": str, "DomainName": str},
    total=False,
)

ClientListCertificatesResponseTypeDef = TypedDict(
    "ClientListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificateSummaryList": List[ClientListCertificatesResponseCertificateSummaryListTypeDef],
    },
    total=False,
)

ClientListTagsForCertificateResponseTagsTypeDef = TypedDict(
    "ClientListTagsForCertificateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForCertificateResponseTypeDef = TypedDict(
    "ClientListTagsForCertificateResponseTypeDef",
    {"Tags": List[ClientListTagsForCertificateResponseTagsTypeDef]},
    total=False,
)

_RequiredClientRemoveTagsFromCertificateTagsTypeDef = TypedDict(
    "_RequiredClientRemoveTagsFromCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsFromCertificateTagsTypeDef = TypedDict(
    "_OptionalClientRemoveTagsFromCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsFromCertificateTagsTypeDef(
    _RequiredClientRemoveTagsFromCertificateTagsTypeDef,
    _OptionalClientRemoveTagsFromCertificateTagsTypeDef,
):
    pass


_RequiredClientRequestCertificateDomainValidationOptionsTypeDef = TypedDict(
    "_RequiredClientRequestCertificateDomainValidationOptionsTypeDef", {"DomainName": str}
)
_OptionalClientRequestCertificateDomainValidationOptionsTypeDef = TypedDict(
    "_OptionalClientRequestCertificateDomainValidationOptionsTypeDef",
    {"ValidationDomain": str},
    total=False,
)


class ClientRequestCertificateDomainValidationOptionsTypeDef(
    _RequiredClientRequestCertificateDomainValidationOptionsTypeDef,
    _OptionalClientRequestCertificateDomainValidationOptionsTypeDef,
):
    pass


ClientRequestCertificateOptionsTypeDef = TypedDict(
    "ClientRequestCertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientRequestCertificateResponseTypeDef = TypedDict(
    "ClientRequestCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

_RequiredClientRequestCertificateTagsTypeDef = TypedDict(
    "_RequiredClientRequestCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientRequestCertificateTagsTypeDef = TypedDict(
    "_OptionalClientRequestCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientRequestCertificateTagsTypeDef(
    _RequiredClientRequestCertificateTagsTypeDef, _OptionalClientRequestCertificateTagsTypeDef
):
    pass


ClientUpdateCertificateOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateCertificateOptionsOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "extendedKeyUsage": List[
            Literal[
                "TLS_WEB_SERVER_AUTHENTICATION",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "CODE_SIGNING",
                "EMAIL_PROTECTION",
                "TIME_STAMPING",
                "OCSP_SIGNING",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "ANY",
                "NONE",
                "CUSTOM",
            ]
        ],
        "keyUsage": List[
            Literal[
                "DIGITAL_SIGNATURE",
                "NON_REPUDIATION",
                "KEY_ENCIPHERMENT",
                "DATA_ENCIPHERMENT",
                "KEY_AGREEMENT",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "ENCIPHER_ONLY",
                "DECIPHER_ONLY",
                "ANY",
                "CUSTOM",
            ]
        ],
        "keyTypes": List[
            Literal[
                "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
            ]
        ],
    },
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef", {"CertificateArn": str, "DomainName": str}, total=False
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {"NextToken": str, "CertificateSummaryList": List[CertificateSummaryTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
