"""
Main interface for iotevents service type definitions.

Usage::

    from mypy_boto3.iotevents.type_defs import ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef

    data: ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef",
    "ClientCreateDetectorModelDetectorModelDefinitionTypeDef",
    "ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef",
    "ClientCreateDetectorModelResponseTypeDef",
    "ClientCreateDetectorModelTagsTypeDef",
    "ClientCreateInputInputDefinitionattributesTypeDef",
    "ClientCreateInputInputDefinitionTypeDef",
    "ClientCreateInputResponseinputConfigurationTypeDef",
    "ClientCreateInputResponseTypeDef",
    "ClientCreateInputTagsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModelTypeDef",
    "ClientDescribeDetectorModelResponseTypeDef",
    "ClientDescribeInputResponseinputinputConfigurationTypeDef",
    "ClientDescribeInputResponseinputinputDefinitionattributesTypeDef",
    "ClientDescribeInputResponseinputinputDefinitionTypeDef",
    "ClientDescribeInputResponseinputTypeDef",
    "ClientDescribeInputResponseTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseTypeDef",
    "ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef",
    "ClientListDetectorModelVersionsResponseTypeDef",
    "ClientListDetectorModelsResponsedetectorModelSummariesTypeDef",
    "ClientListDetectorModelsResponseTypeDef",
    "ClientListInputsResponseinputSummariesTypeDef",
    "ClientListInputsResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef",
    "ClientPutLoggingOptionsLoggingOptionsTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef",
    "ClientUpdateDetectorModelDetectorModelDefinitionTypeDef",
    "ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef",
    "ClientUpdateDetectorModelResponseTypeDef",
    "ClientUpdateInputInputDefinitionattributesTypeDef",
    "ClientUpdateInputInputDefinitionTypeDef",
    "ClientUpdateInputResponseinputConfigurationTypeDef",
    "ClientUpdateInputResponseTypeDef",
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    {"events": List[ClientCreateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef]},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    {"events": List[ClientCreateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef]},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)

ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[ClientCreateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef],
        "transitionEvents": List[
            ClientCreateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)

_RequiredClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef", {"stateName": str}
)
_OptionalClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef",
    {
        "onInput": ClientCreateDetectorModelDetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientCreateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientCreateDetectorModelDetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef(
    _RequiredClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef,
    _OptionalClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef,
):
    pass


_RequiredClientCreateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModelDetectorModelDefinitionTypeDef",
    {"states": List[ClientCreateDetectorModelDetectorModelDefinitionstatesTypeDef]},
)
_OptionalClientCreateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModelDetectorModelDefinitionTypeDef",
    {"initialStateName": str},
    total=False,
)


class ClientCreateDetectorModelDetectorModelDefinitionTypeDef(
    _RequiredClientCreateDetectorModelDetectorModelDefinitionTypeDef,
    _OptionalClientCreateDetectorModelDetectorModelDefinitionTypeDef,
):
    pass


ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef = TypedDict(
    "ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "key": str,
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)

ClientCreateDetectorModelResponseTypeDef = TypedDict(
    "ClientCreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef
    },
    total=False,
)

_RequiredClientCreateDetectorModelTagsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModelTagsTypeDef", {"key": str}
)
_OptionalClientCreateDetectorModelTagsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModelTagsTypeDef", {"value": str}, total=False
)


class ClientCreateDetectorModelTagsTypeDef(
    _RequiredClientCreateDetectorModelTagsTypeDef, _OptionalClientCreateDetectorModelTagsTypeDef
):
    pass


ClientCreateInputInputDefinitionattributesTypeDef = TypedDict(
    "ClientCreateInputInputDefinitionattributesTypeDef", {"jsonPath": str}
)

ClientCreateInputInputDefinitionTypeDef = TypedDict(
    "ClientCreateInputInputDefinitionTypeDef",
    {"attributes": List[ClientCreateInputInputDefinitionattributesTypeDef]},
)

ClientCreateInputResponseinputConfigurationTypeDef = TypedDict(
    "ClientCreateInputResponseinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)

ClientCreateInputResponseTypeDef = TypedDict(
    "ClientCreateInputResponseTypeDef",
    {"inputConfiguration": ClientCreateInputResponseinputConfigurationTypeDef},
    total=False,
)

_RequiredClientCreateInputTagsTypeDef = TypedDict(
    "_RequiredClientCreateInputTagsTypeDef", {"key": str}
)
_OptionalClientCreateInputTagsTypeDef = TypedDict(
    "_OptionalClientCreateInputTagsTypeDef", {"value": str}, total=False
)


class ClientCreateInputTagsTypeDef(
    _RequiredClientCreateInputTagsTypeDef, _OptionalClientCreateInputTagsTypeDef
):
    pass


ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "key": str,
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
        ]
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
        ]
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
        ],
        "transitionEvents": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef",
    {
        "stateName": str,
        "onInput": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef",
    {
        "states": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef
        ],
        "initialStateName": str,
    },
    total=False,
)

ClientDescribeDetectorModelResponsedetectorModelTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponsedetectorModelTypeDef",
    {
        "detectorModelDefinition": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef,
        "detectorModelConfiguration": ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDetectorModelResponseTypeDef = TypedDict(
    "ClientDescribeDetectorModelResponseTypeDef",
    {"detectorModel": ClientDescribeDetectorModelResponsedetectorModelTypeDef},
    total=False,
)

ClientDescribeInputResponseinputinputConfigurationTypeDef = TypedDict(
    "ClientDescribeInputResponseinputinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)

ClientDescribeInputResponseinputinputDefinitionattributesTypeDef = TypedDict(
    "ClientDescribeInputResponseinputinputDefinitionattributesTypeDef",
    {"jsonPath": str},
    total=False,
)

ClientDescribeInputResponseinputinputDefinitionTypeDef = TypedDict(
    "ClientDescribeInputResponseinputinputDefinitionTypeDef",
    {"attributes": List[ClientDescribeInputResponseinputinputDefinitionattributesTypeDef]},
    total=False,
)

ClientDescribeInputResponseinputTypeDef = TypedDict(
    "ClientDescribeInputResponseinputTypeDef",
    {
        "inputConfiguration": ClientDescribeInputResponseinputinputConfigurationTypeDef,
        "inputDefinition": ClientDescribeInputResponseinputinputDefinitionTypeDef,
    },
    total=False,
)

ClientDescribeInputResponseTypeDef = TypedDict(
    "ClientDescribeInputResponseTypeDef",
    {"input": ClientDescribeInputResponseinputTypeDef},
    total=False,
)

ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef",
    {"detectorModelName": str, "keyValue": str},
    total=False,
)

ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef = TypedDict(
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR", "INFO", "DEBUG"],
        "enabled": bool,
        "detectorDebugOptions": List[
            ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoggingOptionsResponseTypeDef = TypedDict(
    "ClientDescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef},
    total=False,
)

ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef = TypedDict(
    "ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)

ClientListDetectorModelVersionsResponseTypeDef = TypedDict(
    "ClientListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List[
            ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListDetectorModelsResponsedetectorModelSummariesTypeDef = TypedDict(
    "ClientListDetectorModelsResponsedetectorModelSummariesTypeDef",
    {"detectorModelName": str, "detectorModelDescription": str, "creationTime": datetime},
    total=False,
)

ClientListDetectorModelsResponseTypeDef = TypedDict(
    "ClientListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List[
            ClientListDetectorModelsResponsedetectorModelSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListInputsResponseinputSummariesTypeDef = TypedDict(
    "ClientListInputsResponseinputSummariesTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)

ClientListInputsResponseTypeDef = TypedDict(
    "ClientListInputsResponseTypeDef",
    {"inputSummaries": List[ClientListInputsResponseinputSummariesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef",
    {"detectorModelName": str, "keyValue": str},
    total=False,
)

_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef", {"roleArn": str}
)
_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef",
    {
        "level": Literal["ERROR", "INFO", "DEBUG"],
        "enabled": bool,
        "detectorDebugOptions": List[
            ClientPutLoggingOptionsLoggingOptionsdetectorDebugOptionsTypeDef
        ],
    },
    total=False,
)


class ClientPutLoggingOptionsLoggingOptionsTypeDef(
    _RequiredClientPutLoggingOptionsLoggingOptionsTypeDef,
    _OptionalClientPutLoggingOptionsLoggingOptionsTypeDef,
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef",
    {"events": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesonEntereventsTypeDef]},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef",
    {"events": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesonExiteventsTypeDef]},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)

ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputeventsTypeDef],
        "transitionEvents": List[
            ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)

_RequiredClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef", {"stateName": str}
)
_OptionalClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef",
    {
        "onInput": ClientUpdateDetectorModelDetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientUpdateDetectorModelDetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientUpdateDetectorModelDetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef(
    _RequiredClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef,
    _OptionalClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef,
):
    pass


_RequiredClientUpdateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModelDetectorModelDefinitionTypeDef",
    {"states": List[ClientUpdateDetectorModelDetectorModelDefinitionstatesTypeDef]},
)
_OptionalClientUpdateDetectorModelDetectorModelDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModelDetectorModelDefinitionTypeDef",
    {"initialStateName": str},
    total=False,
)


class ClientUpdateDetectorModelDetectorModelDefinitionTypeDef(
    _RequiredClientUpdateDetectorModelDetectorModelDefinitionTypeDef,
    _OptionalClientUpdateDetectorModelDetectorModelDefinitionTypeDef,
):
    pass


ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef = TypedDict(
    "ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal[
            "ACTIVE", "ACTIVATING", "INACTIVE", "DEPRECATED", "DRAFT", "PAUSED", "FAILED"
        ],
        "key": str,
        "evaluationMethod": Literal["BATCH", "SERIAL"],
    },
    total=False,
)

ClientUpdateDetectorModelResponseTypeDef = TypedDict(
    "ClientUpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef
    },
    total=False,
)

ClientUpdateInputInputDefinitionattributesTypeDef = TypedDict(
    "ClientUpdateInputInputDefinitionattributesTypeDef", {"jsonPath": str}
)

ClientUpdateInputInputDefinitionTypeDef = TypedDict(
    "ClientUpdateInputInputDefinitionTypeDef",
    {"attributes": List[ClientUpdateInputInputDefinitionattributesTypeDef]},
)

ClientUpdateInputResponseinputConfigurationTypeDef = TypedDict(
    "ClientUpdateInputResponseinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING"],
    },
    total=False,
)

ClientUpdateInputResponseTypeDef = TypedDict(
    "ClientUpdateInputResponseTypeDef",
    {"inputConfiguration": ClientUpdateInputResponseinputConfigurationTypeDef},
    total=False,
)
