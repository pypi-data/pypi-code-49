import sys
import typing
from . import types
from . import ops
from . import app
from . import utils
from . import path
from . import props
from . import context

context: 'types.Context' = None

data: 'types.BlendData' = None
'''Access to Blenders internal data '''
