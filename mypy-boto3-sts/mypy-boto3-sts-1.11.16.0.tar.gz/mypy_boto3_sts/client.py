"""
Main interface for sts service client

Usage::

    import boto3
    from mypy_boto3.sts import STSClient

    session = boto3.Session()

    client: STSClient = boto3.client("sts")
    session_client: STSClient = session.client("sts")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sts.client as client_scope
else:
    client_scope = object
from mypy_boto3_sts.type_defs import (
    ClientAssumeRolePolicyArnsTypeDef,
    ClientAssumeRoleResponseTypeDef,
    ClientAssumeRoleTagsTypeDef,
    ClientAssumeRoleWithSamlPolicyArnsTypeDef,
    ClientAssumeRoleWithSamlResponseTypeDef,
    ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef,
    ClientAssumeRoleWithWebIdentityResponseTypeDef,
    ClientDecodeAuthorizationMessageResponseTypeDef,
    ClientGetAccessKeyInfoResponseTypeDef,
    ClientGetCallerIdentityResponseTypeDef,
    ClientGetFederationTokenPolicyArnsTypeDef,
    ClientGetFederationTokenResponseTypeDef,
    ClientGetFederationTokenTagsTypeDef,
    ClientGetSessionTokenResponseTypeDef,
)


__all__ = ("STSClient",)


class STSClient:
    """
    [STS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: List[ClientAssumeRolePolicyArnsTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
        Tags: List[ClientAssumeRoleTagsTypeDef] = None,
        TransitiveTagKeys: List[str] = None,
        ExternalId: str = None,
        SerialNumber: str = None,
        TokenCode: str = None,
    ) -> ClientAssumeRoleResponseTypeDef:
        """
        [Client.assume_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.assume_role)
        """

    def assume_role_with_saml(
        self,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: List[ClientAssumeRoleWithSamlPolicyArnsTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> ClientAssumeRoleWithSamlResponseTypeDef:
        """
        [Client.assume_role_with_saml documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.assume_role_with_saml)
        """

    def assume_role_with_web_identity(
        self,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = None,
        PolicyArns: List[ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> ClientAssumeRoleWithWebIdentityResponseTypeDef:
        """
        [Client.assume_role_with_web_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.assume_role_with_web_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.can_paginate)
        """

    def decode_authorization_message(
        self, EncodedMessage: str
    ) -> ClientDecodeAuthorizationMessageResponseTypeDef:
        """
        [Client.decode_authorization_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.decode_authorization_message)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.generate_presigned_url)
        """

    def get_access_key_info(self, AccessKeyId: str) -> ClientGetAccessKeyInfoResponseTypeDef:
        """
        [Client.get_access_key_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.get_access_key_info)
        """

    def get_caller_identity(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetCallerIdentityResponseTypeDef:
        """
        [Client.get_caller_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.get_caller_identity)
        """

    def get_federation_token(
        self,
        Name: str,
        Policy: str = None,
        PolicyArns: List[ClientGetFederationTokenPolicyArnsTypeDef] = None,
        DurationSeconds: int = None,
        Tags: List[ClientGetFederationTokenTagsTypeDef] = None,
    ) -> ClientGetFederationTokenResponseTypeDef:
        """
        [Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.get_federation_token)
        """

    def get_session_token(
        self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None
    ) -> ClientGetSessionTokenResponseTypeDef:
        """
        [Client.get_session_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sts.html#STS.Client.get_session_token)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    IDPCommunicationErrorException: Boto3ClientError
    IDPRejectedClaimException: Boto3ClientError
    InvalidAuthorizationMessageException: Boto3ClientError
    InvalidIdentityTokenException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    PackedPolicyTooLargeException: Boto3ClientError
    RegionDisabledException: Boto3ClientError
