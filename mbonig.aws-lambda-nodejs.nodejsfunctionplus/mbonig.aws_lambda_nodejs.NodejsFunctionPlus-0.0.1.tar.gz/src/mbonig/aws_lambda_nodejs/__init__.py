"""
## Matt's Lambda Node.js Library

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

This library provides constructs for Node.js Lambda functions. Well, ok, so AWS already does that with the [@aws-cdk/aws-lambda-nodejs](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-lambda-nodejs-readme.html) package.

All this CDK construct does it expose the same `NodejsFunction` construct as that other package, but I set the `AWS_NODEJS_CONNECTION_REUSE_ENABLED` for you. Why? Because it's a super great environment flag built into the AWS SDK which [enables http keep-alive](https://theburningmonk.com/2019/02/lambda-optimization-tip-enable-http-keep-alive/), and greatly improves performance.

## Usage

This is a drop-in replacement:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# import {NodejsFunction} from '@aws-cdk/aws-lambda-nodejs';
from nodejsfunction_plus import NodejsFunction

NodejsFunction(self, "whatever")
```

## Contributing

Just submit a PR.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_lambda
import aws_cdk.aws_lambda_nodejs
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("nodejsfunction-plus", "0.0.1", __name__, "nodejsfunction-plus@0.0.1.jsii.tgz")


class NodejsFunction(aws_cdk.aws_lambda_nodejs.NodejsFunction, metaclass=jsii.JSIIMeta, jsii_type="nodejsfunction-plus.NodejsFunction"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, build_dir: typing.Optional[str]=None, cache_dir: typing.Optional[str]=None, entry: typing.Optional[str]=None, handler: typing.Optional[str]=None, minify: typing.Optional[bool]=None, runtime: typing.Optional[aws_cdk.aws_lambda.Runtime]=None, source_maps: typing.Optional[bool]=None, allow_all_outbound: typing.Optional[bool]=None, dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue]=None, dead_letter_queue_enabled: typing.Optional[bool]=None, description: typing.Optional[str]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, events: typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]]=None, function_name: typing.Optional[str]=None, initial_policy: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]=None, layers: typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]]=None, log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays]=None, log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, memory_size: typing.Optional[jsii.Number]=None, reserved_concurrent_executions: typing.Optional[jsii.Number]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, security_groups: typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None, tracing: typing.Optional[aws_cdk.aws_lambda.Tracing]=None, vpc: typing.Optional[aws_cdk.aws_ec2.IVpc]=None, vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, max_event_age: typing.Optional[aws_cdk.core.Duration]=None, on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination]=None, on_success: typing.Optional[aws_cdk.aws_lambda.IDestination]=None, retry_attempts: typing.Optional[jsii.Number]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param build_dir: The build directory. Default: - ``.build`` in the entry file directory
        :param cache_dir: The cache directory. Parcel uses a filesystem cache for fast rebuilds. Default: - ``.cache`` in the root directory
        :param entry: Path to the entry file (JavaScript or TypeScript). Default: - Derived from the name of the defining file and the construct's id. If the ``NodejsFunction`` is defined in ``stack.ts`` with ``my-handler`` as id (``new NodejsFunction(this, 'my-handler')``), the construct will look at ``stack.my-handler.ts`` and ``stack.my-handler.js``.
        :param handler: The name of the exported handler in the entry file. Default: handler
        :param minify: Whether to minify files when bundling. Default: false
        :param runtime: The runtime environment. Only runtimes of the Node.js family are supported. Default: - ``NODEJS_12_X`` if ``process.versions.node`` >= '12.0.0', ``NODEJS_10_X`` otherwise.
        :param source_maps: Whether to include source maps when bundling. Default: false
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - Private subnets.
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        """
        props = aws_cdk.aws_lambda_nodejs.NodejsFunctionProps(build_dir=build_dir, cache_dir=cache_dir, entry=entry, handler=handler, minify=minify, runtime=runtime, source_maps=source_maps, allow_all_outbound=allow_all_outbound, dead_letter_queue=dead_letter_queue, dead_letter_queue_enabled=dead_letter_queue_enabled, description=description, environment=environment, events=events, function_name=function_name, initial_policy=initial_policy, layers=layers, log_retention=log_retention, log_retention_role=log_retention_role, memory_size=memory_size, reserved_concurrent_executions=reserved_concurrent_executions, role=role, security_group=security_group, security_groups=security_groups, timeout=timeout, tracing=tracing, vpc=vpc, vpc_subnets=vpc_subnets, max_event_age=max_event_age, on_failure=on_failure, on_success=on_success, retry_attempts=retry_attempts)

        jsii.create(NodejsFunction, self, [scope, id, props])


__all__ = ["NodejsFunction", "__jsii_assembly__"]

publication.publish()
