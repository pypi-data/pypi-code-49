
from .cache import *

from .types import *
from .tools import *
from .access import *
from .helpers import *
from .utils import *

from . import updates


__all__ = (*cache.__all__, *types.__all__, *tools.__all__, *access.__all__,
           *helpers.__all__, *utils.__all__, 'update', 'missing')


def update(value, data, **kwargs):

    """
    Update the value with new data.
    """

    return updates.any(value, data, **kwargs)


missing = types.missing
