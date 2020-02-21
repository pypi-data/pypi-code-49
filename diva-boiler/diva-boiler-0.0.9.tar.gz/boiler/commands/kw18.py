import json
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple

import click

from boiler import cli
from boiler.commands.utils import summarize_activities
from boiler.serialization.kw18 import KW18FileSet
from boiler.serialization.web import serialize_validation_errors
from boiler.validate import validate_activities


def _find_kw18_files(paths: List[str], recursive: bool) -> Iterator[Path]:
    if recursive:
        for p in paths:
            for g in Path(p).glob('**/*.kw18'):
                yield g.parent
    else:
        for p in paths:
            yield Path(p)


def _validate_kw18(path: Path) -> Tuple[List[str], List[str], Dict[str, Any]]:
    kw18_file_set = KW18FileSet.create_from_path(path)
    try:
        activity_list = kw18_file_set.read()
    except Exception as err:
        return [], serialize_validation_errors([err]), {}

    summary = summarize_activities(activity_list)
    warnings, errors = validate_activities(activity_list)
    error = serialize_validation_errors(errors)
    warning = serialize_validation_errors(warnings)
    return warning, error, summary


def _serialize_output(
    path: Path, error: List[str], warning: List[str], summary: Dict[str, Any]
) -> str:
    try:
        prefix = click.style(next(path.glob('*.kw18')).stem, bold=True)
    except StopIteration:
        prefix = ''

    content: List[str] = []
    if error:
        mark = click.style(f'✗  {prefix}', fg='red')
    elif warning:
        mark = click.style(f'⚠  {prefix}', fg='yellow')
    else:
        mark = click.style(f'✔️  {prefix}', fg='green')

    content.extend(
        [
            # str(path),  TODO: maybe add a verbose option for full path
            mark
        ]
    )
    indent = ' ' * 4

    for e in error:
        content.append(click.style(f'{indent * 2}{e}', fg='red'))

    for w in warning:
        content.append(click.style(f'{indent * 2} {w}', fg='yellow'))

    # TODO: add summary information

    return '\n'.join(content)


@click.group(name='kw18', short_help='Ingest and validate kw18')
@click.pass_obj
def kw18(ctx):
    pass


@kw18.command(name='validate', help='validate one or more kw18 annotations')
@click.argument('path', type=click.Path(exists=True, file_okay=False), nargs=-1)
@click.option('--recursive', '-r', is_flag=True)
@click.pass_context
def validate(ctx, path: List[str], recursive):
    has_invalid = False
    for base_path in _find_kw18_files(path, recursive):
        try:
            warning, error, summary = _validate_kw18(base_path)
        except FileNotFoundError:
            warning = []
            summary = {}
            error = ['Could not determine kw18 file']

        click.echo(_serialize_output(path=base_path, error=error, warning=warning, summary=summary))
        click.echo('')

    ctx.exit(0 if not has_invalid else 1)


@kw18.command(name='ingest', short_help='push files from the annotation repository')
@click.argument('path', type=click.Path(exists=True, file_okay=False), nargs=-1)
@click.option('--recursive', '-r', is_flag=True)
@click.pass_obj
def ingest(ctx, path, recursive):
    """Ingest one or more annotations from the annotation repository.

    This command takes a set of KW18 annotation files from the provided paths
    and sends them to Stumpf.  Stumpf will first detect whether the files have
    changed or not.  If they have not, no further action will be taken.  If
    they have, then Stumpf will:

    \b
    1. Generate a transition to the "annotation" status
    2. Run server side validation.
    3. If validation fails, return failure information.
    4. If validation succeeds, transition to the "audit" state
       and ingest activities from the KW18 files.
    """
    session = ctx['session']
    for base_path in _find_kw18_files(path, recursive):
        kw18_file_upload = KW18FileSet.create_from_path(base_path).upload(session)
        data = {
            'annotation_repo_path': str(base_path),
            'kw18_file_upload_id': kw18_file_upload['id'],
        }

        r = ctx['session'].post('video-pipeline/process-annotation', json=data)
        # TODO: replace with human friendly output
        print(json.dumps(r.json(), indent=2))


cli.add_command(kw18)  # type: ignore
