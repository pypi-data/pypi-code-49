"""Everything required to print the UI for the user

:copyright: Copyright 2019 Edward Armitage.
:license: MIT, see LICENSE for details.
"""
import sys
from textwrap import indent

from colorama import init, Fore, Style


class ConsoleWriter:
    """Class for grouping UI functionality"""

    def __init__(self, silent_mode: bool) -> None:
        """
        :param silent_mode: When True, status() and action() are effectively
                no-op methods.
        """
        init(autoreset=True)
        self._silent_mode = silent_mode

    @staticmethod
    def fatal(error_code: int, msg: str) -> None:
        """Prints an error message, and exits with the provided error code

        :param error_code: The error code to use when exiting
        :param msg: The error message to be shown
        """
        print(Fore.RED + "❌ A fatal error occurred:", file=sys.stderr)
        print(indent(Fore.RED + msg, "    "), file=sys.stderr)
        print(Fore.RED + "Exiting" + Style.RESET_ALL, file=sys.stderr)
        sys.exit(error_code)

    def status(self, msg: str) -> None:
        """Prints a message indicating the current status

        :param msg: The message to be printed
        """
        if not self._silent_mode:
            print(Fore.YELLOW + msg)

    def action(self, msg: str) -> None:
        """Prints a message showing an action that is being performed

        :param msg: The message to be printed
        """
        if not self._silent_mode:
            print(Fore.GREEN + msg)
