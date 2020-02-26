from functools import partial
import itertools as it
import re

import numpy as np
import scipy.constants as constants
import scipy.special


regex = {
    'comment': re.compile('^(?:!|//)\s*(.*)$'),
    'attribute': re.compile(
        r'''
            (?P<name>[a-z][a-z0-9_]*)
            (?:
                \s* :?= \s*
                (?P<value>
                    [a-z0-9_.\-+*/\s{}(),\"]+
                )
            )?
        ''',
        re.I | re.X
    ),
    'line': re.compile(
        r'''
        ^
        (?P<label>
            [a-z][a-z0-9_.]*
        )
        (?P<args>
            [a-z][a-z0-9_.]*
            (?:
                \s* , \s*
                [a-z][a-z0-9_.]*
            )*
        )?
        : \s*
        LINE
        \s* = \s*
        \(
        (?P<members>
            [a-z][a-z0-9_.]*
            (?:
                \s* , \s*
                [a-z][a-z0-9_.]*
            )*
        )
        \)
        ;
        ''',
        re.I | re.X
    ),
    'variable': re.compile(
        r'''
        ^
        (?:
            CONST \s*
        )?
        (?P<name>
            [a-z][a-z0-9_.]*
        )
        (?:
            ->
            (?P<attr>
                [a-z][a-z0-9_.]*
            )
        )?
        \s* :?= \s*
        (?P<value>
            [a-z0-9_.\-+*/()\s{},]+
        )
        ;
        ''',
        re.I | re.X
    )
}
regex['command'] = re.compile(
    r'''
        ^
        (?:
            (?P<label>
                [a-z][a-z0-9_.]*
            )
            : \s*
        )?
        (?P<keyword>
            [a-z][a-z0-9]*
        )
        \s*
        (?:
            , \s*
            (?P<attributes>
                %(attribute)s
                (?:
                    \s* , \s*
                    %(attribute)s
                )*
            )
        )?
        ;
    ''' % {'attribute': regex['attribute'].pattern.replace('P<name>', ':').replace('P<value>', ':')},
    re.I | re.X
)


class Statement:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.regex = regex[cls.__name__.lower()]

    def __init__(self, statement):
        super().__init__()
        self.statement = statement
        self.match = self.regex.match(statement)
        if self.match is None:
            raise ValueError(f'{statement} is not a {self.__class__.__name__}')

    def __repr__(self):
        return f'[{self.__class__.__name__}]'


class Comment(Statement):
    def __init__(self, statement):
        super().__init__(statement)
        self.text = self.match.group(1)

    def __repr__(self):
        return f'{super().__repr__()} # {self.text}'


class Command(Statement):
    def __init__(self, statement):
        super().__init__(statement)
        self.label = self.match.group('label')
        self.keyword = self.match.group('keyword')
        self.attributes = dict(map(
            lambda x: re.match(regex['attribute'], x.strip()).groups(),
            re.split(r',\s*(?![^{}]*\})', self.match.group('attributes'))
        )) if self.match.group('attributes') is not None else {}
        for name, value in self.attributes.items():
            if value is None:
                continue
            match = re.match(r'{([a-z0-9_.\-+*/]+(?:\s*,\s*[a-z0-9_.\-+*/]+)*)}', value)
            if match is not None:
                self.attributes[name] = [x.strip() for x in match.group(1).split(',')]

    def __repr__(self):
        return f'{super().__repr__()} {self.label}: {self.keyword} {self.attributes}'

    def __getitem__(self, item):
        return self.attributes[item]


class Line(Statement):
    def __init__(self, statement):
        super().__init__(statement)
        self.members = [x.strip() for x in self.match.group('members').split(',')]

    def __repr__(self):
        return f'{super().__repr__()} members = {self.members}'


class Variable(Statement):
    def __init__(self, statement):
        super().__init__(statement)
        self.name = self.match.group('name')
        self.value = self.match.group('value')

    def __repr__(self):
        return f'{super().__repr__()} {self.name} = {self.value}'


class Parser:
    _types = [Comment, Command, Line, Variable]
    _external = {x: getattr(np, x)
                 for x in ['sqrt', 'log', 'log10', 'exp', 'sin', 'cos', 'tan', 'sinh', 'cosh',
                           'tanh', 'sinc', 'abs', 'floor', 'ceil', 'round']}
    _external['asin'] = np.arcsin
    _external['acos'] = np.arccos
    _external['atan'] = np.arctan
    _external['erf'] = scipy.special.erf
    _external['erfc'] = scipy.special.erfc
    _external['ranf'] = np.random.uniform
    _external['gauss'] = np.random.normal
    _external['pi'] = np.pi
    _external['twopi'] = 2 * np.pi
    _external['degrad'] = 180 / np.pi
    _external['raddeg'] = np.pi / 180
    _external['e'] = np.exp(1)
    _external['emass'] = constants.physical_constants['electron mass energy equivalent in MeV'][0] / 1e3
    _external['pmass'] = constants.physical_constants['proton mass energy equivalent in MeV'][0] / 1e3
    _external['nmass'] = 0.931494061
    _external['mumass'] = constants.physical_constants['muon mass energy equivalent in MeV'][0] / 1e3
    _external['clight'] = constants.speed_of_light
    _external['qelect'] = constants.elementary_charge
    _external['hbar'] = constants.hbar
    _external['erad'] = constants.physical_constants['classical electron radius'][0]
    _external['prad'] = _external['erad'] * _external['emass'] / _external['pmass']

    # TODO: Deal with multiline statements.
    @classmethod
    def raw_parse(cls, text, lowercase=True):
        if lowercase:
            text = text.lower()
        statements = []
        for line in filter(None, map(str.strip, text.split('\n'))):
            if not line:
                continue
            for t in cls._types:
                try:
                    statements.append(t(line))
                except ValueError:
                    pass
                else:
                    break
            else:
                raise ValueError(f'No type for statement: {line}')
        return statements

    @classmethod
    def parse(cls, text, lowercase=True):
        def _safe_math_eval(string, locals_dict=None):
            is_unsafe = [
                any(map(
                    lambda x: x in string,
                    ('import', '__', '()', '[]', '{}', 'lambda', ',', ';', ':', '"', "'")
                )),
                re.search(r'\(\s*\)', string) is not None,
                re.search(r'\[\s*\]', string) is not None,
                re.search(r'\{\s*\}', string) is not None,
                # Allow a-z for numpy or math functions.
                re.match(r'^[.*/+\-0-9a-zA-Z\s()_]+$', string) is None
            ]
            if any(is_unsafe):
                raise ValueError(f'Evaluation of {repr(string)} is not safe')
            return eval(string, {'__builtins__': {}}, locals_dict or {})

        def _eval_expr(x):
            if x is None:
                return x
            if x.startswith(('"', '\'')) and x.endswith(('"', '\'')):
                return str(x)
            try:
                return int(x)
            except ValueError:
                pass
            try:
                return float(x)
            except ValueError:
                pass
            if re.match(r'(true|false)', x):
                return x == 'true'
            try:
                return _safe_math_eval(x, dict(cls._external, **variables))
            except NameError:
                return str(x)

        if isinstance(text, str):
            text = (text,)
        statements = list(it.chain(*map(partial(cls.raw_parse, lowercase=lowercase), text)))
        variables = {}
        for st in statements:
            if isinstance(st, Variable):
                variables[st.name] = _eval_expr(st.value)
            elif isinstance(st, Command):
                st.attributes = {
                    k: _eval_expr(v) if not isinstance(v, list) else [_eval_expr(x) for x in v]
                    for k, v in st.attributes.items()
                }
        return list(filter(lambda x: not isinstance(x, (Comment, Variable)), statements))
