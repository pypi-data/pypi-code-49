#!/usr/bin/env python3 -i
# Copyright 2019-2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0
"""Use Jinja2 to render an addition to the CHANGES file.

This should be the only file that needs to import Jinja2,
so if you want to do something else for templating, you can.
"""

import logging
from datetime import date
from io import StringIO

from jinja2 import (ChoiceLoader, Environment, FileSystemLoader, PackageLoader,
                    TemplateSyntaxError)


def render_template(project, project_version, release_date=None):
    """Render the CHANGES template for a project.

    Returns the rendered text.
    """
    log = logging.getLogger(__name__)
    search_path = [project.default_base]
    log.debug(
        "Template search path is %s, followed by built-in templates.",
        str(search_path))
    loader = ChoiceLoader([
        FileSystemLoader(search_path),
        PackageLoader("proclamation", "templates")
    ])

    if release_date is None:
        release_date = date.today().isoformat().strip()

    env = Environment(autoescape=False, loader=loader)
    try:
        template = env.get_template(project.template)
    except TemplateSyntaxError as e:
        print("template syntax error during parse: {}:{} error: {}".
              format(e.filename, e.lineno, e.message))
        raise RuntimeError("Jinja2 template syntax error")

    log.info("Loaded template %s from %s", project.template, template.filename)
    try:
        return template.render({
            "project_name": project.name,
            "project_version": project_version,
            "date": release_date,
            "sections": project.sections
        })
    except TemplateSyntaxError as e:
        print("template syntax error during render: {}:{} error: {}".
              format(e.filename, e.lineno, e.message))
        raise RuntimeError("Jinja2 template syntax error")


def split_news_contents(project_settings, news_contents):
    """Split the contents of a NEWS file based on the insert point pattern.

    Two strings are returned: the content before the insert point, and the
    content after the insert point, including the line that matched the
    pattern.
    """
    io = StringIO(news_contents)
    before = []
    after = []
    found_first_line = False

    insert_point_re = project_settings.insert_point_re

    for line in io:
        if found_first_line:
            after.append(line)
            continue
        if insert_point_re.match(line):
            # OK, we hadn't found it, but now we did.
            found_first_line = True
            after.append(line)
            continue

        # haven't found it yet
        before.append(line)

    log = logging.getLogger(__name__)
    log.info("%d lines before the insert point in existing file, %d after",
             len(before), len(after))
    if not found_first_line:
        log.warning("Did not find a line that matches the "
                    "insert_point_pattern, there may be an error in "
                    "your settings")
    return "".join(before), "".join(after)


def get_split_news_file(project_settings):
    """Load configured NEWS file and return the content for before and after
    our new entry.

    We make a minimal default if we can't open the original.
    """
    fn = project_settings.news_filename
    try:
        with open(fn, 'r', encoding='utf-8') as fp:
            content = fp.read()
        return split_news_contents(project_settings, content)
    except FileNotFoundError:
        # Default "empty" changelog file
        return "# Changelog\n\n", ""


def combine_changelogs(before, after, project, project_version, release_date):
    """Return the text of the updated, complete CHANGES/NEWS file given
    pre-split contents."""
    new_portion = render_template(project, project_version, release_date)

    first_new_line = new_portion.split("\n", 1)[0]
    first_after_line = after.split("\n", 1)[0]

    log = logging.getLogger(__name__)
    log.info("First line of insert point: %s", first_after_line.rstrip())
    if first_after_line.rstrip() == first_new_line.rstrip():
        raise RuntimeError(
            "Your new NEWS entry has the same heading as the most recent "
            "existing entry! Probably duplicating version numbers.")
    return "".join((before,
                    new_portion,
                    after))


def generate_updated_changelog(project, project_version, release_date=None):
    """Return the text of the updated, complete CHANGES/NEWS file."""
    before, after = get_split_news_file(project.settings)

    return combine_changelogs(before, after, project, project_version,
                              release_date)
