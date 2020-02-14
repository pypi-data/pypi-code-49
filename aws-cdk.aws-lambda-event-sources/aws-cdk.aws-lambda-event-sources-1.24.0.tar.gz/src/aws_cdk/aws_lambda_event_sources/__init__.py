"""
## AWS Lambda Event Sources

<!--BEGIN STABILITY BANNER-->---


![Stability: Stable](https://img.shields.io/badge/stability-Stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module includes classes that allow using various AWS services as event
sources for AWS Lambda via the high-level `lambda.addEventSource(source)` API.

NOTE: In most cases, it is also possible to use the resource APIs to invoke an
AWS Lambda function. This library provides a uniform API for all Lambda event
sources regardless of the underlying mechanism they use.

### SQS

Amazon Simple Queue Service (Amazon SQS) allows you to build asynchronous
workflows. For more information about Amazon SQS, see Amazon Simple Queue
Service. You can configure AWS Lambda to poll for these messages as they arrive
and then pass the event to a Lambda function invocation. To view a sample event,
see [Amazon SQS Event](https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html#eventsources-sqs).

To set up Amazon Simple Queue Service as an event source for AWS Lambda, you
first create or update an Amazon SQS queue and select custom values for the
queue parameters. The following parameters will impact Amazon SQS's polling
behavior:

* **visibilityTimeout**: May impact the period between retries.
* **receiveMessageWaitTime**: Will determine [long
  poll](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html)
  duration. The default value is 20 seconds.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sqs as sqs
from aws_cdk.aws_lambda_event_sources import SqsEventSource
from aws_cdk.core import Duration

queue = sqs.Queue(self, "MyQueue",
    visibility_timeout=Duration.seconds(30), # default,
    receive_message_wait_time=Duration.seconds(20)
)

lambda.add_event_source(SqsEventSource(queue,
    batch_size=10
))
```

### S3

You can write Lambda functions to process S3 bucket events, such as the
object-created or object-deleted events. For example, when a user uploads a
photo to a bucket, you might want Amazon S3 to invoke your Lambda function so
that it reads the image and creates a thumbnail for the photo.

You can use the bucket notification configuration feature in Amazon S3 to
configure the event source mapping, identifying the bucket events that you want
Amazon S3 to publish and which Lambda function to invoke.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_s3 as s3
from aws_cdk.aws_lambda_event_sources import S3EventSource

bucket = s3.Bucket(...)

lambda.add_event_source(S3EventSource(bucket,
    events=[s3.EventType.OBJECT_CREATED, s3.EventType.OBJECT_REMOVED],
    filters=[NotificationKeyFilter(prefix="subdir/")]
))
```

### SNS

You can write Lambda functions to process Amazon Simple Notification Service
notifications. When a message is published to an Amazon SNS topic, the service
can invoke your Lambda function by passing the message payload as a parameter.
Your Lambda function code can then process the event, for example publish the
message to other Amazon SNS topics, or send the message to other AWS services.

This also enables you to trigger a Lambda function in response to Amazon
CloudWatch alarms and other AWS services that use Amazon SNS.

For an example event, see [Appendix: Message and JSON
Formats](https://docs.aws.amazon.com/sns/latest/dg/json-formats.html) and
[Amazon SNS Sample
Event](https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html#eventsources-sns).
For an example use case, see [Using AWS Lambda with Amazon SNS from Different
Accounts](https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html).

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sns as sns
from aws_cdk.aws_lambda_event_sources import SnsEventSource

topic = sns.Topic(...)

lambda.add_event_source(SnsEventSource(topic))
```

When a user calls the SNS Publish API on a topic that your Lambda function is
subscribed to, Amazon SNS will call Lambda to invoke your function
asynchronously. Lambda will then return a delivery status. If there was an error
calling Lambda, Amazon SNS will retry invoking the Lambda function up to three
times. After three tries, if Amazon SNS still could not successfully invoke the
Lambda function, then Amazon SNS will send a delivery status failure message to
CloudWatch.

### DynamoDB Streams

You can write Lambda functions to process change events from a DynamoDB Table. An event is emitted to a DynamoDB stream (if configured) whenever a write (Put, Delete, Update)
operation is performed against the table. See [Using AWS Lambda with Amazon DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html) for more information.

To process events with a Lambda function, first create or update a DynamoDB table and enable a `stream` specification. Then, create a `DynamoEventSource`
and add it to your Lambda function. The following parameters will impact Amazon DynamoDB's polling behavior:

* **batchSize**: Determines how many records are buffered before invoking your lambda function - could impact your function's memory usage (if too high) and ability to keep up with incoming data velocity (if too low).
* **startingPosition**: Will determine where to being consumption, either at the most recent ('LATEST') record or the oldest record ('TRIM_HORIZON'). 'TRIM_HORIZON' will ensure you process all available data, while 'LATEST' will ignore all reocrds that arrived prior to attaching the event source.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_lambda as lambda
from aws_cdk.aws_lambda_event_sources import DynamoEventSource

table = dynamodb.Table(...,
    partition_key=, ...,
    stream=dynamodb.StreamViewType.NEW_IMAGE
)def ():
    passlambda.Function(...)
def ():
    passadd_event_source(DynamoEventSource(table,
    starting_position=lambda.StartingPosition.TRIM_HORIZON
))
```

### Kinesis

You can write Lambda functions to process streaming data in Amazon Kinesis Streams. For more information about Amazon SQS, see [Amazon Kinesis
Service](https://aws.amazon.com/kinesis/data-streams/). To view a sample event,
see [Amazon SQS Event](https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html#eventsources-kinesis-streams).

To set up Amazon Kinesis as an event source for AWS Lambda, you
first create or update an Amazon Kinesis stream and select custom values for the
event source parameters. The following parameters will impact Amazon Kinesis's polling
behavior:

* **batchSize**: Determines how many records are buffered before invoking your lambnda function - could impact your function's memory usage (if too high) and ability to keep up with incoming data velocity (if too low).
* **startingPosition**: Will determine where to being consumption, either at the most recent ('LATEST') record or the oldest record ('TRIM_HORIZON'). 'TRIM_HORIZON' will ensure you process all available data, while 'LATEST' will ignore all reocrds that arrived prior to attaching the event source.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lambda as lambda
import aws_cdk.aws_kinesis as kinesis
from aws_cdk.aws_lambda_event_sources import KinesisEventSource

stream = kinesis.Stream(self, "MyStream")

my_function.add_event_source(KinesisEventSource(queue,
    batch_size=100, # default
    starting_position=lambda.StartingPosition.TRIM_HORIZON
))
```

## Roadmap

Eventually, this module will support all the event sources described under
[Supported Event
Sources](https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html)
in the AWS Lambda Developer Guide.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_apigateway
import aws_cdk.aws_dynamodb
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_kinesis
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.aws_s3_notifications
import aws_cdk.aws_sns
import aws_cdk.aws_sns_subscriptions
import aws_cdk.aws_sqs
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-lambda-event-sources", "1.24.0", __name__, "aws-lambda-event-sources@1.24.0.jsii.tgz")


@jsii.implements(aws_cdk.aws_lambda.IEventSource)
class ApiEventSource(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-event-sources.ApiEventSource"):
    def __init__(self, method: str, path: str, *, api_key_required: typing.Optional[bool]=None, authorization_type: typing.Optional[aws_cdk.aws_apigateway.AuthorizationType]=None, authorizer: typing.Optional[aws_cdk.aws_apigateway.IAuthorizer]=None, method_responses: typing.Optional[typing.List[aws_cdk.aws_apigateway.MethodResponse]]=None, operation_name: typing.Optional[str]=None, request_models: typing.Optional[typing.Mapping[str,aws_cdk.aws_apigateway.IModel]]=None, request_parameters: typing.Optional[typing.Mapping[str,bool]]=None, request_validator: typing.Optional[aws_cdk.aws_apigateway.IRequestValidator]=None) -> None:
        """
        :param method: -
        :param path: -
        :param api_key_required: Indicates whether the method requires clients to submit a valid API key. Default: false
        :param authorization_type: Method authorization. If the value is set of ``Custom``, an ``authorizer`` must also be specified. If you're using one of the authorizers that are available via the {@link Authorizer} class, such as {@link Authorizer#token()}, it is recommended that this option not be specified. The authorizer will take care of setting the correct authorization type. However, specifying an authorization type using this property that conflicts with what is expected by the {@link Authorizer} will result in an error. Default: - open access unless ``authorizer`` is specified
        :param authorizer: If ``authorizationType`` is ``Custom``, this specifies the ID of the method authorizer resource. If specified, the value of ``authorizationType`` must be set to ``Custom``
        :param method_responses: The responses that can be sent to the client who calls the method. Default: None This property is not required, but if these are not supplied for a Lambda proxy integration, the Lambda function must return a value of the correct format, for the integration response to be correctly mapped to a response to the client.
        :param operation_name: A friendly operation name for the method. For example, you can assign the OperationName of ListPets for the GET /pets method.
        :param request_models: The resources that are used for the response's content type. Specify request models as key-value pairs (string-to-string mapping), with a content type as the key and a Model resource name as the value
        :param request_parameters: The request parameters that API Gateway accepts. Specify request parameters as key-value pairs (string-to-Boolean mapping), with a source as the key and a Boolean as the value. The Boolean specifies whether a parameter is required. A source must match the format method.request.location.name, where the location is querystring, path, or header, and name is a valid, unique parameter name. Default: None
        :param request_validator: The ID of the associated request validator.
        """
        options = aws_cdk.aws_apigateway.MethodOptions(api_key_required=api_key_required, authorization_type=authorization_type, authorizer=authorizer, method_responses=method_responses, operation_name=operation_name, request_models=request_models, request_parameters=request_parameters, request_validator=request_validator)

        jsii.create(ApiEventSource, self, [method, path, options])

    @jsii.member(jsii_name="bind")
    def bind(self, target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: -
        """
        return jsii.invoke(self, "bind", [target])


@jsii.implements(aws_cdk.aws_lambda.IEventSource)
class S3EventSource(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-event-sources.S3EventSource"):
    """Use S3 bucket notifications as an event source for AWS Lambda."""
    def __init__(self, bucket: aws_cdk.aws_s3.Bucket, *, events: typing.List[aws_cdk.aws_s3.EventType], filters: typing.Optional[typing.List[aws_cdk.aws_s3.NotificationKeyFilter]]=None) -> None:
        """
        :param bucket: -
        :param events: The s3 event types that will trigger the notification.
        :param filters: S3 object key filter rules to determine which objects trigger this event. Each filter must include a ``prefix`` and/or ``suffix`` that will be matched against the s3 object key. Refer to the S3 Developer Guide for details about allowed filter rules.
        """
        props = S3EventSourceProps(events=events, filters=filters)

        jsii.create(S3EventSource, self, [bucket, props])

    @jsii.member(jsii_name="bind")
    def bind(self, target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: -
        """
        return jsii.invoke(self, "bind", [target])

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> aws_cdk.aws_s3.Bucket:
        return jsii.get(self, "bucket")


@jsii.data_type(jsii_type="@aws-cdk/aws-lambda-event-sources.S3EventSourceProps", jsii_struct_bases=[], name_mapping={'events': 'events', 'filters': 'filters'})
class S3EventSourceProps():
    def __init__(self, *, events: typing.List[aws_cdk.aws_s3.EventType], filters: typing.Optional[typing.List[aws_cdk.aws_s3.NotificationKeyFilter]]=None):
        """
        :param events: The s3 event types that will trigger the notification.
        :param filters: S3 object key filter rules to determine which objects trigger this event. Each filter must include a ``prefix`` and/or ``suffix`` that will be matched against the s3 object key. Refer to the S3 Developer Guide for details about allowed filter rules.
        """
        self._values = {
            'events': events,
        }
        if filters is not None: self._values["filters"] = filters

    @builtins.property
    def events(self) -> typing.List[aws_cdk.aws_s3.EventType]:
        """The s3 event types that will trigger the notification."""
        return self._values.get('events')

    @builtins.property
    def filters(self) -> typing.Optional[typing.List[aws_cdk.aws_s3.NotificationKeyFilter]]:
        """S3 object key filter rules to determine which objects trigger this event.

        Each filter must include a ``prefix`` and/or ``suffix`` that will be matched
        against the s3 object key. Refer to the S3 Developer Guide for details
        about allowed filter rules.
        """
        return self._values.get('filters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'S3EventSourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_lambda.IEventSource)
class SnsEventSource(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-event-sources.SnsEventSource"):
    """Use an Amazon SNS topic as an event source for AWS Lambda."""
    def __init__(self, topic: aws_cdk.aws_sns.ITopic) -> None:
        """
        :param topic: -
        """
        jsii.create(SnsEventSource, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(self, target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: -
        """
        return jsii.invoke(self, "bind", [target])

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> aws_cdk.aws_sns.ITopic:
        return jsii.get(self, "topic")


@jsii.implements(aws_cdk.aws_lambda.IEventSource)
class SqsEventSource(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-event-sources.SqsEventSource"):
    """Use an Amazon SQS queue as an event source for AWS Lambda."""
    def __init__(self, queue: aws_cdk.aws_sqs.IQueue, *, batch_size: typing.Optional[jsii.Number]=None) -> None:
        """
        :param queue: -
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10. Default: 10
        """
        props = SqsEventSourceProps(batch_size=batch_size)

        jsii.create(SqsEventSource, self, [queue, props])

    @jsii.member(jsii_name="bind")
    def bind(self, target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: -
        """
        return jsii.invoke(self, "bind", [target])

    @builtins.property
    @jsii.member(jsii_name="queue")
    def queue(self) -> aws_cdk.aws_sqs.IQueue:
        return jsii.get(self, "queue")


@jsii.data_type(jsii_type="@aws-cdk/aws-lambda-event-sources.SqsEventSourceProps", jsii_struct_bases=[], name_mapping={'batch_size': 'batchSize'})
class SqsEventSourceProps():
    def __init__(self, *, batch_size: typing.Optional[jsii.Number]=None):
        """
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10. Default: 10
        """
        self._values = {
        }
        if batch_size is not None: self._values["batch_size"] = batch_size

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.

        Your function receives an
        event with all the retrieved records.

        Valid Range: Minimum value of 1. Maximum value of 10.

        default
        :default: 10
        """
        return self._values.get('batch_size')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SqsEventSourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_lambda.IEventSource)
class StreamEventSource(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-lambda-event-sources.StreamEventSource"):
    """Use an stream as an event source for AWS Lambda."""
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _StreamEventSourceProxy

    def __init__(self, *, starting_position: aws_cdk.aws_lambda.StartingPosition, batch_size: typing.Optional[jsii.Number]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        :param starting_position: Where to begin consuming the stream.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: - Minimum value of 1 - Maximum value of: - 1000 for {@link DynamoEventSource} - 10000 for {@link KinesisEventSource} Default: 100
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        """
        props = StreamEventSourceProps(starting_position=starting_position, batch_size=batch_size, max_batching_window=max_batching_window)

        jsii.create(StreamEventSource, self, [props])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, _target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param _target: -
        """
        ...

    @jsii.member(jsii_name="enrichMappingOptions")
    def _enrich_mapping_options(self, *, event_source_arn: str, batch_size: typing.Optional[jsii.Number]=None, enabled: typing.Optional[bool]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None, starting_position: typing.Optional[aws_cdk.aws_lambda.StartingPosition]=None) -> aws_cdk.aws_lambda.EventSourceMappingOptions:
        """
        :param event_source_arn: The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis and Amazon DynamoDB is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        :param enabled: Set to false to disable the event source upon creation. Default: true
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param starting_position: The position in the DynamoDB or Kinesis stream where AWS Lambda should start reading. Default: - Required for Amazon Kinesis and Amazon DynamoDB Streams sources.
        """
        options = aws_cdk.aws_lambda.EventSourceMappingOptions(event_source_arn=event_source_arn, batch_size=batch_size, enabled=enabled, max_batching_window=max_batching_window, starting_position=starting_position)

        return jsii.invoke(self, "enrichMappingOptions", [options])

    @builtins.property
    @jsii.member(jsii_name="props")
    def _props(self) -> "StreamEventSourceProps":
        return jsii.get(self, "props")


class _StreamEventSourceProxy(StreamEventSource):
    @jsii.member(jsii_name="bind")
    def bind(self, _target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param _target: -
        """
        return jsii.invoke(self, "bind", [_target])


class DynamoEventSource(StreamEventSource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-event-sources.DynamoEventSource"):
    """Use an Amazon DynamoDB stream as an event source for AWS Lambda."""
    def __init__(self, table: aws_cdk.aws_dynamodb.Table, *, starting_position: aws_cdk.aws_lambda.StartingPosition, batch_size: typing.Optional[jsii.Number]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        :param table: -
        :param starting_position: Where to begin consuming the stream.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: - Minimum value of 1 - Maximum value of: - 1000 for {@link DynamoEventSource} - 10000 for {@link KinesisEventSource} Default: 100
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        """
        props = DynamoEventSourceProps(starting_position=starting_position, batch_size=batch_size, max_batching_window=max_batching_window)

        jsii.create(DynamoEventSource, self, [table, props])

    @jsii.member(jsii_name="bind")
    def bind(self, target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: -
        """
        return jsii.invoke(self, "bind", [target])


class KinesisEventSource(StreamEventSource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-event-sources.KinesisEventSource"):
    """Use an Amazon Kinesis stream as an event source for AWS Lambda."""
    def __init__(self, stream: aws_cdk.aws_kinesis.IStream, *, starting_position: aws_cdk.aws_lambda.StartingPosition, batch_size: typing.Optional[jsii.Number]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        :param stream: -
        :param starting_position: Where to begin consuming the stream.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: - Minimum value of 1 - Maximum value of: - 1000 for {@link DynamoEventSource} - 10000 for {@link KinesisEventSource} Default: 100
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        """
        props = KinesisEventSourceProps(starting_position=starting_position, batch_size=batch_size, max_batching_window=max_batching_window)

        jsii.create(KinesisEventSource, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(self, target: aws_cdk.aws_lambda.IFunction) -> None:
        """Called by ``lambda.addEventSource`` to allow the event source to bind to this function.

        :param target: -
        """
        return jsii.invoke(self, "bind", [target])

    @builtins.property
    @jsii.member(jsii_name="stream")
    def stream(self) -> aws_cdk.aws_kinesis.IStream:
        return jsii.get(self, "stream")


@jsii.data_type(jsii_type="@aws-cdk/aws-lambda-event-sources.StreamEventSourceProps", jsii_struct_bases=[], name_mapping={'starting_position': 'startingPosition', 'batch_size': 'batchSize', 'max_batching_window': 'maxBatchingWindow'})
class StreamEventSourceProps():
    def __init__(self, *, starting_position: aws_cdk.aws_lambda.StartingPosition, batch_size: typing.Optional[jsii.Number]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None):
        """The set of properties for event sources that follow the streaming model, such as, Dynamo and Kinesis.

        :param starting_position: Where to begin consuming the stream.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: - Minimum value of 1 - Maximum value of: - 1000 for {@link DynamoEventSource} - 10000 for {@link KinesisEventSource} Default: 100
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        """
        self._values = {
            'starting_position': starting_position,
        }
        if batch_size is not None: self._values["batch_size"] = batch_size
        if max_batching_window is not None: self._values["max_batching_window"] = max_batching_window

    @builtins.property
    def starting_position(self) -> aws_cdk.aws_lambda.StartingPosition:
        """Where to begin consuming the stream."""
        return self._values.get('starting_position')

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.

        Your function receives an
        event with all the retrieved records.

        Valid Range:

        - Minimum value of 1
        - Maximum value of:

          - 1000 for {@link DynamoEventSource}
          - 10000 for {@link KinesisEventSource}

        default
        :default: 100
        """
        return self._values.get('batch_size')

    @builtins.property
    def max_batching_window(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The maximum amount of time to gather records before invoking the function.

        Maximum of Duration.minutes(5)

        default
        :default: Duration.seconds(0)
        """
        return self._values.get('max_batching_window')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StreamEventSourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-lambda-event-sources.DynamoEventSourceProps", jsii_struct_bases=[StreamEventSourceProps], name_mapping={'starting_position': 'startingPosition', 'batch_size': 'batchSize', 'max_batching_window': 'maxBatchingWindow'})
class DynamoEventSourceProps(StreamEventSourceProps):
    def __init__(self, *, starting_position: aws_cdk.aws_lambda.StartingPosition, batch_size: typing.Optional[jsii.Number]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None):
        """
        :param starting_position: Where to begin consuming the stream.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: - Minimum value of 1 - Maximum value of: - 1000 for {@link DynamoEventSource} - 10000 for {@link KinesisEventSource} Default: 100
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        """
        self._values = {
            'starting_position': starting_position,
        }
        if batch_size is not None: self._values["batch_size"] = batch_size
        if max_batching_window is not None: self._values["max_batching_window"] = max_batching_window

    @builtins.property
    def starting_position(self) -> aws_cdk.aws_lambda.StartingPosition:
        """Where to begin consuming the stream."""
        return self._values.get('starting_position')

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.

        Your function receives an
        event with all the retrieved records.

        Valid Range:

        - Minimum value of 1
        - Maximum value of:

          - 1000 for {@link DynamoEventSource}
          - 10000 for {@link KinesisEventSource}

        default
        :default: 100
        """
        return self._values.get('batch_size')

    @builtins.property
    def max_batching_window(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The maximum amount of time to gather records before invoking the function.

        Maximum of Duration.minutes(5)

        default
        :default: Duration.seconds(0)
        """
        return self._values.get('max_batching_window')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DynamoEventSourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-lambda-event-sources.KinesisEventSourceProps", jsii_struct_bases=[StreamEventSourceProps], name_mapping={'starting_position': 'startingPosition', 'batch_size': 'batchSize', 'max_batching_window': 'maxBatchingWindow'})
class KinesisEventSourceProps(StreamEventSourceProps):
    def __init__(self, *, starting_position: aws_cdk.aws_lambda.StartingPosition, batch_size: typing.Optional[jsii.Number]=None, max_batching_window: typing.Optional[aws_cdk.core.Duration]=None):
        """
        :param starting_position: Where to begin consuming the stream.
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: - Minimum value of 1 - Maximum value of: - 1000 for {@link DynamoEventSource} - 10000 for {@link KinesisEventSource} Default: 100
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        """
        self._values = {
            'starting_position': starting_position,
        }
        if batch_size is not None: self._values["batch_size"] = batch_size
        if max_batching_window is not None: self._values["max_batching_window"] = max_batching_window

    @builtins.property
    def starting_position(self) -> aws_cdk.aws_lambda.StartingPosition:
        """Where to begin consuming the stream."""
        return self._values.get('starting_position')

    @builtins.property
    def batch_size(self) -> typing.Optional[jsii.Number]:
        """The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.

        Your function receives an
        event with all the retrieved records.

        Valid Range:

        - Minimum value of 1
        - Maximum value of:

          - 1000 for {@link DynamoEventSource}
          - 10000 for {@link KinesisEventSource}

        default
        :default: 100
        """
        return self._values.get('batch_size')

    @builtins.property
    def max_batching_window(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The maximum amount of time to gather records before invoking the function.

        Maximum of Duration.minutes(5)

        default
        :default: Duration.seconds(0)
        """
        return self._values.get('max_batching_window')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'KinesisEventSourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["ApiEventSource", "DynamoEventSource", "DynamoEventSourceProps", "KinesisEventSource", "KinesisEventSourceProps", "S3EventSource", "S3EventSourceProps", "SnsEventSource", "SqsEventSource", "SqsEventSourceProps", "StreamEventSource", "StreamEventSourceProps", "__jsii_assembly__"]

publication.publish()
