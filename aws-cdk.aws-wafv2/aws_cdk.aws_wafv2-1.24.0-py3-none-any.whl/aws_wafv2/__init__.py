"""
## AWS::WAFv2 Construct Library

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
import aws_cdk.aws_wafv2 as wafv2
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-wafv2", "1.24.0", __name__, "aws-wafv2@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIPSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-wafv2.CfnIPSet"):
    """A CloudFormation ``AWS::WAFv2::IPSet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html
    cloudformationResource:
    :cloudformationResource:: AWS::WAFv2::IPSet
    """
    def __init__(self, scope_: aws_cdk.core.Construct, id: str, *, addresses: typing.Union["IPAddressesProperty", aws_cdk.core.IResolvable], ip_address_version: str, scope: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None, tags: typing.Optional["TagListProperty"]=None) -> None:
        """Create a new ``AWS::WAFv2::IPSet``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param addresses: ``AWS::WAFv2::IPSet.Addresses``.
        :param ip_address_version: ``AWS::WAFv2::IPSet.IPAddressVersion``.
        :param scope: ``AWS::WAFv2::IPSet.Scope``.
        :param description: ``AWS::WAFv2::IPSet.Description``.
        :param name: ``AWS::WAFv2::IPSet.Name``.
        :param tags: ``AWS::WAFv2::IPSet.Tags``.
        """
        props = CfnIPSetProps(addresses=addresses, ip_address_version=ip_address_version, scope=scope, description=description, name=name, tags=tags)

        jsii.create(CfnIPSet, self, [scope_, id, props])

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
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.Union["IPAddressesProperty", aws_cdk.core.IResolvable]:
        """``AWS::WAFv2::IPSet.Addresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses
        """
        return jsii.get(self, "addresses")

    @addresses.setter
    def addresses(self, value: typing.Union["IPAddressesProperty", aws_cdk.core.IResolvable]):
        jsii.set(self, "addresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressVersion")
    def ip_address_version(self) -> str:
        """``AWS::WAFv2::IPSet.IPAddressVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion
        """
        return jsii.get(self, "ipAddressVersion")

    @ip_address_version.setter
    def ip_address_version(self, value: str):
        jsii.set(self, "ipAddressVersion", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> str:
        """``AWS::WAFv2::IPSet.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope
        """
        return jsii.get(self, "scope")

    @scope.setter
    def scope(self, value: str):
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::IPSet.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::IPSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional["TagListProperty"]:
        """``AWS::WAFv2::IPSet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags
        """
        return jsii.get(self, "tags")

    @tags.setter
    def tags(self, value: typing.Optional["TagListProperty"]):
        jsii.set(self, "tags", value)

    @jsii.interface(jsii_type="@aws-cdk/aws-wafv2.CfnIPSet.IPAddressesProperty")
    class IPAddressesProperty(jsii.compat.Protocol):
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipaddresses.html
        """
        @builtins.staticmethod
        def __jsii_proxy_class__():
            return _IPAddressesPropertyProxy

        @builtins.property
        @jsii.member(jsii_name="ipAddresses")
        def ip_addresses(self) -> typing.Optional[typing.List[str]]:
            """``CfnIPSet.IPAddressesProperty.IPAddresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipaddresses.html#cfn-wafv2-ipset-ipaddresses-ipaddresses
            """
            ...


    class _IPAddressesPropertyProxy():
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipaddresses.html
        """
        __jsii_type__ = "@aws-cdk/aws-wafv2.CfnIPSet.IPAddressesProperty"
        @builtins.property
        @jsii.member(jsii_name="ipAddresses")
        def ip_addresses(self) -> typing.Optional[typing.List[str]]:
            """``CfnIPSet.IPAddressesProperty.IPAddresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipaddresses.html#cfn-wafv2-ipset-ipaddresses-ipaddresses
            """
            return jsii.get(self, "ipAddresses")


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnIPSet.TagListProperty", jsii_struct_bases=[], name_mapping={'tag_list': 'tagList'})
    class TagListProperty():
        def __init__(self, *, tag_list: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]=None):
            """
            :param tag_list: ``CfnIPSet.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-taglist.html
            """
            self._values = {
            }
            if tag_list is not None: self._values["tag_list"] = tag_list

        @builtins.property
        def tag_list(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]:
            """``CfnIPSet.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-taglist.html#cfn-wafv2-ipset-taglist-taglist
            """
            return self._values.get('tag_list')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagListProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnIPSetProps", jsii_struct_bases=[], name_mapping={'addresses': 'addresses', 'ip_address_version': 'ipAddressVersion', 'scope': 'scope', 'description': 'description', 'name': 'name', 'tags': 'tags'})
class CfnIPSetProps():
    def __init__(self, *, addresses: typing.Union["CfnIPSet.IPAddressesProperty", aws_cdk.core.IResolvable], ip_address_version: str, scope: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None, tags: typing.Optional["CfnIPSet.TagListProperty"]=None):
        """Properties for defining a ``AWS::WAFv2::IPSet``.

        :param addresses: ``AWS::WAFv2::IPSet.Addresses``.
        :param ip_address_version: ``AWS::WAFv2::IPSet.IPAddressVersion``.
        :param scope: ``AWS::WAFv2::IPSet.Scope``.
        :param description: ``AWS::WAFv2::IPSet.Description``.
        :param name: ``AWS::WAFv2::IPSet.Name``.
        :param tags: ``AWS::WAFv2::IPSet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html
        """
        if isinstance(tags, dict): tags = CfnIPSet.TagListProperty(**tags)
        self._values = {
            'addresses': addresses,
            'ip_address_version': ip_address_version,
            'scope': scope,
        }
        if description is not None: self._values["description"] = description
        if name is not None: self._values["name"] = name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def addresses(self) -> typing.Union["CfnIPSet.IPAddressesProperty", aws_cdk.core.IResolvable]:
        """``AWS::WAFv2::IPSet.Addresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses
        """
        return self._values.get('addresses')

    @builtins.property
    def ip_address_version(self) -> str:
        """``AWS::WAFv2::IPSet.IPAddressVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion
        """
        return self._values.get('ip_address_version')

    @builtins.property
    def scope(self) -> str:
        """``AWS::WAFv2::IPSet.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope
        """
        return self._values.get('scope')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::IPSet.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description
        """
        return self._values.get('description')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::IPSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name
        """
        return self._values.get('name')

    @builtins.property
    def tags(self) -> typing.Optional["CfnIPSet.TagListProperty"]:
        """``AWS::WAFv2::IPSet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnIPSetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRegexPatternSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSet"):
    """A CloudFormation ``AWS::WAFv2::RegexPatternSet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html
    cloudformationResource:
    :cloudformationResource:: AWS::WAFv2::RegexPatternSet
    """
    def __init__(self, scope_: aws_cdk.core.Construct, id: str, *, regular_expression_list: typing.Union[aws_cdk.core.IResolvable, "RegularExpressionListProperty"], scope: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None, tags: typing.Optional["TagListProperty"]=None) -> None:
        """Create a new ``AWS::WAFv2::RegexPatternSet``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param regular_expression_list: ``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.
        :param scope: ``AWS::WAFv2::RegexPatternSet.Scope``.
        :param description: ``AWS::WAFv2::RegexPatternSet.Description``.
        :param name: ``AWS::WAFv2::RegexPatternSet.Name``.
        :param tags: ``AWS::WAFv2::RegexPatternSet.Tags``.
        """
        props = CfnRegexPatternSetProps(regular_expression_list=regular_expression_list, scope=scope, description=description, name=name, tags=tags)

        jsii.create(CfnRegexPatternSet, self, [scope_, id, props])

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
    @jsii.member(jsii_name="regularExpressionList")
    def regular_expression_list(self) -> typing.Union[aws_cdk.core.IResolvable, "RegularExpressionListProperty"]:
        """``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist
        """
        return jsii.get(self, "regularExpressionList")

    @regular_expression_list.setter
    def regular_expression_list(self, value: typing.Union[aws_cdk.core.IResolvable, "RegularExpressionListProperty"]):
        jsii.set(self, "regularExpressionList", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> str:
        """``AWS::WAFv2::RegexPatternSet.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope
        """
        return jsii.get(self, "scope")

    @scope.setter
    def scope(self, value: str):
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RegexPatternSet.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RegexPatternSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional["TagListProperty"]:
        """``AWS::WAFv2::RegexPatternSet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags
        """
        return jsii.get(self, "tags")

    @tags.setter
    def tags(self, value: typing.Optional["TagListProperty"]):
        jsii.set(self, "tags", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSet.RegexProperty", jsii_struct_bases=[], name_mapping={'regex_string': 'regexString'})
    class RegexProperty():
        def __init__(self, *, regex_string: typing.Optional[str]=None):
            """
            :param regex_string: ``CfnRegexPatternSet.RegexProperty.RegexString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regex.html
            """
            self._values = {
            }
            if regex_string is not None: self._values["regex_string"] = regex_string

        @builtins.property
        def regex_string(self) -> typing.Optional[str]:
            """``CfnRegexPatternSet.RegexProperty.RegexString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regex.html#cfn-wafv2-regexpatternset-regex-regexstring
            """
            return self._values.get('regex_string')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RegexProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSet.RegularExpressionListProperty", jsii_struct_bases=[], name_mapping={'regular_expression_list': 'regularExpressionList'})
    class RegularExpressionListProperty():
        def __init__(self, *, regular_expression_list: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRegexPatternSet.RegexProperty"]]]]]=None):
            """
            :param regular_expression_list: ``CfnRegexPatternSet.RegularExpressionListProperty.RegularExpressionList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regularexpressionlist.html
            """
            self._values = {
            }
            if regular_expression_list is not None: self._values["regular_expression_list"] = regular_expression_list

        @builtins.property
        def regular_expression_list(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRegexPatternSet.RegexProperty"]]]]]:
            """``CfnRegexPatternSet.RegularExpressionListProperty.RegularExpressionList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regularexpressionlist.html#cfn-wafv2-regexpatternset-regularexpressionlist-regularexpressionlist
            """
            return self._values.get('regular_expression_list')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RegularExpressionListProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSet.TagListProperty", jsii_struct_bases=[], name_mapping={'tag_list': 'tagList'})
    class TagListProperty():
        def __init__(self, *, tag_list: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]=None):
            """
            :param tag_list: ``CfnRegexPatternSet.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-taglist.html
            """
            self._values = {
            }
            if tag_list is not None: self._values["tag_list"] = tag_list

        @builtins.property
        def tag_list(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]:
            """``CfnRegexPatternSet.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-taglist.html#cfn-wafv2-regexpatternset-taglist-taglist
            """
            return self._values.get('tag_list')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagListProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSetProps", jsii_struct_bases=[], name_mapping={'regular_expression_list': 'regularExpressionList', 'scope': 'scope', 'description': 'description', 'name': 'name', 'tags': 'tags'})
class CfnRegexPatternSetProps():
    def __init__(self, *, regular_expression_list: typing.Union[aws_cdk.core.IResolvable, "CfnRegexPatternSet.RegularExpressionListProperty"], scope: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None, tags: typing.Optional["CfnRegexPatternSet.TagListProperty"]=None):
        """Properties for defining a ``AWS::WAFv2::RegexPatternSet``.

        :param regular_expression_list: ``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.
        :param scope: ``AWS::WAFv2::RegexPatternSet.Scope``.
        :param description: ``AWS::WAFv2::RegexPatternSet.Description``.
        :param name: ``AWS::WAFv2::RegexPatternSet.Name``.
        :param tags: ``AWS::WAFv2::RegexPatternSet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html
        """
        if isinstance(tags, dict): tags = CfnRegexPatternSet.TagListProperty(**tags)
        self._values = {
            'regular_expression_list': regular_expression_list,
            'scope': scope,
        }
        if description is not None: self._values["description"] = description
        if name is not None: self._values["name"] = name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def regular_expression_list(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnRegexPatternSet.RegularExpressionListProperty"]:
        """``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist
        """
        return self._values.get('regular_expression_list')

    @builtins.property
    def scope(self) -> str:
        """``AWS::WAFv2::RegexPatternSet.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope
        """
        return self._values.get('scope')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RegexPatternSet.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description
        """
        return self._values.get('description')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RegexPatternSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name
        """
        return self._values.get('name')

    @builtins.property
    def tags(self) -> typing.Optional["CfnRegexPatternSet.TagListProperty"]:
        """``AWS::WAFv2::RegexPatternSet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRegexPatternSetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRuleGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup"):
    """A CloudFormation ``AWS::WAFv2::RuleGroup``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html
    cloudformationResource:
    :cloudformationResource:: AWS::WAFv2::RuleGroup
    """
    def __init__(self, scope_: aws_cdk.core.Construct, id: str, *, capacity: jsii.Number, scope: str, visibility_config: typing.Union[aws_cdk.core.IResolvable, "VisibilityConfigProperty"], description: typing.Optional[str]=None, name: typing.Optional[str]=None, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RulesProperty"]]]=None, tags: typing.Optional["TagListProperty"]=None) -> None:
        """Create a new ``AWS::WAFv2::RuleGroup``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param capacity: ``AWS::WAFv2::RuleGroup.Capacity``.
        :param scope: ``AWS::WAFv2::RuleGroup.Scope``.
        :param visibility_config: ``AWS::WAFv2::RuleGroup.VisibilityConfig``.
        :param description: ``AWS::WAFv2::RuleGroup.Description``.
        :param name: ``AWS::WAFv2::RuleGroup.Name``.
        :param rules: ``AWS::WAFv2::RuleGroup.Rules``.
        :param tags: ``AWS::WAFv2::RuleGroup.Tags``.
        """
        props = CfnRuleGroupProps(capacity=capacity, scope=scope, visibility_config=visibility_config, description=description, name=name, rules=rules, tags=tags)

        jsii.create(CfnRuleGroup, self, [scope_, id, props])

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
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        """``AWS::WAFv2::RuleGroup.Capacity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity
        """
        return jsii.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: jsii.Number):
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> str:
        """``AWS::WAFv2::RuleGroup.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope
        """
        return jsii.get(self, "scope")

    @scope.setter
    def scope(self, value: str):
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="visibilityConfig")
    def visibility_config(self) -> typing.Union[aws_cdk.core.IResolvable, "VisibilityConfigProperty"]:
        """``AWS::WAFv2::RuleGroup.VisibilityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig
        """
        return jsii.get(self, "visibilityConfig")

    @visibility_config.setter
    def visibility_config(self, value: typing.Union[aws_cdk.core.IResolvable, "VisibilityConfigProperty"]):
        jsii.set(self, "visibilityConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RuleGroup.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RuleGroup.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RulesProperty"]]]:
        """``AWS::WAFv2::RuleGroup.Rules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules
        """
        return jsii.get(self, "rules")

    @rules.setter
    def rules(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RulesProperty"]]]):
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional["TagListProperty"]:
        """``AWS::WAFv2::RuleGroup.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags
        """
        return jsii.get(self, "tags")

    @tags.setter
    def tags(self, value: typing.Optional["TagListProperty"]):
        jsii.set(self, "tags", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.AllQueryArgumentsProperty", jsii_struct_bases=[], name_mapping={})
    class AllQueryArgumentsProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-allqueryarguments.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AllQueryArgumentsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.AllowActionProperty", jsii_struct_bases=[], name_mapping={})
    class AllowActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-allowaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AllowActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.AndStatementOneProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class AndStatementOneProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwosProperty"]]]=None):
            """
            :param statements: ``CfnRuleGroup.AndStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementone.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwosProperty"]]]:
            """``CfnRuleGroup.AndStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementone.html#cfn-wafv2-rulegroup-andstatementone-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AndStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.AndStatementTwoProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class AndStatementTwoProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreesProperty"]]]=None):
            """
            :param statements: ``CfnRuleGroup.AndStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementtwo.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreesProperty"]]]:
            """``CfnRuleGroup.AndStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementtwo.html#cfn-wafv2-rulegroup-andstatementtwo-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AndStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.BlockActionProperty", jsii_struct_bases=[], name_mapping={})
    class BlockActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-blockaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BlockActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.BodyProperty", jsii_struct_bases=[], name_mapping={})
    class BodyProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-body.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BodyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.ByteMatchStatementProperty", jsii_struct_bases=[], name_mapping={'field_to_match': 'fieldToMatch', 'positional_constraint': 'positionalConstraint', 'search_string': 'searchString', 'search_string_base64': 'searchStringBase64', 'text_transformations': 'textTransformations'})
    class ByteMatchStatementProperty():
        def __init__(self, *, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]=None, positional_constraint: typing.Optional[str]=None, search_string: typing.Optional[str]=None, search_string_base64: typing.Optional[str]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]=None):
            """
            :param field_to_match: ``CfnRuleGroup.ByteMatchStatementProperty.FieldToMatch``.
            :param positional_constraint: ``CfnRuleGroup.ByteMatchStatementProperty.PositionalConstraint``.
            :param search_string: ``CfnRuleGroup.ByteMatchStatementProperty.SearchString``.
            :param search_string_base64: ``CfnRuleGroup.ByteMatchStatementProperty.SearchStringBase64``.
            :param text_transformations: ``CfnRuleGroup.ByteMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html
            """
            self._values = {
            }
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if positional_constraint is not None: self._values["positional_constraint"] = positional_constraint
            if search_string is not None: self._values["search_string"] = search_string
            if search_string_base64 is not None: self._values["search_string_base64"] = search_string_base64
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]:
            """``CfnRuleGroup.ByteMatchStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def positional_constraint(self) -> typing.Optional[str]:
            """``CfnRuleGroup.ByteMatchStatementProperty.PositionalConstraint``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-positionalconstraint
            """
            return self._values.get('positional_constraint')

        @builtins.property
        def search_string(self) -> typing.Optional[str]:
            """``CfnRuleGroup.ByteMatchStatementProperty.SearchString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstring
            """
            return self._values.get('search_string')

        @builtins.property
        def search_string_base64(self) -> typing.Optional[str]:
            """``CfnRuleGroup.ByteMatchStatementProperty.SearchStringBase64``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstringbase64
            """
            return self._values.get('search_string_base64')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]:
            """``CfnRuleGroup.ByteMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ByteMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.CountActionProperty", jsii_struct_bases=[], name_mapping={})
    class CountActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-countaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CountActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.CountryCodesProperty", jsii_struct_bases=[], name_mapping={'country_codes': 'countryCodes'})
    class CountryCodesProperty():
        def __init__(self, *, country_codes: typing.Optional[typing.List[str]]=None):
            """
            :param country_codes: ``CfnRuleGroup.CountryCodesProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-countrycodes.html
            """
            self._values = {
            }
            if country_codes is not None: self._values["country_codes"] = country_codes

        @builtins.property
        def country_codes(self) -> typing.Optional[typing.List[str]]:
            """``CfnRuleGroup.CountryCodesProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-countrycodes.html#cfn-wafv2-rulegroup-countrycodes-countrycodes
            """
            return self._values.get('country_codes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CountryCodesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.FieldToMatchProperty", jsii_struct_bases=[], name_mapping={'all_query_arguments': 'allQueryArguments', 'body': 'body', 'method': 'method', 'query_string': 'queryString', 'single_header': 'singleHeader', 'single_query_argument': 'singleQueryArgument', 'uri_path': 'uriPath'})
    class FieldToMatchProperty():
        def __init__(self, *, all_query_arguments: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AllQueryArgumentsProperty"]]]=None, body: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.BodyProperty"]]]=None, method: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.MethodProperty"]]]=None, query_string: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.QueryStringProperty"]]]=None, single_header: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SingleHeaderProperty"]]]=None, single_query_argument: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SingleQueryArgumentProperty"]]]=None, uri_path: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.UriPathProperty"]]]=None):
            """
            :param all_query_arguments: ``CfnRuleGroup.FieldToMatchProperty.AllQueryArguments``.
            :param body: ``CfnRuleGroup.FieldToMatchProperty.Body``.
            :param method: ``CfnRuleGroup.FieldToMatchProperty.Method``.
            :param query_string: ``CfnRuleGroup.FieldToMatchProperty.QueryString``.
            :param single_header: ``CfnRuleGroup.FieldToMatchProperty.SingleHeader``.
            :param single_query_argument: ``CfnRuleGroup.FieldToMatchProperty.SingleQueryArgument``.
            :param uri_path: ``CfnRuleGroup.FieldToMatchProperty.UriPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html
            """
            self._values = {
            }
            if all_query_arguments is not None: self._values["all_query_arguments"] = all_query_arguments
            if body is not None: self._values["body"] = body
            if method is not None: self._values["method"] = method
            if query_string is not None: self._values["query_string"] = query_string
            if single_header is not None: self._values["single_header"] = single_header
            if single_query_argument is not None: self._values["single_query_argument"] = single_query_argument
            if uri_path is not None: self._values["uri_path"] = uri_path

        @builtins.property
        def all_query_arguments(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AllQueryArgumentsProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.AllQueryArguments``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments
            """
            return self._values.get('all_query_arguments')

        @builtins.property
        def body(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.BodyProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.Body``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-body
            """
            return self._values.get('body')

        @builtins.property
        def method(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.MethodProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.Method``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-method
            """
            return self._values.get('method')

        @builtins.property
        def query_string(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.QueryStringProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.QueryString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-querystring
            """
            return self._values.get('query_string')

        @builtins.property
        def single_header(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SingleHeaderProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.SingleHeader``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singleheader
            """
            return self._values.get('single_header')

        @builtins.property
        def single_query_argument(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SingleQueryArgumentProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.SingleQueryArgument``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument
            """
            return self._values.get('single_query_argument')

        @builtins.property
        def uri_path(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.UriPathProperty"]]]:
            """``CfnRuleGroup.FieldToMatchProperty.UriPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-uripath
            """
            return self._values.get('uri_path')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FieldToMatchProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.GeoMatchStatementProperty", jsii_struct_bases=[], name_mapping={'country_codes': 'countryCodes'})
    class GeoMatchStatementProperty():
        def __init__(self, *, country_codes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.CountryCodesProperty"]]]=None):
            """
            :param country_codes: ``CfnRuleGroup.GeoMatchStatementProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html
            """
            self._values = {
            }
            if country_codes is not None: self._values["country_codes"] = country_codes

        @builtins.property
        def country_codes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.CountryCodesProperty"]]]:
            """``CfnRuleGroup.GeoMatchStatementProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-countrycodes
            """
            return self._values.get('country_codes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'GeoMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.interface(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.IPSetReferenceStatementProperty")
    class IPSetReferenceStatementProperty(jsii.compat.Protocol):
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html
        """
        @builtins.staticmethod
        def __jsii_proxy_class__():
            return _IPSetReferenceStatementPropertyProxy

        @builtins.property
        @jsii.member(jsii_name="arn")
        def arn(self) -> typing.Optional[str]:
            """``CfnRuleGroup.IPSetReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn
            """
            ...


    class _IPSetReferenceStatementPropertyProxy():
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html
        """
        __jsii_type__ = "@aws-cdk/aws-wafv2.CfnRuleGroup.IPSetReferenceStatementProperty"
        @builtins.property
        @jsii.member(jsii_name="arn")
        def arn(self) -> typing.Optional[str]:
            """``CfnRuleGroup.IPSetReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn
            """
            return jsii.get(self, "arn")


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.MethodProperty", jsii_struct_bases=[], name_mapping={})
    class MethodProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-method.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MethodProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.NotStatementOneProperty", jsii_struct_bases=[], name_mapping={'statement': 'statement'})
    class NotStatementOneProperty():
        def __init__(self, *, statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwoProperty"]]]=None):
            """
            :param statement: ``CfnRuleGroup.NotStatementOneProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementone.html
            """
            self._values = {
            }
            if statement is not None: self._values["statement"] = statement

        @builtins.property
        def statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwoProperty"]]]:
            """``CfnRuleGroup.NotStatementOneProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementone.html#cfn-wafv2-rulegroup-notstatementone-statement
            """
            return self._values.get('statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NotStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.NotStatementTwoProperty", jsii_struct_bases=[], name_mapping={'statement': 'statement'})
    class NotStatementTwoProperty():
        def __init__(self, *, statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreeProperty"]]]=None):
            """
            :param statement: ``CfnRuleGroup.NotStatementTwoProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementtwo.html
            """
            self._values = {
            }
            if statement is not None: self._values["statement"] = statement

        @builtins.property
        def statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreeProperty"]]]:
            """``CfnRuleGroup.NotStatementTwoProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementtwo.html#cfn-wafv2-rulegroup-notstatementtwo-statement
            """
            return self._values.get('statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NotStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.OrStatementOneProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class OrStatementOneProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwosProperty"]]]=None):
            """
            :param statements: ``CfnRuleGroup.OrStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementone.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwosProperty"]]]:
            """``CfnRuleGroup.OrStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementone.html#cfn-wafv2-rulegroup-orstatementone-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'OrStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.OrStatementTwoProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class OrStatementTwoProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreesProperty"]]]=None):
            """
            :param statements: ``CfnRuleGroup.OrStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementtwo.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreesProperty"]]]:
            """``CfnRuleGroup.OrStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementtwo.html#cfn-wafv2-rulegroup-orstatementtwo-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'OrStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.QueryStringProperty", jsii_struct_bases=[], name_mapping={})
    class QueryStringProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-querystring.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'QueryStringProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RateBasedStatementOneProperty", jsii_struct_bases=[], name_mapping={'aggregate_key_type': 'aggregateKeyType', 'limit': 'limit', 'scope_down_statement': 'scopeDownStatement'})
    class RateBasedStatementOneProperty():
        def __init__(self, *, aggregate_key_type: typing.Optional[str]=None, limit: typing.Optional[jsii.Number]=None, scope_down_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwoProperty"]]]=None):
            """
            :param aggregate_key_type: ``CfnRuleGroup.RateBasedStatementOneProperty.AggregateKeyType``.
            :param limit: ``CfnRuleGroup.RateBasedStatementOneProperty.Limit``.
            :param scope_down_statement: ``CfnRuleGroup.RateBasedStatementOneProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementone.html
            """
            self._values = {
            }
            if aggregate_key_type is not None: self._values["aggregate_key_type"] = aggregate_key_type
            if limit is not None: self._values["limit"] = limit
            if scope_down_statement is not None: self._values["scope_down_statement"] = scope_down_statement

        @builtins.property
        def aggregate_key_type(self) -> typing.Optional[str]:
            """``CfnRuleGroup.RateBasedStatementOneProperty.AggregateKeyType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementone.html#cfn-wafv2-rulegroup-ratebasedstatementone-aggregatekeytype
            """
            return self._values.get('aggregate_key_type')

        @builtins.property
        def limit(self) -> typing.Optional[jsii.Number]:
            """``CfnRuleGroup.RateBasedStatementOneProperty.Limit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementone.html#cfn-wafv2-rulegroup-ratebasedstatementone-limit
            """
            return self._values.get('limit')

        @builtins.property
        def scope_down_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementTwoProperty"]]]:
            """``CfnRuleGroup.RateBasedStatementOneProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementone.html#cfn-wafv2-rulegroup-ratebasedstatementone-scopedownstatement
            """
            return self._values.get('scope_down_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RateBasedStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RateBasedStatementTwoProperty", jsii_struct_bases=[], name_mapping={'aggregate_key_type': 'aggregateKeyType', 'limit': 'limit', 'scope_down_statement': 'scopeDownStatement'})
    class RateBasedStatementTwoProperty():
        def __init__(self, *, aggregate_key_type: typing.Optional[str]=None, limit: typing.Optional[jsii.Number]=None, scope_down_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreeProperty"]]]=None):
            """
            :param aggregate_key_type: ``CfnRuleGroup.RateBasedStatementTwoProperty.AggregateKeyType``.
            :param limit: ``CfnRuleGroup.RateBasedStatementTwoProperty.Limit``.
            :param scope_down_statement: ``CfnRuleGroup.RateBasedStatementTwoProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementtwo.html
            """
            self._values = {
            }
            if aggregate_key_type is not None: self._values["aggregate_key_type"] = aggregate_key_type
            if limit is not None: self._values["limit"] = limit
            if scope_down_statement is not None: self._values["scope_down_statement"] = scope_down_statement

        @builtins.property
        def aggregate_key_type(self) -> typing.Optional[str]:
            """``CfnRuleGroup.RateBasedStatementTwoProperty.AggregateKeyType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementtwo.html#cfn-wafv2-rulegroup-ratebasedstatementtwo-aggregatekeytype
            """
            return self._values.get('aggregate_key_type')

        @builtins.property
        def limit(self) -> typing.Optional[jsii.Number]:
            """``CfnRuleGroup.RateBasedStatementTwoProperty.Limit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementtwo.html#cfn-wafv2-rulegroup-ratebasedstatementtwo-limit
            """
            return self._values.get('limit')

        @builtins.property
        def scope_down_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementThreeProperty"]]]:
            """``CfnRuleGroup.RateBasedStatementTwoProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementtwo.html#cfn-wafv2-rulegroup-ratebasedstatementtwo-scopedownstatement
            """
            return self._values.get('scope_down_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RateBasedStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RegexPatternSetReferenceStatementProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn', 'field_to_match': 'fieldToMatch', 'text_transformations': 'textTransformations'})
    class RegexPatternSetReferenceStatementProperty():
        def __init__(self, *, arn: typing.Optional[str]=None, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]=None):
            """
            :param arn: ``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.Arn``.
            :param field_to_match: ``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html
            """
            self._values = {
            }
            if arn is not None: self._values["arn"] = arn
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def arn(self) -> typing.Optional[str]:
            """``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn
            """
            return self._values.get('arn')

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]:
            """``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]:
            """``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RegexPatternSetReferenceStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RuleActionProperty", jsii_struct_bases=[], name_mapping={'allow': 'allow', 'block': 'block', 'count': 'count'})
    class RuleActionProperty():
        def __init__(self, *, allow: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AllowActionProperty"]]]=None, block: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.BlockActionProperty"]]]=None, count: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.CountActionProperty"]]]=None):
            """
            :param allow: ``CfnRuleGroup.RuleActionProperty.Allow``.
            :param block: ``CfnRuleGroup.RuleActionProperty.Block``.
            :param count: ``CfnRuleGroup.RuleActionProperty.Count``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html
            """
            self._values = {
            }
            if allow is not None: self._values["allow"] = allow
            if block is not None: self._values["block"] = block
            if count is not None: self._values["count"] = count

        @builtins.property
        def allow(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AllowActionProperty"]]]:
            """``CfnRuleGroup.RuleActionProperty.Allow``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-allow
            """
            return self._values.get('allow')

        @builtins.property
        def block(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.BlockActionProperty"]]]:
            """``CfnRuleGroup.RuleActionProperty.Block``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-block
            """
            return self._values.get('block')

        @builtins.property
        def count(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.CountActionProperty"]]]:
            """``CfnRuleGroup.RuleActionProperty.Count``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-count
            """
            return self._values.get('count')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RuleProperty", jsii_struct_bases=[], name_mapping={'action': 'action', 'name': 'name', 'priority': 'priority', 'statement': 'statement', 'visibility_config': 'visibilityConfig'})
    class RuleProperty():
        def __init__(self, *, action: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RuleActionProperty"]]]=None, name: typing.Optional[str]=None, priority: typing.Optional[jsii.Number]=None, statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementOneProperty"]]]=None, visibility_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.VisibilityConfigProperty"]]]=None):
            """
            :param action: ``CfnRuleGroup.RuleProperty.Action``.
            :param name: ``CfnRuleGroup.RuleProperty.Name``.
            :param priority: ``CfnRuleGroup.RuleProperty.Priority``.
            :param statement: ``CfnRuleGroup.RuleProperty.Statement``.
            :param visibility_config: ``CfnRuleGroup.RuleProperty.VisibilityConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html
            """
            self._values = {
            }
            if action is not None: self._values["action"] = action
            if name is not None: self._values["name"] = name
            if priority is not None: self._values["priority"] = priority
            if statement is not None: self._values["statement"] = statement
            if visibility_config is not None: self._values["visibility_config"] = visibility_config

        @builtins.property
        def action(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RuleActionProperty"]]]:
            """``CfnRuleGroup.RuleProperty.Action``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-action
            """
            return self._values.get('action')

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnRuleGroup.RuleProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-name
            """
            return self._values.get('name')

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnRuleGroup.RuleProperty.Priority``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-priority
            """
            return self._values.get('priority')

        @builtins.property
        def statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.StatementOneProperty"]]]:
            """``CfnRuleGroup.RuleProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-statement
            """
            return self._values.get('statement')

        @builtins.property
        def visibility_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.VisibilityConfigProperty"]]]:
            """``CfnRuleGroup.RuleProperty.VisibilityConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-visibilityconfig
            """
            return self._values.get('visibility_config')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RulesProperty", jsii_struct_bases=[], name_mapping={'rules': 'rules'})
    class RulesProperty():
        def __init__(self, *, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleProperty"]]]]]=None):
            """
            :param rules: ``CfnRuleGroup.RulesProperty.Rules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rules.html
            """
            self._values = {
            }
            if rules is not None: self._values["rules"] = rules

        @builtins.property
        def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleProperty"]]]]]:
            """``CfnRuleGroup.RulesProperty.Rules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rules.html#cfn-wafv2-rulegroup-rules-rules
            """
            return self._values.get('rules')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RulesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.SingleHeaderProperty", jsii_struct_bases=[], name_mapping={'name': 'name'})
    class SingleHeaderProperty():
        def __init__(self, *, name: typing.Optional[str]=None):
            """
            :param name: ``CfnRuleGroup.SingleHeaderProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singleheader.html
            """
            self._values = {
            }
            if name is not None: self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnRuleGroup.SingleHeaderProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singleheader.html#cfn-wafv2-rulegroup-singleheader-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SingleHeaderProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.SingleQueryArgumentProperty", jsii_struct_bases=[], name_mapping={'name': 'name'})
    class SingleQueryArgumentProperty():
        def __init__(self, *, name: typing.Optional[str]=None):
            """
            :param name: ``CfnRuleGroup.SingleQueryArgumentProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singlequeryargument.html
            """
            self._values = {
            }
            if name is not None: self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnRuleGroup.SingleQueryArgumentProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singlequeryargument.html#cfn-wafv2-rulegroup-singlequeryargument-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SingleQueryArgumentProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.SizeConstraintStatementProperty", jsii_struct_bases=[], name_mapping={'comparison_operator': 'comparisonOperator', 'field_to_match': 'fieldToMatch', 'size': 'size', 'text_transformations': 'textTransformations'})
    class SizeConstraintStatementProperty():
        def __init__(self, *, comparison_operator: typing.Optional[str]=None, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]=None, size: typing.Optional[jsii.Number]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]=None):
            """
            :param comparison_operator: ``CfnRuleGroup.SizeConstraintStatementProperty.ComparisonOperator``.
            :param field_to_match: ``CfnRuleGroup.SizeConstraintStatementProperty.FieldToMatch``.
            :param size: ``CfnRuleGroup.SizeConstraintStatementProperty.Size``.
            :param text_transformations: ``CfnRuleGroup.SizeConstraintStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html
            """
            self._values = {
            }
            if comparison_operator is not None: self._values["comparison_operator"] = comparison_operator
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if size is not None: self._values["size"] = size
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def comparison_operator(self) -> typing.Optional[str]:
            """``CfnRuleGroup.SizeConstraintStatementProperty.ComparisonOperator``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-comparisonoperator
            """
            return self._values.get('comparison_operator')

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]:
            """``CfnRuleGroup.SizeConstraintStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            """``CfnRuleGroup.SizeConstraintStatementProperty.Size``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-size
            """
            return self._values.get('size')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]:
            """``CfnRuleGroup.SizeConstraintStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SizeConstraintStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.SqliMatchStatementProperty", jsii_struct_bases=[], name_mapping={'field_to_match': 'fieldToMatch', 'text_transformations': 'textTransformations'})
    class SqliMatchStatementProperty():
        def __init__(self, *, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]=None):
            """
            :param field_to_match: ``CfnRuleGroup.SqliMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnRuleGroup.SqliMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html
            """
            self._values = {
            }
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]:
            """``CfnRuleGroup.SqliMatchStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]:
            """``CfnRuleGroup.SqliMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SqliMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.StatementOneProperty", jsii_struct_bases=[], name_mapping={'and_statement': 'andStatement', 'byte_match_statement': 'byteMatchStatement', 'geo_match_statement': 'geoMatchStatement', 'ip_set_reference_statement': 'ipSetReferenceStatement', 'not_statement': 'notStatement', 'or_statement': 'orStatement', 'rate_based_statement': 'rateBasedStatement', 'regex_pattern_set_reference_statement': 'regexPatternSetReferenceStatement', 'size_constraint_statement': 'sizeConstraintStatement', 'sqli_match_statement': 'sqliMatchStatement', 'xss_match_statement': 'xssMatchStatement'})
    class StatementOneProperty():
        def __init__(self, *, and_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AndStatementOneProperty"]]]=None, byte_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.ByteMatchStatementProperty"]]]=None, geo_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.GeoMatchStatementProperty"]]]=None, ip_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.IPSetReferenceStatementProperty"]]]=None, not_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.NotStatementOneProperty"]]]=None, or_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.OrStatementOneProperty"]]]=None, rate_based_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RateBasedStatementOneProperty"]]]=None, regex_pattern_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]]=None, size_constraint_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SizeConstraintStatementProperty"]]]=None, sqli_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SqliMatchStatementProperty"]]]=None, xss_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.XssMatchStatementProperty"]]]=None):
            """
            :param and_statement: ``CfnRuleGroup.StatementOneProperty.AndStatement``.
            :param byte_match_statement: ``CfnRuleGroup.StatementOneProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnRuleGroup.StatementOneProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnRuleGroup.StatementOneProperty.IPSetReferenceStatement``.
            :param not_statement: ``CfnRuleGroup.StatementOneProperty.NotStatement``.
            :param or_statement: ``CfnRuleGroup.StatementOneProperty.OrStatement``.
            :param rate_based_statement: ``CfnRuleGroup.StatementOneProperty.RateBasedStatement``.
            :param regex_pattern_set_reference_statement: ``CfnRuleGroup.StatementOneProperty.RegexPatternSetReferenceStatement``.
            :param size_constraint_statement: ``CfnRuleGroup.StatementOneProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnRuleGroup.StatementOneProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnRuleGroup.StatementOneProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html
            """
            self._values = {
            }
            if and_statement is not None: self._values["and_statement"] = and_statement
            if byte_match_statement is not None: self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None: self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None: self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if not_statement is not None: self._values["not_statement"] = not_statement
            if or_statement is not None: self._values["or_statement"] = or_statement
            if rate_based_statement is not None: self._values["rate_based_statement"] = rate_based_statement
            if regex_pattern_set_reference_statement is not None: self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if size_constraint_statement is not None: self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None: self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None: self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def and_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AndStatementOneProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.AndStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-andstatement
            """
            return self._values.get('and_statement')

        @builtins.property
        def byte_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.ByteMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.ByteMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-bytematchstatement
            """
            return self._values.get('byte_match_statement')

        @builtins.property
        def geo_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.GeoMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.GeoMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-geomatchstatement
            """
            return self._values.get('geo_match_statement')

        @builtins.property
        def ip_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.IPSetReferenceStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.IPSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-ipsetreferencestatement
            """
            return self._values.get('ip_set_reference_statement')

        @builtins.property
        def not_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.NotStatementOneProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.NotStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-notstatement
            """
            return self._values.get('not_statement')

        @builtins.property
        def or_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.OrStatementOneProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.OrStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-orstatement
            """
            return self._values.get('or_statement')

        @builtins.property
        def rate_based_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RateBasedStatementOneProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.RateBasedStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-ratebasedstatement
            """
            return self._values.get('rate_based_statement')

        @builtins.property
        def regex_pattern_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.RegexPatternSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-regexpatternsetreferencestatement
            """
            return self._values.get('regex_pattern_set_reference_statement')

        @builtins.property
        def size_constraint_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SizeConstraintStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.SizeConstraintStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-sizeconstraintstatement
            """
            return self._values.get('size_constraint_statement')

        @builtins.property
        def sqli_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SqliMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.SqliMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-sqlimatchstatement
            """
            return self._values.get('sqli_match_statement')

        @builtins.property
        def xss_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.XssMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementOneProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html#cfn-wafv2-rulegroup-statementone-xssmatchstatement
            """
            return self._values.get('xss_match_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.StatementThreeProperty", jsii_struct_bases=[], name_mapping={'byte_match_statement': 'byteMatchStatement', 'geo_match_statement': 'geoMatchStatement', 'ip_set_reference_statement': 'ipSetReferenceStatement', 'regex_pattern_set_reference_statement': 'regexPatternSetReferenceStatement', 'size_constraint_statement': 'sizeConstraintStatement', 'sqli_match_statement': 'sqliMatchStatement', 'xss_match_statement': 'xssMatchStatement'})
    class StatementThreeProperty():
        def __init__(self, *, byte_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.ByteMatchStatementProperty"]]]=None, geo_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.GeoMatchStatementProperty"]]]=None, ip_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.IPSetReferenceStatementProperty"]]]=None, regex_pattern_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]]=None, size_constraint_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SizeConstraintStatementProperty"]]]=None, sqli_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SqliMatchStatementProperty"]]]=None, xss_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.XssMatchStatementProperty"]]]=None):
            """
            :param byte_match_statement: ``CfnRuleGroup.StatementThreeProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnRuleGroup.StatementThreeProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnRuleGroup.StatementThreeProperty.IPSetReferenceStatement``.
            :param regex_pattern_set_reference_statement: ``CfnRuleGroup.StatementThreeProperty.RegexPatternSetReferenceStatement``.
            :param size_constraint_statement: ``CfnRuleGroup.StatementThreeProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnRuleGroup.StatementThreeProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnRuleGroup.StatementThreeProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html
            """
            self._values = {
            }
            if byte_match_statement is not None: self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None: self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None: self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if regex_pattern_set_reference_statement is not None: self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if size_constraint_statement is not None: self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None: self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None: self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def byte_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.ByteMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.ByteMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-bytematchstatement
            """
            return self._values.get('byte_match_statement')

        @builtins.property
        def geo_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.GeoMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.GeoMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-geomatchstatement
            """
            return self._values.get('geo_match_statement')

        @builtins.property
        def ip_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.IPSetReferenceStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.IPSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-ipsetreferencestatement
            """
            return self._values.get('ip_set_reference_statement')

        @builtins.property
        def regex_pattern_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.RegexPatternSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-regexpatternsetreferencestatement
            """
            return self._values.get('regex_pattern_set_reference_statement')

        @builtins.property
        def size_constraint_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SizeConstraintStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.SizeConstraintStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-sizeconstraintstatement
            """
            return self._values.get('size_constraint_statement')

        @builtins.property
        def sqli_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SqliMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.SqliMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-sqlimatchstatement
            """
            return self._values.get('sqli_match_statement')

        @builtins.property
        def xss_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.XssMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementThreeProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html#cfn-wafv2-rulegroup-statementthree-xssmatchstatement
            """
            return self._values.get('xss_match_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementThreeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.StatementThreesProperty", jsii_struct_bases=[], name_mapping={'statement_threes': 'statementThrees'})
    class StatementThreesProperty():
        def __init__(self, *, statement_threes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementThreeProperty"]]]]]=None):
            """
            :param statement_threes: ``CfnRuleGroup.StatementThreesProperty.StatementThrees``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthrees.html
            """
            self._values = {
            }
            if statement_threes is not None: self._values["statement_threes"] = statement_threes

        @builtins.property
        def statement_threes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementThreeProperty"]]]]]:
            """``CfnRuleGroup.StatementThreesProperty.StatementThrees``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthrees.html#cfn-wafv2-rulegroup-statementthrees-statementthrees
            """
            return self._values.get('statement_threes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementThreesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.StatementTwoProperty", jsii_struct_bases=[], name_mapping={'and_statement': 'andStatement', 'byte_match_statement': 'byteMatchStatement', 'geo_match_statement': 'geoMatchStatement', 'ip_set_reference_statement': 'ipSetReferenceStatement', 'not_statement': 'notStatement', 'or_statement': 'orStatement', 'rate_based_statement': 'rateBasedStatement', 'regex_pattern_set_reference_statement': 'regexPatternSetReferenceStatement', 'size_constraint_statement': 'sizeConstraintStatement', 'sqli_match_statement': 'sqliMatchStatement', 'xss_match_statement': 'xssMatchStatement'})
    class StatementTwoProperty():
        def __init__(self, *, and_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AndStatementTwoProperty"]]]=None, byte_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.ByteMatchStatementProperty"]]]=None, geo_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.GeoMatchStatementProperty"]]]=None, ip_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.IPSetReferenceStatementProperty"]]]=None, not_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.NotStatementTwoProperty"]]]=None, or_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.OrStatementTwoProperty"]]]=None, rate_based_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RateBasedStatementTwoProperty"]]]=None, regex_pattern_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]]=None, size_constraint_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SizeConstraintStatementProperty"]]]=None, sqli_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SqliMatchStatementProperty"]]]=None, xss_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.XssMatchStatementProperty"]]]=None):
            """
            :param and_statement: ``CfnRuleGroup.StatementTwoProperty.AndStatement``.
            :param byte_match_statement: ``CfnRuleGroup.StatementTwoProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnRuleGroup.StatementTwoProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnRuleGroup.StatementTwoProperty.IPSetReferenceStatement``.
            :param not_statement: ``CfnRuleGroup.StatementTwoProperty.NotStatement``.
            :param or_statement: ``CfnRuleGroup.StatementTwoProperty.OrStatement``.
            :param rate_based_statement: ``CfnRuleGroup.StatementTwoProperty.RateBasedStatement``.
            :param regex_pattern_set_reference_statement: ``CfnRuleGroup.StatementTwoProperty.RegexPatternSetReferenceStatement``.
            :param size_constraint_statement: ``CfnRuleGroup.StatementTwoProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnRuleGroup.StatementTwoProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnRuleGroup.StatementTwoProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html
            """
            self._values = {
            }
            if and_statement is not None: self._values["and_statement"] = and_statement
            if byte_match_statement is not None: self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None: self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None: self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if not_statement is not None: self._values["not_statement"] = not_statement
            if or_statement is not None: self._values["or_statement"] = or_statement
            if rate_based_statement is not None: self._values["rate_based_statement"] = rate_based_statement
            if regex_pattern_set_reference_statement is not None: self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if size_constraint_statement is not None: self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None: self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None: self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def and_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.AndStatementTwoProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.AndStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-andstatement
            """
            return self._values.get('and_statement')

        @builtins.property
        def byte_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.ByteMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.ByteMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-bytematchstatement
            """
            return self._values.get('byte_match_statement')

        @builtins.property
        def geo_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.GeoMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.GeoMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-geomatchstatement
            """
            return self._values.get('geo_match_statement')

        @builtins.property
        def ip_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.IPSetReferenceStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.IPSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-ipsetreferencestatement
            """
            return self._values.get('ip_set_reference_statement')

        @builtins.property
        def not_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.NotStatementTwoProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.NotStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-notstatement
            """
            return self._values.get('not_statement')

        @builtins.property
        def or_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.OrStatementTwoProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.OrStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-orstatement
            """
            return self._values.get('or_statement')

        @builtins.property
        def rate_based_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RateBasedStatementTwoProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.RateBasedStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-ratebasedstatement
            """
            return self._values.get('rate_based_statement')

        @builtins.property
        def regex_pattern_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.RegexPatternSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-regexpatternsetreferencestatement
            """
            return self._values.get('regex_pattern_set_reference_statement')

        @builtins.property
        def size_constraint_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SizeConstraintStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.SizeConstraintStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-sizeconstraintstatement
            """
            return self._values.get('size_constraint_statement')

        @builtins.property
        def sqli_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.SqliMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.SqliMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-sqlimatchstatement
            """
            return self._values.get('sqli_match_statement')

        @builtins.property
        def xss_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.XssMatchStatementProperty"]]]:
            """``CfnRuleGroup.StatementTwoProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html#cfn-wafv2-rulegroup-statementtwo-xssmatchstatement
            """
            return self._values.get('xss_match_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.StatementTwosProperty", jsii_struct_bases=[], name_mapping={'statement_twos': 'statementTwos'})
    class StatementTwosProperty():
        def __init__(self, *, statement_twos: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementTwoProperty"]]]]]=None):
            """
            :param statement_twos: ``CfnRuleGroup.StatementTwosProperty.StatementTwos``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwos.html
            """
            self._values = {
            }
            if statement_twos is not None: self._values["statement_twos"] = statement_twos

        @builtins.property
        def statement_twos(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementTwoProperty"]]]]]:
            """``CfnRuleGroup.StatementTwosProperty.StatementTwos``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwos.html#cfn-wafv2-rulegroup-statementtwos-statementtwos
            """
            return self._values.get('statement_twos')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementTwosProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.TagListProperty", jsii_struct_bases=[], name_mapping={'tag_list': 'tagList'})
    class TagListProperty():
        def __init__(self, *, tag_list: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]=None):
            """
            :param tag_list: ``CfnRuleGroup.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-taglist.html
            """
            self._values = {
            }
            if tag_list is not None: self._values["tag_list"] = tag_list

        @builtins.property
        def tag_list(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]:
            """``CfnRuleGroup.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-taglist.html#cfn-wafv2-rulegroup-taglist-taglist
            """
            return self._values.get('tag_list')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagListProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.TextTransformationProperty", jsii_struct_bases=[], name_mapping={'priority': 'priority', 'type': 'type'})
    class TextTransformationProperty():
        def __init__(self, *, priority: typing.Optional[jsii.Number]=None, type: typing.Optional[str]=None):
            """
            :param priority: ``CfnRuleGroup.TextTransformationProperty.Priority``.
            :param type: ``CfnRuleGroup.TextTransformationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html
            """
            self._values = {
            }
            if priority is not None: self._values["priority"] = priority
            if type is not None: self._values["type"] = type

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnRuleGroup.TextTransformationProperty.Priority``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-priority
            """
            return self._values.get('priority')

        @builtins.property
        def type(self) -> typing.Optional[str]:
            """``CfnRuleGroup.TextTransformationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TextTransformationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.TextTransformationsProperty", jsii_struct_bases=[], name_mapping={'text_transformations': 'textTransformations'})
    class TextTransformationsProperty():
        def __init__(self, *, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]]]=None):
            """
            :param text_transformations: ``CfnRuleGroup.TextTransformationsProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformations.html
            """
            self._values = {
            }
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]]]:
            """``CfnRuleGroup.TextTransformationsProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformations.html#cfn-wafv2-rulegroup-texttransformations-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TextTransformationsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.UriPathProperty", jsii_struct_bases=[], name_mapping={})
    class UriPathProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-uripath.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'UriPathProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.VisibilityConfigProperty", jsii_struct_bases=[], name_mapping={'cloud_watch_metrics_enabled': 'cloudWatchMetricsEnabled', 'metric_name': 'metricName', 'sampled_requests_enabled': 'sampledRequestsEnabled'})
    class VisibilityConfigProperty():
        def __init__(self, *, cloud_watch_metrics_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, metric_name: typing.Optional[str]=None, sampled_requests_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param cloud_watch_metrics_enabled: ``CfnRuleGroup.VisibilityConfigProperty.CloudWatchMetricsEnabled``.
            :param metric_name: ``CfnRuleGroup.VisibilityConfigProperty.MetricName``.
            :param sampled_requests_enabled: ``CfnRuleGroup.VisibilityConfigProperty.SampledRequestsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html
            """
            self._values = {
            }
            if cloud_watch_metrics_enabled is not None: self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled
            if metric_name is not None: self._values["metric_name"] = metric_name
            if sampled_requests_enabled is not None: self._values["sampled_requests_enabled"] = sampled_requests_enabled

        @builtins.property
        def cloud_watch_metrics_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnRuleGroup.VisibilityConfigProperty.CloudWatchMetricsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled
            """
            return self._values.get('cloud_watch_metrics_enabled')

        @builtins.property
        def metric_name(self) -> typing.Optional[str]:
            """``CfnRuleGroup.VisibilityConfigProperty.MetricName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-metricname
            """
            return self._values.get('metric_name')

        @builtins.property
        def sampled_requests_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnRuleGroup.VisibilityConfigProperty.SampledRequestsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled
            """
            return self._values.get('sampled_requests_enabled')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'VisibilityConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.XssMatchStatementProperty", jsii_struct_bases=[], name_mapping={'field_to_match': 'fieldToMatch', 'text_transformations': 'textTransformations'})
    class XssMatchStatementProperty():
        def __init__(self, *, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]=None):
            """
            :param field_to_match: ``CfnRuleGroup.XssMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnRuleGroup.XssMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html
            """
            self._values = {
            }
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.FieldToMatchProperty"]]]:
            """``CfnRuleGroup.XssMatchStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.TextTransformationsProperty"]]]:
            """``CfnRuleGroup.XssMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'XssMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroupProps", jsii_struct_bases=[], name_mapping={'capacity': 'capacity', 'scope': 'scope', 'visibility_config': 'visibilityConfig', 'description': 'description', 'name': 'name', 'rules': 'rules', 'tags': 'tags'})
class CfnRuleGroupProps():
    def __init__(self, *, capacity: jsii.Number, scope: str, visibility_config: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"], description: typing.Optional[str]=None, name: typing.Optional[str]=None, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RulesProperty"]]]=None, tags: typing.Optional["CfnRuleGroup.TagListProperty"]=None):
        """Properties for defining a ``AWS::WAFv2::RuleGroup``.

        :param capacity: ``AWS::WAFv2::RuleGroup.Capacity``.
        :param scope: ``AWS::WAFv2::RuleGroup.Scope``.
        :param visibility_config: ``AWS::WAFv2::RuleGroup.VisibilityConfig``.
        :param description: ``AWS::WAFv2::RuleGroup.Description``.
        :param name: ``AWS::WAFv2::RuleGroup.Name``.
        :param rules: ``AWS::WAFv2::RuleGroup.Rules``.
        :param tags: ``AWS::WAFv2::RuleGroup.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html
        """
        if isinstance(tags, dict): tags = CfnRuleGroup.TagListProperty(**tags)
        self._values = {
            'capacity': capacity,
            'scope': scope,
            'visibility_config': visibility_config,
        }
        if description is not None: self._values["description"] = description
        if name is not None: self._values["name"] = name
        if rules is not None: self._values["rules"] = rules
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def capacity(self) -> jsii.Number:
        """``AWS::WAFv2::RuleGroup.Capacity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity
        """
        return self._values.get('capacity')

    @builtins.property
    def scope(self) -> str:
        """``AWS::WAFv2::RuleGroup.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope
        """
        return self._values.get('scope')

    @builtins.property
    def visibility_config(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"]:
        """``AWS::WAFv2::RuleGroup.VisibilityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig
        """
        return self._values.get('visibility_config')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RuleGroup.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description
        """
        return self._values.get('description')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::RuleGroup.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name
        """
        return self._values.get('name')

    @builtins.property
    def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRuleGroup.RulesProperty"]]]:
        """``AWS::WAFv2::RuleGroup.Rules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules
        """
        return self._values.get('rules')

    @builtins.property
    def tags(self) -> typing.Optional["CfnRuleGroup.TagListProperty"]:
        """``AWS::WAFv2::RuleGroup.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRuleGroupProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWebACL(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-wafv2.CfnWebACL"):
    """A CloudFormation ``AWS::WAFv2::WebACL``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html
    cloudformationResource:
    :cloudformationResource:: AWS::WAFv2::WebACL
    """
    def __init__(self, scope_: aws_cdk.core.Construct, id: str, *, default_action: typing.Union[aws_cdk.core.IResolvable, "DefaultActionProperty"], scope: str, visibility_config: typing.Union[aws_cdk.core.IResolvable, "VisibilityConfigProperty"], description: typing.Optional[str]=None, name: typing.Optional[str]=None, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RulesProperty"]]]=None, tags: typing.Optional["TagListProperty"]=None) -> None:
        """Create a new ``AWS::WAFv2::WebACL``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param default_action: ``AWS::WAFv2::WebACL.DefaultAction``.
        :param scope: ``AWS::WAFv2::WebACL.Scope``.
        :param visibility_config: ``AWS::WAFv2::WebACL.VisibilityConfig``.
        :param description: ``AWS::WAFv2::WebACL.Description``.
        :param name: ``AWS::WAFv2::WebACL.Name``.
        :param rules: ``AWS::WAFv2::WebACL.Rules``.
        :param tags: ``AWS::WAFv2::WebACL.Tags``.
        """
        props = CfnWebACLProps(default_action=default_action, scope=scope, visibility_config=visibility_config, description=description, name=name, rules=rules, tags=tags)

        jsii.create(CfnWebACL, self, [scope_, id, props])

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
    @jsii.member(jsii_name="attrCapacity")
    def attr_capacity(self) -> jsii.Number:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Capacity
        """
        return jsii.get(self, "attrCapacity")

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
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> typing.Union[aws_cdk.core.IResolvable, "DefaultActionProperty"]:
        """``AWS::WAFv2::WebACL.DefaultAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction
        """
        return jsii.get(self, "defaultAction")

    @default_action.setter
    def default_action(self, value: typing.Union[aws_cdk.core.IResolvable, "DefaultActionProperty"]):
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> str:
        """``AWS::WAFv2::WebACL.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope
        """
        return jsii.get(self, "scope")

    @scope.setter
    def scope(self, value: str):
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="visibilityConfig")
    def visibility_config(self) -> typing.Union[aws_cdk.core.IResolvable, "VisibilityConfigProperty"]:
        """``AWS::WAFv2::WebACL.VisibilityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig
        """
        return jsii.get(self, "visibilityConfig")

    @visibility_config.setter
    def visibility_config(self, value: typing.Union[aws_cdk.core.IResolvable, "VisibilityConfigProperty"]):
        jsii.set(self, "visibilityConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::WebACL.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::WebACL.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RulesProperty"]]]:
        """``AWS::WAFv2::WebACL.Rules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules
        """
        return jsii.get(self, "rules")

    @rules.setter
    def rules(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RulesProperty"]]]):
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional["TagListProperty"]:
        """``AWS::WAFv2::WebACL.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags
        """
        return jsii.get(self, "tags")

    @tags.setter
    def tags(self, value: typing.Optional["TagListProperty"]):
        jsii.set(self, "tags", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.AllQueryArgumentsProperty", jsii_struct_bases=[], name_mapping={})
    class AllQueryArgumentsProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allqueryarguments.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AllQueryArgumentsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.AllowActionProperty", jsii_struct_bases=[], name_mapping={})
    class AllowActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AllowActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.AndStatementOneProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class AndStatementOneProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwosProperty"]]]=None):
            """
            :param statements: ``CfnWebACL.AndStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementone.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwosProperty"]]]:
            """``CfnWebACL.AndStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementone.html#cfn-wafv2-webacl-andstatementone-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AndStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.AndStatementTwoProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class AndStatementTwoProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreesProperty"]]]=None):
            """
            :param statements: ``CfnWebACL.AndStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementtwo.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreesProperty"]]]:
            """``CfnWebACL.AndStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementtwo.html#cfn-wafv2-webacl-andstatementtwo-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AndStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.BlockActionProperty", jsii_struct_bases=[], name_mapping={})
    class BlockActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BlockActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.BodyProperty", jsii_struct_bases=[], name_mapping={})
    class BodyProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-body.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BodyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ByteMatchStatementProperty", jsii_struct_bases=[], name_mapping={'field_to_match': 'fieldToMatch', 'positional_constraint': 'positionalConstraint', 'search_string': 'searchString', 'search_string_base64': 'searchStringBase64', 'text_transformations': 'textTransformations'})
    class ByteMatchStatementProperty():
        def __init__(self, *, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]=None, positional_constraint: typing.Optional[str]=None, search_string: typing.Optional[str]=None, search_string_base64: typing.Optional[str]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]=None):
            """
            :param field_to_match: ``CfnWebACL.ByteMatchStatementProperty.FieldToMatch``.
            :param positional_constraint: ``CfnWebACL.ByteMatchStatementProperty.PositionalConstraint``.
            :param search_string: ``CfnWebACL.ByteMatchStatementProperty.SearchString``.
            :param search_string_base64: ``CfnWebACL.ByteMatchStatementProperty.SearchStringBase64``.
            :param text_transformations: ``CfnWebACL.ByteMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html
            """
            self._values = {
            }
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if positional_constraint is not None: self._values["positional_constraint"] = positional_constraint
            if search_string is not None: self._values["search_string"] = search_string
            if search_string_base64 is not None: self._values["search_string_base64"] = search_string_base64
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]:
            """``CfnWebACL.ByteMatchStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def positional_constraint(self) -> typing.Optional[str]:
            """``CfnWebACL.ByteMatchStatementProperty.PositionalConstraint``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-positionalconstraint
            """
            return self._values.get('positional_constraint')

        @builtins.property
        def search_string(self) -> typing.Optional[str]:
            """``CfnWebACL.ByteMatchStatementProperty.SearchString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstring
            """
            return self._values.get('search_string')

        @builtins.property
        def search_string_base64(self) -> typing.Optional[str]:
            """``CfnWebACL.ByteMatchStatementProperty.SearchStringBase64``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstringbase64
            """
            return self._values.get('search_string_base64')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]:
            """``CfnWebACL.ByteMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ByteMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CountActionProperty", jsii_struct_bases=[], name_mapping={})
    class CountActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CountActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CountryCodesProperty", jsii_struct_bases=[], name_mapping={'country_codes': 'countryCodes'})
    class CountryCodesProperty():
        def __init__(self, *, country_codes: typing.Optional[typing.List[str]]=None):
            """
            :param country_codes: ``CfnWebACL.CountryCodesProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countrycodes.html
            """
            self._values = {
            }
            if country_codes is not None: self._values["country_codes"] = country_codes

        @builtins.property
        def country_codes(self) -> typing.Optional[typing.List[str]]:
            """``CfnWebACL.CountryCodesProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countrycodes.html#cfn-wafv2-webacl-countrycodes-countrycodes
            """
            return self._values.get('country_codes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CountryCodesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.DefaultActionProperty", jsii_struct_bases=[], name_mapping={'allow': 'allow', 'block': 'block'})
    class DefaultActionProperty():
        def __init__(self, *, allow: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AllowActionProperty"]]]=None, block: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.BlockActionProperty"]]]=None):
            """
            :param allow: ``CfnWebACL.DefaultActionProperty.Allow``.
            :param block: ``CfnWebACL.DefaultActionProperty.Block``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html
            """
            self._values = {
            }
            if allow is not None: self._values["allow"] = allow
            if block is not None: self._values["block"] = block

        @builtins.property
        def allow(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AllowActionProperty"]]]:
            """``CfnWebACL.DefaultActionProperty.Allow``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-allow
            """
            return self._values.get('allow')

        @builtins.property
        def block(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.BlockActionProperty"]]]:
            """``CfnWebACL.DefaultActionProperty.Block``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-block
            """
            return self._values.get('block')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'DefaultActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ExcludedRuleProperty", jsii_struct_bases=[], name_mapping={'name': 'name'})
    class ExcludedRuleProperty():
        def __init__(self, *, name: typing.Optional[str]=None):
            """
            :param name: ``CfnWebACL.ExcludedRuleProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html
            """
            self._values = {
            }
            if name is not None: self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnWebACL.ExcludedRuleProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html#cfn-wafv2-webacl-excludedrule-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ExcludedRuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ExcludedRulesProperty", jsii_struct_bases=[], name_mapping={'excluded_rules': 'excludedRules'})
    class ExcludedRulesProperty():
        def __init__(self, *, excluded_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]]]=None):
            """
            :param excluded_rules: ``CfnWebACL.ExcludedRulesProperty.ExcludedRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrules.html
            """
            self._values = {
            }
            if excluded_rules is not None: self._values["excluded_rules"] = excluded_rules

        @builtins.property
        def excluded_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]]]:
            """``CfnWebACL.ExcludedRulesProperty.ExcludedRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrules.html#cfn-wafv2-webacl-excludedrules-excludedrules
            """
            return self._values.get('excluded_rules')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ExcludedRulesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.FieldToMatchProperty", jsii_struct_bases=[], name_mapping={'all_query_arguments': 'allQueryArguments', 'body': 'body', 'method': 'method', 'query_string': 'queryString', 'single_header': 'singleHeader', 'single_query_argument': 'singleQueryArgument', 'uri_path': 'uriPath'})
    class FieldToMatchProperty():
        def __init__(self, *, all_query_arguments: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AllQueryArgumentsProperty"]]]=None, body: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.BodyProperty"]]]=None, method: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.MethodProperty"]]]=None, query_string: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.QueryStringProperty"]]]=None, single_header: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SingleHeaderProperty"]]]=None, single_query_argument: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SingleQueryArgumentProperty"]]]=None, uri_path: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.UriPathProperty"]]]=None):
            """
            :param all_query_arguments: ``CfnWebACL.FieldToMatchProperty.AllQueryArguments``.
            :param body: ``CfnWebACL.FieldToMatchProperty.Body``.
            :param method: ``CfnWebACL.FieldToMatchProperty.Method``.
            :param query_string: ``CfnWebACL.FieldToMatchProperty.QueryString``.
            :param single_header: ``CfnWebACL.FieldToMatchProperty.SingleHeader``.
            :param single_query_argument: ``CfnWebACL.FieldToMatchProperty.SingleQueryArgument``.
            :param uri_path: ``CfnWebACL.FieldToMatchProperty.UriPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html
            """
            self._values = {
            }
            if all_query_arguments is not None: self._values["all_query_arguments"] = all_query_arguments
            if body is not None: self._values["body"] = body
            if method is not None: self._values["method"] = method
            if query_string is not None: self._values["query_string"] = query_string
            if single_header is not None: self._values["single_header"] = single_header
            if single_query_argument is not None: self._values["single_query_argument"] = single_query_argument
            if uri_path is not None: self._values["uri_path"] = uri_path

        @builtins.property
        def all_query_arguments(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AllQueryArgumentsProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.AllQueryArguments``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-allqueryarguments
            """
            return self._values.get('all_query_arguments')

        @builtins.property
        def body(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.BodyProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.Body``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-body
            """
            return self._values.get('body')

        @builtins.property
        def method(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.MethodProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.Method``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-method
            """
            return self._values.get('method')

        @builtins.property
        def query_string(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.QueryStringProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.QueryString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-querystring
            """
            return self._values.get('query_string')

        @builtins.property
        def single_header(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SingleHeaderProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.SingleHeader``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singleheader
            """
            return self._values.get('single_header')

        @builtins.property
        def single_query_argument(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SingleQueryArgumentProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.SingleQueryArgument``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singlequeryargument
            """
            return self._values.get('single_query_argument')

        @builtins.property
        def uri_path(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.UriPathProperty"]]]:
            """``CfnWebACL.FieldToMatchProperty.UriPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-uripath
            """
            return self._values.get('uri_path')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FieldToMatchProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.GeoMatchStatementProperty", jsii_struct_bases=[], name_mapping={'country_codes': 'countryCodes'})
    class GeoMatchStatementProperty():
        def __init__(self, *, country_codes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.CountryCodesProperty"]]]=None):
            """
            :param country_codes: ``CfnWebACL.GeoMatchStatementProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html
            """
            self._values = {
            }
            if country_codes is not None: self._values["country_codes"] = country_codes

        @builtins.property
        def country_codes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.CountryCodesProperty"]]]:
            """``CfnWebACL.GeoMatchStatementProperty.CountryCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-countrycodes
            """
            return self._values.get('country_codes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'GeoMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.interface(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.IPSetReferenceStatementProperty")
    class IPSetReferenceStatementProperty(jsii.compat.Protocol):
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html
        """
        @builtins.staticmethod
        def __jsii_proxy_class__():
            return _IPSetReferenceStatementPropertyProxy

        @builtins.property
        @jsii.member(jsii_name="arn")
        def arn(self) -> typing.Optional[str]:
            """``CfnWebACL.IPSetReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn
            """
            ...


    class _IPSetReferenceStatementPropertyProxy():
        """
        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html
        """
        __jsii_type__ = "@aws-cdk/aws-wafv2.CfnWebACL.IPSetReferenceStatementProperty"
        @builtins.property
        @jsii.member(jsii_name="arn")
        def arn(self) -> typing.Optional[str]:
            """``CfnWebACL.IPSetReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn
            """
            return jsii.get(self, "arn")


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ManagedRuleGroupStatementProperty", jsii_struct_bases=[], name_mapping={'excluded_rules': 'excludedRules', 'name': 'name', 'vendor_name': 'vendorName'})
    class ManagedRuleGroupStatementProperty():
        def __init__(self, *, excluded_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ExcludedRulesProperty"]]]=None, name: typing.Optional[str]=None, vendor_name: typing.Optional[str]=None):
            """
            :param excluded_rules: ``CfnWebACL.ManagedRuleGroupStatementProperty.ExcludedRules``.
            :param name: ``CfnWebACL.ManagedRuleGroupStatementProperty.Name``.
            :param vendor_name: ``CfnWebACL.ManagedRuleGroupStatementProperty.VendorName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html
            """
            self._values = {
            }
            if excluded_rules is not None: self._values["excluded_rules"] = excluded_rules
            if name is not None: self._values["name"] = name
            if vendor_name is not None: self._values["vendor_name"] = vendor_name

        @builtins.property
        def excluded_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ExcludedRulesProperty"]]]:
            """``CfnWebACL.ManagedRuleGroupStatementProperty.ExcludedRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules
            """
            return self._values.get('excluded_rules')

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnWebACL.ManagedRuleGroupStatementProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-name
            """
            return self._values.get('name')

        @builtins.property
        def vendor_name(self) -> typing.Optional[str]:
            """``CfnWebACL.ManagedRuleGroupStatementProperty.VendorName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-vendorname
            """
            return self._values.get('vendor_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ManagedRuleGroupStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.MethodProperty", jsii_struct_bases=[], name_mapping={})
    class MethodProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-method.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MethodProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.NoneActionProperty", jsii_struct_bases=[], name_mapping={})
    class NoneActionProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-noneaction.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NoneActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.NotStatementOneProperty", jsii_struct_bases=[], name_mapping={'statement': 'statement'})
    class NotStatementOneProperty():
        def __init__(self, *, statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwoProperty"]]]=None):
            """
            :param statement: ``CfnWebACL.NotStatementOneProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementone.html
            """
            self._values = {
            }
            if statement is not None: self._values["statement"] = statement

        @builtins.property
        def statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwoProperty"]]]:
            """``CfnWebACL.NotStatementOneProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementone.html#cfn-wafv2-webacl-notstatementone-statement
            """
            return self._values.get('statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NotStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.NotStatementTwoProperty", jsii_struct_bases=[], name_mapping={'statement': 'statement'})
    class NotStatementTwoProperty():
        def __init__(self, *, statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreeProperty"]]]=None):
            """
            :param statement: ``CfnWebACL.NotStatementTwoProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementtwo.html
            """
            self._values = {
            }
            if statement is not None: self._values["statement"] = statement

        @builtins.property
        def statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreeProperty"]]]:
            """``CfnWebACL.NotStatementTwoProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementtwo.html#cfn-wafv2-webacl-notstatementtwo-statement
            """
            return self._values.get('statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NotStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.OrStatementOneProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class OrStatementOneProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwosProperty"]]]=None):
            """
            :param statements: ``CfnWebACL.OrStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementone.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwosProperty"]]]:
            """``CfnWebACL.OrStatementOneProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementone.html#cfn-wafv2-webacl-orstatementone-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'OrStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.OrStatementTwoProperty", jsii_struct_bases=[], name_mapping={'statements': 'statements'})
    class OrStatementTwoProperty():
        def __init__(self, *, statements: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreesProperty"]]]=None):
            """
            :param statements: ``CfnWebACL.OrStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementtwo.html
            """
            self._values = {
            }
            if statements is not None: self._values["statements"] = statements

        @builtins.property
        def statements(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreesProperty"]]]:
            """``CfnWebACL.OrStatementTwoProperty.Statements``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementtwo.html#cfn-wafv2-webacl-orstatementtwo-statements
            """
            return self._values.get('statements')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'OrStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.OverrideActionProperty", jsii_struct_bases=[], name_mapping={'count': 'count', 'none': 'none'})
    class OverrideActionProperty():
        def __init__(self, *, count: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.CountActionProperty"]]]=None, none: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.NoneActionProperty"]]]=None):
            """
            :param count: ``CfnWebACL.OverrideActionProperty.Count``.
            :param none: ``CfnWebACL.OverrideActionProperty.None``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html
            """
            self._values = {
            }
            if count is not None: self._values["count"] = count
            if none is not None: self._values["none"] = none

        @builtins.property
        def count(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.CountActionProperty"]]]:
            """``CfnWebACL.OverrideActionProperty.Count``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-count
            """
            return self._values.get('count')

        @builtins.property
        def none(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.NoneActionProperty"]]]:
            """``CfnWebACL.OverrideActionProperty.None``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-none
            """
            return self._values.get('none')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'OverrideActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.QueryStringProperty", jsii_struct_bases=[], name_mapping={})
    class QueryStringProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-querystring.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'QueryStringProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RateBasedStatementOneProperty", jsii_struct_bases=[], name_mapping={'aggregate_key_type': 'aggregateKeyType', 'limit': 'limit', 'scope_down_statement': 'scopeDownStatement'})
    class RateBasedStatementOneProperty():
        def __init__(self, *, aggregate_key_type: typing.Optional[str]=None, limit: typing.Optional[jsii.Number]=None, scope_down_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwoProperty"]]]=None):
            """
            :param aggregate_key_type: ``CfnWebACL.RateBasedStatementOneProperty.AggregateKeyType``.
            :param limit: ``CfnWebACL.RateBasedStatementOneProperty.Limit``.
            :param scope_down_statement: ``CfnWebACL.RateBasedStatementOneProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementone.html
            """
            self._values = {
            }
            if aggregate_key_type is not None: self._values["aggregate_key_type"] = aggregate_key_type
            if limit is not None: self._values["limit"] = limit
            if scope_down_statement is not None: self._values["scope_down_statement"] = scope_down_statement

        @builtins.property
        def aggregate_key_type(self) -> typing.Optional[str]:
            """``CfnWebACL.RateBasedStatementOneProperty.AggregateKeyType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementone.html#cfn-wafv2-webacl-ratebasedstatementone-aggregatekeytype
            """
            return self._values.get('aggregate_key_type')

        @builtins.property
        def limit(self) -> typing.Optional[jsii.Number]:
            """``CfnWebACL.RateBasedStatementOneProperty.Limit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementone.html#cfn-wafv2-webacl-ratebasedstatementone-limit
            """
            return self._values.get('limit')

        @builtins.property
        def scope_down_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementTwoProperty"]]]:
            """``CfnWebACL.RateBasedStatementOneProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementone.html#cfn-wafv2-webacl-ratebasedstatementone-scopedownstatement
            """
            return self._values.get('scope_down_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RateBasedStatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RateBasedStatementTwoProperty", jsii_struct_bases=[], name_mapping={'aggregate_key_type': 'aggregateKeyType', 'limit': 'limit', 'scope_down_statement': 'scopeDownStatement'})
    class RateBasedStatementTwoProperty():
        def __init__(self, *, aggregate_key_type: typing.Optional[str]=None, limit: typing.Optional[jsii.Number]=None, scope_down_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreeProperty"]]]=None):
            """
            :param aggregate_key_type: ``CfnWebACL.RateBasedStatementTwoProperty.AggregateKeyType``.
            :param limit: ``CfnWebACL.RateBasedStatementTwoProperty.Limit``.
            :param scope_down_statement: ``CfnWebACL.RateBasedStatementTwoProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementtwo.html
            """
            self._values = {
            }
            if aggregate_key_type is not None: self._values["aggregate_key_type"] = aggregate_key_type
            if limit is not None: self._values["limit"] = limit
            if scope_down_statement is not None: self._values["scope_down_statement"] = scope_down_statement

        @builtins.property
        def aggregate_key_type(self) -> typing.Optional[str]:
            """``CfnWebACL.RateBasedStatementTwoProperty.AggregateKeyType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementtwo.html#cfn-wafv2-webacl-ratebasedstatementtwo-aggregatekeytype
            """
            return self._values.get('aggregate_key_type')

        @builtins.property
        def limit(self) -> typing.Optional[jsii.Number]:
            """``CfnWebACL.RateBasedStatementTwoProperty.Limit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementtwo.html#cfn-wafv2-webacl-ratebasedstatementtwo-limit
            """
            return self._values.get('limit')

        @builtins.property
        def scope_down_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementThreeProperty"]]]:
            """``CfnWebACL.RateBasedStatementTwoProperty.ScopeDownStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementtwo.html#cfn-wafv2-webacl-ratebasedstatementtwo-scopedownstatement
            """
            return self._values.get('scope_down_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RateBasedStatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RegexPatternSetReferenceStatementProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn', 'field_to_match': 'fieldToMatch', 'text_transformations': 'textTransformations'})
    class RegexPatternSetReferenceStatementProperty():
        def __init__(self, *, arn: typing.Optional[str]=None, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]=None):
            """
            :param arn: ``CfnWebACL.RegexPatternSetReferenceStatementProperty.Arn``.
            :param field_to_match: ``CfnWebACL.RegexPatternSetReferenceStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnWebACL.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html
            """
            self._values = {
            }
            if arn is not None: self._values["arn"] = arn
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def arn(self) -> typing.Optional[str]:
            """``CfnWebACL.RegexPatternSetReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-arn
            """
            return self._values.get('arn')

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]:
            """``CfnWebACL.RegexPatternSetReferenceStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]:
            """``CfnWebACL.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RegexPatternSetReferenceStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RuleActionProperty", jsii_struct_bases=[], name_mapping={'allow': 'allow', 'block': 'block', 'count': 'count'})
    class RuleActionProperty():
        def __init__(self, *, allow: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AllowActionProperty"]]]=None, block: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.BlockActionProperty"]]]=None, count: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.CountActionProperty"]]]=None):
            """
            :param allow: ``CfnWebACL.RuleActionProperty.Allow``.
            :param block: ``CfnWebACL.RuleActionProperty.Block``.
            :param count: ``CfnWebACL.RuleActionProperty.Count``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html
            """
            self._values = {
            }
            if allow is not None: self._values["allow"] = allow
            if block is not None: self._values["block"] = block
            if count is not None: self._values["count"] = count

        @builtins.property
        def allow(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AllowActionProperty"]]]:
            """``CfnWebACL.RuleActionProperty.Allow``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-allow
            """
            return self._values.get('allow')

        @builtins.property
        def block(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.BlockActionProperty"]]]:
            """``CfnWebACL.RuleActionProperty.Block``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-block
            """
            return self._values.get('block')

        @builtins.property
        def count(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.CountActionProperty"]]]:
            """``CfnWebACL.RuleActionProperty.Count``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-count
            """
            return self._values.get('count')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleActionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RuleGroupReferenceStatementProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn', 'excluded_rules': 'excludedRules'})
    class RuleGroupReferenceStatementProperty():
        def __init__(self, *, arn: typing.Optional[str]=None, excluded_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ExcludedRulesProperty"]]]=None):
            """
            :param arn: ``CfnWebACL.RuleGroupReferenceStatementProperty.Arn``.
            :param excluded_rules: ``CfnWebACL.RuleGroupReferenceStatementProperty.ExcludedRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html
            """
            self._values = {
            }
            if arn is not None: self._values["arn"] = arn
            if excluded_rules is not None: self._values["excluded_rules"] = excluded_rules

        @builtins.property
        def arn(self) -> typing.Optional[str]:
            """``CfnWebACL.RuleGroupReferenceStatementProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-arn
            """
            return self._values.get('arn')

        @builtins.property
        def excluded_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ExcludedRulesProperty"]]]:
            """``CfnWebACL.RuleGroupReferenceStatementProperty.ExcludedRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-excludedrules
            """
            return self._values.get('excluded_rules')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleGroupReferenceStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RuleProperty", jsii_struct_bases=[], name_mapping={'action': 'action', 'name': 'name', 'override_action': 'overrideAction', 'priority': 'priority', 'statement': 'statement', 'visibility_config': 'visibilityConfig'})
    class RuleProperty():
        def __init__(self, *, action: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleActionProperty"]]]=None, name: typing.Optional[str]=None, override_action: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.OverrideActionProperty"]]]=None, priority: typing.Optional[jsii.Number]=None, statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementOneProperty"]]]=None, visibility_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.VisibilityConfigProperty"]]]=None):
            """
            :param action: ``CfnWebACL.RuleProperty.Action``.
            :param name: ``CfnWebACL.RuleProperty.Name``.
            :param override_action: ``CfnWebACL.RuleProperty.OverrideAction``.
            :param priority: ``CfnWebACL.RuleProperty.Priority``.
            :param statement: ``CfnWebACL.RuleProperty.Statement``.
            :param visibility_config: ``CfnWebACL.RuleProperty.VisibilityConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html
            """
            self._values = {
            }
            if action is not None: self._values["action"] = action
            if name is not None: self._values["name"] = name
            if override_action is not None: self._values["override_action"] = override_action
            if priority is not None: self._values["priority"] = priority
            if statement is not None: self._values["statement"] = statement
            if visibility_config is not None: self._values["visibility_config"] = visibility_config

        @builtins.property
        def action(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleActionProperty"]]]:
            """``CfnWebACL.RuleProperty.Action``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-action
            """
            return self._values.get('action')

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnWebACL.RuleProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-name
            """
            return self._values.get('name')

        @builtins.property
        def override_action(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.OverrideActionProperty"]]]:
            """``CfnWebACL.RuleProperty.OverrideAction``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-overrideaction
            """
            return self._values.get('override_action')

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnWebACL.RuleProperty.Priority``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-priority
            """
            return self._values.get('priority')

        @builtins.property
        def statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.StatementOneProperty"]]]:
            """``CfnWebACL.RuleProperty.Statement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-statement
            """
            return self._values.get('statement')

        @builtins.property
        def visibility_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.VisibilityConfigProperty"]]]:
            """``CfnWebACL.RuleProperty.VisibilityConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-visibilityconfig
            """
            return self._values.get('visibility_config')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RulesProperty", jsii_struct_bases=[], name_mapping={'rules': 'rules'})
    class RulesProperty():
        def __init__(self, *, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleProperty"]]]]]=None):
            """
            :param rules: ``CfnWebACL.RulesProperty.Rules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rules.html
            """
            self._values = {
            }
            if rules is not None: self._values["rules"] = rules

        @builtins.property
        def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleProperty"]]]]]:
            """``CfnWebACL.RulesProperty.Rules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rules.html#cfn-wafv2-webacl-rules-rules
            """
            return self._values.get('rules')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RulesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.SingleHeaderProperty", jsii_struct_bases=[], name_mapping={'name': 'name'})
    class SingleHeaderProperty():
        def __init__(self, *, name: typing.Optional[str]=None):
            """
            :param name: ``CfnWebACL.SingleHeaderProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singleheader.html
            """
            self._values = {
            }
            if name is not None: self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnWebACL.SingleHeaderProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singleheader.html#cfn-wafv2-webacl-singleheader-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SingleHeaderProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.SingleQueryArgumentProperty", jsii_struct_bases=[], name_mapping={'name': 'name'})
    class SingleQueryArgumentProperty():
        def __init__(self, *, name: typing.Optional[str]=None):
            """
            :param name: ``CfnWebACL.SingleQueryArgumentProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singlequeryargument.html
            """
            self._values = {
            }
            if name is not None: self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[str]:
            """``CfnWebACL.SingleQueryArgumentProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singlequeryargument.html#cfn-wafv2-webacl-singlequeryargument-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SingleQueryArgumentProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.SizeConstraintStatementProperty", jsii_struct_bases=[], name_mapping={'comparison_operator': 'comparisonOperator', 'field_to_match': 'fieldToMatch', 'size': 'size', 'text_transformations': 'textTransformations'})
    class SizeConstraintStatementProperty():
        def __init__(self, *, comparison_operator: typing.Optional[str]=None, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]=None, size: typing.Optional[jsii.Number]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]=None):
            """
            :param comparison_operator: ``CfnWebACL.SizeConstraintStatementProperty.ComparisonOperator``.
            :param field_to_match: ``CfnWebACL.SizeConstraintStatementProperty.FieldToMatch``.
            :param size: ``CfnWebACL.SizeConstraintStatementProperty.Size``.
            :param text_transformations: ``CfnWebACL.SizeConstraintStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html
            """
            self._values = {
            }
            if comparison_operator is not None: self._values["comparison_operator"] = comparison_operator
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if size is not None: self._values["size"] = size
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def comparison_operator(self) -> typing.Optional[str]:
            """``CfnWebACL.SizeConstraintStatementProperty.ComparisonOperator``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator
            """
            return self._values.get('comparison_operator')

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]:
            """``CfnWebACL.SizeConstraintStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            """``CfnWebACL.SizeConstraintStatementProperty.Size``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-size
            """
            return self._values.get('size')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]:
            """``CfnWebACL.SizeConstraintStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SizeConstraintStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.SqliMatchStatementProperty", jsii_struct_bases=[], name_mapping={'field_to_match': 'fieldToMatch', 'text_transformations': 'textTransformations'})
    class SqliMatchStatementProperty():
        def __init__(self, *, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]=None):
            """
            :param field_to_match: ``CfnWebACL.SqliMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnWebACL.SqliMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html
            """
            self._values = {
            }
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]:
            """``CfnWebACL.SqliMatchStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]:
            """``CfnWebACL.SqliMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SqliMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.StatementOneProperty", jsii_struct_bases=[], name_mapping={'and_statement': 'andStatement', 'byte_match_statement': 'byteMatchStatement', 'geo_match_statement': 'geoMatchStatement', 'ip_set_reference_statement': 'ipSetReferenceStatement', 'managed_rule_group_statement': 'managedRuleGroupStatement', 'not_statement': 'notStatement', 'or_statement': 'orStatement', 'rate_based_statement': 'rateBasedStatement', 'regex_pattern_set_reference_statement': 'regexPatternSetReferenceStatement', 'rule_group_reference_statement': 'ruleGroupReferenceStatement', 'size_constraint_statement': 'sizeConstraintStatement', 'sqli_match_statement': 'sqliMatchStatement', 'xss_match_statement': 'xssMatchStatement'})
    class StatementOneProperty():
        def __init__(self, *, and_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AndStatementOneProperty"]]]=None, byte_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ByteMatchStatementProperty"]]]=None, geo_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.GeoMatchStatementProperty"]]]=None, ip_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.IPSetReferenceStatementProperty"]]]=None, managed_rule_group_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ManagedRuleGroupStatementProperty"]]]=None, not_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.NotStatementOneProperty"]]]=None, or_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.OrStatementOneProperty"]]]=None, rate_based_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RateBasedStatementOneProperty"]]]=None, regex_pattern_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RegexPatternSetReferenceStatementProperty"]]]=None, rule_group_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleGroupReferenceStatementProperty"]]]=None, size_constraint_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SizeConstraintStatementProperty"]]]=None, sqli_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SqliMatchStatementProperty"]]]=None, xss_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.XssMatchStatementProperty"]]]=None):
            """
            :param and_statement: ``CfnWebACL.StatementOneProperty.AndStatement``.
            :param byte_match_statement: ``CfnWebACL.StatementOneProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnWebACL.StatementOneProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnWebACL.StatementOneProperty.IPSetReferenceStatement``.
            :param managed_rule_group_statement: ``CfnWebACL.StatementOneProperty.ManagedRuleGroupStatement``.
            :param not_statement: ``CfnWebACL.StatementOneProperty.NotStatement``.
            :param or_statement: ``CfnWebACL.StatementOneProperty.OrStatement``.
            :param rate_based_statement: ``CfnWebACL.StatementOneProperty.RateBasedStatement``.
            :param regex_pattern_set_reference_statement: ``CfnWebACL.StatementOneProperty.RegexPatternSetReferenceStatement``.
            :param rule_group_reference_statement: ``CfnWebACL.StatementOneProperty.RuleGroupReferenceStatement``.
            :param size_constraint_statement: ``CfnWebACL.StatementOneProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnWebACL.StatementOneProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnWebACL.StatementOneProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html
            """
            self._values = {
            }
            if and_statement is not None: self._values["and_statement"] = and_statement
            if byte_match_statement is not None: self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None: self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None: self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if managed_rule_group_statement is not None: self._values["managed_rule_group_statement"] = managed_rule_group_statement
            if not_statement is not None: self._values["not_statement"] = not_statement
            if or_statement is not None: self._values["or_statement"] = or_statement
            if rate_based_statement is not None: self._values["rate_based_statement"] = rate_based_statement
            if regex_pattern_set_reference_statement is not None: self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if rule_group_reference_statement is not None: self._values["rule_group_reference_statement"] = rule_group_reference_statement
            if size_constraint_statement is not None: self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None: self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None: self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def and_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AndStatementOneProperty"]]]:
            """``CfnWebACL.StatementOneProperty.AndStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-andstatement
            """
            return self._values.get('and_statement')

        @builtins.property
        def byte_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ByteMatchStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.ByteMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-bytematchstatement
            """
            return self._values.get('byte_match_statement')

        @builtins.property
        def geo_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.GeoMatchStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.GeoMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-geomatchstatement
            """
            return self._values.get('geo_match_statement')

        @builtins.property
        def ip_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.IPSetReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.IPSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-ipsetreferencestatement
            """
            return self._values.get('ip_set_reference_statement')

        @builtins.property
        def managed_rule_group_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ManagedRuleGroupStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.ManagedRuleGroupStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-managedrulegroupstatement
            """
            return self._values.get('managed_rule_group_statement')

        @builtins.property
        def not_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.NotStatementOneProperty"]]]:
            """``CfnWebACL.StatementOneProperty.NotStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-notstatement
            """
            return self._values.get('not_statement')

        @builtins.property
        def or_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.OrStatementOneProperty"]]]:
            """``CfnWebACL.StatementOneProperty.OrStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-orstatement
            """
            return self._values.get('or_statement')

        @builtins.property
        def rate_based_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RateBasedStatementOneProperty"]]]:
            """``CfnWebACL.StatementOneProperty.RateBasedStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-ratebasedstatement
            """
            return self._values.get('rate_based_statement')

        @builtins.property
        def regex_pattern_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RegexPatternSetReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.RegexPatternSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-regexpatternsetreferencestatement
            """
            return self._values.get('regex_pattern_set_reference_statement')

        @builtins.property
        def rule_group_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleGroupReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.RuleGroupReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-rulegroupreferencestatement
            """
            return self._values.get('rule_group_reference_statement')

        @builtins.property
        def size_constraint_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SizeConstraintStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.SizeConstraintStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-sizeconstraintstatement
            """
            return self._values.get('size_constraint_statement')

        @builtins.property
        def sqli_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SqliMatchStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.SqliMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-sqlimatchstatement
            """
            return self._values.get('sqli_match_statement')

        @builtins.property
        def xss_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.XssMatchStatementProperty"]]]:
            """``CfnWebACL.StatementOneProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html#cfn-wafv2-webacl-statementone-xssmatchstatement
            """
            return self._values.get('xss_match_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementOneProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.StatementThreeProperty", jsii_struct_bases=[], name_mapping={'byte_match_statement': 'byteMatchStatement', 'geo_match_statement': 'geoMatchStatement', 'ip_set_reference_statement': 'ipSetReferenceStatement', 'managed_rule_group_statement': 'managedRuleGroupStatement', 'regex_pattern_set_reference_statement': 'regexPatternSetReferenceStatement', 'rule_group_reference_statement': 'ruleGroupReferenceStatement', 'size_constraint_statement': 'sizeConstraintStatement', 'sqli_match_statement': 'sqliMatchStatement', 'xss_match_statement': 'xssMatchStatement'})
    class StatementThreeProperty():
        def __init__(self, *, byte_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ByteMatchStatementProperty"]]]=None, geo_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.GeoMatchStatementProperty"]]]=None, ip_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.IPSetReferenceStatementProperty"]]]=None, managed_rule_group_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ManagedRuleGroupStatementProperty"]]]=None, regex_pattern_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RegexPatternSetReferenceStatementProperty"]]]=None, rule_group_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleGroupReferenceStatementProperty"]]]=None, size_constraint_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SizeConstraintStatementProperty"]]]=None, sqli_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SqliMatchStatementProperty"]]]=None, xss_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.XssMatchStatementProperty"]]]=None):
            """
            :param byte_match_statement: ``CfnWebACL.StatementThreeProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnWebACL.StatementThreeProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnWebACL.StatementThreeProperty.IPSetReferenceStatement``.
            :param managed_rule_group_statement: ``CfnWebACL.StatementThreeProperty.ManagedRuleGroupStatement``.
            :param regex_pattern_set_reference_statement: ``CfnWebACL.StatementThreeProperty.RegexPatternSetReferenceStatement``.
            :param rule_group_reference_statement: ``CfnWebACL.StatementThreeProperty.RuleGroupReferenceStatement``.
            :param size_constraint_statement: ``CfnWebACL.StatementThreeProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnWebACL.StatementThreeProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnWebACL.StatementThreeProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html
            """
            self._values = {
            }
            if byte_match_statement is not None: self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None: self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None: self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if managed_rule_group_statement is not None: self._values["managed_rule_group_statement"] = managed_rule_group_statement
            if regex_pattern_set_reference_statement is not None: self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if rule_group_reference_statement is not None: self._values["rule_group_reference_statement"] = rule_group_reference_statement
            if size_constraint_statement is not None: self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None: self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None: self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def byte_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ByteMatchStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.ByteMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-bytematchstatement
            """
            return self._values.get('byte_match_statement')

        @builtins.property
        def geo_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.GeoMatchStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.GeoMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-geomatchstatement
            """
            return self._values.get('geo_match_statement')

        @builtins.property
        def ip_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.IPSetReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.IPSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-ipsetreferencestatement
            """
            return self._values.get('ip_set_reference_statement')

        @builtins.property
        def managed_rule_group_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ManagedRuleGroupStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.ManagedRuleGroupStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-managedrulegroupstatement
            """
            return self._values.get('managed_rule_group_statement')

        @builtins.property
        def regex_pattern_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RegexPatternSetReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.RegexPatternSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-regexpatternsetreferencestatement
            """
            return self._values.get('regex_pattern_set_reference_statement')

        @builtins.property
        def rule_group_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleGroupReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.RuleGroupReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-rulegroupreferencestatement
            """
            return self._values.get('rule_group_reference_statement')

        @builtins.property
        def size_constraint_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SizeConstraintStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.SizeConstraintStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-sizeconstraintstatement
            """
            return self._values.get('size_constraint_statement')

        @builtins.property
        def sqli_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SqliMatchStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.SqliMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-sqlimatchstatement
            """
            return self._values.get('sqli_match_statement')

        @builtins.property
        def xss_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.XssMatchStatementProperty"]]]:
            """``CfnWebACL.StatementThreeProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html#cfn-wafv2-webacl-statementthree-xssmatchstatement
            """
            return self._values.get('xss_match_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementThreeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.StatementThreesProperty", jsii_struct_bases=[], name_mapping={'statement_threes': 'statementThrees'})
    class StatementThreesProperty():
        def __init__(self, *, statement_threes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementThreeProperty"]]]]]=None):
            """
            :param statement_threes: ``CfnWebACL.StatementThreesProperty.StatementThrees``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthrees.html
            """
            self._values = {
            }
            if statement_threes is not None: self._values["statement_threes"] = statement_threes

        @builtins.property
        def statement_threes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementThreeProperty"]]]]]:
            """``CfnWebACL.StatementThreesProperty.StatementThrees``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthrees.html#cfn-wafv2-webacl-statementthrees-statementthrees
            """
            return self._values.get('statement_threes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementThreesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.StatementTwoProperty", jsii_struct_bases=[], name_mapping={'and_statement': 'andStatement', 'byte_match_statement': 'byteMatchStatement', 'geo_match_statement': 'geoMatchStatement', 'ip_set_reference_statement': 'ipSetReferenceStatement', 'managed_rule_group_statement': 'managedRuleGroupStatement', 'not_statement': 'notStatement', 'or_statement': 'orStatement', 'rate_based_statement': 'rateBasedStatement', 'regex_pattern_set_reference_statement': 'regexPatternSetReferenceStatement', 'rule_group_reference_statement': 'ruleGroupReferenceStatement', 'size_constraint_statement': 'sizeConstraintStatement', 'sqli_match_statement': 'sqliMatchStatement', 'xss_match_statement': 'xssMatchStatement'})
    class StatementTwoProperty():
        def __init__(self, *, and_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AndStatementTwoProperty"]]]=None, byte_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ByteMatchStatementProperty"]]]=None, geo_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.GeoMatchStatementProperty"]]]=None, ip_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.IPSetReferenceStatementProperty"]]]=None, managed_rule_group_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ManagedRuleGroupStatementProperty"]]]=None, not_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.NotStatementTwoProperty"]]]=None, or_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.OrStatementTwoProperty"]]]=None, rate_based_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RateBasedStatementTwoProperty"]]]=None, regex_pattern_set_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RegexPatternSetReferenceStatementProperty"]]]=None, rule_group_reference_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleGroupReferenceStatementProperty"]]]=None, size_constraint_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SizeConstraintStatementProperty"]]]=None, sqli_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SqliMatchStatementProperty"]]]=None, xss_match_statement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.XssMatchStatementProperty"]]]=None):
            """
            :param and_statement: ``CfnWebACL.StatementTwoProperty.AndStatement``.
            :param byte_match_statement: ``CfnWebACL.StatementTwoProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnWebACL.StatementTwoProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnWebACL.StatementTwoProperty.IPSetReferenceStatement``.
            :param managed_rule_group_statement: ``CfnWebACL.StatementTwoProperty.ManagedRuleGroupStatement``.
            :param not_statement: ``CfnWebACL.StatementTwoProperty.NotStatement``.
            :param or_statement: ``CfnWebACL.StatementTwoProperty.OrStatement``.
            :param rate_based_statement: ``CfnWebACL.StatementTwoProperty.RateBasedStatement``.
            :param regex_pattern_set_reference_statement: ``CfnWebACL.StatementTwoProperty.RegexPatternSetReferenceStatement``.
            :param rule_group_reference_statement: ``CfnWebACL.StatementTwoProperty.RuleGroupReferenceStatement``.
            :param size_constraint_statement: ``CfnWebACL.StatementTwoProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnWebACL.StatementTwoProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnWebACL.StatementTwoProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html
            """
            self._values = {
            }
            if and_statement is not None: self._values["and_statement"] = and_statement
            if byte_match_statement is not None: self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None: self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None: self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if managed_rule_group_statement is not None: self._values["managed_rule_group_statement"] = managed_rule_group_statement
            if not_statement is not None: self._values["not_statement"] = not_statement
            if or_statement is not None: self._values["or_statement"] = or_statement
            if rate_based_statement is not None: self._values["rate_based_statement"] = rate_based_statement
            if regex_pattern_set_reference_statement is not None: self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if rule_group_reference_statement is not None: self._values["rule_group_reference_statement"] = rule_group_reference_statement
            if size_constraint_statement is not None: self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None: self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None: self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def and_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.AndStatementTwoProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.AndStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-andstatement
            """
            return self._values.get('and_statement')

        @builtins.property
        def byte_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ByteMatchStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.ByteMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-bytematchstatement
            """
            return self._values.get('byte_match_statement')

        @builtins.property
        def geo_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.GeoMatchStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.GeoMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-geomatchstatement
            """
            return self._values.get('geo_match_statement')

        @builtins.property
        def ip_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.IPSetReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.IPSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-ipsetreferencestatement
            """
            return self._values.get('ip_set_reference_statement')

        @builtins.property
        def managed_rule_group_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.ManagedRuleGroupStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.ManagedRuleGroupStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-managedrulegroupstatement
            """
            return self._values.get('managed_rule_group_statement')

        @builtins.property
        def not_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.NotStatementTwoProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.NotStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-notstatement
            """
            return self._values.get('not_statement')

        @builtins.property
        def or_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.OrStatementTwoProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.OrStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-orstatement
            """
            return self._values.get('or_statement')

        @builtins.property
        def rate_based_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RateBasedStatementTwoProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.RateBasedStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-ratebasedstatement
            """
            return self._values.get('rate_based_statement')

        @builtins.property
        def regex_pattern_set_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RegexPatternSetReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.RegexPatternSetReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-regexpatternsetreferencestatement
            """
            return self._values.get('regex_pattern_set_reference_statement')

        @builtins.property
        def rule_group_reference_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RuleGroupReferenceStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.RuleGroupReferenceStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-rulegroupreferencestatement
            """
            return self._values.get('rule_group_reference_statement')

        @builtins.property
        def size_constraint_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SizeConstraintStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.SizeConstraintStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-sizeconstraintstatement
            """
            return self._values.get('size_constraint_statement')

        @builtins.property
        def sqli_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.SqliMatchStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.SqliMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-sqlimatchstatement
            """
            return self._values.get('sqli_match_statement')

        @builtins.property
        def xss_match_statement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.XssMatchStatementProperty"]]]:
            """``CfnWebACL.StatementTwoProperty.XssMatchStatement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html#cfn-wafv2-webacl-statementtwo-xssmatchstatement
            """
            return self._values.get('xss_match_statement')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementTwoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.StatementTwosProperty", jsii_struct_bases=[], name_mapping={'statement_twos': 'statementTwos'})
    class StatementTwosProperty():
        def __init__(self, *, statement_twos: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementTwoProperty"]]]]]=None):
            """
            :param statement_twos: ``CfnWebACL.StatementTwosProperty.StatementTwos``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwos.html
            """
            self._values = {
            }
            if statement_twos is not None: self._values["statement_twos"] = statement_twos

        @builtins.property
        def statement_twos(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementTwoProperty"]]]]]:
            """``CfnWebACL.StatementTwosProperty.StatementTwos``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwos.html#cfn-wafv2-webacl-statementtwos-statementtwos
            """
            return self._values.get('statement_twos')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StatementTwosProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.TagListProperty", jsii_struct_bases=[], name_mapping={'tag_list': 'tagList'})
    class TagListProperty():
        def __init__(self, *, tag_list: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]=None):
            """
            :param tag_list: ``CfnWebACL.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-taglist.html
            """
            self._values = {
            }
            if tag_list is not None: self._values["tag_list"] = tag_list

        @builtins.property
        def tag_list(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]]:
            """``CfnWebACL.TagListProperty.TagList``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-taglist.html#cfn-wafv2-webacl-taglist-taglist
            """
            return self._values.get('tag_list')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagListProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.TextTransformationProperty", jsii_struct_bases=[], name_mapping={'priority': 'priority', 'type': 'type'})
    class TextTransformationProperty():
        def __init__(self, *, priority: typing.Optional[jsii.Number]=None, type: typing.Optional[str]=None):
            """
            :param priority: ``CfnWebACL.TextTransformationProperty.Priority``.
            :param type: ``CfnWebACL.TextTransformationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html
            """
            self._values = {
            }
            if priority is not None: self._values["priority"] = priority
            if type is not None: self._values["type"] = type

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnWebACL.TextTransformationProperty.Priority``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-priority
            """
            return self._values.get('priority')

        @builtins.property
        def type(self) -> typing.Optional[str]:
            """``CfnWebACL.TextTransformationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TextTransformationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.TextTransformationsProperty", jsii_struct_bases=[], name_mapping={'text_transformations': 'textTransformations'})
    class TextTransformationsProperty():
        def __init__(self, *, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]]]=None):
            """
            :param text_transformations: ``CfnWebACL.TextTransformationsProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformations.html
            """
            self._values = {
            }
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]]]:
            """``CfnWebACL.TextTransformationsProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformations.html#cfn-wafv2-webacl-texttransformations-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TextTransformationsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.UriPathProperty", jsii_struct_bases=[], name_mapping={})
    class UriPathProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-uripath.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'UriPathProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.VisibilityConfigProperty", jsii_struct_bases=[], name_mapping={'cloud_watch_metrics_enabled': 'cloudWatchMetricsEnabled', 'metric_name': 'metricName', 'sampled_requests_enabled': 'sampledRequestsEnabled'})
    class VisibilityConfigProperty():
        def __init__(self, *, cloud_watch_metrics_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, metric_name: typing.Optional[str]=None, sampled_requests_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param cloud_watch_metrics_enabled: ``CfnWebACL.VisibilityConfigProperty.CloudWatchMetricsEnabled``.
            :param metric_name: ``CfnWebACL.VisibilityConfigProperty.MetricName``.
            :param sampled_requests_enabled: ``CfnWebACL.VisibilityConfigProperty.SampledRequestsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html
            """
            self._values = {
            }
            if cloud_watch_metrics_enabled is not None: self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled
            if metric_name is not None: self._values["metric_name"] = metric_name
            if sampled_requests_enabled is not None: self._values["sampled_requests_enabled"] = sampled_requests_enabled

        @builtins.property
        def cloud_watch_metrics_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnWebACL.VisibilityConfigProperty.CloudWatchMetricsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-cloudwatchmetricsenabled
            """
            return self._values.get('cloud_watch_metrics_enabled')

        @builtins.property
        def metric_name(self) -> typing.Optional[str]:
            """``CfnWebACL.VisibilityConfigProperty.MetricName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-metricname
            """
            return self._values.get('metric_name')

        @builtins.property
        def sampled_requests_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnWebACL.VisibilityConfigProperty.SampledRequestsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-sampledrequestsenabled
            """
            return self._values.get('sampled_requests_enabled')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'VisibilityConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.XssMatchStatementProperty", jsii_struct_bases=[], name_mapping={'field_to_match': 'fieldToMatch', 'text_transformations': 'textTransformations'})
    class XssMatchStatementProperty():
        def __init__(self, *, field_to_match: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]=None, text_transformations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]=None):
            """
            :param field_to_match: ``CfnWebACL.XssMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnWebACL.XssMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html
            """
            self._values = {
            }
            if field_to_match is not None: self._values["field_to_match"] = field_to_match
            if text_transformations is not None: self._values["text_transformations"] = text_transformations

        @builtins.property
        def field_to_match(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.FieldToMatchProperty"]]]:
            """``CfnWebACL.XssMatchStatementProperty.FieldToMatch``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-fieldtomatch
            """
            return self._values.get('field_to_match')

        @builtins.property
        def text_transformations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.TextTransformationsProperty"]]]:
            """``CfnWebACL.XssMatchStatementProperty.TextTransformations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-texttransformations
            """
            return self._values.get('text_transformations')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'XssMatchStatementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.implements(aws_cdk.core.IInspectable)
class CfnWebACLAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-wafv2.CfnWebACLAssociation"):
    """A CloudFormation ``AWS::WAFv2::WebACLAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html
    cloudformationResource:
    :cloudformationResource:: AWS::WAFv2::WebACLAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, resource_arn: str, web_acl_arn: str) -> None:
        """Create a new ``AWS::WAFv2::WebACLAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_arn: ``AWS::WAFv2::WebACLAssociation.ResourceArn``.
        :param web_acl_arn: ``AWS::WAFv2::WebACLAssociation.WebACLArn``.
        """
        props = CfnWebACLAssociationProps(resource_arn=resource_arn, web_acl_arn=web_acl_arn)

        jsii.create(CfnWebACLAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> str:
        """``AWS::WAFv2::WebACLAssociation.ResourceArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn
        """
        return jsii.get(self, "resourceArn")

    @resource_arn.setter
    def resource_arn(self, value: str):
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="webAclArn")
    def web_acl_arn(self) -> str:
        """``AWS::WAFv2::WebACLAssociation.WebACLArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn
        """
        return jsii.get(self, "webAclArn")

    @web_acl_arn.setter
    def web_acl_arn(self, value: str):
        jsii.set(self, "webAclArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACLAssociationProps", jsii_struct_bases=[], name_mapping={'resource_arn': 'resourceArn', 'web_acl_arn': 'webAclArn'})
class CfnWebACLAssociationProps():
    def __init__(self, *, resource_arn: str, web_acl_arn: str):
        """Properties for defining a ``AWS::WAFv2::WebACLAssociation``.

        :param resource_arn: ``AWS::WAFv2::WebACLAssociation.ResourceArn``.
        :param web_acl_arn: ``AWS::WAFv2::WebACLAssociation.WebACLArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html
        """
        self._values = {
            'resource_arn': resource_arn,
            'web_acl_arn': web_acl_arn,
        }

    @builtins.property
    def resource_arn(self) -> str:
        """``AWS::WAFv2::WebACLAssociation.ResourceArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn
        """
        return self._values.get('resource_arn')

    @builtins.property
    def web_acl_arn(self) -> str:
        """``AWS::WAFv2::WebACLAssociation.WebACLArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn
        """
        return self._values.get('web_acl_arn')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnWebACLAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-wafv2.CfnWebACLProps", jsii_struct_bases=[], name_mapping={'default_action': 'defaultAction', 'scope': 'scope', 'visibility_config': 'visibilityConfig', 'description': 'description', 'name': 'name', 'rules': 'rules', 'tags': 'tags'})
class CfnWebACLProps():
    def __init__(self, *, default_action: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.DefaultActionProperty"], scope: str, visibility_config: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"], description: typing.Optional[str]=None, name: typing.Optional[str]=None, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RulesProperty"]]]=None, tags: typing.Optional["CfnWebACL.TagListProperty"]=None):
        """Properties for defining a ``AWS::WAFv2::WebACL``.

        :param default_action: ``AWS::WAFv2::WebACL.DefaultAction``.
        :param scope: ``AWS::WAFv2::WebACL.Scope``.
        :param visibility_config: ``AWS::WAFv2::WebACL.VisibilityConfig``.
        :param description: ``AWS::WAFv2::WebACL.Description``.
        :param name: ``AWS::WAFv2::WebACL.Name``.
        :param rules: ``AWS::WAFv2::WebACL.Rules``.
        :param tags: ``AWS::WAFv2::WebACL.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html
        """
        if isinstance(tags, dict): tags = CfnWebACL.TagListProperty(**tags)
        self._values = {
            'default_action': default_action,
            'scope': scope,
            'visibility_config': visibility_config,
        }
        if description is not None: self._values["description"] = description
        if name is not None: self._values["name"] = name
        if rules is not None: self._values["rules"] = rules
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def default_action(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.DefaultActionProperty"]:
        """``AWS::WAFv2::WebACL.DefaultAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction
        """
        return self._values.get('default_action')

    @builtins.property
    def scope(self) -> str:
        """``AWS::WAFv2::WebACL.Scope``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope
        """
        return self._values.get('scope')

    @builtins.property
    def visibility_config(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"]:
        """``AWS::WAFv2::WebACL.VisibilityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig
        """
        return self._values.get('visibility_config')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::WAFv2::WebACL.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description
        """
        return self._values.get('description')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::WAFv2::WebACL.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name
        """
        return self._values.get('name')

    @builtins.property
    def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnWebACL.RulesProperty"]]]:
        """``AWS::WAFv2::WebACL.Rules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules
        """
        return self._values.get('rules')

    @builtins.property
    def tags(self) -> typing.Optional["CfnWebACL.TagListProperty"]:
        """``AWS::WAFv2::WebACL.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnWebACLProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnIPSet", "CfnIPSetProps", "CfnRegexPatternSet", "CfnRegexPatternSetProps", "CfnRuleGroup", "CfnRuleGroupProps", "CfnWebACL", "CfnWebACLAssociation", "CfnWebACLAssociationProps", "CfnWebACLProps", "__jsii_assembly__"]

publication.publish()
