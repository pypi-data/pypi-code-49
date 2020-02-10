"""
Plugin that allows you to manage a python virtual env

## Requirements

- `pipenv`
- `pipenv-setup` if you want to run the `sync_setup` operation

"""
from __future__ import absolute_import, division, print_function

import os
import sys
import argparse
import re

import ctl
import ctl.config
import subprocess
import select
import confu.schema

from ctl.auth import expose
from ctl.plugins import command
from ctl.exceptions import UsageError
from ctl.docs import pymdgen_confu_types

try:
    import pipenv_setup
except ImportError:
    pipenv_setup = None


@pymdgen_confu_types()
class VenvPluginConfig(confu.schema.Schema):
    """
    Configuration schema for `VenvPlugin`
    """

    python_version = confu.schema.Str(choices=["2.7", "3.4", "3.5", "3.6", "3.7"])
    pipfile = confu.schema.Str(help="path to Pipfile", default="{{ctx.home}}/Pipfile")


@ctl.plugin.register("venv")
class VenvPlugin(command.CommandPlugin):

    """
    manage a virtual python envinronment

    # Instanced Attributes

    - binpath (`str`): path to venv `bin/` directory

    """

    class ConfigSchema(ctl.plugins.PluginBase.ConfigSchema):
        config = VenvPluginConfig()

    description = "manage a virtualenv using venv"

    @classmethod
    def add_arguments(cls, parser, plugin_config, confu_cli_args):
        install_parser = argparse.ArgumentParser(add_help=False)
        group = install_parser.add_mutually_exclusive_group(required=False)
        group.add_argument("output", nargs="?", type=str, help="venv location")

        # subparser that routes operation
        sub = parser.add_subparsers(title="Operation", dest="op")

        op_build_parser = sub.add_parser(
            "build", help="build virtualenv", parents=[install_parser]
        )

        op_sync_parser = sub.add_parser(
            "sync",
            help="sync virtualenv using pipenv, "
            "will build venv first if it does not exist",
            parents=[install_parser],
        )

        op_copy_parser = sub.add_parser("copy", help="copy virtualenv")
        op_copy_parser.add_argument(
            "source", nargs="?", type=str, help="venv source location"
        )
        op_copy_parser.add_argument(
            "output", nargs="?", type=str, help="venv output location"
        )

        op_sync_setup_parser = sub.add_parser(
            "sync_setup", help="sync setup.py from Pipfile"
        )
        op_sync_setup_parser.add_argument(
            "setup_file",
            nargs="?",
            default=".",
            type=str,
            help="location of the setup.py file you want to sync",
        )
        op_sync_setup_parser.add_argument(
            "--dry", action="store_true", help="Do a dry run"
        )

    def venv_exists(self, path=None):
        """
        Does a valid virtual environment exist at location?

        If no location is supplied the path in `self.output` is checked

        **Keyword Arguments**

        - path (`str`): path to check (should be virtuelenv root directory)

        **Returns**

        `True` if venv exists, `False` if not
        """

        return os.path.exists(os.path.join(path or self.output, "bin", "activate"))

    def venv_validate(self, path=None):
        """
        Validate virtualenv at location

        If no location is supplied the path in `self.output` is checked

        Will raise a `UsageError` on validation failure

        **Keyword Arguments**

        - path (`str`): path to check (should be virtuelenv root directory)
        """

        if not self.venv_exists(path):
            raise UsageError("No virtualenv found at {}".format(path or self.output))

    def execute(self, **kwargs):

        self.kwargs = kwargs

        python_version = self.get_config("python_version")
        pipfile = self.get_config("pipfile")

        self.python_version = self.render_tmpl(python_version)
        self.pipfile = self.render_tmpl(pipfile)

        output = self.get_config("output") or ""

        self.log.info("Pipfile: {}".format(self.pipfile))

        self.output = os.path.abspath(self.render_tmpl(output))
        self.binpath = os.path.join(os.path.dirname(__file__), "..", "bin")

        self.prepare()
        self.shell = True

        op = self.get_op(kwargs.get("op"))
        op(**kwargs)

    @expose("ctl.{plugin_name}.build")
    def build(self, **kwargs):
        """
        build a fresh virtualenv
        """
        command = ["ctl_venv_build {} {}".format(self.output, self.python_version)]
        self._run_commands(command, **kwargs)

    @expose("ctl.{plugin_name}.sync")
    def sync(self, **kwargs):
        """
        sync a virtualenv using pipenv

        will build a fresh virtualenv if it doesnt exist yet
        """
        if not self.venv_exists():
            self.build(**kwargs)
        command = ["ctl_venv_sync {} {}".format(self.output, self.pipfile)]
        self._run_commands(command, **kwargs)

    @expose("ctl.{plugin_name}.copy")
    def copy(self, source, **kwargs):
        """
        copy virtualenv to new location
        """
        source = os.path.abspath(self.render_tmpl(source))
        self.venv_validate(source)

        command = ["ctl_venv_copy {} {}".format(source, self.output)]

        self._run_commands(command, **kwargs)

    @expose("ctl.{plugin_name}.sync_setup")
    def sync_setup(self, setup_file=".", dry=False, **kwargs):
        """
        Syncs setup.py requirements from Pipfile

        **Keyword Arguments**

        - setup_file (`str`): path to `setup.py` file. If not specified
          will check in `.` instead
        - dry (`bool`=`False`): if `True` do a dry run and report what
          updates would be done to `setup.py`
        """

        if not pipenv_setup:
            raise UsageError(
                "Please install `pipenv-setup` to be able to use this command"
            )

        if dry:
            sub_command = "check"
        else:
            sub_command = "sync"

        with self.cwd_ctx(os.path.dirname(setup_file) or "."):
            command = ["pipenv-setup {}".format(sub_command)]
            self._run_commands(command, **kwargs)
