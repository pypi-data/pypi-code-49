"""
Change log:

    since version number will increment automatically using bumpversion, even if 
    nothing in this package changes, not all version numbers will be present in 
    the below table


    Version             Date                Description             Contributer
    -------             ----                -----------             -----------
    0.0.2               02.2020             initial relase          c.sooriyakumaran 



"""
import logging

from aiolos_code_instrumentation import add_logging_level
logging.getLogger(__name__).addHandler(logging.NullHandler())
__all__ = ['Timer']

__author__  = "c. Sooriyakumaran <Christopher@aiolos.com>"
__status__  = "development"
__version__ = "0.0.2"
__date__    = "October 2019"


