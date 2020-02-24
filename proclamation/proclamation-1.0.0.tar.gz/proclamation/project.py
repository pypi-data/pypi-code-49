#!/usr/bin/env python3 -i
# Copyright 2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0
"""Loading data for a project."""

import logging
from itertools import chain
from pathlib import Path

from .types import ReferenceParser, Section


def _resolve_with_base(base_dir, path):
    path = Path(path)
    return (base_dir / path).resolve()


class Project:
    """A project has sections and fragments."""

    def __init__(self, settings, ref_parser=None, default_base=None):
        """Construct a project.

        settings: a ProjectSettings object.
        ref_parser: optional, a reference parser if the default is not
        suitable.
        default_base: optional, default base directory. If unset, defaults to
        the current working directory.
        """
        super().__init__()
        if default_base is None:
            default_base = Path(".").resolve()
        self.default_base = default_base

        if ref_parser is None:
            ref_parser = ReferenceParser()
        self.ref_parser = ref_parser

        self.name = settings.name
        self.settings = settings
        self.template = settings.template

        self._log = logging.getLogger(
            __name__).getChild("Project." + self.name)

        self.sections = []
        sections = self.sections
        for section_settings in settings.sections:
            self._log.debug("Instantiating section %s", section_settings.name)
            section = Section(section_settings.name,
                              section_settings.directory)
            sections.append(section)

    def populate_sections(self, ref_parser=None):
        """Load fragments associated with each section."""
        if ref_parser is None:
            ref_parser = self.ref_parser
        for section in self.sections:
            directory = _resolve_with_base(
                self.default_base, section.relative_directory)
            self._log.info("Populating section %s from files in %s",
                           section.name, str(directory))
            section.populate_from_directory(directory, ref_parser)

    @property
    def fragment_filenames(self):
        """Return filenames for all fragments added in all sections."""
        return chain(*(section.fragment_filenames
                       for section in self.sections))
