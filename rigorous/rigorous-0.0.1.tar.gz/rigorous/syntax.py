# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses
import functools
import operator
import re

import miniparse


_LATEX_ESCAPE = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\lettertilde{}",
    "^": r"\letterhat{}",
    "\\": r"\letterbackslash{}",
}

_latex_escape_pattern = re.compile(
    "|".join(re.escape(source) for source in _LATEX_ESCAPE)
)


def _latex_escape(source: str) -> str:
    return _latex_escape_pattern.sub(lambda match: _LATEX_ESCAPE[match[0]], source)


SYNTAX = """
<expr> ::= ‘True’ | ‘False’ | ‘None’ | ‘Ellipsis’           (* constants *)
         | INTEGER | FLOAT | STRING                         (* literals *)
         | ‘[’ [<elements>] ‘]’ | ‘(’ [<elements>] ‘)’      (* sequences *)
         | ‘{’ [<entries>] ‘}’                              (* dictionaries *)
         | UNARY_OPERATOR <expr>                            (* unary operators *)
         | <expr> BINARY_OPERATOR <expr>                    (* binary operators *)
         | ‘yield’ <expr>                                   (* yield *)
         | <target>;                                        (* target *)


<elements> ::= <expr> [‘::’ <elements>];

<entries> ::= <entry> [‘::’ <entries>];
<entry> ::= <expr> ‘:’ <expr>;


<target> ::= IDENTIFER
           | <expr> ‘.’ IDENTIFIER | <expr> ‘[’ <expr> ‘]’
           | ‘[’ <target-list> ‘]’;
<target-list> ::= <target> | <target> ‘::’ <targets>;

<stmt> ::= <expr>
         | <target> ‘=’ <expr>
         | ‘pass’
         | ‘return’ <expr>
         | ‘raise’ <expr>
         | ‘del’ <target>
         | ‘break’ | ‘continue’                                     (* loop-control *)
         | ‘for’ <target> ‘in’ <expr> ‘do’ <body> ‘else’ <body>     (* for-loop *)
         | ‘while’ <expr> ‘do’ <body> ‘else’ <body>                 (* while-loop *)
         | ‘if’ <expr> ‘then’ <body> ‘else’ <body>                  (* conditional *)
         | <definition>;


<arguments> ::= [<positional-arguments>] [<star-argument>] <keyword-arguments> [<kwargs>];

<positional-argument> ::= [‘*’] <expr>;
<positional-arguments> ::= <positional-argument> [‘::’ <positional-arguments>];

<keyword-argument> ::= IDENTIFIER ‘=’ <expr>;



<definition> ::= ‘@’ <expr> <definition>
               | <class-definition>
               | <function-definition>;


<class-definition> ::= ‘class’ IDENTIFIER ‘(’ [<arguments>] ‘)’ ‘:’ <body>;

<function-definition> ::= ‘def’ IDENTIFIER;

<body> ::= <stmt> | <stmt> ‘;’ <body>;


"""


class TokenType(miniparse.regex.TokenTypeEnum):
    DEFINE = r"::="
    ALTERNATIVE = r"\|"

    SEMICOLON = r";"

    COMMENT = r"\(\*(.|\s)*?\*\)"

    LEFT_PARENTHESIS = r"\("
    RIGHT_PARENTHESIS = r"\)"

    LEFT_BRACKET = r"\["
    RIGHT_BRACKET = r"\]"

    LITERAL_TERMINAL = r"‘(?P<literal>[^’]*)’"
    NAMED_TERMINAL = r"\w+"

    TYPE_NAME = r"<(?P<type_name>(\w|-)+)>"

    WHITESPACE = r"\s+"
    ERROR = r"."


lexer = TokenType.create_lexer()
stream_options = miniparse.stream.Options(
    ignore_types={TokenType.WHITESPACE, TokenType.COMMENT},
    error_types={TokenType.ERROR},
)


@dataclasses.dataclass(frozen=True)
class Context:
    patterns: t.Dict[str, t.Sequence[Pattern]] = dataclasses.field(default_factory=dict)


Token = miniparse.regex.RegexToken[TokenType]
Stream = miniparse.stream.TokenStream[Token, TokenType]


class Pattern:
    position: t.Optional[miniparse.Position] = None


class Leaf(Pattern):
    pass


@dataclasses.dataclass
class Named(Leaf):
    name: str


@dataclasses.dataclass
class Literal(Leaf):
    literal: str


@dataclasses.dataclass
class Optional(Pattern):
    pattern: Pattern


@dataclasses.dataclass
class Sequence(Pattern):
    patterns: t.Tuple[Pattern, ...]


@dataclasses.dataclass
class Reference(Pattern):
    name: str


def _parse_sequence(stream: Stream, ctx: Context) -> Sequence:
    components: t.List[Pattern] = []
    sequence_position = stream.position
    while True:
        pattern: Pattern
        position = stream.position
        if stream.check(TokenType.LITERAL_TERMINAL):
            literal = stream.consume().match["literal"]
            pattern = Literal(literal)
        elif stream.check(TokenType.NAMED_TERMINAL):
            name = stream.consume().text
            pattern = Named(name)
        elif stream.check(TokenType.TYPE_NAME):
            name = stream.consume().match["type_name"]
            pattern = Reference(name)
        elif stream.accept(TokenType.LEFT_PARENTHESIS):
            pattern = _parse_sequence(stream, ctx)
            stream.expect(TokenType.RIGHT_PARENTHESIS)
        elif stream.accept(TokenType.LEFT_BRACKET):
            pattern = Optional(_parse_sequence(stream, ctx))
            stream.expect(TokenType.RIGHT_BRACKET)
        else:
            break
        pattern.position = position
        components.append(pattern)
    sequence = Sequence(tuple(components))
    sequence.position = sequence_position
    return sequence


def _parse_constructor_type(stream: Stream, ctx: Context) -> None:
    name = stream.expect(TokenType.TYPE_NAME).match["type_name"]
    stream.expect("::=")
    patterns = []
    while True:
        patterns.append(_parse_sequence(stream, ctx))
        if not stream.accept("|"):
            stream.expect(";")
            break
    ctx.patterns[name] = patterns


unit = lexer.lex(SYNTAX)
stream = unit.create_stream(stream_options)

context = Context()
while stream.check(TokenType.TYPE_NAME):
    _parse_constructor_type(stream, context)


LATEX_NAMED_MAP = {
    "INTEGER": r"z \in \Int",
    "FLOAT": r"x \in \mb{F}",
    "STRING": r"s \in \mb{S}",
}


@functools.singledispatch
def _latexify_pattern(pattern: Pattern) -> str:
    raise NotImplementedError(f"no implementation for {pattern}")


@_latexify_pattern.register
def _latexify_literal(pattern: Literal) -> str:
    if pattern.literal.isalpha():
        return fr"\textcolor{{koehlma-blue}}{{\texttt{{{_latex_escape(pattern.literal)}}}}}"
    else:
        return fr"\textcolor{{koehlma-orange}}{{\texttt{{{_latex_escape(pattern.literal)}}}}}"


@_latexify_pattern.register
def _latexify_sequence(pattern: Sequence) -> str:
    return "\\ ".join(map(_latexify_pattern, pattern.patterns))


@_latexify_pattern.register
def _latexify_named(pattern: Named) -> str:
    try:
        return fr"\textcolor{{koehlma-green}}{{{LATEX_NAMED_MAP[pattern.name]}}}"
    except KeyError:
        return (
            fr"\textcolor{{koehlma-green}}{{\texttt{{{_latex_escape(pattern.name)}}}}}"
        )


@_latexify_pattern.register
def _latexify_reference(pattern: Reference) -> str:
    return fr"\textcolor{{black}}{{\langle\textit{{{pattern.name}}}\mskip 1mu\rangle}}"


@_latexify_pattern.register
def _latexify_optional(pattern: Optional) -> str:
    return fr"\left[ {_latexify_pattern(pattern.pattern)} \right]"


lines = []
for name, patterns in context.patterns.items():
    line = [
        fr"\textcolor{{black}}{{\langle\textit{{{name}}}\mskip 1mu\rangle}}"
        fr"\Coloneqq &\ "
    ]
    assert patterns[0].position is not None
    current_row = patterns[0].position.row
    line_patterns: t.List[str] = []
    for pattern in patterns:
        assert pattern.position is not None
        if pattern.position.row != current_row:
            line.append("\\ \\ |\\ \\ ".join(line_patterns))
            line_patterns = []
            lines.append(" ".join(line))
            line = [fr"|\, &\ "]
            current_row = pattern.position.row
        line_patterns.append(_latexify_pattern(pattern))
    if line_patterns:
        line.append("\\ \\ |\\ \\ ".join(line_patterns))
        line_patterns = []
        lines.append(" ".join(line))


LATEX_FULL_SYNTAX = "\\\\\n".join(lines)

