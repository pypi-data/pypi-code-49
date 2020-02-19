"""
Main interface for cognito-idp service type definitions.

Usage::

    from mypy_boto3.cognito_idp.type_defs import GroupTypeTypeDef

    data: GroupTypeTypeDef = {...}
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
    "GroupTypeTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "ChallengeResponseTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef",
    "ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef",
    "ClientAddCustomAttributesCustomAttributesTypeDef",
    "ClientAdminCreateUserResponseUserAttributesTypeDef",
    "ClientAdminCreateUserResponseUserMFAOptionsTypeDef",
    "ClientAdminCreateUserResponseUserTypeDef",
    "ClientAdminCreateUserResponseTypeDef",
    "ClientAdminCreateUserUserAttributesTypeDef",
    "ClientAdminCreateUserValidationDataTypeDef",
    "ClientAdminDisableProviderForUserUserTypeDef",
    "ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef",
    "ClientAdminGetDeviceResponseDeviceTypeDef",
    "ClientAdminGetDeviceResponseTypeDef",
    "ClientAdminGetUserResponseMFAOptionsTypeDef",
    "ClientAdminGetUserResponseUserAttributesTypeDef",
    "ClientAdminGetUserResponseTypeDef",
    "ClientAdminInitiateAuthAnalyticsMetadataTypeDef",
    "ClientAdminInitiateAuthContextDataHttpHeadersTypeDef",
    "ClientAdminInitiateAuthContextDataTypeDef",
    "ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientAdminInitiateAuthResponseAuthenticationResultTypeDef",
    "ClientAdminInitiateAuthResponseTypeDef",
    "ClientAdminLinkProviderForUserDestinationUserTypeDef",
    "ClientAdminLinkProviderForUserSourceUserTypeDef",
    "ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef",
    "ClientAdminListDevicesResponseDevicesTypeDef",
    "ClientAdminListDevicesResponseTypeDef",
    "ClientAdminListGroupsForUserResponseGroupsTypeDef",
    "ClientAdminListGroupsForUserResponseTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsTypeDef",
    "ClientAdminListUserAuthEventsResponseTypeDef",
    "ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef",
    "ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef",
    "ClientAdminRespondToAuthChallengeContextDataTypeDef",
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    "ClientAdminRespondToAuthChallengeResponseTypeDef",
    "ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    "ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    "ClientAdminSetUserSettingsMFAOptionsTypeDef",
    "ClientAdminUpdateUserAttributesUserAttributesTypeDef",
    "ClientAssociateSoftwareTokenResponseTypeDef",
    "ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef",
    "ClientConfirmDeviceResponseTypeDef",
    "ClientConfirmForgotPasswordAnalyticsMetadataTypeDef",
    "ClientConfirmForgotPasswordUserContextDataTypeDef",
    "ClientConfirmSignUpAnalyticsMetadataTypeDef",
    "ClientConfirmSignUpUserContextDataTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateIdentityProviderResponseIdentityProviderTypeDef",
    "ClientCreateIdentityProviderResponseTypeDef",
    "ClientCreateResourceServerResponseResourceServerScopesTypeDef",
    "ClientCreateResourceServerResponseResourceServerTypeDef",
    "ClientCreateResourceServerResponseTypeDef",
    "ClientCreateResourceServerScopesTypeDef",
    "ClientCreateUserImportJobResponseUserImportJobTypeDef",
    "ClientCreateUserImportJobResponseTypeDef",
    "ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientCreateUserPoolAccountRecoverySettingTypeDef",
    "ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientCreateUserPoolAdminCreateUserConfigTypeDef",
    "ClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientCreateUserPoolClientResponseUserPoolClientTypeDef",
    "ClientCreateUserPoolClientResponseTypeDef",
    "ClientCreateUserPoolDeviceConfigurationTypeDef",
    "ClientCreateUserPoolDomainCustomDomainConfigTypeDef",
    "ClientCreateUserPoolDomainResponseTypeDef",
    "ClientCreateUserPoolEmailConfigurationTypeDef",
    "ClientCreateUserPoolLambdaConfigTypeDef",
    "ClientCreateUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientCreateUserPoolPoliciesTypeDef",
    "ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    "ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef",
    "ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientCreateUserPoolResponseUserPoolPoliciesTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef",
    "ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    "ClientCreateUserPoolResponseUserPoolUsernameConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    "ClientCreateUserPoolResponseUserPoolTypeDef",
    "ClientCreateUserPoolResponseTypeDef",
    "ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef",
    "ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef",
    "ClientCreateUserPoolSchemaTypeDef",
    "ClientCreateUserPoolSmsConfigurationTypeDef",
    "ClientCreateUserPoolUserPoolAddOnsTypeDef",
    "ClientCreateUserPoolUsernameConfigurationTypeDef",
    "ClientCreateUserPoolVerificationMessageTemplateTypeDef",
    "ClientDescribeIdentityProviderResponseIdentityProviderTypeDef",
    "ClientDescribeIdentityProviderResponseTypeDef",
    "ClientDescribeResourceServerResponseResourceServerScopesTypeDef",
    "ClientDescribeResourceServerResponseResourceServerTypeDef",
    "ClientDescribeResourceServerResponseTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseTypeDef",
    "ClientDescribeUserImportJobResponseUserImportJobTypeDef",
    "ClientDescribeUserImportJobResponseTypeDef",
    "ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientDescribeUserPoolClientResponseUserPoolClientTypeDef",
    "ClientDescribeUserPoolClientResponseTypeDef",
    "ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef",
    "ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef",
    "ClientDescribeUserPoolDomainResponseTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    "ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef",
    "ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolUsernameConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    "ClientDescribeUserPoolResponseUserPoolTypeDef",
    "ClientDescribeUserPoolResponseTypeDef",
    "ClientForgotPasswordAnalyticsMetadataTypeDef",
    "ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef",
    "ClientForgotPasswordResponseTypeDef",
    "ClientForgotPasswordUserContextDataTypeDef",
    "ClientGetCsvHeaderResponseTypeDef",
    "ClientGetDeviceResponseDeviceDeviceAttributesTypeDef",
    "ClientGetDeviceResponseDeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef",
    "ClientGetIdentityProviderByIdentifierResponseTypeDef",
    "ClientGetSigningCertificateResponseTypeDef",
    "ClientGetUiCustomizationResponseUICustomizationTypeDef",
    "ClientGetUiCustomizationResponseTypeDef",
    "ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef",
    "ClientGetUserAttributeVerificationCodeResponseTypeDef",
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseTypeDef",
    "ClientGetUserResponseMFAOptionsTypeDef",
    "ClientGetUserResponseUserAttributesTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientInitiateAuthAnalyticsMetadataTypeDef",
    "ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientInitiateAuthResponseAuthenticationResultTypeDef",
    "ClientInitiateAuthResponseTypeDef",
    "ClientInitiateAuthUserContextDataTypeDef",
    "ClientListDevicesResponseDevicesDeviceAttributesTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListIdentityProvidersResponseProvidersTypeDef",
    "ClientListIdentityProvidersResponseTypeDef",
    "ClientListResourceServersResponseResourceServersScopesTypeDef",
    "ClientListResourceServersResponseResourceServersTypeDef",
    "ClientListResourceServersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUserImportJobsResponseUserImportJobsTypeDef",
    "ClientListUserImportJobsResponseTypeDef",
    "ClientListUserPoolClientsResponseUserPoolClientsTypeDef",
    "ClientListUserPoolClientsResponseTypeDef",
    "ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef",
    "ClientListUserPoolsResponseUserPoolsTypeDef",
    "ClientListUserPoolsResponseTypeDef",
    "ClientListUsersInGroupResponseUsersAttributesTypeDef",
    "ClientListUsersInGroupResponseUsersMFAOptionsTypeDef",
    "ClientListUsersInGroupResponseUsersTypeDef",
    "ClientListUsersInGroupResponseTypeDef",
    "ClientListUsersResponseUsersAttributesTypeDef",
    "ClientListUsersResponseUsersMFAOptionsTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientResendConfirmationCodeAnalyticsMetadataTypeDef",
    "ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef",
    "ClientResendConfirmationCodeResponseTypeDef",
    "ClientResendConfirmationCodeUserContextDataTypeDef",
    "ClientRespondToAuthChallengeAnalyticsMetadataTypeDef",
    "ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    "ClientRespondToAuthChallengeResponseTypeDef",
    "ClientRespondToAuthChallengeUserContextDataTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseTypeDef",
    "ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientSetUiCustomizationResponseUICustomizationTypeDef",
    "ClientSetUiCustomizationResponseTypeDef",
    "ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    "ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseTypeDef",
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef",
    "ClientSetUserSettingsMFAOptionsTypeDef",
    "ClientSignUpAnalyticsMetadataTypeDef",
    "ClientSignUpResponseCodeDeliveryDetailsTypeDef",
    "ClientSignUpResponseTypeDef",
    "ClientSignUpUserAttributesTypeDef",
    "ClientSignUpUserContextDataTypeDef",
    "ClientSignUpValidationDataTypeDef",
    "ClientStartUserImportJobResponseUserImportJobTypeDef",
    "ClientStartUserImportJobResponseTypeDef",
    "ClientStopUserImportJobResponseUserImportJobTypeDef",
    "ClientStopUserImportJobResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateIdentityProviderResponseIdentityProviderTypeDef",
    "ClientUpdateIdentityProviderResponseTypeDef",
    "ClientUpdateResourceServerResponseResourceServerScopesTypeDef",
    "ClientUpdateResourceServerResponseResourceServerTypeDef",
    "ClientUpdateResourceServerResponseTypeDef",
    "ClientUpdateResourceServerScopesTypeDef",
    "ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef",
    "ClientUpdateUserAttributesResponseTypeDef",
    "ClientUpdateUserAttributesUserAttributesTypeDef",
    "ClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientUpdateUserPoolAccountRecoverySettingTypeDef",
    "ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientUpdateUserPoolAdminCreateUserConfigTypeDef",
    "ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientUpdateUserPoolClientResponseUserPoolClientTypeDef",
    "ClientUpdateUserPoolClientResponseTypeDef",
    "ClientUpdateUserPoolDeviceConfigurationTypeDef",
    "ClientUpdateUserPoolDomainCustomDomainConfigTypeDef",
    "ClientUpdateUserPoolDomainResponseTypeDef",
    "ClientUpdateUserPoolEmailConfigurationTypeDef",
    "ClientUpdateUserPoolLambdaConfigTypeDef",
    "ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientUpdateUserPoolPoliciesTypeDef",
    "ClientUpdateUserPoolSmsConfigurationTypeDef",
    "ClientUpdateUserPoolUserPoolAddOnsTypeDef",
    "ClientUpdateUserPoolVerificationMessageTemplateTypeDef",
    "ClientVerifySoftwareTokenResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ProviderDescriptionTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "ListResourceServersResponseTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "ListUserPoolsResponseTypeDef",
    "AttributeTypeTypeDef",
    "MFAOptionTypeTypeDef",
    "UserTypeTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {"Groups": List[GroupTypeTypeDef], "NextToken": str},
    total=False,
)

ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {
        "ChallengeName": Literal["Password", "Mfa"],
        "ChallengeResponse": Literal["Success", "Failure"],
    },
    total=False,
)

EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)

_RequiredEventFeedbackTypeTypeDef = TypedDict(
    "_RequiredEventFeedbackTypeTypeDef",
    {"FeedbackValue": Literal["Valid", "Invalid"], "Provider": str},
)
_OptionalEventFeedbackTypeTypeDef = TypedDict(
    "_OptionalEventFeedbackTypeTypeDef", {"FeedbackDate": datetime}, total=False
)


class EventFeedbackTypeTypeDef(
    _RequiredEventFeedbackTypeTypeDef, _OptionalEventFeedbackTypeTypeDef
):
    pass


EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": Literal["NoRisk", "AccountTakeover", "Block"],
        "RiskLevel": Literal["Low", "Medium", "High"],
    },
    total=False,
)

AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": str,
        "EventType": Literal["SignIn", "SignUp", "ForgotPassword"],
        "CreationDate": datetime,
        "EventResponse": Literal["Success", "Failure"],
        "EventRisk": EventRiskTypeTypeDef,
        "ChallengeResponses": List[ChallengeResponseTypeTypeDef],
        "EventContextData": EventContextDataTypeTypeDef,
        "EventFeedback": EventFeedbackTypeTypeDef,
    },
    total=False,
)

AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {"AuthEvents": List[AuthEventTypeTypeDef], "NextToken": str},
    total=False,
)

ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)

ClientAddCustomAttributesCustomAttributesTypeDef = TypedDict(
    "ClientAddCustomAttributesCustomAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)

ClientAdminCreateUserResponseUserAttributesTypeDef = TypedDict(
    "ClientAdminCreateUserResponseUserAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientAdminCreateUserResponseUserMFAOptionsTypeDef = TypedDict(
    "ClientAdminCreateUserResponseUserMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientAdminCreateUserResponseUserTypeDef = TypedDict(
    "ClientAdminCreateUserResponseUserTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientAdminCreateUserResponseUserAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientAdminCreateUserResponseUserMFAOptionsTypeDef],
    },
    total=False,
)

ClientAdminCreateUserResponseTypeDef = TypedDict(
    "ClientAdminCreateUserResponseTypeDef",
    {"User": ClientAdminCreateUserResponseUserTypeDef},
    total=False,
)

_RequiredClientAdminCreateUserUserAttributesTypeDef = TypedDict(
    "_RequiredClientAdminCreateUserUserAttributesTypeDef", {"Name": str}
)
_OptionalClientAdminCreateUserUserAttributesTypeDef = TypedDict(
    "_OptionalClientAdminCreateUserUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientAdminCreateUserUserAttributesTypeDef(
    _RequiredClientAdminCreateUserUserAttributesTypeDef,
    _OptionalClientAdminCreateUserUserAttributesTypeDef,
):
    pass


_RequiredClientAdminCreateUserValidationDataTypeDef = TypedDict(
    "_RequiredClientAdminCreateUserValidationDataTypeDef", {"Name": str}
)
_OptionalClientAdminCreateUserValidationDataTypeDef = TypedDict(
    "_OptionalClientAdminCreateUserValidationDataTypeDef", {"Value": str}, total=False
)


class ClientAdminCreateUserValidationDataTypeDef(
    _RequiredClientAdminCreateUserValidationDataTypeDef,
    _OptionalClientAdminCreateUserValidationDataTypeDef,
):
    pass


ClientAdminDisableProviderForUserUserTypeDef = TypedDict(
    "ClientAdminDisableProviderForUserUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)

ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef = TypedDict(
    "ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientAdminGetDeviceResponseDeviceTypeDef = TypedDict(
    "ClientAdminGetDeviceResponseDeviceTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

ClientAdminGetDeviceResponseTypeDef = TypedDict(
    "ClientAdminGetDeviceResponseTypeDef",
    {"Device": ClientAdminGetDeviceResponseDeviceTypeDef},
    total=False,
)

ClientAdminGetUserResponseMFAOptionsTypeDef = TypedDict(
    "ClientAdminGetUserResponseMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientAdminGetUserResponseUserAttributesTypeDef = TypedDict(
    "ClientAdminGetUserResponseUserAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientAdminGetUserResponseTypeDef = TypedDict(
    "ClientAdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[ClientAdminGetUserResponseUserAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientAdminGetUserResponseMFAOptionsTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)

ClientAdminInitiateAuthAnalyticsMetadataTypeDef = TypedDict(
    "ClientAdminInitiateAuthAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)

ClientAdminInitiateAuthContextDataHttpHeadersTypeDef = TypedDict(
    "ClientAdminInitiateAuthContextDataHttpHeadersTypeDef",
    {"headerName": str, "headerValue": str},
    total=False,
)

_RequiredClientAdminInitiateAuthContextDataTypeDef = TypedDict(
    "_RequiredClientAdminInitiateAuthContextDataTypeDef", {"IpAddress": str}
)
_OptionalClientAdminInitiateAuthContextDataTypeDef = TypedDict(
    "_OptionalClientAdminInitiateAuthContextDataTypeDef",
    {
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List[ClientAdminInitiateAuthContextDataHttpHeadersTypeDef],
        "EncodedData": str,
    },
    total=False,
)


class ClientAdminInitiateAuthContextDataTypeDef(
    _RequiredClientAdminInitiateAuthContextDataTypeDef,
    _OptionalClientAdminInitiateAuthContextDataTypeDef,
):
    pass


ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)

ClientAdminInitiateAuthResponseAuthenticationResultTypeDef = TypedDict(
    "ClientAdminInitiateAuthResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)

ClientAdminInitiateAuthResponseTypeDef = TypedDict(
    "ClientAdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": Literal[
            "SMS_MFA",
            "SOFTWARE_TOKEN_MFA",
            "SELECT_MFA_TYPE",
            "MFA_SETUP",
            "PASSWORD_VERIFIER",
            "CUSTOM_CHALLENGE",
            "DEVICE_SRP_AUTH",
            "DEVICE_PASSWORD_VERIFIER",
            "ADMIN_NO_SRP_AUTH",
            "NEW_PASSWORD_REQUIRED",
        ],
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientAdminInitiateAuthResponseAuthenticationResultTypeDef,
    },
    total=False,
)

ClientAdminLinkProviderForUserDestinationUserTypeDef = TypedDict(
    "ClientAdminLinkProviderForUserDestinationUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)

ClientAdminLinkProviderForUserSourceUserTypeDef = TypedDict(
    "ClientAdminLinkProviderForUserSourceUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)

ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef = TypedDict(
    "ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientAdminListDevicesResponseDevicesTypeDef = TypedDict(
    "ClientAdminListDevicesResponseDevicesTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

ClientAdminListDevicesResponseTypeDef = TypedDict(
    "ClientAdminListDevicesResponseTypeDef",
    {"Devices": List[ClientAdminListDevicesResponseDevicesTypeDef], "PaginationToken": str},
    total=False,
)

ClientAdminListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "ClientAdminListGroupsForUserResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientAdminListGroupsForUserResponseTypeDef = TypedDict(
    "ClientAdminListGroupsForUserResponseTypeDef",
    {"Groups": List[ClientAdminListGroupsForUserResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef = TypedDict(
    "ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef",
    {
        "ChallengeName": Literal["Password", "Mfa"],
        "ChallengeResponse": Literal["Success", "Failure"],
    },
    total=False,
)

ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef = TypedDict(
    "ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)

ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef = TypedDict(
    "ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef",
    {"FeedbackValue": Literal["Valid", "Invalid"], "Provider": str, "FeedbackDate": datetime},
    total=False,
)

ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef = TypedDict(
    "ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef",
    {
        "RiskDecision": Literal["NoRisk", "AccountTakeover", "Block"],
        "RiskLevel": Literal["Low", "Medium", "High"],
    },
    total=False,
)

ClientAdminListUserAuthEventsResponseAuthEventsTypeDef = TypedDict(
    "ClientAdminListUserAuthEventsResponseAuthEventsTypeDef",
    {
        "EventId": str,
        "EventType": Literal["SignIn", "SignUp", "ForgotPassword"],
        "CreationDate": datetime,
        "EventResponse": Literal["Success", "Failure"],
        "EventRisk": ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef,
        "ChallengeResponses": List[
            ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef
        ],
        "EventContextData": ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef,
        "EventFeedback": ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef,
    },
    total=False,
)

ClientAdminListUserAuthEventsResponseTypeDef = TypedDict(
    "ClientAdminListUserAuthEventsResponseTypeDef",
    {"AuthEvents": List[ClientAdminListUserAuthEventsResponseAuthEventsTypeDef], "NextToken": str},
    total=False,
)

ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef = TypedDict(
    "ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)

ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef = TypedDict(
    "ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef",
    {"headerName": str, "headerValue": str},
    total=False,
)

_RequiredClientAdminRespondToAuthChallengeContextDataTypeDef = TypedDict(
    "_RequiredClientAdminRespondToAuthChallengeContextDataTypeDef", {"IpAddress": str}
)
_OptionalClientAdminRespondToAuthChallengeContextDataTypeDef = TypedDict(
    "_OptionalClientAdminRespondToAuthChallengeContextDataTypeDef",
    {
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List[ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef],
        "EncodedData": str,
    },
    total=False,
)


class ClientAdminRespondToAuthChallengeContextDataTypeDef(
    _RequiredClientAdminRespondToAuthChallengeContextDataTypeDef,
    _OptionalClientAdminRespondToAuthChallengeContextDataTypeDef,
):
    pass


ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)

ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef = TypedDict(
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)

ClientAdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "ClientAdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": Literal[
            "SMS_MFA",
            "SOFTWARE_TOKEN_MFA",
            "SELECT_MFA_TYPE",
            "MFA_SETUP",
            "PASSWORD_VERIFIER",
            "CUSTOM_CHALLENGE",
            "DEVICE_SRP_AUTH",
            "DEVICE_PASSWORD_VERIFIER",
            "ADMIN_NO_SRP_AUTH",
            "NEW_PASSWORD_REQUIRED",
        ],
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef,
    },
    total=False,
)

ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef = TypedDict(
    "ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)

ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = TypedDict(
    "ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)

ClientAdminSetUserSettingsMFAOptionsTypeDef = TypedDict(
    "ClientAdminSetUserSettingsMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

_RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef", {"Name": str}
)
_OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientAdminUpdateUserAttributesUserAttributesTypeDef(
    _RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef,
    _OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef,
):
    pass


ClientAssociateSoftwareTokenResponseTypeDef = TypedDict(
    "ClientAssociateSoftwareTokenResponseTypeDef", {"SecretCode": str, "Session": str}, total=False
)

ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef = TypedDict(
    "ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef",
    {"PasswordVerifier": str, "Salt": str},
    total=False,
)

ClientConfirmDeviceResponseTypeDef = TypedDict(
    "ClientConfirmDeviceResponseTypeDef", {"UserConfirmationNecessary": bool}, total=False
)

ClientConfirmForgotPasswordAnalyticsMetadataTypeDef = TypedDict(
    "ClientConfirmForgotPasswordAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)

ClientConfirmForgotPasswordUserContextDataTypeDef = TypedDict(
    "ClientConfirmForgotPasswordUserContextDataTypeDef", {"EncodedData": str}, total=False
)

ClientConfirmSignUpAnalyticsMetadataTypeDef = TypedDict(
    "ClientConfirmSignUpAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)

ClientConfirmSignUpUserContextDataTypeDef = TypedDict(
    "ClientConfirmSignUpUserContextDataTypeDef", {"EncodedData": str}, total=False
)

ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)

ClientCreateIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "ClientCreateIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientCreateIdentityProviderResponseTypeDef = TypedDict(
    "ClientCreateIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientCreateIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)

ClientCreateResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "ClientCreateResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)

ClientCreateResourceServerResponseResourceServerTypeDef = TypedDict(
    "ClientCreateResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientCreateResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)

ClientCreateResourceServerResponseTypeDef = TypedDict(
    "ClientCreateResourceServerResponseTypeDef",
    {"ResourceServer": ClientCreateResourceServerResponseResourceServerTypeDef},
    total=False,
)

_RequiredClientCreateResourceServerScopesTypeDef = TypedDict(
    "_RequiredClientCreateResourceServerScopesTypeDef", {"ScopeName": str}
)
_OptionalClientCreateResourceServerScopesTypeDef = TypedDict(
    "_OptionalClientCreateResourceServerScopesTypeDef", {"ScopeDescription": str}, total=False
)


class ClientCreateResourceServerScopesTypeDef(
    _RequiredClientCreateResourceServerScopesTypeDef,
    _OptionalClientCreateResourceServerScopesTypeDef,
):
    pass


ClientCreateUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "ClientCreateUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

ClientCreateUserImportJobResponseTypeDef = TypedDict(
    "ClientCreateUserImportJobResponseTypeDef",
    {"UserImportJob": ClientCreateUserImportJobResponseUserImportJobTypeDef},
    total=False,
)

ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int, "Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)

ClientCreateUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "ClientCreateUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)

ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)

ClientCreateUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "ClientCreateUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)

_RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef", {"ApplicationId": str}
)
_OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    {"RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientCreateUserPoolClientAnalyticsConfigurationTypeDef(
    _RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
    _OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
):
    pass


ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)

ClientCreateUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "ClientCreateUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
            ]
        ],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[Literal["code", "implicit", "client_credentials"]],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": Literal["LEGACY", "ENABLED"],
    },
    total=False,
)

ClientCreateUserPoolClientResponseTypeDef = TypedDict(
    "ClientCreateUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientCreateUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)

ClientCreateUserPoolDeviceConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)

ClientCreateUserPoolDomainCustomDomainConfigTypeDef = TypedDict(
    "ClientCreateUserPoolDomainCustomDomainConfigTypeDef", {"CertificateArn": str}
)

ClientCreateUserPoolDomainResponseTypeDef = TypedDict(
    "ClientCreateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)

ClientCreateUserPoolEmailConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

ClientCreateUserPoolLambdaConfigTypeDef = TypedDict(
    "ClientCreateUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)

ClientCreateUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "ClientCreateUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ClientCreateUserPoolPoliciesTypeDef = TypedDict(
    "ClientCreateUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientCreateUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)

ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int, "Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)

ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)

ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)

ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolPoliciesTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)

ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)

ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)

ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
    total=False,
)

ClientCreateUserPoolResponseUserPoolUsernameConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolUsernameConfigurationTypeDef",
    {"CaseSensitive": bool},
    total=False,
)

ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)

ClientCreateUserPoolResponseUserPoolTypeDef = TypedDict(
    "ClientCreateUserPoolResponseUserPoolTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": ClientCreateUserPoolResponseUserPoolPoliciesTypeDef,
        "LambdaConfig": ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef],
        "AutoVerifiedAttributes": List[Literal["phone_number", "email"]],
        "AliasAttributes": List[Literal["phone_number", "email", "preferred_username"]],
        "UsernameAttributes": List[Literal["phone_number", "email"]],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
        "DeviceConfiguration": ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef,
        "SmsConfiguration": ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef,
        "UserPoolAddOns": ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef,
        "UsernameConfiguration": ClientCreateUserPoolResponseUserPoolUsernameConfigurationTypeDef,
        "Arn": str,
        "AccountRecoverySetting": ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef,
    },
    total=False,
)

ClientCreateUserPoolResponseTypeDef = TypedDict(
    "ClientCreateUserPoolResponseTypeDef",
    {"UserPool": ClientCreateUserPoolResponseUserPoolTypeDef},
    total=False,
)

ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef = TypedDict(
    "ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef = TypedDict(
    "ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)

ClientCreateUserPoolSchemaTypeDef = TypedDict(
    "ClientCreateUserPoolSchemaTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef,
    },
    total=False,
)

_RequiredClientCreateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateUserPoolSmsConfigurationTypeDef", {"SnsCallerArn": str}
)
_OptionalClientCreateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateUserPoolSmsConfigurationTypeDef", {"ExternalId": str}, total=False
)


class ClientCreateUserPoolSmsConfigurationTypeDef(
    _RequiredClientCreateUserPoolSmsConfigurationTypeDef,
    _OptionalClientCreateUserPoolSmsConfigurationTypeDef,
):
    pass


ClientCreateUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "ClientCreateUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
)

ClientCreateUserPoolUsernameConfigurationTypeDef = TypedDict(
    "ClientCreateUserPoolUsernameConfigurationTypeDef", {"CaseSensitive": bool}
)

ClientCreateUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "ClientCreateUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)

ClientDescribeIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "ClientDescribeIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientDescribeIdentityProviderResponseTypeDef = TypedDict(
    "ClientDescribeIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientDescribeIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)

ClientDescribeResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "ClientDescribeResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)

ClientDescribeResourceServerResponseResourceServerTypeDef = TypedDict(
    "ClientDescribeResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientDescribeResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)

ClientDescribeResourceServerResponseTypeDef = TypedDict(
    "ClientDescribeResourceServerResponseTypeDef",
    {"ResourceServer": ClientDescribeResourceServerResponseResourceServerTypeDef},
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": Literal["BLOCK", "NO_ACTION"]},
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[Literal["SIGN_IN", "PASSWORD_CHANGE", "SIGN_UP"]],
        "Actions": ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)

ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
        "AccountTakeoverRiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
        "RiskExceptionConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeRiskConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeRiskConfigurationResponseTypeDef",
    {"RiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef},
    total=False,
)

ClientDescribeUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "ClientDescribeUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

ClientDescribeUserImportJobResponseTypeDef = TypedDict(
    "ClientDescribeUserImportJobResponseTypeDef",
    {"UserImportJob": ClientDescribeUserImportJobResponseUserImportJobTypeDef},
    total=False,
)

ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)

ClientDescribeUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "ClientDescribeUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
            ]
        ],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[Literal["code", "implicit", "client_credentials"]],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": Literal["LEGACY", "ENABLED"],
    },
    total=False,
)

ClientDescribeUserPoolClientResponseTypeDef = TypedDict(
    "ClientDescribeUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientDescribeUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)

ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef = TypedDict(
    "ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef",
    {"CertificateArn": str},
    total=False,
)

ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef = TypedDict(
    "ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": Literal["CREATING", "DELETING", "UPDATING", "ACTIVE", "FAILED"],
        "CustomDomainConfig": ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef,
    },
    total=False,
)

ClientDescribeUserPoolDomainResponseTypeDef = TypedDict(
    "ClientDescribeUserPoolDomainResponseTypeDef",
    {"DomainDescription": ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int, "Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolUsernameConfigurationTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolUsernameConfigurationTypeDef",
    {"CaseSensitive": bool},
    total=False,
)

ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)

ClientDescribeUserPoolResponseUserPoolTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseUserPoolTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef,
        "LambdaConfig": ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef],
        "AutoVerifiedAttributes": List[Literal["phone_number", "email"]],
        "AliasAttributes": List[Literal["phone_number", "email", "preferred_username"]],
        "UsernameAttributes": List[Literal["phone_number", "email"]],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
        "DeviceConfiguration": ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef,
        "SmsConfiguration": ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef,
        "UserPoolAddOns": ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef,
        "UsernameConfiguration": ClientDescribeUserPoolResponseUserPoolUsernameConfigurationTypeDef,
        "Arn": str,
        "AccountRecoverySetting": ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef,
    },
    total=False,
)

ClientDescribeUserPoolResponseTypeDef = TypedDict(
    "ClientDescribeUserPoolResponseTypeDef",
    {"UserPool": ClientDescribeUserPoolResponseUserPoolTypeDef},
    total=False,
)

ClientForgotPasswordAnalyticsMetadataTypeDef = TypedDict(
    "ClientForgotPasswordAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)

ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientForgotPasswordResponseTypeDef = TypedDict(
    "ClientForgotPasswordResponseTypeDef",
    {"CodeDeliveryDetails": ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef},
    total=False,
)

ClientForgotPasswordUserContextDataTypeDef = TypedDict(
    "ClientForgotPasswordUserContextDataTypeDef", {"EncodedData": str}, total=False
)

ClientGetCsvHeaderResponseTypeDef = TypedDict(
    "ClientGetCsvHeaderResponseTypeDef", {"UserPoolId": str, "CSVHeader": List[str]}, total=False
)

ClientGetDeviceResponseDeviceDeviceAttributesTypeDef = TypedDict(
    "ClientGetDeviceResponseDeviceDeviceAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientGetDeviceResponseDeviceTypeDef = TypedDict(
    "ClientGetDeviceResponseDeviceTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientGetDeviceResponseDeviceDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

ClientGetDeviceResponseTypeDef = TypedDict(
    "ClientGetDeviceResponseTypeDef", {"Device": ClientGetDeviceResponseDeviceTypeDef}, total=False
)

ClientGetGroupResponseGroupTypeDef = TypedDict(
    "ClientGetGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)

ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef = TypedDict(
    "ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "ClientGetIdentityProviderByIdentifierResponseTypeDef",
    {"IdentityProvider": ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef},
    total=False,
)

ClientGetSigningCertificateResponseTypeDef = TypedDict(
    "ClientGetSigningCertificateResponseTypeDef", {"Certificate": str}, total=False
)

ClientGetUiCustomizationResponseUICustomizationTypeDef = TypedDict(
    "ClientGetUiCustomizationResponseUICustomizationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetUiCustomizationResponseTypeDef = TypedDict(
    "ClientGetUiCustomizationResponseTypeDef",
    {"UICustomization": ClientGetUiCustomizationResponseUICustomizationTypeDef},
    total=False,
)

ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientGetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "ClientGetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef
    },
    total=False,
)

ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)

ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef = TypedDict(
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)

ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientGetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "ClientGetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef,
        "SoftwareTokenMfaConfiguration": ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
    },
    total=False,
)

ClientGetUserResponseMFAOptionsTypeDef = TypedDict(
    "ClientGetUserResponseMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientGetUserResponseUserAttributesTypeDef = TypedDict(
    "ClientGetUserResponseUserAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientGetUserResponseTypeDef = TypedDict(
    "ClientGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[ClientGetUserResponseUserAttributesTypeDef],
        "MFAOptions": List[ClientGetUserResponseMFAOptionsTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)

ClientInitiateAuthAnalyticsMetadataTypeDef = TypedDict(
    "ClientInitiateAuthAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)

ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)

ClientInitiateAuthResponseAuthenticationResultTypeDef = TypedDict(
    "ClientInitiateAuthResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)

ClientInitiateAuthResponseTypeDef = TypedDict(
    "ClientInitiateAuthResponseTypeDef",
    {
        "ChallengeName": Literal[
            "SMS_MFA",
            "SOFTWARE_TOKEN_MFA",
            "SELECT_MFA_TYPE",
            "MFA_SETUP",
            "PASSWORD_VERIFIER",
            "CUSTOM_CHALLENGE",
            "DEVICE_SRP_AUTH",
            "DEVICE_PASSWORD_VERIFIER",
            "ADMIN_NO_SRP_AUTH",
            "NEW_PASSWORD_REQUIRED",
        ],
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientInitiateAuthResponseAuthenticationResultTypeDef,
    },
    total=False,
)

ClientInitiateAuthUserContextDataTypeDef = TypedDict(
    "ClientInitiateAuthUserContextDataTypeDef", {"EncodedData": str}, total=False
)

ClientListDevicesResponseDevicesDeviceAttributesTypeDef = TypedDict(
    "ClientListDevicesResponseDevicesDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "ClientListDevicesResponseDevicesTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientListDevicesResponseDevicesDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

ClientListDevicesResponseTypeDef = TypedDict(
    "ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "PaginationToken": str},
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListIdentityProvidersResponseProvidersTypeDef = TypedDict(
    "ClientListIdentityProvidersResponseProvidersTypeDef",
    {
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientListIdentityProvidersResponseTypeDef = TypedDict(
    "ClientListIdentityProvidersResponseTypeDef",
    {"Providers": List[ClientListIdentityProvidersResponseProvidersTypeDef], "NextToken": str},
    total=False,
)

ClientListResourceServersResponseResourceServersScopesTypeDef = TypedDict(
    "ClientListResourceServersResponseResourceServersScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)

ClientListResourceServersResponseResourceServersTypeDef = TypedDict(
    "ClientListResourceServersResponseResourceServersTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientListResourceServersResponseResourceServersScopesTypeDef],
    },
    total=False,
)

ClientListResourceServersResponseTypeDef = TypedDict(
    "ClientListResourceServersResponseTypeDef",
    {
        "ResourceServers": List[ClientListResourceServersResponseResourceServersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListUserImportJobsResponseUserImportJobsTypeDef = TypedDict(
    "ClientListUserImportJobsResponseUserImportJobsTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

ClientListUserImportJobsResponseTypeDef = TypedDict(
    "ClientListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List[ClientListUserImportJobsResponseUserImportJobsTypeDef],
        "PaginationToken": str,
    },
    total=False,
)

ClientListUserPoolClientsResponseUserPoolClientsTypeDef = TypedDict(
    "ClientListUserPoolClientsResponseUserPoolClientsTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)

ClientListUserPoolClientsResponseTypeDef = TypedDict(
    "ClientListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List[ClientListUserPoolClientsResponseUserPoolClientsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef = TypedDict(
    "ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)

ClientListUserPoolsResponseUserPoolsTypeDef = TypedDict(
    "ClientListUserPoolsResponseUserPoolsTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientListUserPoolsResponseTypeDef = TypedDict(
    "ClientListUserPoolsResponseTypeDef",
    {"UserPools": List[ClientListUserPoolsResponseUserPoolsTypeDef], "NextToken": str},
    total=False,
)

ClientListUsersInGroupResponseUsersAttributesTypeDef = TypedDict(
    "ClientListUsersInGroupResponseUsersAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientListUsersInGroupResponseUsersMFAOptionsTypeDef = TypedDict(
    "ClientListUsersInGroupResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientListUsersInGroupResponseUsersTypeDef = TypedDict(
    "ClientListUsersInGroupResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientListUsersInGroupResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientListUsersInGroupResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)

ClientListUsersInGroupResponseTypeDef = TypedDict(
    "ClientListUsersInGroupResponseTypeDef",
    {"Users": List[ClientListUsersInGroupResponseUsersTypeDef], "NextToken": str},
    total=False,
)

ClientListUsersResponseUsersAttributesTypeDef = TypedDict(
    "ClientListUsersResponseUsersAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientListUsersResponseUsersMFAOptionsTypeDef = TypedDict(
    "ClientListUsersResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientListUsersResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientListUsersResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "PaginationToken": str},
    total=False,
)

ClientResendConfirmationCodeAnalyticsMetadataTypeDef = TypedDict(
    "ClientResendConfirmationCodeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)

ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientResendConfirmationCodeResponseTypeDef = TypedDict(
    "ClientResendConfirmationCodeResponseTypeDef",
    {"CodeDeliveryDetails": ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef},
    total=False,
)

ClientResendConfirmationCodeUserContextDataTypeDef = TypedDict(
    "ClientResendConfirmationCodeUserContextDataTypeDef", {"EncodedData": str}, total=False
)

ClientRespondToAuthChallengeAnalyticsMetadataTypeDef = TypedDict(
    "ClientRespondToAuthChallengeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)

ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)

ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef = TypedDict(
    "ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)

ClientRespondToAuthChallengeResponseTypeDef = TypedDict(
    "ClientRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": Literal[
            "SMS_MFA",
            "SOFTWARE_TOKEN_MFA",
            "SELECT_MFA_TYPE",
            "MFA_SETUP",
            "PASSWORD_VERIFIER",
            "CUSTOM_CHALLENGE",
            "DEVICE_SRP_AUTH",
            "DEVICE_PASSWORD_VERIFIER",
            "ADMIN_NO_SRP_AUTH",
            "NEW_PASSWORD_REQUIRED",
        ],
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef,
    },
    total=False,
)

ClientRespondToAuthChallengeUserContextDataTypeDef = TypedDict(
    "ClientRespondToAuthChallengeUserContextDataTypeDef", {"EncodedData": str}, total=False
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": Literal["BLOCK", "NO_ACTION"]},
    total=False,
)

ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[Literal["SIGN_IN", "PASSWORD_CHANGE", "SIGN_UP"]],
        "Actions": ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": Literal["BLOCK", "NO_ACTION"]},
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[Literal["SIGN_IN", "PASSWORD_CHANGE", "SIGN_UP"]],
        "Actions": ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)

ClientSetRiskConfigurationResponseRiskConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseRiskConfigurationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
        "AccountTakeoverRiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
        "RiskExceptionConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)

ClientSetRiskConfigurationResponseTypeDef = TypedDict(
    "ClientSetRiskConfigurationResponseTypeDef",
    {"RiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationTypeDef},
    total=False,
)

ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)

ClientSetUiCustomizationResponseUICustomizationTypeDef = TypedDict(
    "ClientSetUiCustomizationResponseUICustomizationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientSetUiCustomizationResponseTypeDef = TypedDict(
    "ClientSetUiCustomizationResponseTypeDef",
    {"UICustomization": ClientSetUiCustomizationResponseUICustomizationTypeDef},
    total=False,
)

ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef = TypedDict(
    "ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)

ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = TypedDict(
    "ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)

ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)

ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)

ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientSetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef,
        "SoftwareTokenMfaConfiguration": ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
    },
    total=False,
)

ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)

ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)

ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef", {"Enabled": bool}, total=False
)

ClientSetUserSettingsMFAOptionsTypeDef = TypedDict(
    "ClientSetUserSettingsMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientSignUpAnalyticsMetadataTypeDef = TypedDict(
    "ClientSignUpAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)

ClientSignUpResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "ClientSignUpResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientSignUpResponseTypeDef = TypedDict(
    "ClientSignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": ClientSignUpResponseCodeDeliveryDetailsTypeDef,
        "UserSub": str,
    },
    total=False,
)

_RequiredClientSignUpUserAttributesTypeDef = TypedDict(
    "_RequiredClientSignUpUserAttributesTypeDef", {"Name": str}
)
_OptionalClientSignUpUserAttributesTypeDef = TypedDict(
    "_OptionalClientSignUpUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientSignUpUserAttributesTypeDef(
    _RequiredClientSignUpUserAttributesTypeDef, _OptionalClientSignUpUserAttributesTypeDef
):
    pass


ClientSignUpUserContextDataTypeDef = TypedDict(
    "ClientSignUpUserContextDataTypeDef", {"EncodedData": str}, total=False
)

_RequiredClientSignUpValidationDataTypeDef = TypedDict(
    "_RequiredClientSignUpValidationDataTypeDef", {"Name": str}
)
_OptionalClientSignUpValidationDataTypeDef = TypedDict(
    "_OptionalClientSignUpValidationDataTypeDef", {"Value": str}, total=False
)


class ClientSignUpValidationDataTypeDef(
    _RequiredClientSignUpValidationDataTypeDef, _OptionalClientSignUpValidationDataTypeDef
):
    pass


ClientStartUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "ClientStartUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

ClientStartUserImportJobResponseTypeDef = TypedDict(
    "ClientStartUserImportJobResponseTypeDef",
    {"UserImportJob": ClientStartUserImportJobResponseUserImportJobTypeDef},
    total=False,
)

ClientStopUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "ClientStopUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

ClientStopUserImportJobResponseTypeDef = TypedDict(
    "ClientStopUserImportJobResponseTypeDef",
    {"UserImportJob": ClientStopUserImportJobResponseUserImportJobTypeDef},
    total=False,
)

ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "ClientUpdateGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientUpdateGroupResponseTypeDef = TypedDict(
    "ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)

ClientUpdateIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "ClientUpdateIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ClientUpdateIdentityProviderResponseTypeDef = TypedDict(
    "ClientUpdateIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientUpdateIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)

ClientUpdateResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "ClientUpdateResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)

ClientUpdateResourceServerResponseResourceServerTypeDef = TypedDict(
    "ClientUpdateResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientUpdateResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)

ClientUpdateResourceServerResponseTypeDef = TypedDict(
    "ClientUpdateResourceServerResponseTypeDef",
    {"ResourceServer": ClientUpdateResourceServerResponseResourceServerTypeDef},
    total=False,
)

_RequiredClientUpdateResourceServerScopesTypeDef = TypedDict(
    "_RequiredClientUpdateResourceServerScopesTypeDef", {"ScopeName": str}
)
_OptionalClientUpdateResourceServerScopesTypeDef = TypedDict(
    "_OptionalClientUpdateResourceServerScopesTypeDef", {"ScopeDescription": str}, total=False
)


class ClientUpdateResourceServerScopesTypeDef(
    _RequiredClientUpdateResourceServerScopesTypeDef,
    _OptionalClientUpdateResourceServerScopesTypeDef,
):
    pass


ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef = TypedDict(
    "ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

ClientUpdateUserAttributesResponseTypeDef = TypedDict(
    "ClientUpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List[
            ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef
        ]
    },
    total=False,
)

_RequiredClientUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_RequiredClientUpdateUserAttributesUserAttributesTypeDef", {"Name": str}
)
_OptionalClientUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_OptionalClientUpdateUserAttributesUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientUpdateUserAttributesUserAttributesTypeDef(
    _RequiredClientUpdateUserAttributesUserAttributesTypeDef,
    _OptionalClientUpdateUserAttributesUserAttributesTypeDef,
):
    pass


_RequiredClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int},
)
_OptionalClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)


class ClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef(
    _RequiredClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef,
    _OptionalClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef,
):
    pass


ClientUpdateUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "ClientUpdateUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)

ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)

ClientUpdateUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "ClientUpdateUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)

_RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef", {"ApplicationId": str}
)
_OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    {"RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef(
    _RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
    _OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
):
    pass


ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)

ClientUpdateUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "ClientUpdateUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
            ]
        ],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[Literal["code", "implicit", "client_credentials"]],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": Literal["LEGACY", "ENABLED"],
    },
    total=False,
)

ClientUpdateUserPoolClientResponseTypeDef = TypedDict(
    "ClientUpdateUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientUpdateUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)

ClientUpdateUserPoolDeviceConfigurationTypeDef = TypedDict(
    "ClientUpdateUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)

ClientUpdateUserPoolDomainCustomDomainConfigTypeDef = TypedDict(
    "ClientUpdateUserPoolDomainCustomDomainConfigTypeDef", {"CertificateArn": str}
)

ClientUpdateUserPoolDomainResponseTypeDef = TypedDict(
    "ClientUpdateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)

ClientUpdateUserPoolEmailConfigurationTypeDef = TypedDict(
    "ClientUpdateUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

ClientUpdateUserPoolLambdaConfigTypeDef = TypedDict(
    "ClientUpdateUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)

ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ClientUpdateUserPoolPoliciesTypeDef = TypedDict(
    "ClientUpdateUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)

_RequiredClientUpdateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolSmsConfigurationTypeDef", {"SnsCallerArn": str}
)
_OptionalClientUpdateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolSmsConfigurationTypeDef", {"ExternalId": str}, total=False
)


class ClientUpdateUserPoolSmsConfigurationTypeDef(
    _RequiredClientUpdateUserPoolSmsConfigurationTypeDef,
    _OptionalClientUpdateUserPoolSmsConfigurationTypeDef,
):
    pass


ClientUpdateUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "ClientUpdateUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
)

ClientUpdateUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "ClientUpdateUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)

ClientVerifySoftwareTokenResponseTypeDef = TypedDict(
    "ClientVerifySoftwareTokenResponseTypeDef",
    {"Status": Literal["SUCCESS", "ERROR"], "Session": str},
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef", {"Groups": List[GroupTypeTypeDef], "NextToken": str}, total=False
)

ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredListIdentityProvidersResponseTypeDef = TypedDict(
    "_RequiredListIdentityProvidersResponseTypeDef", {"Providers": List[ProviderDescriptionTypeDef]}
)
_OptionalListIdentityProvidersResponseTypeDef = TypedDict(
    "_OptionalListIdentityProvidersResponseTypeDef", {"NextToken": str}, total=False
)


class ListIdentityProvidersResponseTypeDef(
    _RequiredListIdentityProvidersResponseTypeDef, _OptionalListIdentityProvidersResponseTypeDef
):
    pass


ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef", {"ScopeName": str, "ScopeDescription": str}
)

ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ResourceServerScopeTypeTypeDef],
    },
    total=False,
)

_RequiredListResourceServersResponseTypeDef = TypedDict(
    "_RequiredListResourceServersResponseTypeDef",
    {"ResourceServers": List[ResourceServerTypeTypeDef]},
)
_OptionalListResourceServersResponseTypeDef = TypedDict(
    "_OptionalListResourceServersResponseTypeDef", {"NextToken": str}, total=False
)


class ListResourceServersResponseTypeDef(
    _RequiredListResourceServersResponseTypeDef, _OptionalListResourceServersResponseTypeDef
):
    pass


UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)

ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {"UserPoolClients": List[UserPoolClientDescriptionTypeDef], "NextToken": str},
    total=False,
)

LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)

UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": LambdaConfigTypeTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {"UserPools": List[UserPoolDescriptionTypeTypeDef], "NextToken": str},
    total=False,
)

_RequiredAttributeTypeTypeDef = TypedDict("_RequiredAttributeTypeTypeDef", {"Name": str})
_OptionalAttributeTypeTypeDef = TypedDict(
    "_OptionalAttributeTypeTypeDef", {"Value": str}, total=False
)


class AttributeTypeTypeDef(_RequiredAttributeTypeTypeDef, _OptionalAttributeTypeTypeDef):
    pass


MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)

UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": str,
        "Attributes": List[AttributeTypeTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[MFAOptionTypeTypeDef],
    },
    total=False,
)

ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {"Users": List[UserTypeTypeDef], "NextToken": str},
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {"Users": List[UserTypeTypeDef], "PaginationToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
