#!/usr/bin/env python3 -i
# Copyright 2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0

from ..types import Fragment, ReferenceParser

from io import StringIO


def test_ref_parse():
    parser = ReferenceParser()
    assert(parser.parse("issue.54.md").item_type == "issue")
    assert(parser.parse("issue.54.md").number == 54)

    assert(parser.parse("issue.54").item_type == "issue")
    assert(parser.parse("issue.54").number == 54)

    assert(parser.parse("issue.54").as_tuple() ==
           parser.parse("issue.54.md").as_tuple())

    assert(parser.parse(".gitignore") is None)
    assert(parser.parse(".git-keep") is None)


def test_ref_parse_filename():
    parser = ReferenceParser()
    assert(parser.parse_filename("issue.54.md").item_type == "issue")
    assert(parser.parse_filename("issue.54.md").number == 54)
    assert(parser.parse_filename("issue.54") is None)
    assert(parser.parse_filename(".gitignore") is None)
    assert(parser.parse_filename(".git-keep") is None)


FRAGMENT = """---
- issue.55
- mr.23
pr.25
issue.54
---
This is content.
"""


def test_fragment():
    fn = "issue.54.md"
    fragmentio = StringIO(FRAGMENT)
    fragment = Fragment(fn, io=fragmentio)
    assert(str(fragment.filename) == fn)
    assert(len(fragment.refs) == 1)
    fragment.parse_file()
    assert("content" in fragment.text)
    assert("---" not in fragment.text)

    # duplicates don't get added
    assert(len(fragment.refs) == 4)


SIMPLE_FRAGMENT = """This is a simple fragment content.
"""


def test_simple_fragment():
    fn = "issue.54.md"
    fragmentio = StringIO(SIMPLE_FRAGMENT)
    fragment = Fragment(fn, io=fragmentio)
    assert(str(fragment.filename) == fn)
    assert(len(fragment.refs) == 1)
    fragment.parse_file()
    assert(len(fragment.refs) == 1)
    assert("content" in fragment.text)
