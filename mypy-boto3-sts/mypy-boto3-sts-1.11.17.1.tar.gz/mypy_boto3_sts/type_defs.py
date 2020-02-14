"""
Main interface for sts service type definitions.

Usage::

    from mypy_boto3.sts.type_defs import ClientAssumeRolePolicyArnsTypeDef

    data: ClientAssumeRolePolicyArnsTypeDef = {...}
"""
from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAssumeRolePolicyArnsTypeDef",
    "ClientAssumeRoleResponseAssumedRoleUserTypeDef",
    "ClientAssumeRoleResponseCredentialsTypeDef",
    "ClientAssumeRoleResponseTypeDef",
    "ClientAssumeRoleTagsTypeDef",
    "ClientAssumeRoleWithSamlPolicyArnsTypeDef",
    "ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef",
    "ClientAssumeRoleWithSamlResponseCredentialsTypeDef",
    "ClientAssumeRoleWithSamlResponseTypeDef",
    "ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef",
    "ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef",
    "ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef",
    "ClientAssumeRoleWithWebIdentityResponseTypeDef",
    "ClientDecodeAuthorizationMessageResponseTypeDef",
    "ClientGetAccessKeyInfoResponseTypeDef",
    "ClientGetCallerIdentityResponseTypeDef",
    "ClientGetFederationTokenPolicyArnsTypeDef",
    "ClientGetFederationTokenResponseCredentialsTypeDef",
    "ClientGetFederationTokenResponseFederatedUserTypeDef",
    "ClientGetFederationTokenResponseTypeDef",
    "ClientGetFederationTokenTagsTypeDef",
    "ClientGetSessionTokenResponseCredentialsTypeDef",
    "ClientGetSessionTokenResponseTypeDef",
)

ClientAssumeRolePolicyArnsTypeDef = TypedDict(
    "ClientAssumeRolePolicyArnsTypeDef", {"arn": str}, total=False
)

ClientAssumeRoleResponseAssumedRoleUserTypeDef = TypedDict(
    "ClientAssumeRoleResponseAssumedRoleUserTypeDef",
    {"AssumedRoleId": str, "Arn": str},
    total=False,
)

ClientAssumeRoleResponseCredentialsTypeDef = TypedDict(
    "ClientAssumeRoleResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)

ClientAssumeRoleResponseTypeDef = TypedDict(
    "ClientAssumeRoleResponseTypeDef",
    {
        "Credentials": ClientAssumeRoleResponseCredentialsTypeDef,
        "AssumedRoleUser": ClientAssumeRoleResponseAssumedRoleUserTypeDef,
        "PackedPolicySize": int,
    },
    total=False,
)

ClientAssumeRoleTagsTypeDef = TypedDict(
    "ClientAssumeRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAssumeRoleWithSamlPolicyArnsTypeDef = TypedDict(
    "ClientAssumeRoleWithSamlPolicyArnsTypeDef", {"arn": str}, total=False
)

ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef = TypedDict(
    "ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef",
    {"AssumedRoleId": str, "Arn": str},
    total=False,
)

ClientAssumeRoleWithSamlResponseCredentialsTypeDef = TypedDict(
    "ClientAssumeRoleWithSamlResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)

ClientAssumeRoleWithSamlResponseTypeDef = TypedDict(
    "ClientAssumeRoleWithSamlResponseTypeDef",
    {
        "Credentials": ClientAssumeRoleWithSamlResponseCredentialsTypeDef,
        "AssumedRoleUser": ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "Subject": str,
        "SubjectType": str,
        "Issuer": str,
        "Audience": str,
        "NameQualifier": str,
    },
    total=False,
)

ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef = TypedDict(
    "ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef", {"arn": str}, total=False
)

ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef = TypedDict(
    "ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef",
    {"AssumedRoleId": str, "Arn": str},
    total=False,
)

ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef = TypedDict(
    "ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)

ClientAssumeRoleWithWebIdentityResponseTypeDef = TypedDict(
    "ClientAssumeRoleWithWebIdentityResponseTypeDef",
    {
        "Credentials": ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef,
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
    },
    total=False,
)

ClientDecodeAuthorizationMessageResponseTypeDef = TypedDict(
    "ClientDecodeAuthorizationMessageResponseTypeDef", {"DecodedMessage": str}, total=False
)

ClientGetAccessKeyInfoResponseTypeDef = TypedDict(
    "ClientGetAccessKeyInfoResponseTypeDef", {"Account": str}, total=False
)

ClientGetCallerIdentityResponseTypeDef = TypedDict(
    "ClientGetCallerIdentityResponseTypeDef",
    {"UserId": str, "Account": str, "Arn": str},
    total=False,
)

ClientGetFederationTokenPolicyArnsTypeDef = TypedDict(
    "ClientGetFederationTokenPolicyArnsTypeDef", {"arn": str}, total=False
)

ClientGetFederationTokenResponseCredentialsTypeDef = TypedDict(
    "ClientGetFederationTokenResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)

ClientGetFederationTokenResponseFederatedUserTypeDef = TypedDict(
    "ClientGetFederationTokenResponseFederatedUserTypeDef",
    {"FederatedUserId": str, "Arn": str},
    total=False,
)

ClientGetFederationTokenResponseTypeDef = TypedDict(
    "ClientGetFederationTokenResponseTypeDef",
    {
        "Credentials": ClientGetFederationTokenResponseCredentialsTypeDef,
        "FederatedUser": ClientGetFederationTokenResponseFederatedUserTypeDef,
        "PackedPolicySize": int,
    },
    total=False,
)

ClientGetFederationTokenTagsTypeDef = TypedDict(
    "ClientGetFederationTokenTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetSessionTokenResponseCredentialsTypeDef = TypedDict(
    "ClientGetSessionTokenResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)

ClientGetSessionTokenResponseTypeDef = TypedDict(
    "ClientGetSessionTokenResponseTypeDef",
    {"Credentials": ClientGetSessionTokenResponseCredentialsTypeDef},
    total=False,
)
