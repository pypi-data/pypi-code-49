"""
mambaex http server library
~~~~~~~~~~~~~~~~~~~~~
Mambaex is an HTTP server library, written in Python, for creating a simplified
webservice in ease manner.
Basic GET usage:
   >>> import mambaex
   >>> r = mambaex.getServer('<nameOfServer>')

The other methods are supported - see `mambaex.api`. Full documentation
is at <https://mambaex.readthedocs.io>.

:copyright: (c) 2020 by Prashant Farkya.
:license: MIT License, see LICENSE for more details.
"""


from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __build__, __author__, __author_email__, __license__
from .__version__ import __copyright__, __cake__

from .api import getServer
