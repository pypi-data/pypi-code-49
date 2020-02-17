import datetime

import click

from yeahyeah_plugins.clockify_plugin.context import (
    ClockifyPluginContext,
    pass_clockify_context,
    default_context,
    default_settings_file_name,
)

from yeahyeah_plugins.clockify_plugin.decorators import handle_clockify_exceptions
from yeahyeah_plugins.clockify_plugin.parameters import TIME
from yeahyeah_plugins.clockify_plugin.time import as_local, now_local
from yeahyeah.decorators import pass_yeahyeah_context
from yeahyeah.context import YeahYeahContext
from yeahyeah.persistence import JSONSettingsFile


@click.group(name="log")
@click.pass_context
@pass_yeahyeah_context
def main(context: YeahYeahContext, ctx):
    """write to clockify log"""
    settings_file = JSONSettingsFile(
        path=context.settings_path / default_settings_file_name
    )
    if not settings_file.exists():
        click.echo(
            f"Settings file not found. Writing default context to {settings_file.path}"
        )
        settings_file.save(dict_in=default_context.to_dict())
    ctx.obj = ClockifyPluginContext.init_from_dict(settings_file.load())


@click.command()
@pass_clockify_context
def status(context: ClockifyPluginContext):
    """Show server and api key"""
    click.echo(f"Using clockify web API session {context.session}")


@click.command()
@pass_clockify_context
@click.argument("message", nargs=-1)
@click.option("-p", "--project", type=str)
@click.option(
    "-t",
    "--time",
    type=TIME,
    default=0,
    help="Time (HH:MM) or time increment(+/-MM or +/-HH:MM)",
)
@handle_clockify_exceptions
def add(context: ClockifyPluginContext, message, project, time):
    """add log message"""
    if not message:
        raise click.BadParameter("Log message may not be empty")
    else:
        message = " ".join(message)
    if not time:
        time = now_local()
    if project:
        project_obj = find_project(context.session.get_projects(), project)
    else:
        project_obj = None

    log_start = time
    click.echo(f"Adding {message} at {as_local(log_start)} to project {project_obj}")
    context.session.add_time_entry(
        start_time=time, description=message, project=project_obj
    )


def find_project(project_list, project_name_part):
    """Try to match project_name to one of the projects found in context. Returns the first project that starts with
    project_name

    Parameters
    ----------
    project_list: List[Project]
        all projects to search in
    project_name_part: str
        pro

    Raises
    ------
    click.BadParameter
        When project can not be found
    """
    for project in project_list:
        if project.name.lower().startswith(project_name_part.lower()):
            return project
    msg = (
        f'Could not find project starting with "{project_name_part}". '
        f'Options: {", ".join([x.name for x in project_list])}'
    )
    raise click.BadParameter(msg)


@click.command()
@pass_clockify_context
@click.option(
    "-t",
    "--time",
    type=TIME,
    default=0,
    help="Time (HH:MM) or time increment(+/-MM or +/-HH:MM)",
)
@handle_clockify_exceptions
def stop(context: ClockifyPluginContext, time):
    """stop any active logging stopwatch"""
    if not time:
        time = now_local()
    result = context.session.stop_timer(time)
    if result:
        click.echo(f"stopped {result}")
    else:
        click.echo("No timer was running")


@click.command()
@pass_clockify_context
@handle_clockify_exceptions
def projects(context: ClockifyPluginContext):
    """Lists available projects for current clockify user"""
    projects_in = context.session.get_projects()
    if not projects_in:
        click.echo(f"No projects found")
    else:
        click.echo("\n".join([str(x) for x in projects_in]))


for func in [status, add, stop, projects]:
    main.add_command(func)


@click.command()
@pass_yeahyeah_context
def edit_settings(context: YeahYeahContext):
    """Open context file for editing"""
    click.launch(str(context.settings_path / default_settings_file_name))
