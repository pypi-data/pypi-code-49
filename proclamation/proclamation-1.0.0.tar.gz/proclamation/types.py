#!/usr/bin/env python3 -i
# Copyright 2020 Collabora, Ltd.
#
# SPDX-License-Identifier: Apache-2.0

import logging

from pathlib import Path

_LOG = logging.getLogger(__name__)

FRONT_MATTER_DELIMITER = "---"


class Reference:
    """A simple class storing the information about a reference."""

    def __init__(self, item_type, number, service_params):
        """Construct a Reference from a parsed reference string."""
        super().__init__()

        self.item_type = item_type
        """Item type, like issue, mr, pr."""

        self.number = number
        """Reference number."""

        self.service_params = service_params
        """A list/tuple of any additional parameters associated with the
        service."""

    def as_tuple(self):
        """Return all contents as a tuple for use in sets and maps.

        Required of all classes that are to be used as a reference,
        for de-duplication.
        """
        return (self.item_type, self.number, tuple(self.service_params))


class ReferenceParser:
    """The base class and default "reference parser".

    If you choose to customize this functionality, inherit from it.
    Otherwise, use it as-is.

    Reference parsers may (this one does) use the Reference class from this
    module, but it's not required.
    Whatever suits you best is fine as long as it works with your template.

    References are things like ticket numbers, issue numbers, merge/pull
    request numbers, etc. This portion of the system is left fairly flexible
    since there are almost as many project administration structures as there
    are projects.
    """

    def __init__(self):
        """Construct parser."""
        self.extensions_to_drop = set(('md', 'rst', 'txt'))

    def split_on_dot_and_drop_ext(self, s):
        """Return the .-delimited portions of a name/ref, excluding a file extension,
        and whether or not a file extension was removed.

        A utility function likely to be used in classes resembling this one.
        """
        elts = s.split(".")
        if elts[-1] in self.extensions_to_drop:
            elts.pop()
            return elts, True
        return elts, False

    def make_reference(self, elts):
        """Convert a tuple of elements into a reference.

        This might be the only function you need to override.
        """
        if len(elts) < 2:
            # Only one component: Can't be a ref.
            return None
        try:
            return Reference(item_type=elts[0],
                             number=int(elts[1]),
                             service_params=elts[2:])
        except ValueError:
            # Conversion failure, etc. means this isn't actually a ref
            return None

    def parse_filename(self, s):
        """Turn a filename string into a reference or None.

        May override or extend.
        """
        elts, removed_extension = self.split_on_dot_and_drop_ext(s)
        if not removed_extension:
            # Filenames must have the extension
            return None
        elts = s.split(".")
        if elts[-1] in self.extensions_to_drop:
            elts.pop()
        else:
            return None

        if elts and not elts[0]:
            # Empty first component: not a valid ref file.
            return None
        return self.make_reference(elts)

    def parse(self, s):
        """Turn a string into a reference or None.

        May override or extend.
        """
        elts, _ = self.split_on_dot_and_drop_ext(s)

        return self.make_reference(elts)


class Fragment:
    """A single CHANGES/NEWS entry, provided as text to insert into the templates.

    A fragment comes from a file or stream.

    The fragment filename is parsed to provide one reference. Optionally, an
    extremely small subset of "YAML front matter" can be used to list
    additional references in the fragment file contents. Delimit the front
    matter with --- both before and after, and place one reference per line
    (with or without leading -) between those delimiters.
    """

    def __init__(self, filename, reference=None, ref_parser=None, io=None):
        """Construct a fragment.

        Filename is used to open the file, if io is not provided.
        ref_parser parses "reference" strings (referring to PR/MR/issue) into
        a reference object.
        A default is provided.
        For testing or advanced stuff, pass a file handle or something like
        StringIO to io, in which case filename is not used.
        """
        super().__init__()
        filename = Path(filename)
        self.filename = filename
        self.text = ""
        self.io = io
        if ref_parser is None:
            ref_parser = ReferenceParser()
        self._ref_parser = ref_parser

        if not reference:
            reference = ref_parser.parse_filename(filename.name)
        self.ref = reference
        self.refs = []
        self.known_refs = set()
        self._insert_ref(reference)

    def _insert_ref(self, reference):
        ref_tuple = reference.as_tuple()
        if ref_tuple not in self.known_refs:
            self.refs.append(reference)
            self.known_refs.add(ref_tuple)

    def add_ref(self, s):
        """Parse a string as a reference and add it to this fragment."""
        ref_tuple = self._ref_parser.parse(s)
        if not ref_tuple:
            return
        self._insert_ref(ref_tuple)

    def _parse_front_matter(self, fp):
        log = logging.getLogger(__name__)
        while 1:
            line = fp.readline()
            if not line:
                return
            line = line.strip()
            if line == FRONT_MATTER_DELIMITER:
                return

            # Strip "bullet points" so this can look more yaml-like
            if line.startswith("- "):
                line = line[2:].strip()
            log.debug("Front matter reference text: %s", line)
            self.add_ref(line)

    def _parse_io(self, fp):
        line = fp.readline()
        if line.strip() == FRONT_MATTER_DELIMITER:
            self._parse_front_matter(fp)
            line = fp.readline()
        while 1:
            if not line:
                break
            self.text += line
            line = fp.readline()
        self.text = self.text.strip()
        log = logging.getLogger(__name__)
        log.debug("Got fragment starting with '%s'", self.text[:20])

    def parse_file(self):
        """Open the file and parse content, and front matter if any.

        If io was provided at construction time, that is parsed instead.
        """
        if self.io is not None:
            self._parse_io(self.io)
            return
        with open(str(self.filename), 'r', encoding='utf-8') as fp:
            self._parse_io(fp)


class Section:
    """A section is a component/aspect of a project.

    Changes for a Section are (potentially) separated out in the news file.
    For example, sections might include "Drivers", "UI", etc.
    """

    def __init__(self, name, relative_directory=None):
        super().__init__()
        self.name = name
        self.relative_directory = relative_directory
        self.fragments = []
        self._log = _LOG.getChild("Section." + name)

    def populate_from_directory(self, directory, ref_parser):
        """Iterate through a directory, trying to parse each filename as a reference.

        Files that parse properly are assumed to be fragments,
        and a Fragment object is instantiated for them.
        """
        for fragment_name in directory.iterdir():
            fragment_ref = ref_parser.parse(fragment_name.name)
            if not fragment_ref:
                # Actually not a fragment, skipping
                # print()
                self._log.debug("Not actually a fragment: %s", fragment_name)
                continue
            fragment = Fragment(fragment_name, fragment_ref, ref_parser)
            self.fragments.append(fragment)
            self._log.debug("added: %s", fragment_name)
            fragment.parse_file()

    @property
    def fragment_filenames(self):
        """Return a generator of filenames for all fragments added."""
        return (fragment.filename for fragment in self.fragments)
