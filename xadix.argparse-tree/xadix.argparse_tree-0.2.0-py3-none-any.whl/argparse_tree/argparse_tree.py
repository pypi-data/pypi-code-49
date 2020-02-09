#!/usr/bin/env python3
# vim: set filetype=python sts=4 ts=4 sw=4 expandtab tw=100 cc=+1:
# pylint: disable=bad-continuation,multiple-statements
# SPDX-License-Identifier: CC0-1.0
"""
This package provides a class :py:class:`ArgParseNode` which makes it easier to create complex
nested subcommands with argparse.

The author(s) of this file has made it available under CC0-1.0
https://spdx.org/licenses/CC0-1.0.html
"""

import argparse
import re

class ArgParseNode:
    # pylint: disable=too-many-instance-attributes,too-many-arguments
    """
    This class is a node in a tree of various subcommands.

    :param dict options: passed to :py:class:`argparse.ArgumentParser` constructor if this
        is the root node or the :py:meth:`argparse._SubParsersAction.add_parser` method.
    :param dict default_options: options to use when calling
        :py:meth:`argparse._SubParsersAction.add_parser` if none is supplied.
    :param dict subparser_options: options to pass to
        :py:meth:`argparse.ArgumentParser.add_subparsers`.
    :param str name: name of this node.
    :param ArgParseNode parent: parent of this node.
    """
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
        """
        Explicitly creates a child of this node which has the specified `name`.

        :param str name: The name of the child node to retrieve or create.
        :param dict options: the options to pass to :py:meth:`argparse._SubParsersAction.add_parser`
            when creating the new node.
        :param subparser_options: Options to pass to the add_subparsers call
            on this node's parser.
        :return: The child node.
        :rtype: ArgParseNode
        :raises KeyError: if there is already a node named `name`
        """
        if name in self.children:
            raise KeyError("Node with name {} already exist on {}".format(name, self.name))
        return self.get(name, options, None, subparser_options)

    def get(self, name, options=None, no_create=None, subparser_options=None):
        """
        Retrieve or create a child of this node which has the specified `name`.

        :param str name: The name of the child node to retrieve or create.
        :param dict options: the options to pass to :py:meth:`argparse._SubParsersAction.add_parser`
            when creating the new node.
        :param bool no_create: Whether or not a new node may be created. If failse this method will
            throw if the node does not exist.
        :param subparser_options: Options to pass to the add_subparsers call
            on this node's parser.
        :return: The child node.
        :rtype: ArgParseNode
        :raises KeyError: if `no_create` is set and there is no node named `name`
        """
        if name not in self.children:
            if no_create:
                raise KeyError("Node with name {} does not exist on {}".format(name, self.name))
            self.children[name] = ArgParseNode(options, None, subparser_options, name, self)
        return self.children[name]

    def get_path(self, path, options=None, no_create=None, subparser_options=None):
        """
        Retrieve or create a child of this node which has the specified `name`.

        :param str path: The forward slash ('/') delimited path for the node to retrieve.
        :param dict options: the options to pass to :py:meth:`argparse._SubParsersAction.add_parser`
            when creating the new node.
        :param bool no_create: Whether or not a new node may be created. If failse this method will
            throw if the node does not exist.
        :param subparser_options: Options to pass to the add_subparsers call
            on this node's parser.
        :return: The child node.
        :rtype: ArgParseNode
        :raises KeyError: if `no_create` is set and there is no node named `name`
        """
        current = self
        for segment in path.split("/"):
            current = current.get(segment, options, no_create, subparser_options)
        return current

    @property
    def parser(self):
        """
        The actual :py:class:`argparse.ArgumentParser` object associated with this node.
        """
        return self._parser

    @property
    def level(self):
        """
        The level index of this node (root is 0).
        """
        if self.parent is not None: return self.parent.level + 1
        return 0

    @property
    def subparsers(self):
        """
        The :py:class:`argparse._SubParsersAction` associated with this node as returned
        by :py:meth:`argparse.ArgumentParser.add_subparsers`
        """
        if self._subparsers is None:
            self._subparsers = self.parser.add_subparsers(
                dest="subparser_{:d}".format(self.level), **self.subparser_options)
        return self._subparsers

    @property
    def path_list(self):
        """
        The path to the current `ArgParseNode` as a list of strings that consist
        of each of the :py:attr:`ArgParseNode.name` values of the nodes (except for the root).
        """
        if self.parent is not None:
            tmp = self.parent.path_list
            tmp.append(self.name)
            return tmp
        return []

    @property
    def path(self):
        """
        The path to the current `ArgParseNode` as `/` seperated list of strings that consist
        of each of the :py:attr:`ArgParseNode.name` values of the nodes (except for the root).
        """
        return "/".join(self.path_list)

    @classmethod
    def get_selected_path_list(cls, parse_result):
        """
        This method returns the path to the selected node as a list of name strings.

        :param argparse.Namespace parse_result: A namespace object returned by
            :py:meth:`argparse.ArgumentParser.parse_args`.
        :rtype: list
        """
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
        """
        This method returns the path to the selected node as a `/` seperated string.

        :param argparse.Namespace parse_result: A namespace object returned by
            :py:meth:`argparse.ArgumentParser.parse_args`.
        :rtype: str
        """
        path_list = cls.get_selected_path_list(parse_result)
        return "/".join(path_list)

    def get_selected_node(self, parse_result):
        """
        This method returns the selected node.

        :param argparse.Namespace parse_result: A namespace object returned by
            :py:meth:`argparse.ArgumentParser.parse_args`.
        :rtype: ArgParseNode
        """
        if self is not self.root: return self.root.get_selected_node(parse_result)
        selected_path_list = self.get_selected_path_list(parse_result)
        if not selected_path_list: return self
        selected_node = self
        for part in selected_path_list:
            selected_node = selected_node.get(part, None, True)
        return selected_node
