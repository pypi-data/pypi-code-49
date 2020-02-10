"""
Main interface for es service type definitions.

Usage::

    from mypy_boto3.es.type_defs import ClientAddTagsTagListTypeDef

    data: ClientAddTagsTagListTypeDef = {...}
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
    "ClientAddTagsTagListTypeDef",
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ClientCreateElasticsearchDomainCognitoOptionsTypeDef",
    "ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef",
    "ClientCreateElasticsearchDomainEBSOptionsTypeDef",
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef",
    "ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef",
    "ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientCreateElasticsearchDomainResponseTypeDef",
    "ClientCreateElasticsearchDomainSnapshotOptionsTypeDef",
    "ClientCreateElasticsearchDomainVPCOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientDeleteElasticsearchDomainResponseTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientDescribeElasticsearchDomainResponseTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef",
    "ClientDescribeElasticsearchDomainsResponseTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseTypeDef",
    "ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef",
    "ClientGetCompatibleElasticsearchVersionsResponseTypeDef",
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef",
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef",
    "ClientGetUpgradeHistoryResponseTypeDef",
    "ClientGetUpgradeStatusResponseTypeDef",
    "ClientListDomainNamesResponseDomainNamesTypeDef",
    "ClientListDomainNamesResponseTypeDef",
    "ClientListElasticsearchInstanceTypesResponseTypeDef",
    "ClientListElasticsearchVersionsResponseTypeDef",
    "ClientListTagsResponseTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    "ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseTypeDef",
    "ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef",
    "ClientUpgradeElasticsearchDomainResponseTypeDef",
    "RecurringChargeTypeDef",
    "ReservedElasticsearchInstanceOfferingTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "ReservedElasticsearchInstanceTypeDef",
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    "UpgradeStepItemTypeDef",
    "UpgradeHistoryTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "ListElasticsearchInstanceTypesResponseTypeDef",
    "ListElasticsearchVersionsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredClientAddTagsTagListTypeDef = TypedDict(
    "_RequiredClientAddTagsTagListTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagListTypeDef = TypedDict(
    "_OptionalClientAddTagsTagListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagListTypeDef(
    _RequiredClientAddTagsTagListTypeDef, _OptionalClientAddTagsTagListTypeDef
):
    pass


ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef = TypedDict(
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)

ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
    },
    total=False,
)

ClientCreateElasticsearchDomainCognitoOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientCreateElasticsearchDomainEBSOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ClientCreateElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str, ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
        ],
        "ServiceSoftwareOptions": ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)

ClientCreateElasticsearchDomainResponseTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientCreateElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)

ClientCreateElasticsearchDomainSnapshotOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientCreateElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "ClientCreateElasticsearchDomainVPCOptionsTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str, ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
        ],
        "ServiceSoftwareOptions": ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)

ClientDeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "ClientDeleteElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    {
        "Options": Dict[str, str],
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    {
        "Options": Dict[
            str,
            ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef,
        ],
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef",
    {
        "ElasticsearchVersion": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef,
        "AccessPolicies": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef,
        "SnapshotOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef,
        "LogPublishingOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str, ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
        ],
        "ServiceSoftwareOptions": ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str,
            ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef,
        ],
        "ServiceSoftwareOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef,
    },
    total=False,
)

ClientDescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "ClientDescribeElasticsearchDomainsResponseTypeDef",
    {"DomainStatusList": List[ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef]},
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef",
    {"LimitName": str, "LimitValues": List[str]},
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef",
    {"MinimumInstanceCount": int, "MaximumInstanceCount": int},
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef",
    {
        "InstanceCountLimits": ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef
    },
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef",
    {"LimitName": str, "LimitValues": List[str]},
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef",
    {
        "StorageTypeName": str,
        "StorageSubTypeName": str,
        "StorageTypeLimits": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef
        ],
    },
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef",
    {
        "StorageTypes": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef
        ],
        "InstanceLimits": ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef,
        "AdditionalLimits": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef
        ],
    },
    total=False,
)

ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[
            str, ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef
        ]
    },
    total=False,
)

ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef = TypedDict(
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[
            ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef = TypedDict(
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef = TypedDict(
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[
            ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientDescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "ClientDescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List[
            ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef
        ],
    },
    total=False,
)

ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef = TypedDict(
    "ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef",
    {"SourceVersion": str, "TargetVersions": List[str]},
    total=False,
)

ClientGetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "ClientGetCompatibleElasticsearchVersionsResponseTypeDef",
    {
        "CompatibleElasticsearchVersions": List[
            ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef
        ]
    },
    total=False,
)

ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef = TypedDict(
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "UpgradeStepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)

ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef = TypedDict(
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "StepsList": List[ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef],
    },
    total=False,
)

ClientGetUpgradeHistoryResponseTypeDef = TypedDict(
    "ClientGetUpgradeHistoryResponseTypeDef",
    {
        "UpgradeHistories": List[ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetUpgradeStatusResponseTypeDef = TypedDict(
    "ClientGetUpgradeStatusResponseTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "StepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "UpgradeName": str,
    },
    total=False,
)

ClientListDomainNamesResponseDomainNamesTypeDef = TypedDict(
    "ClientListDomainNamesResponseDomainNamesTypeDef", {"DomainName": str}, total=False
)

ClientListDomainNamesResponseTypeDef = TypedDict(
    "ClientListDomainNamesResponseTypeDef",
    {"DomainNames": List[ClientListDomainNamesResponseDomainNamesTypeDef]},
    total=False,
)

ClientListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "ClientListElasticsearchInstanceTypesResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[
            Literal[
                "m3.medium.elasticsearch",
                "m3.large.elasticsearch",
                "m3.xlarge.elasticsearch",
                "m3.2xlarge.elasticsearch",
                "m4.large.elasticsearch",
                "m4.xlarge.elasticsearch",
                "m4.2xlarge.elasticsearch",
                "m4.4xlarge.elasticsearch",
                "m4.10xlarge.elasticsearch",
                "m5.large.elasticsearch",
                "m5.xlarge.elasticsearch",
                "m5.2xlarge.elasticsearch",
                "m5.4xlarge.elasticsearch",
                "m5.12xlarge.elasticsearch",
                "r5.large.elasticsearch",
                "r5.xlarge.elasticsearch",
                "r5.2xlarge.elasticsearch",
                "r5.4xlarge.elasticsearch",
                "r5.12xlarge.elasticsearch",
                "c5.large.elasticsearch",
                "c5.xlarge.elasticsearch",
                "c5.2xlarge.elasticsearch",
                "c5.4xlarge.elasticsearch",
                "c5.9xlarge.elasticsearch",
                "c5.18xlarge.elasticsearch",
                "ultrawarm1.medium.elasticsearch",
                "ultrawarm1.large.elasticsearch",
                "t2.micro.elasticsearch",
                "t2.small.elasticsearch",
                "t2.medium.elasticsearch",
                "r3.large.elasticsearch",
                "r3.xlarge.elasticsearch",
                "r3.2xlarge.elasticsearch",
                "r3.4xlarge.elasticsearch",
                "r3.8xlarge.elasticsearch",
                "i2.xlarge.elasticsearch",
                "i2.2xlarge.elasticsearch",
                "d2.xlarge.elasticsearch",
                "d2.2xlarge.elasticsearch",
                "d2.4xlarge.elasticsearch",
                "d2.8xlarge.elasticsearch",
                "c4.large.elasticsearch",
                "c4.xlarge.elasticsearch",
                "c4.2xlarge.elasticsearch",
                "c4.4xlarge.elasticsearch",
                "c4.8xlarge.elasticsearch",
                "r4.large.elasticsearch",
                "r4.xlarge.elasticsearch",
                "r4.2xlarge.elasticsearch",
                "r4.4xlarge.elasticsearch",
                "r4.8xlarge.elasticsearch",
                "r4.16xlarge.elasticsearch",
                "i3.large.elasticsearch",
                "i3.xlarge.elasticsearch",
                "i3.2xlarge.elasticsearch",
                "i3.4xlarge.elasticsearch",
                "i3.8xlarge.elasticsearch",
                "i3.16xlarge.elasticsearch",
            ]
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListElasticsearchVersionsResponseTypeDef = TypedDict(
    "ClientListElasticsearchVersionsResponseTypeDef",
    {"ElasticsearchVersions": List[str], "NextToken": str},
    total=False,
)

ClientListTagsResponseTagListTypeDef = TypedDict(
    "ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef]},
    total=False,
)

ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {"ReservedElasticsearchInstanceId": str, "ReservationName": str},
    total=False,
)

ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef = TypedDict(
    "ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)

ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    {
        "Options": Dict[str, str],
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": Literal["ultrawarm1.medium.elasticsearch", "ultrawarm1.large.elasticsearch"],
        "WarmCount": int,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    {
        "Options": Dict[
            str,
            ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef,
        ],
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef",
    {
        "ElasticsearchVersion": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef,
        "ElasticsearchClusterConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef,
        "AccessPolicies": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef,
        "SnapshotOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef,
        "VPCOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef,
        "CognitoOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef,
        "LogPublishingOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef,
        "DomainEndpointOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef,
    },
    total=False,
)

ClientUpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef},
    total=False,
)

ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)

ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef = TypedDict(
    "ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientUpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "ClientUpgradeElasticsearchDomainResponseTypeDef",
    {"DomainName": str, "TargetVersion": str, "PerformCheckOnly": bool},
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedElasticsearchInstanceOfferingTypeDef = TypedDict(
    "ReservedElasticsearchInstanceOfferingTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[RecurringChargeTypeDef],
    },
    total=False,
)

DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            ReservedElasticsearchInstanceOfferingTypeDef
        ],
    },
    total=False,
)

ReservedElasticsearchInstanceTypeDef = TypedDict(
    "ReservedElasticsearchInstanceTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[RecurringChargeTypeDef],
    },
    total=False,
)

DescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List[ReservedElasticsearchInstanceTypeDef],
    },
    total=False,
)

UpgradeStepItemTypeDef = TypedDict(
    "UpgradeStepItemTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "UpgradeStepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)

UpgradeHistoryTypeDef = TypedDict(
    "UpgradeHistoryTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "StepsList": List[UpgradeStepItemTypeDef],
    },
    total=False,
)

GetUpgradeHistoryResponseTypeDef = TypedDict(
    "GetUpgradeHistoryResponseTypeDef",
    {"UpgradeHistories": List[UpgradeHistoryTypeDef], "NextToken": str},
    total=False,
)

ListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[
            Literal[
                "m3.medium.elasticsearch",
                "m3.large.elasticsearch",
                "m3.xlarge.elasticsearch",
                "m3.2xlarge.elasticsearch",
                "m4.large.elasticsearch",
                "m4.xlarge.elasticsearch",
                "m4.2xlarge.elasticsearch",
                "m4.4xlarge.elasticsearch",
                "m4.10xlarge.elasticsearch",
                "m5.large.elasticsearch",
                "m5.xlarge.elasticsearch",
                "m5.2xlarge.elasticsearch",
                "m5.4xlarge.elasticsearch",
                "m5.12xlarge.elasticsearch",
                "r5.large.elasticsearch",
                "r5.xlarge.elasticsearch",
                "r5.2xlarge.elasticsearch",
                "r5.4xlarge.elasticsearch",
                "r5.12xlarge.elasticsearch",
                "c5.large.elasticsearch",
                "c5.xlarge.elasticsearch",
                "c5.2xlarge.elasticsearch",
                "c5.4xlarge.elasticsearch",
                "c5.9xlarge.elasticsearch",
                "c5.18xlarge.elasticsearch",
                "ultrawarm1.medium.elasticsearch",
                "ultrawarm1.large.elasticsearch",
                "t2.micro.elasticsearch",
                "t2.small.elasticsearch",
                "t2.medium.elasticsearch",
                "r3.large.elasticsearch",
                "r3.xlarge.elasticsearch",
                "r3.2xlarge.elasticsearch",
                "r3.4xlarge.elasticsearch",
                "r3.8xlarge.elasticsearch",
                "i2.xlarge.elasticsearch",
                "i2.2xlarge.elasticsearch",
                "d2.xlarge.elasticsearch",
                "d2.2xlarge.elasticsearch",
                "d2.4xlarge.elasticsearch",
                "d2.8xlarge.elasticsearch",
                "c4.large.elasticsearch",
                "c4.xlarge.elasticsearch",
                "c4.2xlarge.elasticsearch",
                "c4.4xlarge.elasticsearch",
                "c4.8xlarge.elasticsearch",
                "r4.large.elasticsearch",
                "r4.xlarge.elasticsearch",
                "r4.2xlarge.elasticsearch",
                "r4.4xlarge.elasticsearch",
                "r4.8xlarge.elasticsearch",
                "r4.16xlarge.elasticsearch",
                "i3.large.elasticsearch",
                "i3.xlarge.elasticsearch",
                "i3.2xlarge.elasticsearch",
                "i3.4xlarge.elasticsearch",
                "i3.8xlarge.elasticsearch",
                "i3.16xlarge.elasticsearch",
            ]
        ],
        "NextToken": str,
    },
    total=False,
)

ListElasticsearchVersionsResponseTypeDef = TypedDict(
    "ListElasticsearchVersionsResponseTypeDef",
    {"ElasticsearchVersions": List[str], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
