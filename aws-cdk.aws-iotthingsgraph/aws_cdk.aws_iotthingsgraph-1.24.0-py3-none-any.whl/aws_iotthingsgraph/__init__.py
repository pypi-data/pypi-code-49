"""
## AWS IoT Things Graph Construct Library

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
import aws_cdk.aws_iotthingsgraph as iotthingsgraph
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-iotthingsgraph", "1.24.0", __name__, "aws-iotthingsgraph@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFlowTemplate(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-iotthingsgraph.CfnFlowTemplate"):
    """A CloudFormation ``AWS::IoTThingsGraph::FlowTemplate``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
    cloudformationResource:
    :cloudformationResource:: AWS::IoTThingsGraph::FlowTemplate
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, definition: typing.Union["DefinitionDocumentProperty", aws_cdk.core.IResolvable], compatible_namespace_version: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::IoTThingsGraph::FlowTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param definition: ``AWS::IoTThingsGraph::FlowTemplate.Definition``.
        :param compatible_namespace_version: ``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.
        """
        props = CfnFlowTemplateProps(definition=definition, compatible_namespace_version=compatible_namespace_version)

        jsii.create(CfnFlowTemplate, self, [scope, id, props])

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
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Union["DefinitionDocumentProperty", aws_cdk.core.IResolvable]:
        """``AWS::IoTThingsGraph::FlowTemplate.Definition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition
        """
        return jsii.get(self, "definition")

    @definition.setter
    def definition(self, value: typing.Union["DefinitionDocumentProperty", aws_cdk.core.IResolvable]):
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="compatibleNamespaceVersion")
    def compatible_namespace_version(self) -> typing.Optional[jsii.Number]:
        """``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion
        """
        return jsii.get(self, "compatibleNamespaceVersion")

    @compatible_namespace_version.setter
    def compatible_namespace_version(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "compatibleNamespaceVersion", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-iotthingsgraph.CfnFlowTemplate.DefinitionDocumentProperty", jsii_struct_bases=[], name_mapping={'language': 'language', 'text': 'text'})
    class DefinitionDocumentProperty():
        def __init__(self, *, language: str, text: str):
            """
            :param language: ``CfnFlowTemplate.DefinitionDocumentProperty.Language``.
            :param text: ``CfnFlowTemplate.DefinitionDocumentProperty.Text``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html
            """
            self._values = {
                'language': language,
                'text': text,
            }

        @builtins.property
        def language(self) -> str:
            """``CfnFlowTemplate.DefinitionDocumentProperty.Language``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-language
            """
            return self._values.get('language')

        @builtins.property
        def text(self) -> str:
            """``CfnFlowTemplate.DefinitionDocumentProperty.Text``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-text
            """
            return self._values.get('text')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'DefinitionDocumentProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-iotthingsgraph.CfnFlowTemplateProps", jsii_struct_bases=[], name_mapping={'definition': 'definition', 'compatible_namespace_version': 'compatibleNamespaceVersion'})
class CfnFlowTemplateProps():
    def __init__(self, *, definition: typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", aws_cdk.core.IResolvable], compatible_namespace_version: typing.Optional[jsii.Number]=None):
        """Properties for defining a ``AWS::IoTThingsGraph::FlowTemplate``.

        :param definition: ``AWS::IoTThingsGraph::FlowTemplate.Definition``.
        :param compatible_namespace_version: ``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
        """
        self._values = {
            'definition': definition,
        }
        if compatible_namespace_version is not None: self._values["compatible_namespace_version"] = compatible_namespace_version

    @builtins.property
    def definition(self) -> typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", aws_cdk.core.IResolvable]:
        """``AWS::IoTThingsGraph::FlowTemplate.Definition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition
        """
        return self._values.get('definition')

    @builtins.property
    def compatible_namespace_version(self) -> typing.Optional[jsii.Number]:
        """``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion
        """
        return self._values.get('compatible_namespace_version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnFlowTemplateProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnFlowTemplate", "CfnFlowTemplateProps", "__jsii_assembly__"]

publication.publish()
