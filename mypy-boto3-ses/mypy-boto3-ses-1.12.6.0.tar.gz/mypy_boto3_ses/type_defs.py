"""
Main interface for ses service type definitions.

Usage::

    from mypy_boto3.ses.type_defs import ClientCreateConfigurationSetConfigurationSetTypeDef

    data: ClientCreateConfigurationSetConfigurationSetTypeDef = {...}
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
    "ClientCreateConfigurationSetConfigurationSetTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    "ClientCreateReceiptFilterFilterIpFilterTypeDef",
    "ClientCreateReceiptFilterFilterTypeDef",
    "ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsS3ActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsSNSActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsStopActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsTypeDef",
    "ClientCreateReceiptRuleRuleTypeDef",
    "ClientCreateTemplateTemplateTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseTypeDef",
    "ClientDescribeConfigurationSetResponseConfigurationSetTypeDef",
    "ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsTypeDef",
    "ClientDescribeConfigurationSetResponseReputationOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsTypeDef",
    "ClientDescribeReceiptRuleResponseRuleTypeDef",
    "ClientDescribeReceiptRuleResponseTypeDef",
    "ClientDescribeReceiptRuleSetResponseMetadataTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesTypeDef",
    "ClientDescribeReceiptRuleSetResponseTypeDef",
    "ClientGetAccountSendingEnabledResponseTypeDef",
    "ClientGetCustomVerificationEmailTemplateResponseTypeDef",
    "ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef",
    "ClientGetIdentityDkimAttributesResponseTypeDef",
    "ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef",
    "ClientGetIdentityMailFromDomainAttributesResponseTypeDef",
    "ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef",
    "ClientGetIdentityNotificationAttributesResponseTypeDef",
    "ClientGetIdentityPoliciesResponseTypeDef",
    "ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef",
    "ClientGetIdentityVerificationAttributesResponseTypeDef",
    "ClientGetSendQuotaResponseTypeDef",
    "ClientGetSendStatisticsResponseSendDataPointsTypeDef",
    "ClientGetSendStatisticsResponseTypeDef",
    "ClientGetTemplateResponseTemplateTypeDef",
    "ClientGetTemplateResponseTypeDef",
    "ClientListConfigurationSetsResponseConfigurationSetsTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef",
    "ClientListCustomVerificationEmailTemplatesResponseTypeDef",
    "ClientListIdentitiesResponseTypeDef",
    "ClientListIdentityPoliciesResponseTypeDef",
    "ClientListReceiptFiltersResponseFiltersIpFilterTypeDef",
    "ClientListReceiptFiltersResponseFiltersTypeDef",
    "ClientListReceiptFiltersResponseTypeDef",
    "ClientListReceiptRuleSetsResponseRuleSetsTypeDef",
    "ClientListReceiptRuleSetsResponseTypeDef",
    "ClientListTemplatesResponseTemplatesMetadataTypeDef",
    "ClientListTemplatesResponseTypeDef",
    "ClientListVerifiedEmailAddressesResponseTypeDef",
    "ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListTypeDef",
    "ClientSendBounceMessageDsnExtensionFieldsTypeDef",
    "ClientSendBounceMessageDsnTypeDef",
    "ClientSendBounceResponseTypeDef",
    "ClientSendBulkTemplatedEmailDefaultTagsTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsTypeDef",
    "ClientSendBulkTemplatedEmailResponseStatusTypeDef",
    "ClientSendBulkTemplatedEmailResponseTypeDef",
    "ClientSendCustomVerificationEmailResponseTypeDef",
    "ClientSendEmailDestinationTypeDef",
    "ClientSendEmailMessageBodyHtmlTypeDef",
    "ClientSendEmailMessageBodyTextTypeDef",
    "ClientSendEmailMessageBodyTypeDef",
    "ClientSendEmailMessageSubjectTypeDef",
    "ClientSendEmailMessageTypeDef",
    "ClientSendEmailResponseTypeDef",
    "ClientSendEmailTagsTypeDef",
    "ClientSendRawEmailRawMessageTypeDef",
    "ClientSendRawEmailResponseTypeDef",
    "ClientSendRawEmailTagsTypeDef",
    "ClientSendTemplatedEmailDestinationTypeDef",
    "ClientSendTemplatedEmailResponseTypeDef",
    "ClientSendTemplatedEmailTagsTypeDef",
    "ClientTestRenderTemplateResponseTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    "ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsStopActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsTypeDef",
    "ClientUpdateReceiptRuleRuleTypeDef",
    "ClientUpdateTemplateTemplateTypeDef",
    "ClientVerifyDomainDkimResponseTypeDef",
    "ClientVerifyDomainIdentityResponseTypeDef",
    "ConfigurationSetTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "TemplateMetadataTypeDef",
    "ListTemplatesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientCreateConfigurationSetConfigurationSetTypeDef = TypedDict(
    "ClientCreateConfigurationSetConfigurationSetTypeDef", {"Name": str}
)

ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)

_RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef", {"Name": str}
)
_OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
            ]
        ],
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SNSDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    _OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
):
    pass


ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef = TypedDict(
    "ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)

ClientCreateReceiptFilterFilterIpFilterTypeDef = TypedDict(
    "ClientCreateReceiptFilterFilterIpFilterTypeDef",
    {"Policy": Literal["Block", "Allow"], "Cidr": str},
    total=False,
)

_RequiredClientCreateReceiptFilterFilterTypeDef = TypedDict(
    "_RequiredClientCreateReceiptFilterFilterTypeDef", {"Name": str}
)
_OptionalClientCreateReceiptFilterFilterTypeDef = TypedDict(
    "_OptionalClientCreateReceiptFilterFilterTypeDef",
    {"IpFilter": ClientCreateReceiptFilterFilterIpFilterTypeDef},
    total=False,
)


class ClientCreateReceiptFilterFilterTypeDef(
    _RequiredClientCreateReceiptFilterFilterTypeDef, _OptionalClientCreateReceiptFilterFilterTypeDef
):
    pass


ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)

ClientCreateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)

ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)

ClientCreateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)

ClientCreateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)

ClientCreateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)

ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)

ClientCreateReceiptRuleRuleActionsTypeDef = TypedDict(
    "ClientCreateReceiptRuleRuleActionsTypeDef",
    {
        "S3Action": ClientCreateReceiptRuleRuleActionsS3ActionTypeDef,
        "BounceAction": ClientCreateReceiptRuleRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef,
        "StopAction": ClientCreateReceiptRuleRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientCreateReceiptRuleRuleActionsSNSActionTypeDef,
    },
    total=False,
)

_RequiredClientCreateReceiptRuleRuleTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleTypeDef", {"Name": str}
)
_OptionalClientCreateReceiptRuleRuleTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientCreateReceiptRuleRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientCreateReceiptRuleRuleTypeDef(
    _RequiredClientCreateReceiptRuleRuleTypeDef, _OptionalClientCreateReceiptRuleRuleTypeDef
):
    pass


_RequiredClientCreateTemplateTemplateTypeDef = TypedDict(
    "_RequiredClientCreateTemplateTemplateTypeDef", {"TemplateName": str}
)
_OptionalClientCreateTemplateTemplateTypeDef = TypedDict(
    "_OptionalClientCreateTemplateTemplateTypeDef",
    {"SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientCreateTemplateTemplateTypeDef(
    _RequiredClientCreateTemplateTemplateTypeDef, _OptionalClientCreateTemplateTemplateTypeDef
):
    pass


ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef",
    {
        "S3Action": ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef,
    },
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)

ClientDescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "ClientDescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef,
        "Rules": List[ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef],
    },
    total=False,
)

ClientDescribeConfigurationSetResponseConfigurationSetTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseConfigurationSetTypeDef", {"Name": str}, total=False
)

ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["Require", "Optional"]},
    total=False,
)

ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
    total=False,
)

ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)

ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)

ClientDescribeConfigurationSetResponseEventDestinationsTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseEventDestinationsTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
            ]
        ],
        "KinesisFirehoseDestination": ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef,
        "SNSDestination": ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef,
    },
    total=False,
)

ClientDescribeConfigurationSetResponseReputationOptionsTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseReputationOptionsTypeDef",
    {"SendingEnabled": bool, "ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)

ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)

ClientDescribeConfigurationSetResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": ClientDescribeConfigurationSetResponseConfigurationSetTypeDef,
        "EventDestinations": List[ClientDescribeConfigurationSetResponseEventDestinationsTypeDef],
        "TrackingOptions": ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef,
        "DeliveryOptions": ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef,
        "ReputationOptions": ClientDescribeConfigurationSetResponseReputationOptionsTypeDef,
    },
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)

ClientDescribeReceiptRuleResponseRuleActionsTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleActionsTypeDef",
    {
        "S3Action": ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef,
    },
    total=False,
)

ClientDescribeReceiptRuleResponseRuleTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseRuleTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientDescribeReceiptRuleResponseRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)

ClientDescribeReceiptRuleResponseTypeDef = TypedDict(
    "ClientDescribeReceiptRuleResponseTypeDef",
    {"Rule": ClientDescribeReceiptRuleResponseRuleTypeDef},
    total=False,
)

ClientDescribeReceiptRuleSetResponseMetadataTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef",
    {
        "S3Action": ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef,
    },
    total=False,
)

ClientDescribeReceiptRuleSetResponseRulesTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseRulesTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)

ClientDescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "ClientDescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ClientDescribeReceiptRuleSetResponseMetadataTypeDef,
        "Rules": List[ClientDescribeReceiptRuleSetResponseRulesTypeDef],
    },
    total=False,
)

ClientGetAccountSendingEnabledResponseTypeDef = TypedDict(
    "ClientGetAccountSendingEnabledResponseTypeDef", {"Enabled": bool}, total=False
)

ClientGetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "ClientGetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef = TypedDict(
    "ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": Literal[
            "Pending", "Success", "Failed", "TemporaryFailure", "NotStarted"
        ],
        "DkimTokens": List[str],
    },
    total=False,
)

ClientGetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "ClientGetIdentityDkimAttributesResponseTypeDef",
    {"DkimAttributes": Dict[str, ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef]},
    total=False,
)

ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef = TypedDict(
    "ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": Literal["Pending", "Success", "Failed", "TemporaryFailure"],
        "BehaviorOnMXFailure": Literal["UseDefaultValue", "RejectMessage"],
    },
    total=False,
)

ClientGetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "ClientGetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[
            str, ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef
        ]
    },
    total=False,
)

ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef = TypedDict(
    "ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
        "HeadersInBounceNotificationsEnabled": bool,
        "HeadersInComplaintNotificationsEnabled": bool,
        "HeadersInDeliveryNotificationsEnabled": bool,
    },
    total=False,
)

ClientGetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "ClientGetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[
            str, ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef
        ]
    },
    total=False,
)

ClientGetIdentityPoliciesResponseTypeDef = TypedDict(
    "ClientGetIdentityPoliciesResponseTypeDef", {"Policies": Dict[str, str]}, total=False
)

ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef = TypedDict(
    "ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef",
    {
        "VerificationStatus": Literal[
            "Pending", "Success", "Failed", "TemporaryFailure", "NotStarted"
        ],
        "VerificationToken": str,
    },
    total=False,
)

ClientGetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "ClientGetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[
            str, ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef
        ]
    },
    total=False,
)

ClientGetSendQuotaResponseTypeDef = TypedDict(
    "ClientGetSendQuotaResponseTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)

ClientGetSendStatisticsResponseSendDataPointsTypeDef = TypedDict(
    "ClientGetSendStatisticsResponseSendDataPointsTypeDef",
    {
        "Timestamp": datetime,
        "DeliveryAttempts": int,
        "Bounces": int,
        "Complaints": int,
        "Rejects": int,
    },
    total=False,
)

ClientGetSendStatisticsResponseTypeDef = TypedDict(
    "ClientGetSendStatisticsResponseTypeDef",
    {"SendDataPoints": List[ClientGetSendStatisticsResponseSendDataPointsTypeDef]},
    total=False,
)

ClientGetTemplateResponseTemplateTypeDef = TypedDict(
    "ClientGetTemplateResponseTemplateTypeDef",
    {"TemplateName": str, "SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)

ClientGetTemplateResponseTypeDef = TypedDict(
    "ClientGetTemplateResponseTypeDef",
    {"Template": ClientGetTemplateResponseTemplateTypeDef},
    total=False,
)

ClientListConfigurationSetsResponseConfigurationSetsTypeDef = TypedDict(
    "ClientListConfigurationSetsResponseConfigurationSetsTypeDef", {"Name": str}, total=False
)

ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "ClientListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[ClientListConfigurationSetsResponseConfigurationSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef = TypedDict(
    "ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

ClientListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ClientListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[
            ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListIdentitiesResponseTypeDef = TypedDict(
    "ClientListIdentitiesResponseTypeDef", {"Identities": List[str], "NextToken": str}, total=False
)

ClientListIdentityPoliciesResponseTypeDef = TypedDict(
    "ClientListIdentityPoliciesResponseTypeDef", {"PolicyNames": List[str]}, total=False
)

ClientListReceiptFiltersResponseFiltersIpFilterTypeDef = TypedDict(
    "ClientListReceiptFiltersResponseFiltersIpFilterTypeDef",
    {"Policy": Literal["Block", "Allow"], "Cidr": str},
    total=False,
)

ClientListReceiptFiltersResponseFiltersTypeDef = TypedDict(
    "ClientListReceiptFiltersResponseFiltersTypeDef",
    {"Name": str, "IpFilter": ClientListReceiptFiltersResponseFiltersIpFilterTypeDef},
    total=False,
)

ClientListReceiptFiltersResponseTypeDef = TypedDict(
    "ClientListReceiptFiltersResponseTypeDef",
    {"Filters": List[ClientListReceiptFiltersResponseFiltersTypeDef]},
    total=False,
)

ClientListReceiptRuleSetsResponseRuleSetsTypeDef = TypedDict(
    "ClientListReceiptRuleSetsResponseRuleSetsTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)

ClientListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ClientListReceiptRuleSetsResponseTypeDef",
    {"RuleSets": List[ClientListReceiptRuleSetsResponseRuleSetsTypeDef], "NextToken": str},
    total=False,
)

ClientListTemplatesResponseTemplatesMetadataTypeDef = TypedDict(
    "ClientListTemplatesResponseTemplatesMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)

ClientListTemplatesResponseTypeDef = TypedDict(
    "ClientListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List[ClientListTemplatesResponseTemplatesMetadataTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "ClientListVerifiedEmailAddressesResponseTypeDef",
    {"VerifiedEmailAddresses": List[str]},
    total=False,
)

ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef = TypedDict(
    "ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["Require", "Optional"]},
    total=False,
)

ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef = TypedDict(
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef = TypedDict(
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    {
        "FinalRecipient": str,
        "Action": Literal["failed", "delayed", "delivered", "relayed", "expanded"],
        "RemoteMta": str,
        "Status": str,
        "DiagnosticCode": str,
        "LastAttemptDate": datetime,
        "ExtensionFields": List[
            ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef
        ],
    },
    total=False,
)

_RequiredClientSendBounceBouncedRecipientInfoListTypeDef = TypedDict(
    "_RequiredClientSendBounceBouncedRecipientInfoListTypeDef", {"Recipient": str}
)
_OptionalClientSendBounceBouncedRecipientInfoListTypeDef = TypedDict(
    "_OptionalClientSendBounceBouncedRecipientInfoListTypeDef",
    {
        "RecipientArn": str,
        "BounceType": Literal[
            "DoesNotExist",
            "MessageTooLarge",
            "ExceededQuota",
            "ContentRejected",
            "Undefined",
            "TemporaryFailure",
        ],
        "RecipientDsnFields": ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef,
    },
    total=False,
)


class ClientSendBounceBouncedRecipientInfoListTypeDef(
    _RequiredClientSendBounceBouncedRecipientInfoListTypeDef,
    _OptionalClientSendBounceBouncedRecipientInfoListTypeDef,
):
    pass


ClientSendBounceMessageDsnExtensionFieldsTypeDef = TypedDict(
    "ClientSendBounceMessageDsnExtensionFieldsTypeDef", {"Name": str, "Value": str}, total=False
)

_RequiredClientSendBounceMessageDsnTypeDef = TypedDict(
    "_RequiredClientSendBounceMessageDsnTypeDef", {"ReportingMta": str}
)
_OptionalClientSendBounceMessageDsnTypeDef = TypedDict(
    "_OptionalClientSendBounceMessageDsnTypeDef",
    {
        "ArrivalDate": datetime,
        "ExtensionFields": List[ClientSendBounceMessageDsnExtensionFieldsTypeDef],
    },
    total=False,
)


class ClientSendBounceMessageDsnTypeDef(
    _RequiredClientSendBounceMessageDsnTypeDef, _OptionalClientSendBounceMessageDsnTypeDef
):
    pass


ClientSendBounceResponseTypeDef = TypedDict(
    "ClientSendBounceResponseTypeDef", {"MessageId": str}, total=False
)

_RequiredClientSendBulkTemplatedEmailDefaultTagsTypeDef = TypedDict(
    "_RequiredClientSendBulkTemplatedEmailDefaultTagsTypeDef", {"Name": str}
)
_OptionalClientSendBulkTemplatedEmailDefaultTagsTypeDef = TypedDict(
    "_OptionalClientSendBulkTemplatedEmailDefaultTagsTypeDef", {"Value": str}, total=False
)


class ClientSendBulkTemplatedEmailDefaultTagsTypeDef(
    _RequiredClientSendBulkTemplatedEmailDefaultTagsTypeDef,
    _OptionalClientSendBulkTemplatedEmailDefaultTagsTypeDef,
):
    pass


ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef = TypedDict(
    "ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)

ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef = TypedDict(
    "ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

_RequiredClientSendBulkTemplatedEmailDestinationsTypeDef = TypedDict(
    "_RequiredClientSendBulkTemplatedEmailDestinationsTypeDef",
    {"Destination": ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef},
)
_OptionalClientSendBulkTemplatedEmailDestinationsTypeDef = TypedDict(
    "_OptionalClientSendBulkTemplatedEmailDestinationsTypeDef",
    {
        "ReplacementTags": List[ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef],
        "ReplacementTemplateData": str,
    },
    total=False,
)


class ClientSendBulkTemplatedEmailDestinationsTypeDef(
    _RequiredClientSendBulkTemplatedEmailDestinationsTypeDef,
    _OptionalClientSendBulkTemplatedEmailDestinationsTypeDef,
):
    pass


ClientSendBulkTemplatedEmailResponseStatusTypeDef = TypedDict(
    "ClientSendBulkTemplatedEmailResponseStatusTypeDef",
    {
        "Status": Literal[
            "Success",
            "MessageRejected",
            "MailFromDomainNotVerified",
            "ConfigurationSetDoesNotExist",
            "TemplateDoesNotExist",
            "AccountSuspended",
            "AccountThrottled",
            "AccountDailyQuotaExceeded",
            "InvalidSendingPoolName",
            "AccountSendingPaused",
            "ConfigurationSetSendingPaused",
            "InvalidParameterValue",
            "TransientFailure",
            "Failed",
        ],
        "Error": str,
        "MessageId": str,
    },
    total=False,
)

ClientSendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "ClientSendBulkTemplatedEmailResponseTypeDef",
    {"Status": List[ClientSendBulkTemplatedEmailResponseStatusTypeDef]},
    total=False,
)

ClientSendCustomVerificationEmailResponseTypeDef = TypedDict(
    "ClientSendCustomVerificationEmailResponseTypeDef", {"MessageId": str}, total=False
)

ClientSendEmailDestinationTypeDef = TypedDict(
    "ClientSendEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)

ClientSendEmailMessageBodyHtmlTypeDef = TypedDict(
    "ClientSendEmailMessageBodyHtmlTypeDef", {"Data": str, "Charset": str}, total=False
)

ClientSendEmailMessageBodyTextTypeDef = TypedDict(
    "ClientSendEmailMessageBodyTextTypeDef", {"Data": str, "Charset": str}, total=False
)

ClientSendEmailMessageBodyTypeDef = TypedDict(
    "ClientSendEmailMessageBodyTypeDef",
    {"Text": ClientSendEmailMessageBodyTextTypeDef, "Html": ClientSendEmailMessageBodyHtmlTypeDef},
    total=False,
)

_RequiredClientSendEmailMessageSubjectTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageSubjectTypeDef", {"Data": str}
)
_OptionalClientSendEmailMessageSubjectTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageSubjectTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailMessageSubjectTypeDef(
    _RequiredClientSendEmailMessageSubjectTypeDef, _OptionalClientSendEmailMessageSubjectTypeDef
):
    pass


_RequiredClientSendEmailMessageTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageTypeDef", {"Subject": ClientSendEmailMessageSubjectTypeDef}
)
_OptionalClientSendEmailMessageTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageTypeDef",
    {"Body": ClientSendEmailMessageBodyTypeDef},
    total=False,
)


class ClientSendEmailMessageTypeDef(
    _RequiredClientSendEmailMessageTypeDef, _OptionalClientSendEmailMessageTypeDef
):
    pass


ClientSendEmailResponseTypeDef = TypedDict(
    "ClientSendEmailResponseTypeDef", {"MessageId": str}, total=False
)

_RequiredClientSendEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendEmailTagsTypeDef(
    _RequiredClientSendEmailTagsTypeDef, _OptionalClientSendEmailTagsTypeDef
):
    pass


ClientSendRawEmailRawMessageTypeDef = TypedDict(
    "ClientSendRawEmailRawMessageTypeDef", {"Data": bytes}
)

ClientSendRawEmailResponseTypeDef = TypedDict(
    "ClientSendRawEmailResponseTypeDef", {"MessageId": str}, total=False
)

_RequiredClientSendRawEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendRawEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendRawEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendRawEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendRawEmailTagsTypeDef(
    _RequiredClientSendRawEmailTagsTypeDef, _OptionalClientSendRawEmailTagsTypeDef
):
    pass


ClientSendTemplatedEmailDestinationTypeDef = TypedDict(
    "ClientSendTemplatedEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)

ClientSendTemplatedEmailResponseTypeDef = TypedDict(
    "ClientSendTemplatedEmailResponseTypeDef", {"MessageId": str}, total=False
)

_RequiredClientSendTemplatedEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendTemplatedEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendTemplatedEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendTemplatedEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendTemplatedEmailTagsTypeDef(
    _RequiredClientSendTemplatedEmailTagsTypeDef, _OptionalClientSendTemplatedEmailTagsTypeDef
):
    pass


ClientTestRenderTemplateResponseTypeDef = TypedDict(
    "ClientTestRenderTemplateResponseTypeDef", {"RenderedTemplate": str}, total=False
)

ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)

_RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef", {"Name": str}
)
_OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
            ]
        ],
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SNSDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
    _OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
):
    pass


ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef = TypedDict(
    "ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)

ClientUpdateReceiptRuleRuleActionsTypeDef = TypedDict(
    "ClientUpdateReceiptRuleRuleActionsTypeDef",
    {
        "S3Action": ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef,
        "BounceAction": ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef,
        "StopAction": ClientUpdateReceiptRuleRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef,
    },
    total=False,
)

_RequiredClientUpdateReceiptRuleRuleTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleTypeDef", {"Name": str}
)
_OptionalClientUpdateReceiptRuleRuleTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientUpdateReceiptRuleRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientUpdateReceiptRuleRuleTypeDef(
    _RequiredClientUpdateReceiptRuleRuleTypeDef, _OptionalClientUpdateReceiptRuleRuleTypeDef
):
    pass


_RequiredClientUpdateTemplateTemplateTypeDef = TypedDict(
    "_RequiredClientUpdateTemplateTemplateTypeDef", {"TemplateName": str}
)
_OptionalClientUpdateTemplateTemplateTypeDef = TypedDict(
    "_OptionalClientUpdateTemplateTemplateTypeDef",
    {"SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientUpdateTemplateTemplateTypeDef(
    _RequiredClientUpdateTemplateTemplateTypeDef, _OptionalClientUpdateTemplateTemplateTypeDef
):
    pass


ClientVerifyDomainDkimResponseTypeDef = TypedDict(
    "ClientVerifyDomainDkimResponseTypeDef", {"DkimTokens": List[str]}, total=False
)

ClientVerifyDomainIdentityResponseTypeDef = TypedDict(
    "ClientVerifyDomainIdentityResponseTypeDef", {"VerificationToken": str}, total=False
)

ConfigurationSetTypeDef = TypedDict("ConfigurationSetTypeDef", {"Name": str})

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[ConfigurationSetTypeDef], "NextToken": str},
    total=False,
)

CustomVerificationEmailTemplateTypeDef = TypedDict(
    "CustomVerificationEmailTemplateTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[CustomVerificationEmailTemplateTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredListIdentitiesResponseTypeDef = TypedDict(
    "_RequiredListIdentitiesResponseTypeDef", {"Identities": List[str]}
)
_OptionalListIdentitiesResponseTypeDef = TypedDict(
    "_OptionalListIdentitiesResponseTypeDef", {"NextToken": str}, total=False
)


class ListIdentitiesResponseTypeDef(
    _RequiredListIdentitiesResponseTypeDef, _OptionalListIdentitiesResponseTypeDef
):
    pass


ReceiptRuleSetMetadataTypeDef = TypedDict(
    "ReceiptRuleSetMetadataTypeDef", {"Name": str, "CreatedTimestamp": datetime}, total=False
)

ListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseTypeDef",
    {"RuleSets": List[ReceiptRuleSetMetadataTypeDef], "NextToken": str},
    total=False,
)

TemplateMetadataTypeDef = TypedDict(
    "TemplateMetadataTypeDef", {"Name": str, "CreatedTimestamp": datetime}, total=False
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {"TemplatesMetadata": List[TemplateMetadataTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
