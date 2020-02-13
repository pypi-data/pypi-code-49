"""
Main interface for route53 service type definitions.

Usage::

    from mypy_boto3.route53.type_defs import ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef

    data: ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef = {...}
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
    "ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef",
    "ClientAssociateVpcWithHostedZoneResponseTypeDef",
    "ClientAssociateVpcWithHostedZoneVPCTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchTypeDef",
    "ClientChangeResourceRecordSetsResponseChangeInfoTypeDef",
    "ClientChangeResourceRecordSetsResponseTypeDef",
    "ClientChangeTagsForResourceAddTagsTypeDef",
    "ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientCreateHealthCheckHealthCheckConfigTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckTypeDef",
    "ClientCreateHealthCheckResponseTypeDef",
    "ClientCreateHostedZoneHostedZoneConfigTypeDef",
    "ClientCreateHostedZoneResponseChangeInfoTypeDef",
    "ClientCreateHostedZoneResponseDelegationSetTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneConfigTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneTypeDef",
    "ClientCreateHostedZoneResponseVPCTypeDef",
    "ClientCreateHostedZoneResponseTypeDef",
    "ClientCreateHostedZoneVPCTypeDef",
    "ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    "ClientCreateQueryLoggingConfigResponseTypeDef",
    "ClientCreateReusableDelegationSetResponseDelegationSetTypeDef",
    "ClientCreateReusableDelegationSetResponseTypeDef",
    "ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientCreateTrafficPolicyInstanceResponseTypeDef",
    "ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef",
    "ClientCreateTrafficPolicyResponseTypeDef",
    "ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef",
    "ClientCreateTrafficPolicyVersionResponseTypeDef",
    "ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef",
    "ClientCreateVpcAssociationAuthorizationResponseTypeDef",
    "ClientCreateVpcAssociationAuthorizationVPCTypeDef",
    "ClientDeleteHostedZoneResponseChangeInfoTypeDef",
    "ClientDeleteHostedZoneResponseTypeDef",
    "ClientDeleteVpcAssociationAuthorizationVPCTypeDef",
    "ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef",
    "ClientDisassociateVpcFromHostedZoneResponseTypeDef",
    "ClientDisassociateVpcFromHostedZoneVPCTypeDef",
    "ClientGetAccountLimitResponseLimitTypeDef",
    "ClientGetAccountLimitResponseTypeDef",
    "ClientGetChangeResponseChangeInfoTypeDef",
    "ClientGetChangeResponseTypeDef",
    "ClientGetCheckerIpRangesResponseTypeDef",
    "ClientGetGeoLocationResponseGeoLocationDetailsTypeDef",
    "ClientGetGeoLocationResponseTypeDef",
    "ClientGetHealthCheckCountResponseTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseTypeDef",
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientGetHealthCheckResponseHealthCheckTypeDef",
    "ClientGetHealthCheckResponseTypeDef",
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef",
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef",
    "ClientGetHealthCheckStatusResponseTypeDef",
    "ClientGetHostedZoneCountResponseTypeDef",
    "ClientGetHostedZoneLimitResponseLimitTypeDef",
    "ClientGetHostedZoneLimitResponseTypeDef",
    "ClientGetHostedZoneResponseDelegationSetTypeDef",
    "ClientGetHostedZoneResponseHostedZoneConfigTypeDef",
    "ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    "ClientGetHostedZoneResponseHostedZoneTypeDef",
    "ClientGetHostedZoneResponseVPCsTypeDef",
    "ClientGetHostedZoneResponseTypeDef",
    "ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    "ClientGetQueryLoggingConfigResponseTypeDef",
    "ClientGetReusableDelegationSetLimitResponseLimitTypeDef",
    "ClientGetReusableDelegationSetLimitResponseTypeDef",
    "ClientGetReusableDelegationSetResponseDelegationSetTypeDef",
    "ClientGetReusableDelegationSetResponseTypeDef",
    "ClientGetTrafficPolicyInstanceCountResponseTypeDef",
    "ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientGetTrafficPolicyInstanceResponseTypeDef",
    "ClientGetTrafficPolicyResponseTrafficPolicyTypeDef",
    "ClientGetTrafficPolicyResponseTypeDef",
    "ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef",
    "ClientListGeoLocationsResponseTypeDef",
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef",
    "ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef",
    "ClientListHealthChecksResponseHealthChecksTypeDef",
    "ClientListHealthChecksResponseTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesTypeDef",
    "ClientListHostedZonesByNameResponseTypeDef",
    "ClientListHostedZonesResponseHostedZonesConfigTypeDef",
    "ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef",
    "ClientListHostedZonesResponseHostedZonesTypeDef",
    "ClientListHostedZonesResponseTypeDef",
    "ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef",
    "ClientListQueryLoggingConfigsResponseTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef",
    "ClientListResourceRecordSetsResponseTypeDef",
    "ClientListReusableDelegationSetsResponseDelegationSetsTypeDef",
    "ClientListReusableDelegationSetsResponseTypeDef",
    "ClientListTagsForResourceResponseResourceTagSetTagsTypeDef",
    "ClientListTagsForResourceResponseResourceTagSetTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef",
    "ClientListTagsForResourcesResponseResourceTagSetsTypeDef",
    "ClientListTagsForResourcesResponseTypeDef",
    "ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef",
    "ClientListTrafficPoliciesResponseTypeDef",
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesResponseTypeDef",
    "ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef",
    "ClientListTrafficPolicyVersionsResponseTypeDef",
    "ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef",
    "ClientListVpcAssociationAuthorizationsResponseTypeDef",
    "ClientTestDnsAnswerResponseTypeDef",
    "ClientUpdateHealthCheckAlarmIdentifierTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckTypeDef",
    "ClientUpdateHealthCheckResponseTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef",
    "ClientUpdateHostedZoneCommentResponseTypeDef",
    "ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef",
    "ClientUpdateTrafficPolicyCommentResponseTypeDef",
    "ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientUpdateTrafficPolicyInstanceResponseTypeDef",
    "DimensionTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "AlarmIdentifierTypeDef",
    "HealthCheckConfigTypeDef",
    "LinkedServiceTypeDef",
    "HealthCheckTypeDef",
    "ListHealthChecksResponseTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneTypeDef",
    "ListHostedZonesResponseTypeDef",
    "QueryLoggingConfigTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "AliasTargetTypeDef",
    "GeoLocationTypeDef",
    "ResourceRecordTypeDef",
    "ResourceRecordSetTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "VPCTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)

ClientAssociateVpcWithHostedZoneResponseTypeDef = TypedDict(
    "ClientAssociateVpcWithHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef},
    total=False,
)

ClientAssociateVpcWithHostedZoneVPCTypeDef = TypedDict(
    "ClientAssociateVpcWithHostedZoneVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef",
    {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool},
    total=False,
)

ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)

ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef",
    {"Value": str},
    total=False,
)

ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
        ],
        "GeoLocation": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef,
        "Failover": Literal["PRIMARY", "SECONDARY"],
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List[
            ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef
        ],
        "AliasTarget": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef,
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)

ClientChangeResourceRecordSetsChangeBatchChangesTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsChangeBatchChangesTypeDef",
    {
        "Action": Literal["CREATE", "DELETE", "UPSERT"],
        "ResourceRecordSet": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef,
    },
    total=False,
)

ClientChangeResourceRecordSetsChangeBatchTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsChangeBatchTypeDef",
    {"Comment": str, "Changes": List[ClientChangeResourceRecordSetsChangeBatchChangesTypeDef]},
    total=False,
)

ClientChangeResourceRecordSetsResponseChangeInfoTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)

ClientChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "ClientChangeResourceRecordSetsResponseTypeDef",
    {"ChangeInfo": ClientChangeResourceRecordSetsResponseChangeInfoTypeDef},
    total=False,
)

ClientChangeTagsForResourceAddTagsTypeDef = TypedDict(
    "ClientChangeTagsForResourceAddTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)

ClientCreateHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "ClientCreateHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)

ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)

ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)

ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)

ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientCreateHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)

ClientCreateHealthCheckResponseTypeDef = TypedDict(
    "ClientCreateHealthCheckResponseTypeDef",
    {"HealthCheck": ClientCreateHealthCheckResponseHealthCheckTypeDef, "Location": str},
    total=False,
)

ClientCreateHostedZoneHostedZoneConfigTypeDef = TypedDict(
    "ClientCreateHostedZoneHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)

ClientCreateHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)

ClientCreateHostedZoneResponseDelegationSetTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)

ClientCreateHostedZoneResponseHostedZoneConfigTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)

ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientCreateHostedZoneResponseHostedZoneTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientCreateHostedZoneResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)

ClientCreateHostedZoneResponseVPCTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientCreateHostedZoneResponseTypeDef = TypedDict(
    "ClientCreateHostedZoneResponseTypeDef",
    {
        "HostedZone": ClientCreateHostedZoneResponseHostedZoneTypeDef,
        "ChangeInfo": ClientCreateHostedZoneResponseChangeInfoTypeDef,
        "DelegationSet": ClientCreateHostedZoneResponseDelegationSetTypeDef,
        "VPC": ClientCreateHostedZoneResponseVPCTypeDef,
        "Location": str,
    },
    total=False,
)

ClientCreateHostedZoneVPCTypeDef = TypedDict(
    "ClientCreateHostedZoneVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef = TypedDict(
    "ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)

ClientCreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "ClientCreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef,
        "Location": str,
    },
    total=False,
)

ClientCreateReusableDelegationSetResponseDelegationSetTypeDef = TypedDict(
    "ClientCreateReusableDelegationSetResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)

ClientCreateReusableDelegationSetResponseTypeDef = TypedDict(
    "ClientCreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": ClientCreateReusableDelegationSetResponseDelegationSetTypeDef,
        "Location": str,
    },
    total=False,
)

ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)

ClientCreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "ClientCreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef,
        "Location": str,
    },
    total=False,
)

ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef = TypedDict(
    "ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)

ClientCreateTrafficPolicyResponseTypeDef = TypedDict(
    "ClientCreateTrafficPolicyResponseTypeDef",
    {"TrafficPolicy": ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef, "Location": str},
    total=False,
)

ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef = TypedDict(
    "ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)

ClientCreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "ClientCreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef,
        "Location": str,
    },
    total=False,
)

ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef = TypedDict(
    "ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientCreateVpcAssociationAuthorizationResponseTypeDef = TypedDict(
    "ClientCreateVpcAssociationAuthorizationResponseTypeDef",
    {"HostedZoneId": str, "VPC": ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef},
    total=False,
)

ClientCreateVpcAssociationAuthorizationVPCTypeDef = TypedDict(
    "ClientCreateVpcAssociationAuthorizationVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientDeleteHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "ClientDeleteHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)

ClientDeleteHostedZoneResponseTypeDef = TypedDict(
    "ClientDeleteHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientDeleteHostedZoneResponseChangeInfoTypeDef},
    total=False,
)

ClientDeleteVpcAssociationAuthorizationVPCTypeDef = TypedDict(
    "ClientDeleteVpcAssociationAuthorizationVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)

ClientDisassociateVpcFromHostedZoneResponseTypeDef = TypedDict(
    "ClientDisassociateVpcFromHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef},
    total=False,
)

ClientDisassociateVpcFromHostedZoneVPCTypeDef = TypedDict(
    "ClientDisassociateVpcFromHostedZoneVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientGetAccountLimitResponseLimitTypeDef = TypedDict(
    "ClientGetAccountLimitResponseLimitTypeDef",
    {
        "Type": Literal[
            "MAX_HEALTH_CHECKS_BY_OWNER",
            "MAX_HOSTED_ZONES_BY_OWNER",
            "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
            "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
            "MAX_TRAFFIC_POLICIES_BY_OWNER",
        ],
        "Value": int,
    },
    total=False,
)

ClientGetAccountLimitResponseTypeDef = TypedDict(
    "ClientGetAccountLimitResponseTypeDef",
    {"Limit": ClientGetAccountLimitResponseLimitTypeDef, "Count": int},
    total=False,
)

ClientGetChangeResponseChangeInfoTypeDef = TypedDict(
    "ClientGetChangeResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)

ClientGetChangeResponseTypeDef = TypedDict(
    "ClientGetChangeResponseTypeDef",
    {"ChangeInfo": ClientGetChangeResponseChangeInfoTypeDef},
    total=False,
)

ClientGetCheckerIpRangesResponseTypeDef = TypedDict(
    "ClientGetCheckerIpRangesResponseTypeDef", {"CheckerIpRanges": List[str]}, total=False
)

ClientGetGeoLocationResponseGeoLocationDetailsTypeDef = TypedDict(
    "ClientGetGeoLocationResponseGeoLocationDetailsTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)

ClientGetGeoLocationResponseTypeDef = TypedDict(
    "ClientGetGeoLocationResponseTypeDef",
    {"GeoLocationDetails": ClientGetGeoLocationResponseGeoLocationDetailsTypeDef},
    total=False,
)

ClientGetHealthCheckCountResponseTypeDef = TypedDict(
    "ClientGetHealthCheckCountResponseTypeDef", {"HealthCheckCount": int}, total=False
)

ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef = TypedDict(
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef",
    {"Status": str, "CheckedTime": datetime},
    total=False,
)

ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef = TypedDict(
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
        ],
        "IPAddress": str,
        "StatusReport": ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef,
    },
    total=False,
)

ClientGetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "ClientGetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List[
            ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef
        ]
    },
    total=False,
)

ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)

ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)

ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)

ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientGetHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "ClientGetHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)

ClientGetHealthCheckResponseTypeDef = TypedDict(
    "ClientGetHealthCheckResponseTypeDef",
    {"HealthCheck": ClientGetHealthCheckResponseHealthCheckTypeDef},
    total=False,
)

ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef = TypedDict(
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef",
    {"Status": str, "CheckedTime": datetime},
    total=False,
)

ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef = TypedDict(
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
        ],
        "IPAddress": str,
        "StatusReport": ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef,
    },
    total=False,
)

ClientGetHealthCheckStatusResponseTypeDef = TypedDict(
    "ClientGetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List[
            ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef
        ]
    },
    total=False,
)

ClientGetHostedZoneCountResponseTypeDef = TypedDict(
    "ClientGetHostedZoneCountResponseTypeDef", {"HostedZoneCount": int}, total=False
)

ClientGetHostedZoneLimitResponseLimitTypeDef = TypedDict(
    "ClientGetHostedZoneLimitResponseLimitTypeDef",
    {"Type": Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"], "Value": int},
    total=False,
)

ClientGetHostedZoneLimitResponseTypeDef = TypedDict(
    "ClientGetHostedZoneLimitResponseTypeDef",
    {"Limit": ClientGetHostedZoneLimitResponseLimitTypeDef, "Count": int},
    total=False,
)

ClientGetHostedZoneResponseDelegationSetTypeDef = TypedDict(
    "ClientGetHostedZoneResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)

ClientGetHostedZoneResponseHostedZoneConfigTypeDef = TypedDict(
    "ClientGetHostedZoneResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)

ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientGetHostedZoneResponseHostedZoneTypeDef = TypedDict(
    "ClientGetHostedZoneResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientGetHostedZoneResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)

ClientGetHostedZoneResponseVPCsTypeDef = TypedDict(
    "ClientGetHostedZoneResponseVPCsTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientGetHostedZoneResponseTypeDef = TypedDict(
    "ClientGetHostedZoneResponseTypeDef",
    {
        "HostedZone": ClientGetHostedZoneResponseHostedZoneTypeDef,
        "DelegationSet": ClientGetHostedZoneResponseDelegationSetTypeDef,
        "VPCs": List[ClientGetHostedZoneResponseVPCsTypeDef],
    },
    total=False,
)

ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef = TypedDict(
    "ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)

ClientGetQueryLoggingConfigResponseTypeDef = TypedDict(
    "ClientGetQueryLoggingConfigResponseTypeDef",
    {"QueryLoggingConfig": ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef},
    total=False,
)

ClientGetReusableDelegationSetLimitResponseLimitTypeDef = TypedDict(
    "ClientGetReusableDelegationSetLimitResponseLimitTypeDef",
    {"Type": str, "Value": int},
    total=False,
)

ClientGetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "ClientGetReusableDelegationSetLimitResponseTypeDef",
    {"Limit": ClientGetReusableDelegationSetLimitResponseLimitTypeDef, "Count": int},
    total=False,
)

ClientGetReusableDelegationSetResponseDelegationSetTypeDef = TypedDict(
    "ClientGetReusableDelegationSetResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)

ClientGetReusableDelegationSetResponseTypeDef = TypedDict(
    "ClientGetReusableDelegationSetResponseTypeDef",
    {"DelegationSet": ClientGetReusableDelegationSetResponseDelegationSetTypeDef},
    total=False,
)

ClientGetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "ClientGetTrafficPolicyInstanceCountResponseTypeDef",
    {"TrafficPolicyInstanceCount": int},
    total=False,
)

ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)

ClientGetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "ClientGetTrafficPolicyInstanceResponseTypeDef",
    {"TrafficPolicyInstance": ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef},
    total=False,
)

ClientGetTrafficPolicyResponseTrafficPolicyTypeDef = TypedDict(
    "ClientGetTrafficPolicyResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)

ClientGetTrafficPolicyResponseTypeDef = TypedDict(
    "ClientGetTrafficPolicyResponseTypeDef",
    {"TrafficPolicy": ClientGetTrafficPolicyResponseTrafficPolicyTypeDef},
    total=False,
)

ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef = TypedDict(
    "ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)

ClientListGeoLocationsResponseTypeDef = TypedDict(
    "ClientListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List[ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)

ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)

ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef = TypedDict(
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)

ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef = TypedDict(
    "ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientListHealthChecksResponseHealthChecksTypeDef = TypedDict(
    "ClientListHealthChecksResponseHealthChecksTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef,
        "HealthCheckConfig": ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)

ClientListHealthChecksResponseTypeDef = TypedDict(
    "ClientListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List[ClientListHealthChecksResponseHealthChecksTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef = TypedDict(
    "ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)

ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientListHostedZonesByNameResponseHostedZonesTypeDef = TypedDict(
    "ClientListHostedZonesByNameResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)

ClientListHostedZonesByNameResponseTypeDef = TypedDict(
    "ClientListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List[ClientListHostedZonesByNameResponseHostedZonesTypeDef],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListHostedZonesResponseHostedZonesConfigTypeDef = TypedDict(
    "ClientListHostedZonesResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)

ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientListHostedZonesResponseHostedZonesTypeDef = TypedDict(
    "ClientListHostedZonesResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientListHostedZonesResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)

ClientListHostedZonesResponseTypeDef = TypedDict(
    "ClientListHostedZonesResponseTypeDef",
    {
        "HostedZones": List[ClientListHostedZonesResponseHostedZonesTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef = TypedDict(
    "ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)

ClientListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "ClientListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List[
            ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef = TypedDict(
    "ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef",
    {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool},
    total=False,
)

ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef = TypedDict(
    "ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)

ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef = TypedDict(
    "ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef",
    {"Value": str},
    total=False,
)

ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef = TypedDict(
    "ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
        ],
        "GeoLocation": ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef,
        "Failover": Literal["PRIMARY", "SECONDARY"],
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List[
            ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef
        ],
        "AliasTarget": ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef,
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)

ClientListResourceRecordSetsResponseTypeDef = TypedDict(
    "ClientListResourceRecordSetsResponseTypeDef",
    {
        "ResourceRecordSets": List[ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef],
        "IsTruncated": bool,
        "NextRecordName": str,
        "NextRecordType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "NextRecordIdentifier": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListReusableDelegationSetsResponseDelegationSetsTypeDef = TypedDict(
    "ClientListReusableDelegationSetsResponseDelegationSetsTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)

ClientListReusableDelegationSetsResponseTypeDef = TypedDict(
    "ClientListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List[ClientListReusableDelegationSetsResponseDelegationSetsTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListTagsForResourceResponseResourceTagSetTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseResourceTagSetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListTagsForResourceResponseResourceTagSetTypeDef = TypedDict(
    "ClientListTagsForResourceResponseResourceTagSetTypeDef",
    {
        "ResourceType": Literal["healthcheck", "hostedzone"],
        "ResourceId": str,
        "Tags": List[ClientListTagsForResourceResponseResourceTagSetTagsTypeDef],
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"ResourceTagSet": ClientListTagsForResourceResponseResourceTagSetTypeDef},
    total=False,
)

ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef = TypedDict(
    "ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListTagsForResourcesResponseResourceTagSetsTypeDef = TypedDict(
    "ClientListTagsForResourcesResponseResourceTagSetsTypeDef",
    {
        "ResourceType": Literal["healthcheck", "hostedzone"],
        "ResourceId": str,
        "Tags": List[ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef],
    },
    total=False,
)

ClientListTagsForResourcesResponseTypeDef = TypedDict(
    "ClientListTagsForResourcesResponseTypeDef",
    {"ResourceTagSets": List[ClientListTagsForResourcesResponseResourceTagSetsTypeDef]},
    total=False,
)

ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef = TypedDict(
    "ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
    total=False,
)

ClientListTrafficPoliciesResponseTypeDef = TypedDict(
    "ClientListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List[
            ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef
        ],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)

ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef
        ],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)

ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)

ClientListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "ClientListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef
        ],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)

ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)

ClientListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "ClientListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef
        ],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)

ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef = TypedDict(
    "ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)

ClientListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "ClientListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List[ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef = TypedDict(
    "ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ClientListVpcAssociationAuthorizationsResponseTypeDef = TypedDict(
    "ClientListVpcAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "VPCs": List[ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef],
    },
    total=False,
)

ClientTestDnsAnswerResponseTypeDef = TypedDict(
    "ClientTestDnsAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
    },
    total=False,
)

_RequiredClientUpdateHealthCheckAlarmIdentifierTypeDef = TypedDict(
    "_RequiredClientUpdateHealthCheckAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ]
    },
)
_OptionalClientUpdateHealthCheckAlarmIdentifierTypeDef = TypedDict(
    "_OptionalClientUpdateHealthCheckAlarmIdentifierTypeDef", {"Name": str}, total=False
)


class ClientUpdateHealthCheckAlarmIdentifierTypeDef(
    _RequiredClientUpdateHealthCheckAlarmIdentifierTypeDef,
    _OptionalClientUpdateHealthCheckAlarmIdentifierTypeDef,
):
    pass


ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)

ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)

ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)

ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientUpdateHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateHealthCheckResponseTypeDef = TypedDict(
    "ClientUpdateHealthCheckResponseTypeDef",
    {"HealthCheck": ClientUpdateHealthCheckResponseHealthCheckTypeDef},
    total=False,
)

ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef = TypedDict(
    "ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)

ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)

ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef = TypedDict(
    "ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)

ClientUpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "ClientUpdateHostedZoneCommentResponseTypeDef",
    {"HostedZone": ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef},
    total=False,
)

ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef = TypedDict(
    "ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)

ClientUpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "ClientUpdateTrafficPolicyCommentResponseTypeDef",
    {"TrafficPolicy": ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef},
    total=False,
)

ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)

ClientUpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "ClientUpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
    },
    total=False,
)

DimensionTypeDef = TypedDict("DimensionTypeDef", {"Name": str, "Value": str})

_RequiredCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
    },
)
_OptionalCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmConfigurationTypeDef",
    {"Dimensions": List[DimensionTypeDef]},
    total=False,
)


class CloudWatchAlarmConfigurationTypeDef(
    _RequiredCloudWatchAlarmConfigurationTypeDef, _OptionalCloudWatchAlarmConfigurationTypeDef
):
    pass


AlarmIdentifierTypeDef = TypedDict(
    "AlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
)

_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef",
    {
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ]
    },
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": AlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass


LinkedServiceTypeDef = TypedDict(
    "LinkedServiceTypeDef", {"ServicePrincipal": str, "Description": str}, total=False
)

_RequiredHealthCheckTypeDef = TypedDict(
    "_RequiredHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "HealthCheckConfig": HealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
    },
)
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {
        "LinkedService": LinkedServiceTypeDef,
        "CloudWatchAlarmConfiguration": CloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass


_RequiredListHealthChecksResponseTypeDef = TypedDict(
    "_RequiredListHealthChecksResponseTypeDef",
    {"HealthChecks": List[HealthCheckTypeDef], "Marker": str, "IsTruncated": bool, "MaxItems": str},
)
_OptionalListHealthChecksResponseTypeDef = TypedDict(
    "_OptionalListHealthChecksResponseTypeDef", {"NextMarker": str}, total=False
)


class ListHealthChecksResponseTypeDef(
    _RequiredListHealthChecksResponseTypeDef, _OptionalListHealthChecksResponseTypeDef
):
    pass


HostedZoneConfigTypeDef = TypedDict(
    "HostedZoneConfigTypeDef", {"Comment": str, "PrivateZone": bool}, total=False
)

_RequiredHostedZoneTypeDef = TypedDict(
    "_RequiredHostedZoneTypeDef", {"Id": str, "Name": str, "CallerReference": str}
)
_OptionalHostedZoneTypeDef = TypedDict(
    "_OptionalHostedZoneTypeDef",
    {
        "Config": HostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": LinkedServiceTypeDef,
    },
    total=False,
)


class HostedZoneTypeDef(_RequiredHostedZoneTypeDef, _OptionalHostedZoneTypeDef):
    pass


_RequiredListHostedZonesResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesResponseTypeDef",
    {"HostedZones": List[HostedZoneTypeDef], "Marker": str, "IsTruncated": bool, "MaxItems": str},
)
_OptionalListHostedZonesResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesResponseTypeDef", {"NextMarker": str}, total=False
)


class ListHostedZonesResponseTypeDef(
    _RequiredListHostedZonesResponseTypeDef, _OptionalListHostedZonesResponseTypeDef
):
    pass


QueryLoggingConfigTypeDef = TypedDict(
    "QueryLoggingConfigTypeDef", {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str}
)

_RequiredListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_RequiredListQueryLoggingConfigsResponseTypeDef",
    {"QueryLoggingConfigs": List[QueryLoggingConfigTypeDef]},
)
_OptionalListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_OptionalListQueryLoggingConfigsResponseTypeDef", {"NextToken": str}, total=False
)


class ListQueryLoggingConfigsResponseTypeDef(
    _RequiredListQueryLoggingConfigsResponseTypeDef, _OptionalListQueryLoggingConfigsResponseTypeDef
):
    pass


AliasTargetTypeDef = TypedDict(
    "AliasTargetTypeDef", {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool}
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)

ResourceRecordTypeDef = TypedDict("ResourceRecordTypeDef", {"Value": str})

_RequiredResourceRecordSetTypeDef = TypedDict(
    "_RequiredResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
)
_OptionalResourceRecordSetTypeDef = TypedDict(
    "_OptionalResourceRecordSetTypeDef",
    {
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
        ],
        "GeoLocation": GeoLocationTypeDef,
        "Failover": Literal["PRIMARY", "SECONDARY"],
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List[ResourceRecordTypeDef],
        "AliasTarget": AliasTargetTypeDef,
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)


class ResourceRecordSetTypeDef(
    _RequiredResourceRecordSetTypeDef, _OptionalResourceRecordSetTypeDef
):
    pass


_RequiredListResourceRecordSetsResponseTypeDef = TypedDict(
    "_RequiredListResourceRecordSetsResponseTypeDef",
    {"ResourceRecordSets": List[ResourceRecordSetTypeDef], "IsTruncated": bool, "MaxItems": str},
)
_OptionalListResourceRecordSetsResponseTypeDef = TypedDict(
    "_OptionalListResourceRecordSetsResponseTypeDef",
    {
        "NextRecordName": str,
        "NextRecordType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "NextRecordIdentifier": str,
    },
    total=False,
)


class ListResourceRecordSetsResponseTypeDef(
    _RequiredListResourceRecordSetsResponseTypeDef, _OptionalListResourceRecordSetsResponseTypeDef
):
    pass


VPCTypeDef = TypedDict(
    "VPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)

_RequiredListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_RequiredListVPCAssociationAuthorizationsResponseTypeDef",
    {"HostedZoneId": str, "VPCs": List[VPCTypeDef]},
)
_OptionalListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_OptionalListVPCAssociationAuthorizationsResponseTypeDef", {"NextToken": str}, total=False
)


class ListVPCAssociationAuthorizationsResponseTypeDef(
    _RequiredListVPCAssociationAuthorizationsResponseTypeDef,
    _OptionalListVPCAssociationAuthorizationsResponseTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
