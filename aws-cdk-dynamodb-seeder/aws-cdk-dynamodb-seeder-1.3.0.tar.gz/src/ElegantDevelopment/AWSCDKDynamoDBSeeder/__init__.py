"""
# aws-cdk-dynamodb-seeder [![Mentioned in Awesome CDK](https://awesome.re/mentioned-badge.svg)](https://github.com/eladb/awesome-cdk)

![Node.js CI](https://github.com/elegantdevelopment/aws-cdk-dynamodb-seeder/workflows/Node.js%20CI/badge.svg)
[![codecov](https://codecov.io/gh/elegantdevelopment/aws-cdk-dynamodb-seeder/branch/master/graph/badge.svg)](https://codecov.io/gh/elegantdevelopment/aws-cdk-dynamodb-seeder)
[![npm version](https://badge.fury.io/js/aws-cdk-dynamodb-seeder.svg)](https://badge.fury.io/js/aws-cdk-dynamodb-seeder)
[![dependencies Status](https://david-dm.org/elegantdevelopment/aws-cdk-dynamodb-seeder/status.svg)](https://david-dm.org/elegantdevelopment/aws-cdk-dynamodb-seeder)
[![npm](https://img.shields.io/npm/dt/aws-cdk-dynamodb-seeder)](https://www.npmjs.com/package/aws-cdk-dynamodb-seeder)

A simple CDK JSON seeder for DynamoDB

## Why this package

Glad you asked!

Using [AWS CDK](https://aws.amazon.com/cdk) for automating infrastructure deployments is an amazing way of integrating the development and operations into one process and one codebase.

However, building dev or test environments that come pre-populated with data can be tricky, especially when using [Amazon DynamoDB](https://aws.amazon.com/dynamodb).

## How do I use it

Install using your favourite package manager:

```sh
yarn add aws-cdk-dynamodb-seeder
```

### Example usage

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk_dynamodb_seeder import Seeder
my_table = Table(stack, "MyTable",
    table_name="MyTable",
    partition_key={"name": "Id", "type": AttributeType.STRING}
)
Seeder(stack, "MySeeder",
    table=my_table,
    table_name="MyTable",
    setup=require("./items-to-put.json"),
    teardown=require("./keys-to-delete.json"),
    refresh_on_update=True
)
```

For a more in-depth example, see: [elegantdevelopment/aws-cdk-dynamodb-seeder-examples](https://github.com/elegantdevelopment/aws-cdk-dynamodb-seeder-examples).

### Importing seed data

Data passed into `setup` ("Items" to put) or `teardown` ("Keys" to delete) should be an `array` of JavaScript objects (that are, in turn, representations of `string` to [AttributeValue](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeValue.html) maps).

* `setup` elements should use the format of `params.Item` from [AWS.DynamoDB.DocumentClient.put()](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#put-property)
* `teardown` elements should use the format of `params.Key` from [AWS.DynamoDB.DocumentClient.delete()](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#delete-property)

## Internals

Behind the scenes we use an [AwsCustomResource](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/custom-resources/awscustomresource.html) as a representation of the related table's seed state. The custom resource's event handlers invoke a [Function](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/aws-lambda/function.html#aws_lambda_Function) to perform setup and/or teardown actions.

### Deploying a stack

On deployment, we write copies of your seed data locally and use a [BucketDeployment](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/aws-s3-deployment/bucketdeployment.html#aws_s3_deployment_BucketDeployment) to write it to an S3 [Bucket](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/aws-s3/bucket.html#aws_s3_Bucket).

We then create the handler function and custom resource to field seed requests (the `onCreate` event will immediate fire as the stack deploys, reading the data from the bucket and seeding the table using [AWS.DynamoDB.DocumentClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html)).

### Updating a stack

On a stack update, the `onUpdate` handler is triggered when `Seeder.props.refreshOnUpdate` is `true`.

This will run [AWS.DynamoDB.DocumentClient.delete()](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#delete-property) on every teardown "Key" followed by [AWS.DynamoDB.DocumentClient.put()](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#put-property) on every setup "Item".

### Destroying a stack

When the stack is destroyed, the event handler's `onDelete` function will be invoked, providing `Seeder.props.teardown` is set.

This simply runs [AWS.DynamoDB.DocumentClient.delete()](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#delete-property) on every teardown "Key" before destroying the `Seeder`'s resources.

<!-- Internals -->
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_dynamodb
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.aws_s3_deployment
import aws_cdk.core
import aws_cdk.custom_resources

__jsii_assembly__ = jsii.JSIIAssembly.load("aws-cdk-dynamodb-seeder", "1.3.0", __name__, "aws-cdk-dynamodb-seeder@1.3.0.jsii.tgz")


@jsii.data_type(jsii_type="aws-cdk-dynamodb-seeder.Item", jsii_struct_bases=[], name_mapping={})
class Item():
    def __init__(self):
        """
        stability
        :stability: experimental
        """
        self._values = {
        }

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Item(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="aws-cdk-dynamodb-seeder.ItemKey", jsii_struct_bases=[], name_mapping={})
class ItemKey():
    def __init__(self):
        """
        stability
        :stability: experimental
        """
        self._values = {
        }

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ItemKey(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="aws-cdk-dynamodb-seeder.Props", jsii_struct_bases=[], name_mapping={'setup': 'setup', 'table': 'table', 'table_name': 'tableName', 'refresh_on_update': 'refreshOnUpdate', 'teardown': 'teardown'})
class Props():
    def __init__(self, *, setup: typing.List["Item"], table: aws_cdk.aws_dynamodb.Table, table_name: str, refresh_on_update: typing.Optional[bool]=None, teardown: typing.Optional[typing.List["ItemKey"]]=None):
        """
        :param setup: 
        :param table: 
        :param table_name: 
        :param refresh_on_update: 
        :param teardown: 

        stability
        :stability: experimental
        """
        self._values = {
            'setup': setup,
            'table': table,
            'table_name': table_name,
        }
        if refresh_on_update is not None: self._values["refresh_on_update"] = refresh_on_update
        if teardown is not None: self._values["teardown"] = teardown

    @builtins.property
    def setup(self) -> typing.List["Item"]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('setup')

    @builtins.property
    def table(self) -> aws_cdk.aws_dynamodb.Table:
        """
        stability
        :stability: experimental
        """
        return self._values.get('table')

    @builtins.property
    def table_name(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('table_name')

    @builtins.property
    def refresh_on_update(self) -> typing.Optional[bool]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('refresh_on_update')

    @builtins.property
    def teardown(self) -> typing.Optional[typing.List["ItemKey"]]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('teardown')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Props(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Seeder(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-dynamodb-seeder.Seeder"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, setup: typing.List["Item"], table: aws_cdk.aws_dynamodb.Table, table_name: str, refresh_on_update: typing.Optional[bool]=None, teardown: typing.Optional[typing.List["ItemKey"]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param setup: 
        :param table: 
        :param table_name: 
        :param refresh_on_update: 
        :param teardown: 

        stability
        :stability: experimental
        """
        props = Props(setup=setup, table=table, table_name=table_name, refresh_on_update=refresh_on_update, teardown=teardown)

        jsii.create(Seeder, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="props")
    def _props(self) -> "Props":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "props")

    @_props.setter
    def _props(self, value: "Props"):
        jsii.set(self, "props", value)


__all__ = ["Item", "ItemKey", "Props", "Seeder", "__jsii_assembly__"]

publication.publish()
