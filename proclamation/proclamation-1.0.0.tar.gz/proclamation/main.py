#!/usr/bin/env python3
# Copyright (c) 2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0
"""Main entry point."""

import logging

import click

from .project import Project
from .render import generate_updated_changelog, render_template
from .settings import settings_from_json_file


class ProjectCollection:
    """Specifies a config file, project, and other options.

    Typically populated by whatever is parsing a command line.
    """

    def __init__(self, config_file, project_name, default_base,
                 ref_parser=None):
        """Construct the ProjectCollection, including creating all Project
        objects."""
        self.project_name = project_name
        self.default_base = default_base
        settings = settings_from_json_file(config_file)
        self.projects = []
        log = logging.getLogger(__name__).getChild("ProjectCollection")
        for project_settings in settings.projects:
            if not self.should_process_project(project_settings.name):
                log.info("Skipping project %s, not selected on command line")
                continue

            log.debug("Initializing project %s", project_settings.name)
            self.projects.append(Project(project_settings,
                                         default_base=default_base,
                                         ref_parser=ref_parser))

    def should_process_project(self, proj_name):
        if self.project_name is None:
            return True
        return self.project_name == proj_name


pass_project_collection = click.make_pass_decorator(ProjectCollection)


@click.group()
@click.option("-c", "--config",
              "config_file",
              type=click.Path(file_okay=True, dir_okay=False, readable=True),
              default=".proclamation.json",
              show_default=True,
              help="Config filename")
@click.option("-p", "--project",
              "project_name",
              metavar="NAME",
              default=None,
              help="Specify a single project from the config to process. "
              "If omitted, all projects in the config will be processed.")
@click.option("--default-base",
              "default_base",
              default=None,
              type=click.Path(file_okay=False, dir_okay=True),
              help="Specify a different default base directory to search.")
@click.option("-v", "--verbose",
              "verbose",
              count=True,
              help="Show verbose info messages. Repeat for more verbosity.")
@click.pass_context
def cli(ctx, config_file, project_name, default_base, verbose):
    """Proclamation builds your NEWS files from fragments."""
    fmt = "[%(levelname)s:%(name)s]  %(message)s"
    if verbose >= 2:
        logging.basicConfig(format=fmt, level=logging.DEBUG)
        logging.getLogger(__name__).debug("Debug logging enabled.")
    elif verbose == 1:
        logging.basicConfig(format=fmt, level=logging.INFO)
        logging.getLogger(__name__).info("Verbose logging enabled.")
    else:
        logging.basicConfig(format=fmt)
    ctx.obj = ProjectCollection(config_file, project_name, default_base)


@cli.command()
@click.argument("project_version", metavar="VERSION", required=False)
@click.option("--date",
              "release_date",
              default=None,
              help="Release date if not today.")
@click.pass_context
@pass_project_collection
def draft(project_collection, ctx, project_version, release_date=None,
          ref_parser=None):
    """Preview the new VERSION portion of your NEWS file(s) to stdout.

    If no version is provided, a dummy value is used."""

    if project_version is None:
        project_version = "v.next (DRAFT)"
    for project in project_collection.projects:
        project.populate_sections(ref_parser)
        print(render_template(project, project_version, release_date))


@cli.command()
@click.argument("project_version", metavar="VERSION")
@click.option("--date",
              "release_date",
              default=None,
              help="Release date if not today.")
@click.option("-d", "--delete-fragments",
              "delete_fragments",
              is_flag=True,
              help="Delete processed fragments when complete")
@click.option("-o", "--overwrite",
              is_flag=True,
              help="Write updated changelog to disk, instead of to stdout.")
@click.pass_context
@pass_project_collection
def build(project_collection, ctx, project_version, release_date=None,
          delete_fragments=False, overwrite=False, ref_parser=None):
    """Build your new NEWS file."""
    if not overwrite and len(project_collection.projects) != 1:
        raise click.UsageError(
            "You may only build a single project at a time: "
            "please specify --project-name or use --overwrite",
            ctx)
    for project in project_collection.projects:
        project.populate_sections(ref_parser)
        new_contents = generate_updated_changelog(project, project_version,
                                                  release_date)
        if overwrite:
            fn = project.settings.news_filename
            with open(fn, 'w', encoding='utf-8') as fp:
                fp.write(new_contents)
        else:
            print(new_contents)

    if delete_fragments:
        remove_fragments(project_collection, ctx, ref_parser=ref_parser)


@cli.command()
@click.confirmation_option()
@click.pass_context
@pass_project_collection
def remove_fragments(project_collection, ctx, ref_parser=None):
    """Remove NEWS fragments associated with all projects (or specified projects).

    If you only have one project, or your projects don't share sections,
    you may consider using the --delete-fragments option of "build" instead.
    """
    all_files = set()
    for project in project_collection.projects:
        project.populate_sections(ref_parser)
        all_files += set(project.fragment_filenames)
    remove_files(all_files)


def remove_files(files):
    log = logging.getLogger(__name__)
    for f in files:
        try:
            f.unlink()
            log.info("Removed %s", f)
        except FileNotFoundError:
            log.info("Skipping %s, not found", f)
