"""Provides TemplateIngestStrategy class."""
import re
from typing import Union, List

from pydantic import Field

from ..config import BaseIngestConfig
from ..template import parse_template_list, parse_template_string
from .abstract import AbstractIngestStrategy


class TemplateIngestStrategyConfig(BaseIngestConfig):
    """Template ingest strategy"""
    strategy_type: str = Field("template", argparse_opts={
        "skip": True,
    })
    template: Union[str, List] = Field(..., argparse_opts={
        "positional": True,
        "nargs": "?",
        "help": "The template string",
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

class TemplateIngestStrategy(AbstractIngestStrategy):
    """Ingest strategy class to import hierarchy by a given template."""
    help_text = "Ingest a folder using a template"
    config_cls = TemplateIngestStrategyConfig

    def initialize(self):
        """Initialize the strategy."""
        if not self.config.template:
            raise ValueError('Template must be specified, either with --template argument or in the config file')
        if isinstance(self.config.template, str):
            # Build the template string
            try:
                self.root_node = parse_template_string(self.config)
            except (ValueError, re.error) as exc:
                raise ValueError(f'Invalid template: {exc}')
        else:
            self.root_node = parse_template_list(self.config)

        self.check_group_reference()

    def check_group_reference(self):
        """Check if template or config.group refer to group id"""
        if not self.config.group:
            node = self.root_node
            while node:
                if hasattr(node, 'template') and 'group' in node.template.pattern:
                    break
                node = getattr(node, 'next_node', None)
            else:
                raise ValueError('Group must be specified either in the template or using -g')
