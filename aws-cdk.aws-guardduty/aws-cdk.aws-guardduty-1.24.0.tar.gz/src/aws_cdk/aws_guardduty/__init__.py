"""
## Amazon GuardDuty Construct Library

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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-guardduty", "1.24.0", __name__, "aws-guardduty@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDetector(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnDetector"):
    """A CloudFormation ``AWS::GuardDuty::Detector``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    cloudformationResource:
    :cloudformationResource:: AWS::GuardDuty::Detector
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, enable: typing.Union[bool, aws_cdk.core.IResolvable], finding_publishing_frequency: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Detector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param enable: ``AWS::GuardDuty::Detector.Enable``.
        :param finding_publishing_frequency: ``AWS::GuardDuty::Detector.FindingPublishingFrequency``.
        """
        props = CfnDetectorProps(enable=enable, finding_publishing_frequency=finding_publishing_frequency)

        jsii.create(CfnDetector, self, [scope, id, props])

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
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::Detector.Enable``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        """
        return jsii.get(self, "enable")

    @enable.setter
    def enable(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        """
        return jsii.get(self, "findingPublishingFrequency")

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(self, value: typing.Optional[str]):
        jsii.set(self, "findingPublishingFrequency", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnDetectorProps", jsii_struct_bases=[], name_mapping={'enable': 'enable', 'finding_publishing_frequency': 'findingPublishingFrequency'})
class CfnDetectorProps():
    def __init__(self, *, enable: typing.Union[bool, aws_cdk.core.IResolvable], finding_publishing_frequency: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GuardDuty::Detector``.

        :param enable: ``AWS::GuardDuty::Detector.Enable``.
        :param finding_publishing_frequency: ``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
        """
        self._values = {
            'enable': enable,
        }
        if finding_publishing_frequency is not None: self._values["finding_publishing_frequency"] = finding_publishing_frequency

    @builtins.property
    def enable(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::Detector.Enable``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        """
        return self._values.get('enable')

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        """
        return self._values.get('finding_publishing_frequency')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDetectorProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFilter(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnFilter"):
    """A CloudFormation ``AWS::GuardDuty::Filter``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    cloudformationResource:
    :cloudformationResource:: AWS::GuardDuty::Filter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, action: str, description: str, detector_id: str, finding_criteria: typing.Union[aws_cdk.core.IResolvable, "FindingCriteriaProperty"], name: str, rank: jsii.Number) -> None:
        """Create a new ``AWS::GuardDuty::Filter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::GuardDuty::Filter.Action``.
        :param description: ``AWS::GuardDuty::Filter.Description``.
        :param detector_id: ``AWS::GuardDuty::Filter.DetectorId``.
        :param finding_criteria: ``AWS::GuardDuty::Filter.FindingCriteria``.
        :param name: ``AWS::GuardDuty::Filter.Name``.
        :param rank: ``AWS::GuardDuty::Filter.Rank``.
        """
        props = CfnFilterProps(action=action, description=description, detector_id=detector_id, finding_criteria=finding_criteria, name=name, rank=rank)

        jsii.create(CfnFilter, self, [scope, id, props])

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
    @jsii.member(jsii_name="action")
    def action(self) -> str:
        """``AWS::GuardDuty::Filter.Action``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        """
        return jsii.get(self, "action")

    @action.setter
    def action(self, value: str):
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> str:
        """``AWS::GuardDuty::Filter.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: str):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Filter.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(self) -> typing.Union[aws_cdk.core.IResolvable, "FindingCriteriaProperty"]:
        """``AWS::GuardDuty::Filter.FindingCriteria``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        """
        return jsii.get(self, "findingCriteria")

    @finding_criteria.setter
    def finding_criteria(self, value: typing.Union[aws_cdk.core.IResolvable, "FindingCriteriaProperty"]):
        jsii.set(self, "findingCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::GuardDuty::Filter.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rank")
    def rank(self) -> jsii.Number:
        """``AWS::GuardDuty::Filter.Rank``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        """
        return jsii.get(self, "rank")

    @rank.setter
    def rank(self, value: jsii.Number):
        jsii.set(self, "rank", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnFilter.ConditionProperty", jsii_struct_bases=[], name_mapping={'eq': 'eq', 'gte': 'gte', 'lt': 'lt', 'lte': 'lte', 'neq': 'neq'})
    class ConditionProperty():
        def __init__(self, *, eq: typing.Optional[typing.List[str]]=None, gte: typing.Optional[jsii.Number]=None, lt: typing.Optional[jsii.Number]=None, lte: typing.Optional[jsii.Number]=None, neq: typing.Optional[typing.List[str]]=None):
            """
            :param eq: ``CfnFilter.ConditionProperty.Eq``.
            :param gte: ``CfnFilter.ConditionProperty.Gte``.
            :param lt: ``CfnFilter.ConditionProperty.Lt``.
            :param lte: ``CfnFilter.ConditionProperty.Lte``.
            :param neq: ``CfnFilter.ConditionProperty.Neq``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html
            """
            self._values = {
            }
            if eq is not None: self._values["eq"] = eq
            if gte is not None: self._values["gte"] = gte
            if lt is not None: self._values["lt"] = lt
            if lte is not None: self._values["lte"] = lte
            if neq is not None: self._values["neq"] = neq

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[str]]:
            """``CfnFilter.ConditionProperty.Eq``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-eq
            """
            return self._values.get('eq')

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            """``CfnFilter.ConditionProperty.Gte``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gte
            """
            return self._values.get('gte')

        @builtins.property
        def lt(self) -> typing.Optional[jsii.Number]:
            """``CfnFilter.ConditionProperty.Lt``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lt
            """
            return self._values.get('lt')

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            """``CfnFilter.ConditionProperty.Lte``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lte
            """
            return self._values.get('lte')

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[str]]:
            """``CfnFilter.ConditionProperty.Neq``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-neq
            """
            return self._values.get('neq')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ConditionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnFilter.FindingCriteriaProperty", jsii_struct_bases=[], name_mapping={'criterion': 'criterion', 'item_type': 'itemType'})
    class FindingCriteriaProperty():
        def __init__(self, *, criterion: typing.Any=None, item_type: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFilter.ConditionProperty"]]]=None):
            """
            :param criterion: ``CfnFilter.FindingCriteriaProperty.Criterion``.
            :param item_type: ``CfnFilter.FindingCriteriaProperty.ItemType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html
            """
            self._values = {
            }
            if criterion is not None: self._values["criterion"] = criterion
            if item_type is not None: self._values["item_type"] = item_type

        @builtins.property
        def criterion(self) -> typing.Any:
            """``CfnFilter.FindingCriteriaProperty.Criterion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-criterion
            """
            return self._values.get('criterion')

        @builtins.property
        def item_type(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFilter.ConditionProperty"]]]:
            """``CfnFilter.FindingCriteriaProperty.ItemType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-itemtype
            """
            return self._values.get('item_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FindingCriteriaProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnFilterProps", jsii_struct_bases=[], name_mapping={'action': 'action', 'description': 'description', 'detector_id': 'detectorId', 'finding_criteria': 'findingCriteria', 'name': 'name', 'rank': 'rank'})
class CfnFilterProps():
    def __init__(self, *, action: str, description: str, detector_id: str, finding_criteria: typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"], name: str, rank: jsii.Number):
        """Properties for defining a ``AWS::GuardDuty::Filter``.

        :param action: ``AWS::GuardDuty::Filter.Action``.
        :param description: ``AWS::GuardDuty::Filter.Description``.
        :param detector_id: ``AWS::GuardDuty::Filter.DetectorId``.
        :param finding_criteria: ``AWS::GuardDuty::Filter.FindingCriteria``.
        :param name: ``AWS::GuardDuty::Filter.Name``.
        :param rank: ``AWS::GuardDuty::Filter.Rank``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
        """
        self._values = {
            'action': action,
            'description': description,
            'detector_id': detector_id,
            'finding_criteria': finding_criteria,
            'name': name,
            'rank': rank,
        }

    @builtins.property
    def action(self) -> str:
        """``AWS::GuardDuty::Filter.Action``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        """
        return self._values.get('action')

    @builtins.property
    def description(self) -> str:
        """``AWS::GuardDuty::Filter.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        """
        return self._values.get('description')

    @builtins.property
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Filter.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        """
        return self._values.get('detector_id')

    @builtins.property
    def finding_criteria(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"]:
        """``AWS::GuardDuty::Filter.FindingCriteria``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        """
        return self._values.get('finding_criteria')

    @builtins.property
    def name(self) -> str:
        """``AWS::GuardDuty::Filter.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        """
        return self._values.get('name')

    @builtins.property
    def rank(self) -> jsii.Number:
        """``AWS::GuardDuty::Filter.Rank``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        """
        return self._values.get('rank')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnFilterProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIPSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnIPSet"):
    """A CloudFormation ``AWS::GuardDuty::IPSet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    cloudformationResource:
    :cloudformationResource:: AWS::GuardDuty::IPSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, activate: typing.Union[bool, aws_cdk.core.IResolvable], detector_id: str, format: str, location: str, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::IPSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activate: ``AWS::GuardDuty::IPSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::IPSet.DetectorId``.
        :param format: ``AWS::GuardDuty::IPSet.Format``.
        :param location: ``AWS::GuardDuty::IPSet.Location``.
        :param name: ``AWS::GuardDuty::IPSet.Name``.
        """
        props = CfnIPSetProps(activate=activate, detector_id=detector_id, format=format, location=location, name=name)

        jsii.create(CfnIPSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::IPSet.Activate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        """
        return jsii.get(self, "activate")

    @activate.setter
    def activate(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        jsii.set(self, "activate", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::IPSet.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> str:
        """``AWS::GuardDuty::IPSet.Format``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        """
        return jsii.get(self, "format")

    @format.setter
    def format(self, value: str):
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> str:
        """``AWS::GuardDuty::IPSet.Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        """
        return jsii.get(self, "location")

    @location.setter
    def location(self, value: str):
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::IPSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnIPSetProps", jsii_struct_bases=[], name_mapping={'activate': 'activate', 'detector_id': 'detectorId', 'format': 'format', 'location': 'location', 'name': 'name'})
class CfnIPSetProps():
    def __init__(self, *, activate: typing.Union[bool, aws_cdk.core.IResolvable], detector_id: str, format: str, location: str, name: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GuardDuty::IPSet``.

        :param activate: ``AWS::GuardDuty::IPSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::IPSet.DetectorId``.
        :param format: ``AWS::GuardDuty::IPSet.Format``.
        :param location: ``AWS::GuardDuty::IPSet.Location``.
        :param name: ``AWS::GuardDuty::IPSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
        """
        self._values = {
            'activate': activate,
            'detector_id': detector_id,
            'format': format,
            'location': location,
        }
        if name is not None: self._values["name"] = name

    @builtins.property
    def activate(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::IPSet.Activate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        """
        return self._values.get('activate')

    @builtins.property
    def detector_id(self) -> str:
        """``AWS::GuardDuty::IPSet.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        """
        return self._values.get('detector_id')

    @builtins.property
    def format(self) -> str:
        """``AWS::GuardDuty::IPSet.Format``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        """
        return self._values.get('format')

    @builtins.property
    def location(self) -> str:
        """``AWS::GuardDuty::IPSet.Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        """
        return self._values.get('location')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::IPSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        """
        return self._values.get('name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnIPSetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMaster(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnMaster"):
    """A CloudFormation ``AWS::GuardDuty::Master``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    cloudformationResource:
    :cloudformationResource:: AWS::GuardDuty::Master
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, detector_id: str, master_id: str, invitation_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Master``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: ``AWS::GuardDuty::Master.DetectorId``.
        :param master_id: ``AWS::GuardDuty::Master.MasterId``.
        :param invitation_id: ``AWS::GuardDuty::Master.InvitationId``.
        """
        props = CfnMasterProps(detector_id=detector_id, master_id=master_id, invitation_id=invitation_id)

        jsii.create(CfnMaster, self, [scope, id, props])

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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Master.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="masterId")
    def master_id(self) -> str:
        """``AWS::GuardDuty::Master.MasterId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        """
        return jsii.get(self, "masterId")

    @master_id.setter
    def master_id(self, value: str):
        jsii.set(self, "masterId", value)

    @builtins.property
    @jsii.member(jsii_name="invitationId")
    def invitation_id(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Master.InvitationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        """
        return jsii.get(self, "invitationId")

    @invitation_id.setter
    def invitation_id(self, value: typing.Optional[str]):
        jsii.set(self, "invitationId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnMasterProps", jsii_struct_bases=[], name_mapping={'detector_id': 'detectorId', 'master_id': 'masterId', 'invitation_id': 'invitationId'})
class CfnMasterProps():
    def __init__(self, *, detector_id: str, master_id: str, invitation_id: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GuardDuty::Master``.

        :param detector_id: ``AWS::GuardDuty::Master.DetectorId``.
        :param master_id: ``AWS::GuardDuty::Master.MasterId``.
        :param invitation_id: ``AWS::GuardDuty::Master.InvitationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
        """
        self._values = {
            'detector_id': detector_id,
            'master_id': master_id,
        }
        if invitation_id is not None: self._values["invitation_id"] = invitation_id

    @builtins.property
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Master.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        """
        return self._values.get('detector_id')

    @builtins.property
    def master_id(self) -> str:
        """``AWS::GuardDuty::Master.MasterId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        """
        return self._values.get('master_id')

    @builtins.property
    def invitation_id(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Master.InvitationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        """
        return self._values.get('invitation_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMasterProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMember(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnMember"):
    """A CloudFormation ``AWS::GuardDuty::Member``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    cloudformationResource:
    :cloudformationResource:: AWS::GuardDuty::Member
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, detector_id: str, email: str, member_id: str, disable_email_notification: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, message: typing.Optional[str]=None, status: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Member``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: ``AWS::GuardDuty::Member.DetectorId``.
        :param email: ``AWS::GuardDuty::Member.Email``.
        :param member_id: ``AWS::GuardDuty::Member.MemberId``.
        :param disable_email_notification: ``AWS::GuardDuty::Member.DisableEmailNotification``.
        :param message: ``AWS::GuardDuty::Member.Message``.
        :param status: ``AWS::GuardDuty::Member.Status``.
        """
        props = CfnMemberProps(detector_id=detector_id, email=email, member_id=member_id, disable_email_notification=disable_email_notification, message=message, status=status)

        jsii.create(CfnMember, self, [scope, id, props])

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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Member.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> str:
        """``AWS::GuardDuty::Member.Email``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        """
        return jsii.get(self, "email")

    @email.setter
    def email(self, value: str):
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> str:
        """``AWS::GuardDuty::Member.MemberId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        """
        return jsii.get(self, "memberId")

    @member_id.setter
    def member_id(self, value: str):
        jsii.set(self, "memberId", value)

    @builtins.property
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::GuardDuty::Member.DisableEmailNotification``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        """
        return jsii.get(self, "disableEmailNotification")

    @disable_email_notification.setter
    def disable_email_notification(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Member.Message``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        """
        return jsii.get(self, "message")

    @message.setter
    def message(self, value: typing.Optional[str]):
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Member.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        """
        return jsii.get(self, "status")

    @status.setter
    def status(self, value: typing.Optional[str]):
        jsii.set(self, "status", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnMemberProps", jsii_struct_bases=[], name_mapping={'detector_id': 'detectorId', 'email': 'email', 'member_id': 'memberId', 'disable_email_notification': 'disableEmailNotification', 'message': 'message', 'status': 'status'})
class CfnMemberProps():
    def __init__(self, *, detector_id: str, email: str, member_id: str, disable_email_notification: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, message: typing.Optional[str]=None, status: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GuardDuty::Member``.

        :param detector_id: ``AWS::GuardDuty::Member.DetectorId``.
        :param email: ``AWS::GuardDuty::Member.Email``.
        :param member_id: ``AWS::GuardDuty::Member.MemberId``.
        :param disable_email_notification: ``AWS::GuardDuty::Member.DisableEmailNotification``.
        :param message: ``AWS::GuardDuty::Member.Message``.
        :param status: ``AWS::GuardDuty::Member.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
        """
        self._values = {
            'detector_id': detector_id,
            'email': email,
            'member_id': member_id,
        }
        if disable_email_notification is not None: self._values["disable_email_notification"] = disable_email_notification
        if message is not None: self._values["message"] = message
        if status is not None: self._values["status"] = status

    @builtins.property
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Member.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        """
        return self._values.get('detector_id')

    @builtins.property
    def email(self) -> str:
        """``AWS::GuardDuty::Member.Email``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        """
        return self._values.get('email')

    @builtins.property
    def member_id(self) -> str:
        """``AWS::GuardDuty::Member.MemberId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        """
        return self._values.get('member_id')

    @builtins.property
    def disable_email_notification(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::GuardDuty::Member.DisableEmailNotification``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        """
        return self._values.get('disable_email_notification')

    @builtins.property
    def message(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Member.Message``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        """
        return self._values.get('message')

    @builtins.property
    def status(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Member.Status``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        """
        return self._values.get('status')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMemberProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnThreatIntelSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnThreatIntelSet"):
    """A CloudFormation ``AWS::GuardDuty::ThreatIntelSet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    cloudformationResource:
    :cloudformationResource:: AWS::GuardDuty::ThreatIntelSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, activate: typing.Union[bool, aws_cdk.core.IResolvable], detector_id: str, format: str, location: str, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::ThreatIntelSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activate: ``AWS::GuardDuty::ThreatIntelSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::ThreatIntelSet.DetectorId``.
        :param format: ``AWS::GuardDuty::ThreatIntelSet.Format``.
        :param location: ``AWS::GuardDuty::ThreatIntelSet.Location``.
        :param name: ``AWS::GuardDuty::ThreatIntelSet.Name``.
        """
        props = CfnThreatIntelSetProps(activate=activate, detector_id=detector_id, format=format, location=location, name=name)

        jsii.create(CfnThreatIntelSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::ThreatIntelSet.Activate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        """
        return jsii.get(self, "activate")

    @activate.setter
    def activate(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        jsii.set(self, "activate", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.Format``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        """
        return jsii.get(self, "format")

    @format.setter
    def format(self, value: str):
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        """
        return jsii.get(self, "location")

    @location.setter
    def location(self, value: str):
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::ThreatIntelSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnThreatIntelSetProps", jsii_struct_bases=[], name_mapping={'activate': 'activate', 'detector_id': 'detectorId', 'format': 'format', 'location': 'location', 'name': 'name'})
class CfnThreatIntelSetProps():
    def __init__(self, *, activate: typing.Union[bool, aws_cdk.core.IResolvable], detector_id: str, format: str, location: str, name: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GuardDuty::ThreatIntelSet``.

        :param activate: ``AWS::GuardDuty::ThreatIntelSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::ThreatIntelSet.DetectorId``.
        :param format: ``AWS::GuardDuty::ThreatIntelSet.Format``.
        :param location: ``AWS::GuardDuty::ThreatIntelSet.Location``.
        :param name: ``AWS::GuardDuty::ThreatIntelSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
        """
        self._values = {
            'activate': activate,
            'detector_id': detector_id,
            'format': format,
            'location': location,
        }
        if name is not None: self._values["name"] = name

    @builtins.property
    def activate(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::ThreatIntelSet.Activate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        """
        return self._values.get('activate')

    @builtins.property
    def detector_id(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.DetectorId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        """
        return self._values.get('detector_id')

    @builtins.property
    def format(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.Format``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        """
        return self._values.get('format')

    @builtins.property
    def location(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        """
        return self._values.get('location')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::ThreatIntelSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        """
        return self._values.get('name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnThreatIntelSetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnDetector", "CfnDetectorProps", "CfnFilter", "CfnFilterProps", "CfnIPSet", "CfnIPSetProps", "CfnMaster", "CfnMasterProps", "CfnMember", "CfnMemberProps", "CfnThreatIntelSet", "CfnThreatIntelSetProps", "__jsii_assembly__"]

publication.publish()
