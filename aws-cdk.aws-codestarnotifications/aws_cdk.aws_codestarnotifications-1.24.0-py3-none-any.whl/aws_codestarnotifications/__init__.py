"""
## AWS::CodeStarNotifications Construct Library

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
import aws_cdk.aws_codestarnotifications as codestarnotifications
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-codestarnotifications", "1.24.0", __name__, "aws-codestarnotifications@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotificationRule(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codestarnotifications.CfnNotificationRule"):
    """A CloudFormation ``AWS::CodeStarNotifications::NotificationRule``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
    cloudformationResource:
    :cloudformationResource:: AWS::CodeStarNotifications::NotificationRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, detail_type: str, event_type_ids: typing.List[str], name: str, resource: str, targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["TargetProperty", aws_cdk.core.IResolvable]]], status: typing.Optional[str]=None, tags: typing.Any=None) -> None:
        """Create a new ``AWS::CodeStarNotifications::NotificationRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detail_type: ``AWS::CodeStarNotifications::NotificationRule.DetailType``.
        :param event_type_ids: ``AWS::CodeStarNotifications::NotificationRule.EventTypeIds``.
        :param name: ``AWS::CodeStarNotifications::NotificationRule.Name``.
        :param resource: ``AWS::CodeStarNotifications::NotificationRule.Resource``.
        :param targets: ``AWS::CodeStarNotifications::NotificationRule.Targets``.
        :param status: ``AWS::CodeStarNotifications::NotificationRule.Status``.
        :param tags: ``AWS::CodeStarNotifications::NotificationRule.Tags``.
        """
        props = CfnNotificationRuleProps(detail_type=detail_type, event_type_ids=event_type_ids, name=name, resource=resource, targets=targets, status=status, tags=tags)

        jsii.create(CfnNotificationRule, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::CodeStarNotifications::NotificationRule.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="detailType")
    def detail_type(self) -> str:
        """``AWS::CodeStarNotifications::NotificationRule.DetailType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
        """
        return jsii.get(self, "detailType")

    @detail_type.setter
    def detail_type(self, value: str):
        jsii.set(self, "detailType", value)

    @builtins.property
    @jsii.member(jsii_name="eventTypeIds")
    def event_type_ids(self) -> typing.List[str]:
        """``AWS::CodeStarNotifications::NotificationRule.EventTypeIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
        """
        return jsii.get(self, "eventTypeIds")

    @event_type_ids.setter
    def event_type_ids(self, value: typing.List[str]):
        jsii.set(self, "eventTypeIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::CodeStarNotifications::NotificationRule.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> str:
        """``AWS::CodeStarNotifications::NotificationRule.Resource``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
        """
        return jsii.get(self, "resource")

    @resource.setter
    def resource(self, value: str):
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["TargetProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::CodeStarNotifications::NotificationRule.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["TargetProperty", aws_cdk.core.IResolvable]]]):
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[str]:
        """``AWS::CodeStarNotifications::NotificationRule.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
        """
        return jsii.get(self, "status")

    @status.setter
    def status(self, value: typing.Optional[str]):
        jsii.set(self, "status", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-codestarnotifications.CfnNotificationRule.TargetProperty", jsii_struct_bases=[], name_mapping={'target_address': 'targetAddress', 'target_type': 'targetType'})
    class TargetProperty():
        def __init__(self, *, target_address: typing.Optional[str]=None, target_type: typing.Optional[str]=None):
            """
            :param target_address: ``CfnNotificationRule.TargetProperty.TargetAddress``.
            :param target_type: ``CfnNotificationRule.TargetProperty.TargetType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html
            """
            self._values = {
            }
            if target_address is not None: self._values["target_address"] = target_address
            if target_type is not None: self._values["target_type"] = target_type

        @builtins.property
        def target_address(self) -> typing.Optional[str]:
            """``CfnNotificationRule.TargetProperty.TargetAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targetaddress
            """
            return self._values.get('target_address')

        @builtins.property
        def target_type(self) -> typing.Optional[str]:
            """``CfnNotificationRule.TargetProperty.TargetType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targettype
            """
            return self._values.get('target_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-codestarnotifications.CfnNotificationRuleProps", jsii_struct_bases=[], name_mapping={'detail_type': 'detailType', 'event_type_ids': 'eventTypeIds', 'name': 'name', 'resource': 'resource', 'targets': 'targets', 'status': 'status', 'tags': 'tags'})
class CfnNotificationRuleProps():
    def __init__(self, *, detail_type: str, event_type_ids: typing.List[str], name: str, resource: str, targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnNotificationRule.TargetProperty", aws_cdk.core.IResolvable]]], status: typing.Optional[str]=None, tags: typing.Any=None):
        """Properties for defining a ``AWS::CodeStarNotifications::NotificationRule``.

        :param detail_type: ``AWS::CodeStarNotifications::NotificationRule.DetailType``.
        :param event_type_ids: ``AWS::CodeStarNotifications::NotificationRule.EventTypeIds``.
        :param name: ``AWS::CodeStarNotifications::NotificationRule.Name``.
        :param resource: ``AWS::CodeStarNotifications::NotificationRule.Resource``.
        :param targets: ``AWS::CodeStarNotifications::NotificationRule.Targets``.
        :param status: ``AWS::CodeStarNotifications::NotificationRule.Status``.
        :param tags: ``AWS::CodeStarNotifications::NotificationRule.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
        """
        self._values = {
            'detail_type': detail_type,
            'event_type_ids': event_type_ids,
            'name': name,
            'resource': resource,
            'targets': targets,
        }
        if status is not None: self._values["status"] = status
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def detail_type(self) -> str:
        """``AWS::CodeStarNotifications::NotificationRule.DetailType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
        """
        return self._values.get('detail_type')

    @builtins.property
    def event_type_ids(self) -> typing.List[str]:
        """``AWS::CodeStarNotifications::NotificationRule.EventTypeIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
        """
        return self._values.get('event_type_ids')

    @builtins.property
    def name(self) -> str:
        """``AWS::CodeStarNotifications::NotificationRule.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
        """
        return self._values.get('name')

    @builtins.property
    def resource(self) -> str:
        """``AWS::CodeStarNotifications::NotificationRule.Resource``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
        """
        return self._values.get('resource')

    @builtins.property
    def targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnNotificationRule.TargetProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::CodeStarNotifications::NotificationRule.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
        """
        return self._values.get('targets')

    @builtins.property
    def status(self) -> typing.Optional[str]:
        """``AWS::CodeStarNotifications::NotificationRule.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
        """
        return self._values.get('status')

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::CodeStarNotifications::NotificationRule.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNotificationRuleProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnNotificationRule", "CfnNotificationRuleProps", "__jsii_assembly__"]

publication.publish()
