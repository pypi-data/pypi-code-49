from .APOinputclasses import Sky, Instrument, Observation, InterpolationMultiplier

import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, 'data', path)


print(get_data('apo3_5/Arctic'))
