"""
Main interface for lex-runtime service type definitions.

Usage::

    from mypy_boto3.lex_runtime.type_defs import ClientDeleteSessionResponseTypeDef

    data: ClientDeleteSessionResponseTypeDef = {...}
"""
import sys
from typing import Any, Dict, List, Union
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDeleteSessionResponseTypeDef",
    "ClientGetSessionResponsedialogActionTypeDef",
    "ClientGetSessionResponserecentIntentSummaryViewTypeDef",
    "ClientGetSessionResponseTypeDef",
    "ClientPostContentResponseTypeDef",
    "ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef",
    "ClientPostTextResponseresponseCardgenericAttachmentsTypeDef",
    "ClientPostTextResponseresponseCardTypeDef",
    "ClientPostTextResponsesentimentResponseTypeDef",
    "ClientPostTextResponseTypeDef",
    "ClientPutSessionDialogActionTypeDef",
    "ClientPutSessionRecentIntentSummaryViewTypeDef",
    "ClientPutSessionResponseTypeDef",
)

ClientDeleteSessionResponseTypeDef = TypedDict(
    "ClientDeleteSessionResponseTypeDef",
    {"botName": str, "botAlias": str, "userId": str, "sessionId": str},
    total=False,
)

ClientGetSessionResponsedialogActionTypeDef = TypedDict(
    "ClientGetSessionResponsedialogActionTypeDef",
    {
        "type": Literal["ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"],
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
    },
    total=False,
)

ClientGetSessionResponserecentIntentSummaryViewTypeDef = TypedDict(
    "ClientGetSessionResponserecentIntentSummaryViewTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": Literal["None", "Confirmed", "Denied"],
        "dialogActionType": Literal[
            "ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"
        ],
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "slotToElicit": str,
    },
    total=False,
)

ClientGetSessionResponseTypeDef = TypedDict(
    "ClientGetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List[ClientGetSessionResponserecentIntentSummaryViewTypeDef],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": ClientGetSessionResponsedialogActionTypeDef,
    },
    total=False,
)

ClientPostContentResponseTypeDef = TypedDict(
    "ClientPostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "sessionAttributes": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "sentimentResponse": str,
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
        "dialogState": Literal[
            "ElicitIntent",
            "ConfirmIntent",
            "ElicitSlot",
            "Fulfilled",
            "ReadyForFulfillment",
            "Failed",
        ],
        "slotToElicit": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
        "sessionId": str,
    },
    total=False,
)

ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef = TypedDict(
    "ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef",
    {"text": str, "value": str},
    total=False,
)

ClientPostTextResponseresponseCardgenericAttachmentsTypeDef = TypedDict(
    "ClientPostTextResponseresponseCardgenericAttachmentsTypeDef",
    {
        "title": str,
        "subTitle": str,
        "attachmentLinkUrl": str,
        "imageUrl": str,
        "buttons": List[ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef],
    },
    total=False,
)

ClientPostTextResponseresponseCardTypeDef = TypedDict(
    "ClientPostTextResponseresponseCardTypeDef",
    {
        "version": str,
        "contentType": str,
        "genericAttachments": List[ClientPostTextResponseresponseCardgenericAttachmentsTypeDef],
    },
    total=False,
)

ClientPostTextResponsesentimentResponseTypeDef = TypedDict(
    "ClientPostTextResponsesentimentResponseTypeDef",
    {"sentimentLabel": str, "sentimentScore": str},
    total=False,
)

ClientPostTextResponseTypeDef = TypedDict(
    "ClientPostTextResponseTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": ClientPostTextResponsesentimentResponseTypeDef,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
        "dialogState": Literal[
            "ElicitIntent",
            "ConfirmIntent",
            "ElicitSlot",
            "Fulfilled",
            "ReadyForFulfillment",
            "Failed",
        ],
        "slotToElicit": str,
        "responseCard": ClientPostTextResponseresponseCardTypeDef,
        "sessionId": str,
    },
    total=False,
)

_RequiredClientPutSessionDialogActionTypeDef = TypedDict(
    "_RequiredClientPutSessionDialogActionTypeDef",
    {"type": Literal["ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"]},
)
_OptionalClientPutSessionDialogActionTypeDef = TypedDict(
    "_OptionalClientPutSessionDialogActionTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
    },
    total=False,
)


class ClientPutSessionDialogActionTypeDef(
    _RequiredClientPutSessionDialogActionTypeDef, _OptionalClientPutSessionDialogActionTypeDef
):
    pass


ClientPutSessionRecentIntentSummaryViewTypeDef = TypedDict(
    "ClientPutSessionRecentIntentSummaryViewTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": Literal["None", "Confirmed", "Denied"],
        "dialogActionType": Literal[
            "ElicitIntent", "ConfirmIntent", "ElicitSlot", "Close", "Delegate"
        ],
        "fulfillmentState": Literal["Fulfilled", "Failed", "ReadyForFulfillment"],
        "slotToElicit": str,
    },
    total=False,
)

ClientPutSessionResponseTypeDef = TypedDict(
    "ClientPutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "sessionAttributes": Union[Dict[str, Any], List[Any], int, float, str, bool, None],
        "message": str,
        "messageFormat": Literal["PlainText", "CustomPayload", "SSML", "Composite"],
        "dialogState": Literal[
            "ElicitIntent",
            "ConfirmIntent",
            "ElicitSlot",
            "Fulfilled",
            "ReadyForFulfillment",
            "Failed",
        ],
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
    },
    total=False,
)
