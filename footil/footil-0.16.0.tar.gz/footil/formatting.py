"""Manipulate data to have different format or output different data."""
import traceback
import sys
import yattag
import uuid
from typing import Optional
import ast
from string import Formatter
from operator import attrgetter
import re
from email.utils import parseaddr, formataddr

from footil.lib import pattern_methods

PATTERN_METHODS = {
    'join_parent_attrs': {
        'method': pattern_methods._join_parent_attrs,
        # Key represents argument position and val method how
        # to convert argument.
        'conversion': {3: ast.literal_eval}
    }
}


def format_list_to_html(
        line_height=1, collapse_cfg: Optional[dict] = None) -> str:
    """Format list of strings into HTML string.

    Lines are converted into HTML paragraphs. line-height attribute is
    set for all paragraphs. This is default format.

    Optionally can specify collapse_cfg to make part of text
    "togglable" (aka read more/read less). Two ways are supported:
        - bootstrap collapse (default).
        - attr_toggle on div that is "togglable".

    In both cases max_lines key is required.

    First case is used if max_lines is specified (maximum lines to
    show initially), but not attr_toggle. Optionally collapse_id can be
    passed to use it as anchor for bootstrap collapse toggle. Otherwise
    str(uuid.uuid4()) value is used.

    Second case is used if attr_toggle is used. This way only specified
    custom attribute is added on div that wraps paragraphs that should
    be hidden initially. Paragraphs toggle implementation must be done
    externally in this case.

    Args:
        line_height: paragraph height (default: {1})
        collapse_cfg: toggle show/hide part of text config
            (default: {None}) Used keys:
              - max_lines (int): number of paragraphs to show initially.
              - collapse_id (str): anchor for collapse div
                identification. If not set, will use randomly generated
                ID. Bootstrap implementation only.
              - attr_toggle (tuple): attribute used to toggle show/hide
                part of text. Custom implementation only.

    Returns:
        HTML string

    """
    def build_lines(lines):
        for line in lines:
            # Assuming that line is one paragraph, so `\n` is not needed.
            line = line.replace('\n', '')
            with tag('p'):
                text(line)

    def build_bootstrap_collapse(lines_to_hide):
        # Default to random ID if none was specified. It has
        # very low chance to run in collision, so there should
        # be no problem.
        collapse_id = (
            collapse_cfg.get('collapse_id') or str(uuid.uuid4()))
        with tag('div', id=collapse_id, klass='collapse'):
            build_lines(lines_to_hide)
        # Add button to toggle hidden lines.
        with tag(
            'a',
            ('data-toggle', 'collapse'),
            ('data-target', '#%s' % collapse_id),
                klass='btn btn-link'):
            text('Toggle More')

    def format_html(lines):
        with tag('div'):
            doc.attr(style='line-height: %s' % line_height)
            max_lines = collapse_cfg['max_lines']
            if max_lines == -1:  # Everything is showed.
                build_lines(lines)
            else:
                # Split into lines to show and to hide.
                # Lines to hide.
                lines_to_show = lines[0:max_lines]
                lines_to_hide = lines[max_lines:]
                # Build lines that will be visible all the time.
                build_lines(lines_to_show)
                # Build lines that will be hidden initially.
                if collapse_cfg.get('attr_toggle'):
                    # Using custom specified attribute that should be
                    # used to handle toggling of lines_to_hide (
                    # implementation must be done externally from this
                    # method).
                    with tag('div', collapse_cfg['attr_toggle']):
                        build_lines(lines_to_hide)
                else:
                    # Default to bootstrap implementation.
                    build_bootstrap_collapse(lines_to_hide)
        return doc.getvalue()

    if not collapse_cfg:
        collapse_cfg = {'max_lines': -1}
    doc, tag, text = yattag.Doc().tagtext()
    return format_html


def _format_exception() -> list:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    return traceback.format_exception(exc_type, exc_value, exc_traceback)


def _get_formatted_exception(
        exc_lines: list, formatter=None) -> str:
    if not formatter:
        return ''.join(exc_lines)
    return formatter(exc_lines)


def get_formatted_exception(formatter=None) -> str:
    """Convert exception lines into formatter string.

    How string is formatted, depends on formatter function passed.
    Formatter acts as constructor, so it needs to be executed where its
    closure function can take specified arguments (if there are any) and
    do actual formatting.

    Args:
        formatter: logic how to format (default: {None}). If not
        specified will default to ''.join(exc_lines).

    Returns:
        formatted exception lines string

    """
    exc_lines = _format_exception()
    return _get_formatted_exception(exc_lines, formatter=formatter)


def _parse_pattern_methods(pattern: str, obj: object) -> str:
    def convert_args(args, conversion_map):
        new_args = []
        for index, arg in enumerate(args):
            new_args.append(
                conversion_map[index](arg) if index in conversion_map else
                arg)
        return new_args

    # Catch all methods and their content.
    for key, dct in PATTERN_METHODS.items():
        method = dct['method']
        for match in re.findall(r'\$%s\(.*?\)' % key, pattern):
            args = re.findall(r'\"(.*?)\"', match)
            if dct.get('conversion'):
                args = convert_args(args, dct['conversion'])
            parsed = method(obj, *args)
            pattern = pattern.replace(match, parsed)
    return pattern


def generate_name(pattern: str, obj: object, strip_falsy: bool = True) -> str:
    """Generate name by pattern, using attributes specified by it.

    Object is used to get required attributes values. If object does
    not have truthy value for attribute, it can be stripped using
    keyword argument strip_falsy.

    Args:
        pattern (str): pattern to generate name by. e.g.
            'test {a.b} / {c}'
        obj (object): object to retrieve attributes from.
        strip_falsy (bool): whether to strip away falsy attribute
            values or not. If stripped away, then leading string is
            also stripped away for next attribute to not look like
            '/ attr_value'. It instead just looks like 'attr_value'
            (default: {True}).

    Returns:
        Generated name using pattern and obj attributes.
        str

    """
    def get_prev_attr_val():
        attr_vals_len = len(attrs_vals)
        if attr_vals_len > 1:
            return attrs_vals[attr_vals_len-2]

    def get_leading_str(leading_str):
        prev_attr_val = get_prev_attr_val()
        # None means, current item is first and there is no previous
        # one.
        if prev_attr_val is None:
            return leading_str
        # We have falsy value (on prev attribute) and we need to
        # strip it away, so we use empty string.
        if not prev_attr_val and strip_falsy:
            return ''
        return leading_str

    # First parse pattern methods if there are any defined on a
    # pattern.
    pattern = _parse_pattern_methods(pattern, obj)
    name = ''
    # To track previous attribute value.
    attrs_vals = []
    for item in Formatter().parse(pattern):
        # if item[1] is Falsy, it means there are no variables in
        # string and we only got leading string from item[0]. With
        # that information we can terminate function at this point,
        # because there is nothing else to do.
        if not item[1]:
            # Here we return pattern itself, instead of name,
            # because name in this case is empty, but pattern
            # already has all leading strings and parsed pattern
            # methods if those were used.
            return pattern
        # Get attribute value from attr key. We use attrgetter from
        # operator module to be able to access n-depth attributes.
        # In Other words access attribute of objects that are
        # related with another object.
        f = attrgetter(item[1])  # item[1] is attribute key.
        attr_val = f(obj)
        attrs_vals.append(attr_val)
        # item[0] holds original leading string.
        leading_str = get_leading_str(item[0])
        if attr_val or not strip_falsy:
            name += leading_str + str(attr_val)
    return name


def generate_names(cfg: dict) -> list:
    """Wrap generate_name and reuse for multiple objects.

    cfg keys:
        pattern (str): pattern to generate name by. e.g.
            'test {a.b} / {c}'
        objects (iterable): iterable of objects to use.
        strip_falsy (bool): whether to strip away falsy attribute
            values or not. If stripped away, then leading string is
            also stripped away for next attribute to not look like
            '/ attr_value'. It instead just looks like 'attr_value'
            (default: {True})
        key (str): attribute name to put its value into tuple
            (default: {'id'})

    Returns:
        list of tuple pairs, where first item is identifier, second
        generated name string.

    """
    try:
        pattern = cfg['pattern']
        objects = cfg['objects']
    except KeyError as e:
        raise ValueError("cfg is missing required key '%s'" % e)
    # strip falsy values is True on default.
    strip_falsy = cfg.get('strip_falsy', True)
    # Default key is 'id' attribute.
    key = cfg.get('key', 'id')
    return [
        (
            getattr(obj, key),
            generate_name(pattern, obj, strip_falsy=strip_falsy)
        )
        for obj in objects
    ]


# Email formatting utilities.

def replace_email_name(name: str, old_email: str) -> str:
    """Replace email name with new one."""
    _, email_part = parseaddr(old_email)
    return formataddr((name, email_part))


def replace_email(email_part: str, old_email: str) -> str:
    """Replace email part with new one.

    Email name is kept the same if one was present.

    Args:
        email_part: new email to replace with.
        old_email: email to replace to.
    """
    name, _ = parseaddr(old_email)
    return formataddr((name, email_part))


# String formatting

def replace_ic(
    term: str,
    to_replace: str,
        replace_with: Optional[str] = '') -> str:
    """Replace fragment in term with other fragment (ignore case).

    This is case-insensitive replacement, e.g. words 'Hello' and
    'heLLo' will be replaced if key to replace is 'HELLO', 'HeLlo'
    and etc.

    Args:
        term (str): term where fragment to replace will be searched
            for and replaced with new fragment.
        to_replace (str): fragment to be replaced (old fragment).
        replace_with (str): fragment to be replaced with
            (new fragment) (default: {''}).

    Returns:
        new term where old fragment (to_replace) in term is replaced
        with new fragment (to_replace).
        str

    """
    insensitive_fragment = re.compile(to_replace, re.IGNORECASE)
    return insensitive_fragment.sub(replace_with, term)


def strip_space(s: str):
    r"""Replace all spaces from string.

    Removes space like ' ', '\t', '\n' or '\r'. It will remove between
    chars too.

    Args:
        s: string to remove white space for.

    Returns:
        New string with all spaces removed.

    """
    return ''.join(s.split())
