"""
A module for internationalization (i18n) utilities.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""


def n_(message):
    """Returns its input unchanged.

    A transparent function for gettext language translation to protect members
    of data structures from translation before they are presented to a user.
    """
    return message
