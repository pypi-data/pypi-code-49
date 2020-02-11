"""
CLI commands for docker actions
"""


import json
import tempfile
from os import makedirs, path

import click

from brewblox_dev import utils

WORKDIR = path.expanduser('~/.cache/brewblox-dev/docker')

PYTHON_TAGS = [
    '3.7', '3.7-slim',
    '3.8', '3.8-slim',
]
NODE_TAGS = [
    '10', '10-alpine',
    '12', '12-alpine',
]

AMD_ARM_REPOS = [
    'brewblox/brewblox-ctl-lib',
    'brewblox/brewblox-devcon-spark',
    'brewblox/brewblox-history',
    'brewblox/brewblox-mdns',
    'brewblox/brewblox-ui',
    'brewblox/firmware-flasher',
    'brewblox/brewblox-emitter',
]
AMD_REPOS = [
    'brewblox/firmware-simulator',
]


@click.group()
def cli():
    """Collection group"""


def enable_experimental():
    cfg = '/etc/docker/daemon.json'
    try:
        with open(cfg, 'r') as f:
            content = f.read()
            config = json.loads(content or '{}')
    except FileNotFoundError:  # pragma: no cover
        config = {}

    if config.get('experimental'):
        return

    h, temp = tempfile.mkstemp()

    with open(temp, 'w') as f:
        config['experimental'] = True
        json.dump(config, f, indent=4)

    utils.run(f'sudo mv -f {temp} {cfg}')
    utils.run('sudo systemctl restart docker')


def install_qemu():
    utils.run('sudo apt update')
    utils.run('sudo apt install -y qemu qemu-user-static qemu-user binfmt-support')
    utils.run(f'cp $(which qemu-arm-static) {WORKDIR}/')


def build_python_images():
    for tag in PYTHON_TAGS:
        with open(f'{WORKDIR}/Dockerfile', 'w') as f:
            f.write('\n'.join([
                f'FROM arm32v7/python:{tag}',
                'COPY ./qemu-arm-static /usr/bin/qemu-arm-static',
            ]))
        utils.run(f'docker pull --platform=linux/arm arm32v7/python:{tag}')
        utils.run(f'docker build --platform=linux/arm --no-cache -t brewblox/rpi-python:{tag} {WORKDIR}')
        utils.run(f'docker push brewblox/rpi-python:{tag}')


def build_node_images():
    for tag in NODE_TAGS:
        with open(f'{WORKDIR}/Dockerfile', 'w') as f:
            f.write('\n'.join([
                f'FROM arm32v7/node:{tag}',
                'COPY ./qemu-arm-static /usr/bin/qemu-arm-static',
            ]))
        utils.run(f'docker pull --platform=linux/arm arm32v7/node:{tag}')
        utils.run(f'docker build --platform=linux/arm --no-cache -t brewblox/rpi-node:{tag} {WORKDIR}')
        utils.run(f'docker push brewblox/rpi-node:{tag}')

    # Alpine is an exception, as it runs on armv6, and must install packages
    with open(f'{WORKDIR}/Dockerfile', 'w') as f:
        f.write('\n'.join([
            'FROM arm32v6/alpine',
            'COPY ./qemu-arm-static /usr/bin/qemu-arm-static',
            'RUN apk add --no-cache nodejs npm',
        ]))

    utils.run('docker pull --platform=linux/arm arm32v6/alpine')
    utils.run(f'docker build --platform=linux/arm --no-cache -t brewblox/rpi-node:10-alpine {WORKDIR}')
    utils.run('docker push brewblox/rpi-node:10-alpine')


@cli.command()
def docker_info():
    print(f'Stash directory:', WORKDIR)
    print('Python tags', *PYTHON_TAGS, sep='\n\t')
    print('Node tags', *NODE_TAGS, sep='\n\t')
    print('AMD+ARM repositories:', *AMD_ARM_REPOS, sep='\n\t')
    print('AMD repositories:', *AMD_REPOS, sep='\n\t')


@cli.command()
@click.option('--python', is_flag=True, help='Build and push Python images')
@click.option('--node', is_flag=True, help='Build and push Node images')
def docker_images(python, node):
    """Create base images used by various BrewBlox projects"""
    makedirs(WORKDIR, exist_ok=True)
    enable_experimental()
    install_qemu()

    if python:
        build_python_images()

    if node:
        build_node_images()


@cli.command()
def release_stable():
    """Push newest-tag -> stable for all managed repositories"""
    for repo in AMD_ARM_REPOS + AMD_REPOS:
        utils.run(f'docker pull {repo}:newest-tag')

    for repo in AMD_ARM_REPOS:
        utils.run(f'docker pull {repo}:rpi-newest-tag')

    # start pushing after all pulls are ok

    for repo in AMD_ARM_REPOS + AMD_REPOS:
        utils.run(f'docker tag {repo}:newest-tag {repo}:stable')
        utils.run(f'docker push {repo}:stable')

    for repo in AMD_ARM_REPOS:
        utils.run(f'docker tag {repo}:rpi-newest-tag {repo}:rpi-stable')
        utils.run(f'docker push {repo}:rpi-stable')
