
from copy import deepcopy

from . import console, markdown, json, html


REPORT_TYPES = {
    'console': console.create,
    'json': json.create,
    'markdown': markdown.create,
    'html': html.create,
}


def make_report(environment, fmt, options=None):
    """
    Creates a report containing the environment information.

    :param environment:
        the information about the environment to make the report about
    :type environment: dict
    :param fmt: the type of report to make
    :type fmt: str
    :type options: dict
    :rtype: str
    """

    if fmt not in REPORT_TYPES:
        raise ValueError('"%s" is not a valid report type' % (fmt,))

    options = deepcopy(options)
    options['tty'] = options.get('tty', False)
    options['summary_only'] = options.get('summary_only', False)
    options['problems_only'] = options.get('problems_only', False)

    return REPORT_TYPES[fmt](environment, options or {})

