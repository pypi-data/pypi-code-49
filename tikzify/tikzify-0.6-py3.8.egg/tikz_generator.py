import re
import sys
from contextlib import contextmanager
from textwrap import dedent
from typing import Mapping, TextIO

import numpy as np

__all__ = ['even_offsets',
           'formatter',
           'pf',
           'pf_option',
           'pf_option_value',
           'tex_pic',
           'tex_file']


def even_offsets(x, out_of, start_stop):
    if out_of == 1:
        return sum(start_stop) / 2
    return np.linspace(start_stop[0], start_stop[1], out_of)[x]


def formatter(string_to_be_printed, **kwargs):
    """
    Perform recursive string formatting on a string.
    Any keywords enclosed in curly quotation marks are expanded using the
    keyword arguments passed into the function with a few details:
    * The formatter is applied recursively to the expanded string.  E.g.,
      formatter("“a”", a="expanded “b”", b="expanded c")
      returns
      'expanded expanded c'
    * If a keyword is a comma-separated list like “a, b, c”, then each of
      the keywords "a", "b", and "c" are expanded and the results of joined
      with intervening commas.  If any expansion results in the None object,
      the formatter acts as if that term were not there.  E.g.,
      formatter("“a, b, c”", a="expanded a", b=None, c="expanded c")
      returns
      'expanded a, expanded c'
    * Any keyword can contain a ':' in which case the Python string formatting
      applies, e.g., “a:.6f” would look for 'a' in the keyword arguments and
      expanded the floating point number to six decimal places.
      formatter("“a:.3f, b:3d”", a=1.23456, b=7)
      returns
      '1.235, 007'
    Finally, the returned string is unindented and stripped of whitespace
    at either end.
    """
    def repl(m):
        keyword = m.group(1)
        retval = []
        for x in keyword.split(','):
            add_space = x and x[-1] == ' '
            x = x.strip()
            if x == '':
                retval.append('')
                continue
            if kwargs[x.split(':')[0]] is not None:
                y = str(('{' + x + '}').format(**kwargs))
                if add_space:
                    y += ' '
                retval.append(y)
        return ", ".join(retval)

    try:
        retval = re.sub(r"“(.+?)”", repl,
                        dedent(string_to_be_printed)).strip('\n')
    except KeyError as e:
        raise Exception(
            "No key \"{}\" found in {} for formatted string {}.".format(
                e.args[0],
                kwargs,
                string_to_be_printed))
    if '“' in retval:
        return formatter(retval, **kwargs)
    return retval


def pf(string_to_be_printed, file=sys.stdout, end='\n', **kwargs):
    """
    Format the string using formatter and print it to file with the given
    ending character.
    """
    print(formatter(string_to_be_printed, **kwargs), end=end, file=file)


def pf_option(dict_, name, key_name=None):
    if key_name is None:
        key_name = name
    if name in dict_ and dict_[name] is not None:
        value = dict_[name]
        if isinstance(value, (list, tuple)):
            value = ":".join(str(x) for x in value)
            retval = key_name + '=' + value
        elif value is True:
            retval = key_name
        else:
            value = str(value)
            retval = key_name + '=' + value
        return retval
    return None


def pf_option_value(name, value):
    if value is None:
        return None
    return "{}={}".format(name, value)


@contextmanager
def tex_pic(f: TextIO, filename: str, pic_type: str, options: Mapping = None):
    """
    A context manager that creates a tikzpicture environment in the given
    file.  filename is the name of the generated pdf for the tikz code.
    """
    if options is None:
        options = {}
    pf(r"""
       % “filename” (fold)
       “ext”
       \begin{tikzpicture}“pt”
       """,
       pt=r"[/“pic_type”]" if pic_type else "",
       pic_type=pic_type,
       ext=r"\tikzsetnextfilename{“filename”}" if filename else "",
       filename=filename,
       file=f,
       **options)
    yield
    pf(r"""
       \end{tikzpicture} % (end)
       """,
       end='\n\n',
       file=f)


@contextmanager
def tex_file(filename, inputs=None, preamble=None):
    if inputs is None:
        inputs = []
    input_string = "\n".join(rf"\input{{{i}.tex}}"
                             for i in inputs)
    if preamble is not None:
        input_string += "\n" + preamble
    with open(filename, 'wt') as f:
        pf(r"""
           \documentclass{memoir}
           \setlrmarginsandblock{25mm}{25mm}{*}
           \setulmarginsandblock{25mm}{25mm}{*}
           \setheadfoot{13pt}{26pt}
           \setheaderspaces{*}{13pt}{*}
           \checkandfixthelayout
           \makeatletter
           “input_string”
           \begin{document}
           """,
           file=f,
           input_string=input_string)
        yield f
        pf(r"""
           \end{document}
           """,
           file=f)
