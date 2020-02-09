# -*- coding: utf-8 -*-

import re

from pygments.lexer import Lexer, RegexLexer, include, words, do_insertions, bygroups
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic


line_re  = re.compile('.*?\n')


class CustomSLexer(RegexLexer):
    """
    For S, S-plus, and R source code.

    .. versionadded:: 0.10
    """

    name = 'S'
    aliases = ['splus', 's', 'r']
    filenames = ['*.S', '*.R', '.Rhistory', '.Rprofile', '.Renviron']
    mimetypes = ['text/S-plus', 'text/S', 'text/x-r-source', 'text/x-r',
                 'text/x-R', 'text/x-r-history', 'text/x-r-profile']

    valid_name = r'(?:`[^`\\]*(?:\\.[^`\\]*)*`)|(?:(?:[a-zA-z]|[_.][^0-9])[\w_.]*)'
    tokens = {
        'comments': [
            (r'#.*$', Comment.Single),
        ],
        'valid_name': [
            (valid_name, Name),
        ],
        'punctuation': [
            (r'\[{1,2}|\]{1,2}|\(|\)|;|,', Punctuation),
        ],
        'keywords': [
            (r'(if|else|for|while|repeat|in|next|break|return|switch|function)'
             r'(?![\w.])',
             Keyword.Reserved),
            (r'(array|category|character|complex|double|function|integer|list|'
             r'logical|matrix|numeric|vector|data.frame|c)'
             r'(?![\w.])',
             Keyword.Type),
            (r'(library|require|attach|detach|source)'
             r'(?![\w.])',
             Keyword.Namespace)
        ],
        'operators': [
            (r'<<?-|->>?|-|==|<=|>=|<|>|&&?|!=|\|\|?|\?', Operator),
            (r'\*|\+|\^|/|!|%[^%]*%|=|~|\$|@|:{1,3}', Operator),
        ],
        'builtin_symbols': [
            (r'(NULL|NA(_(integer|real|complex|character)_)?|'
             r'letters|LETTERS|Inf|TRUE|FALSE|NaN|pi|\.\.(\.|[0-9]+))'
             r'(?![\w.])',
             Keyword.Constant),
            (r'(T|F)\b', Name.Builtin.Pseudo),
        ],
        'numbers': [
            # hex number
            (r'0[xX][a-fA-F0-9]+([pP][0-9]+)?[Li]?', Number.Hex),
            # decimal number
            (r'[+-]?([0-9]+(\.[0-9]+)?|\.[0-9]+|\.)([eE][+-]?[0-9]+)?[Li]?',
             Number),
        ],
        'statements': [
            include('comments'),
            # whitespaces
            (r'\s+', Text),
            (r'\'', String, 'string_squote'),
            (r'\"', String, 'string_dquote'),
            include('builtin_symbols'),
            include('valid_name'),
            include('numbers'),
            include('operators'),
        ],
        'root': [
            # calls:
            include('keywords'),
            include('punctuation'),
            ('r%s\s*(?=\()' % valid_name, Keyword.Pseudo),
            include('statements'),
            
            # blocks:
            (r'\{|\}', Punctuation),
            # (r'\{', Punctuation, 'block'),
            (r'.', Text),
        ],
        'string_squote': [
            (r'([^\'\\]|\\.)*\'', String, '#pop'),
        ],
        'string_dquote': [
            (r'([^"\\]|\\.)*"', String, '#pop'),
        ],
    }

    def analyse_text(text):
        if re.search(r'[a-z0-9_\])\s]<-(?!-)', text):
            return 0.11
