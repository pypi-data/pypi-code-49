import logging

from code_instrumentation import add_logging_level
logging.getLogger(__name__).addHandler(logging.NullHandler())
__all__ = ['Timer']

__author__  = "c. Sooriyakumaran <Christopher@aiolos.com>"
__status__  = "development"
__version__ = "0.2.7"
__date__    = "October 2019"
