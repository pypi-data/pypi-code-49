"""
# build

build packages

```
npm run all
```

# cicd pipeline stack

cicd:deploy
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_codebuild
import aws_cdk.aws_codecommit
import aws_cdk.aws_events
import aws_cdk.aws_events_targets
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-pull-request-builder", "0.2.0", __name__, "cdk-pull-request-builder@0.2.0.jsii.tgz")


@jsii.data_type(jsii_type="cdk-pull-request-builder.BuildFailureEmailProps", jsii_struct_bases=[], name_mapping={'source_email_param': 'sourceEmailParam', 'notification_email_param': 'notificationEmailParam'})
class BuildFailureEmailProps():
    def __init__(self, *, source_email_param: str, notification_email_param: typing.Optional[str]=None):
        """
        :param source_email_param: 
        :param notification_email_param: 
        """
        self._values = {
            'source_email_param': source_email_param,
        }
        if notification_email_param is not None: self._values["notification_email_param"] = notification_email_param

    @builtins.property
    def source_email_param(self) -> str:
        return self._values.get('source_email_param')

    @builtins.property
    def notification_email_param(self) -> typing.Optional[str]:
        return self._values.get('notification_email_param')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'BuildFailureEmailProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-pull-request-builder.CommonFunctionProps", jsii_struct_bases=[], name_mapping={'code': 'code', 'role': 'role', 'runtime': 'runtime'})
class CommonFunctionProps():
    def __init__(self, *, code: aws_cdk.aws_lambda.Code, role: aws_cdk.aws_iam.Role, runtime: aws_cdk.aws_lambda.Runtime):
        """
        :param code: 
        :param role: 
        :param runtime: 
        """
        self._values = {
            'code': code,
            'role': role,
            'runtime': runtime,
        }

    @builtins.property
    def code(self) -> aws_cdk.aws_lambda.Code:
        return self._values.get('code')

    @builtins.property
    def role(self) -> aws_cdk.aws_iam.Role:
        return self._values.get('role')

    @builtins.property
    def runtime(self) -> aws_cdk.aws_lambda.Runtime:
        return self._values.get('runtime')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CommonFunctionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class PullRequestBuilder(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-pull-request-builder.PullRequestBuilder"):
    """CDK PullRequestBuilder.

    Implements an event-driven workflow using
    CodeBuild, CodeCommit, CloudWatchEvents,
    CloudWatchLogs, and Lambda to achieve a basic
    automated test cycle for pull requests.

    CodeBuild is started when a pull request is opened
    or updated. The PR is updated with comments as
    the build changes its state.

    Optionally, the job can enforce an approval rule on
    the PR by configuring PullRequestBuilderProps.enforceApproval
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, enforce_approval: bool, project: aws_cdk.aws_codebuild.Project, repo: aws_cdk.aws_codecommit.Repository, build_failure_email_settings: typing.Optional["BuildFailureEmailProps"]=None, lambda_role: typing.Optional[aws_cdk.aws_iam.Role]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param enforce_approval: 
        :param project: 
        :param repo: 
        :param build_failure_email_settings: 
        :param lambda_role: 
        """
        props = PullRequestBuilderProps(enforce_approval=enforce_approval, project=project, repo=repo, build_failure_email_settings=build_failure_email_settings, lambda_role=lambda_role)

        jsii.create(PullRequestBuilder, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-pull-request-builder.PullRequestBuilderProps", jsii_struct_bases=[], name_mapping={'enforce_approval': 'enforceApproval', 'project': 'project', 'repo': 'repo', 'build_failure_email_settings': 'buildFailureEmailSettings', 'lambda_role': 'lambdaRole'})
class PullRequestBuilderProps():
    def __init__(self, *, enforce_approval: bool, project: aws_cdk.aws_codebuild.Project, repo: aws_cdk.aws_codecommit.Repository, build_failure_email_settings: typing.Optional["BuildFailureEmailProps"]=None, lambda_role: typing.Optional[aws_cdk.aws_iam.Role]=None):
        """
        :param enforce_approval: 
        :param project: 
        :param repo: 
        :param build_failure_email_settings: 
        :param lambda_role: 
        """
        if isinstance(build_failure_email_settings, dict): build_failure_email_settings = BuildFailureEmailProps(**build_failure_email_settings)
        self._values = {
            'enforce_approval': enforce_approval,
            'project': project,
            'repo': repo,
        }
        if build_failure_email_settings is not None: self._values["build_failure_email_settings"] = build_failure_email_settings
        if lambda_role is not None: self._values["lambda_role"] = lambda_role

    @builtins.property
    def enforce_approval(self) -> bool:
        return self._values.get('enforce_approval')

    @builtins.property
    def project(self) -> aws_cdk.aws_codebuild.Project:
        return self._values.get('project')

    @builtins.property
    def repo(self) -> aws_cdk.aws_codecommit.Repository:
        return self._values.get('repo')

    @builtins.property
    def build_failure_email_settings(self) -> typing.Optional["BuildFailureEmailProps"]:
        return self._values.get('build_failure_email_settings')

    @builtins.property
    def lambda_role(self) -> typing.Optional[aws_cdk.aws_iam.Role]:
        return self._values.get('lambda_role')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PullRequestBuilderProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["BuildFailureEmailProps", "CommonFunctionProps", "PullRequestBuilder", "PullRequestBuilderProps", "__jsii_assembly__"]

publication.publish()
