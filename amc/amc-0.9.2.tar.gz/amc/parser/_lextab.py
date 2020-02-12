# _lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('BOOL', 'DECLARE', 'IDENTIFIER', 'NUMBER', 'PERM', 'STRING', 'SUBSCRIPT', 'SUM'))
_lexreflags   = 64
_lexliterals  = '+-*/;(){}=,^'
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_newline>\\n+)|(?P<t_PERM>P\\((?:[a-z0-9]+|\\{[a-z0-9 ]+\\})(?:/(?:[a-z0-9]+|\\{[a-z0-9 ]+\\}))*\\))|(?P<t_BOOL>[Tt]rue|[Ff]alse)|(?P<t_IDENTIFIER>[a-zA-Z][a-zA-Z0-9]*)|(?P<t_SUBSCRIPT>_[a-z0-9]+|_\\{[a-z0-9_ ]*\\})|(?P<t_NUMBER>\\d+)|(?P<t_STRING>" ([^"\\\\\\n]|\\\\.)* ")|(?P<t_ignore_COMMENT>\\#.*)', [None, ('t_newline', 'newline'), ('t_PERM', 'PERM'), ('t_BOOL', 'BOOL'), ('t_IDENTIFIER', 'IDENTIFIER'), ('t_SUBSCRIPT', 'SUBSCRIPT'), ('t_NUMBER', 'NUMBER'), ('t_STRING', 'STRING'), None, (None, None)])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
