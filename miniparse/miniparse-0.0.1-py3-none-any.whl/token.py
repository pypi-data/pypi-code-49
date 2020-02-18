# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses


TokenTypeT = t.TypeVar("TokenTypeT")


@dataclasses.dataclass(frozen=True)
class Position:
    row: int = 0
    column: int = 0

    def advance(self, text: str) -> Position:
        if "\n" in text:
            row = self.row + text.count("\n")
            column = len(text.rpartition("\n")[2])
        else:
            row = self.row
            column = self.column + len(text)
        return Position(row, column)


@dataclasses.dataclass(frozen=True)
class Token(t.Generic[TokenTypeT]):
    token_type: TokenTypeT

    text: str

    index: int

    start_position: Position
    end_position: Position
