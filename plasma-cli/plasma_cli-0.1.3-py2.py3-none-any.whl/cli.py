#!/usr/bin/env python

import plasmacli.component_manager as component_manager
import plasmacli.workflow_manager as workflow_manager
import plasmacli.project_manager as project_manager
import click
import os
import collections


class OrderedGroup(click.Group):
    def __init__(self, name=None, commands=None, **attrs):
        super(OrderedGroup, self).__init__(name, commands, **attrs)
        #: the registered subcommands by their exported names.
        self.commands = commands or collections.OrderedDict()

    def list_commands(self, ctx):
        return self.commands


@click.group(cls=OrderedGroup)
def cli():
    pass


# Plasma project group 

@click.group(cls=OrderedGroup,help='manage plasma projects')
def project():
    pass


@click.argument('project_name', required=True)
@click.command(name="create", help="creates a plasma project", )
def create_plasma_project(project_name):
    project_manager.create_project(project_name)


@click.argument('project_path', required=True)
@click.command(name="load", help="loads a plasma project", )
def load_plasma_project(project_path):
    project_manager.load_project(project_path)


@click.command(name="info", help="displays plasma project info", )
def describe_project(project_name):
    get_project_info()



# Workflow command group

@click.group(cls=OrderedGroup,help="manage plasma workflows")
def workflow():
    pass


@click.command(name="list", help="list existing workflows")
def list_workflow():
    workflow_manager.list_workflows()


@click.command(name="run", help="run workflow")
@click.argument('workflow_name', required=True)
def run_workflow(workflow_name):
    print('\n> Running workflow '+workflow_name+'\n')
    workflow_manager.run_workflow(workflow_name)


@click.command(name="stop", help="stop workflow")
@click.argument('workflow_name', required=True)
def stop_workflow(workflow_name):
    print('\n> Stopping workflow '+workflow_name+'\n')
    workflow_manager.stop_workflow(workflow_name)


@click.command(name="schedule", help="schedule workflows")
@click.argument('workflow_name', required=True)
@click.argument('cron_rule',required=True)
def schedule_workflow(workflow_name,cron_rule):
    workflow_manager.schedule_workflow(workflow_name,cron_rule)


# Component command group

@click.group(cls=OrderedGroup,help="manage plasma components")
def component():
    pass


@click.command(name="list", help="list components")
def list_component():
    component_manager.list_components()


@click.command(name="search", help="search for components")
@click.argument('component_name', required=True)
def search_component(component_name):
    component_manager.search_components(component_name)


@click.command(name="get", help="download components")
@click.argument('component_name', required=True)
def get_component(component_name):
    component_manager.download_component(component_name)


@click.command(name="describe", help="download components")
@click.argument('component_name', required=True)
def describe_component(component_name):
    component_manager.describe_component(component_name)


def build_cli():
    project.add_command(create_plasma_project)
    project.add_command(load_plasma_project)
    project.add_command(describe_project)
    workflow.add_command(list_workflow)
    workflow.add_command(run_workflow)
    workflow.add_command(stop_workflow)
    workflow.add_command(schedule_workflow)
    component.add_command(list_component)
    component.add_command(search_component)
    component.add_command(get_component)
    component.add_command(describe_component)
    cli.add_command(project)
    cli.add_command(component)
    cli.add_command(workflow)
    return cli


def main():
    cli = build_cli()
    cli()


if __name__=="__main__":
    main()
