"""
## Amazon GameLift Construct Library

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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-gamelift", "1.24.0", __name__, "aws-gamelift@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAlias(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnAlias"):
    """A CloudFormation ``AWS::GameLift::Alias``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::Alias
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, routing_strategy: typing.Union[aws_cdk.core.IResolvable, "RoutingStrategyProperty"], description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GameLift::Alias``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::GameLift::Alias.Name``.
        :param routing_strategy: ``AWS::GameLift::Alias.RoutingStrategy``.
        :param description: ``AWS::GameLift::Alias.Description``.
        """
        props = CfnAliasProps(name=name, routing_strategy=routing_strategy, description=description)

        jsii.create(CfnAlias, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::GameLift::Alias.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="routingStrategy")
    def routing_strategy(self) -> typing.Union[aws_cdk.core.IResolvable, "RoutingStrategyProperty"]:
        """``AWS::GameLift::Alias.RoutingStrategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-routingstrategy
        """
        return jsii.get(self, "routingStrategy")

    @routing_strategy.setter
    def routing_strategy(self, value: typing.Union[aws_cdk.core.IResolvable, "RoutingStrategyProperty"]):
        jsii.set(self, "routingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::GameLift::Alias.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnAlias.RoutingStrategyProperty", jsii_struct_bases=[], name_mapping={'type': 'type', 'fleet_id': 'fleetId', 'message': 'message'})
    class RoutingStrategyProperty():
        def __init__(self, *, type: str, fleet_id: typing.Optional[str]=None, message: typing.Optional[str]=None):
            """
            :param type: ``CfnAlias.RoutingStrategyProperty.Type``.
            :param fleet_id: ``CfnAlias.RoutingStrategyProperty.FleetId``.
            :param message: ``CfnAlias.RoutingStrategyProperty.Message``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html
            """
            self._values = {
                'type': type,
            }
            if fleet_id is not None: self._values["fleet_id"] = fleet_id
            if message is not None: self._values["message"] = message

        @builtins.property
        def type(self) -> str:
            """``CfnAlias.RoutingStrategyProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-type
            """
            return self._values.get('type')

        @builtins.property
        def fleet_id(self) -> typing.Optional[str]:
            """``CfnAlias.RoutingStrategyProperty.FleetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-fleetid
            """
            return self._values.get('fleet_id')

        @builtins.property
        def message(self) -> typing.Optional[str]:
            """``CfnAlias.RoutingStrategyProperty.Message``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-message
            """
            return self._values.get('message')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RoutingStrategyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnAliasProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'routing_strategy': 'routingStrategy', 'description': 'description'})
class CfnAliasProps():
    def __init__(self, *, name: str, routing_strategy: typing.Union[aws_cdk.core.IResolvable, "CfnAlias.RoutingStrategyProperty"], description: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GameLift::Alias``.

        :param name: ``AWS::GameLift::Alias.Name``.
        :param routing_strategy: ``AWS::GameLift::Alias.RoutingStrategy``.
        :param description: ``AWS::GameLift::Alias.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
        """
        self._values = {
            'name': name,
            'routing_strategy': routing_strategy,
        }
        if description is not None: self._values["description"] = description

    @builtins.property
    def name(self) -> str:
        """``AWS::GameLift::Alias.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-name
        """
        return self._values.get('name')

    @builtins.property
    def routing_strategy(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnAlias.RoutingStrategyProperty"]:
        """``AWS::GameLift::Alias.RoutingStrategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-routingstrategy
        """
        return self._values.get('routing_strategy')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::GameLift::Alias.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-description
        """
        return self._values.get('description')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnAliasProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBuild(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnBuild"):
    """A CloudFormation ``AWS::GameLift::Build``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::Build
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: typing.Optional[str]=None, operating_system: typing.Optional[str]=None, storage_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["S3LocationProperty"]]]=None, version: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GameLift::Build``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::GameLift::Build.Name``.
        :param operating_system: ``AWS::GameLift::Build.OperatingSystem``.
        :param storage_location: ``AWS::GameLift::Build.StorageLocation``.
        :param version: ``AWS::GameLift::Build.Version``.
        """
        props = CfnBuildProps(name=name, operating_system=operating_system, storage_location=storage_location, version=version)

        jsii.create(CfnBuild, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GameLift::Build.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[str]:
        """``AWS::GameLift::Build.OperatingSystem``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-operatingsystem
        """
        return jsii.get(self, "operatingSystem")

    @operating_system.setter
    def operating_system(self, value: typing.Optional[str]):
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="storageLocation")
    def storage_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["S3LocationProperty"]]]:
        """``AWS::GameLift::Build.StorageLocation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-storagelocation
        """
        return jsii.get(self, "storageLocation")

    @storage_location.setter
    def storage_location(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["S3LocationProperty"]]]):
        jsii.set(self, "storageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[str]:
        """``AWS::GameLift::Build.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-version
        """
        return jsii.get(self, "version")

    @version.setter
    def version(self, value: typing.Optional[str]):
        jsii.set(self, "version", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnBuild.S3LocationProperty", jsii_struct_bases=[], name_mapping={'bucket': 'bucket', 'key': 'key', 'role_arn': 'roleArn', 'object_version': 'objectVersion'})
    class S3LocationProperty():
        def __init__(self, *, bucket: str, key: str, role_arn: str, object_version: typing.Optional[str]=None):
            """
            :param bucket: ``CfnBuild.S3LocationProperty.Bucket``.
            :param key: ``CfnBuild.S3LocationProperty.Key``.
            :param role_arn: ``CfnBuild.S3LocationProperty.RoleArn``.
            :param object_version: ``CfnBuild.S3LocationProperty.ObjectVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html
            """
            self._values = {
                'bucket': bucket,
                'key': key,
                'role_arn': role_arn,
            }
            if object_version is not None: self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> str:
            """``CfnBuild.S3LocationProperty.Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storage-bucket
            """
            return self._values.get('bucket')

        @builtins.property
        def key(self) -> str:
            """``CfnBuild.S3LocationProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storage-key
            """
            return self._values.get('key')

        @builtins.property
        def role_arn(self) -> str:
            """``CfnBuild.S3LocationProperty.RoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storage-rolearn
            """
            return self._values.get('role_arn')

        @builtins.property
        def object_version(self) -> typing.Optional[str]:
            """``CfnBuild.S3LocationProperty.ObjectVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-object-verison
            """
            return self._values.get('object_version')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'S3LocationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnBuildProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'operating_system': 'operatingSystem', 'storage_location': 'storageLocation', 'version': 'version'})
class CfnBuildProps():
    def __init__(self, *, name: typing.Optional[str]=None, operating_system: typing.Optional[str]=None, storage_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnBuild.S3LocationProperty"]]]=None, version: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GameLift::Build``.

        :param name: ``AWS::GameLift::Build.Name``.
        :param operating_system: ``AWS::GameLift::Build.OperatingSystem``.
        :param storage_location: ``AWS::GameLift::Build.StorageLocation``.
        :param version: ``AWS::GameLift::Build.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
        """
        self._values = {
        }
        if name is not None: self._values["name"] = name
        if operating_system is not None: self._values["operating_system"] = operating_system
        if storage_location is not None: self._values["storage_location"] = storage_location
        if version is not None: self._values["version"] = version

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::GameLift::Build.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-name
        """
        return self._values.get('name')

    @builtins.property
    def operating_system(self) -> typing.Optional[str]:
        """``AWS::GameLift::Build.OperatingSystem``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-operatingsystem
        """
        return self._values.get('operating_system')

    @builtins.property
    def storage_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnBuild.S3LocationProperty"]]]:
        """``AWS::GameLift::Build.StorageLocation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-storagelocation
        """
        return self._values.get('storage_location')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """``AWS::GameLift::Build.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-version
        """
        return self._values.get('version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnBuildProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFleet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnFleet"):
    """A CloudFormation ``AWS::GameLift::Fleet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::Fleet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, ec2_instance_type: str, name: str, build_id: typing.Optional[str]=None, certificate_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CertificateConfigurationProperty"]]]=None, description: typing.Optional[str]=None, desired_ec2_instances: typing.Optional[jsii.Number]=None, ec2_inbound_permissions: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "IpPermissionProperty"]]]]]=None, fleet_type: typing.Optional[str]=None, instance_role_arn: typing.Optional[str]=None, log_paths: typing.Optional[typing.List[str]]=None, max_size: typing.Optional[jsii.Number]=None, metric_groups: typing.Optional[typing.List[str]]=None, min_size: typing.Optional[jsii.Number]=None, new_game_session_protection_policy: typing.Optional[str]=None, peer_vpc_aws_account_id: typing.Optional[str]=None, peer_vpc_id: typing.Optional[str]=None, resource_creation_limit_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ResourceCreationLimitPolicyProperty"]]]=None, runtime_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RuntimeConfigurationProperty"]]]=None, script_id: typing.Optional[str]=None, server_launch_parameters: typing.Optional[str]=None, server_launch_path: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GameLift::Fleet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ec2_instance_type: ``AWS::GameLift::Fleet.EC2InstanceType``.
        :param name: ``AWS::GameLift::Fleet.Name``.
        :param build_id: ``AWS::GameLift::Fleet.BuildId``.
        :param certificate_configuration: ``AWS::GameLift::Fleet.CertificateConfiguration``.
        :param description: ``AWS::GameLift::Fleet.Description``.
        :param desired_ec2_instances: ``AWS::GameLift::Fleet.DesiredEC2Instances``.
        :param ec2_inbound_permissions: ``AWS::GameLift::Fleet.EC2InboundPermissions``.
        :param fleet_type: ``AWS::GameLift::Fleet.FleetType``.
        :param instance_role_arn: ``AWS::GameLift::Fleet.InstanceRoleARN``.
        :param log_paths: ``AWS::GameLift::Fleet.LogPaths``.
        :param max_size: ``AWS::GameLift::Fleet.MaxSize``.
        :param metric_groups: ``AWS::GameLift::Fleet.MetricGroups``.
        :param min_size: ``AWS::GameLift::Fleet.MinSize``.
        :param new_game_session_protection_policy: ``AWS::GameLift::Fleet.NewGameSessionProtectionPolicy``.
        :param peer_vpc_aws_account_id: ``AWS::GameLift::Fleet.PeerVpcAwsAccountId``.
        :param peer_vpc_id: ``AWS::GameLift::Fleet.PeerVpcId``.
        :param resource_creation_limit_policy: ``AWS::GameLift::Fleet.ResourceCreationLimitPolicy``.
        :param runtime_configuration: ``AWS::GameLift::Fleet.RuntimeConfiguration``.
        :param script_id: ``AWS::GameLift::Fleet.ScriptId``.
        :param server_launch_parameters: ``AWS::GameLift::Fleet.ServerLaunchParameters``.
        :param server_launch_path: ``AWS::GameLift::Fleet.ServerLaunchPath``.
        """
        props = CfnFleetProps(ec2_instance_type=ec2_instance_type, name=name, build_id=build_id, certificate_configuration=certificate_configuration, description=description, desired_ec2_instances=desired_ec2_instances, ec2_inbound_permissions=ec2_inbound_permissions, fleet_type=fleet_type, instance_role_arn=instance_role_arn, log_paths=log_paths, max_size=max_size, metric_groups=metric_groups, min_size=min_size, new_game_session_protection_policy=new_game_session_protection_policy, peer_vpc_aws_account_id=peer_vpc_aws_account_id, peer_vpc_id=peer_vpc_id, resource_creation_limit_policy=resource_creation_limit_policy, runtime_configuration=runtime_configuration, script_id=script_id, server_launch_parameters=server_launch_parameters, server_launch_path=server_launch_path)

        jsii.create(CfnFleet, self, [scope, id, props])

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
    @jsii.member(jsii_name="ec2InstanceType")
    def ec2_instance_type(self) -> str:
        """``AWS::GameLift::Fleet.EC2InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2instancetype
        """
        return jsii.get(self, "ec2InstanceType")

    @ec2_instance_type.setter
    def ec2_instance_type(self, value: str):
        jsii.set(self, "ec2InstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::GameLift::Fleet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.BuildId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-buildid
        """
        return jsii.get(self, "buildId")

    @build_id.setter
    def build_id(self, value: typing.Optional[str]):
        jsii.set(self, "buildId", value)

    @builtins.property
    @jsii.member(jsii_name="certificateConfiguration")
    def certificate_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CertificateConfigurationProperty"]]]:
        """``AWS::GameLift::Fleet.CertificateConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-certificateconfiguration
        """
        return jsii.get(self, "certificateConfiguration")

    @certificate_configuration.setter
    def certificate_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CertificateConfigurationProperty"]]]):
        jsii.set(self, "certificateConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredEc2Instances")
    def desired_ec2_instances(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::Fleet.DesiredEC2Instances``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-desiredec2instances
        """
        return jsii.get(self, "desiredEc2Instances")

    @desired_ec2_instances.setter
    def desired_ec2_instances(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "desiredEc2Instances", value)

    @builtins.property
    @jsii.member(jsii_name="ec2InboundPermissions")
    def ec2_inbound_permissions(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "IpPermissionProperty"]]]]]:
        """``AWS::GameLift::Fleet.EC2InboundPermissions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2inboundpermissions
        """
        return jsii.get(self, "ec2InboundPermissions")

    @ec2_inbound_permissions.setter
    def ec2_inbound_permissions(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "IpPermissionProperty"]]]]]):
        jsii.set(self, "ec2InboundPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="fleetType")
    def fleet_type(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.FleetType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-fleettype
        """
        return jsii.get(self, "fleetType")

    @fleet_type.setter
    def fleet_type(self, value: typing.Optional[str]):
        jsii.set(self, "fleetType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceRoleArn")
    def instance_role_arn(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.InstanceRoleARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolearn
        """
        return jsii.get(self, "instanceRoleArn")

    @instance_role_arn.setter
    def instance_role_arn(self, value: typing.Optional[str]):
        jsii.set(self, "instanceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="logPaths")
    def log_paths(self) -> typing.Optional[typing.List[str]]:
        """``AWS::GameLift::Fleet.LogPaths``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-logpaths
        """
        return jsii.get(self, "logPaths")

    @log_paths.setter
    def log_paths(self, value: typing.Optional[typing.List[str]]):
        jsii.set(self, "logPaths", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::Fleet.MaxSize``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-maxsize
        """
        return jsii.get(self, "maxSize")

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="metricGroups")
    def metric_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::GameLift::Fleet.MetricGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-metricgroups
        """
        return jsii.get(self, "metricGroups")

    @metric_groups.setter
    def metric_groups(self, value: typing.Optional[typing.List[str]]):
        jsii.set(self, "metricGroups", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::Fleet.MinSize``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-minsize
        """
        return jsii.get(self, "minSize")

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.NewGameSessionProtectionPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-newgamesessionprotectionpolicy
        """
        return jsii.get(self, "newGameSessionProtectionPolicy")

    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(self, value: typing.Optional[str]):
        jsii.set(self, "newGameSessionProtectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="peerVpcAwsAccountId")
    def peer_vpc_aws_account_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.PeerVpcAwsAccountId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcawsaccountid
        """
        return jsii.get(self, "peerVpcAwsAccountId")

    @peer_vpc_aws_account_id.setter
    def peer_vpc_aws_account_id(self, value: typing.Optional[str]):
        jsii.set(self, "peerVpcAwsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="peerVpcId")
    def peer_vpc_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.PeerVpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcid
        """
        return jsii.get(self, "peerVpcId")

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: typing.Optional[str]):
        jsii.set(self, "peerVpcId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ResourceCreationLimitPolicyProperty"]]]:
        """``AWS::GameLift::Fleet.ResourceCreationLimitPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-resourcecreationlimitpolicy
        """
        return jsii.get(self, "resourceCreationLimitPolicy")

    @resource_creation_limit_policy.setter
    def resource_creation_limit_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ResourceCreationLimitPolicyProperty"]]]):
        jsii.set(self, "resourceCreationLimitPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeConfiguration")
    def runtime_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RuntimeConfigurationProperty"]]]:
        """``AWS::GameLift::Fleet.RuntimeConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-runtimeconfiguration
        """
        return jsii.get(self, "runtimeConfiguration")

    @runtime_configuration.setter
    def runtime_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RuntimeConfigurationProperty"]]]):
        jsii.set(self, "runtimeConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.ScriptId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scriptid
        """
        return jsii.get(self, "scriptId")

    @script_id.setter
    def script_id(self, value: typing.Optional[str]):
        jsii.set(self, "scriptId", value)

    @builtins.property
    @jsii.member(jsii_name="serverLaunchParameters")
    def server_launch_parameters(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.ServerLaunchParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchparameters
        """
        return jsii.get(self, "serverLaunchParameters")

    @server_launch_parameters.setter
    def server_launch_parameters(self, value: typing.Optional[str]):
        jsii.set(self, "serverLaunchParameters", value)

    @builtins.property
    @jsii.member(jsii_name="serverLaunchPath")
    def server_launch_path(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.ServerLaunchPath``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchpath
        """
        return jsii.get(self, "serverLaunchPath")

    @server_launch_path.setter
    def server_launch_path(self, value: typing.Optional[str]):
        jsii.set(self, "serverLaunchPath", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnFleet.CertificateConfigurationProperty", jsii_struct_bases=[], name_mapping={'certificate_type': 'certificateType'})
    class CertificateConfigurationProperty():
        def __init__(self, *, certificate_type: str):
            """
            :param certificate_type: ``CfnFleet.CertificateConfigurationProperty.CertificateType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html
            """
            self._values = {
                'certificate_type': certificate_type,
            }

        @builtins.property
        def certificate_type(self) -> str:
            """``CfnFleet.CertificateConfigurationProperty.CertificateType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html#cfn-gamelift-fleet-certificateconfiguration-certificatetype
            """
            return self._values.get('certificate_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CertificateConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnFleet.IpPermissionProperty", jsii_struct_bases=[], name_mapping={'from_port': 'fromPort', 'ip_range': 'ipRange', 'protocol': 'protocol', 'to_port': 'toPort'})
    class IpPermissionProperty():
        def __init__(self, *, from_port: jsii.Number, ip_range: str, protocol: str, to_port: jsii.Number):
            """
            :param from_port: ``CfnFleet.IpPermissionProperty.FromPort``.
            :param ip_range: ``CfnFleet.IpPermissionProperty.IpRange``.
            :param protocol: ``CfnFleet.IpPermissionProperty.Protocol``.
            :param to_port: ``CfnFleet.IpPermissionProperty.ToPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ec2inboundpermission.html
            """
            self._values = {
                'from_port': from_port,
                'ip_range': ip_range,
                'protocol': protocol,
                'to_port': to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            """``CfnFleet.IpPermissionProperty.FromPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ec2inboundpermission.html#cfn-gamelift-fleet-ec2inboundpermissions-fromport
            """
            return self._values.get('from_port')

        @builtins.property
        def ip_range(self) -> str:
            """``CfnFleet.IpPermissionProperty.IpRange``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ec2inboundpermission.html#cfn-gamelift-fleet-ec2inboundpermissions-iprange
            """
            return self._values.get('ip_range')

        @builtins.property
        def protocol(self) -> str:
            """``CfnFleet.IpPermissionProperty.Protocol``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ec2inboundpermission.html#cfn-gamelift-fleet-ec2inboundpermissions-protocol
            """
            return self._values.get('protocol')

        @builtins.property
        def to_port(self) -> jsii.Number:
            """``CfnFleet.IpPermissionProperty.ToPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ec2inboundpermission.html#cfn-gamelift-fleet-ec2inboundpermissions-toport
            """
            return self._values.get('to_port')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'IpPermissionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnFleet.ResourceCreationLimitPolicyProperty", jsii_struct_bases=[], name_mapping={'new_game_sessions_per_creator': 'newGameSessionsPerCreator', 'policy_period_in_minutes': 'policyPeriodInMinutes'})
    class ResourceCreationLimitPolicyProperty():
        def __init__(self, *, new_game_sessions_per_creator: typing.Optional[jsii.Number]=None, policy_period_in_minutes: typing.Optional[jsii.Number]=None):
            """
            :param new_game_sessions_per_creator: ``CfnFleet.ResourceCreationLimitPolicyProperty.NewGameSessionsPerCreator``.
            :param policy_period_in_minutes: ``CfnFleet.ResourceCreationLimitPolicyProperty.PolicyPeriodInMinutes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html
            """
            self._values = {
            }
            if new_game_sessions_per_creator is not None: self._values["new_game_sessions_per_creator"] = new_game_sessions_per_creator
            if policy_period_in_minutes is not None: self._values["policy_period_in_minutes"] = policy_period_in_minutes

        @builtins.property
        def new_game_sessions_per_creator(self) -> typing.Optional[jsii.Number]:
            """``CfnFleet.ResourceCreationLimitPolicyProperty.NewGameSessionsPerCreator``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-newgamesessionspercreator
            """
            return self._values.get('new_game_sessions_per_creator')

        @builtins.property
        def policy_period_in_minutes(self) -> typing.Optional[jsii.Number]:
            """``CfnFleet.ResourceCreationLimitPolicyProperty.PolicyPeriodInMinutes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-policyperiodinminutes
            """
            return self._values.get('policy_period_in_minutes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ResourceCreationLimitPolicyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnFleet.RuntimeConfigurationProperty", jsii_struct_bases=[], name_mapping={'game_session_activation_timeout_seconds': 'gameSessionActivationTimeoutSeconds', 'max_concurrent_game_session_activations': 'maxConcurrentGameSessionActivations', 'server_processes': 'serverProcesses'})
    class RuntimeConfigurationProperty():
        def __init__(self, *, game_session_activation_timeout_seconds: typing.Optional[jsii.Number]=None, max_concurrent_game_session_activations: typing.Optional[jsii.Number]=None, server_processes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFleet.ServerProcessProperty"]]]]]=None):
            """
            :param game_session_activation_timeout_seconds: ``CfnFleet.RuntimeConfigurationProperty.GameSessionActivationTimeoutSeconds``.
            :param max_concurrent_game_session_activations: ``CfnFleet.RuntimeConfigurationProperty.MaxConcurrentGameSessionActivations``.
            :param server_processes: ``CfnFleet.RuntimeConfigurationProperty.ServerProcesses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html
            """
            self._values = {
            }
            if game_session_activation_timeout_seconds is not None: self._values["game_session_activation_timeout_seconds"] = game_session_activation_timeout_seconds
            if max_concurrent_game_session_activations is not None: self._values["max_concurrent_game_session_activations"] = max_concurrent_game_session_activations
            if server_processes is not None: self._values["server_processes"] = server_processes

        @builtins.property
        def game_session_activation_timeout_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnFleet.RuntimeConfigurationProperty.GameSessionActivationTimeoutSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-gamesessionactivationtimeoutseconds
            """
            return self._values.get('game_session_activation_timeout_seconds')

        @builtins.property
        def max_concurrent_game_session_activations(self) -> typing.Optional[jsii.Number]:
            """``CfnFleet.RuntimeConfigurationProperty.MaxConcurrentGameSessionActivations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-maxconcurrentgamesessionactivations
            """
            return self._values.get('max_concurrent_game_session_activations')

        @builtins.property
        def server_processes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFleet.ServerProcessProperty"]]]]]:
            """``CfnFleet.RuntimeConfigurationProperty.ServerProcesses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-serverprocesses
            """
            return self._values.get('server_processes')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuntimeConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnFleet.ServerProcessProperty", jsii_struct_bases=[], name_mapping={'concurrent_executions': 'concurrentExecutions', 'launch_path': 'launchPath', 'parameters': 'parameters'})
    class ServerProcessProperty():
        def __init__(self, *, concurrent_executions: jsii.Number, launch_path: str, parameters: typing.Optional[str]=None):
            """
            :param concurrent_executions: ``CfnFleet.ServerProcessProperty.ConcurrentExecutions``.
            :param launch_path: ``CfnFleet.ServerProcessProperty.LaunchPath``.
            :param parameters: ``CfnFleet.ServerProcessProperty.Parameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html
            """
            self._values = {
                'concurrent_executions': concurrent_executions,
                'launch_path': launch_path,
            }
            if parameters is not None: self._values["parameters"] = parameters

        @builtins.property
        def concurrent_executions(self) -> jsii.Number:
            """``CfnFleet.ServerProcessProperty.ConcurrentExecutions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-concurrentexecutions
            """
            return self._values.get('concurrent_executions')

        @builtins.property
        def launch_path(self) -> str:
            """``CfnFleet.ServerProcessProperty.LaunchPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-launchpath
            """
            return self._values.get('launch_path')

        @builtins.property
        def parameters(self) -> typing.Optional[str]:
            """``CfnFleet.ServerProcessProperty.Parameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-parameters
            """
            return self._values.get('parameters')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ServerProcessProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnFleetProps", jsii_struct_bases=[], name_mapping={'ec2_instance_type': 'ec2InstanceType', 'name': 'name', 'build_id': 'buildId', 'certificate_configuration': 'certificateConfiguration', 'description': 'description', 'desired_ec2_instances': 'desiredEc2Instances', 'ec2_inbound_permissions': 'ec2InboundPermissions', 'fleet_type': 'fleetType', 'instance_role_arn': 'instanceRoleArn', 'log_paths': 'logPaths', 'max_size': 'maxSize', 'metric_groups': 'metricGroups', 'min_size': 'minSize', 'new_game_session_protection_policy': 'newGameSessionProtectionPolicy', 'peer_vpc_aws_account_id': 'peerVpcAwsAccountId', 'peer_vpc_id': 'peerVpcId', 'resource_creation_limit_policy': 'resourceCreationLimitPolicy', 'runtime_configuration': 'runtimeConfiguration', 'script_id': 'scriptId', 'server_launch_parameters': 'serverLaunchParameters', 'server_launch_path': 'serverLaunchPath'})
class CfnFleetProps():
    def __init__(self, *, ec2_instance_type: str, name: str, build_id: typing.Optional[str]=None, certificate_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFleet.CertificateConfigurationProperty"]]]=None, description: typing.Optional[str]=None, desired_ec2_instances: typing.Optional[jsii.Number]=None, ec2_inbound_permissions: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFleet.IpPermissionProperty"]]]]]=None, fleet_type: typing.Optional[str]=None, instance_role_arn: typing.Optional[str]=None, log_paths: typing.Optional[typing.List[str]]=None, max_size: typing.Optional[jsii.Number]=None, metric_groups: typing.Optional[typing.List[str]]=None, min_size: typing.Optional[jsii.Number]=None, new_game_session_protection_policy: typing.Optional[str]=None, peer_vpc_aws_account_id: typing.Optional[str]=None, peer_vpc_id: typing.Optional[str]=None, resource_creation_limit_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFleet.ResourceCreationLimitPolicyProperty"]]]=None, runtime_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFleet.RuntimeConfigurationProperty"]]]=None, script_id: typing.Optional[str]=None, server_launch_parameters: typing.Optional[str]=None, server_launch_path: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GameLift::Fleet``.

        :param ec2_instance_type: ``AWS::GameLift::Fleet.EC2InstanceType``.
        :param name: ``AWS::GameLift::Fleet.Name``.
        :param build_id: ``AWS::GameLift::Fleet.BuildId``.
        :param certificate_configuration: ``AWS::GameLift::Fleet.CertificateConfiguration``.
        :param description: ``AWS::GameLift::Fleet.Description``.
        :param desired_ec2_instances: ``AWS::GameLift::Fleet.DesiredEC2Instances``.
        :param ec2_inbound_permissions: ``AWS::GameLift::Fleet.EC2InboundPermissions``.
        :param fleet_type: ``AWS::GameLift::Fleet.FleetType``.
        :param instance_role_arn: ``AWS::GameLift::Fleet.InstanceRoleARN``.
        :param log_paths: ``AWS::GameLift::Fleet.LogPaths``.
        :param max_size: ``AWS::GameLift::Fleet.MaxSize``.
        :param metric_groups: ``AWS::GameLift::Fleet.MetricGroups``.
        :param min_size: ``AWS::GameLift::Fleet.MinSize``.
        :param new_game_session_protection_policy: ``AWS::GameLift::Fleet.NewGameSessionProtectionPolicy``.
        :param peer_vpc_aws_account_id: ``AWS::GameLift::Fleet.PeerVpcAwsAccountId``.
        :param peer_vpc_id: ``AWS::GameLift::Fleet.PeerVpcId``.
        :param resource_creation_limit_policy: ``AWS::GameLift::Fleet.ResourceCreationLimitPolicy``.
        :param runtime_configuration: ``AWS::GameLift::Fleet.RuntimeConfiguration``.
        :param script_id: ``AWS::GameLift::Fleet.ScriptId``.
        :param server_launch_parameters: ``AWS::GameLift::Fleet.ServerLaunchParameters``.
        :param server_launch_path: ``AWS::GameLift::Fleet.ServerLaunchPath``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
        """
        self._values = {
            'ec2_instance_type': ec2_instance_type,
            'name': name,
        }
        if build_id is not None: self._values["build_id"] = build_id
        if certificate_configuration is not None: self._values["certificate_configuration"] = certificate_configuration
        if description is not None: self._values["description"] = description
        if desired_ec2_instances is not None: self._values["desired_ec2_instances"] = desired_ec2_instances
        if ec2_inbound_permissions is not None: self._values["ec2_inbound_permissions"] = ec2_inbound_permissions
        if fleet_type is not None: self._values["fleet_type"] = fleet_type
        if instance_role_arn is not None: self._values["instance_role_arn"] = instance_role_arn
        if log_paths is not None: self._values["log_paths"] = log_paths
        if max_size is not None: self._values["max_size"] = max_size
        if metric_groups is not None: self._values["metric_groups"] = metric_groups
        if min_size is not None: self._values["min_size"] = min_size
        if new_game_session_protection_policy is not None: self._values["new_game_session_protection_policy"] = new_game_session_protection_policy
        if peer_vpc_aws_account_id is not None: self._values["peer_vpc_aws_account_id"] = peer_vpc_aws_account_id
        if peer_vpc_id is not None: self._values["peer_vpc_id"] = peer_vpc_id
        if resource_creation_limit_policy is not None: self._values["resource_creation_limit_policy"] = resource_creation_limit_policy
        if runtime_configuration is not None: self._values["runtime_configuration"] = runtime_configuration
        if script_id is not None: self._values["script_id"] = script_id
        if server_launch_parameters is not None: self._values["server_launch_parameters"] = server_launch_parameters
        if server_launch_path is not None: self._values["server_launch_path"] = server_launch_path

    @builtins.property
    def ec2_instance_type(self) -> str:
        """``AWS::GameLift::Fleet.EC2InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2instancetype
        """
        return self._values.get('ec2_instance_type')

    @builtins.property
    def name(self) -> str:
        """``AWS::GameLift::Fleet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-name
        """
        return self._values.get('name')

    @builtins.property
    def build_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.BuildId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-buildid
        """
        return self._values.get('build_id')

    @builtins.property
    def certificate_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFleet.CertificateConfigurationProperty"]]]:
        """``AWS::GameLift::Fleet.CertificateConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-certificateconfiguration
        """
        return self._values.get('certificate_configuration')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-description
        """
        return self._values.get('description')

    @builtins.property
    def desired_ec2_instances(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::Fleet.DesiredEC2Instances``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-desiredec2instances
        """
        return self._values.get('desired_ec2_instances')

    @builtins.property
    def ec2_inbound_permissions(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFleet.IpPermissionProperty"]]]]]:
        """``AWS::GameLift::Fleet.EC2InboundPermissions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2inboundpermissions
        """
        return self._values.get('ec2_inbound_permissions')

    @builtins.property
    def fleet_type(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.FleetType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-fleettype
        """
        return self._values.get('fleet_type')

    @builtins.property
    def instance_role_arn(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.InstanceRoleARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolearn
        """
        return self._values.get('instance_role_arn')

    @builtins.property
    def log_paths(self) -> typing.Optional[typing.List[str]]:
        """``AWS::GameLift::Fleet.LogPaths``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-logpaths
        """
        return self._values.get('log_paths')

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::Fleet.MaxSize``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-maxsize
        """
        return self._values.get('max_size')

    @builtins.property
    def metric_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::GameLift::Fleet.MetricGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-metricgroups
        """
        return self._values.get('metric_groups')

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::Fleet.MinSize``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-minsize
        """
        return self._values.get('min_size')

    @builtins.property
    def new_game_session_protection_policy(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.NewGameSessionProtectionPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-newgamesessionprotectionpolicy
        """
        return self._values.get('new_game_session_protection_policy')

    @builtins.property
    def peer_vpc_aws_account_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.PeerVpcAwsAccountId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcawsaccountid
        """
        return self._values.get('peer_vpc_aws_account_id')

    @builtins.property
    def peer_vpc_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.PeerVpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcid
        """
        return self._values.get('peer_vpc_id')

    @builtins.property
    def resource_creation_limit_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFleet.ResourceCreationLimitPolicyProperty"]]]:
        """``AWS::GameLift::Fleet.ResourceCreationLimitPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-resourcecreationlimitpolicy
        """
        return self._values.get('resource_creation_limit_policy')

    @builtins.property
    def runtime_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnFleet.RuntimeConfigurationProperty"]]]:
        """``AWS::GameLift::Fleet.RuntimeConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-runtimeconfiguration
        """
        return self._values.get('runtime_configuration')

    @builtins.property
    def script_id(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.ScriptId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scriptid
        """
        return self._values.get('script_id')

    @builtins.property
    def server_launch_parameters(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.ServerLaunchParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchparameters
        """
        return self._values.get('server_launch_parameters')

    @builtins.property
    def server_launch_path(self) -> typing.Optional[str]:
        """``AWS::GameLift::Fleet.ServerLaunchPath``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchpath
        """
        return self._values.get('server_launch_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnFleetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnGameSessionQueue(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnGameSessionQueue"):
    """A CloudFormation ``AWS::GameLift::GameSessionQueue``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::GameSessionQueue
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, destinations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "DestinationProperty"]]]]]=None, player_latency_policies: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PlayerLatencyPolicyProperty"]]]]]=None, timeout_in_seconds: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::GameLift::GameSessionQueue``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::GameLift::GameSessionQueue.Name``.
        :param destinations: ``AWS::GameLift::GameSessionQueue.Destinations``.
        :param player_latency_policies: ``AWS::GameLift::GameSessionQueue.PlayerLatencyPolicies``.
        :param timeout_in_seconds: ``AWS::GameLift::GameSessionQueue.TimeoutInSeconds``.
        """
        props = CfnGameSessionQueueProps(name=name, destinations=destinations, player_latency_policies=player_latency_policies, timeout_in_seconds=timeout_in_seconds)

        jsii.create(CfnGameSessionQueue, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::GameLift::GameSessionQueue.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="destinations")
    def destinations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "DestinationProperty"]]]]]:
        """``AWS::GameLift::GameSessionQueue.Destinations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-destinations
        """
        return jsii.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "DestinationProperty"]]]]]):
        jsii.set(self, "destinations", value)

    @builtins.property
    @jsii.member(jsii_name="playerLatencyPolicies")
    def player_latency_policies(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PlayerLatencyPolicyProperty"]]]]]:
        """``AWS::GameLift::GameSessionQueue.PlayerLatencyPolicies``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-playerlatencypolicies
        """
        return jsii.get(self, "playerLatencyPolicies")

    @player_latency_policies.setter
    def player_latency_policies(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PlayerLatencyPolicyProperty"]]]]]):
        jsii.set(self, "playerLatencyPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::GameSessionQueue.TimeoutInSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-timeoutinseconds
        """
        return jsii.get(self, "timeoutInSeconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "timeoutInSeconds", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnGameSessionQueue.DestinationProperty", jsii_struct_bases=[], name_mapping={'destination_arn': 'destinationArn'})
    class DestinationProperty():
        def __init__(self, *, destination_arn: typing.Optional[str]=None):
            """
            :param destination_arn: ``CfnGameSessionQueue.DestinationProperty.DestinationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html
            """
            self._values = {
            }
            if destination_arn is not None: self._values["destination_arn"] = destination_arn

        @builtins.property
        def destination_arn(self) -> typing.Optional[str]:
            """``CfnGameSessionQueue.DestinationProperty.DestinationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html#cfn-gamelift-gamesessionqueue-destination-destinationarn
            """
            return self._values.get('destination_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'DestinationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty", jsii_struct_bases=[], name_mapping={'maximum_individual_player_latency_milliseconds': 'maximumIndividualPlayerLatencyMilliseconds', 'policy_duration_seconds': 'policyDurationSeconds'})
    class PlayerLatencyPolicyProperty():
        def __init__(self, *, maximum_individual_player_latency_milliseconds: typing.Optional[jsii.Number]=None, policy_duration_seconds: typing.Optional[jsii.Number]=None):
            """
            :param maximum_individual_player_latency_milliseconds: ``CfnGameSessionQueue.PlayerLatencyPolicyProperty.MaximumIndividualPlayerLatencyMilliseconds``.
            :param policy_duration_seconds: ``CfnGameSessionQueue.PlayerLatencyPolicyProperty.PolicyDurationSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html
            """
            self._values = {
            }
            if maximum_individual_player_latency_milliseconds is not None: self._values["maximum_individual_player_latency_milliseconds"] = maximum_individual_player_latency_milliseconds
            if policy_duration_seconds is not None: self._values["policy_duration_seconds"] = policy_duration_seconds

        @builtins.property
        def maximum_individual_player_latency_milliseconds(self) -> typing.Optional[jsii.Number]:
            """``CfnGameSessionQueue.PlayerLatencyPolicyProperty.MaximumIndividualPlayerLatencyMilliseconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-maximumindividualplayerlatencymilliseconds
            """
            return self._values.get('maximum_individual_player_latency_milliseconds')

        @builtins.property
        def policy_duration_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnGameSessionQueue.PlayerLatencyPolicyProperty.PolicyDurationSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-policydurationseconds
            """
            return self._values.get('policy_duration_seconds')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PlayerLatencyPolicyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnGameSessionQueueProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'destinations': 'destinations', 'player_latency_policies': 'playerLatencyPolicies', 'timeout_in_seconds': 'timeoutInSeconds'})
class CfnGameSessionQueueProps():
    def __init__(self, *, name: str, destinations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGameSessionQueue.DestinationProperty"]]]]]=None, player_latency_policies: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]]]=None, timeout_in_seconds: typing.Optional[jsii.Number]=None):
        """Properties for defining a ``AWS::GameLift::GameSessionQueue``.

        :param name: ``AWS::GameLift::GameSessionQueue.Name``.
        :param destinations: ``AWS::GameLift::GameSessionQueue.Destinations``.
        :param player_latency_policies: ``AWS::GameLift::GameSessionQueue.PlayerLatencyPolicies``.
        :param timeout_in_seconds: ``AWS::GameLift::GameSessionQueue.TimeoutInSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
        """
        self._values = {
            'name': name,
        }
        if destinations is not None: self._values["destinations"] = destinations
        if player_latency_policies is not None: self._values["player_latency_policies"] = player_latency_policies
        if timeout_in_seconds is not None: self._values["timeout_in_seconds"] = timeout_in_seconds

    @builtins.property
    def name(self) -> str:
        """``AWS::GameLift::GameSessionQueue.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-name
        """
        return self._values.get('name')

    @builtins.property
    def destinations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGameSessionQueue.DestinationProperty"]]]]]:
        """``AWS::GameLift::GameSessionQueue.Destinations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-destinations
        """
        return self._values.get('destinations')

    @builtins.property
    def player_latency_policies(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]]]:
        """``AWS::GameLift::GameSessionQueue.PlayerLatencyPolicies``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-playerlatencypolicies
        """
        return self._values.get('player_latency_policies')

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::GameSessionQueue.TimeoutInSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-timeoutinseconds
        """
        return self._values.get('timeout_in_seconds')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnGameSessionQueueProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMatchmakingConfiguration(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnMatchmakingConfiguration"):
    """A CloudFormation ``AWS::GameLift::MatchmakingConfiguration``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::MatchmakingConfiguration
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, acceptance_required: typing.Union[bool, aws_cdk.core.IResolvable], game_session_queue_arns: typing.List[str], name: str, request_timeout_seconds: jsii.Number, rule_set_name: str, acceptance_timeout_seconds: typing.Optional[jsii.Number]=None, additional_player_count: typing.Optional[jsii.Number]=None, backfill_mode: typing.Optional[str]=None, custom_event_data: typing.Optional[str]=None, description: typing.Optional[str]=None, game_properties: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "GamePropertyProperty"]]]]]=None, game_session_data: typing.Optional[str]=None, notification_target: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GameLift::MatchmakingConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param acceptance_required: ``AWS::GameLift::MatchmakingConfiguration.AcceptanceRequired``.
        :param game_session_queue_arns: ``AWS::GameLift::MatchmakingConfiguration.GameSessionQueueArns``.
        :param name: ``AWS::GameLift::MatchmakingConfiguration.Name``.
        :param request_timeout_seconds: ``AWS::GameLift::MatchmakingConfiguration.RequestTimeoutSeconds``.
        :param rule_set_name: ``AWS::GameLift::MatchmakingConfiguration.RuleSetName``.
        :param acceptance_timeout_seconds: ``AWS::GameLift::MatchmakingConfiguration.AcceptanceTimeoutSeconds``.
        :param additional_player_count: ``AWS::GameLift::MatchmakingConfiguration.AdditionalPlayerCount``.
        :param backfill_mode: ``AWS::GameLift::MatchmakingConfiguration.BackfillMode``.
        :param custom_event_data: ``AWS::GameLift::MatchmakingConfiguration.CustomEventData``.
        :param description: ``AWS::GameLift::MatchmakingConfiguration.Description``.
        :param game_properties: ``AWS::GameLift::MatchmakingConfiguration.GameProperties``.
        :param game_session_data: ``AWS::GameLift::MatchmakingConfiguration.GameSessionData``.
        :param notification_target: ``AWS::GameLift::MatchmakingConfiguration.NotificationTarget``.
        """
        props = CfnMatchmakingConfigurationProps(acceptance_required=acceptance_required, game_session_queue_arns=game_session_queue_arns, name=name, request_timeout_seconds=request_timeout_seconds, rule_set_name=rule_set_name, acceptance_timeout_seconds=acceptance_timeout_seconds, additional_player_count=additional_player_count, backfill_mode=backfill_mode, custom_event_data=custom_event_data, description=description, game_properties=game_properties, game_session_data=game_session_data, notification_target=notification_target)

        jsii.create(CfnMatchmakingConfiguration, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="acceptanceRequired")
    def acceptance_required(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GameLift::MatchmakingConfiguration.AcceptanceRequired``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancerequired
        """
        return jsii.get(self, "acceptanceRequired")

    @acceptance_required.setter
    def acceptance_required(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        jsii.set(self, "acceptanceRequired", value)

    @builtins.property
    @jsii.member(jsii_name="gameSessionQueueArns")
    def game_session_queue_arns(self) -> typing.List[str]:
        """``AWS::GameLift::MatchmakingConfiguration.GameSessionQueueArns``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessionqueuearns
        """
        return jsii.get(self, "gameSessionQueueArns")

    @game_session_queue_arns.setter
    def game_session_queue_arns(self, value: typing.List[str]):
        jsii.set(self, "gameSessionQueueArns", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::GameLift::MatchmakingConfiguration.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requestTimeoutSeconds")
    def request_timeout_seconds(self) -> jsii.Number:
        """``AWS::GameLift::MatchmakingConfiguration.RequestTimeoutSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-requesttimeoutseconds
        """
        return jsii.get(self, "requestTimeoutSeconds")

    @request_timeout_seconds.setter
    def request_timeout_seconds(self, value: jsii.Number):
        jsii.set(self, "requestTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> str:
        """``AWS::GameLift::MatchmakingConfiguration.RuleSetName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetname
        """
        return jsii.get(self, "ruleSetName")

    @rule_set_name.setter
    def rule_set_name(self, value: str):
        jsii.set(self, "ruleSetName", value)

    @builtins.property
    @jsii.member(jsii_name="acceptanceTimeoutSeconds")
    def acceptance_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::MatchmakingConfiguration.AcceptanceTimeoutSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancetimeoutseconds
        """
        return jsii.get(self, "acceptanceTimeoutSeconds")

    @acceptance_timeout_seconds.setter
    def acceptance_timeout_seconds(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "acceptanceTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="additionalPlayerCount")
    def additional_player_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::MatchmakingConfiguration.AdditionalPlayerCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-additionalplayercount
        """
        return jsii.get(self, "additionalPlayerCount")

    @additional_player_count.setter
    def additional_player_count(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "additionalPlayerCount", value)

    @builtins.property
    @jsii.member(jsii_name="backfillMode")
    def backfill_mode(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.BackfillMode``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-backfillmode
        """
        return jsii.get(self, "backfillMode")

    @backfill_mode.setter
    def backfill_mode(self, value: typing.Optional[str]):
        jsii.set(self, "backfillMode", value)

    @builtins.property
    @jsii.member(jsii_name="customEventData")
    def custom_event_data(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.CustomEventData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-customeventdata
        """
        return jsii.get(self, "customEventData")

    @custom_event_data.setter
    def custom_event_data(self, value: typing.Optional[str]):
        jsii.set(self, "customEventData", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="gameProperties")
    def game_properties(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "GamePropertyProperty"]]]]]:
        """``AWS::GameLift::MatchmakingConfiguration.GameProperties``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gameproperties
        """
        return jsii.get(self, "gameProperties")

    @game_properties.setter
    def game_properties(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "GamePropertyProperty"]]]]]):
        jsii.set(self, "gameProperties", value)

    @builtins.property
    @jsii.member(jsii_name="gameSessionData")
    def game_session_data(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.GameSessionData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessiondata
        """
        return jsii.get(self, "gameSessionData")

    @game_session_data.setter
    def game_session_data(self, value: typing.Optional[str]):
        jsii.set(self, "gameSessionData", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTarget")
    def notification_target(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.NotificationTarget``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-notificationtarget
        """
        return jsii.get(self, "notificationTarget")

    @notification_target.setter
    def notification_target(self, value: typing.Optional[str]):
        jsii.set(self, "notificationTarget", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnMatchmakingConfiguration.GamePropertyProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class GamePropertyProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnMatchmakingConfiguration.GamePropertyProperty.Key``.
            :param value: ``CfnMatchmakingConfiguration.GamePropertyProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @builtins.property
        def key(self) -> str:
            """``CfnMatchmakingConfiguration.GamePropertyProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-key
            """
            return self._values.get('key')

        @builtins.property
        def value(self) -> str:
            """``CfnMatchmakingConfiguration.GamePropertyProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'GamePropertyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnMatchmakingConfigurationProps", jsii_struct_bases=[], name_mapping={'acceptance_required': 'acceptanceRequired', 'game_session_queue_arns': 'gameSessionQueueArns', 'name': 'name', 'request_timeout_seconds': 'requestTimeoutSeconds', 'rule_set_name': 'ruleSetName', 'acceptance_timeout_seconds': 'acceptanceTimeoutSeconds', 'additional_player_count': 'additionalPlayerCount', 'backfill_mode': 'backfillMode', 'custom_event_data': 'customEventData', 'description': 'description', 'game_properties': 'gameProperties', 'game_session_data': 'gameSessionData', 'notification_target': 'notificationTarget'})
class CfnMatchmakingConfigurationProps():
    def __init__(self, *, acceptance_required: typing.Union[bool, aws_cdk.core.IResolvable], game_session_queue_arns: typing.List[str], name: str, request_timeout_seconds: jsii.Number, rule_set_name: str, acceptance_timeout_seconds: typing.Optional[jsii.Number]=None, additional_player_count: typing.Optional[jsii.Number]=None, backfill_mode: typing.Optional[str]=None, custom_event_data: typing.Optional[str]=None, description: typing.Optional[str]=None, game_properties: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]]]=None, game_session_data: typing.Optional[str]=None, notification_target: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GameLift::MatchmakingConfiguration``.

        :param acceptance_required: ``AWS::GameLift::MatchmakingConfiguration.AcceptanceRequired``.
        :param game_session_queue_arns: ``AWS::GameLift::MatchmakingConfiguration.GameSessionQueueArns``.
        :param name: ``AWS::GameLift::MatchmakingConfiguration.Name``.
        :param request_timeout_seconds: ``AWS::GameLift::MatchmakingConfiguration.RequestTimeoutSeconds``.
        :param rule_set_name: ``AWS::GameLift::MatchmakingConfiguration.RuleSetName``.
        :param acceptance_timeout_seconds: ``AWS::GameLift::MatchmakingConfiguration.AcceptanceTimeoutSeconds``.
        :param additional_player_count: ``AWS::GameLift::MatchmakingConfiguration.AdditionalPlayerCount``.
        :param backfill_mode: ``AWS::GameLift::MatchmakingConfiguration.BackfillMode``.
        :param custom_event_data: ``AWS::GameLift::MatchmakingConfiguration.CustomEventData``.
        :param description: ``AWS::GameLift::MatchmakingConfiguration.Description``.
        :param game_properties: ``AWS::GameLift::MatchmakingConfiguration.GameProperties``.
        :param game_session_data: ``AWS::GameLift::MatchmakingConfiguration.GameSessionData``.
        :param notification_target: ``AWS::GameLift::MatchmakingConfiguration.NotificationTarget``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
        """
        self._values = {
            'acceptance_required': acceptance_required,
            'game_session_queue_arns': game_session_queue_arns,
            'name': name,
            'request_timeout_seconds': request_timeout_seconds,
            'rule_set_name': rule_set_name,
        }
        if acceptance_timeout_seconds is not None: self._values["acceptance_timeout_seconds"] = acceptance_timeout_seconds
        if additional_player_count is not None: self._values["additional_player_count"] = additional_player_count
        if backfill_mode is not None: self._values["backfill_mode"] = backfill_mode
        if custom_event_data is not None: self._values["custom_event_data"] = custom_event_data
        if description is not None: self._values["description"] = description
        if game_properties is not None: self._values["game_properties"] = game_properties
        if game_session_data is not None: self._values["game_session_data"] = game_session_data
        if notification_target is not None: self._values["notification_target"] = notification_target

    @builtins.property
    def acceptance_required(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GameLift::MatchmakingConfiguration.AcceptanceRequired``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancerequired
        """
        return self._values.get('acceptance_required')

    @builtins.property
    def game_session_queue_arns(self) -> typing.List[str]:
        """``AWS::GameLift::MatchmakingConfiguration.GameSessionQueueArns``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessionqueuearns
        """
        return self._values.get('game_session_queue_arns')

    @builtins.property
    def name(self) -> str:
        """``AWS::GameLift::MatchmakingConfiguration.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-name
        """
        return self._values.get('name')

    @builtins.property
    def request_timeout_seconds(self) -> jsii.Number:
        """``AWS::GameLift::MatchmakingConfiguration.RequestTimeoutSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-requesttimeoutseconds
        """
        return self._values.get('request_timeout_seconds')

    @builtins.property
    def rule_set_name(self) -> str:
        """``AWS::GameLift::MatchmakingConfiguration.RuleSetName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetname
        """
        return self._values.get('rule_set_name')

    @builtins.property
    def acceptance_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::MatchmakingConfiguration.AcceptanceTimeoutSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancetimeoutseconds
        """
        return self._values.get('acceptance_timeout_seconds')

    @builtins.property
    def additional_player_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::GameLift::MatchmakingConfiguration.AdditionalPlayerCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-additionalplayercount
        """
        return self._values.get('additional_player_count')

    @builtins.property
    def backfill_mode(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.BackfillMode``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-backfillmode
        """
        return self._values.get('backfill_mode')

    @builtins.property
    def custom_event_data(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.CustomEventData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-customeventdata
        """
        return self._values.get('custom_event_data')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-description
        """
        return self._values.get('description')

    @builtins.property
    def game_properties(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]]]:
        """``AWS::GameLift::MatchmakingConfiguration.GameProperties``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gameproperties
        """
        return self._values.get('game_properties')

    @builtins.property
    def game_session_data(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.GameSessionData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessiondata
        """
        return self._values.get('game_session_data')

    @builtins.property
    def notification_target(self) -> typing.Optional[str]:
        """``AWS::GameLift::MatchmakingConfiguration.NotificationTarget``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-notificationtarget
        """
        return self._values.get('notification_target')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMatchmakingConfigurationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMatchmakingRuleSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnMatchmakingRuleSet"):
    """A CloudFormation ``AWS::GameLift::MatchmakingRuleSet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::MatchmakingRuleSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, rule_set_body: str) -> None:
        """Create a new ``AWS::GameLift::MatchmakingRuleSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::GameLift::MatchmakingRuleSet.Name``.
        :param rule_set_body: ``AWS::GameLift::MatchmakingRuleSet.RuleSetBody``.
        """
        props = CfnMatchmakingRuleSetProps(name=name, rule_set_body=rule_set_body)

        jsii.create(CfnMatchmakingRuleSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::GameLift::MatchmakingRuleSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetBody")
    def rule_set_body(self) -> str:
        """``AWS::GameLift::MatchmakingRuleSet.RuleSetBody``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-rulesetbody
        """
        return jsii.get(self, "ruleSetBody")

    @rule_set_body.setter
    def rule_set_body(self, value: str):
        jsii.set(self, "ruleSetBody", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnMatchmakingRuleSetProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'rule_set_body': 'ruleSetBody'})
class CfnMatchmakingRuleSetProps():
    def __init__(self, *, name: str, rule_set_body: str):
        """Properties for defining a ``AWS::GameLift::MatchmakingRuleSet``.

        :param name: ``AWS::GameLift::MatchmakingRuleSet.Name``.
        :param rule_set_body: ``AWS::GameLift::MatchmakingRuleSet.RuleSetBody``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
        """
        self._values = {
            'name': name,
            'rule_set_body': rule_set_body,
        }

    @builtins.property
    def name(self) -> str:
        """``AWS::GameLift::MatchmakingRuleSet.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-name
        """
        return self._values.get('name')

    @builtins.property
    def rule_set_body(self) -> str:
        """``AWS::GameLift::MatchmakingRuleSet.RuleSetBody``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-rulesetbody
        """
        return self._values.get('rule_set_body')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMatchmakingRuleSetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnScript(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-gamelift.CfnScript"):
    """A CloudFormation ``AWS::GameLift::Script``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
    cloudformationResource:
    :cloudformationResource:: AWS::GameLift::Script
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, storage_location: typing.Union[aws_cdk.core.IResolvable, "S3LocationProperty"], name: typing.Optional[str]=None, version: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GameLift::Script``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param storage_location: ``AWS::GameLift::Script.StorageLocation``.
        :param name: ``AWS::GameLift::Script.Name``.
        :param version: ``AWS::GameLift::Script.Version``.
        """
        props = CfnScriptProps(storage_location=storage_location, name=name, version=version)

        jsii.create(CfnScript, self, [scope, id, props])

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
    @jsii.member(jsii_name="storageLocation")
    def storage_location(self) -> typing.Union[aws_cdk.core.IResolvable, "S3LocationProperty"]:
        """``AWS::GameLift::Script.StorageLocation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-storagelocation
        """
        return jsii.get(self, "storageLocation")

    @storage_location.setter
    def storage_location(self, value: typing.Union[aws_cdk.core.IResolvable, "S3LocationProperty"]):
        jsii.set(self, "storageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GameLift::Script.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[str]:
        """``AWS::GameLift::Script.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-version
        """
        return jsii.get(self, "version")

    @version.setter
    def version(self, value: typing.Optional[str]):
        jsii.set(self, "version", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnScript.S3LocationProperty", jsii_struct_bases=[], name_mapping={'bucket': 'bucket', 'key': 'key', 'role_arn': 'roleArn', 'object_version': 'objectVersion'})
    class S3LocationProperty():
        def __init__(self, *, bucket: str, key: str, role_arn: str, object_version: typing.Optional[str]=None):
            """
            :param bucket: ``CfnScript.S3LocationProperty.Bucket``.
            :param key: ``CfnScript.S3LocationProperty.Key``.
            :param role_arn: ``CfnScript.S3LocationProperty.RoleArn``.
            :param object_version: ``CfnScript.S3LocationProperty.ObjectVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html
            """
            self._values = {
                'bucket': bucket,
                'key': key,
                'role_arn': role_arn,
            }
            if object_version is not None: self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> str:
            """``CfnScript.S3LocationProperty.Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-bucket
            """
            return self._values.get('bucket')

        @builtins.property
        def key(self) -> str:
            """``CfnScript.S3LocationProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-key
            """
            return self._values.get('key')

        @builtins.property
        def role_arn(self) -> str:
            """``CfnScript.S3LocationProperty.RoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-rolearn
            """
            return self._values.get('role_arn')

        @builtins.property
        def object_version(self) -> typing.Optional[str]:
            """``CfnScript.S3LocationProperty.ObjectVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-objectversion
            """
            return self._values.get('object_version')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'S3LocationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-gamelift.CfnScriptProps", jsii_struct_bases=[], name_mapping={'storage_location': 'storageLocation', 'name': 'name', 'version': 'version'})
class CfnScriptProps():
    def __init__(self, *, storage_location: typing.Union[aws_cdk.core.IResolvable, "CfnScript.S3LocationProperty"], name: typing.Optional[str]=None, version: typing.Optional[str]=None):
        """Properties for defining a ``AWS::GameLift::Script``.

        :param storage_location: ``AWS::GameLift::Script.StorageLocation``.
        :param name: ``AWS::GameLift::Script.Name``.
        :param version: ``AWS::GameLift::Script.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
        """
        self._values = {
            'storage_location': storage_location,
        }
        if name is not None: self._values["name"] = name
        if version is not None: self._values["version"] = version

    @builtins.property
    def storage_location(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnScript.S3LocationProperty"]:
        """``AWS::GameLift::Script.StorageLocation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-storagelocation
        """
        return self._values.get('storage_location')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::GameLift::Script.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-name
        """
        return self._values.get('name')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """``AWS::GameLift::Script.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-version
        """
        return self._values.get('version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnScriptProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnAlias", "CfnAliasProps", "CfnBuild", "CfnBuildProps", "CfnFleet", "CfnFleetProps", "CfnGameSessionQueue", "CfnGameSessionQueueProps", "CfnMatchmakingConfiguration", "CfnMatchmakingConfigurationProps", "CfnMatchmakingRuleSet", "CfnMatchmakingRuleSetProps", "CfnScript", "CfnScriptProps", "__jsii_assembly__"]

publication.publish()
