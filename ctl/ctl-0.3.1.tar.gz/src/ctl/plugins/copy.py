"""
A plugin that allows you to copy files
"""

from __future__ import absolute_import

import os
import shutil
import re

import confu.schema
import ctl

from ctl.plugins.walk_dir import WalkDirPlugin, WalkDirPluginConfig
from ctl.docs import pymdgen_confu_types


@pymdgen_confu_types()
class CopyPluginConfig(WalkDirPluginConfig):
    copy_metadata = confu.schema.Bool(
        "copy_metadata", default=True, help="Copy file metadata"
    )


@ctl.plugin.register("copy")
class CopyPlugin(WalkDirPlugin):

    """
    copy files
    """

    class ConfigSchema(ctl.plugins.PluginBase.ConfigSchema):
        config = CopyPluginConfig("config")

    def prepare(self):
        """
        Prepare plugin for execution

        *overrides and calls `WalkDirPlugin.prepare`*
        """

        super(CopyPlugin, self).prepare()
        self.requires_output = True
        self.debug_info["copied"] = []
        self.copy_metadata = self.get_config("copy_metadata")

    def process_file(self, path, dirpath):
        """
        Process file - automatically calls `copy_file`

        *overrides and calls `WalkDirPlugin.process_file`*
        """

        r = self.copy_file(path, dirpath)
        super(CopyPlugin, self).process_file(path, dirpath)
        return r

    def copy_file(self, path, dirpath):
        """
        Copy file

        **Arguments**

        - path (`str`): relative filepath being processed
        - dirpath (`str`): relative dirpath being processed
        """
        output_dir = os.path.dirname(self.output(path))
        self.log.info(self.output(path))

        self.debug_append("copied", self.output(path))

        if self.copy_metadata:
            shutil.copy2(self.source(path), self.output(path))
        else:
            shutil.copy(self.source(path), self.output(path))
