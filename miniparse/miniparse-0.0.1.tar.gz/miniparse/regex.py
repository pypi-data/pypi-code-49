# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses
import enum
import re

from .stream import Unit
from .token import Position, Token, TokenTypeT


@dataclasses.dataclass(frozen=True)
class RegexToken(Token[TokenTypeT], t.Generic[TokenTypeT]):
    match: t.Match[str]


class TokenTypeEnum(enum.Enum):
    regex: t.Optional[str]
    description: t.Optional[str]

    pseudo: bool

    def __init__(self, regex_or_description: str, pseudo: bool = False) -> None:
        if pseudo:
            self.regex = None
            self.description = regex_or_description
        else:
            self.regex = regex_or_description
            self.description = None
        self.pseudo = pseudo

    @classmethod
    def compile_regex(cls) -> t.Pattern[str]:
        return re.compile(
            r"|".join(
                f"(?P<{token_type.name}>{token_type.regex})"
                for token_type in cls
                if token_type.regex is not None
            )
        )

    @classmethod
    def create_lexer(cls: t.Type[TokenTypeEnumT]) -> Lexer[TokenTypeEnumT]:
        return Lexer(cls)


TokenTypeEnumT = t.TypeVar("TokenTypeEnumT", bound=TokenTypeEnum)


class Lexer(t.Generic[TokenTypeEnumT]):
    _token_type_enum: t.Type[TokenTypeEnumT]
    _regex: t.Pattern[str]

    def __init__(self, token_type_enum: t.Type[TokenTypeEnumT]) -> None:
        self._token_type_enum = token_type_enum
        self._regex = self._token_type_enum.compile_regex()

    def _lex(self, code: str) -> t.Iterator[RegexToken[TokenTypeEnumT]]:
        start_position = Position()
        end_position = Position()
        for index, match in enumerate(self._regex.finditer(code)):
            assert isinstance(match.lastgroup, str)
            token_type = self._token_type_enum[match.lastgroup]
            text = match[0]
            end_position = start_position.advance(text)
            yield RegexToken(
                token_type, text, index, start_position, end_position, match
            )
            start_position = end_position

    def lex(self, code: str) -> Unit[RegexToken[TokenTypeEnumT]]:
        tokens: t.Sequence[RegexToken[TokenTypeEnumT]] = list(self._lex(code))
        return Unit(code, tokens)
