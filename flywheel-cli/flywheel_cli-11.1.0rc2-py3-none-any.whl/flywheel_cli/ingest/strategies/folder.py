"""Provides FolderImporter class."""

import re

from pydantic import Field

from ..config import BaseIngestConfig
from ..template import StringMatchNode
from .abstract import AbstractIngestStrategy


class FolderIngestStrategyConfig(BaseIngestConfig):
    """Config class for folder import strategy"""
    strategy_type: str = Field("folder", const=True, argparse_opts={
        "skip": True,
    })

    group: str = Field(None, argparse_opts={
        "flags": ["-g", "--group"],
        "metavar": "<id>",
        "help": "The id of the group, if not in folder structure",
    })
    project: str = Field(None, argparse_opts={
        "flags": ["-p", "--project"],
        "metavar": "<label>",
        "help": "The label of the project, if not in folder structure",
    })
    dicom: str = Field("dicom", argparse_opts={
        "mutually_exclusive_group": "acq",
        "metavar": "<name>",
        "help": "The name of dicom subfolders to be zipped prior to upload",
    })
    pack_acquisitions: str = Field(None, argparse_opts={
        "mutually_exclusive_group": "acq",
        "metavar": "<type>",
        "help": "Acquisition folders only contain acquisitions of <type> and are zipped prior to upload",
    })
    root_dirs: int = Field(0, argparse_opts={
        "help": "The number of directories to discard before matching"
    })


class FolderIngestStrategy(AbstractIngestStrategy):
    """Ingest strategy to import a folder hierarchy"""
    help_text = "Ingest a folder"
    config_cls = FolderIngestStrategyConfig

    def initialize(self):
        """Initialize the strategy."""
        for _ in range(self.config.root_dirs):
            self.add_template_node(StringMatchNode(re.compile(".*")))

        if not self.config.group:
            self.add_template_node(StringMatchNode("group"))

        if not self.config.project:
            self.add_template_node(StringMatchNode("project"))

        if not self.config.no_subjects:
            self.add_template_node(StringMatchNode("subject"))

        if not self.config.no_sessions:
            self.add_template_node(StringMatchNode("session"))

        if self.config.pack_acquisitions:
            self.add_template_node(StringMatchNode('acquisition', packfile_type=self.config.pack_acquisitions))
        else:
            self.add_template_node(StringMatchNode('acquisition'))
            self.add_template_node(StringMatchNode(re.compile(self.config.dicom), packfile_type='dicom'))
