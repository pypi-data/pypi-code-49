"""
Main interface for secretsmanager service type definitions.

Usage::

    from mypy_boto3.secretsmanager.type_defs import ClientCancelRotateSecretResponseTypeDef

    data: ClientCancelRotateSecretResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCancelRotateSecretResponseTypeDef",
    "ClientCreateSecretResponseTypeDef",
    "ClientCreateSecretTagsTypeDef",
    "ClientDeleteResourcePolicyResponseTypeDef",
    "ClientDeleteSecretResponseTypeDef",
    "ClientDescribeSecretResponseRotationRulesTypeDef",
    "ClientDescribeSecretResponseTagsTypeDef",
    "ClientDescribeSecretResponseTypeDef",
    "ClientGetRandomPasswordResponseTypeDef",
    "ClientGetResourcePolicyResponseTypeDef",
    "ClientGetSecretValueResponseTypeDef",
    "ClientListSecretVersionIdsResponseVersionsTypeDef",
    "ClientListSecretVersionIdsResponseTypeDef",
    "ClientListSecretsResponseSecretListRotationRulesTypeDef",
    "ClientListSecretsResponseSecretListTagsTypeDef",
    "ClientListSecretsResponseSecretListTypeDef",
    "ClientListSecretsResponseTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientPutSecretValueResponseTypeDef",
    "ClientRestoreSecretResponseTypeDef",
    "ClientRotateSecretResponseTypeDef",
    "ClientRotateSecretRotationRulesTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateSecretResponseTypeDef",
    "ClientUpdateSecretVersionStageResponseTypeDef",
    "RotationRulesTypeTypeDef",
    "TagTypeDef",
    "SecretListEntryTypeDef",
    "ListSecretsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCancelRotateSecretResponseTypeDef = TypedDict(
    "ClientCancelRotateSecretResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str},
    total=False,
)

ClientCreateSecretResponseTypeDef = TypedDict(
    "ClientCreateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

ClientCreateSecretTagsTypeDef = TypedDict(
    "ClientCreateSecretTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteResourcePolicyResponseTypeDef = TypedDict(
    "ClientDeleteResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

ClientDeleteSecretResponseTypeDef = TypedDict(
    "ClientDeleteSecretResponseTypeDef",
    {"ARN": str, "Name": str, "DeletionDate": datetime},
    total=False,
)

ClientDescribeSecretResponseRotationRulesTypeDef = TypedDict(
    "ClientDescribeSecretResponseRotationRulesTypeDef", {"AutomaticallyAfterDays": int}, total=False
)

ClientDescribeSecretResponseTagsTypeDef = TypedDict(
    "ClientDescribeSecretResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeSecretResponseTypeDef = TypedDict(
    "ClientDescribeSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ClientDescribeSecretResponseRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ClientDescribeSecretResponseTagsTypeDef],
        "VersionIdsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)

ClientGetRandomPasswordResponseTypeDef = TypedDict(
    "ClientGetRandomPasswordResponseTypeDef", {"RandomPassword": str}, total=False
)

ClientGetResourcePolicyResponseTypeDef = TypedDict(
    "ClientGetResourcePolicyResponseTypeDef",
    {"ARN": str, "Name": str, "ResourcePolicy": str},
    total=False,
)

ClientGetSecretValueResponseTypeDef = TypedDict(
    "ClientGetSecretValueResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "SecretBinary": bytes,
        "SecretString": str,
        "VersionStages": List[str],
        "CreatedDate": datetime,
    },
    total=False,
)

ClientListSecretVersionIdsResponseVersionsTypeDef = TypedDict(
    "ClientListSecretVersionIdsResponseVersionsTypeDef",
    {
        "VersionId": str,
        "VersionStages": List[str],
        "LastAccessedDate": datetime,
        "CreatedDate": datetime,
    },
    total=False,
)

ClientListSecretVersionIdsResponseTypeDef = TypedDict(
    "ClientListSecretVersionIdsResponseTypeDef",
    {
        "Versions": List[ClientListSecretVersionIdsResponseVersionsTypeDef],
        "NextToken": str,
        "ARN": str,
        "Name": str,
    },
    total=False,
)

ClientListSecretsResponseSecretListRotationRulesTypeDef = TypedDict(
    "ClientListSecretsResponseSecretListRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)

ClientListSecretsResponseSecretListTagsTypeDef = TypedDict(
    "ClientListSecretsResponseSecretListTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListSecretsResponseSecretListTypeDef = TypedDict(
    "ClientListSecretsResponseSecretListTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ClientListSecretsResponseSecretListRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ClientListSecretsResponseSecretListTagsTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)

ClientListSecretsResponseTypeDef = TypedDict(
    "ClientListSecretsResponseTypeDef",
    {"SecretList": List[ClientListSecretsResponseSecretListTypeDef], "NextToken": str},
    total=False,
)

ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

ClientPutSecretValueResponseTypeDef = TypedDict(
    "ClientPutSecretValueResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str, "VersionStages": List[str]},
    total=False,
)

ClientRestoreSecretResponseTypeDef = TypedDict(
    "ClientRestoreSecretResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

ClientRotateSecretResponseTypeDef = TypedDict(
    "ClientRotateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

ClientRotateSecretRotationRulesTypeDef = TypedDict(
    "ClientRotateSecretRotationRulesTypeDef", {"AutomaticallyAfterDays": int}, total=False
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateSecretResponseTypeDef = TypedDict(
    "ClientUpdateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)

ClientUpdateSecretVersionStageResponseTypeDef = TypedDict(
    "ClientUpdateSecretVersionStageResponseTypeDef", {"ARN": str, "Name": str}, total=False
)

RotationRulesTypeTypeDef = TypedDict(
    "RotationRulesTypeTypeDef", {"AutomaticallyAfterDays": int}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

SecretListEntryTypeDef = TypedDict(
    "SecretListEntryTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": RotationRulesTypeTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[TagTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)

ListSecretsResponseTypeDef = TypedDict(
    "ListSecretsResponseTypeDef",
    {"SecretList": List[SecretListEntryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
