from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import super
from builtins import str
from future import standard_library
standard_library.install_aliases()
try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence
from typing import Any
from typing import Dict
from typing import List

from gcloud.rest.datastore import value


# https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/runQuery#ArrayValue
class Array(Sequence):
    def __init__(self, items           )        :
        super(Sequence, self).__init__()  # pylint: disable=bad-super-call
        self.items = items

    def __eq__(self, other     )        :
        if not isinstance(other, Array):
            return False
        return self.items == other.items

    def __repr__(self)       :
        return str(self.to_repr())

    def __getitem__(self, index     )       :
        return self.items[index]

    def __len__(self)       :
        return len(self.items)

    @classmethod
    def from_repr(cls, data                )           :
        return cls([value.Value.from_repr(x) for x in data['values']])

    def to_repr(self)                  :
        return {'values': [x.to_repr() for x in self]}
