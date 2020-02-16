"""queue_utilities - utility functions for a better queue experience
  @jaycosaur / https://github.com/jaycosaur/queue-utilities
"""

name = "queue_utilities"

from .select import Select
from .multiplex import Multiplex
from .multicast import Multicast
from .pipe import Pipe
from .ticker import Ticker
from .timer import Timer

__version__ = "0.0.4"
