"""
Controller that handles the base command, mpaas.\n
All other commands are nested inside this controller.\n
Handles commands such as:\n

- Use\n
- Download
"""

from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version

VERSION_BANNER = """
CLI for helm chart customization and deployment %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    """
    Child class of Controller class.
    """
    class Meta:
        """
        Meta class attributes.
        base represents base 'mpaas' command.
        """
        label = 'base'

        # text displayed at the top of --help output
        description = 'CLI for helm chart customization and deployment'

        # text displayed at the bottom of --help output
        epilog = 'Usage: kompaas command1 --foo bar'

        usage = 'kompaas [SUB-COMMANDS]'

        # controller level arguments. ex: 'mpaas --version'
        arguments = [
            # add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()
    @ex(
        help="Show current context."
    )
    def context(self):
        """
        Prints current context.
        """
        data = {'context': self.app.ch.get_context_all()}

        self.app.render(data, 'context.jinja2')
