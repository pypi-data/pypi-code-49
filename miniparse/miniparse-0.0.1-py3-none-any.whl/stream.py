# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import collections
import dataclasses

from .token import Position, Token, TokenTypeT


class ExhaustedStreamError(ValueError):
    pass


class InvalidSyntaxError(Exception):
    pass


Expected = t.Union[TokenTypeT, str, t.AbstractSet[TokenTypeT], t.AbstractSet[str]]

TokenT = t.TypeVar("TokenT", bound=Token[t.Any])


@dataclasses.dataclass(frozen=True)
class Unit(t.Generic[TokenT]):
    code: str
    tokens: t.Sequence[TokenT]

    def create_stream(
        self, options: t.Optional[Options[TokenTypeT]] = None
    ) -> TokenStream[TokenT, TokenTypeT]:
        return TokenStream(self, options)

    def slice_error_rows(self, row: int) -> str:
        start = max(0, row - 3)
        end = row + 1
        return "\n".join(self.code.split("\n")[start:end])


def _is_expected(expected: Expected[TokenTypeT], token: Token[TokenTypeT]) -> bool:
    if isinstance(expected, str):
        if token.text != expected:
            return False
    elif isinstance(expected, t.AbstractSet):
        if token.token_type not in expected and token.text not in expected:
            return False
    elif token.token_type is not expected:
        return False
    return True


@dataclasses.dataclass(frozen=True)
class Options(t.Generic[TokenTypeT]):
    ignore_types: t.AbstractSet[TokenTypeT] = dataclasses.field(
        default_factory=frozenset
    )
    error_types: t.AbstractSet[TokenTypeT] = dataclasses.field(
        default_factory=frozenset
    )


class TokenStream(t.Generic[TokenT, TokenTypeT]):
    unit: Unit[TokenT]

    options: Options[TokenTypeT]

    position: Position

    _iterator: t.Iterator[TokenT]
    _pending: t.Deque[TokenT]
    _exhausted: bool

    def __init__(
        self, unit: Unit[TokenT], options: t.Optional[Options[TokenTypeT]] = None,
    ):
        self.unit = unit
        self.options = options or Options()
        self.position = Position()
        self._iterator = iter(self.unit.tokens)
        self._pending = collections.deque()
        self._exhausted = False
        self._fill()

    def _fill(self, lookahead: int = 1) -> None:
        if not self._exhausted:
            try:
                while len(self._pending) < lookahead:
                    token = next(self._iterator)
                    if token.token_type not in self.options.ignore_types:
                        self._pending.append(token)
            except StopIteration:
                self._exhausted = True

    def consume(self) -> TokenT:
        if self._pending:
            token = self._pending.popleft()
            self._fill()
            try:
                self.position = self._pending[0].start_position
                if self._pending[0].token_type in self.options.error_types:
                    raise self.make_error("invalid character(s)")
            except IndexError:
                self.position = token.end_position
            return token
        else:
            raise ExhaustedStreamError("cannot consume token from exhausted stream")

    def _accept(
        self,
        expected: Expected[TokenTypeT],
        *,
        consume: bool = True,
        lookahead: int = 0,
    ) -> t.Optional[TokenT]:
        consume = consume and lookahead == 0
        self._fill(lookahead)
        if lookahead < len(self._pending):
            token = self._pending[lookahead]
            if _is_expected(expected, token):
                if consume:
                    return self.consume()
                return token
            return None
        else:
            return None

    @t.overload
    def accept(
        self, expected: Expected[TokenTypeT], *, consume: bool = True
    ) -> t.Optional[TokenT]:
        pass

    @t.overload
    def accept(
        self, expected: Expected[TokenTypeT], *, lookahead: int = 0
    ) -> t.Optional[TokenT]:
        pass

    def accept(
        self,
        expected: Expected[TokenTypeT],
        *,
        consume: bool = True,
        lookahead: int = 0,
    ) -> t.Optional[TokenT]:
        return self._accept(expected, consume=consume, lookahead=lookahead)

    @t.overload
    def expect(self, expected: Expected[TokenTypeT], *, consume: bool = True) -> TokenT:
        pass

    @t.overload
    def expect(self, expected: Expected[TokenTypeT], *, lookahead: int = 0) -> TokenT:
        pass

    def expect(
        self,
        expected: Expected[TokenTypeT],
        *,
        consume: bool = True,
        lookahead: int = 0,
    ) -> Token[TokenTypeT]:
        token = self._accept(expected, consume=consume, lookahead=lookahead)
        if token is None:
            raise self.make_error(f"expected {expected}")
        return token

    def check(self, expected: Expected[TokenTypeT], *, lookahead: int = 0) -> bool:
        return bool(self._accept(expected, consume=False, lookahead=lookahead))

    @property
    def exhausted(self) -> bool:
        return self._exhausted and not self._pending

    def make_error(self, message: str) -> InvalidSyntaxError:
        return InvalidSyntaxError(
            f"{message} at {self.position.row}:{self.position.column}\n\n"
            f"{self.unit.slice_error_rows(self.position.row)}\n"
            f"{' ' * self.position.column}^"
        )
