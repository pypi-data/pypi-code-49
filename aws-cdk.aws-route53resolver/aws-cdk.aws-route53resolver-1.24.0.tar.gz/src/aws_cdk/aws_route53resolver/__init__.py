"""
## Amazon Route53 Resolver Construct Library

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

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
route53resolver = require("@aws-cdk/aws-route53resolver")
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-route53resolver", "1.24.0", __name__, "aws-route53resolver@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverEndpoint(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53resolver.CfnResolverEndpoint"):
    """A CloudFormation ``AWS::Route53Resolver::ResolverEndpoint``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
    cloudformationResource:
    :cloudformationResource:: AWS::Route53Resolver::ResolverEndpoint
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, direction: str, ip_addresses: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["IpAddressRequestProperty", aws_cdk.core.IResolvable]]], security_group_ids: typing.List[str], name: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::Route53Resolver::ResolverEndpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param direction: ``AWS::Route53Resolver::ResolverEndpoint.Direction``.
        :param ip_addresses: ``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.
        :param security_group_ids: ``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.
        :param name: ``AWS::Route53Resolver::ResolverEndpoint.Name``.
        :param tags: ``AWS::Route53Resolver::ResolverEndpoint.Tags``.
        """
        props = CfnResolverEndpointProps(direction=direction, ip_addresses=ip_addresses, security_group_ids=security_group_ids, name=name, tags=tags)

        jsii.create(CfnResolverEndpoint, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrDirection")
    def attr_direction(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Direction
        """
        return jsii.get(self, "attrDirection")

    @builtins.property
    @jsii.member(jsii_name="attrHostVpcId")
    def attr_host_vpc_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: HostVPCId
        """
        return jsii.get(self, "attrHostVpcId")

    @builtins.property
    @jsii.member(jsii_name="attrIpAddressCount")
    def attr_ip_address_count(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: IpAddressCount
        """
        return jsii.get(self, "attrIpAddressCount")

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="attrResolverEndpointId")
    def attr_resolver_endpoint_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ResolverEndpointId
        """
        return jsii.get(self, "attrResolverEndpointId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Route53Resolver::ResolverEndpoint.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> str:
        """``AWS::Route53Resolver::ResolverEndpoint.Direction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction
        """
        return jsii.get(self, "direction")

    @direction.setter
    def direction(self, value: str):
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["IpAddressRequestProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses
        """
        return jsii.get(self, "ipAddresses")

    @ip_addresses.setter
    def ip_addresses(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["IpAddressRequestProperty", aws_cdk.core.IResolvable]]]):
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[str]:
        """``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids
        """
        return jsii.get(self, "securityGroupIds")

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[str]):
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverEndpoint.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53resolver.CfnResolverEndpoint.IpAddressRequestProperty", jsii_struct_bases=[], name_mapping={'subnet_id': 'subnetId', 'ip': 'ip'})
    class IpAddressRequestProperty():
        def __init__(self, *, subnet_id: str, ip: typing.Optional[str]=None):
            """
            :param subnet_id: ``CfnResolverEndpoint.IpAddressRequestProperty.SubnetId``.
            :param ip: ``CfnResolverEndpoint.IpAddressRequestProperty.Ip``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html
            """
            self._values = {
                'subnet_id': subnet_id,
            }
            if ip is not None: self._values["ip"] = ip

        @builtins.property
        def subnet_id(self) -> str:
            """``CfnResolverEndpoint.IpAddressRequestProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid
            """
            return self._values.get('subnet_id')

        @builtins.property
        def ip(self) -> typing.Optional[str]:
            """``CfnResolverEndpoint.IpAddressRequestProperty.Ip``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip
            """
            return self._values.get('ip')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'IpAddressRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-route53resolver.CfnResolverEndpointProps", jsii_struct_bases=[], name_mapping={'direction': 'direction', 'ip_addresses': 'ipAddresses', 'security_group_ids': 'securityGroupIds', 'name': 'name', 'tags': 'tags'})
class CfnResolverEndpointProps():
    def __init__(self, *, direction: str, ip_addresses: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnResolverEndpoint.IpAddressRequestProperty", aws_cdk.core.IResolvable]]], security_group_ids: typing.List[str], name: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::Route53Resolver::ResolverEndpoint``.

        :param direction: ``AWS::Route53Resolver::ResolverEndpoint.Direction``.
        :param ip_addresses: ``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.
        :param security_group_ids: ``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.
        :param name: ``AWS::Route53Resolver::ResolverEndpoint.Name``.
        :param tags: ``AWS::Route53Resolver::ResolverEndpoint.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
        """
        self._values = {
            'direction': direction,
            'ip_addresses': ip_addresses,
            'security_group_ids': security_group_ids,
        }
        if name is not None: self._values["name"] = name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def direction(self) -> str:
        """``AWS::Route53Resolver::ResolverEndpoint.Direction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction
        """
        return self._values.get('direction')

    @builtins.property
    def ip_addresses(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnResolverEndpoint.IpAddressRequestProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses
        """
        return self._values.get('ip_addresses')

    @builtins.property
    def security_group_ids(self) -> typing.List[str]:
        """``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids
        """
        return self._values.get('security_group_ids')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverEndpoint.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name
        """
        return self._values.get('name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Route53Resolver::ResolverEndpoint.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnResolverEndpointProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverRule(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRule"):
    """A CloudFormation ``AWS::Route53Resolver::ResolverRule``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
    cloudformationResource:
    :cloudformationResource:: AWS::Route53Resolver::ResolverRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain_name: str, rule_type: str, name: typing.Optional[str]=None, resolver_endpoint_id: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, target_ips: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetAddressProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Route53Resolver::ResolverRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::Route53Resolver::ResolverRule.DomainName``.
        :param rule_type: ``AWS::Route53Resolver::ResolverRule.RuleType``.
        :param name: ``AWS::Route53Resolver::ResolverRule.Name``.
        :param resolver_endpoint_id: ``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.
        :param tags: ``AWS::Route53Resolver::ResolverRule.Tags``.
        :param target_ips: ``AWS::Route53Resolver::ResolverRule.TargetIps``.
        """
        props = CfnResolverRuleProps(domain_name=domain_name, rule_type=rule_type, name=name, resolver_endpoint_id=resolver_endpoint_id, tags=tags, target_ips=target_ips)

        jsii.create(CfnResolverRule, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DomainName
        """
        return jsii.get(self, "attrDomainName")

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="attrResolverEndpointId")
    def attr_resolver_endpoint_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ResolverEndpointId
        """
        return jsii.get(self, "attrResolverEndpointId")

    @builtins.property
    @jsii.member(jsii_name="attrResolverRuleId")
    def attr_resolver_rule_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ResolverRuleId
        """
        return jsii.get(self, "attrResolverRuleId")

    @builtins.property
    @jsii.member(jsii_name="attrTargetIps")
    def attr_target_ips(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: TargetIps
        """
        return jsii.get(self, "attrTargetIps")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Route53Resolver::ResolverRule.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """``AWS::Route53Resolver::ResolverRule.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname
        """
        return jsii.get(self, "domainName")

    @domain_name.setter
    def domain_name(self, value: str):
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> str:
        """``AWS::Route53Resolver::ResolverRule.RuleType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype
        """
        return jsii.get(self, "ruleType")

    @rule_type.setter
    def rule_type(self, value: str):
        jsii.set(self, "ruleType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverRule.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resolverEndpointId")
    def resolver_endpoint_id(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid
        """
        return jsii.get(self, "resolverEndpointId")

    @resolver_endpoint_id.setter
    def resolver_endpoint_id(self, value: typing.Optional[str]):
        jsii.set(self, "resolverEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="targetIps")
    def target_ips(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetAddressProperty"]]]]]:
        """``AWS::Route53Resolver::ResolverRule.TargetIps``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips
        """
        return jsii.get(self, "targetIps")

    @target_ips.setter
    def target_ips(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetAddressProperty"]]]]]):
        jsii.set(self, "targetIps", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRule.TargetAddressProperty", jsii_struct_bases=[], name_mapping={'ip': 'ip', 'port': 'port'})
    class TargetAddressProperty():
        def __init__(self, *, ip: str, port: typing.Optional[str]=None):
            """
            :param ip: ``CfnResolverRule.TargetAddressProperty.Ip``.
            :param port: ``CfnResolverRule.TargetAddressProperty.Port``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html
            """
            self._values = {
                'ip': ip,
            }
            if port is not None: self._values["port"] = port

        @builtins.property
        def ip(self) -> str:
            """``CfnResolverRule.TargetAddressProperty.Ip``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ip
            """
            return self._values.get('ip')

        @builtins.property
        def port(self) -> typing.Optional[str]:
            """``CfnResolverRule.TargetAddressProperty.Port``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-port
            """
            return self._values.get('port')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetAddressProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverRuleAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRuleAssociation"):
    """A CloudFormation ``AWS::Route53Resolver::ResolverRuleAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
    cloudformationResource:
    :cloudformationResource:: AWS::Route53Resolver::ResolverRuleAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, resolver_rule_id: str, vpc_id: str, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Route53Resolver::ResolverRuleAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resolver_rule_id: ``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.
        :param vpc_id: ``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.
        :param name: ``AWS::Route53Resolver::ResolverRuleAssociation.Name``.
        """
        props = CfnResolverRuleAssociationProps(resolver_rule_id=resolver_rule_id, vpc_id=vpc_id, name=name)

        jsii.create(CfnResolverRuleAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="attrResolverRuleAssociationId")
    def attr_resolver_rule_association_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ResolverRuleAssociationId
        """
        return jsii.get(self, "attrResolverRuleAssociationId")

    @builtins.property
    @jsii.member(jsii_name="attrResolverRuleId")
    def attr_resolver_rule_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ResolverRuleId
        """
        return jsii.get(self, "attrResolverRuleId")

    @builtins.property
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: VPCId
        """
        return jsii.get(self, "attrVpcId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="resolverRuleId")
    def resolver_rule_id(self) -> str:
        """``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid
        """
        return jsii.get(self, "resolverRuleId")

    @resolver_rule_id.setter
    def resolver_rule_id(self, value: str):
        jsii.set(self, "resolverRuleId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverRuleAssociation.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRuleAssociationProps", jsii_struct_bases=[], name_mapping={'resolver_rule_id': 'resolverRuleId', 'vpc_id': 'vpcId', 'name': 'name'})
class CfnResolverRuleAssociationProps():
    def __init__(self, *, resolver_rule_id: str, vpc_id: str, name: typing.Optional[str]=None):
        """Properties for defining a ``AWS::Route53Resolver::ResolverRuleAssociation``.

        :param resolver_rule_id: ``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.
        :param vpc_id: ``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.
        :param name: ``AWS::Route53Resolver::ResolverRuleAssociation.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
        """
        self._values = {
            'resolver_rule_id': resolver_rule_id,
            'vpc_id': vpc_id,
        }
        if name is not None: self._values["name"] = name

    @builtins.property
    def resolver_rule_id(self) -> str:
        """``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid
        """
        return self._values.get('resolver_rule_id')

    @builtins.property
    def vpc_id(self) -> str:
        """``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid
        """
        return self._values.get('vpc_id')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverRuleAssociation.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name
        """
        return self._values.get('name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnResolverRuleAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRuleProps", jsii_struct_bases=[], name_mapping={'domain_name': 'domainName', 'rule_type': 'ruleType', 'name': 'name', 'resolver_endpoint_id': 'resolverEndpointId', 'tags': 'tags', 'target_ips': 'targetIps'})
class CfnResolverRuleProps():
    def __init__(self, *, domain_name: str, rule_type: str, name: typing.Optional[str]=None, resolver_endpoint_id: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, target_ips: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverRule.TargetAddressProperty"]]]]]=None):
        """Properties for defining a ``AWS::Route53Resolver::ResolverRule``.

        :param domain_name: ``AWS::Route53Resolver::ResolverRule.DomainName``.
        :param rule_type: ``AWS::Route53Resolver::ResolverRule.RuleType``.
        :param name: ``AWS::Route53Resolver::ResolverRule.Name``.
        :param resolver_endpoint_id: ``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.
        :param tags: ``AWS::Route53Resolver::ResolverRule.Tags``.
        :param target_ips: ``AWS::Route53Resolver::ResolverRule.TargetIps``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
        """
        self._values = {
            'domain_name': domain_name,
            'rule_type': rule_type,
        }
        if name is not None: self._values["name"] = name
        if resolver_endpoint_id is not None: self._values["resolver_endpoint_id"] = resolver_endpoint_id
        if tags is not None: self._values["tags"] = tags
        if target_ips is not None: self._values["target_ips"] = target_ips

    @builtins.property
    def domain_name(self) -> str:
        """``AWS::Route53Resolver::ResolverRule.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname
        """
        return self._values.get('domain_name')

    @builtins.property
    def rule_type(self) -> str:
        """``AWS::Route53Resolver::ResolverRule.RuleType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype
        """
        return self._values.get('rule_type')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverRule.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name
        """
        return self._values.get('name')

    @builtins.property
    def resolver_endpoint_id(self) -> typing.Optional[str]:
        """``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid
        """
        return self._values.get('resolver_endpoint_id')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Route53Resolver::ResolverRule.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags
        """
        return self._values.get('tags')

    @builtins.property
    def target_ips(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverRule.TargetAddressProperty"]]]]]:
        """``AWS::Route53Resolver::ResolverRule.TargetIps``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips
        """
        return self._values.get('target_ips')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnResolverRuleProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnResolverEndpoint", "CfnResolverEndpointProps", "CfnResolverRule", "CfnResolverRuleAssociation", "CfnResolverRuleAssociationProps", "CfnResolverRuleProps", "__jsii_assembly__"]

publication.publish()
