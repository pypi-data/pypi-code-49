"""
Main interface for ds service type definitions.

Usage::

    from mypy_boto3.ds.type_defs import ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef

    data: ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef = {...}
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
    "ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef",
    "ClientAcceptSharedDirectoryResponseTypeDef",
    "ClientAddIpRoutesIpRoutesTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientConnectDirectoryConnectSettingsTypeDef",
    "ClientConnectDirectoryResponseTypeDef",
    "ClientConnectDirectoryTagsTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateComputerComputerAttributesTypeDef",
    "ClientCreateComputerResponseComputerComputerAttributesTypeDef",
    "ClientCreateComputerResponseComputerTypeDef",
    "ClientCreateComputerResponseTypeDef",
    "ClientCreateDirectoryResponseTypeDef",
    "ClientCreateDirectoryTagsTypeDef",
    "ClientCreateDirectoryVpcSettingsTypeDef",
    "ClientCreateMicrosoftAdResponseTypeDef",
    "ClientCreateMicrosoftAdTagsTypeDef",
    "ClientCreateMicrosoftAdVpcSettingsTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientCreateTrustResponseTypeDef",
    "ClientDeleteDirectoryResponseTypeDef",
    "ClientDeleteSnapshotResponseTypeDef",
    "ClientDeleteTrustResponseTypeDef",
    "ClientDescribeCertificateResponseCertificateTypeDef",
    "ClientDescribeCertificateResponseTypeDef",
    "ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef",
    "ClientDescribeConditionalForwardersResponseTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef",
    "ClientDescribeDirectoriesResponseTypeDef",
    "ClientDescribeDomainControllersResponseDomainControllersTypeDef",
    "ClientDescribeDomainControllersResponseTypeDef",
    "ClientDescribeEventTopicsResponseEventTopicsTypeDef",
    "ClientDescribeEventTopicsResponseTypeDef",
    "ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef",
    "ClientDescribeLdapsSettingsResponseTypeDef",
    "ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef",
    "ClientDescribeSharedDirectoriesResponseTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseTypeDef",
    "ClientDescribeTrustsResponseTrustsTypeDef",
    "ClientDescribeTrustsResponseTypeDef",
    "ClientEnableRadiusRadiusSettingsTypeDef",
    "ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef",
    "ClientGetDirectoryLimitsResponseTypeDef",
    "ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef",
    "ClientGetSnapshotLimitsResponseTypeDef",
    "ClientListCertificatesResponseCertificatesInfoTypeDef",
    "ClientListCertificatesResponseTypeDef",
    "ClientListIpRoutesResponseIpRoutesInfoTypeDef",
    "ClientListIpRoutesResponseTypeDef",
    "ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef",
    "ClientListLogSubscriptionsResponseTypeDef",
    "ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef",
    "ClientListSchemaExtensionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRegisterCertificateResponseTypeDef",
    "ClientRejectSharedDirectoryResponseTypeDef",
    "ClientShareDirectoryResponseTypeDef",
    "ClientShareDirectoryShareTargetTypeDef",
    "ClientStartSchemaExtensionResponseTypeDef",
    "ClientUnshareDirectoryResponseTypeDef",
    "ClientUnshareDirectoryUnshareTargetTypeDef",
    "ClientUpdateRadiusRadiusSettingsTypeDef",
    "ClientUpdateTrustResponseTypeDef",
    "ClientVerifyTrustResponseTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "RadiusSettingsTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "DirectoryDescriptionTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DomainControllerTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "SharedDirectoryTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "SnapshotTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "TrustTypeDef",
    "DescribeTrustsResultTypeDef",
    "IpRouteInfoTypeDef",
    "ListIpRoutesResultTypeDef",
    "LogSubscriptionTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "TagTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef = TypedDict(
    "ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientAcceptSharedDirectoryResponseTypeDef = TypedDict(
    "ClientAcceptSharedDirectoryResponseTypeDef",
    {"SharedDirectory": ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef},
    total=False,
)

ClientAddIpRoutesIpRoutesTypeDef = TypedDict(
    "ClientAddIpRoutesIpRoutesTypeDef", {"CidrIp": str, "Description": str}, total=False
)

_RequiredClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_RequiredClientAddTagsToResourceTagsTypeDef", {"Key": str}
)
_OptionalClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsToResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(
    _RequiredClientAddTagsToResourceTagsTypeDef, _OptionalClientAddTagsToResourceTagsTypeDef
):
    pass


_RequiredClientConnectDirectoryConnectSettingsTypeDef = TypedDict(
    "_RequiredClientConnectDirectoryConnectSettingsTypeDef", {"VpcId": str}
)
_OptionalClientConnectDirectoryConnectSettingsTypeDef = TypedDict(
    "_OptionalClientConnectDirectoryConnectSettingsTypeDef",
    {"SubnetIds": List[str], "CustomerDnsIps": List[str], "CustomerUserName": str},
    total=False,
)


class ClientConnectDirectoryConnectSettingsTypeDef(
    _RequiredClientConnectDirectoryConnectSettingsTypeDef,
    _OptionalClientConnectDirectoryConnectSettingsTypeDef,
):
    pass


ClientConnectDirectoryResponseTypeDef = TypedDict(
    "ClientConnectDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)

_RequiredClientConnectDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientConnectDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientConnectDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientConnectDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientConnectDirectoryTagsTypeDef(
    _RequiredClientConnectDirectoryTagsTypeDef, _OptionalClientConnectDirectoryTagsTypeDef
):
    pass


ClientCreateAliasResponseTypeDef = TypedDict(
    "ClientCreateAliasResponseTypeDef", {"DirectoryId": str, "Alias": str}, total=False
)

ClientCreateComputerComputerAttributesTypeDef = TypedDict(
    "ClientCreateComputerComputerAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientCreateComputerResponseComputerComputerAttributesTypeDef = TypedDict(
    "ClientCreateComputerResponseComputerComputerAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateComputerResponseComputerTypeDef = TypedDict(
    "ClientCreateComputerResponseComputerTypeDef",
    {
        "ComputerId": str,
        "ComputerName": str,
        "ComputerAttributes": List[ClientCreateComputerResponseComputerComputerAttributesTypeDef],
    },
    total=False,
)

ClientCreateComputerResponseTypeDef = TypedDict(
    "ClientCreateComputerResponseTypeDef",
    {"Computer": ClientCreateComputerResponseComputerTypeDef},
    total=False,
)

ClientCreateDirectoryResponseTypeDef = TypedDict(
    "ClientCreateDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)

_RequiredClientCreateDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientCreateDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientCreateDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDirectoryTagsTypeDef(
    _RequiredClientCreateDirectoryTagsTypeDef, _OptionalClientCreateDirectoryTagsTypeDef
):
    pass


_RequiredClientCreateDirectoryVpcSettingsTypeDef = TypedDict(
    "_RequiredClientCreateDirectoryVpcSettingsTypeDef", {"VpcId": str}
)
_OptionalClientCreateDirectoryVpcSettingsTypeDef = TypedDict(
    "_OptionalClientCreateDirectoryVpcSettingsTypeDef", {"SubnetIds": List[str]}, total=False
)


class ClientCreateDirectoryVpcSettingsTypeDef(
    _RequiredClientCreateDirectoryVpcSettingsTypeDef,
    _OptionalClientCreateDirectoryVpcSettingsTypeDef,
):
    pass


ClientCreateMicrosoftAdResponseTypeDef = TypedDict(
    "ClientCreateMicrosoftAdResponseTypeDef", {"DirectoryId": str}, total=False
)

_RequiredClientCreateMicrosoftAdTagsTypeDef = TypedDict(
    "_RequiredClientCreateMicrosoftAdTagsTypeDef", {"Key": str}
)
_OptionalClientCreateMicrosoftAdTagsTypeDef = TypedDict(
    "_OptionalClientCreateMicrosoftAdTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateMicrosoftAdTagsTypeDef(
    _RequiredClientCreateMicrosoftAdTagsTypeDef, _OptionalClientCreateMicrosoftAdTagsTypeDef
):
    pass


_RequiredClientCreateMicrosoftAdVpcSettingsTypeDef = TypedDict(
    "_RequiredClientCreateMicrosoftAdVpcSettingsTypeDef", {"VpcId": str}
)
_OptionalClientCreateMicrosoftAdVpcSettingsTypeDef = TypedDict(
    "_OptionalClientCreateMicrosoftAdVpcSettingsTypeDef", {"SubnetIds": List[str]}, total=False
)


class ClientCreateMicrosoftAdVpcSettingsTypeDef(
    _RequiredClientCreateMicrosoftAdVpcSettingsTypeDef,
    _OptionalClientCreateMicrosoftAdVpcSettingsTypeDef,
):
    pass


ClientCreateSnapshotResponseTypeDef = TypedDict(
    "ClientCreateSnapshotResponseTypeDef", {"SnapshotId": str}, total=False
)

ClientCreateTrustResponseTypeDef = TypedDict(
    "ClientCreateTrustResponseTypeDef", {"TrustId": str}, total=False
)

ClientDeleteDirectoryResponseTypeDef = TypedDict(
    "ClientDeleteDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)

ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "ClientDeleteSnapshotResponseTypeDef", {"SnapshotId": str}, total=False
)

ClientDeleteTrustResponseTypeDef = TypedDict(
    "ClientDeleteTrustResponseTypeDef", {"TrustId": str}, total=False
)

ClientDescribeCertificateResponseCertificateTypeDef = TypedDict(
    "ClientDescribeCertificateResponseCertificateTypeDef",
    {
        "CertificateId": str,
        "State": Literal[
            "Registering",
            "Registered",
            "RegisterFailed",
            "Deregistering",
            "Deregistered",
            "DeregisterFailed",
        ],
        "StateReason": str,
        "CommonName": str,
        "RegisteredDateTime": datetime,
        "ExpiryDateTime": datetime,
    },
    total=False,
)

ClientDescribeCertificateResponseTypeDef = TypedDict(
    "ClientDescribeCertificateResponseTypeDef",
    {"Certificate": ClientDescribeCertificateResponseCertificateTypeDef},
    total=False,
)

ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef = TypedDict(
    "ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef",
    {"RemoteDomainName": str, "DnsIpAddrs": List[str], "ReplicationScope": str},
    total=False,
)

ClientDescribeConditionalForwardersResponseTypeDef = TypedDict(
    "ClientDescribeConditionalForwardersResponseTypeDef",
    {
        "ConditionalForwarders": List[
            ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef
        ]
    },
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef,
        "RadiusSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
    },
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)

ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": Literal["Small", "Large"],
        "Edition": Literal["Enterprise", "Standard"],
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": Literal[
            "Requested",
            "Creating",
            "Created",
            "Active",
            "Inoperable",
            "Impaired",
            "Restoring",
            "RestoreFailed",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": Literal["SimpleAD", "ADConnector", "MicrosoftAD", "SharedMicrosoftAD"],
        "VpcSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef,
        "ConnectSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef,
        "RadiusSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef,
    },
    total=False,
)

ClientDescribeDirectoriesResponseTypeDef = TypedDict(
    "ClientDescribeDirectoriesResponseTypeDef",
    {
        "DirectoryDescriptions": List[
            ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeDomainControllersResponseDomainControllersTypeDef = TypedDict(
    "ClientDescribeDomainControllersResponseDomainControllersTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": Literal[
            "Creating", "Active", "Impaired", "Restoring", "Deleting", "Deleted", "Failed"
        ],
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeDomainControllersResponseTypeDef = TypedDict(
    "ClientDescribeDomainControllersResponseTypeDef",
    {
        "DomainControllers": List[ClientDescribeDomainControllersResponseDomainControllersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeEventTopicsResponseEventTopicsTypeDef = TypedDict(
    "ClientDescribeEventTopicsResponseEventTopicsTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": Literal["Registered", "Topic not found", "Failed", "Deleted"],
    },
    total=False,
)

ClientDescribeEventTopicsResponseTypeDef = TypedDict(
    "ClientDescribeEventTopicsResponseTypeDef",
    {"EventTopics": List[ClientDescribeEventTopicsResponseEventTopicsTypeDef]},
    total=False,
)

ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef = TypedDict(
    "ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef",
    {
        "LDAPSStatus": Literal["Enabling", "Enabled", "EnableFailed", "Disabled"],
        "LDAPSStatusReason": str,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeLdapsSettingsResponseTypeDef = TypedDict(
    "ClientDescribeLdapsSettingsResponseTypeDef",
    {
        "LDAPSSettingsInfo": List[ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef = TypedDict(
    "ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeSharedDirectoriesResponseTypeDef = TypedDict(
    "ClientDescribeSharedDirectoriesResponseTypeDef",
    {
        "SharedDirectories": List[ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": Literal["Auto", "Manual"],
        "Name": str,
        "Status": Literal["Creating", "Completed", "Failed"],
        "StartTime": datetime,
    },
    total=False,
)

ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeSnapshotsResponseTypeDef",
    {"Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTrustsResponseTrustsTypeDef = TypedDict(
    "ClientDescribeTrustsResponseTrustsTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": Literal["Forest", "External"],
        "TrustDirection": Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        "TrustState": Literal[
            "Creating",
            "Created",
            "Verifying",
            "VerifyFailed",
            "Verified",
            "Updating",
            "UpdateFailed",
            "Updated",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": Literal["Enabled", "Disabled"],
    },
    total=False,
)

ClientDescribeTrustsResponseTypeDef = TypedDict(
    "ClientDescribeTrustsResponseTypeDef",
    {"Trusts": List[ClientDescribeTrustsResponseTrustsTypeDef], "NextToken": str},
    total=False,
)

ClientEnableRadiusRadiusSettingsTypeDef = TypedDict(
    "ClientEnableRadiusRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef = TypedDict(
    "ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": int,
        "CloudOnlyDirectoriesCurrentCount": int,
        "CloudOnlyDirectoriesLimitReached": bool,
        "CloudOnlyMicrosoftADLimit": int,
        "CloudOnlyMicrosoftADCurrentCount": int,
        "CloudOnlyMicrosoftADLimitReached": bool,
        "ConnectedDirectoriesLimit": int,
        "ConnectedDirectoriesCurrentCount": int,
        "ConnectedDirectoriesLimitReached": bool,
    },
    total=False,
)

ClientGetDirectoryLimitsResponseTypeDef = TypedDict(
    "ClientGetDirectoryLimitsResponseTypeDef",
    {"DirectoryLimits": ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef},
    total=False,
)

ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef = TypedDict(
    "ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": int,
        "ManualSnapshotsCurrentCount": int,
        "ManualSnapshotsLimitReached": bool,
    },
    total=False,
)

ClientGetSnapshotLimitsResponseTypeDef = TypedDict(
    "ClientGetSnapshotLimitsResponseTypeDef",
    {"SnapshotLimits": ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef},
    total=False,
)

ClientListCertificatesResponseCertificatesInfoTypeDef = TypedDict(
    "ClientListCertificatesResponseCertificatesInfoTypeDef",
    {
        "CertificateId": str,
        "CommonName": str,
        "State": Literal[
            "Registering",
            "Registered",
            "RegisterFailed",
            "Deregistering",
            "Deregistered",
            "DeregisterFailed",
        ],
    },
    total=False,
)

ClientListCertificatesResponseTypeDef = TypedDict(
    "ClientListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificatesInfo": List[ClientListCertificatesResponseCertificatesInfoTypeDef],
    },
    total=False,
)

ClientListIpRoutesResponseIpRoutesInfoTypeDef = TypedDict(
    "ClientListIpRoutesResponseIpRoutesInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": Literal[
            "Adding", "Added", "Removing", "Removed", "AddFailed", "RemoveFailed"
        ],
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)

ClientListIpRoutesResponseTypeDef = TypedDict(
    "ClientListIpRoutesResponseTypeDef",
    {"IpRoutesInfo": List[ClientListIpRoutesResponseIpRoutesInfoTypeDef], "NextToken": str},
    total=False,
)

ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef = TypedDict(
    "ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)

ClientListLogSubscriptionsResponseTypeDef = TypedDict(
    "ClientListLogSubscriptionsResponseTypeDef",
    {
        "LogSubscriptions": List[ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef = TypedDict(
    "ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": Literal[
            "Initializing",
            "CreatingSnapshot",
            "UpdatingSchema",
            "Replicating",
            "CancelInProgress",
            "RollbackInProgress",
            "Cancelled",
            "Failed",
            "Completed",
        ],
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

ClientListSchemaExtensionsResponseTypeDef = TypedDict(
    "ClientListSchemaExtensionsResponseTypeDef",
    {
        "SchemaExtensionsInfo": List[ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientRegisterCertificateResponseTypeDef = TypedDict(
    "ClientRegisterCertificateResponseTypeDef", {"CertificateId": str}, total=False
)

ClientRejectSharedDirectoryResponseTypeDef = TypedDict(
    "ClientRejectSharedDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)

ClientShareDirectoryResponseTypeDef = TypedDict(
    "ClientShareDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)

_RequiredClientShareDirectoryShareTargetTypeDef = TypedDict(
    "_RequiredClientShareDirectoryShareTargetTypeDef", {"Id": str}
)
_OptionalClientShareDirectoryShareTargetTypeDef = TypedDict(
    "_OptionalClientShareDirectoryShareTargetTypeDef", {"Type": str}, total=False
)


class ClientShareDirectoryShareTargetTypeDef(
    _RequiredClientShareDirectoryShareTargetTypeDef, _OptionalClientShareDirectoryShareTargetTypeDef
):
    pass


ClientStartSchemaExtensionResponseTypeDef = TypedDict(
    "ClientStartSchemaExtensionResponseTypeDef", {"SchemaExtensionId": str}, total=False
)

ClientUnshareDirectoryResponseTypeDef = TypedDict(
    "ClientUnshareDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)

_RequiredClientUnshareDirectoryUnshareTargetTypeDef = TypedDict(
    "_RequiredClientUnshareDirectoryUnshareTargetTypeDef", {"Id": str}
)
_OptionalClientUnshareDirectoryUnshareTargetTypeDef = TypedDict(
    "_OptionalClientUnshareDirectoryUnshareTargetTypeDef", {"Type": str}, total=False
)


class ClientUnshareDirectoryUnshareTargetTypeDef(
    _RequiredClientUnshareDirectoryUnshareTargetTypeDef,
    _OptionalClientUnshareDirectoryUnshareTargetTypeDef,
):
    pass


ClientUpdateRadiusRadiusSettingsTypeDef = TypedDict(
    "ClientUpdateRadiusRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

ClientUpdateTrustResponseTypeDef = TypedDict(
    "ClientUpdateTrustResponseTypeDef", {"RequestId": str, "TrustId": str}, total=False
)

ClientVerifyTrustResponseTypeDef = TypedDict(
    "ClientVerifyTrustResponseTypeDef", {"TrustId": str}, total=False
)

DirectoryConnectSettingsDescriptionTypeDef = TypedDict(
    "DirectoryConnectSettingsDescriptionTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)

DirectoryVpcSettingsDescriptionTypeDef = TypedDict(
    "DirectoryVpcSettingsDescriptionTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)

RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

OwnerDirectoryDescriptionTypeDef = TypedDict(
    "OwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": DirectoryVpcSettingsDescriptionTypeDef,
        "RadiusSettings": RadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
    },
    total=False,
)

DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": Literal["Small", "Large"],
        "Edition": Literal["Enterprise", "Standard"],
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": Literal[
            "Requested",
            "Creating",
            "Created",
            "Active",
            "Inoperable",
            "Impaired",
            "Restoring",
            "RestoreFailed",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": Literal["SimpleAD", "ADConnector", "MicrosoftAD", "SharedMicrosoftAD"],
        "VpcSettings": DirectoryVpcSettingsDescriptionTypeDef,
        "ConnectSettings": DirectoryConnectSettingsDescriptionTypeDef,
        "RadiusSettings": RadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": OwnerDirectoryDescriptionTypeDef,
    },
    total=False,
)

DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {"DirectoryDescriptions": List[DirectoryDescriptionTypeDef], "NextToken": str},
    total=False,
)

DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": Literal[
            "Creating", "Active", "Impaired", "Restoring", "Deleting", "Deleted", "Failed"
        ],
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {"DomainControllers": List[DomainControllerTypeDef], "NextToken": str},
    total=False,
)

SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {"SharedDirectories": List[SharedDirectoryTypeDef], "NextToken": str},
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": Literal["Auto", "Manual"],
        "Name": str,
        "Status": Literal["Creating", "Completed", "Failed"],
        "StartTime": datetime,
    },
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {"Snapshots": List[SnapshotTypeDef], "NextToken": str},
    total=False,
)

TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": Literal["Forest", "External"],
        "TrustDirection": Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        "TrustState": Literal[
            "Creating",
            "Created",
            "Verifying",
            "VerifyFailed",
            "Verified",
            "Updating",
            "UpdateFailed",
            "Updated",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": Literal["Enabled", "Disabled"],
    },
    total=False,
)

DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef", {"Trusts": List[TrustTypeDef], "NextToken": str}, total=False
)

IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": Literal[
            "Adding", "Added", "Removing", "Removed", "AddFailed", "RemoveFailed"
        ],
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)

ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {"IpRoutesInfo": List[IpRouteInfoTypeDef], "NextToken": str},
    total=False,
)

LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)

ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {"LogSubscriptions": List[LogSubscriptionTypeDef], "NextToken": str},
    total=False,
)

SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": Literal[
            "Initializing",
            "CreatingSnapshot",
            "UpdatingSchema",
            "Replicating",
            "CancelInProgress",
            "RollbackInProgress",
            "Cancelled",
            "Failed",
            "Completed",
        ],
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {"SchemaExtensionsInfo": List[SchemaExtensionInfoTypeDef], "NextToken": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
