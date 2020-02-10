from dataclasses import dataclass
from enum import Enum
from typing import Any, List


class TokeniserError(Exception):
    """Error raised in the tokeniser."""


class TokenType(Enum):
    """Token type."""

    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    COMMA = ","
    PLUS = "+"
    MINUS = "-"
    SLASH = "/"
    STAR = "*"

    BANG = "!"
    EQUAL = "="
    BANG_EQUAL = "!="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="

    INT = "int"
    FLOAT = "float"
    STRING = "string"
    IDENT = "ident"

    AND = "and"
    OR = "or"

    EOF = "eof"


@dataclass
class Token:
    """Representation of a token."""

    token_type: TokenType
    lexeme: str


@dataclass
class TokenLiteral(Token):
    """Representation of a literal."""

    literal: Any


class Tokeniser:
    def __init__(self):
        self.start: int = 0
        self.current: int = 0
        self.source: str = ""
        self.tokens: List[Token] = []

    def tokenise(self, source: str) -> List[Token]:
        """Tokenise an input in a list of tokens."""
        self.source = source
        self.current = 0
        self.start = 0
        while self.current < len(self.source):
            self.start = self.current
            self.scan_token()
        return self.tokens

    def scan_token(self):
        c = self.source[self.current]
        self.current += 1
        if c.strip() == "":
            # Skip whitespace
            return
        if c in ("(", ")", ",", "+", "-", "*", "=", "/"):
            # Match characters that are unambiguously only single characters
            self.add_token(TokenType(c))
        elif c == "!":
            if self.source[self.current] == "=":
                self.add_token(TokenType.BANG_EQUAL)
                self.current += 1
            else:
                self.add_token(TokenType.BANG)
        elif c == "<":
            if self.source[self.current] == "=":
                self.current += 1
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)
        elif c == ">":
            if self.source[self.current] == "=":
                self.current += 1
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)
        elif c in ("'", '"'):
            self.string()
        elif c.isdigit():
            self.numeric()
        elif c.isalpha():
            self.identifier()
        else:
            raise TokeniserError(f"Unexpected character: '{c}'")

    def add_token(self, token_type: TokenType):
        lexeme = self.source[self.start : self.current]
        token = Token(token_type, lexeme)
        self.tokens.append(token)

    def string(self):
        while self.current < len(self.source) and self.source[self.current] not in (
            "'",
            '"',
        ):
            self.current += 1
        if self.current >= len(self.source):
            raise TokeniserError("Unterminated string")
        self.current += 1  # Consume closing quote
        lexeme = self.source[self.start : self.current]
        string = self.source[self.start + 1 : self.current - 1]
        token = TokenLiteral(TokenType.STRING, lexeme, string)
        self.tokens.append(token)

    def numeric(self):
        while self.current < len(self.source) and self.source[self.current].isdigit():
            self.current += 1

        # Invalid to finish expression with "."
        if self.current == len(self.source) - 1 and self.source[self.current] == ".":
            raise TokeniserError("Expression cannot finish with '.'")

        if self.current < len(self.source) and self.source[self.current] == ".":
            # Consume the "." so we can start consuming digits again
            self.current += 1
            if not self.source[self.current].isdigit():
                raise TokeniserError(
                    f"Expected digit after '.', found '{self.source[self.current]}'"
                )

            # Match a float
            while (
                self.current < len(self.source) and self.source[self.current].isdigit()
            ):
                self.current += 1
            float_ = self.source[self.start : self.current]
            token = TokenLiteral(TokenType.FLOAT, float_, float(float_))
            self.tokens.append(token)
        else:
            int_ = self.source[self.start : self.current]
            token = TokenLiteral(TokenType.INT, int_, int(int_))
            self.tokens.append(token)

    def identifier(self):
        #  Identifiers can be made up of letters, numbers and '_'
        while self.current < len(self.source) and (
            self.source[self.current].isalpha()
            or self.source[self.current].isdigit()
            or self.source[self.current] == "_"
        ):
            self.current += 1
        ident = self.source[self.start : self.current]
        token = TokenLiteral(TokenType.IDENT, ident, ident)
        self.tokens.append(token)
