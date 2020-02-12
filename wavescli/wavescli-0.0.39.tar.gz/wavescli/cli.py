#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import yaml
import subprocess
import click

from wavescli import VERSION


@click.group()
@click.pass_context
@click.version_option(version=VERSION)
def main(ctx):
    WAVES_URL = os.environ.get('WAVES_URL')

    ctx.obj['config'] = {
        'WAVES_URL': WAVES_URL,
    }


@main.command(name='create')
@click.option('--workflow/--businesstask', required=True, default=True)
@click.argument('yaml_filepath', required=True, type=click.File('r'))
@click.pass_context
def create(ctx, workflow, yaml_filepath):
    """
    Create a workflow/business task from a YAML file
    """
    definition_str = yaml_filepath.read()
    if workflow and definition_str:
        click.secho("   Creating workflow...", fg='green')
        output = ctx.obj.client.create_workflow(definition_str)

    elif not workflow and definition_str:
        click.secho("   Creating businesstask...", fg='green')
        output = ctx.obj.client.register_businesstask(definition_str)

    click.secho(json.dumps(output, indent=2, sort_keys=True), fg='yellow')


@main.command(name='publish')
@click.option('--businesstask', required=True, default=True)
@click.argument('yaml_filepath', required=True, type=click.File('r'))
@click.pass_context
def publish(ctx, businesstask, yaml_filepath):
    """
    Publish a business task from a YAML file
    """
    definition_str = yaml_filepath.read()
    if businesstask and definition_str:
        click.secho("   Publishing businesstask...", fg='green')
        new_btask = ctx.obj.client.publish_businesstask(definition_str)
        click.secho(json.dumps(new_btask, indent=2, sort_keys=True), fg='yellow')


@main.command(name='worker')
@click.option('--start/--stop', required=True, default=True)
@click.option('--tasks', required=False, help='The path for the business task tasks.py file')
@click.argument('yaml_filepath', required=True, type=click.File('rb'))
def worker(start, tasks, yaml_filepath):
    """
    Start/Stop worker to receiving messages from Waves broker
    """
    definition = yaml.load(yaml_filepath, Loader=yaml.FullLoader)

    if start and definition:
        start_worker(definition, tasks)
    else:
        stop_worker(definition, tasks)


def start_worker(definition, tasks):
    task_name = definition.get('name')
    task_version = definition.get('version', 'latest')
    tasks_module = definition.get('tasks_module', 'waves.btasks.app')
    if tasks:
        tasks_module = tasks
    default_queue = 'wv_{}@{}'.format(task_name, task_version)
    loglevel = 'INFO'

    concurrency = os.environ.get('CELERY_CONCURRENCY', 1)
    queue = os.environ.get('QUEUE_NAME', default_queue)
    worker_name = os.environ.get('WORKER_PRIVATE_IP', '%h')

    # --detach
    cmd = 'celery -A {} worker --hostname {}@{} --loglevel={} --task-events -Ofair -c {} -Q {}'.format(
        tasks_module, task_name, worker_name, loglevel, concurrency, queue)
    click.secho("   ...Starting worker\n{}".format(cmd), fg='yellow')

    subprocess.call(cmd.split(' '))


def stop_worker(definition, tasks):
    tasks_module = definition.get('tasks_module', 'waves.btasks.app')

    if tasks:
        tasks_module = tasks

    cmd = 'celery -A {} control shutdown'.format(tasks_module)
    click.secho("   ...Stopping worker\n{}".format(cmd), fg='yellow')

    subprocess.call(cmd.split(' '))


@main.command(name='init')
@click.option('--project',
              type=click.Choice(['New', 'Existing'], case_sensitive=False), prompt=True)
def worker_init(project):
    """
    Add waves files
    cookiecutter https://gitlab.spacetimeanalytics.com/waves/bt-template.git -c existing
    """
    click.secho("   ...project{}".format(project), fg='yellow')

    template = 'https://gitlab.spacetimeanalytics.com/waves/bt-template.git'

    existing_project = project.upper() == 'EXISTING'
    cmd = 'cookiecutter {}{}'.format(
        template, ' -f -c existing' if existing_project else '')

    click.secho("   ...Initializing Waves' files\n", fg='yellow')

    subprocess.call(cmd.split(' '))
