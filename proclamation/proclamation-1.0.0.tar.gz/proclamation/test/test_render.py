#!/usr/bin/env python3 -i
# Copyright 2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0

from ..project import Project
from ..render import (combine_changelogs, get_split_news_file,
                      split_news_contents)
from ..settings import ProjectSettings

NEWS_FILE_1 = """# Sample NEWS file

## Test 1.0 (date goes here)

## Previous

## More previous

"""


def test_split_news():
    proj_settings = ProjectSettings("Test")
    before, after = split_news_contents(proj_settings, NEWS_FILE_1)
    assert("Sample" in before)
    assert("Previous" in after)
    assert(after.startswith("##"))


def test_missing_news_file():
    proj_settings = ProjectSettings("Test", news_filename="nonexistent-file")
    before, after = get_split_news_file(proj_settings)
    assert(after == "")
    assert(before.endswith("\n"))


def test_duplicated_version():
    proj_settings = ProjectSettings("Test", news_filename="nonexistent-file")
    before, after = split_news_contents(proj_settings, NEWS_FILE_1)
    assert("Test 1.0" in after)
    project = Project(proj_settings)
    try:
        combine_changelogs(before, after, project, "1.0", "date goes here")
    except RuntimeError:
        assert(True)
        return
    assert(False)  # We expect an error.
