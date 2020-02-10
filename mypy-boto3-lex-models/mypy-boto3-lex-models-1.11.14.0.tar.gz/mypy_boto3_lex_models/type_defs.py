"""
Main interface for lex-models service type definitions.

Usage::

    from mypy_boto3.lex_models.type_defs import ClientCreateBotVersionResponseabortStatementmessagesTypeDef

    data: ClientCreateBotVersionResponseabortStatementmessagesTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBotVersionResponseabortStatementmessagesTypeDef",
    "ClientCreateBotVersionResponseabortStatementTypeDef",
    "ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef",
    "ClientCreateBotVersionResponseclarificationPromptTypeDef",
    "ClientCreateBotVersionResponseintentsTypeDef",
    "ClientCreateBotVersionResponseTypeDef",
    "ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponseconclusionStatementTypeDef",
    "ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef",
    "ClientCreateIntentVersionResponseconfirmationPromptTypeDef",
    "ClientCreateIntentVersionResponsedialogCodeHookTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptTypeDef",
    "ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef",
    "ClientCreateIntentVersionResponsefulfillmentActivityTypeDef",
    "ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponserejectionStatementTypeDef",
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef",
    "ClientCreateIntentVersionResponseslotsTypeDef",
    "ClientCreateIntentVersionResponseTypeDef",
    "ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef",
    "ClientCreateSlotTypeVersionResponseslotTypeConfigurationsregexConfigurationTypeDef",
    "ClientCreateSlotTypeVersionResponseslotTypeConfigurationsTypeDef",
    "ClientCreateSlotTypeVersionResponseTypeDef",
    "ClientGetBotAliasResponseconversationLogslogSettingsTypeDef",
    "ClientGetBotAliasResponseconversationLogsTypeDef",
    "ClientGetBotAliasResponseTypeDef",
    "ClientGetBotAliasesResponseBotAliasesconversationLogslogSettingsTypeDef",
    "ClientGetBotAliasesResponseBotAliasesconversationLogsTypeDef",
    "ClientGetBotAliasesResponseBotAliasesTypeDef",
    "ClientGetBotAliasesResponseTypeDef",
    "ClientGetBotChannelAssociationResponseTypeDef",
    "ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef",
    "ClientGetBotChannelAssociationsResponseTypeDef",
    "ClientGetBotResponseabortStatementmessagesTypeDef",
    "ClientGetBotResponseabortStatementTypeDef",
    "ClientGetBotResponseclarificationPromptmessagesTypeDef",
    "ClientGetBotResponseclarificationPromptTypeDef",
    "ClientGetBotResponseintentsTypeDef",
    "ClientGetBotResponseTypeDef",
    "ClientGetBotVersionsResponsebotsTypeDef",
    "ClientGetBotVersionsResponseTypeDef",
    "ClientGetBotsResponsebotsTypeDef",
    "ClientGetBotsResponseTypeDef",
    "ClientGetBuiltinIntentResponseslotsTypeDef",
    "ClientGetBuiltinIntentResponseTypeDef",
    "ClientGetBuiltinIntentsResponseintentsTypeDef",
    "ClientGetBuiltinIntentsResponseTypeDef",
    "ClientGetBuiltinSlotTypesResponseslotTypesTypeDef",
    "ClientGetBuiltinSlotTypesResponseTypeDef",
    "ClientGetExportResponseTypeDef",
    "ClientGetImportResponseTypeDef",
    "ClientGetIntentResponseconclusionStatementmessagesTypeDef",
    "ClientGetIntentResponseconclusionStatementTypeDef",
    "ClientGetIntentResponseconfirmationPromptmessagesTypeDef",
    "ClientGetIntentResponseconfirmationPromptTypeDef",
    "ClientGetIntentResponsedialogCodeHookTypeDef",
    "ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientGetIntentResponsefollowUpPromptpromptTypeDef",
    "ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientGetIntentResponsefollowUpPromptTypeDef",
    "ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef",
    "ClientGetIntentResponsefulfillmentActivityTypeDef",
    "ClientGetIntentResponserejectionStatementmessagesTypeDef",
    "ClientGetIntentResponserejectionStatementTypeDef",
    "ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientGetIntentResponseslotsvalueElicitationPromptTypeDef",
    "ClientGetIntentResponseslotsTypeDef",
    "ClientGetIntentResponseTypeDef",
    "ClientGetIntentVersionsResponseintentsTypeDef",
    "ClientGetIntentVersionsResponseTypeDef",
    "ClientGetIntentsResponseintentsTypeDef",
    "ClientGetIntentsResponseTypeDef",
    "ClientGetSlotTypeResponseenumerationValuesTypeDef",
    "ClientGetSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef",
    "ClientGetSlotTypeResponseslotTypeConfigurationsTypeDef",
    "ClientGetSlotTypeResponseTypeDef",
    "ClientGetSlotTypeVersionsResponseslotTypesTypeDef",
    "ClientGetSlotTypeVersionsResponseTypeDef",
    "ClientGetSlotTypesResponseslotTypesTypeDef",
    "ClientGetSlotTypesResponseTypeDef",
    "ClientGetUtterancesViewResponseutterancesutterancesTypeDef",
    "ClientGetUtterancesViewResponseutterancesTypeDef",
    "ClientGetUtterancesViewResponseTypeDef",
    "ClientPutBotAbortStatementmessagesTypeDef",
    "ClientPutBotAbortStatementTypeDef",
    "ClientPutBotAliasConversationLogslogSettingsTypeDef",
    "ClientPutBotAliasConversationLogsTypeDef",
    "ClientPutBotAliasResponseconversationLogslogSettingsTypeDef",
    "ClientPutBotAliasResponseconversationLogsTypeDef",
    "ClientPutBotAliasResponseTypeDef",
    "ClientPutBotClarificationPromptmessagesTypeDef",
    "ClientPutBotClarificationPromptTypeDef",
    "ClientPutBotIntentsTypeDef",
    "ClientPutBotResponseabortStatementmessagesTypeDef",
    "ClientPutBotResponseabortStatementTypeDef",
    "ClientPutBotResponseclarificationPromptmessagesTypeDef",
    "ClientPutBotResponseclarificationPromptTypeDef",
    "ClientPutBotResponseintentsTypeDef",
    "ClientPutBotResponseTypeDef",
    "ClientPutIntentConclusionStatementmessagesTypeDef",
    "ClientPutIntentConclusionStatementTypeDef",
    "ClientPutIntentConfirmationPromptmessagesTypeDef",
    "ClientPutIntentConfirmationPromptTypeDef",
    "ClientPutIntentDialogCodeHookTypeDef",
    "ClientPutIntentFollowUpPromptpromptmessagesTypeDef",
    "ClientPutIntentFollowUpPromptpromptTypeDef",
    "ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientPutIntentFollowUpPromptrejectionStatementTypeDef",
    "ClientPutIntentFollowUpPromptTypeDef",
    "ClientPutIntentFulfillmentActivitycodeHookTypeDef",
    "ClientPutIntentFulfillmentActivityTypeDef",
    "ClientPutIntentRejectionStatementmessagesTypeDef",
    "ClientPutIntentRejectionStatementTypeDef",
    "ClientPutIntentResponseconclusionStatementmessagesTypeDef",
    "ClientPutIntentResponseconclusionStatementTypeDef",
    "ClientPutIntentResponseconfirmationPromptmessagesTypeDef",
    "ClientPutIntentResponseconfirmationPromptTypeDef",
    "ClientPutIntentResponsedialogCodeHookTypeDef",
    "ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientPutIntentResponsefollowUpPromptpromptTypeDef",
    "ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientPutIntentResponsefollowUpPromptTypeDef",
    "ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef",
    "ClientPutIntentResponsefulfillmentActivityTypeDef",
    "ClientPutIntentResponserejectionStatementmessagesTypeDef",
    "ClientPutIntentResponserejectionStatementTypeDef",
    "ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientPutIntentResponseslotsvalueElicitationPromptTypeDef",
    "ClientPutIntentResponseslotsTypeDef",
    "ClientPutIntentResponseTypeDef",
    "ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef",
    "ClientPutIntentSlotsvalueElicitationPromptTypeDef",
    "ClientPutIntentSlotsTypeDef",
    "ClientPutSlotTypeEnumerationValuesTypeDef",
    "ClientPutSlotTypeResponseenumerationValuesTypeDef",
    "ClientPutSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef",
    "ClientPutSlotTypeResponseslotTypeConfigurationsTypeDef",
    "ClientPutSlotTypeResponseTypeDef",
    "ClientPutSlotTypeSlotTypeConfigurationsregexConfigurationTypeDef",
    "ClientPutSlotTypeSlotTypeConfigurationsTypeDef",
    "ClientStartImportResponseTypeDef",
    "LogSettingsResponseTypeDef",
    "ConversationLogsResponseTypeDef",
    "BotAliasMetadataTypeDef",
    "GetBotAliasesResponseTypeDef",
    "BotChannelAssociationTypeDef",
    "GetBotChannelAssociationsResponseTypeDef",
    "BotMetadataTypeDef",
    "GetBotVersionsResponseTypeDef",
    "GetBotsResponseTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "GetBuiltinIntentsResponseTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "GetBuiltinSlotTypesResponseTypeDef",
    "IntentMetadataTypeDef",
    "GetIntentVersionsResponseTypeDef",
    "GetIntentsResponseTypeDef",
    "SlotTypeMetadataTypeDef",
    "GetSlotTypeVersionsResponseTypeDef",
    "GetSlotTypesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateBotVersionResponseabortStatementmessagesTypeDef = TypedDict(
    "ClientCreateBotVersionResponseabortStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateBotVersionResponseabortStatementTypeDef = TypedDict(
    "ClientCreateBotVersionResponseabortStatementTypeDef",
    {
        "messages": List[ClientCreateBotVersionResponseabortStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef = TypedDict(
    "ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateBotVersionResponseclarificationPromptTypeDef = TypedDict(
    "ClientCreateBotVersionResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientCreateBotVersionResponseintentsTypeDef = TypedDict(
    "ClientCreateBotVersionResponseintentsTypeDef",
    {"intentName": str, "intentVersion": str},
    total=False,
)

ClientCreateBotVersionResponseTypeDef = TypedDict(
    "ClientCreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientCreateBotVersionResponseintentsTypeDef],
        "clarificationPrompt": ClientCreateBotVersionResponseclarificationPromptTypeDef,
        "abortStatement": ClientCreateBotVersionResponseabortStatementTypeDef,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": Literal["en-US", "en-GB", "de-DE"],
        "childDirected": bool,
        "detectSentiment": bool,
    },
    total=False,
)

ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateIntentVersionResponseconclusionStatementTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateIntentVersionResponseconfirmationPromptTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientCreateIntentVersionResponsedialogCodeHookTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)

ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)

ClientCreateIntentVersionResponsefollowUpPromptTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)

ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)

ClientCreateIntentVersionResponsefulfillmentActivityTypeDef = TypedDict(
    "ClientCreateIntentVersionResponsefulfillmentActivityTypeDef",
    {
        "type": Literal["ReturnIntent", "CodeHook"],
        "codeHook": ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)

ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef = TypedDict(
    "ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateIntentVersionResponserejectionStatementTypeDef = TypedDict(
    "ClientCreateIntentVersionResponserejectionStatementTypeDef",
    {
        "messages": List[ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientCreateIntentVersionResponseslotsTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": Literal["NONE", "DEFAULT_OBFUSCATION"],
    },
    total=False,
)

ClientCreateIntentVersionResponseTypeDef = TypedDict(
    "ClientCreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientCreateIntentVersionResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientCreateIntentVersionResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientCreateIntentVersionResponserejectionStatementTypeDef,
        "followUpPrompt": ClientCreateIntentVersionResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientCreateIntentVersionResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientCreateIntentVersionResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientCreateIntentVersionResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
    },
    total=False,
)

ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef = TypedDict(
    "ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)

ClientCreateSlotTypeVersionResponseslotTypeConfigurationsregexConfigurationTypeDef = TypedDict(
    "ClientCreateSlotTypeVersionResponseslotTypeConfigurationsregexConfigurationTypeDef",
    {"pattern": str},
    total=False,
)

ClientCreateSlotTypeVersionResponseslotTypeConfigurationsTypeDef = TypedDict(
    "ClientCreateSlotTypeVersionResponseslotTypeConfigurationsTypeDef",
    {
        "regexConfiguration": ClientCreateSlotTypeVersionResponseslotTypeConfigurationsregexConfigurationTypeDef
    },
    total=False,
)

ClientCreateSlotTypeVersionResponseTypeDef = TypedDict(
    "ClientCreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"],
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[
            ClientCreateSlotTypeVersionResponseslotTypeConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientGetBotAliasResponseconversationLogslogSettingsTypeDef = TypedDict(
    "ClientGetBotAliasResponseconversationLogslogSettingsTypeDef",
    {
        "logType": Literal["AUDIO", "TEXT"],
        "destination": Literal["CLOUDWATCH_LOGS", "S3"],
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

ClientGetBotAliasResponseconversationLogsTypeDef = TypedDict(
    "ClientGetBotAliasResponseconversationLogsTypeDef",
    {
        "logSettings": List[ClientGetBotAliasResponseconversationLogslogSettingsTypeDef],
        "iamRoleArn": str,
    },
    total=False,
)

ClientGetBotAliasResponseTypeDef = TypedDict(
    "ClientGetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ClientGetBotAliasResponseconversationLogsTypeDef,
    },
    total=False,
)

ClientGetBotAliasesResponseBotAliasesconversationLogslogSettingsTypeDef = TypedDict(
    "ClientGetBotAliasesResponseBotAliasesconversationLogslogSettingsTypeDef",
    {
        "logType": Literal["AUDIO", "TEXT"],
        "destination": Literal["CLOUDWATCH_LOGS", "S3"],
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

ClientGetBotAliasesResponseBotAliasesconversationLogsTypeDef = TypedDict(
    "ClientGetBotAliasesResponseBotAliasesconversationLogsTypeDef",
    {
        "logSettings": List[
            ClientGetBotAliasesResponseBotAliasesconversationLogslogSettingsTypeDef
        ],
        "iamRoleArn": str,
    },
    total=False,
)

ClientGetBotAliasesResponseBotAliasesTypeDef = TypedDict(
    "ClientGetBotAliasesResponseBotAliasesTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ClientGetBotAliasesResponseBotAliasesconversationLogsTypeDef,
    },
    total=False,
)

ClientGetBotAliasesResponseTypeDef = TypedDict(
    "ClientGetBotAliasesResponseTypeDef",
    {"BotAliases": List[ClientGetBotAliasesResponseBotAliasesTypeDef], "nextToken": str},
    total=False,
)

ClientGetBotChannelAssociationResponseTypeDef = TypedDict(
    "ClientGetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": Literal["Facebook", "Slack", "Twilio-Sms", "Kik"],
        "botConfiguration": Dict[str, str],
        "status": Literal["IN_PROGRESS", "CREATED", "FAILED"],
        "failureReason": str,
    },
    total=False,
)

ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef = TypedDict(
    "ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": Literal["Facebook", "Slack", "Twilio-Sms", "Kik"],
        "botConfiguration": Dict[str, str],
        "status": Literal["IN_PROGRESS", "CREATED", "FAILED"],
        "failureReason": str,
    },
    total=False,
)

ClientGetBotChannelAssociationsResponseTypeDef = TypedDict(
    "ClientGetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List[
            ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientGetBotResponseabortStatementmessagesTypeDef = TypedDict(
    "ClientGetBotResponseabortStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetBotResponseabortStatementTypeDef = TypedDict(
    "ClientGetBotResponseabortStatementTypeDef",
    {"messages": List[ClientGetBotResponseabortStatementmessagesTypeDef], "responseCard": str},
    total=False,
)

ClientGetBotResponseclarificationPromptmessagesTypeDef = TypedDict(
    "ClientGetBotResponseclarificationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetBotResponseclarificationPromptTypeDef = TypedDict(
    "ClientGetBotResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientGetBotResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientGetBotResponseintentsTypeDef = TypedDict(
    "ClientGetBotResponseintentsTypeDef", {"intentName": str, "intentVersion": str}, total=False
)

ClientGetBotResponseTypeDef = TypedDict(
    "ClientGetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientGetBotResponseintentsTypeDef],
        "clarificationPrompt": ClientGetBotResponseclarificationPromptTypeDef,
        "abortStatement": ClientGetBotResponseabortStatementTypeDef,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": Literal["en-US", "en-GB", "de-DE"],
        "childDirected": bool,
        "detectSentiment": bool,
    },
    total=False,
)

ClientGetBotVersionsResponsebotsTypeDef = TypedDict(
    "ClientGetBotVersionsResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

ClientGetBotVersionsResponseTypeDef = TypedDict(
    "ClientGetBotVersionsResponseTypeDef",
    {"bots": List[ClientGetBotVersionsResponsebotsTypeDef], "nextToken": str},
    total=False,
)

ClientGetBotsResponsebotsTypeDef = TypedDict(
    "ClientGetBotsResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

ClientGetBotsResponseTypeDef = TypedDict(
    "ClientGetBotsResponseTypeDef",
    {"bots": List[ClientGetBotsResponsebotsTypeDef], "nextToken": str},
    total=False,
)

ClientGetBuiltinIntentResponseslotsTypeDef = TypedDict(
    "ClientGetBuiltinIntentResponseslotsTypeDef", {"name": str}, total=False
)

ClientGetBuiltinIntentResponseTypeDef = TypedDict(
    "ClientGetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]],
        "slots": List[ClientGetBuiltinIntentResponseslotsTypeDef],
    },
    total=False,
)

ClientGetBuiltinIntentsResponseintentsTypeDef = TypedDict(
    "ClientGetBuiltinIntentsResponseintentsTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)

ClientGetBuiltinIntentsResponseTypeDef = TypedDict(
    "ClientGetBuiltinIntentsResponseTypeDef",
    {"intents": List[ClientGetBuiltinIntentsResponseintentsTypeDef], "nextToken": str},
    total=False,
)

ClientGetBuiltinSlotTypesResponseslotTypesTypeDef = TypedDict(
    "ClientGetBuiltinSlotTypesResponseslotTypesTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)

ClientGetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "ClientGetBuiltinSlotTypesResponseTypeDef",
    {"slotTypes": List[ClientGetBuiltinSlotTypesResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)

ClientGetExportResponseTypeDef = TypedDict(
    "ClientGetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": Literal["BOT", "INTENT", "SLOT_TYPE"],
        "exportType": Literal["ALEXA_SKILLS_KIT", "LEX"],
        "exportStatus": Literal["IN_PROGRESS", "READY", "FAILED"],
        "failureReason": str,
        "url": str,
    },
    total=False,
)

ClientGetImportResponseTypeDef = TypedDict(
    "ClientGetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": Literal["BOT", "INTENT", "SLOT_TYPE"],
        "mergeStrategy": Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
        "importId": str,
        "importStatus": Literal["IN_PROGRESS", "COMPLETE", "FAILED"],
        "failureReason": List[str],
        "createdDate": datetime,
    },
    total=False,
)

ClientGetIntentResponseconclusionStatementmessagesTypeDef = TypedDict(
    "ClientGetIntentResponseconclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetIntentResponseconclusionStatementTypeDef = TypedDict(
    "ClientGetIntentResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientGetIntentResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "ClientGetIntentResponseconfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetIntentResponseconfirmationPromptTypeDef = TypedDict(
    "ClientGetIntentResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientGetIntentResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientGetIntentResponsedialogCodeHookTypeDef = TypedDict(
    "ClientGetIntentResponsedialogCodeHookTypeDef", {"uri": str, "messageVersion": str}, total=False
)

ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetIntentResponsefollowUpPromptpromptTypeDef = TypedDict(
    "ClientGetIntentResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientGetIntentResponsefollowUpPromptTypeDef = TypedDict(
    "ClientGetIntentResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientGetIntentResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)

ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)

ClientGetIntentResponsefulfillmentActivityTypeDef = TypedDict(
    "ClientGetIntentResponsefulfillmentActivityTypeDef",
    {
        "type": Literal["ReturnIntent", "CodeHook"],
        "codeHook": ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)

ClientGetIntentResponserejectionStatementmessagesTypeDef = TypedDict(
    "ClientGetIntentResponserejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetIntentResponserejectionStatementTypeDef = TypedDict(
    "ClientGetIntentResponserejectionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientGetIntentResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "ClientGetIntentResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientGetIntentResponseslotsTypeDef = TypedDict(
    "ClientGetIntentResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientGetIntentResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": Literal["NONE", "DEFAULT_OBFUSCATION"],
    },
    total=False,
)

ClientGetIntentResponseTypeDef = TypedDict(
    "ClientGetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientGetIntentResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientGetIntentResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientGetIntentResponserejectionStatementTypeDef,
        "followUpPrompt": ClientGetIntentResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientGetIntentResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientGetIntentResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientGetIntentResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
    },
    total=False,
)

ClientGetIntentVersionsResponseintentsTypeDef = TypedDict(
    "ClientGetIntentVersionsResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

ClientGetIntentVersionsResponseTypeDef = TypedDict(
    "ClientGetIntentVersionsResponseTypeDef",
    {"intents": List[ClientGetIntentVersionsResponseintentsTypeDef], "nextToken": str},
    total=False,
)

ClientGetIntentsResponseintentsTypeDef = TypedDict(
    "ClientGetIntentsResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

ClientGetIntentsResponseTypeDef = TypedDict(
    "ClientGetIntentsResponseTypeDef",
    {"intents": List[ClientGetIntentsResponseintentsTypeDef], "nextToken": str},
    total=False,
)

ClientGetSlotTypeResponseenumerationValuesTypeDef = TypedDict(
    "ClientGetSlotTypeResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)

ClientGetSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef = TypedDict(
    "ClientGetSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef",
    {"pattern": str},
    total=False,
)

ClientGetSlotTypeResponseslotTypeConfigurationsTypeDef = TypedDict(
    "ClientGetSlotTypeResponseslotTypeConfigurationsTypeDef",
    {
        "regexConfiguration": ClientGetSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef
    },
    total=False,
)

ClientGetSlotTypeResponseTypeDef = TypedDict(
    "ClientGetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientGetSlotTypeResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"],
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[ClientGetSlotTypeResponseslotTypeConfigurationsTypeDef],
    },
    total=False,
)

ClientGetSlotTypeVersionsResponseslotTypesTypeDef = TypedDict(
    "ClientGetSlotTypeVersionsResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

ClientGetSlotTypeVersionsResponseTypeDef = TypedDict(
    "ClientGetSlotTypeVersionsResponseTypeDef",
    {"slotTypes": List[ClientGetSlotTypeVersionsResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)

ClientGetSlotTypesResponseslotTypesTypeDef = TypedDict(
    "ClientGetSlotTypesResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

ClientGetSlotTypesResponseTypeDef = TypedDict(
    "ClientGetSlotTypesResponseTypeDef",
    {"slotTypes": List[ClientGetSlotTypesResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)

ClientGetUtterancesViewResponseutterancesutterancesTypeDef = TypedDict(
    "ClientGetUtterancesViewResponseutterancesutterancesTypeDef",
    {
        "utteranceString": str,
        "count": int,
        "distinctUsers": int,
        "firstUtteredDate": datetime,
        "lastUtteredDate": datetime,
    },
    total=False,
)

ClientGetUtterancesViewResponseutterancesTypeDef = TypedDict(
    "ClientGetUtterancesViewResponseutterancesTypeDef",
    {
        "botVersion": str,
        "utterances": List[ClientGetUtterancesViewResponseutterancesutterancesTypeDef],
    },
    total=False,
)

ClientGetUtterancesViewResponseTypeDef = TypedDict(
    "ClientGetUtterancesViewResponseTypeDef",
    {"botName": str, "utterances": List[ClientGetUtterancesViewResponseutterancesTypeDef]},
    total=False,
)

_RequiredClientPutBotAbortStatementmessagesTypeDef = TypedDict(
    "_RequiredClientPutBotAbortStatementmessagesTypeDef",
    {"contentType": Literal["PlainText", "SSML", "CustomPayload"]},
)
_OptionalClientPutBotAbortStatementmessagesTypeDef = TypedDict(
    "_OptionalClientPutBotAbortStatementmessagesTypeDef",
    {"content": str, "groupNumber": int},
    total=False,
)


class ClientPutBotAbortStatementmessagesTypeDef(
    _RequiredClientPutBotAbortStatementmessagesTypeDef,
    _OptionalClientPutBotAbortStatementmessagesTypeDef,
):
    pass


_RequiredClientPutBotAbortStatementTypeDef = TypedDict(
    "_RequiredClientPutBotAbortStatementTypeDef",
    {"messages": List[ClientPutBotAbortStatementmessagesTypeDef]},
)
_OptionalClientPutBotAbortStatementTypeDef = TypedDict(
    "_OptionalClientPutBotAbortStatementTypeDef", {"responseCard": str}, total=False
)


class ClientPutBotAbortStatementTypeDef(
    _RequiredClientPutBotAbortStatementTypeDef, _OptionalClientPutBotAbortStatementTypeDef
):
    pass


_RequiredClientPutBotAliasConversationLogslogSettingsTypeDef = TypedDict(
    "_RequiredClientPutBotAliasConversationLogslogSettingsTypeDef",
    {"logType": Literal["AUDIO", "TEXT"]},
)
_OptionalClientPutBotAliasConversationLogslogSettingsTypeDef = TypedDict(
    "_OptionalClientPutBotAliasConversationLogslogSettingsTypeDef",
    {"destination": Literal["CLOUDWATCH_LOGS", "S3"], "kmsKeyArn": str, "resourceArn": str},
    total=False,
)


class ClientPutBotAliasConversationLogslogSettingsTypeDef(
    _RequiredClientPutBotAliasConversationLogslogSettingsTypeDef,
    _OptionalClientPutBotAliasConversationLogslogSettingsTypeDef,
):
    pass


_RequiredClientPutBotAliasConversationLogsTypeDef = TypedDict(
    "_RequiredClientPutBotAliasConversationLogsTypeDef",
    {"logSettings": List[ClientPutBotAliasConversationLogslogSettingsTypeDef]},
)
_OptionalClientPutBotAliasConversationLogsTypeDef = TypedDict(
    "_OptionalClientPutBotAliasConversationLogsTypeDef", {"iamRoleArn": str}, total=False
)


class ClientPutBotAliasConversationLogsTypeDef(
    _RequiredClientPutBotAliasConversationLogsTypeDef,
    _OptionalClientPutBotAliasConversationLogsTypeDef,
):
    pass


ClientPutBotAliasResponseconversationLogslogSettingsTypeDef = TypedDict(
    "ClientPutBotAliasResponseconversationLogslogSettingsTypeDef",
    {
        "logType": Literal["AUDIO", "TEXT"],
        "destination": Literal["CLOUDWATCH_LOGS", "S3"],
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

ClientPutBotAliasResponseconversationLogsTypeDef = TypedDict(
    "ClientPutBotAliasResponseconversationLogsTypeDef",
    {
        "logSettings": List[ClientPutBotAliasResponseconversationLogslogSettingsTypeDef],
        "iamRoleArn": str,
    },
    total=False,
)

ClientPutBotAliasResponseTypeDef = TypedDict(
    "ClientPutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ClientPutBotAliasResponseconversationLogsTypeDef,
    },
    total=False,
)

_RequiredClientPutBotClarificationPromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutBotClarificationPromptmessagesTypeDef",
    {"contentType": Literal["PlainText", "SSML", "CustomPayload"]},
)
_OptionalClientPutBotClarificationPromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutBotClarificationPromptmessagesTypeDef",
    {"content": str, "groupNumber": int},
    total=False,
)


class ClientPutBotClarificationPromptmessagesTypeDef(
    _RequiredClientPutBotClarificationPromptmessagesTypeDef,
    _OptionalClientPutBotClarificationPromptmessagesTypeDef,
):
    pass


_RequiredClientPutBotClarificationPromptTypeDef = TypedDict(
    "_RequiredClientPutBotClarificationPromptTypeDef",
    {"messages": List[ClientPutBotClarificationPromptmessagesTypeDef]},
)
_OptionalClientPutBotClarificationPromptTypeDef = TypedDict(
    "_OptionalClientPutBotClarificationPromptTypeDef",
    {"maxAttempts": int, "responseCard": str},
    total=False,
)


class ClientPutBotClarificationPromptTypeDef(
    _RequiredClientPutBotClarificationPromptTypeDef, _OptionalClientPutBotClarificationPromptTypeDef
):
    pass


_RequiredClientPutBotIntentsTypeDef = TypedDict(
    "_RequiredClientPutBotIntentsTypeDef", {"intentName": str}
)
_OptionalClientPutBotIntentsTypeDef = TypedDict(
    "_OptionalClientPutBotIntentsTypeDef", {"intentVersion": str}, total=False
)


class ClientPutBotIntentsTypeDef(
    _RequiredClientPutBotIntentsTypeDef, _OptionalClientPutBotIntentsTypeDef
):
    pass


ClientPutBotResponseabortStatementmessagesTypeDef = TypedDict(
    "ClientPutBotResponseabortStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutBotResponseabortStatementTypeDef = TypedDict(
    "ClientPutBotResponseabortStatementTypeDef",
    {"messages": List[ClientPutBotResponseabortStatementmessagesTypeDef], "responseCard": str},
    total=False,
)

ClientPutBotResponseclarificationPromptmessagesTypeDef = TypedDict(
    "ClientPutBotResponseclarificationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutBotResponseclarificationPromptTypeDef = TypedDict(
    "ClientPutBotResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientPutBotResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientPutBotResponseintentsTypeDef = TypedDict(
    "ClientPutBotResponseintentsTypeDef", {"intentName": str, "intentVersion": str}, total=False
)

ClientPutBotResponseTypeDef = TypedDict(
    "ClientPutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientPutBotResponseintentsTypeDef],
        "clarificationPrompt": ClientPutBotResponseclarificationPromptTypeDef,
        "abortStatement": ClientPutBotResponseabortStatementTypeDef,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": Literal["en-US", "en-GB", "de-DE"],
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
    },
    total=False,
)

ClientPutIntentConclusionStatementmessagesTypeDef = TypedDict(
    "ClientPutIntentConclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentConclusionStatementTypeDef = TypedDict(
    "ClientPutIntentConclusionStatementTypeDef",
    {"messages": List[ClientPutIntentConclusionStatementmessagesTypeDef], "responseCard": str},
    total=False,
)

ClientPutIntentConfirmationPromptmessagesTypeDef = TypedDict(
    "ClientPutIntentConfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentConfirmationPromptTypeDef = TypedDict(
    "ClientPutIntentConfirmationPromptTypeDef",
    {
        "messages": List[ClientPutIntentConfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

_RequiredClientPutIntentDialogCodeHookTypeDef = TypedDict(
    "_RequiredClientPutIntentDialogCodeHookTypeDef", {"uri": str}
)
_OptionalClientPutIntentDialogCodeHookTypeDef = TypedDict(
    "_OptionalClientPutIntentDialogCodeHookTypeDef", {"messageVersion": str}, total=False
)


class ClientPutIntentDialogCodeHookTypeDef(
    _RequiredClientPutIntentDialogCodeHookTypeDef, _OptionalClientPutIntentDialogCodeHookTypeDef
):
    pass


_RequiredClientPutIntentFollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentFollowUpPromptpromptmessagesTypeDef",
    {"contentType": Literal["PlainText", "SSML", "CustomPayload"]},
)
_OptionalClientPutIntentFollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentFollowUpPromptpromptmessagesTypeDef",
    {"content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentFollowUpPromptpromptmessagesTypeDef(
    _RequiredClientPutIntentFollowUpPromptpromptmessagesTypeDef,
    _OptionalClientPutIntentFollowUpPromptpromptmessagesTypeDef,
):
    pass


_RequiredClientPutIntentFollowUpPromptpromptTypeDef = TypedDict(
    "_RequiredClientPutIntentFollowUpPromptpromptTypeDef",
    {"messages": List[ClientPutIntentFollowUpPromptpromptmessagesTypeDef]},
)
_OptionalClientPutIntentFollowUpPromptpromptTypeDef = TypedDict(
    "_OptionalClientPutIntentFollowUpPromptpromptTypeDef",
    {"maxAttempts": int, "responseCard": str},
    total=False,
)


class ClientPutIntentFollowUpPromptpromptTypeDef(
    _RequiredClientPutIntentFollowUpPromptpromptTypeDef,
    _OptionalClientPutIntentFollowUpPromptpromptTypeDef,
):
    pass


ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentFollowUpPromptrejectionStatementTypeDef = TypedDict(
    "ClientPutIntentFollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentFollowUpPromptrejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

_RequiredClientPutIntentFollowUpPromptTypeDef = TypedDict(
    "_RequiredClientPutIntentFollowUpPromptTypeDef",
    {"prompt": ClientPutIntentFollowUpPromptpromptTypeDef},
)
_OptionalClientPutIntentFollowUpPromptTypeDef = TypedDict(
    "_OptionalClientPutIntentFollowUpPromptTypeDef",
    {"rejectionStatement": ClientPutIntentFollowUpPromptrejectionStatementTypeDef},
    total=False,
)


class ClientPutIntentFollowUpPromptTypeDef(
    _RequiredClientPutIntentFollowUpPromptTypeDef, _OptionalClientPutIntentFollowUpPromptTypeDef
):
    pass


ClientPutIntentFulfillmentActivitycodeHookTypeDef = TypedDict(
    "ClientPutIntentFulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)

_RequiredClientPutIntentFulfillmentActivityTypeDef = TypedDict(
    "_RequiredClientPutIntentFulfillmentActivityTypeDef",
    {"type": Literal["ReturnIntent", "CodeHook"]},
)
_OptionalClientPutIntentFulfillmentActivityTypeDef = TypedDict(
    "_OptionalClientPutIntentFulfillmentActivityTypeDef",
    {"codeHook": ClientPutIntentFulfillmentActivitycodeHookTypeDef},
    total=False,
)


class ClientPutIntentFulfillmentActivityTypeDef(
    _RequiredClientPutIntentFulfillmentActivityTypeDef,
    _OptionalClientPutIntentFulfillmentActivityTypeDef,
):
    pass


ClientPutIntentRejectionStatementmessagesTypeDef = TypedDict(
    "ClientPutIntentRejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentRejectionStatementTypeDef = TypedDict(
    "ClientPutIntentRejectionStatementTypeDef",
    {"messages": List[ClientPutIntentRejectionStatementmessagesTypeDef], "responseCard": str},
    total=False,
)

ClientPutIntentResponseconclusionStatementmessagesTypeDef = TypedDict(
    "ClientPutIntentResponseconclusionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentResponseconclusionStatementTypeDef = TypedDict(
    "ClientPutIntentResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientPutIntentResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "ClientPutIntentResponseconfirmationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentResponseconfirmationPromptTypeDef = TypedDict(
    "ClientPutIntentResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientPutIntentResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientPutIntentResponsedialogCodeHookTypeDef = TypedDict(
    "ClientPutIntentResponsedialogCodeHookTypeDef", {"uri": str, "messageVersion": str}, total=False
)

ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentResponsefollowUpPromptpromptTypeDef = TypedDict(
    "ClientPutIntentResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientPutIntentResponsefollowUpPromptTypeDef = TypedDict(
    "ClientPutIntentResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientPutIntentResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)

ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)

ClientPutIntentResponsefulfillmentActivityTypeDef = TypedDict(
    "ClientPutIntentResponsefulfillmentActivityTypeDef",
    {
        "type": Literal["ReturnIntent", "CodeHook"],
        "codeHook": ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)

ClientPutIntentResponserejectionStatementmessagesTypeDef = TypedDict(
    "ClientPutIntentResponserejectionStatementmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentResponserejectionStatementTypeDef = TypedDict(
    "ClientPutIntentResponserejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)

ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "ClientPutIntentResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

ClientPutIntentResponseslotsTypeDef = TypedDict(
    "ClientPutIntentResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientPutIntentResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": Literal["NONE", "DEFAULT_OBFUSCATION"],
    },
    total=False,
)

ClientPutIntentResponseTypeDef = TypedDict(
    "ClientPutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientPutIntentResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientPutIntentResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientPutIntentResponserejectionStatementTypeDef,
        "followUpPrompt": ClientPutIntentResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientPutIntentResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientPutIntentResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientPutIntentResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
    },
    total=False,
)

ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef",
    {
        "contentType": Literal["PlainText", "SSML", "CustomPayload"],
        "content": str,
        "groupNumber": int,
    },
    total=False,
)

ClientPutIntentSlotsvalueElicitationPromptTypeDef = TypedDict(
    "ClientPutIntentSlotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientPutIntentSlotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)

_RequiredClientPutIntentSlotsTypeDef = TypedDict(
    "_RequiredClientPutIntentSlotsTypeDef", {"name": str}
)
_OptionalClientPutIntentSlotsTypeDef = TypedDict(
    "_OptionalClientPutIntentSlotsTypeDef",
    {
        "description": str,
        "slotConstraint": Literal["Required", "Optional"],
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientPutIntentSlotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": Literal["NONE", "DEFAULT_OBFUSCATION"],
    },
    total=False,
)


class ClientPutIntentSlotsTypeDef(
    _RequiredClientPutIntentSlotsTypeDef, _OptionalClientPutIntentSlotsTypeDef
):
    pass


_RequiredClientPutSlotTypeEnumerationValuesTypeDef = TypedDict(
    "_RequiredClientPutSlotTypeEnumerationValuesTypeDef", {"value": str}
)
_OptionalClientPutSlotTypeEnumerationValuesTypeDef = TypedDict(
    "_OptionalClientPutSlotTypeEnumerationValuesTypeDef", {"synonyms": List[str]}, total=False
)


class ClientPutSlotTypeEnumerationValuesTypeDef(
    _RequiredClientPutSlotTypeEnumerationValuesTypeDef,
    _OptionalClientPutSlotTypeEnumerationValuesTypeDef,
):
    pass


ClientPutSlotTypeResponseenumerationValuesTypeDef = TypedDict(
    "ClientPutSlotTypeResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)

ClientPutSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef = TypedDict(
    "ClientPutSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef",
    {"pattern": str},
    total=False,
)

ClientPutSlotTypeResponseslotTypeConfigurationsTypeDef = TypedDict(
    "ClientPutSlotTypeResponseslotTypeConfigurationsTypeDef",
    {
        "regexConfiguration": ClientPutSlotTypeResponseslotTypeConfigurationsregexConfigurationTypeDef
    },
    total=False,
)

ClientPutSlotTypeResponseTypeDef = TypedDict(
    "ClientPutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientPutSlotTypeResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"],
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[ClientPutSlotTypeResponseslotTypeConfigurationsTypeDef],
    },
    total=False,
)

ClientPutSlotTypeSlotTypeConfigurationsregexConfigurationTypeDef = TypedDict(
    "ClientPutSlotTypeSlotTypeConfigurationsregexConfigurationTypeDef", {"pattern": str}
)

ClientPutSlotTypeSlotTypeConfigurationsTypeDef = TypedDict(
    "ClientPutSlotTypeSlotTypeConfigurationsTypeDef",
    {"regexConfiguration": ClientPutSlotTypeSlotTypeConfigurationsregexConfigurationTypeDef},
    total=False,
)

ClientStartImportResponseTypeDef = TypedDict(
    "ClientStartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": Literal["BOT", "INTENT", "SLOT_TYPE"],
        "mergeStrategy": Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
        "importId": str,
        "importStatus": Literal["IN_PROGRESS", "COMPLETE", "FAILED"],
        "createdDate": datetime,
    },
    total=False,
)

LogSettingsResponseTypeDef = TypedDict(
    "LogSettingsResponseTypeDef",
    {
        "logType": Literal["AUDIO", "TEXT"],
        "destination": Literal["CLOUDWATCH_LOGS", "S3"],
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

ConversationLogsResponseTypeDef = TypedDict(
    "ConversationLogsResponseTypeDef",
    {"logSettings": List[LogSettingsResponseTypeDef], "iamRoleArn": str},
    total=False,
)

BotAliasMetadataTypeDef = TypedDict(
    "BotAliasMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ConversationLogsResponseTypeDef,
    },
    total=False,
)

GetBotAliasesResponseTypeDef = TypedDict(
    "GetBotAliasesResponseTypeDef",
    {"BotAliases": List[BotAliasMetadataTypeDef], "nextToken": str},
    total=False,
)

BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": Literal["Facebook", "Slack", "Twilio-Sms", "Kik"],
        "botConfiguration": Dict[str, str],
        "status": Literal["IN_PROGRESS", "CREATED", "FAILED"],
        "failureReason": str,
    },
    total=False,
)

GetBotChannelAssociationsResponseTypeDef = TypedDict(
    "GetBotChannelAssociationsResponseTypeDef",
    {"botChannelAssociations": List[BotChannelAssociationTypeDef], "nextToken": str},
    total=False,
)

BotMetadataTypeDef = TypedDict(
    "BotMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "status": Literal["BUILDING", "READY", "READY_BASIC_TESTING", "FAILED", "NOT_BUILT"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

GetBotVersionsResponseTypeDef = TypedDict(
    "GetBotVersionsResponseTypeDef",
    {"bots": List[BotMetadataTypeDef], "nextToken": str},
    total=False,
)

GetBotsResponseTypeDef = TypedDict(
    "GetBotsResponseTypeDef", {"bots": List[BotMetadataTypeDef], "nextToken": str}, total=False
)

BuiltinIntentMetadataTypeDef = TypedDict(
    "BuiltinIntentMetadataTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)

GetBuiltinIntentsResponseTypeDef = TypedDict(
    "GetBuiltinIntentsResponseTypeDef",
    {"intents": List[BuiltinIntentMetadataTypeDef], "nextToken": str},
    total=False,
)

BuiltinSlotTypeMetadataTypeDef = TypedDict(
    "BuiltinSlotTypeMetadataTypeDef",
    {"signature": str, "supportedLocales": List[Literal["en-US", "en-GB", "de-DE"]]},
    total=False,
)

GetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "GetBuiltinSlotTypesResponseTypeDef",
    {"slotTypes": List[BuiltinSlotTypeMetadataTypeDef], "nextToken": str},
    total=False,
)

IntentMetadataTypeDef = TypedDict(
    "IntentMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

GetIntentVersionsResponseTypeDef = TypedDict(
    "GetIntentVersionsResponseTypeDef",
    {"intents": List[IntentMetadataTypeDef], "nextToken": str},
    total=False,
)

GetIntentsResponseTypeDef = TypedDict(
    "GetIntentsResponseTypeDef",
    {"intents": List[IntentMetadataTypeDef], "nextToken": str},
    total=False,
)

SlotTypeMetadataTypeDef = TypedDict(
    "SlotTypeMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

GetSlotTypeVersionsResponseTypeDef = TypedDict(
    "GetSlotTypeVersionsResponseTypeDef",
    {"slotTypes": List[SlotTypeMetadataTypeDef], "nextToken": str},
    total=False,
)

GetSlotTypesResponseTypeDef = TypedDict(
    "GetSlotTypesResponseTypeDef",
    {"slotTypes": List[SlotTypeMetadataTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
