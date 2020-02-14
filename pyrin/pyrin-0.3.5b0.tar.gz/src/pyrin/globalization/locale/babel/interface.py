# -*- coding: utf-8 -*-
"""
locale babel interface module.
"""

from pyrin.cli.interface import CLIHandlerBase, CLIHandlerOptionsMetadata


class BabelCLIHandlerBase(CLIHandlerBase):
    """
    babel cli handler base class.
    all babel cli handlers must be subclassed from this.
    """

    def __init__(self, name):
        """
        initializes an instance of BabelCLIHandlerBase.

        :param str name: the handler name that should be registered
                         with. this name must be the exact name that
                         this handler must emmit to cli.
        """

        super().__init__(name)

    def _inject_common_cli_options(self, commands):
        """
        injecting some common cli options into the given list.

        :param list commands: a list of all commands and their
                              values to be sent to cli command.
        """

        bounded_options = ['pybabel']
        for i in range(len(bounded_options)):
            commands.insert(i, bounded_options[i])

    def _generate_common_cli_handler_options_metadata(self):
        """
        generates common cli handler options metadata.

        :rtype: list[CLIHandlerOptionsMetadata]
        """

        help_option = CLIHandlerOptionsMetadata('help', None, {True: '--help', False: None})
        output_file = CLIHandlerOptionsMetadata('output_file', '--output-file')

        options = [help_option, output_file]

        return options
