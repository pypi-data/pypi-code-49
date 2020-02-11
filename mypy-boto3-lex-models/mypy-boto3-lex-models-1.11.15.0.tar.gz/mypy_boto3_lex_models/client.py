"""
Main interface for lex-models service client

Usage::

    import boto3
    from mypy_boto3.lex_models import LexModelBuildingServiceClient

    session = boto3.Session()

    client: LexModelBuildingServiceClient = boto3.client("lex-models")
    session_client: LexModelBuildingServiceClient = session.client("lex-models")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_lex_models.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_lex_models.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_lex_models.type_defs import (
    ClientCreateBotVersionResponseTypeDef,
    ClientCreateIntentVersionResponseTypeDef,
    ClientCreateSlotTypeVersionResponseTypeDef,
    ClientGetBotAliasResponseTypeDef,
    ClientGetBotAliasesResponseTypeDef,
    ClientGetBotChannelAssociationResponseTypeDef,
    ClientGetBotChannelAssociationsResponseTypeDef,
    ClientGetBotResponseTypeDef,
    ClientGetBotVersionsResponseTypeDef,
    ClientGetBotsResponseTypeDef,
    ClientGetBuiltinIntentResponseTypeDef,
    ClientGetBuiltinIntentsResponseTypeDef,
    ClientGetBuiltinSlotTypesResponseTypeDef,
    ClientGetExportResponseTypeDef,
    ClientGetImportResponseTypeDef,
    ClientGetIntentResponseTypeDef,
    ClientGetIntentVersionsResponseTypeDef,
    ClientGetIntentsResponseTypeDef,
    ClientGetSlotTypeResponseTypeDef,
    ClientGetSlotTypeVersionsResponseTypeDef,
    ClientGetSlotTypesResponseTypeDef,
    ClientGetUtterancesViewResponseTypeDef,
    ClientPutBotAbortStatementTypeDef,
    ClientPutBotAliasConversationLogsTypeDef,
    ClientPutBotAliasResponseTypeDef,
    ClientPutBotClarificationPromptTypeDef,
    ClientPutBotIntentsTypeDef,
    ClientPutBotResponseTypeDef,
    ClientPutIntentConclusionStatementTypeDef,
    ClientPutIntentConfirmationPromptTypeDef,
    ClientPutIntentDialogCodeHookTypeDef,
    ClientPutIntentFollowUpPromptTypeDef,
    ClientPutIntentFulfillmentActivityTypeDef,
    ClientPutIntentRejectionStatementTypeDef,
    ClientPutIntentResponseTypeDef,
    ClientPutIntentSlotsTypeDef,
    ClientPutSlotTypeEnumerationValuesTypeDef,
    ClientPutSlotTypeResponseTypeDef,
    ClientPutSlotTypeSlotTypeConfigurationsTypeDef,
    ClientStartImportResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LexModelBuildingServiceClient",)


class LexModelBuildingServiceClient:
    """
    [LexModelBuildingService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.can_paginate)
        """

    def create_bot_version(
        self, name: str, checksum: str = None
    ) -> ClientCreateBotVersionResponseTypeDef:
        """
        [Client.create_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.create_bot_version)
        """

    def create_intent_version(
        self, name: str, checksum: str = None
    ) -> ClientCreateIntentVersionResponseTypeDef:
        """
        [Client.create_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.create_intent_version)
        """

    def create_slot_type_version(
        self, name: str, checksum: str = None
    ) -> ClientCreateSlotTypeVersionResponseTypeDef:
        """
        [Client.create_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.create_slot_type_version)
        """

    def delete_bot(self, name: str) -> None:
        """
        [Client.delete_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot)
        """

    def delete_bot_alias(self, name: str, botName: str) -> None:
        """
        [Client.delete_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_alias)
        """

    def delete_bot_channel_association(self, name: str, botName: str, botAlias: str) -> None:
        """
        [Client.delete_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_channel_association)
        """

    def delete_bot_version(self, name: str, version: str) -> None:
        """
        [Client.delete_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_version)
        """

    def delete_intent(self, name: str) -> None:
        """
        [Client.delete_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent)
        """

    def delete_intent_version(self, name: str, version: str) -> None:
        """
        [Client.delete_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent_version)
        """

    def delete_slot_type(self, name: str) -> None:
        """
        [Client.delete_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type)
        """

    def delete_slot_type_version(self, name: str, version: str) -> None:
        """
        [Client.delete_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type_version)
        """

    def delete_utterances(self, botName: str, userId: str) -> None:
        """
        [Client.delete_utterances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.delete_utterances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.generate_presigned_url)
        """

    def get_bot(self, name: str, versionOrAlias: str) -> ClientGetBotResponseTypeDef:
        """
        [Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot)
        """

    def get_bot_alias(self, name: str, botName: str) -> ClientGetBotAliasResponseTypeDef:
        """
        [Client.get_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_alias)
        """

    def get_bot_aliases(
        self, botName: str, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> ClientGetBotAliasesResponseTypeDef:
        """
        [Client.get_bot_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_aliases)
        """

    def get_bot_channel_association(
        self, name: str, botName: str, botAlias: str
    ) -> ClientGetBotChannelAssociationResponseTypeDef:
        """
        [Client.get_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_association)
        """

    def get_bot_channel_associations(
        self,
        botName: str,
        botAlias: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None,
    ) -> ClientGetBotChannelAssociationsResponseTypeDef:
        """
        [Client.get_bot_channel_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_associations)
        """

    def get_bot_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetBotVersionsResponseTypeDef:
        """
        [Client.get_bot_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_versions)
        """

    def get_bots(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> ClientGetBotsResponseTypeDef:
        """
        [Client.get_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_bots)
        """

    def get_builtin_intent(self, signature: str) -> ClientGetBuiltinIntentResponseTypeDef:
        """
        [Client.get_builtin_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intent)
        """

    def get_builtin_intents(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetBuiltinIntentsResponseTypeDef:
        """
        [Client.get_builtin_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intents)
        """

    def get_builtin_slot_types(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetBuiltinSlotTypesResponseTypeDef:
        """
        [Client.get_builtin_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_slot_types)
        """

    def get_export(
        self,
        name: str,
        version: str,
        resourceType: Literal["BOT", "INTENT", "SLOT_TYPE"],
        exportType: Literal["ALEXA_SKILLS_KIT", "LEX"],
    ) -> ClientGetExportResponseTypeDef:
        """
        [Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_export)
        """

    def get_import(self, importId: str) -> ClientGetImportResponseTypeDef:
        """
        [Client.get_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_import)
        """

    def get_intent(self, name: str, version: str) -> ClientGetIntentResponseTypeDef:
        """
        [Client.get_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent)
        """

    def get_intent_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetIntentVersionsResponseTypeDef:
        """
        [Client.get_intent_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent_versions)
        """

    def get_intents(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> ClientGetIntentsResponseTypeDef:
        """
        [Client.get_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_intents)
        """

    def get_slot_type(self, name: str, version: str) -> ClientGetSlotTypeResponseTypeDef:
        """
        [Client.get_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type)
        """

    def get_slot_type_versions(
        self, name: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetSlotTypeVersionsResponseTypeDef:
        """
        [Client.get_slot_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type_versions)
        """

    def get_slot_types(
        self, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> ClientGetSlotTypesResponseTypeDef:
        """
        [Client.get_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_types)
        """

    def get_utterances_view(
        self, botName: str, botVersions: List[str], statusType: Literal["Detected", "Missed"]
    ) -> ClientGetUtterancesViewResponseTypeDef:
        """
        [Client.get_utterances_view documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.get_utterances_view)
        """

    def put_bot(
        self,
        name: str,
        locale: Literal["en-US", "en-GB", "de-DE"],
        childDirected: bool,
        description: str = None,
        intents: List[ClientPutBotIntentsTypeDef] = None,
        clarificationPrompt: ClientPutBotClarificationPromptTypeDef = None,
        abortStatement: ClientPutBotAbortStatementTypeDef = None,
        idleSessionTTLInSeconds: int = None,
        voiceId: str = None,
        checksum: str = None,
        processBehavior: Literal["SAVE", "BUILD"] = None,
        detectSentiment: bool = None,
        createVersion: bool = None,
    ) -> ClientPutBotResponseTypeDef:
        """
        [Client.put_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot)
        """

    def put_bot_alias(
        self,
        name: str,
        botVersion: str,
        botName: str,
        description: str = None,
        checksum: str = None,
        conversationLogs: ClientPutBotAliasConversationLogsTypeDef = None,
    ) -> ClientPutBotAliasResponseTypeDef:
        """
        [Client.put_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot_alias)
        """

    def put_intent(
        self,
        name: str,
        description: str = None,
        slots: List[ClientPutIntentSlotsTypeDef] = None,
        sampleUtterances: List[str] = None,
        confirmationPrompt: ClientPutIntentConfirmationPromptTypeDef = None,
        rejectionStatement: ClientPutIntentRejectionStatementTypeDef = None,
        followUpPrompt: ClientPutIntentFollowUpPromptTypeDef = None,
        conclusionStatement: ClientPutIntentConclusionStatementTypeDef = None,
        dialogCodeHook: ClientPutIntentDialogCodeHookTypeDef = None,
        fulfillmentActivity: ClientPutIntentFulfillmentActivityTypeDef = None,
        parentIntentSignature: str = None,
        checksum: str = None,
        createVersion: bool = None,
    ) -> ClientPutIntentResponseTypeDef:
        """
        [Client.put_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.put_intent)
        """

    def put_slot_type(
        self,
        name: str,
        description: str = None,
        enumerationValues: List[ClientPutSlotTypeEnumerationValuesTypeDef] = None,
        checksum: str = None,
        valueSelectionStrategy: Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"] = None,
        createVersion: bool = None,
        parentSlotTypeSignature: str = None,
        slotTypeConfigurations: List[ClientPutSlotTypeSlotTypeConfigurationsTypeDef] = None,
    ) -> ClientPutSlotTypeResponseTypeDef:
        """
        [Client.put_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.put_slot_type)
        """

    def start_import(
        self,
        payload: bytes,
        resourceType: Literal["BOT", "INTENT", "SLOT_TYPE"],
        mergeStrategy: Literal["OVERWRITE_LATEST", "FAIL_ON_CONFLICT"],
    ) -> ClientStartImportResponseTypeDef:
        """
        [Client.start_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Client.start_import)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bot_aliases"]
    ) -> "paginator_scope.GetBotAliasesPaginator":
        """
        [Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bot_channel_associations"]
    ) -> "paginator_scope.GetBotChannelAssociationsPaginator":
        """
        [Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bot_versions"]
    ) -> "paginator_scope.GetBotVersionsPaginator":
        """
        [Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bots"]
    ) -> "paginator_scope.GetBotsPaginator":
        """
        [Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_intents"]
    ) -> "paginator_scope.GetBuiltinIntentsPaginator":
        """
        [Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_slot_types"]
    ) -> "paginator_scope.GetBuiltinSlotTypesPaginator":
        """
        [Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_intent_versions"]
    ) -> "paginator_scope.GetIntentVersionsPaginator":
        """
        [Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_intents"]
    ) -> "paginator_scope.GetIntentsPaginator":
        """
        [Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_slot_type_versions"]
    ) -> "paginator_scope.GetSlotTypeVersionsPaginator":
        """
        [Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_slot_types"]
    ) -> "paginator_scope.GetSlotTypesPaginator":
        """
        [Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    PreconditionFailedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
