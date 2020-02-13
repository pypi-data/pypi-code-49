import datetime
from distutils.version import StrictVersion
from pathlib import Path
import platform
import sys
import traceback


import click
import requests
from requests.exceptions import RequestException
from requests_toolbelt.sessions import BaseUrlSession

__version__ = '0.0.8'


class BoilerSession(BaseUrlSession):

    page_size = 50

    def __init__(self, base_url, token):
        base_url = f'{base_url.rstrip("/")}/'  # tolerate input with or without trailing slash
        super(BoilerSession, self).__init__(base_url=base_url)
        self.token = token
        self.headers.update(
            {
                'User-agent': f'boiler/{__version__}',
                'Accept': 'application/json',
                'X-Stumpf-Token': self.token,
            }
        )


class KW18BaseName(click.ParamType):
    name = 'kw18_basename'

    def convert(self, value, param, ctx):
        expected_files = [
            Path(value + x) for x in ['.kw18.types', '.kw18', '.txt', '.kw18.regions']
        ]
        missing_files = [x for x in expected_files if not x.exists()]

        if missing_files:
            self.fail(f'Missing one or more expected kw18 files for {value}', param, ctx)

        return {
            'activities': {'file': open(expected_files[2], 'r'), 'model': None},
            'types': {'file': open(expected_files[0], 'r'), 'model': None},
            'regions': {'file': open(expected_files[3], 'r'), 'model': None},
            'geom': {'file': open(expected_files[1], 'r'), 'model': None},
        }


def newer_version_available():
    r = requests.get('https://pypi.org/pypi/diva-boiler/json', timeout=(5, 5))
    r.raise_for_status()
    releases = list(r.json()['releases'])
    return any(StrictVersion(r) > StrictVersion(__version__) for r in releases)


def main():
    try:
        cli()
    except Exception:
        click.echo(
            click.style(
                'The following unexpected error occurred while attempting your operation:\n',
                fg='red',
            ),
            err=True,
        )

        click.echo(traceback.format_exc(), err=True)

        click.echo(f'boiler:  v{__version__}', err=True)
        click.echo(f'python:  v{platform.python_version()}', err=True)
        click.echo(f'time:    {datetime.datetime.now(datetime.timezone.utc).isoformat()}', err=True)
        click.echo(f'os:      {platform.platform()}', err=True)
        click.echo(f'command: {" ".join(sys.argv[1:])}\n', err=True)

        click.echo(
            click.style(
                'This is a bug in boiler and should be reported here with the above output:',
                fg='yellow',
            ),
            err=True,
        )
        click.echo(
            'https://gitlab.com/diva-mturk/stumpf-diva/issues/new', err=True,
        )


@click.group()
@click.option(
    '--api-url',
    default='https://stumpf-the-younger.avidannotations.com/api/diva/',
    envvar='STUMPF_API_URL',
)
@click.option('--x-stumpf-token', envvar='X_STUMPF_TOKEN')
@click.option('--offline', is_flag=True)
@click.version_option()
@click.pass_context
def cli(ctx, api_url, x_stumpf_token, offline):
    if not offline:
        try:
            if newer_version_available():
                click.echo(
                    click.style(
                        """There is a newer version of boiler available.
You must upgrade to the latest version before continuing.
If you are using pip, then you can upgrade by running the following command:
""",
                        fg='yellow',
                    ),
                    err=True,
                )
                click.echo(click.style('pipx upgrade diva-boiler', fg='green'), err=True)
                sys.exit(1)
        except RequestException:
            click.echo(
                click.style('Failed to check for newer version of boiler:', fg='red'), err=True
            )
            raise

    session = BoilerSession(api_url, x_stumpf_token)
    ctx.obj = {'session': session}


# TODO: re-enable kpf once deserialization is fixed
from boiler.commands import activity, gunrunner, kw18, vendor, video  # noqa: F401 E402
