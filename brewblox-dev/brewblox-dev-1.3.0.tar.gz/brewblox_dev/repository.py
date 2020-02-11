"""
Commands for git operations
"""

from contextlib import suppress
from distutils.version import StrictVersion
from os import makedirs, path
from shutil import which
from subprocess import STDOUT, CalledProcessError, check_call, check_output

import click

from brewblox_dev import utils

HUB_VERSION = '2.10.0'
WORKDIR = path.expanduser('~/.cache/brewblox-dev/git')
REPOS = [
    'brewblox-devcon-spark',
    'brewblox-history',
    'brewblox-mdns',
    'brewblox-ui',
    'brewblox-ctl-lib',
    'brewblox-web-editor',
    'brewblox-firmware',
    'brewblox-plaato',
    'brewblox-emitter',
]


@click.group()
def cli():
    """Command collector"""


def create_repos():
    makedirs(WORKDIR, exist_ok=True)
    [
        check_output(
            f'git clone --no-checkout https://github.com/BrewBlox/{repo}.git', shell=True, cwd=WORKDIR)
        for repo in REPOS
        if not path.exists(f'{WORKDIR}/{repo}/.git')
    ]


def install_hub():
    [
        check_output(cmd, shell=True)
        for cmd in [
            f'wget https://github.com/github/hub/releases/download/v{HUB_VERSION}/hub-linux-amd64-{HUB_VERSION}.tgz',
            f'tar zxvf hub-linux-amd64-{HUB_VERSION}.tgz',
            f'sudo ./hub-linux-amd64-{HUB_VERSION}/install',
            f'rm -rf hub-linux-amd64-{HUB_VERSION}*',
        ]
    ]


def prepare():
    create_repos()
    if not which('hub') and utils.confirm('hub cli not found - do you want to install it?'):
        install_hub()


@cli.command()
def git_info():
    print('Stash directory:', WORKDIR)
    print('Github repositories:', *REPOS, sep='\n\t')
    check_call('hub --version', shell=True)


@cli.command()
def delta():
    """Show commit delta for all managed repositories"""
    prepare()

    headers = ['repository'.ljust(25), 'develop >', 'edge >', 'tag']
    print(*headers)
    # will include separators added by print()
    print('-' * len(' '.join(headers)))
    for repo in REPOS:
        check_output('git fetch --tags --quiet',
                     shell=True,
                     cwd=f'{WORKDIR}/{repo}')
        dev_edge = check_output(
            'git rev-list --count origin/edge..origin/develop',
            shell=True,
            cwd=f'{WORKDIR}/{repo}').decode().rstrip()
        edge_tag = check_output(
            'git rev-list --count $(git rev-list --tags --max-count=1)..origin/edge',
            shell=True,
            cwd=f'{WORKDIR}/{repo}').decode().rstrip()
        vals = [repo, dev_edge, edge_tag, '-']
        print(*[v.ljust(len(headers[idx])) for idx, v in enumerate(vals)])


@cli.command()
def release_edge():
    """Create develop -> edge PRs for all managed repositories"""
    prepare()

    for repo in REPOS:
        if not utils.confirm(f'Do you want to create a develop -> edge PR for {repo}?'):
            continue

        with suppress(CalledProcessError):
            check_call(
                'hub pull-request -b edge -h develop -m "edge release"',
                shell=True,
                cwd=f'{WORKDIR}/{repo}')


def bumped_version(current_version: str, bump_type: str) -> str:
    major, minor, patch = StrictVersion(current_version).version

    return {
        'major': lambda: f'{major + 1}.{0}.{0}',
        'minor': lambda: f'{major}.{minor + 1}.{0}',
        'patch': lambda: f'{major}.{minor}.{patch + 1}',
    }[bump_type]()


@cli.command()
@click.argument('increment', required=True, type=click.Choice(['major', 'minor', 'patch']))
@click.option('--init', is_flag=True)
def bump(increment, init):
    """Increases git tag containing semantic version"""
    if init:
        current_version = '0.0.0'
    else:
        # Get all version-formatted tags, but use the latest
        current_version = check_output(
            r'git tag -l *.*.* --contains $(git rev-list --tags --max-count=1)',
            shell=True
        ).decode().rstrip().split('\n')[-1]

    new_version = bumped_version(current_version, increment)

    print(f'Bumping "{increment}" version: {current_version} ==> {new_version}')

    if utils.confirm('Do you want to tag the current commit with that version?'):
        check_output(f'git tag -a {new_version} -m "Version {new_version}"', shell=True)

        print('Latest tags:')
        print(check_output('git tag --sort=-version:refname -n1 | head -n5', shell=True).decode().rstrip())

    else:
        print('Aborted. No tags were added!')
        return

    if utils.confirm('Do you want to push this tag?'):
        check_call('git push --tags', shell=True, stderr=STDOUT)
