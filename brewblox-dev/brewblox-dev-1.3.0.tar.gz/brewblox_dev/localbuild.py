#! /usr/bin/python3


import re
from glob import glob
from os import getenv, remove
from subprocess import check_output

import click

from brewblox_dev import utils


@click.group()
def cli():
    """Command collector"""


@cli.command()
@click.option('-a', '--arch', multiple=True, type=click.Choice(['amd', 'arm']),
              help='Build target. Can be repeated. Default: amd')
@click.option('-r', '--repo', default=lambda: getenv('DOCKER_REPO'),
              help='Docker repository name.')
@click.option('-c', '--context', default='docker',
              help='Docker build context.')
@click.option('-f', '--file', default='Dockerfile',
              help='Filename inside build context.')
@click.option('-t', '--tag', multiple=True,
              help='Additional tag. the "local" tag is always built.')
@click.option('--branch-tag', is_flag=True,
              help='Use sanitized branch name as tag. ARM automatically gets prefixed with "rpi-".')
@click.option('--setup/--no-setup', default=True,
              help='Perform Python-related setup steps.')
@click.option('--pull', is_flag=True,
              help='Pull base images.')
@click.option('--push', is_flag=True,
              help='Push all tags except "local" to Docker Hub.')
def localbuild(arch, repo, context, file, tag, branch_tag, setup, pull, push):
    """Build docker containers"""
    arch = list(arch or ['amd'])
    tags = list(tag)

    if branch_tag:
        tags.append(getenv('TRAVIS_BRANCH')  # Travis
                    or getenv('Build.SourceBranchName')  # Azure Pipelines
                    or check_output('git rev-parse --abbrev-ref HEAD'.split()).decode().rstrip())

    tags = [re.sub('[/_:]', '-', t) for t in tags]

    if setup:
        for f in glob('dist/*'):
            remove(f)

        utils.run('python setup.py sdist')
        utils.run(f'pipenv lock --requirements > {context}/requirements.txt')
        utils.distcopy('dist/', [f'{context}/dist/'])

    # single command
    utils.run(f'cd {context}'
              ' && if [ -f ./localbuild.sh ]; then bash ./localbuild.sh; fi')

    for a in arch:
        prefix = ''
        commands = []
        build_args = []
        build_tags = [
            'local',
            *tags
        ]

        if a == 'arm':
            prefix = 'rpi-'
            commands += [
                'docker run --rm --privileged multiarch/qemu-user-static:register --reset',
            ]

        if pull:
            build_args.append('--pull')

        build_args += [
            '--build-arg service_info="$(git describe) @ $(date)"',
            '--no-cache',
            ' '.join([f'--tag {repo}:{prefix}{t}' for t in build_tags]),
            f'--file {context}/{a}/{file}',
            context,
        ]

        commands.append(f'docker build {" ".join(build_args)}')
        utils.run(' && '.join(commands))

        if push:
            # We're skipping the local tag
            [utils.run(f'docker push {repo}:{prefix}{t}') for t in tags]
