"""
## AWS::FMS Construct Library

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> **This is a *developer preview* (public beta) module. Releases might lack important features and might have
> future breaking changes.**
>
> This API is still under active development and subject to non-backward
> compatible changes or removal in any future version. Use of the API is not recommended in production
> environments. Experimental APIs are not subject to the Semantic Versioning model.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_fms as fms
```
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-fms", "1.25.0", __name__, "aws-fms@1.25.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotificationChannel(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-fms.CfnNotificationChannel"):
    """A CloudFormation ``AWS::FMS::NotificationChannel``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
    cloudformationResource:
    :cloudformationResource:: AWS::FMS::NotificationChannel
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, sns_role_name: str, sns_topic_arn: str) -> None:
        """Create a new ``AWS::FMS::NotificationChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param sns_role_name: ``AWS::FMS::NotificationChannel.SnsRoleName``.
        :param sns_topic_arn: ``AWS::FMS::NotificationChannel.SnsTopicArn``.
        """
        props = CfnNotificationChannelProps(sns_role_name=sns_role_name, sns_topic_arn=sns_topic_arn)

        jsii.create(CfnNotificationChannel, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="snsRoleName")
    def sns_role_name(self) -> str:
        """``AWS::FMS::NotificationChannel.SnsRoleName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        """
        return jsii.get(self, "snsRoleName")

    @sns_role_name.setter
    def sns_role_name(self, value: str):
        jsii.set(self, "snsRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> str:
        """``AWS::FMS::NotificationChannel.SnsTopicArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        """
        return jsii.get(self, "snsTopicArn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: str):
        jsii.set(self, "snsTopicArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-fms.CfnNotificationChannelProps", jsii_struct_bases=[], name_mapping={'sns_role_name': 'snsRoleName', 'sns_topic_arn': 'snsTopicArn'})
class CfnNotificationChannelProps():
    def __init__(self, *, sns_role_name: str, sns_topic_arn: str):
        """Properties for defining a ``AWS::FMS::NotificationChannel``.

        :param sns_role_name: ``AWS::FMS::NotificationChannel.SnsRoleName``.
        :param sns_topic_arn: ``AWS::FMS::NotificationChannel.SnsTopicArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
        """
        self._values = {
            'sns_role_name': sns_role_name,
            'sns_topic_arn': sns_topic_arn,
        }

    @builtins.property
    def sns_role_name(self) -> str:
        """``AWS::FMS::NotificationChannel.SnsRoleName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        """
        return self._values.get('sns_role_name')

    @builtins.property
    def sns_topic_arn(self) -> str:
        """``AWS::FMS::NotificationChannel.SnsTopicArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        """
        return self._values.get('sns_topic_arn')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNotificationChannelProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPolicy(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-fms.CfnPolicy"):
    """A CloudFormation ``AWS::FMS::Policy``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
    cloudformationResource:
    :cloudformationResource:: AWS::FMS::Policy
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, exclude_resource_tags: typing.Union[bool, aws_cdk.core.IResolvable], policy_name: str, remediation_enabled: typing.Union[bool, aws_cdk.core.IResolvable], resource_type: str, security_service_policy_data: typing.Any, delete_all_policy_resources: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, exclude_map: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IEMapProperty"]]]=None, include_map: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IEMapProperty"]]]=None, resource_tags: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ResourceTagProperty"]]]]]=None, resource_type_list: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List["PolicyTagProperty"]]=None) -> None:
        """Create a new ``AWS::FMS::Policy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param exclude_resource_tags: ``AWS::FMS::Policy.ExcludeResourceTags``.
        :param policy_name: ``AWS::FMS::Policy.PolicyName``.
        :param remediation_enabled: ``AWS::FMS::Policy.RemediationEnabled``.
        :param resource_type: ``AWS::FMS::Policy.ResourceType``.
        :param security_service_policy_data: ``AWS::FMS::Policy.SecurityServicePolicyData``.
        :param delete_all_policy_resources: ``AWS::FMS::Policy.DeleteAllPolicyResources``.
        :param exclude_map: ``AWS::FMS::Policy.ExcludeMap``.
        :param include_map: ``AWS::FMS::Policy.IncludeMap``.
        :param resource_tags: ``AWS::FMS::Policy.ResourceTags``.
        :param resource_type_list: ``AWS::FMS::Policy.ResourceTypeList``.
        :param tags: ``AWS::FMS::Policy.Tags``.
        """
        props = CfnPolicyProps(exclude_resource_tags=exclude_resource_tags, policy_name=policy_name, remediation_enabled=remediation_enabled, resource_type=resource_type, security_service_policy_data=security_service_policy_data, delete_all_policy_resources=delete_all_policy_resources, exclude_map=exclude_map, include_map=include_map, resource_tags=resource_tags, resource_type_list=resource_type_list, tags=tags)

        jsii.create(CfnPolicy, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Id
        """
        return jsii.get(self, "attrId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="excludeResourceTags")
    def exclude_resource_tags(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::FMS::Policy.ExcludeResourceTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        """
        return jsii.get(self, "excludeResourceTags")

    @exclude_resource_tags.setter
    def exclude_resource_tags(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        jsii.set(self, "excludeResourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> str:
        """``AWS::FMS::Policy.PolicyName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        """
        return jsii.get(self, "policyName")

    @policy_name.setter
    def policy_name(self, value: str):
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="remediationEnabled")
    def remediation_enabled(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::FMS::Policy.RemediationEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        """
        return jsii.get(self, "remediationEnabled")

    @remediation_enabled.setter
    def remediation_enabled(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        jsii.set(self, "remediationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> str:
        """``AWS::FMS::Policy.ResourceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        """
        return jsii.get(self, "resourceType")

    @resource_type.setter
    def resource_type(self, value: str):
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="securityServicePolicyData")
    def security_service_policy_data(self) -> typing.Any:
        """``AWS::FMS::Policy.SecurityServicePolicyData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        """
        return jsii.get(self, "securityServicePolicyData")

    @security_service_policy_data.setter
    def security_service_policy_data(self, value: typing.Any):
        jsii.set(self, "securityServicePolicyData", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAllPolicyResources")
    def delete_all_policy_resources(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::FMS::Policy.DeleteAllPolicyResources``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        """
        return jsii.get(self, "deleteAllPolicyResources")

    @delete_all_policy_resources.setter
    def delete_all_policy_resources(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "deleteAllPolicyResources", value)

    @builtins.property
    @jsii.member(jsii_name="excludeMap")
    def exclude_map(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IEMapProperty"]]]:
        """``AWS::FMS::Policy.ExcludeMap``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        """
        return jsii.get(self, "excludeMap")

    @exclude_map.setter
    def exclude_map(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IEMapProperty"]]]):
        jsii.set(self, "excludeMap", value)

    @builtins.property
    @jsii.member(jsii_name="includeMap")
    def include_map(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IEMapProperty"]]]:
        """``AWS::FMS::Policy.IncludeMap``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        """
        return jsii.get(self, "includeMap")

    @include_map.setter
    def include_map(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IEMapProperty"]]]):
        jsii.set(self, "includeMap", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ResourceTagProperty"]]]]]:
        """``AWS::FMS::Policy.ResourceTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        """
        return jsii.get(self, "resourceTags")

    @resource_tags.setter
    def resource_tags(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ResourceTagProperty"]]]]]):
        jsii.set(self, "resourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTypeList")
    def resource_type_list(self) -> typing.Optional[typing.List[str]]:
        """``AWS::FMS::Policy.ResourceTypeList``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        """
        return jsii.get(self, "resourceTypeList")

    @resource_type_list.setter
    def resource_type_list(self, value: typing.Optional[typing.List[str]]):
        jsii.set(self, "resourceTypeList", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["PolicyTagProperty"]]:
        """``AWS::FMS::Policy.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        """
        return jsii.get(self, "tags")

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["PolicyTagProperty"]]):
        jsii.set(self, "tags", value)

    @jsii.interface(jsii_type="@aws-cdk/aws-fms.CfnPolicy.IEMapProperty")
    class IEMapProperty(jsii.compat.Protocol):
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
        """
        @builtins.staticmethod
        def __jsii_proxy_class__():
            return _IEMapPropertyProxy

        @builtins.property
        @jsii.member(jsii_name="account")
        def account(self) -> typing.Optional[typing.List[str]]:
            """``CfnPolicy.IEMapProperty.ACCOUNT``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
            """
            ...


    class _IEMapPropertyProxy():
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
        """
        __jsii_type__ = "@aws-cdk/aws-fms.CfnPolicy.IEMapProperty"
        @builtins.property
        @jsii.member(jsii_name="account")
        def account(self) -> typing.Optional[typing.List[str]]:
            """``CfnPolicy.IEMapProperty.ACCOUNT``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
            """
            return jsii.get(self, "account")


    @jsii.data_type(jsii_type="@aws-cdk/aws-fms.CfnPolicy.PolicyTagProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class PolicyTagProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnPolicy.PolicyTagProperty.Key``.
            :param value: ``CfnPolicy.PolicyTagProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @builtins.property
        def key(self) -> str:
            """``CfnPolicy.PolicyTagProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key
            """
            return self._values.get('key')

        @builtins.property
        def value(self) -> str:
            """``CfnPolicy.PolicyTagProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PolicyTagProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-fms.CfnPolicy.ResourceTagProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class ResourceTagProperty():
        def __init__(self, *, key: str, value: typing.Optional[str]=None):
            """
            :param key: ``CfnPolicy.ResourceTagProperty.Key``.
            :param value: ``CfnPolicy.ResourceTagProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html
            """
            self._values = {
                'key': key,
            }
            if value is not None: self._values["value"] = value

        @builtins.property
        def key(self) -> str:
            """``CfnPolicy.ResourceTagProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key
            """
            return self._values.get('key')

        @builtins.property
        def value(self) -> typing.Optional[str]:
            """``CfnPolicy.ResourceTagProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ResourceTagProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-fms.CfnPolicyProps", jsii_struct_bases=[], name_mapping={'exclude_resource_tags': 'excludeResourceTags', 'policy_name': 'policyName', 'remediation_enabled': 'remediationEnabled', 'resource_type': 'resourceType', 'security_service_policy_data': 'securityServicePolicyData', 'delete_all_policy_resources': 'deleteAllPolicyResources', 'exclude_map': 'excludeMap', 'include_map': 'includeMap', 'resource_tags': 'resourceTags', 'resource_type_list': 'resourceTypeList', 'tags': 'tags'})
class CfnPolicyProps():
    def __init__(self, *, exclude_resource_tags: typing.Union[bool, aws_cdk.core.IResolvable], policy_name: str, remediation_enabled: typing.Union[bool, aws_cdk.core.IResolvable], resource_type: str, security_service_policy_data: typing.Any, delete_all_policy_resources: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, exclude_map: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPolicy.IEMapProperty"]]]=None, include_map: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPolicy.IEMapProperty"]]]=None, resource_tags: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.ResourceTagProperty"]]]]]=None, resource_type_list: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]]=None):
        """Properties for defining a ``AWS::FMS::Policy``.

        :param exclude_resource_tags: ``AWS::FMS::Policy.ExcludeResourceTags``.
        :param policy_name: ``AWS::FMS::Policy.PolicyName``.
        :param remediation_enabled: ``AWS::FMS::Policy.RemediationEnabled``.
        :param resource_type: ``AWS::FMS::Policy.ResourceType``.
        :param security_service_policy_data: ``AWS::FMS::Policy.SecurityServicePolicyData``.
        :param delete_all_policy_resources: ``AWS::FMS::Policy.DeleteAllPolicyResources``.
        :param exclude_map: ``AWS::FMS::Policy.ExcludeMap``.
        :param include_map: ``AWS::FMS::Policy.IncludeMap``.
        :param resource_tags: ``AWS::FMS::Policy.ResourceTags``.
        :param resource_type_list: ``AWS::FMS::Policy.ResourceTypeList``.
        :param tags: ``AWS::FMS::Policy.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
        """
        self._values = {
            'exclude_resource_tags': exclude_resource_tags,
            'policy_name': policy_name,
            'remediation_enabled': remediation_enabled,
            'resource_type': resource_type,
            'security_service_policy_data': security_service_policy_data,
        }
        if delete_all_policy_resources is not None: self._values["delete_all_policy_resources"] = delete_all_policy_resources
        if exclude_map is not None: self._values["exclude_map"] = exclude_map
        if include_map is not None: self._values["include_map"] = include_map
        if resource_tags is not None: self._values["resource_tags"] = resource_tags
        if resource_type_list is not None: self._values["resource_type_list"] = resource_type_list
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def exclude_resource_tags(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::FMS::Policy.ExcludeResourceTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        """
        return self._values.get('exclude_resource_tags')

    @builtins.property
    def policy_name(self) -> str:
        """``AWS::FMS::Policy.PolicyName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        """
        return self._values.get('policy_name')

    @builtins.property
    def remediation_enabled(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::FMS::Policy.RemediationEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        """
        return self._values.get('remediation_enabled')

    @builtins.property
    def resource_type(self) -> str:
        """``AWS::FMS::Policy.ResourceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        """
        return self._values.get('resource_type')

    @builtins.property
    def security_service_policy_data(self) -> typing.Any:
        """``AWS::FMS::Policy.SecurityServicePolicyData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        """
        return self._values.get('security_service_policy_data')

    @builtins.property
    def delete_all_policy_resources(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::FMS::Policy.DeleteAllPolicyResources``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        """
        return self._values.get('delete_all_policy_resources')

    @builtins.property
    def exclude_map(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPolicy.IEMapProperty"]]]:
        """``AWS::FMS::Policy.ExcludeMap``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        """
        return self._values.get('exclude_map')

    @builtins.property
    def include_map(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPolicy.IEMapProperty"]]]:
        """``AWS::FMS::Policy.IncludeMap``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        """
        return self._values.get('include_map')

    @builtins.property
    def resource_tags(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.ResourceTagProperty"]]]]]:
        """``AWS::FMS::Policy.ResourceTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        """
        return self._values.get('resource_tags')

    @builtins.property
    def resource_type_list(self) -> typing.Optional[typing.List[str]]:
        """``AWS::FMS::Policy.ResourceTypeList``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        """
        return self._values.get('resource_type_list')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]]:
        """``AWS::FMS::Policy.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnPolicyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnNotificationChannel", "CfnNotificationChannelProps", "CfnPolicy", "CfnPolicyProps", "__jsii_assembly__"]

publication.publish()
