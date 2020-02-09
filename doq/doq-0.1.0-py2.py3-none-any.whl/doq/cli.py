import argparse
import contextlib
import os
import re
import sys

from doq import __version__
from doq.outputter import (
    JSONOutputter,
    StringOutptter,
)
from doq.parser import parse
from doq.template import Template


def _sort(key):
    return key['start_lineno']


def find_files(basedir):
    r = re.compile(r'.*.py$')
    files = []
    for root, directories, children in os.walk(os.path.abspath(basedir)):
        directories[:] = [d for d in directories if not d[0] == '.']
        if len(children):
            ret = list(filter(r.match, children))
            if len(ret):
                files += [os.path.join(root, r) for r in ret]

    return files


def get_lines(file, start, end):
    lines = []
    with contextlib.closing(file) as f:
        lines = [l.strip('\n') for l in f]
        start = start - 1
        end = len(lines) if end == 0 else end

        lines = lines[start:end]

    return lines


def get_template_path(template_path, formatter):
    if not template_path:
        path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'templates',
        )

        return os.path.join(os.path.abspath(path), formatter)

    return os.path.abspath(template_path)


def run(lines, path):
    template = Template(paths=[path])
    signatures = parse('\n'.join(lines))

    docstrings = []
    for signature in signatures:
        if 'defs' in signature:
            # Class docstring
            if signature['is_doc_exists'] is False:
                docstring = template.load(params=signature, filename='class.txt')
                docstrings.append({
                    'docstring': docstring,
                    'start_lineno': signature['start_lineno'],
                    'start_col': signature['start_col'],
                    'end_lineno': signature['end_lineno'],
                    'end_col': signature['end_col'],
                })

            # Method docstring
            for d in signature['defs']:
                if d['is_doc_exists'] is False:
                    filename = 'def.txt' if len(d['params']) else 'noarg.txt'
                    docstring = template.load(params=d, filename=filename)
                    docstrings.append({
                        'docstring': docstring,
                        'start_lineno': d['start_lineno'],
                        'start_col': d['start_col'],
                        'end_lineno': d['end_lineno'],
                        'end_col': d['start_col'],
                    })
        else:
            if signature['is_doc_exists'] is False:
                filename = 'def.txt' if len(signature['params']) else 'noarg.txt'
                # Function docstring
                docstring = template.load(params=signature, filename=filename)
                docstrings.append({
                    'docstring': docstring,
                    'start_lineno': signature['start_lineno'],
                    'start_col': signature['start_col'],
                    'end_lineno': signature['end_lineno'],
                    'end_col': signature['start_col'],
                })

    docstrings.sort(key=_sort)

    return docstrings


def get_targets(args):
    targets = []
    if args.recursive:
        files = find_files(args.directory)
        for file in files:
            with open(file) as f:
                lines = get_lines(f, args.start, args.end)
                if len(lines) == 0:
                    continue
                targets.append({
                    'path': file,
                    'lines': lines,
                })
    else:
        lines = get_lines(args.file, args.start, args.end)
        if len(lines) == 0:
            return False

        args.file.name == '<stdin>'
        path = args.file.name \
            if args.file.name == '<stdin>' \
            else os.path.abspath(args.file.name)

        targets.append({
            'path': path,
            'lines': lines,
        })

    return targets


def main(args):
    targets = get_targets(args)
    path = get_template_path(
        template_path=args.template_path,
        formatter=args.formatter,
    )

    if not os.path.exists(path):
        return False

    for target in targets:
        docstrings = run(target['lines'], path)
        if len(docstrings) == 0:
            continue

        if args.style == 'json':
            outputter = JSONOutputter()
        else:
            outputter = StringOutptter()

        output = outputter.format(
            lines=target['lines'],
            docstrings=docstrings,
            indent=args.indent,
        )

        if args.write and target['path'] != '<stdin>':
            with open(target['path'], 'w') as f:
                f.write(output)

        else:
            sys.stdout.write(output)

    return True


def parse_options():
    parser = argparse.ArgumentParser(
        prog='doq',
        description='Docstring generator.',
        add_help=True,
    )
    parser.add_argument(
        '-f',
        '--file',
        type=argparse.FileType('r'),
        default='-',
        help='File or STDIN',
    )
    parser.add_argument(
        '--start',
        type=int,
        default=1,
        help='Start lineno',
    )
    parser.add_argument(
        '--end',
        type=int,
        default=0,
        help='End lineno',
    )
    parser.add_argument(
        '-t',
        '--template_path',
        type=str,
        default=None,
        help='Path to template directory',
    )
    parser.add_argument(
        '-s',
        '--style',
        type=str,
        default='string',
        help='Output style string or json',
    )
    parser.add_argument(
        '--formatter',
        type=str,
        default='sphinx',
        help='Docstring formatter. sphinx,google or numpy',
    )
    parser.add_argument(
        '--indent',
        type=int,
        default=4,
        help='Indent number',
    )
    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        help='Run recursively over directories',
    )
    parser.add_argument(
        '-d',
        '--directory',
        default='',
        help='Dire',
    )
    parser.add_argument(
        '-w',
        '--write',
        action='store_true',
        help='Edit files in-place',
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {0}'.format(__version__),
        help='Output the version number',
    )

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_options()
    try:
        ret = main(args)
        if ret:
            sys.exit(0)

        sys.exit(1)
    except KeyboardInterrupt:
        pass
