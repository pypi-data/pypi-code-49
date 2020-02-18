"""Provides TemplateImporter class."""
import re

from ..exceptions import TemplateImporterError
from ..template import parse_template_list, parse_template_string
from .abstract_importer import AbstractImporter


class TemplateImporter(AbstractImporter):
    """Importer class to import hierarchy by a given template."""
    help_text = "Template importer"

    def initialize(self):
        """Initialize the importer."""
        if not self.config.template:
            raise TemplateImporterError('Template must be specified, either with --template argument or in the config file')
        if isinstance(self.config.template, str):
            # Build the template string
            try:
                self.root_node = parse_template_string(self.config)
            except (ValueError, re.error) as exc:
                raise TemplateImporterError(f'Invalid template: {exc}')
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
                raise TemplateImporterError('Group must be specified either in the template or using -g')
