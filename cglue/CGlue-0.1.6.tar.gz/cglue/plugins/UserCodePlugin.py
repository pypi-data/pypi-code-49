import re

from cglue.function import FunctionImplementation
from cglue.cglue import Plugin, CGlue


parse_section = re.compile(
    '(?P<indent>[ ]*)/\\* Begin User Code Section: (?P<secname>.*?) \\*/[\n]?'
    '(?P<usercode>.*?)[\n]?(?P=indent)/\\* End User Code Section: (?P=secname) \\*/',
    flags=re.DOTALL)

fill_section = re.compile(
    '(?P<indent>[ ]*)/\\* Begin User Code Section: (?P<secname>.*?) \\*/'
    '(?P<usercode>.*?)/\\* End User Code Section: (?P=secname) \\*/',
    flags=re.DOTALL)


def remove_indentation(text, spaces):
    """
    Remove at most n leading spaces from each line.

    >>> remove_indentation('foo\\n bar\\n  baz\\n   barbaz', 2)
    'foo\\nbar\\nbaz\\n barbaz'
    """

    if spaces == 0:
        return text
    else:
        return re.sub(f'^[ ]{{1,{spaces}}}(.*?)$', '\\1', text, flags=re.MULTILINE)


def get_sections(text):
    """
    >>> get_sections('/* Begin User Code Section: foobar */barbaz/* End User Code Section: foobar */')
    {'foobar': 'barbaz'}
    >>> get_sections('/* Begin User Code Section: foobar */\\nbar\\nbaz\\n/* End User Code Section: foobar */')
    {'foobar': 'bar\\nbaz'}
    """
    # parse contents
    matches = parse_section.findall(text)

    return {secname: remove_indentation(usercode, len(indent)) for indent, secname, usercode in matches}


def get_sections_from_file(file_path):
    """Parse the given file for user sections"""
    try:
        with open(file_path, 'r') as f:
            contents = f.read()

        return get_sections(contents)
    except FileNotFoundError:
        return {}


def create_section(name, contents):
    return f'/* Begin User Code Section: {name} */\n{contents}/* End User Code Section: {name} */'


def add_sections_to_function(function: FunctionImplementation, name):
    secname = name + ' Start'
    function.prepend_body(create_section(secname, ''))

    secname = name + ' End'
    function.add_body(create_section(secname, ''))


def fill_sections(source, sections):
    """
    >>> fill_sections(\
'    /* Begin User Code Section: foobar *//* End User Code Section: foobar */', {'foobar': 'barbaz'})
    '    /* Begin User Code Section: foobar */\\n    barbaz\\n    /* End User Code Section: foobar */'
    """
    def repl(matches):
        indent = matches[1]
        secname = matches[2]

        lines = sections.get(secname, '').split("\n")
        indented_lines = (indent + line if line != '' else line for line in lines)
        code_section = "\n".join(indented_lines) + "\n" + indent  # last indent is for the closing comment

        return indent + create_section(secname, code_section)

    return fill_section.sub(repl, source)


def add_sections_to_component(owner: CGlue, component_name, context: dict):
    context['declarations'].insert(0, create_section('Declarations', ''))

    for func_name, functions in context['functions'].items():
        for func_type, function in functions.items():
            name = f'{func_name[func_name.rfind("/") + 1:]}:{func_type}'  # don't need to have the component name
            add_sections_to_function(function, name)


def add_sections_to_runtime(owner: CGlue, context: dict):
    context['declarations'].insert(0, create_section('Declarations', ''))

    for func_name, functions in context['functions'].items():
        for func_type, function in functions.items():
            name = f'{func_name}:{func_type}'
            add_sections_to_function(function, name)


def replace_sections_in_files(context: dict):
    for file, source in context['files'].items():
        sections = get_sections_from_file(file)

        context['files'][file] = fill_sections(source, sections)


def user_code_plugin():
    return Plugin("UserCodePlugin", handlers={
        'before_generating_component': add_sections_to_component,
        'generating_component': lambda owner, component_name, context: replace_sections_in_files(context),
        'before_generating_runtime': add_sections_to_runtime,
        'after_generating_runtime': lambda owner, context: replace_sections_in_files(context)
    })
