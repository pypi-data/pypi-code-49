"""
## AWS Amplify Construct Library

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
import aws_cdk.aws_amplify as amplify
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-amplify", "1.24.0", __name__, "aws-amplify@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApp(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-amplify.CfnApp"):
    """A CloudFormation ``AWS::Amplify::App``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html
    cloudformationResource:
    :cloudformationResource:: AWS::Amplify::App
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, access_token: typing.Optional[str]=None, auto_branch_creation_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AutoBranchCreationConfigProperty"]]]=None, basic_auth_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["BasicAuthConfigProperty"]]]=None, build_spec: typing.Optional[str]=None, custom_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CustomRuleProperty"]]]]]=None, description: typing.Optional[str]=None, environment_variables: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EnvironmentVariableProperty"]]]]]=None, iam_service_role: typing.Optional[str]=None, oauth_token: typing.Optional[str]=None, repository: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::Amplify::App``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Amplify::App.Name``.
        :param access_token: ``AWS::Amplify::App.AccessToken``.
        :param auto_branch_creation_config: ``AWS::Amplify::App.AutoBranchCreationConfig``.
        :param basic_auth_config: ``AWS::Amplify::App.BasicAuthConfig``.
        :param build_spec: ``AWS::Amplify::App.BuildSpec``.
        :param custom_rules: ``AWS::Amplify::App.CustomRules``.
        :param description: ``AWS::Amplify::App.Description``.
        :param environment_variables: ``AWS::Amplify::App.EnvironmentVariables``.
        :param iam_service_role: ``AWS::Amplify::App.IAMServiceRole``.
        :param oauth_token: ``AWS::Amplify::App.OauthToken``.
        :param repository: ``AWS::Amplify::App.Repository``.
        :param tags: ``AWS::Amplify::App.Tags``.
        """
        props = CfnAppProps(name=name, access_token=access_token, auto_branch_creation_config=auto_branch_creation_config, basic_auth_config=basic_auth_config, build_spec=build_spec, custom_rules=custom_rules, description=description, environment_variables=environment_variables, iam_service_role=iam_service_role, oauth_token=oauth_token, repository=repository, tags=tags)

        jsii.create(CfnApp, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAppId")
    def attr_app_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AppId
        """
        return jsii.get(self, "attrAppId")

    @builtins.property
    @jsii.member(jsii_name="attrAppName")
    def attr_app_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AppName
        """
        return jsii.get(self, "attrAppName")

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property
    @jsii.member(jsii_name="attrDefaultDomain")
    def attr_default_domain(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DefaultDomain
        """
        return jsii.get(self, "attrDefaultDomain")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Amplify::App.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::Amplify::App.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.AccessToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-accesstoken
        """
        return jsii.get(self, "accessToken")

    @access_token.setter
    def access_token(self, value: typing.Optional[str]):
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="autoBranchCreationConfig")
    def auto_branch_creation_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AutoBranchCreationConfigProperty"]]]:
        """``AWS::Amplify::App.AutoBranchCreationConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-autobranchcreationconfig
        """
        return jsii.get(self, "autoBranchCreationConfig")

    @auto_branch_creation_config.setter
    def auto_branch_creation_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AutoBranchCreationConfigProperty"]]]):
        jsii.set(self, "autoBranchCreationConfig", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthConfig")
    def basic_auth_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["BasicAuthConfigProperty"]]]:
        """``AWS::Amplify::App.BasicAuthConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-basicauthconfig
        """
        return jsii.get(self, "basicAuthConfig")

    @basic_auth_config.setter
    def basic_auth_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["BasicAuthConfigProperty"]]]):
        jsii.set(self, "basicAuthConfig", value)

    @builtins.property
    @jsii.member(jsii_name="buildSpec")
    def build_spec(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.BuildSpec``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-buildspec
        """
        return jsii.get(self, "buildSpec")

    @build_spec.setter
    def build_spec(self, value: typing.Optional[str]):
        jsii.set(self, "buildSpec", value)

    @builtins.property
    @jsii.member(jsii_name="customRules")
    def custom_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CustomRuleProperty"]]]]]:
        """``AWS::Amplify::App.CustomRules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customrules
        """
        return jsii.get(self, "customRules")

    @custom_rules.setter
    def custom_rules(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CustomRuleProperty"]]]]]):
        jsii.set(self, "customRules", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EnvironmentVariableProperty"]]]]]:
        """``AWS::Amplify::App.EnvironmentVariables``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-environmentvariables
        """
        return jsii.get(self, "environmentVariables")

    @environment_variables.setter
    def environment_variables(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EnvironmentVariableProperty"]]]]]):
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="iamServiceRole")
    def iam_service_role(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.IAMServiceRole``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-iamservicerole
        """
        return jsii.get(self, "iamServiceRole")

    @iam_service_role.setter
    def iam_service_role(self, value: typing.Optional[str]):
        jsii.set(self, "iamServiceRole", value)

    @builtins.property
    @jsii.member(jsii_name="oauthToken")
    def oauth_token(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.OauthToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-oauthtoken
        """
        return jsii.get(self, "oauthToken")

    @oauth_token.setter
    def oauth_token(self, value: typing.Optional[str]):
        jsii.set(self, "oauthToken", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.Repository``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-repository
        """
        return jsii.get(self, "repository")

    @repository.setter
    def repository(self, value: typing.Optional[str]):
        jsii.set(self, "repository", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnApp.AutoBranchCreationConfigProperty", jsii_struct_bases=[], name_mapping={'auto_branch_creation_patterns': 'autoBranchCreationPatterns', 'basic_auth_config': 'basicAuthConfig', 'build_spec': 'buildSpec', 'enable_auto_branch_creation': 'enableAutoBranchCreation', 'enable_auto_build': 'enableAutoBuild', 'enable_pull_request_preview': 'enablePullRequestPreview', 'environment_variables': 'environmentVariables', 'pull_request_environment_name': 'pullRequestEnvironmentName', 'stage': 'stage'})
    class AutoBranchCreationConfigProperty():
        def __init__(self, *, auto_branch_creation_patterns: typing.Optional[typing.List[str]]=None, basic_auth_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApp.BasicAuthConfigProperty"]]]=None, build_spec: typing.Optional[str]=None, enable_auto_branch_creation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_auto_build: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_pull_request_preview: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, environment_variables: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]]]=None, pull_request_environment_name: typing.Optional[str]=None, stage: typing.Optional[str]=None):
            """
            :param auto_branch_creation_patterns: ``CfnApp.AutoBranchCreationConfigProperty.AutoBranchCreationPatterns``.
            :param basic_auth_config: ``CfnApp.AutoBranchCreationConfigProperty.BasicAuthConfig``.
            :param build_spec: ``CfnApp.AutoBranchCreationConfigProperty.BuildSpec``.
            :param enable_auto_branch_creation: ``CfnApp.AutoBranchCreationConfigProperty.EnableAutoBranchCreation``.
            :param enable_auto_build: ``CfnApp.AutoBranchCreationConfigProperty.EnableAutoBuild``.
            :param enable_pull_request_preview: ``CfnApp.AutoBranchCreationConfigProperty.EnablePullRequestPreview``.
            :param environment_variables: ``CfnApp.AutoBranchCreationConfigProperty.EnvironmentVariables``.
            :param pull_request_environment_name: ``CfnApp.AutoBranchCreationConfigProperty.PullRequestEnvironmentName``.
            :param stage: ``CfnApp.AutoBranchCreationConfigProperty.Stage``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html
            """
            self._values = {
            }
            if auto_branch_creation_patterns is not None: self._values["auto_branch_creation_patterns"] = auto_branch_creation_patterns
            if basic_auth_config is not None: self._values["basic_auth_config"] = basic_auth_config
            if build_spec is not None: self._values["build_spec"] = build_spec
            if enable_auto_branch_creation is not None: self._values["enable_auto_branch_creation"] = enable_auto_branch_creation
            if enable_auto_build is not None: self._values["enable_auto_build"] = enable_auto_build
            if enable_pull_request_preview is not None: self._values["enable_pull_request_preview"] = enable_pull_request_preview
            if environment_variables is not None: self._values["environment_variables"] = environment_variables
            if pull_request_environment_name is not None: self._values["pull_request_environment_name"] = pull_request_environment_name
            if stage is not None: self._values["stage"] = stage

        @builtins.property
        def auto_branch_creation_patterns(self) -> typing.Optional[typing.List[str]]:
            """``CfnApp.AutoBranchCreationConfigProperty.AutoBranchCreationPatterns``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns
            """
            return self._values.get('auto_branch_creation_patterns')

        @builtins.property
        def basic_auth_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApp.BasicAuthConfigProperty"]]]:
            """``CfnApp.AutoBranchCreationConfigProperty.BasicAuthConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-basicauthconfig
            """
            return self._values.get('basic_auth_config')

        @builtins.property
        def build_spec(self) -> typing.Optional[str]:
            """``CfnApp.AutoBranchCreationConfigProperty.BuildSpec``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-buildspec
            """
            return self._values.get('build_spec')

        @builtins.property
        def enable_auto_branch_creation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnApp.AutoBranchCreationConfigProperty.EnableAutoBranchCreation``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation
            """
            return self._values.get('enable_auto_branch_creation')

        @builtins.property
        def enable_auto_build(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnApp.AutoBranchCreationConfigProperty.EnableAutoBuild``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobuild
            """
            return self._values.get('enable_auto_build')

        @builtins.property
        def enable_pull_request_preview(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnApp.AutoBranchCreationConfigProperty.EnablePullRequestPreview``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview
            """
            return self._values.get('enable_pull_request_preview')

        @builtins.property
        def environment_variables(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]]]:
            """``CfnApp.AutoBranchCreationConfigProperty.EnvironmentVariables``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-environmentvariables
            """
            return self._values.get('environment_variables')

        @builtins.property
        def pull_request_environment_name(self) -> typing.Optional[str]:
            """``CfnApp.AutoBranchCreationConfigProperty.PullRequestEnvironmentName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname
            """
            return self._values.get('pull_request_environment_name')

        @builtins.property
        def stage(self) -> typing.Optional[str]:
            """``CfnApp.AutoBranchCreationConfigProperty.Stage``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-stage
            """
            return self._values.get('stage')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AutoBranchCreationConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnApp.BasicAuthConfigProperty", jsii_struct_bases=[], name_mapping={'enable_basic_auth': 'enableBasicAuth', 'password': 'password', 'username': 'username'})
    class BasicAuthConfigProperty():
        def __init__(self, *, enable_basic_auth: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, password: typing.Optional[str]=None, username: typing.Optional[str]=None):
            """
            :param enable_basic_auth: ``CfnApp.BasicAuthConfigProperty.EnableBasicAuth``.
            :param password: ``CfnApp.BasicAuthConfigProperty.Password``.
            :param username: ``CfnApp.BasicAuthConfigProperty.Username``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html
            """
            self._values = {
            }
            if enable_basic_auth is not None: self._values["enable_basic_auth"] = enable_basic_auth
            if password is not None: self._values["password"] = password
            if username is not None: self._values["username"] = username

        @builtins.property
        def enable_basic_auth(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnApp.BasicAuthConfigProperty.EnableBasicAuth``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-enablebasicauth
            """
            return self._values.get('enable_basic_auth')

        @builtins.property
        def password(self) -> typing.Optional[str]:
            """``CfnApp.BasicAuthConfigProperty.Password``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-password
            """
            return self._values.get('password')

        @builtins.property
        def username(self) -> typing.Optional[str]:
            """``CfnApp.BasicAuthConfigProperty.Username``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-username
            """
            return self._values.get('username')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BasicAuthConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnApp.CustomRuleProperty", jsii_struct_bases=[], name_mapping={'source': 'source', 'target': 'target', 'condition': 'condition', 'status': 'status'})
    class CustomRuleProperty():
        def __init__(self, *, source: str, target: str, condition: typing.Optional[str]=None, status: typing.Optional[str]=None):
            """
            :param source: ``CfnApp.CustomRuleProperty.Source``.
            :param target: ``CfnApp.CustomRuleProperty.Target``.
            :param condition: ``CfnApp.CustomRuleProperty.Condition``.
            :param status: ``CfnApp.CustomRuleProperty.Status``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html
            """
            self._values = {
                'source': source,
                'target': target,
            }
            if condition is not None: self._values["condition"] = condition
            if status is not None: self._values["status"] = status

        @builtins.property
        def source(self) -> str:
            """``CfnApp.CustomRuleProperty.Source``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-source
            """
            return self._values.get('source')

        @builtins.property
        def target(self) -> str:
            """``CfnApp.CustomRuleProperty.Target``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-target
            """
            return self._values.get('target')

        @builtins.property
        def condition(self) -> typing.Optional[str]:
            """``CfnApp.CustomRuleProperty.Condition``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-condition
            """
            return self._values.get('condition')

        @builtins.property
        def status(self) -> typing.Optional[str]:
            """``CfnApp.CustomRuleProperty.Status``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-status
            """
            return self._values.get('status')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CustomRuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnApp.EnvironmentVariableProperty", jsii_struct_bases=[], name_mapping={'name': 'name', 'value': 'value'})
    class EnvironmentVariableProperty():
        def __init__(self, *, name: str, value: str):
            """
            :param name: ``CfnApp.EnvironmentVariableProperty.Name``.
            :param value: ``CfnApp.EnvironmentVariableProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html
            """
            self._values = {
                'name': name,
                'value': value,
            }

        @builtins.property
        def name(self) -> str:
            """``CfnApp.EnvironmentVariableProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-name
            """
            return self._values.get('name')

        @builtins.property
        def value(self) -> str:
            """``CfnApp.EnvironmentVariableProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EnvironmentVariableProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnAppProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'access_token': 'accessToken', 'auto_branch_creation_config': 'autoBranchCreationConfig', 'basic_auth_config': 'basicAuthConfig', 'build_spec': 'buildSpec', 'custom_rules': 'customRules', 'description': 'description', 'environment_variables': 'environmentVariables', 'iam_service_role': 'iamServiceRole', 'oauth_token': 'oauthToken', 'repository': 'repository', 'tags': 'tags'})
class CfnAppProps():
    def __init__(self, *, name: str, access_token: typing.Optional[str]=None, auto_branch_creation_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApp.AutoBranchCreationConfigProperty"]]]=None, basic_auth_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApp.BasicAuthConfigProperty"]]]=None, build_spec: typing.Optional[str]=None, custom_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.CustomRuleProperty"]]]]]=None, description: typing.Optional[str]=None, environment_variables: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]]]=None, iam_service_role: typing.Optional[str]=None, oauth_token: typing.Optional[str]=None, repository: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::Amplify::App``.

        :param name: ``AWS::Amplify::App.Name``.
        :param access_token: ``AWS::Amplify::App.AccessToken``.
        :param auto_branch_creation_config: ``AWS::Amplify::App.AutoBranchCreationConfig``.
        :param basic_auth_config: ``AWS::Amplify::App.BasicAuthConfig``.
        :param build_spec: ``AWS::Amplify::App.BuildSpec``.
        :param custom_rules: ``AWS::Amplify::App.CustomRules``.
        :param description: ``AWS::Amplify::App.Description``.
        :param environment_variables: ``AWS::Amplify::App.EnvironmentVariables``.
        :param iam_service_role: ``AWS::Amplify::App.IAMServiceRole``.
        :param oauth_token: ``AWS::Amplify::App.OauthToken``.
        :param repository: ``AWS::Amplify::App.Repository``.
        :param tags: ``AWS::Amplify::App.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html
        """
        self._values = {
            'name': name,
        }
        if access_token is not None: self._values["access_token"] = access_token
        if auto_branch_creation_config is not None: self._values["auto_branch_creation_config"] = auto_branch_creation_config
        if basic_auth_config is not None: self._values["basic_auth_config"] = basic_auth_config
        if build_spec is not None: self._values["build_spec"] = build_spec
        if custom_rules is not None: self._values["custom_rules"] = custom_rules
        if description is not None: self._values["description"] = description
        if environment_variables is not None: self._values["environment_variables"] = environment_variables
        if iam_service_role is not None: self._values["iam_service_role"] = iam_service_role
        if oauth_token is not None: self._values["oauth_token"] = oauth_token
        if repository is not None: self._values["repository"] = repository
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def name(self) -> str:
        """``AWS::Amplify::App.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-name
        """
        return self._values.get('name')

    @builtins.property
    def access_token(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.AccessToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-accesstoken
        """
        return self._values.get('access_token')

    @builtins.property
    def auto_branch_creation_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApp.AutoBranchCreationConfigProperty"]]]:
        """``AWS::Amplify::App.AutoBranchCreationConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-autobranchcreationconfig
        """
        return self._values.get('auto_branch_creation_config')

    @builtins.property
    def basic_auth_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApp.BasicAuthConfigProperty"]]]:
        """``AWS::Amplify::App.BasicAuthConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-basicauthconfig
        """
        return self._values.get('basic_auth_config')

    @builtins.property
    def build_spec(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.BuildSpec``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-buildspec
        """
        return self._values.get('build_spec')

    @builtins.property
    def custom_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.CustomRuleProperty"]]]]]:
        """``AWS::Amplify::App.CustomRules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customrules
        """
        return self._values.get('custom_rules')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-description
        """
        return self._values.get('description')

    @builtins.property
    def environment_variables(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]]]:
        """``AWS::Amplify::App.EnvironmentVariables``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-environmentvariables
        """
        return self._values.get('environment_variables')

    @builtins.property
    def iam_service_role(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.IAMServiceRole``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-iamservicerole
        """
        return self._values.get('iam_service_role')

    @builtins.property
    def oauth_token(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.OauthToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-oauthtoken
        """
        return self._values.get('oauth_token')

    @builtins.property
    def repository(self) -> typing.Optional[str]:
        """``AWS::Amplify::App.Repository``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-repository
        """
        return self._values.get('repository')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Amplify::App.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnAppProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBranch(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-amplify.CfnBranch"):
    """A CloudFormation ``AWS::Amplify::Branch``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html
    cloudformationResource:
    :cloudformationResource:: AWS::Amplify::Branch
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, app_id: str, branch_name: str, basic_auth_config: typing.Optional[typing.Union[typing.Optional["BasicAuthConfigProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, build_spec: typing.Optional[str]=None, description: typing.Optional[str]=None, enable_auto_build: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_pull_request_preview: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, environment_variables: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EnvironmentVariableProperty"]]]]]=None, pull_request_environment_name: typing.Optional[str]=None, stage: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::Amplify::Branch``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_id: ``AWS::Amplify::Branch.AppId``.
        :param branch_name: ``AWS::Amplify::Branch.BranchName``.
        :param basic_auth_config: ``AWS::Amplify::Branch.BasicAuthConfig``.
        :param build_spec: ``AWS::Amplify::Branch.BuildSpec``.
        :param description: ``AWS::Amplify::Branch.Description``.
        :param enable_auto_build: ``AWS::Amplify::Branch.EnableAutoBuild``.
        :param enable_pull_request_preview: ``AWS::Amplify::Branch.EnablePullRequestPreview``.
        :param environment_variables: ``AWS::Amplify::Branch.EnvironmentVariables``.
        :param pull_request_environment_name: ``AWS::Amplify::Branch.PullRequestEnvironmentName``.
        :param stage: ``AWS::Amplify::Branch.Stage``.
        :param tags: ``AWS::Amplify::Branch.Tags``.
        """
        props = CfnBranchProps(app_id=app_id, branch_name=branch_name, basic_auth_config=basic_auth_config, build_spec=build_spec, description=description, enable_auto_build=enable_auto_build, enable_pull_request_preview=enable_pull_request_preview, environment_variables=environment_variables, pull_request_environment_name=pull_request_environment_name, stage=stage, tags=tags)

        jsii.create(CfnBranch, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrBranchName")
    def attr_branch_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: BranchName
        """
        return jsii.get(self, "attrBranchName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Amplify::Branch.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> str:
        """``AWS::Amplify::Branch.AppId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-appid
        """
        return jsii.get(self, "appId")

    @app_id.setter
    def app_id(self, value: str):
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> str:
        """``AWS::Amplify::Branch.BranchName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-branchname
        """
        return jsii.get(self, "branchName")

    @branch_name.setter
    def branch_name(self, value: str):
        jsii.set(self, "branchName", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthConfig")
    def basic_auth_config(self) -> typing.Optional[typing.Union[typing.Optional["BasicAuthConfigProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Amplify::Branch.BasicAuthConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-basicauthconfig
        """
        return jsii.get(self, "basicAuthConfig")

    @basic_auth_config.setter
    def basic_auth_config(self, value: typing.Optional[typing.Union[typing.Optional["BasicAuthConfigProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "basicAuthConfig", value)

    @builtins.property
    @jsii.member(jsii_name="buildSpec")
    def build_spec(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.BuildSpec``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-buildspec
        """
        return jsii.get(self, "buildSpec")

    @build_spec.setter
    def build_spec(self, value: typing.Optional[str]):
        jsii.set(self, "buildSpec", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoBuild")
    def enable_auto_build(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Amplify::Branch.EnableAutoBuild``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableautobuild
        """
        return jsii.get(self, "enableAutoBuild")

    @enable_auto_build.setter
    def enable_auto_build(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "enableAutoBuild", value)

    @builtins.property
    @jsii.member(jsii_name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Amplify::Branch.EnablePullRequestPreview``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enablepullrequestpreview
        """
        return jsii.get(self, "enablePullRequestPreview")

    @enable_pull_request_preview.setter
    def enable_pull_request_preview(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "enablePullRequestPreview", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EnvironmentVariableProperty"]]]]]:
        """``AWS::Amplify::Branch.EnvironmentVariables``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-environmentvariables
        """
        return jsii.get(self, "environmentVariables")

    @environment_variables.setter
    def environment_variables(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EnvironmentVariableProperty"]]]]]):
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.PullRequestEnvironmentName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-pullrequestenvironmentname
        """
        return jsii.get(self, "pullRequestEnvironmentName")

    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: typing.Optional[str]):
        jsii.set(self, "pullRequestEnvironmentName", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.Stage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-stage
        """
        return jsii.get(self, "stage")

    @stage.setter
    def stage(self, value: typing.Optional[str]):
        jsii.set(self, "stage", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnBranch.BasicAuthConfigProperty", jsii_struct_bases=[], name_mapping={'password': 'password', 'username': 'username', 'enable_basic_auth': 'enableBasicAuth'})
    class BasicAuthConfigProperty():
        def __init__(self, *, password: str, username: str, enable_basic_auth: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param password: ``CfnBranch.BasicAuthConfigProperty.Password``.
            :param username: ``CfnBranch.BasicAuthConfigProperty.Username``.
            :param enable_basic_auth: ``CfnBranch.BasicAuthConfigProperty.EnableBasicAuth``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html
            """
            self._values = {
                'password': password,
                'username': username,
            }
            if enable_basic_auth is not None: self._values["enable_basic_auth"] = enable_basic_auth

        @builtins.property
        def password(self) -> str:
            """``CfnBranch.BasicAuthConfigProperty.Password``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-password
            """
            return self._values.get('password')

        @builtins.property
        def username(self) -> str:
            """``CfnBranch.BasicAuthConfigProperty.Username``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-username
            """
            return self._values.get('username')

        @builtins.property
        def enable_basic_auth(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnBranch.BasicAuthConfigProperty.EnableBasicAuth``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-enablebasicauth
            """
            return self._values.get('enable_basic_auth')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BasicAuthConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnBranch.EnvironmentVariableProperty", jsii_struct_bases=[], name_mapping={'name': 'name', 'value': 'value'})
    class EnvironmentVariableProperty():
        def __init__(self, *, name: str, value: str):
            """
            :param name: ``CfnBranch.EnvironmentVariableProperty.Name``.
            :param value: ``CfnBranch.EnvironmentVariableProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html
            """
            self._values = {
                'name': name,
                'value': value,
            }

        @builtins.property
        def name(self) -> str:
            """``CfnBranch.EnvironmentVariableProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-name
            """
            return self._values.get('name')

        @builtins.property
        def value(self) -> str:
            """``CfnBranch.EnvironmentVariableProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EnvironmentVariableProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnBranchProps", jsii_struct_bases=[], name_mapping={'app_id': 'appId', 'branch_name': 'branchName', 'basic_auth_config': 'basicAuthConfig', 'build_spec': 'buildSpec', 'description': 'description', 'enable_auto_build': 'enableAutoBuild', 'enable_pull_request_preview': 'enablePullRequestPreview', 'environment_variables': 'environmentVariables', 'pull_request_environment_name': 'pullRequestEnvironmentName', 'stage': 'stage', 'tags': 'tags'})
class CfnBranchProps():
    def __init__(self, *, app_id: str, branch_name: str, basic_auth_config: typing.Optional[typing.Union[typing.Optional["CfnBranch.BasicAuthConfigProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, build_spec: typing.Optional[str]=None, description: typing.Optional[str]=None, enable_auto_build: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_pull_request_preview: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, environment_variables: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBranch.EnvironmentVariableProperty"]]]]]=None, pull_request_environment_name: typing.Optional[str]=None, stage: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::Amplify::Branch``.

        :param app_id: ``AWS::Amplify::Branch.AppId``.
        :param branch_name: ``AWS::Amplify::Branch.BranchName``.
        :param basic_auth_config: ``AWS::Amplify::Branch.BasicAuthConfig``.
        :param build_spec: ``AWS::Amplify::Branch.BuildSpec``.
        :param description: ``AWS::Amplify::Branch.Description``.
        :param enable_auto_build: ``AWS::Amplify::Branch.EnableAutoBuild``.
        :param enable_pull_request_preview: ``AWS::Amplify::Branch.EnablePullRequestPreview``.
        :param environment_variables: ``AWS::Amplify::Branch.EnvironmentVariables``.
        :param pull_request_environment_name: ``AWS::Amplify::Branch.PullRequestEnvironmentName``.
        :param stage: ``AWS::Amplify::Branch.Stage``.
        :param tags: ``AWS::Amplify::Branch.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html
        """
        self._values = {
            'app_id': app_id,
            'branch_name': branch_name,
        }
        if basic_auth_config is not None: self._values["basic_auth_config"] = basic_auth_config
        if build_spec is not None: self._values["build_spec"] = build_spec
        if description is not None: self._values["description"] = description
        if enable_auto_build is not None: self._values["enable_auto_build"] = enable_auto_build
        if enable_pull_request_preview is not None: self._values["enable_pull_request_preview"] = enable_pull_request_preview
        if environment_variables is not None: self._values["environment_variables"] = environment_variables
        if pull_request_environment_name is not None: self._values["pull_request_environment_name"] = pull_request_environment_name
        if stage is not None: self._values["stage"] = stage
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def app_id(self) -> str:
        """``AWS::Amplify::Branch.AppId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-appid
        """
        return self._values.get('app_id')

    @builtins.property
    def branch_name(self) -> str:
        """``AWS::Amplify::Branch.BranchName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-branchname
        """
        return self._values.get('branch_name')

    @builtins.property
    def basic_auth_config(self) -> typing.Optional[typing.Union[typing.Optional["CfnBranch.BasicAuthConfigProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Amplify::Branch.BasicAuthConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-basicauthconfig
        """
        return self._values.get('basic_auth_config')

    @builtins.property
    def build_spec(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.BuildSpec``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-buildspec
        """
        return self._values.get('build_spec')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-description
        """
        return self._values.get('description')

    @builtins.property
    def enable_auto_build(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Amplify::Branch.EnableAutoBuild``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableautobuild
        """
        return self._values.get('enable_auto_build')

    @builtins.property
    def enable_pull_request_preview(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Amplify::Branch.EnablePullRequestPreview``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enablepullrequestpreview
        """
        return self._values.get('enable_pull_request_preview')

    @builtins.property
    def environment_variables(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBranch.EnvironmentVariableProperty"]]]]]:
        """``AWS::Amplify::Branch.EnvironmentVariables``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-environmentvariables
        """
        return self._values.get('environment_variables')

    @builtins.property
    def pull_request_environment_name(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.PullRequestEnvironmentName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-pullrequestenvironmentname
        """
        return self._values.get('pull_request_environment_name')

    @builtins.property
    def stage(self) -> typing.Optional[str]:
        """``AWS::Amplify::Branch.Stage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-stage
        """
        return self._values.get('stage')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Amplify::Branch.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnBranchProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDomain(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-amplify.CfnDomain"):
    """A CloudFormation ``AWS::Amplify::Domain``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html
    cloudformationResource:
    :cloudformationResource:: AWS::Amplify::Domain
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, app_id: str, domain_name: str, sub_domain_settings: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "SubDomainSettingProperty"]]]) -> None:
        """Create a new ``AWS::Amplify::Domain``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_id: ``AWS::Amplify::Domain.AppId``.
        :param domain_name: ``AWS::Amplify::Domain.DomainName``.
        :param sub_domain_settings: ``AWS::Amplify::Domain.SubDomainSettings``.
        """
        props = CfnDomainProps(app_id=app_id, domain_name=domain_name, sub_domain_settings=sub_domain_settings)

        jsii.create(CfnDomain, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCertificateRecord")
    def attr_certificate_record(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: CertificateRecord
        """
        return jsii.get(self, "attrCertificateRecord")

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DomainName
        """
        return jsii.get(self, "attrDomainName")

    @builtins.property
    @jsii.member(jsii_name="attrDomainStatus")
    def attr_domain_status(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DomainStatus
        """
        return jsii.get(self, "attrDomainStatus")

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: StatusReason
        """
        return jsii.get(self, "attrStatusReason")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> str:
        """``AWS::Amplify::Domain.AppId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-appid
        """
        return jsii.get(self, "appId")

    @app_id.setter
    def app_id(self, value: str):
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """``AWS::Amplify::Domain.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-domainname
        """
        return jsii.get(self, "domainName")

    @domain_name.setter
    def domain_name(self, value: str):
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="subDomainSettings")
    def sub_domain_settings(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "SubDomainSettingProperty"]]]:
        """``AWS::Amplify::Domain.SubDomainSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-subdomainsettings
        """
        return jsii.get(self, "subDomainSettings")

    @sub_domain_settings.setter
    def sub_domain_settings(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "SubDomainSettingProperty"]]]):
        jsii.set(self, "subDomainSettings", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnDomain.SubDomainSettingProperty", jsii_struct_bases=[], name_mapping={'branch_name': 'branchName', 'prefix': 'prefix'})
    class SubDomainSettingProperty():
        def __init__(self, *, branch_name: str, prefix: str):
            """
            :param branch_name: ``CfnDomain.SubDomainSettingProperty.BranchName``.
            :param prefix: ``CfnDomain.SubDomainSettingProperty.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html
            """
            self._values = {
                'branch_name': branch_name,
                'prefix': prefix,
            }

        @builtins.property
        def branch_name(self) -> str:
            """``CfnDomain.SubDomainSettingProperty.BranchName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-branchname
            """
            return self._values.get('branch_name')

        @builtins.property
        def prefix(self) -> str:
            """``CfnDomain.SubDomainSettingProperty.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-prefix
            """
            return self._values.get('prefix')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SubDomainSettingProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-amplify.CfnDomainProps", jsii_struct_bases=[], name_mapping={'app_id': 'appId', 'domain_name': 'domainName', 'sub_domain_settings': 'subDomainSettings'})
class CfnDomainProps():
    def __init__(self, *, app_id: str, domain_name: str, sub_domain_settings: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SubDomainSettingProperty"]]]):
        """Properties for defining a ``AWS::Amplify::Domain``.

        :param app_id: ``AWS::Amplify::Domain.AppId``.
        :param domain_name: ``AWS::Amplify::Domain.DomainName``.
        :param sub_domain_settings: ``AWS::Amplify::Domain.SubDomainSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html
        """
        self._values = {
            'app_id': app_id,
            'domain_name': domain_name,
            'sub_domain_settings': sub_domain_settings,
        }

    @builtins.property
    def app_id(self) -> str:
        """``AWS::Amplify::Domain.AppId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-appid
        """
        return self._values.get('app_id')

    @builtins.property
    def domain_name(self) -> str:
        """``AWS::Amplify::Domain.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-domainname
        """
        return self._values.get('domain_name')

    @builtins.property
    def sub_domain_settings(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SubDomainSettingProperty"]]]:
        """``AWS::Amplify::Domain.SubDomainSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-subdomainsettings
        """
        return self._values.get('sub_domain_settings')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDomainProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnApp", "CfnAppProps", "CfnBranch", "CfnBranchProps", "CfnDomain", "CfnDomainProps", "__jsii_assembly__"]

publication.publish()
