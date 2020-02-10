"""
Plugin that allows you to append user information to log messages
"""
import pwd
import os
import ctl
from ctl import plugin
from ctl.plugins.log import LogPlugin


@ctl.plugin.register("log_user")
class LogUserPlugin(LogPlugin):

    """
    append user information to log messages

    # Instanced Attributes

    - username (`str`): username
    """

    def init(self):
        super(LogUserPlugin, self).init()
        self.username = pwd.getpwuid(os.getuid()).pw_name

    def apply(self, message):
        """
        Augment log message with user information

        **Arguments**

        - message (`str`): log message

        **Returns**

        Augmented log message (`str`)
        """

        prefix = "{who}".format(who=self.username)
        return "{prefix} - {message}".format(prefix=prefix, message=message)
