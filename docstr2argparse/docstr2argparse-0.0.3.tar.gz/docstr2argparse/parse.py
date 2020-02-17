import builtins
from inspect import signature, _empty
import re
import argparse


def get_positional_or_keyword_params(f):
    """Get positional or keyword parameters from function signature.
    
    Args:
        f (function): A function to investigate.

    Returns:
        dict: Map parameter to its default value.
    """
    return {n:p.default if not p.default == _empty else None 
            for n,p in signature(f).parameters.items() if 
            p.kind.name in ('POSITIONAL_ONLY','POSITIONAL_OR_KEYWORD')}


def _parse_google_argument_name(arg):
    """Parse google arguments."""
    try:
        arg_type = next(re.finditer(r'\(.*?\)', arg)).group(0)
        arg = arg.replace(arg_type, '')
        arg_type = arg_type[1:-1]
    except StopIteration:
        arg_type = None
    arg = arg.strip()
    return arg, arg_type


def parse_google(docstring, trim=True):
    """Parse goolge style of doctring.

    This is defined as by Sphinx.Napoleon package.

    Args:
        docstring (str): Docstring to parse.
        trim (boolean): Should only existing entries be returned?

    Returns:
        dict: All parameters parsed.
    """
    o = {}
    o['Args'] = o['Arguments'] = []
    o['Attributes'] = []
    o['Example'] = []
    o['Examples'] = []
    o['Keyword Args'] = o['Keyword Arguments'] = []
    o['Methods'] = []
    o['Note'] = []
    o['Notes'] = []
    o['Other Parameters'] = []
    o['Return'] = o['Returns'] = []
    o['Raises'] = []
    o['References'] = []
    o['See Also'] = []
    o['Todo'] = []
    o['Warning'] = o['Warnings'] = []
    o['Warns'] = []
    o['Yield'] = o['Yields'] = []
    # pat = r"\n\s*({}):\s*\n".format("|".join(o))
    pat = r"\n\s*(\S+):\s*\n"
    if docstring:
        split = re.split(pat, docstring)
        desc = split[0].split('\n')
        o['short_description'] = desc[0]
        o['long_description'] = " ".join(x for l in desc[1:] for x in l.split())
        for tag, args in zip(split[1::2], split[2::2]):
            assert tag in o, f"Group not specified in Splinx.Napoleon google-doc-style: '{tag}'"
            args = args.rstrip('\n ')
            for arg in args.split('\n'):
                arg_name, arg_desc = arg.split(':', 1)
                arg_desc = " ".join(arg_desc.split())
                arg_name, arg_type = _parse_google_argument_name(arg_name)
                o[tag].append((arg_name, arg_type, arg_desc))
    for k in list(o.keys()):
        if not o[k]:
            del o[k] 
    return o


def test_parse_google():
    docstring = """Little function.

    That does not help.
    Anybody. Anywhere.
    Is useless.

    Args:
        sadness (boolean): no nothing.
        pain (float): stay afloat.

    Returns:
        shit: specific one.
    """
    x = parse_google(docstring)
    y = {'Args': [('sadness', 'boolean', 'no nothing.'), ('pain', 'float', 'stay afloat.')], 'Arguments': [('sadness', 'boolean', 'no nothing.'),('pain', 'float', 'stay afloat.')],'Return': [('shit', None, 'specific one.')],'Returns': [('shit', None, 'specific one.')],'short_description': 'Little function.','long_description': 'That does not help. Anybody. Anywhere. Is useless.'}
    assert x == y, 'Parsing is wrong.'


def foo2argparse(f, args_prefix='', sort = True):
    param2default = get_positional_or_keyword_params(f)
    parsed = parse_google(f.__doc__)
    short_description = parsed['short_description']
    args = parsed['Args']
    args2desc = {n:d for n,_,d in args}
    # checking docs' completeness
    for p in param2default:
        assert p in args2desc, f"Docs of {f} incomplete: {p} is missing."
        assert args2desc[p]!='', f"Docs of {f} incomplete: {p} has empty description."
    if sort:
        args = sorted(args)
    out = []
    for a_name, a_type, a_desc in args:
        o = {'help':a_desc}
        try:
            o['type'] = getattr(builtins, a_type)
        except AttributeError:
            pass
        default = param2default[a_name]
        if default is not None:
            o['default'] = default
            a_name = '--' + args_prefix + a_name # optionals are those with defaults
            o['help'] += f' [default: {default}].'
        else:
            a_name = args_prefix + a_name
        out.append((a_name, o))
    return short_description, out


def document(f, description=''):
    """Document one function.

    Make a parser, ready to be call parse_args().

    Args:
        f (function): Function to document.
        description (str): Description of the parser.

    Returns:
        argparse.ArgumentParser: with instantiated arguments.
    """
    short, params = foo2argparse(f, '')
    description = description if description else short
    arg_parser = argparse.ArgumentParser(description=description)
    for name, val in params:
        arg_parser.add_argument(name, **val)
    return arg_parser


def document_many(foo_dict, description=''):
    """Document many functions.

    Make a parser, ready to be call parse_args().

    Args:
        foo_dict (dict): Maps prefixes to functions.
        description (str): Description of the parser.

    Returns:
        argparse.ArgumentParser: with instantiated arguments.
    """
    arg_parser = argparse.ArgumentParser(description=description)
    for fname, f in foo_dict.items():
        short, params = foo2argparse(f, fname+'_')
        for name, val in params:
            arg_parser.add_argument(name, **val)
    return arg_parser
