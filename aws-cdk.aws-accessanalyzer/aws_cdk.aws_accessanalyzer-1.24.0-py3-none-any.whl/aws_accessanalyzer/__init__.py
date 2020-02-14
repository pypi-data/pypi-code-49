"""
## AWS::AccessAnalyzer Construct Library

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
import aws_cdk.aws_accessanalyzer as accessanalyzer
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-accessanalyzer", "1.24.0", __name__, "aws-accessanalyzer@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAnalyzer(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzer"):
    """A CloudFormation ``AWS::AccessAnalyzer::Analyzer``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
    cloudformationResource:
    :cloudformationResource:: AWS::AccessAnalyzer::Analyzer
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, type: str, analyzer_name: typing.Optional[str]=None, archive_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["ArchiveRuleProperty", aws_cdk.core.IResolvable]]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::AccessAnalyzer::Analyzer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type: ``AWS::AccessAnalyzer::Analyzer.Type``.
        :param analyzer_name: ``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.
        :param archive_rules: ``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.
        :param tags: ``AWS::AccessAnalyzer::Analyzer.Tags``.
        """
        props = CfnAnalyzerProps(type=type, analyzer_name=analyzer_name, archive_rules=archive_rules, tags=tags)

        jsii.create(CfnAnalyzer, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::AccessAnalyzer::Analyzer.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::AccessAnalyzer::Analyzer.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="analyzerName")
    def analyzer_name(self) -> typing.Optional[str]:
        """``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        """
        return jsii.get(self, "analyzerName")

    @analyzer_name.setter
    def analyzer_name(self, value: typing.Optional[str]):
        jsii.set(self, "analyzerName", value)

    @builtins.property
    @jsii.member(jsii_name="archiveRules")
    def archive_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["ArchiveRuleProperty", aws_cdk.core.IResolvable]]]]]:
        """``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        """
        return jsii.get(self, "archiveRules")

    @archive_rules.setter
    def archive_rules(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["ArchiveRuleProperty", aws_cdk.core.IResolvable]]]]]):
        jsii.set(self, "archiveRules", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzer.ArchiveRuleProperty", jsii_struct_bases=[], name_mapping={'filter': 'filter', 'rule_name': 'ruleName'})
    class ArchiveRuleProperty():
        def __init__(self, *, filter: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalyzer.FilterProperty"]]], rule_name: str):
            """
            :param filter: ``CfnAnalyzer.ArchiveRuleProperty.Filter``.
            :param rule_name: ``CfnAnalyzer.ArchiveRuleProperty.RuleName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html
            """
            self._values = {
                'filter': filter,
                'rule_name': rule_name,
            }

        @builtins.property
        def filter(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalyzer.FilterProperty"]]]:
            """``CfnAnalyzer.ArchiveRuleProperty.Filter``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-filter
            """
            return self._values.get('filter')

        @builtins.property
        def rule_name(self) -> str:
            """``CfnAnalyzer.ArchiveRuleProperty.RuleName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-rulename
            """
            return self._values.get('rule_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ArchiveRuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzer.FilterProperty", jsii_struct_bases=[], name_mapping={'property': 'property', 'contains': 'contains', 'eq': 'eq', 'exists': 'exists', 'neq': 'neq'})
    class FilterProperty():
        def __init__(self, *, property: str, contains: typing.Optional[typing.List[str]]=None, eq: typing.Optional[typing.List[str]]=None, exists: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, neq: typing.Optional[typing.List[str]]=None):
            """
            :param property: ``CfnAnalyzer.FilterProperty.Property``.
            :param contains: ``CfnAnalyzer.FilterProperty.Contains``.
            :param eq: ``CfnAnalyzer.FilterProperty.Eq``.
            :param exists: ``CfnAnalyzer.FilterProperty.Exists``.
            :param neq: ``CfnAnalyzer.FilterProperty.Neq``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html
            """
            self._values = {
                'property': property,
            }
            if contains is not None: self._values["contains"] = contains
            if eq is not None: self._values["eq"] = eq
            if exists is not None: self._values["exists"] = exists
            if neq is not None: self._values["neq"] = neq

        @builtins.property
        def property(self) -> str:
            """``CfnAnalyzer.FilterProperty.Property``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-property
            """
            return self._values.get('property')

        @builtins.property
        def contains(self) -> typing.Optional[typing.List[str]]:
            """``CfnAnalyzer.FilterProperty.Contains``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-contains
            """
            return self._values.get('contains')

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[str]]:
            """``CfnAnalyzer.FilterProperty.Eq``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-eq
            """
            return self._values.get('eq')

        @builtins.property
        def exists(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnAnalyzer.FilterProperty.Exists``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-exists
            """
            return self._values.get('exists')

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[str]]:
            """``CfnAnalyzer.FilterProperty.Neq``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-neq
            """
            return self._values.get('neq')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FilterProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzerProps", jsii_struct_bases=[], name_mapping={'type': 'type', 'analyzer_name': 'analyzerName', 'archive_rules': 'archiveRules', 'tags': 'tags'})
class CfnAnalyzerProps():
    def __init__(self, *, type: str, analyzer_name: typing.Optional[str]=None, archive_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["CfnAnalyzer.ArchiveRuleProperty", aws_cdk.core.IResolvable]]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::AccessAnalyzer::Analyzer``.

        :param type: ``AWS::AccessAnalyzer::Analyzer.Type``.
        :param analyzer_name: ``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.
        :param archive_rules: ``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.
        :param tags: ``AWS::AccessAnalyzer::Analyzer.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
        """
        self._values = {
            'type': type,
        }
        if analyzer_name is not None: self._values["analyzer_name"] = analyzer_name
        if archive_rules is not None: self._values["archive_rules"] = archive_rules
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def type(self) -> str:
        """``AWS::AccessAnalyzer::Analyzer.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        """
        return self._values.get('type')

    @builtins.property
    def analyzer_name(self) -> typing.Optional[str]:
        """``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        """
        return self._values.get('analyzer_name')

    @builtins.property
    def archive_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["CfnAnalyzer.ArchiveRuleProperty", aws_cdk.core.IResolvable]]]]]:
        """``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        """
        return self._values.get('archive_rules')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::AccessAnalyzer::Analyzer.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnAnalyzerProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnAnalyzer", "CfnAnalyzerProps", "__jsii_assembly__"]

publication.publish()
