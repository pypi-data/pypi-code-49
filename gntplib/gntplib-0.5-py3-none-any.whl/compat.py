"""This module makes gntplib compatible with Python 2 and 3."""

import sys


if sys.version_info[0] == 3:
    text_type = str
else:
    text_type = unicode
