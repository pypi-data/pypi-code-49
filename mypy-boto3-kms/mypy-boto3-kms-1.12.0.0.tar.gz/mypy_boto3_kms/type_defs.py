"""
Main interface for kms service type definitions.

Usage::

    from mypy_boto3.kms.type_defs import ClientCancelKeyDeletionResponseTypeDef

    data: ClientCancelKeyDeletionResponseTypeDef = {...}
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
    "ClientCancelKeyDeletionResponseTypeDef",
    "ClientCreateCustomKeyStoreResponseTypeDef",
    "ClientCreateGrantConstraintsTypeDef",
    "ClientCreateGrantResponseTypeDef",
    "ClientCreateKeyResponseKeyMetadataTypeDef",
    "ClientCreateKeyResponseTypeDef",
    "ClientCreateKeyTagsTypeDef",
    "ClientDecryptResponseTypeDef",
    "ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef",
    "ClientDescribeCustomKeyStoresResponseTypeDef",
    "ClientDescribeKeyResponseKeyMetadataTypeDef",
    "ClientDescribeKeyResponseTypeDef",
    "ClientEncryptResponseTypeDef",
    "ClientGenerateDataKeyPairResponseTypeDef",
    "ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "ClientGenerateDataKeyResponseTypeDef",
    "ClientGenerateDataKeyWithoutPlaintextResponseTypeDef",
    "ClientGenerateRandomResponseTypeDef",
    "ClientGetKeyPolicyResponseTypeDef",
    "ClientGetKeyRotationStatusResponseTypeDef",
    "ClientGetParametersForImportResponseTypeDef",
    "ClientGetPublicKeyResponseTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListGrantsResponseGrantsConstraintsTypeDef",
    "ClientListGrantsResponseGrantsTypeDef",
    "ClientListGrantsResponseTypeDef",
    "ClientListKeyPoliciesResponseTypeDef",
    "ClientListKeysResponseKeysTypeDef",
    "ClientListKeysResponseTypeDef",
    "ClientListResourceTagsResponseTagsTypeDef",
    "ClientListResourceTagsResponseTypeDef",
    "ClientListRetirableGrantsResponseGrantsConstraintsTypeDef",
    "ClientListRetirableGrantsResponseGrantsTypeDef",
    "ClientListRetirableGrantsResponseTypeDef",
    "ClientReEncryptResponseTypeDef",
    "ClientScheduleKeyDeletionResponseTypeDef",
    "ClientSignResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientVerifyResponseTypeDef",
    "AliasListEntryTypeDef",
    "ListAliasesResponseTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "KeyListEntryTypeDef",
    "ListKeysResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCancelKeyDeletionResponseTypeDef = TypedDict(
    "ClientCancelKeyDeletionResponseTypeDef", {"KeyId": str}, total=False
)

ClientCreateCustomKeyStoreResponseTypeDef = TypedDict(
    "ClientCreateCustomKeyStoreResponseTypeDef", {"CustomKeyStoreId": str}, total=False
)

ClientCreateGrantConstraintsTypeDef = TypedDict(
    "ClientCreateGrantConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)

ClientCreateGrantResponseTypeDef = TypedDict(
    "ClientCreateGrantResponseTypeDef", {"GrantToken": str, "GrantId": str}, total=False
)

ClientCreateKeyResponseKeyMetadataTypeDef = TypedDict(
    "ClientCreateKeyResponseKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "KeyId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "KeyState": Literal[
            "Enabled", "Disabled", "PendingDeletion", "PendingImport", "Unavailable"
        ],
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"],
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"],
        "KeyManager": Literal["AWS", "CUSTOMER"],
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)

ClientCreateKeyResponseTypeDef = TypedDict(
    "ClientCreateKeyResponseTypeDef",
    {"KeyMetadata": ClientCreateKeyResponseKeyMetadataTypeDef},
    total=False,
)

_RequiredClientCreateKeyTagsTypeDef = TypedDict(
    "_RequiredClientCreateKeyTagsTypeDef", {"TagKey": str}
)
_OptionalClientCreateKeyTagsTypeDef = TypedDict(
    "_OptionalClientCreateKeyTagsTypeDef", {"TagValue": str}, total=False
)


class ClientCreateKeyTagsTypeDef(
    _RequiredClientCreateKeyTagsTypeDef, _OptionalClientCreateKeyTagsTypeDef
):
    pass


ClientDecryptResponseTypeDef = TypedDict(
    "ClientDecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": bytes,
        "EncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)

ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef = TypedDict(
    "ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": Literal[
            "CONNECTED", "CONNECTING", "FAILED", "DISCONNECTED", "DISCONNECTING"
        ],
        "ConnectionErrorCode": Literal[
            "INVALID_CREDENTIALS",
            "CLUSTER_NOT_FOUND",
            "NETWORK_ERRORS",
            "INTERNAL_ERROR",
            "INSUFFICIENT_CLOUDHSM_HSMS",
            "USER_LOCKED_OUT",
            "USER_NOT_FOUND",
            "USER_LOGGED_IN",
            "SUBNET_NOT_FOUND",
        ],
        "CreationDate": datetime,
    },
    total=False,
)

ClientDescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "ClientDescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List[ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)

ClientDescribeKeyResponseKeyMetadataTypeDef = TypedDict(
    "ClientDescribeKeyResponseKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "KeyId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "KeyState": Literal[
            "Enabled", "Disabled", "PendingDeletion", "PendingImport", "Unavailable"
        ],
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"],
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"],
        "KeyManager": Literal["AWS", "CUSTOMER"],
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)

ClientDescribeKeyResponseTypeDef = TypedDict(
    "ClientDescribeKeyResponseTypeDef",
    {"KeyMetadata": ClientDescribeKeyResponseKeyMetadataTypeDef},
    total=False,
)

ClientEncryptResponseTypeDef = TypedDict(
    "ClientEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "EncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)

ClientGenerateDataKeyPairResponseTypeDef = TypedDict(
    "ClientGenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PrivateKeyPlaintext": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
    },
    total=False,
)

ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
    },
    total=False,
)

ClientGenerateDataKeyResponseTypeDef = TypedDict(
    "ClientGenerateDataKeyResponseTypeDef",
    {"CiphertextBlob": bytes, "Plaintext": bytes, "KeyId": str},
    total=False,
)

ClientGenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "ClientGenerateDataKeyWithoutPlaintextResponseTypeDef",
    {"CiphertextBlob": bytes, "KeyId": str},
    total=False,
)

ClientGenerateRandomResponseTypeDef = TypedDict(
    "ClientGenerateRandomResponseTypeDef", {"Plaintext": bytes}, total=False
)

ClientGetKeyPolicyResponseTypeDef = TypedDict(
    "ClientGetKeyPolicyResponseTypeDef", {"Policy": str}, total=False
)

ClientGetKeyRotationStatusResponseTypeDef = TypedDict(
    "ClientGetKeyRotationStatusResponseTypeDef", {"KeyRotationEnabled": bool}, total=False
)

ClientGetParametersForImportResponseTypeDef = TypedDict(
    "ClientGetParametersForImportResponseTypeDef",
    {"KeyId": str, "ImportToken": bytes, "PublicKey": bytes, "ParametersValidTo": datetime},
    total=False,
)

ClientGetPublicKeyResponseTypeDef = TypedDict(
    "ClientGetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": bytes,
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)

ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "ClientListAliasesResponseAliasesTypeDef",
    {"AliasName": str, "AliasArn": str, "TargetKeyId": str},
    total=False,
)

ClientListAliasesResponseTypeDef = TypedDict(
    "ClientListAliasesResponseTypeDef",
    {
        "Aliases": List[ClientListAliasesResponseAliasesTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)

ClientListGrantsResponseGrantsConstraintsTypeDef = TypedDict(
    "ClientListGrantsResponseGrantsConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)

ClientListGrantsResponseGrantsTypeDef = TypedDict(
    "ClientListGrantsResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": ClientListGrantsResponseGrantsConstraintsTypeDef,
    },
    total=False,
)

ClientListGrantsResponseTypeDef = TypedDict(
    "ClientListGrantsResponseTypeDef",
    {"Grants": List[ClientListGrantsResponseGrantsTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)

ClientListKeyPoliciesResponseTypeDef = TypedDict(
    "ClientListKeyPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "NextMarker": str, "Truncated": bool},
    total=False,
)

ClientListKeysResponseKeysTypeDef = TypedDict(
    "ClientListKeysResponseKeysTypeDef", {"KeyId": str, "KeyArn": str}, total=False
)

ClientListKeysResponseTypeDef = TypedDict(
    "ClientListKeysResponseTypeDef",
    {"Keys": List[ClientListKeysResponseKeysTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)

ClientListResourceTagsResponseTagsTypeDef = TypedDict(
    "ClientListResourceTagsResponseTagsTypeDef", {"TagKey": str, "TagValue": str}, total=False
)

ClientListResourceTagsResponseTypeDef = TypedDict(
    "ClientListResourceTagsResponseTypeDef",
    {"Tags": List[ClientListResourceTagsResponseTagsTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)

ClientListRetirableGrantsResponseGrantsConstraintsTypeDef = TypedDict(
    "ClientListRetirableGrantsResponseGrantsConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)

ClientListRetirableGrantsResponseGrantsTypeDef = TypedDict(
    "ClientListRetirableGrantsResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": ClientListRetirableGrantsResponseGrantsConstraintsTypeDef,
    },
    total=False,
)

ClientListRetirableGrantsResponseTypeDef = TypedDict(
    "ClientListRetirableGrantsResponseTypeDef",
    {
        "Grants": List[ClientListRetirableGrantsResponseGrantsTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)

ClientReEncryptResponseTypeDef = TypedDict(
    "ClientReEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
        "DestinationEncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)

ClientScheduleKeyDeletionResponseTypeDef = TypedDict(
    "ClientScheduleKeyDeletionResponseTypeDef",
    {"KeyId": str, "DeletionDate": datetime},
    total=False,
)

ClientSignResponseTypeDef = TypedDict(
    "ClientSignResponseTypeDef",
    {
        "KeyId": str,
        "Signature": bytes,
        "SigningAlgorithm": Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
    },
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"TagKey": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"TagValue": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientVerifyResponseTypeDef = TypedDict(
    "ClientVerifyResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
    },
    total=False,
)

AliasListEntryTypeDef = TypedDict(
    "AliasListEntryTypeDef", {"AliasName": str, "AliasArn": str, "TargetKeyId": str}, total=False
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {"Aliases": List[AliasListEntryTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)

GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)

GrantListEntryTypeDef = TypedDict(
    "GrantListEntryTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": GrantConstraintsTypeDef,
    },
    total=False,
)

ListGrantsResponseTypeDef = TypedDict(
    "ListGrantsResponseTypeDef",
    {"Grants": List[GrantListEntryTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListKeyPoliciesResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "NextMarker": str, "Truncated": bool},
    total=False,
)

KeyListEntryTypeDef = TypedDict("KeyListEntryTypeDef", {"KeyId": str, "KeyArn": str}, total=False)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {"Keys": List[KeyListEntryTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
