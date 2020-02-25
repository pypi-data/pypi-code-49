from collections import OrderedDict
from functools import partial
import re


def __getattr__(name):
    return partial(Command, name)


class E(str):
    """Re-evaluated expression.
    
    Wraps the expression as a string. Use via `E('expression')`.
    """


class Command:
    """Base class representing a MADX element (in fact, this can be any MADX command)."""

    def __init__(self, keyword, **attributes):
        super().__init__()
        self.keyword = keyword
        self.attributes = OrderedDict(**attributes)

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def __str__(self):
        if not self.attributes:
            return f'{self.keyword}'
        keys, values = zip(*self.attributes.items())
        ops = [':=' if isinstance(x, E) else '=' for x in values]
        values = map(
            lambda x: (
                '{' + ', '.join(str(xx) for xx in x) + '}' if isinstance(x, (list, tuple))
                else (str(x) if x is not None else 'true')
            ),
            values
        )
        return f'{self.keyword}, {", ".join(map(" ".join, zip(keys, ops, values)))}'


class DerivedCommand(Command):
    """Class for elements that depend on previous definitions
    
    Derived elements retain the attribute specifications from their templates (parents).
    """

    def __init__(self, base, name, **attributes):
        super().__init__(name, **attributes)
        self.base = base

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.base[key]


class Placeholder(Command):
    """Class that serves as a placeholder for interpolation / formatting later on."""

    def __init__(self, name, **attributes):
        super().__init__('{' + name + '}', **attributes)


class Script:
    """Main class for building MADX scripts.
    
    * Labeled statements can be placed via `script['label'] = ...`,
    * Unlabeled statements can be placed via `script += ...` or `script._ = ...`,
    * Any MADX command can be accessed via `script.COMMAND`,
    * Command arguments can be specified via `script.COMMAND(key=value)`,
    * Unlabeled commands can be placed directly in the script by using a trailing underscore: `script.COMMAND_(key=value)`,
    * Derived commands can be created by first labeling the base `script['BASE'] = script.EXAMPLE(foo='bar') and then
      accessing the definition via `script.BASE_(something='else'),
    * Re-evaluated expressions can be placed via `E('...')`,
    * Comments can be placed via `scipt += '// Comment'`,
    * The script's content can be dumped via `str(script)`.
    
    Example
    -------
    
    ```python
    script = Script()
    script['L'] = 5
    script['DP'] = script.SBEND(l='L', angle='2*PI / 10')
    script.DP_()
    script.TWISS_(file='optics')
    script.EALIGN_(dx=E('0.001 * (2*RANF() - 1)'))
    script += '// Example comment'
    with open('example.madx', 'w') as f:
        f.write(str(script))
    ```
    """

    def __init__(self):
        super().__init__()
        self.elements = []
        self.definitions = OrderedDict()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getattr__(self, name):
        inplace = name.endswith('_')
        name = name.rstrip('_')
        try:
            element =  self.definitions[name]
        except KeyError:
            element =  partial(Command, name)
        else:
            if isinstance(element, Command):
                element = partial(DerivedCommand, element, name)
            elif isinstance(element, str) and element.startswith('{') and element.endswith('}'):
                element = partial(Command, name)
        if inplace:
            def wrapper(**kwargs):
                return self.__iadd__(element(**kwargs))
            wrapper.__name__ = name
            return wrapper
        return element

    def __setattr__(self, key, value):
        if key == '_':
            self.__iadd__(value)
        else:
            super().__setattr__(key, value)

    def __getitem__(self, key):
        return self.definitions[key]

    def __setitem__(self, key, value):
        if self.definitions.get(key) is value:
            return None
        if key is not None:
            self.definitions[key] = value
        self.elements.append((key, value))

    def __iadd__(self, other):
        self.elements.append((None, other))
        return self

    def __str__(self):
        is_template = any(isinstance(x[1], Placeholder) for x in self.elements)
        return '\n'.join(map(partial(self._format_element, template_compatible=is_template), self.elements))

    @staticmethod
    def _format_element(element, template_compatible=False):
        if element[0] is None:
            val = str(element[1])
        elif isinstance(element[1], Command):
            val = f'{element[0]}: {str(element[1])}'
        else:
            val = '{} = {};'.format(*element)
        if not (val.startswith(('//', '/*')) or val.endswith(';')):
            val += ';'
        if template_compatible and not isinstance(element[1], Placeholder) and '{' in val:
            val = val.replace('{', '{{').replace('}', '}}')
        return val


class Block(Command, Script):
    """Represents a block element.
    
    * Blocks can be used as context managers,
    * Blocks work like scripts (i.e. all the `Script` rules apply),
    * Blocks can be added to scripts and will be auto-expanded when the script is dumped.
    """

    def __init__(self, **kwargs):
        super().__init__(self.__class__.__name__.lower(), **kwargs)
        # Any attributes added in `__init__` ended up in `self.elements` due to `__setattr__`.
        self.elements[:] = []

    def __setitem__(self, key, value):
        if isinstance(value, Command):
            Script.__setitem__(self, key, value)
        else:
            Command.__setitem__(self, key, value)

    def __str__(self):
        header = f'{Command.__str__(self)};'
        body = '\n'.join(map('    {}'.format, Script.__str__(self).split('\n')))
        footer = f'end{self.__class__.__name__.lower()};'
        return '\n'.join([header, body, footer])


class Sequence(Block):
    """Main class for building sequences.

    * Sequences can be used as context managers,
    * Sequences work like scripts (i.e. all the `Script` rules apply),
    * Sequences can be added to scripts and will be auto-expanded when the script is dumped.

    Example
    -------

    ```python
    script = Script()

    with Sequence(refer='entry', l='length') as seq:
        seq += script.SBEND(l=..., angle=...)
        ...

    script['LATTICE'] = seq
    ```
    """
    pass


class Track(Block):
    """Main class for creating tracking runs.

    * Tracking blocks can be used as context managers,
    * Tracking blocks work like scripts (i.e. all the `Script` rules apply),
    * Tracking blocks can be added to scripts and will be auto-expanded when the script is dumped.

    Example
    -------

    ```python
    script = Script()

    with Track() as tracking:
        tracking += tracking.start(x=..., px=...)
        tracking += tracking.run(turns=...)
        ...
        
    script += tracking
    ```
    """
    pass


class AdvancedControl:
    class Cursor:
        @property
        def item(self):
            return self.script.elements[self.line_number][1]

        @property
        def label(self):
            return self.script.elements[self.line_number][0]

        def __init__(self, script, line_number=None, label=None):
            super().__setattr__('script', script)
            if line_number is None:
                try:
                    line_number = [x[0] for x in script.elements].index(label)
                except ValueError:
                    pattern = re.compile(r'(?P<keyword>[a-z][a-z0-9]*)(?:\[(?P<nr>[0-9]+)\])?', re.I)
                    match = re.match(pattern, label)
                    if match is None:
                        raise ValueError(f'Cannot find {repr(label)}')
                    keyword = match.groupdict()['keyword']
                    nr = int(match.groupdict()['nr'] or 0)
                    sub_selection = [i for i, (l, e) in enumerate(script.elements)
                                     if isinstance(e, Command) and e.keyword == keyword]
                    try:
                        line_number = sub_selection[int(nr)]
                    except IndexError:
                        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(nr, 'th')
                        raise IndexError(f'Cannot select {nr}{suffix} {keyword} out of {len(sub_selection)}')
            super().__setattr__('line_number', line_number)

        def __invert__(self):
            if self.label is not None:
                del self.script.definitions[self.label]
            self.script.elements.pop(self.line_number)

        def __lshift__(self, offset):
            new_line_number = self.line_number - offset
            if new_line_number < 0 or new_line_number >= len(self.script.elements):
                raise ValueError(f'Cursor out of range: {new_line_number} \u2209 [0, {len(self.script.elements) - 1}]')
            super().__setattr__('line_number', new_line_number)
            return self

        def __rshift__(self, offset):
            return self.__lshift__(-offset)

        def __insert(self, index, element):
            if isinstance(element, (list, tuple)):
                label, element = element
                self.script.definitions[label] = element
            else:
                label = None
            self.script.elements.insert(index, (label, element))

        def __lt__(self, element):
            self.__insert(self.line_number, element)

        def __gt__(self, element):
            self.__insert(self.line_number + 1, element)

        def __eq__(self, element):
            self.__invert__()
            self.__lt__(element)

        def __getattr__(self, item):
            return self.item.__getattr__(item)

        def __setattr__(self, key, value):
            return self.item.__setattr__(key, value)

        def __getitem__(self, item):
            return self.item.__getitem__(item)

        def __setitem__(self, key, value):
            return self.item.__setitem__(key, value)

        def __iadd__(self, other):
            return self.item.__iadd__(other)

        def __str__(self):
            return self.item.__str__()

        @classmethod
        def activate(cls):
            cls.original_getitem = Script.__getitem__
            cls.original_setitem = Script.__setitem__

            def __getitem__(self, key):
                if isinstance(key, int):
                    return cls(self, line_number=key)
                elif isinstance(key, str):
                    return cls(self, label=key)
                else:
                    raise TypeError('Index must be either int or str')

            def __setitem__(self, key, value):
                if isinstance(value, cls):
                    value = value.item()
                return cls.original_setitem(self, key, value)

            Script.__getitem__ = __getitem__
            Script.__setitem__ = __setitem__

        @classmethod
        def deactivate(cls):
            Script.__getitem__ = cls.original_getitem
            Script.__setitem__ = cls.original_setitem
