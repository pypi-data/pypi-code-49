#!/usr/bin/env python3 -i
# Copyright 2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0

import json
from io import StringIO

from ..settings import parse_project, settings_from_json_io

PROJ_NAME = "my project"

PROJECT = {
    "project_name": PROJ_NAME,
    "template": "dummy",
    "sections": {
        "main section": {
            "directory": "changes/main"
        }
    }
}


def dict_to_json_io(config):
    return StringIO(json.dumps(config))


def test_parse_project():
    proj = parse_project(PROJECT)
    assert(proj.name == PROJ_NAME)


def test_single_project():
    config = {
        "projects": [
            PROJECT
        ]
    }
    io = dict_to_json_io(config)
    settings = settings_from_json_io(io)
    assert(len(settings.projects) == 1)
    assert(settings.projects[0].name == PROJ_NAME)
    assert(settings.projects[0].template == "dummy")
    assert(len(settings.projects[0].sections) == 1)

# def test_multi_project():
#     pass


def test_project_toplevel():
    io = dict_to_json_io(PROJECT)
    settings = settings_from_json_io(io)
    assert(len(settings.projects) == 1)
    assert(settings.projects[0].name == PROJ_NAME)
    assert(settings.projects[0].template == "dummy")
    assert(len(settings.projects[0].sections) == 1)
