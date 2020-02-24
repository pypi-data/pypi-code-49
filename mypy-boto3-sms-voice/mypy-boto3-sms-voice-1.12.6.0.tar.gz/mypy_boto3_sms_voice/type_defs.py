"""
Main interface for sms-voice service type definitions.

Usage::

    from mypy_boto3.sms_voice.type_defs import ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef

    data: ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef = {...}
"""
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
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientSendVoiceMessageContentCallInstructionsMessageTypeDef",
    "ClientSendVoiceMessageContentPlainTextMessageTypeDef",
    "ClientSendVoiceMessageContentSSMLMessageTypeDef",
    "ClientSendVoiceMessageContentTypeDef",
    "ClientSendVoiceMessageResponseTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
)

ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    {"IamRoleArn": str, "LogGroupArn": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"DeliveryStreamArn": str, "IamRoleArn": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)

ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "SnsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
    },
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef",
    {"IamRoleArn": str, "LogGroupArn": str},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"DeliveryStreamArn": str, "IamRoleArn": str},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    {
        "CloudWatchLogsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "Name": str,
        "SnsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef,
    },
    total=False,
)

ClientGetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
        ]
    },
    total=False,
)

ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "ClientListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[str], "NextToken": str},
    total=False,
)

ClientSendVoiceMessageContentCallInstructionsMessageTypeDef = TypedDict(
    "ClientSendVoiceMessageContentCallInstructionsMessageTypeDef", {"Text": str}, total=False
)

ClientSendVoiceMessageContentPlainTextMessageTypeDef = TypedDict(
    "ClientSendVoiceMessageContentPlainTextMessageTypeDef",
    {"LanguageCode": str, "Text": str, "VoiceId": str},
    total=False,
)

ClientSendVoiceMessageContentSSMLMessageTypeDef = TypedDict(
    "ClientSendVoiceMessageContentSSMLMessageTypeDef",
    {"LanguageCode": str, "Text": str, "VoiceId": str},
    total=False,
)

ClientSendVoiceMessageContentTypeDef = TypedDict(
    "ClientSendVoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": ClientSendVoiceMessageContentCallInstructionsMessageTypeDef,
        "PlainTextMessage": ClientSendVoiceMessageContentPlainTextMessageTypeDef,
        "SSMLMessage": ClientSendVoiceMessageContentSSMLMessageTypeDef,
    },
    total=False,
)

ClientSendVoiceMessageResponseTypeDef = TypedDict(
    "ClientSendVoiceMessageResponseTypeDef", {"MessageId": str}, total=False
)

ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef",
    {"IamRoleArn": str, "LogGroupArn": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"DeliveryStreamArn": str, "IamRoleArn": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)

ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchLogsDestinationTypeDef,
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "MatchingEventTypes": List[
            Literal[
                "INITIATED_CALL",
                "RINGING",
                "ANSWERED",
                "COMPLETED_CALL",
                "BUSY",
                "FAILED",
                "NO_ANSWER",
            ]
        ],
        "SnsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
    },
    total=False,
)
