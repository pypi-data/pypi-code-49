"""
Main interface for elb service type definitions.

Usage::

    from mypy_boto3.elb.type_defs import ClientAddTagsTagsTypeDef

    data: ClientAddTagsTagsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsTagsTypeDef",
    "ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    "ClientAttachLoadBalancerToSubnetsResponseTypeDef",
    "ClientConfigureHealthCheckHealthCheckTypeDef",
    "ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    "ClientConfigureHealthCheckResponseTypeDef",
    "ClientCreateLoadBalancerListenersListenersTypeDef",
    "ClientCreateLoadBalancerListenersTypeDef",
    "ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    "ClientDescribeAccountLimitsResponseLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeInstanceHealthInstancesTypeDef",
    "ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    "ClientDescribeInstanceHealthResponseTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDetachLoadBalancerFromSubnetsResponseTypeDef",
    "ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    "ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    "ClientRegisterInstancesWithLoadBalancerInstancesTypeDef",
    "ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    "ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    "ClientRemoveTagsTagsTypeDef",
    "BackendServerDescriptionTypeDef",
    "HealthCheckTypeDef",
    "InstanceTypeDef",
    "ListenerTypeDef",
    "ListenerDescriptionTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "PoliciesTypeDef",
    "SourceSecurityGroupTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "DescribeAccessPointsOutputTypeDef",
    "LimitTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"Key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    pass


ClientApplySecurityGroupsToLoadBalancerResponseTypeDef = TypedDict(
    "ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)

ClientAttachLoadBalancerToSubnetsResponseTypeDef = TypedDict(
    "ClientAttachLoadBalancerToSubnetsResponseTypeDef", {"Subnets": List[str]}, total=False
)

_RequiredClientConfigureHealthCheckHealthCheckTypeDef = TypedDict(
    "_RequiredClientConfigureHealthCheckHealthCheckTypeDef", {"Target": str}
)
_OptionalClientConfigureHealthCheckHealthCheckTypeDef = TypedDict(
    "_OptionalClientConfigureHealthCheckHealthCheckTypeDef",
    {"Interval": int, "Timeout": int, "UnhealthyThreshold": int, "HealthyThreshold": int},
    total=False,
)


class ClientConfigureHealthCheckHealthCheckTypeDef(
    _RequiredClientConfigureHealthCheckHealthCheckTypeDef,
    _OptionalClientConfigureHealthCheckHealthCheckTypeDef,
):
    pass


ClientConfigureHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)

ClientConfigureHealthCheckResponseTypeDef = TypedDict(
    "ClientConfigureHealthCheckResponseTypeDef",
    {"HealthCheck": ClientConfigureHealthCheckResponseHealthCheckTypeDef},
    total=False,
)

_RequiredClientCreateLoadBalancerListenersListenersTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerListenersListenersTypeDef", {"Protocol": str}
)
_OptionalClientCreateLoadBalancerListenersListenersTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerListenersListenersTypeDef",
    {
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class ClientCreateLoadBalancerListenersListenersTypeDef(
    _RequiredClientCreateLoadBalancerListenersListenersTypeDef,
    _OptionalClientCreateLoadBalancerListenersListenersTypeDef,
):
    pass


_RequiredClientCreateLoadBalancerListenersTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerListenersTypeDef", {"Protocol": str}
)
_OptionalClientCreateLoadBalancerListenersTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerListenersTypeDef",
    {
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class ClientCreateLoadBalancerListenersTypeDef(
    _RequiredClientCreateLoadBalancerListenersTypeDef,
    _OptionalClientCreateLoadBalancerListenersTypeDef,
):
    pass


ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef = TypedDict(
    "ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)

ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseTypeDef", {"DNSName": str}, total=False
)

_RequiredClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLoadBalancerTagsTypeDef(
    _RequiredClientCreateLoadBalancerTagsTypeDef, _OptionalClientCreateLoadBalancerTagsTypeDef
):
    pass


ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef = TypedDict(
    "ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef", {"InstanceId": str}, total=False
)

ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef = TypedDict(
    "ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

ClientDeregisterInstancesFromLoadBalancerResponseTypeDef = TypedDict(
    "ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    {"Instances": List[ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef]},
    total=False,
)

ClientDescribeAccountLimitsResponseLimitsTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseLimitsTypeDef", {"Name": str, "Max": str}, total=False
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {"Limits": List[ClientDescribeAccountLimitsResponseLimitsTypeDef], "NextMarker": str},
    total=False,
)

ClientDescribeInstanceHealthInstancesTypeDef = TypedDict(
    "ClientDescribeInstanceHealthInstancesTypeDef", {"InstanceId": str}, total=False
)

ClientDescribeInstanceHealthResponseInstanceStatesTypeDef = TypedDict(
    "ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    {"InstanceId": str, "State": str, "ReasonCode": str, "Description": str},
    total=False,
)

ClientDescribeInstanceHealthResponseTypeDef = TypedDict(
    "ClientDescribeInstanceHealthResponseTypeDef",
    {"InstanceStates": List[ClientDescribeInstanceHealthResponseInstanceStatesTypeDef]},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerAttributes": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
    },
    total=False,
)

ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)

ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    {
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributeDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancerPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    {
        "PolicyDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef
        ]
    },
    total=False,
)

ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
        "Description": str,
        "DefaultValue": str,
        "Cardinality": str,
    },
    total=False,
)

ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    {
        "PolicyTypeName": str,
        "Description": str,
        "PolicyAttributeTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancerPolicyTypesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    {
        "PolicyTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef
        ]
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
        ],
        "LBCookieStickinessPolicies": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
        ],
        "OtherPolicies": List[str],
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
        ],
        "Policies": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef,
        "BackendServerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
        ],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef
        ],
        "HealthCheck": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef,
        "SourceSecurityGroup": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeTagsResponseTagDescriptionsTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTagDescriptionsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    {"LoadBalancerName": str, "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef]},
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"TagDescriptions": List[ClientDescribeTagsResponseTagDescriptionsTypeDef]},
    total=False,
)

ClientDetachLoadBalancerFromSubnetsResponseTypeDef = TypedDict(
    "ClientDetachLoadBalancerFromSubnetsResponseTypeDef", {"Subnets": List[str]}, total=False
)

ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)

ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)

ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef,
    },
    total=False,
)

ClientRegisterInstancesWithLoadBalancerInstancesTypeDef = TypedDict(
    "ClientRegisterInstancesWithLoadBalancerInstancesTypeDef", {"InstanceId": str}, total=False
)

ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef = TypedDict(
    "ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

ClientRegisterInstancesWithLoadBalancerResponseTypeDef = TypedDict(
    "ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    {"Instances": List[ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef]},
    total=False,
)

ClientRemoveTagsTagsTypeDef = TypedDict("ClientRemoveTagsTagsTypeDef", {"Key": str}, total=False)

BackendServerDescriptionTypeDef = TypedDict(
    "BackendServerDescriptionTypeDef", {"InstancePort": int, "PolicyNames": List[str]}, total=False
)

HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)

InstanceTypeDef = TypedDict("InstanceTypeDef", {"InstanceId": str}, total=False)

_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef", {"Protocol": str, "LoadBalancerPort": int, "InstancePort": int}
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef", {"InstanceProtocol": str, "SSLCertificateId": str}, total=False
)


class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass


ListenerDescriptionTypeDef = TypedDict(
    "ListenerDescriptionTypeDef",
    {"Listener": ListenerTypeDef, "PolicyNames": List[str]},
    total=False,
)

AppCookieStickinessPolicyTypeDef = TypedDict(
    "AppCookieStickinessPolicyTypeDef", {"PolicyName": str, "CookieName": str}, total=False
)

LBCookieStickinessPolicyTypeDef = TypedDict(
    "LBCookieStickinessPolicyTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)

PoliciesTypeDef = TypedDict(
    "PoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[AppCookieStickinessPolicyTypeDef],
        "LBCookieStickinessPolicies": List[LBCookieStickinessPolicyTypeDef],
        "OtherPolicies": List[str],
    },
    total=False,
)

SourceSecurityGroupTypeDef = TypedDict(
    "SourceSecurityGroupTypeDef", {"OwnerAlias": str, "GroupName": str}, total=False
)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[ListenerDescriptionTypeDef],
        "Policies": PoliciesTypeDef,
        "BackendServerDescriptions": List[BackendServerDescriptionTypeDef],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[InstanceTypeDef],
        "HealthCheck": HealthCheckTypeDef,
        "SourceSecurityGroup": SourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)

DescribeAccessPointsOutputTypeDef = TypedDict(
    "DescribeAccessPointsOutputTypeDef",
    {"LoadBalancerDescriptions": List[LoadBalancerDescriptionTypeDef], "NextMarker": str},
    total=False,
)

LimitTypeDef = TypedDict("LimitTypeDef", {"Name": str, "Max": str}, total=False)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {"Limits": List[LimitTypeDef], "NextMarker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
