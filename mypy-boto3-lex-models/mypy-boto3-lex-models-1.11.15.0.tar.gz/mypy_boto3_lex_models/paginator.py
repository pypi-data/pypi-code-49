"""
Main interface for lex-models service client paginators.

Usage::

    import boto3
    from mypy_boto3.lex_models import (
        GetBotAliasesPaginator,
        GetBotChannelAssociationsPaginator,
        GetBotVersionsPaginator,
        GetBotsPaginator,
        GetBuiltinIntentsPaginator,
        GetBuiltinSlotTypesPaginator,
        GetIntentVersionsPaginator,
        GetIntentsPaginator,
        GetSlotTypeVersionsPaginator,
        GetSlotTypesPaginator,
    )

    client: LexModelBuildingServiceClient = boto3.client("lex-models")

    get_bot_aliases_paginator: GetBotAliasesPaginator = client.get_paginator("get_bot_aliases")
    get_bot_channel_associations_paginator: GetBotChannelAssociationsPaginator = client.get_paginator("get_bot_channel_associations")
    get_bot_versions_paginator: GetBotVersionsPaginator = client.get_paginator("get_bot_versions")
    get_bots_paginator: GetBotsPaginator = client.get_paginator("get_bots")
    get_builtin_intents_paginator: GetBuiltinIntentsPaginator = client.get_paginator("get_builtin_intents")
    get_builtin_slot_types_paginator: GetBuiltinSlotTypesPaginator = client.get_paginator("get_builtin_slot_types")
    get_intent_versions_paginator: GetIntentVersionsPaginator = client.get_paginator("get_intent_versions")
    get_intents_paginator: GetIntentsPaginator = client.get_paginator("get_intents")
    get_slot_type_versions_paginator: GetSlotTypeVersionsPaginator = client.get_paginator("get_slot_type_versions")
    get_slot_types_paginator: GetSlotTypesPaginator = client.get_paginator("get_slot_types")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lex_models.type_defs import (
    GetBotAliasesResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetBotAliasesPaginator",
    "GetBotChannelAssociationsPaginator",
    "GetBotVersionsPaginator",
    "GetBotsPaginator",
    "GetBuiltinIntentsPaginator",
    "GetBuiltinSlotTypesPaginator",
    "GetIntentVersionsPaginator",
    "GetIntentsPaginator",
    "GetSlotTypeVersionsPaginator",
    "GetSlotTypesPaginator",
)


class GetBotAliasesPaginator(Boto3Paginator):
    """
    [Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
    """

    def paginate(
        self,
        botName: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBotAliasesResponseTypeDef, None, None]:
        """
        [GetBotAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases.paginate)
        """


class GetBotChannelAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
    """

    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBotChannelAssociationsResponseTypeDef, None, None]:
        """
        [GetBotChannelAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations.paginate)
        """


class GetBotVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
    """

    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetBotVersionsResponseTypeDef, None, None]:
        """
        [GetBotVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions.paginate)
        """


class GetBotsPaginator(Boto3Paginator):
    """
    [Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
    """

    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetBotsResponseTypeDef, None, None]:
        """
        [GetBots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots.paginate)
        """


class GetBuiltinIntentsPaginator(Boto3Paginator):
    """
    [Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
    """

    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBuiltinIntentsResponseTypeDef, None, None]:
        """
        [GetBuiltinIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents.paginate)
        """


class GetBuiltinSlotTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
    """

    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetBuiltinSlotTypesResponseTypeDef, None, None]:
        """
        [GetBuiltinSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes.paginate)
        """


class GetIntentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
    """

    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetIntentVersionsResponseTypeDef, None, None]:
        """
        [GetIntentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions.paginate)
        """


class GetIntentsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
    """

    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetIntentsResponseTypeDef, None, None]:
        """
        [GetIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents.paginate)
        """


class GetSlotTypeVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
    """

    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSlotTypeVersionsResponseTypeDef, None, None]:
        """
        [GetSlotTypeVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions.paginate)
        """


class GetSlotTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
    """

    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSlotTypesResponseTypeDef, None, None]:
        """
        [GetSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes.paginate)
        """
