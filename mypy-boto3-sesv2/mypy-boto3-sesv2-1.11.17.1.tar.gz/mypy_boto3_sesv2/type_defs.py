"""
Main interface for sesv2 service type definitions.

Usage::

    from mypy_boto3.sesv2.type_defs import ClientCreateConfigurationSetDeliveryOptionsTypeDef

    data: ClientCreateConfigurationSetDeliveryOptionsTypeDef = {...}
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
    "ClientCreateConfigurationSetDeliveryOptionsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientCreateConfigurationSetReputationOptionsTypeDef",
    "ClientCreateConfigurationSetSendingOptionsTypeDef",
    "ClientCreateConfigurationSetSuppressionOptionsTypeDef",
    "ClientCreateConfigurationSetTagsTypeDef",
    "ClientCreateConfigurationSetTrackingOptionsTypeDef",
    "ClientCreateDedicatedIpPoolTagsTypeDef",
    "ClientCreateDeliverabilityTestReportContentRawTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    "ClientCreateDeliverabilityTestReportContentTemplateTypeDef",
    "ClientCreateDeliverabilityTestReportContentTypeDef",
    "ClientCreateDeliverabilityTestReportResponseTypeDef",
    "ClientCreateDeliverabilityTestReportTagsTypeDef",
    "ClientCreateEmailIdentityDkimSigningAttributesTypeDef",
    "ClientCreateEmailIdentityResponseDkimAttributesTypeDef",
    "ClientCreateEmailIdentityResponseTypeDef",
    "ClientCreateEmailIdentityTagsTypeDef",
    "ClientGetAccountResponseSendQuotaTypeDef",
    "ClientGetAccountResponseSuppressionAttributesTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetBlacklistReportsResponseBlacklistReportTypeDef",
    "ClientGetBlacklistReportsResponseTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    "ClientGetConfigurationSetResponseDeliveryOptionsTypeDef",
    "ClientGetConfigurationSetResponseReputationOptionsTypeDef",
    "ClientGetConfigurationSetResponseSendingOptionsTypeDef",
    "ClientGetConfigurationSetResponseSuppressionOptionsTypeDef",
    "ClientGetConfigurationSetResponseTagsTypeDef",
    "ClientGetConfigurationSetResponseTrackingOptionsTypeDef",
    "ClientGetConfigurationSetResponseTypeDef",
    "ClientGetDedicatedIpResponseDedicatedIpTypeDef",
    "ClientGetDedicatedIpResponseTypeDef",
    "ClientGetDedicatedIpsResponseDedicatedIpsTypeDef",
    "ClientGetDedicatedIpsResponseTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseTypeDef",
    "ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef",
    "ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef",
    "ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef",
    "ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef",
    "ClientGetDeliverabilityTestReportResponseTagsTypeDef",
    "ClientGetDeliverabilityTestReportResponseTypeDef",
    "ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef",
    "ClientGetDomainDeliverabilityCampaignResponseTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef",
    "ClientGetDomainStatisticsReportResponseTypeDef",
    "ClientGetEmailIdentityResponseDkimAttributesTypeDef",
    "ClientGetEmailIdentityResponseMailFromAttributesTypeDef",
    "ClientGetEmailIdentityResponseTagsTypeDef",
    "ClientGetEmailIdentityResponseTypeDef",
    "ClientGetSuppressedDestinationResponseSuppressedDestinationAttributesTypeDef",
    "ClientGetSuppressedDestinationResponseSuppressedDestinationTypeDef",
    "ClientGetSuppressedDestinationResponseTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientListDedicatedIpPoolsResponseTypeDef",
    "ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef",
    "ClientListDeliverabilityTestReportsResponseTypeDef",
    "ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef",
    "ClientListDomainDeliverabilityCampaignsResponseTypeDef",
    "ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef",
    "ClientListEmailIdentitiesResponseTypeDef",
    "ClientListSuppressedDestinationsResponseSuppressedDestinationSummariesTypeDef",
    "ClientListSuppressedDestinationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef",
    "ClientPutEmailIdentityDkimSigningAttributesResponseTypeDef",
    "ClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef",
    "ClientSendEmailContentRawTypeDef",
    "ClientSendEmailContentSimpleBodyHtmlTypeDef",
    "ClientSendEmailContentSimpleBodyTextTypeDef",
    "ClientSendEmailContentSimpleBodyTypeDef",
    "ClientSendEmailContentSimpleSubjectTypeDef",
    "ClientSendEmailContentSimpleTypeDef",
    "ClientSendEmailContentTemplateTypeDef",
    "ClientSendEmailContentTypeDef",
    "ClientSendEmailDestinationTypeDef",
    "ClientSendEmailEmailTagsTypeDef",
    "ClientSendEmailResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
)

ClientCreateConfigurationSetDeliveryOptionsTypeDef = TypedDict(
    "ClientCreateConfigurationSetDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["REQUIRE", "OPTIONAL"], "SendingPoolName": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
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
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
            ]
        ],
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SnsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
        "PinpointDestination": ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef,
    },
    total=False,
)

ClientCreateConfigurationSetReputationOptionsTypeDef = TypedDict(
    "ClientCreateConfigurationSetReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)

ClientCreateConfigurationSetSendingOptionsTypeDef = TypedDict(
    "ClientCreateConfigurationSetSendingOptionsTypeDef", {"SendingEnabled": bool}, total=False
)

ClientCreateConfigurationSetSuppressionOptionsTypeDef = TypedDict(
    "ClientCreateConfigurationSetSuppressionOptionsTypeDef",
    {"SuppressedReasons": List[Literal["BOUNCE", "COMPLAINT"]]},
    total=False,
)

_RequiredClientCreateConfigurationSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateConfigurationSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateConfigurationSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateConfigurationSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateConfigurationSetTagsTypeDef(
    _RequiredClientCreateConfigurationSetTagsTypeDef,
    _OptionalClientCreateConfigurationSetTagsTypeDef,
):
    pass


ClientCreateConfigurationSetTrackingOptionsTypeDef = TypedDict(
    "ClientCreateConfigurationSetTrackingOptionsTypeDef", {"CustomRedirectDomain": str}
)

_RequiredClientCreateDedicatedIpPoolTagsTypeDef = TypedDict(
    "_RequiredClientCreateDedicatedIpPoolTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDedicatedIpPoolTagsTypeDef = TypedDict(
    "_OptionalClientCreateDedicatedIpPoolTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDedicatedIpPoolTagsTypeDef(
    _RequiredClientCreateDedicatedIpPoolTagsTypeDef, _OptionalClientCreateDedicatedIpPoolTagsTypeDef
):
    pass


ClientCreateDeliverabilityTestReportContentRawTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportContentRawTypeDef", {"Data": bytes}, total=False
)

ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    {"Data": str, "Charset": str},
    total=False,
)

ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    {"Data": str, "Charset": str},
    total=False,
)

ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef",
    {
        "Text": ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef,
        "Html": ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef,
    },
    total=False,
)

_RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef", {"Data": str}
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    {"Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
):
    pass


_RequiredClientCreateDeliverabilityTestReportContentSimpleTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    {"Subject": ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef},
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    {"Body": ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleTypeDef,
):
    pass


ClientCreateDeliverabilityTestReportContentTemplateTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportContentTemplateTypeDef",
    {"TemplateArn": str, "TemplateData": str},
    total=False,
)

ClientCreateDeliverabilityTestReportContentTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportContentTypeDef",
    {
        "Simple": ClientCreateDeliverabilityTestReportContentSimpleTypeDef,
        "Raw": ClientCreateDeliverabilityTestReportContentRawTypeDef,
        "Template": ClientCreateDeliverabilityTestReportContentTemplateTypeDef,
    },
    total=False,
)

ClientCreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "ClientCreateDeliverabilityTestReportResponseTypeDef",
    {"ReportId": str, "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"]},
    total=False,
)

_RequiredClientCreateDeliverabilityTestReportTagsTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDeliverabilityTestReportTagsTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDeliverabilityTestReportTagsTypeDef(
    _RequiredClientCreateDeliverabilityTestReportTagsTypeDef,
    _OptionalClientCreateDeliverabilityTestReportTagsTypeDef,
):
    pass


_RequiredClientCreateEmailIdentityDkimSigningAttributesTypeDef = TypedDict(
    "_RequiredClientCreateEmailIdentityDkimSigningAttributesTypeDef", {"DomainSigningSelector": str}
)
_OptionalClientCreateEmailIdentityDkimSigningAttributesTypeDef = TypedDict(
    "_OptionalClientCreateEmailIdentityDkimSigningAttributesTypeDef",
    {"DomainSigningPrivateKey": str},
    total=False,
)


class ClientCreateEmailIdentityDkimSigningAttributesTypeDef(
    _RequiredClientCreateEmailIdentityDkimSigningAttributesTypeDef,
    _OptionalClientCreateEmailIdentityDkimSigningAttributesTypeDef,
):
    pass


ClientCreateEmailIdentityResponseDkimAttributesTypeDef = TypedDict(
    "ClientCreateEmailIdentityResponseDkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "Tokens": List[str],
        "SigningAttributesOrigin": Literal["AWS_SES", "EXTERNAL"],
    },
    total=False,
)

ClientCreateEmailIdentityResponseTypeDef = TypedDict(
    "ClientCreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": ClientCreateEmailIdentityResponseDkimAttributesTypeDef,
    },
    total=False,
)

_RequiredClientCreateEmailIdentityTagsTypeDef = TypedDict(
    "_RequiredClientCreateEmailIdentityTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEmailIdentityTagsTypeDef = TypedDict(
    "_OptionalClientCreateEmailIdentityTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEmailIdentityTagsTypeDef(
    _RequiredClientCreateEmailIdentityTagsTypeDef, _OptionalClientCreateEmailIdentityTagsTypeDef
):
    pass


ClientGetAccountResponseSendQuotaTypeDef = TypedDict(
    "ClientGetAccountResponseSendQuotaTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)

ClientGetAccountResponseSuppressionAttributesTypeDef = TypedDict(
    "ClientGetAccountResponseSuppressionAttributesTypeDef",
    {"SuppressedReasons": List[Literal["BOUNCE", "COMPLAINT"]]},
    total=False,
)

ClientGetAccountResponseTypeDef = TypedDict(
    "ClientGetAccountResponseTypeDef",
    {
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "SendQuota": ClientGetAccountResponseSendQuotaTypeDef,
        "SendingEnabled": bool,
        "SuppressionAttributes": ClientGetAccountResponseSuppressionAttributesTypeDef,
    },
    total=False,
)

ClientGetBlacklistReportsResponseBlacklistReportTypeDef = TypedDict(
    "ClientGetBlacklistReportsResponseBlacklistReportTypeDef",
    {"RblName": str, "ListingTime": datetime, "Description": str},
    total=False,
)

ClientGetBlacklistReportsResponseTypeDef = TypedDict(
    "ClientGetBlacklistReportsResponseTypeDef",
    {"BlacklistReport": Dict[str, List[ClientGetBlacklistReportsResponseBlacklistReportTypeDef]]},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
        "DefaultDimensionValue": str,
    },
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
            ]
        ],
        "KinesisFirehoseDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef,
        "SnsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef,
        "PinpointDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef,
    },
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
        ]
    },
    total=False,
)

ClientGetConfigurationSetResponseDeliveryOptionsTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["REQUIRE", "OPTIONAL"], "SendingPoolName": str},
    total=False,
)

ClientGetConfigurationSetResponseReputationOptionsTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)

ClientGetConfigurationSetResponseSendingOptionsTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseSendingOptionsTypeDef", {"SendingEnabled": bool}, total=False
)

ClientGetConfigurationSetResponseSuppressionOptionsTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseSuppressionOptionsTypeDef",
    {"SuppressedReasons": List[Literal["BOUNCE", "COMPLAINT"]]},
    total=False,
)

ClientGetConfigurationSetResponseTagsTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetConfigurationSetResponseTrackingOptionsTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)

ClientGetConfigurationSetResponseTypeDef = TypedDict(
    "ClientGetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": ClientGetConfigurationSetResponseTrackingOptionsTypeDef,
        "DeliveryOptions": ClientGetConfigurationSetResponseDeliveryOptionsTypeDef,
        "ReputationOptions": ClientGetConfigurationSetResponseReputationOptionsTypeDef,
        "SendingOptions": ClientGetConfigurationSetResponseSendingOptionsTypeDef,
        "Tags": List[ClientGetConfigurationSetResponseTagsTypeDef],
        "SuppressionOptions": ClientGetConfigurationSetResponseSuppressionOptionsTypeDef,
    },
    total=False,
)

ClientGetDedicatedIpResponseDedicatedIpTypeDef = TypedDict(
    "ClientGetDedicatedIpResponseDedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": Literal["IN_PROGRESS", "DONE"],
        "WarmupPercentage": int,
        "PoolName": str,
    },
    total=False,
)

ClientGetDedicatedIpResponseTypeDef = TypedDict(
    "ClientGetDedicatedIpResponseTypeDef",
    {"DedicatedIp": ClientGetDedicatedIpResponseDedicatedIpTypeDef},
    total=False,
)

ClientGetDedicatedIpsResponseDedicatedIpsTypeDef = TypedDict(
    "ClientGetDedicatedIpsResponseDedicatedIpsTypeDef",
    {
        "Ip": str,
        "WarmupStatus": Literal["IN_PROGRESS", "DONE"],
        "WarmupPercentage": int,
        "PoolName": str,
    },
    total=False,
)

ClientGetDedicatedIpsResponseTypeDef = TypedDict(
    "ClientGetDedicatedIpsResponseTypeDef",
    {"DedicatedIps": List[ClientGetDedicatedIpsResponseDedicatedIpsTypeDef], "NextToken": str},
    total=False,
)

ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)

ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef = TypedDict(
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)

ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)

ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef = TypedDict(
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)

ClientGetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "ClientGetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": Literal["ACTIVE", "PENDING_EXPIRATION", "DISABLED"],
        "ActiveSubscribedDomains": List[
            ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef
        ],
        "PendingExpirationSubscribedDomains": List[
            ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef
        ],
    },
    total=False,
)

ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef = TypedDict(
    "ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"],
    },
    total=False,
)

ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef = TypedDict(
    "ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)

ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef = TypedDict(
    "ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef",
    {
        "IspName": str,
        "PlacementStatistics": ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef,
    },
    total=False,
)

ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef = TypedDict(
    "ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)

ClientGetDeliverabilityTestReportResponseTagsTypeDef = TypedDict(
    "ClientGetDeliverabilityTestReportResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "ClientGetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef,
        "OverallPlacement": ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef,
        "IspPlacements": List[ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef],
        "Message": str,
        "Tags": List[ClientGetDeliverabilityTestReportResponseTagsTypeDef],
    },
    total=False,
)

ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef = TypedDict(
    "ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)

ClientGetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "ClientGetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef
    },
    total=False,
)

ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)

ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef",
    {"InboxRawCount": int, "SpamRawCount": int, "ProjectedInbox": int, "ProjectedSpam": int},
    total=False,
)

ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef",
    {
        "StartDate": datetime,
        "VolumeStatistics": ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef,
        "DomainIspPlacements": List[
            ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef
        ],
    },
    total=False,
)

ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)

ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef",
    {"InboxRawCount": int, "SpamRawCount": int, "ProjectedInbox": int, "ProjectedSpam": int},
    total=False,
)

ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef",
    {
        "VolumeStatistics": ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef,
        "ReadRatePercent": float,
        "DomainIspPlacements": List[
            ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef
        ],
    },
    total=False,
)

ClientGetDomainStatisticsReportResponseTypeDef = TypedDict(
    "ClientGetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef,
        "DailyVolumes": List[ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef],
    },
    total=False,
)

ClientGetEmailIdentityResponseDkimAttributesTypeDef = TypedDict(
    "ClientGetEmailIdentityResponseDkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "Tokens": List[str],
        "SigningAttributesOrigin": Literal["AWS_SES", "EXTERNAL"],
    },
    total=False,
)

ClientGetEmailIdentityResponseMailFromAttributesTypeDef = TypedDict(
    "ClientGetEmailIdentityResponseMailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE"],
        "BehaviorOnMxFailure": Literal["USE_DEFAULT_VALUE", "REJECT_MESSAGE"],
    },
    total=False,
)

ClientGetEmailIdentityResponseTagsTypeDef = TypedDict(
    "ClientGetEmailIdentityResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetEmailIdentityResponseTypeDef = TypedDict(
    "ClientGetEmailIdentityResponseTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": ClientGetEmailIdentityResponseDkimAttributesTypeDef,
        "MailFromAttributes": ClientGetEmailIdentityResponseMailFromAttributesTypeDef,
        "Tags": List[ClientGetEmailIdentityResponseTagsTypeDef],
    },
    total=False,
)

ClientGetSuppressedDestinationResponseSuppressedDestinationAttributesTypeDef = TypedDict(
    "ClientGetSuppressedDestinationResponseSuppressedDestinationAttributesTypeDef",
    {"MessageId": str, "FeedbackId": str},
    total=False,
)

ClientGetSuppressedDestinationResponseSuppressedDestinationTypeDef = TypedDict(
    "ClientGetSuppressedDestinationResponseSuppressedDestinationTypeDef",
    {
        "EmailAddress": str,
        "Reason": Literal["BOUNCE", "COMPLAINT"],
        "LastUpdateTime": datetime,
        "Attributes": ClientGetSuppressedDestinationResponseSuppressedDestinationAttributesTypeDef,
    },
    total=False,
)

ClientGetSuppressedDestinationResponseTypeDef = TypedDict(
    "ClientGetSuppressedDestinationResponseTypeDef",
    {"SuppressedDestination": ClientGetSuppressedDestinationResponseSuppressedDestinationTypeDef},
    total=False,
)

ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "ClientListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[str], "NextToken": str},
    total=False,
)

ClientListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "ClientListDedicatedIpPoolsResponseTypeDef",
    {"DedicatedIpPools": List[str], "NextToken": str},
    total=False,
)

ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef = TypedDict(
    "ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"],
    },
    total=False,
)

ClientListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "ClientListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List[
            ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef = TypedDict(
    "ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)

ClientListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "ClientListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List[
            ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef = TypedDict(
    "ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)

ClientListEmailIdentitiesResponseTypeDef = TypedDict(
    "ClientListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List[ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSuppressedDestinationsResponseSuppressedDestinationSummariesTypeDef = TypedDict(
    "ClientListSuppressedDestinationsResponseSuppressedDestinationSummariesTypeDef",
    {"EmailAddress": str, "Reason": Literal["BOUNCE", "COMPLAINT"], "LastUpdateTime": datetime},
    total=False,
)

ClientListSuppressedDestinationsResponseTypeDef = TypedDict(
    "ClientListSuppressedDestinationsResponseTypeDef",
    {
        "SuppressedDestinationSummaries": List[
            ClientListSuppressedDestinationsResponseSuppressedDestinationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)

ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef = TypedDict(
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)

ClientPutEmailIdentityDkimSigningAttributesResponseTypeDef = TypedDict(
    "ClientPutEmailIdentityDkimSigningAttributesResponseTypeDef",
    {
        "DkimStatus": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "DkimTokens": List[str],
    },
    total=False,
)

_RequiredClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef = TypedDict(
    "_RequiredClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef",
    {"DomainSigningSelector": str},
)
_OptionalClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef = TypedDict(
    "_OptionalClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef",
    {"DomainSigningPrivateKey": str},
    total=False,
)


class ClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef(
    _RequiredClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef,
    _OptionalClientPutEmailIdentityDkimSigningAttributesSigningAttributesTypeDef,
):
    pass


ClientSendEmailContentRawTypeDef = TypedDict(
    "ClientSendEmailContentRawTypeDef", {"Data": bytes}, total=False
)

ClientSendEmailContentSimpleBodyHtmlTypeDef = TypedDict(
    "ClientSendEmailContentSimpleBodyHtmlTypeDef", {"Data": str, "Charset": str}, total=False
)

ClientSendEmailContentSimpleBodyTextTypeDef = TypedDict(
    "ClientSendEmailContentSimpleBodyTextTypeDef", {"Data": str, "Charset": str}, total=False
)

ClientSendEmailContentSimpleBodyTypeDef = TypedDict(
    "ClientSendEmailContentSimpleBodyTypeDef",
    {
        "Text": ClientSendEmailContentSimpleBodyTextTypeDef,
        "Html": ClientSendEmailContentSimpleBodyHtmlTypeDef,
    },
    total=False,
)

_RequiredClientSendEmailContentSimpleSubjectTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleSubjectTypeDef", {"Data": str}
)
_OptionalClientSendEmailContentSimpleSubjectTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleSubjectTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailContentSimpleSubjectTypeDef(
    _RequiredClientSendEmailContentSimpleSubjectTypeDef,
    _OptionalClientSendEmailContentSimpleSubjectTypeDef,
):
    pass


_RequiredClientSendEmailContentSimpleTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleTypeDef",
    {"Subject": ClientSendEmailContentSimpleSubjectTypeDef},
)
_OptionalClientSendEmailContentSimpleTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleTypeDef",
    {"Body": ClientSendEmailContentSimpleBodyTypeDef},
    total=False,
)


class ClientSendEmailContentSimpleTypeDef(
    _RequiredClientSendEmailContentSimpleTypeDef, _OptionalClientSendEmailContentSimpleTypeDef
):
    pass


ClientSendEmailContentTemplateTypeDef = TypedDict(
    "ClientSendEmailContentTemplateTypeDef", {"TemplateArn": str, "TemplateData": str}, total=False
)

ClientSendEmailContentTypeDef = TypedDict(
    "ClientSendEmailContentTypeDef",
    {
        "Simple": ClientSendEmailContentSimpleTypeDef,
        "Raw": ClientSendEmailContentRawTypeDef,
        "Template": ClientSendEmailContentTemplateTypeDef,
    },
    total=False,
)

ClientSendEmailDestinationTypeDef = TypedDict(
    "ClientSendEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)

_RequiredClientSendEmailEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendEmailEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendEmailEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendEmailEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendEmailEmailTagsTypeDef(
    _RequiredClientSendEmailEmailTagsTypeDef, _OptionalClientSendEmailEmailTagsTypeDef
):
    pass


ClientSendEmailResponseTypeDef = TypedDict(
    "ClientSendEmailResponseTypeDef", {"MessageId": str}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
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
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
            ]
        ],
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SnsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
        "PinpointDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef,
    },
    total=False,
)
