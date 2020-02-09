#!/usr/bin/env python3
# vim: set filetype=python sts=4 ts=4 sw=4 expandtab tw=100 cc=+1:
# pylint: disable=bad-continuation,multiple-statements,missing-docstring
# SPDX-License-Identifier: CC0-1.0

import argparse
import re

class ArgParseNode:
    # pylint: disable=too-many-instance-attributes,too-many-arguments
    _subparser_regex = re.compile("^subparser_(.*)$")
    def __init__(self, options, default_options=None,
        subparser_options=None, name=None, parent=None):
        self.children = {}
        self._subparsers = None
        if parent:
            self.name = name
            self.parent = parent
            self.root = parent.root
            self.default_options = parent.default_options
            self.subparser_options = subparser_options or parent.subparser_options or {}
            self._parser = parent.subparsers.add_parser(name, **(options or self.default_options))
        else:
            self.name = None
            self.parent = None
            self.root = self
            self.default_options = default_options or {}
            self.subparser_options = subparser_options or {}
            self._parser = argparse.ArgumentParser(**(options or self.default_options))

    def create(self, name, options=None, subparser_options=None):
        if name in self.children:
            raise KeyError("Node with name {} already exist on {}".format(name, self.name))
        return self.get(name, options, None, subparser_options)

    def get(self, name, options=None, no_create=None, subparser_options=None):
        if name not in self.children:
            if no_create:
                raise KeyError("Node with name {} does not exist on {}".format(name, self.name))
            self.children[name] = ArgParseNode(options, None, subparser_options, name, self)
        return self.children[name]

    def get_path(self, path, options=None, no_create=None, subparser_options=None):
        current = self
        for segment in path.split("/"):
            current = current.get(segment, options, no_create, subparser_options)
        return current

    @property
    def parser(self):
        return self._parser

    @property
    def level(self):
        if self.parent is not None: return self.parent.level + 1
        return 0

    @property
    def subparsers(self):
        if self._subparsers is None:
            self._subparsers = self.parser.add_subparsers(
                dest="subparser_{:d}".format(self.level), **self.subparser_options)
        return self._subparsers

    @property
    def path_list(self):
        if self.parent is not None:
            tmp = self.parent.path_list
            tmp.append(self.name)
            return tmp
        return []

    @property
    def path(self):
        return "/".join(self.path_list)

    @classmethod
    def get_selected_path_list(cls, parse_result):
        parts = []
        pdict = parse_result.__dict__
        for key, value in pdict.items():
            if value is None: continue
            re_result = cls._subparser_regex.match(key)
            if re_result:
                index = int(re_result.group(1))
                parts.insert(index, value)
        return parts

    @classmethod
    def get_selected_path(cls, parse_result):
        path_list = cls.get_selected_path_list(parse_result)
        return "/".join(path_list)

    def get_selected_node(self, parse_result):
        if self is not self.root: return self.root.get_selected_node(parse_result)
        selected_path_list = self.get_selected_path_list(parse_result)
        if not selected_path_list: return self
        selected_node = self
        for part in selected_path_list:
            selected_node = selected_node.get(part, None, True)
        return selected_node
