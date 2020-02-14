"""
## AWS Elemental MediaStore Construct Library

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
import aws_cdk.aws_mediastore as mediastore
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-mediastore", "1.24.0", __name__, "aws-mediastore@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnContainer(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-mediastore.CfnContainer"):
    """A CloudFormation ``AWS::MediaStore::Container``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html
    cloudformationResource:
    :cloudformationResource:: AWS::MediaStore::Container
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, container_name: str, access_logging_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, cors_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CorsRuleProperty"]]]]]=None, lifecycle_policy: typing.Optional[str]=None, policy: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::MediaStore::Container``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param container_name: ``AWS::MediaStore::Container.ContainerName``.
        :param access_logging_enabled: ``AWS::MediaStore::Container.AccessLoggingEnabled``.
        :param cors_policy: ``AWS::MediaStore::Container.CorsPolicy``.
        :param lifecycle_policy: ``AWS::MediaStore::Container.LifecyclePolicy``.
        :param policy: ``AWS::MediaStore::Container.Policy``.
        """
        props = CfnContainerProps(container_name=container_name, access_logging_enabled=access_logging_enabled, cors_policy=cors_policy, lifecycle_policy=lifecycle_policy, policy=policy)

        jsii.create(CfnContainer, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Endpoint
        """
        return jsii.get(self, "attrEndpoint")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> str:
        """``AWS::MediaStore::Container.ContainerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-containername
        """
        return jsii.get(self, "containerName")

    @container_name.setter
    def container_name(self, value: str):
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="accessLoggingEnabled")
    def access_logging_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::MediaStore::Container.AccessLoggingEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-accessloggingenabled
        """
        return jsii.get(self, "accessLoggingEnabled")

    @access_logging_enabled.setter
    def access_logging_enabled(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "accessLoggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="corsPolicy")
    def cors_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CorsRuleProperty"]]]]]:
        """``AWS::MediaStore::Container.CorsPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-corspolicy
        """
        return jsii.get(self, "corsPolicy")

    @cors_policy.setter
    def cors_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CorsRuleProperty"]]]]]):
        jsii.set(self, "corsPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicy")
    def lifecycle_policy(self) -> typing.Optional[str]:
        """``AWS::MediaStore::Container.LifecyclePolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-lifecyclepolicy
        """
        return jsii.get(self, "lifecyclePolicy")

    @lifecycle_policy.setter
    def lifecycle_policy(self, value: typing.Optional[str]):
        jsii.set(self, "lifecyclePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Optional[str]:
        """``AWS::MediaStore::Container.Policy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-policy
        """
        return jsii.get(self, "policy")

    @policy.setter
    def policy(self, value: typing.Optional[str]):
        jsii.set(self, "policy", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-mediastore.CfnContainer.CorsRuleProperty", jsii_struct_bases=[], name_mapping={'allowed_headers': 'allowedHeaders', 'allowed_methods': 'allowedMethods', 'allowed_origins': 'allowedOrigins', 'expose_headers': 'exposeHeaders', 'max_age_seconds': 'maxAgeSeconds'})
    class CorsRuleProperty():
        def __init__(self, *, allowed_headers: typing.Optional[typing.List[str]]=None, allowed_methods: typing.Optional[typing.List[str]]=None, allowed_origins: typing.Optional[typing.List[str]]=None, expose_headers: typing.Optional[typing.List[str]]=None, max_age_seconds: typing.Optional[jsii.Number]=None):
            """
            :param allowed_headers: ``CfnContainer.CorsRuleProperty.AllowedHeaders``.
            :param allowed_methods: ``CfnContainer.CorsRuleProperty.AllowedMethods``.
            :param allowed_origins: ``CfnContainer.CorsRuleProperty.AllowedOrigins``.
            :param expose_headers: ``CfnContainer.CorsRuleProperty.ExposeHeaders``.
            :param max_age_seconds: ``CfnContainer.CorsRuleProperty.MaxAgeSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html
            """
            self._values = {
            }
            if allowed_headers is not None: self._values["allowed_headers"] = allowed_headers
            if allowed_methods is not None: self._values["allowed_methods"] = allowed_methods
            if allowed_origins is not None: self._values["allowed_origins"] = allowed_origins
            if expose_headers is not None: self._values["expose_headers"] = expose_headers
            if max_age_seconds is not None: self._values["max_age_seconds"] = max_age_seconds

        @builtins.property
        def allowed_headers(self) -> typing.Optional[typing.List[str]]:
            """``CfnContainer.CorsRuleProperty.AllowedHeaders``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedheaders
            """
            return self._values.get('allowed_headers')

        @builtins.property
        def allowed_methods(self) -> typing.Optional[typing.List[str]]:
            """``CfnContainer.CorsRuleProperty.AllowedMethods``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedmethods
            """
            return self._values.get('allowed_methods')

        @builtins.property
        def allowed_origins(self) -> typing.Optional[typing.List[str]]:
            """``CfnContainer.CorsRuleProperty.AllowedOrigins``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedorigins
            """
            return self._values.get('allowed_origins')

        @builtins.property
        def expose_headers(self) -> typing.Optional[typing.List[str]]:
            """``CfnContainer.CorsRuleProperty.ExposeHeaders``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-exposeheaders
            """
            return self._values.get('expose_headers')

        @builtins.property
        def max_age_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnContainer.CorsRuleProperty.MaxAgeSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-maxageseconds
            """
            return self._values.get('max_age_seconds')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CorsRuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-mediastore.CfnContainerProps", jsii_struct_bases=[], name_mapping={'container_name': 'containerName', 'access_logging_enabled': 'accessLoggingEnabled', 'cors_policy': 'corsPolicy', 'lifecycle_policy': 'lifecyclePolicy', 'policy': 'policy'})
class CfnContainerProps():
    def __init__(self, *, container_name: str, access_logging_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, cors_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContainer.CorsRuleProperty"]]]]]=None, lifecycle_policy: typing.Optional[str]=None, policy: typing.Optional[str]=None):
        """Properties for defining a ``AWS::MediaStore::Container``.

        :param container_name: ``AWS::MediaStore::Container.ContainerName``.
        :param access_logging_enabled: ``AWS::MediaStore::Container.AccessLoggingEnabled``.
        :param cors_policy: ``AWS::MediaStore::Container.CorsPolicy``.
        :param lifecycle_policy: ``AWS::MediaStore::Container.LifecyclePolicy``.
        :param policy: ``AWS::MediaStore::Container.Policy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html
        """
        self._values = {
            'container_name': container_name,
        }
        if access_logging_enabled is not None: self._values["access_logging_enabled"] = access_logging_enabled
        if cors_policy is not None: self._values["cors_policy"] = cors_policy
        if lifecycle_policy is not None: self._values["lifecycle_policy"] = lifecycle_policy
        if policy is not None: self._values["policy"] = policy

    @builtins.property
    def container_name(self) -> str:
        """``AWS::MediaStore::Container.ContainerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-containername
        """
        return self._values.get('container_name')

    @builtins.property
    def access_logging_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::MediaStore::Container.AccessLoggingEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-accessloggingenabled
        """
        return self._values.get('access_logging_enabled')

    @builtins.property
    def cors_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContainer.CorsRuleProperty"]]]]]:
        """``AWS::MediaStore::Container.CorsPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-corspolicy
        """
        return self._values.get('cors_policy')

    @builtins.property
    def lifecycle_policy(self) -> typing.Optional[str]:
        """``AWS::MediaStore::Container.LifecyclePolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-lifecyclepolicy
        """
        return self._values.get('lifecycle_policy')

    @builtins.property
    def policy(self) -> typing.Optional[str]:
        """``AWS::MediaStore::Container.Policy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-policy
        """
        return self._values.get('policy')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnContainerProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnContainer", "CfnContainerProps", "__jsii_assembly__"]

publication.publish()
